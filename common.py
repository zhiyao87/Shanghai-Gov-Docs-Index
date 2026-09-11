# -*- coding: utf-8 -*-
"""公共抓取工具：零第三方依赖（仅标准库）。

设计要点
--------
1. 代理可选：默认走环境变量 ``SH_GOV_PROXY`` / ``HTTPS_PROXY`` / ``HTTP_PROXY``，
   没有就用直连。本仓库是公开的，绝不硬编码任何内网代理地址。
2. URL 编码：``urllib`` 不会自动对含中文/空格的 URL 做 percent-encoding（浏览器和
   curl 会），不处理会直接抛 ``UnicodeEncodeError``。统一走 ``encode_url()``。
3. 重试：政府站点偶发抖动，默认重试 3 次、指数退避。
"""

import gzip
import os
import re
import ssl
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import zlib

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124.0 Safari/537.36")

PROXY = (os.environ.get("SH_GOV_PROXY")
         or os.environ.get("https_proxy") or os.environ.get("HTTPS_PROXY")
         or os.environ.get("http_proxy") or os.environ.get("HTTP_PROXY")
         or None)

_SSL_CTX = ssl.create_default_context()
_SSL_CTX.check_hostname = False
_SSL_CTX.verify_mode = ssl.CERT_NONE


def encode_url(url):
    """对 URL 做 percent-encoding，保留已有 % 以免二次编码。"""
    return urllib.parse.quote(url, safe=":/?#[]@!$&'*+,;=%~.-_")


def _opener():
    handlers = [urllib.request.HTTPSHandler(context=_SSL_CTX)]
    if PROXY:
        handlers.append(urllib.request.ProxyHandler({"http": PROXY, "https": PROXY}))
    else:
        handlers.append(urllib.request.ProxyHandler({}))  # 显式禁用环境代理
    return urllib.request.build_opener(*handlers)


def fetch(url, data=None, headers=None, timeout=40, retries=3, encoding="utf-8"):
    """抓取 URL，返回 (status, bytes)。

    失败时 status 为 0，bytes 为错误信息。自动解 gzip/deflate。
    """
    safe = encode_url(url)
    hdrs = {"User-Agent": UA, "Accept-Language": "zh-CN,zh;q=0.9",
            "Accept-Encoding": "gzip, deflate"}
    if headers:
        hdrs.update(headers)
    last = ""
    for attempt in range(retries):
        try:
            req = urllib.request.Request(safe, data=data, headers=hdrs)
            with _opener().open(req, timeout=timeout) as resp:
                raw = resp.read()
                enc = (resp.headers.get("Content-Encoding") or "").lower()
                if "gzip" in enc:
                    raw = gzip.decompress(raw)
                elif "deflate" in enc:
                    try:
                        raw = zlib.decompress(raw)
                    except zlib.error:
                        raw = zlib.decompress(raw, -zlib.MAX_WBITS)
                return resp.status, raw
        except urllib.error.HTTPError as e:
            body = b""
            try:
                body = e.read()
            except Exception:
                pass
            if e.code in (403, 429, 503) and attempt < retries - 1:
                last = "HTTP %s" % e.code
                time.sleep(1.5 * (attempt + 1))
                continue
            return e.code, body
        except Exception as e:  # noqa: BLE001 网络/SSL/超时统一重试
            last = "%s: %s" % (type(e).__name__, e)
            time.sleep(1.5 * (attempt + 1))
    return 0, last.encode("utf-8")


def fetch_text(url, **kw):
    """抓取并解码为文本；失败返回空串。"""
    code, raw = fetch(url, **kw)
    if code != 200:
        return ""
    for enc in (kw.get("encoding", "utf-8"), "gb18030", "utf-8-sig"):
        try:
            return raw.decode(enc)
        except UnicodeDecodeError:
            continue
    return raw.decode("utf-8", errors="replace")


def post_json(url, payload, headers=None, **kw):
    """POST JSON。"""
    import json as _json
    body = _json.dumps(payload, ensure_ascii=False).encode("utf-8")
    hdrs = {"Content-Type": "application/json;charset=UTF-8"}
    if headers:
        hdrs.update(headers)
    code, raw = fetch(url, data=body, headers=hdrs, **kw)
    if code != 200:
        return None
    try:
        return _json.loads(raw.decode("utf-8"))
    except Exception:
        return None


# ---------------------------------------------------------------- HTML 转文本

_TAG = re.compile(r"<[^>]+>")
_SCRIPT = re.compile(r"<(script|style)\b.*?</\1>", re.S | re.I)
_BR = re.compile(r"<(?:br|/p|/div|/tr|/h[1-6]|/li)\s*/?>", re.I)


def html_to_text(html):
    """粗暴但可靠的 HTML → 纯文本（政府站页面结构简单，够用）。"""
    import html as _html
    if not html:
        return ""
    t = _SCRIPT.sub(" ", html)
    t = re.sub(r"<!--.*?-->", " ", t, flags=re.S)
    t = _BR.sub("\n", t)
    t = _TAG.sub("", t)
    t = _html.unescape(t)
    t = t.replace("\u00a0", " ").replace("\u3000", "　")
    lines = [ln.strip() for ln in t.split("\n")]
    out, blank = [], 0
    for ln in lines:
        if not ln:
            blank += 1
            if blank > 1:
                continue
        else:
            blank = 0
        out.append(ln)
    return "\n".join(out).strip()


def log(*a):
    print(*a, file=sys.stderr if False else sys.stdout, flush=True)
