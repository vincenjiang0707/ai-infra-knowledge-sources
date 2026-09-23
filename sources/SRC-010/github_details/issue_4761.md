# [Issue #4761] Unauthenticated SSRF via image_url in the OpenAI-compatible chat endpoint (redirect bypass of the private-IP guard)

source: https://github.com/InternLM/lmdeploy/issues/4761
state: open | updated: 2026-07-20T02:51:25Z
labels: 

## 正文

### Checklist

- [x] 1. I have searched related issues but cannot get the expected help.
- [x] 2. The bug has not been fixed in the latest version.
- [x] 3. Please note that if the bug-related issue you submitted lacks corresponding environment info and a minimal reproducible demo, it will be challenging for us to reproduce and resolve the issue, reducing the likelihood of receiving feedback.

### Describe the bug

reported https://github.com/InternLM/lmdeploy/security/advisories/GHSA-7rf4-7gg3-8vqx on 12 June 2026 - no response.



### Summary

The lmdeploy OpenAI-compatible API server fetches a multimodal `image_url` server-side. It has a private-IP guard (`_is_safe_url`) that resolves the host and rejects non-global addresses, but the guard runs only on the original URL; the HTTP client then follows redirects with no per-hop revalidation. An attacker-controlled public host that returns a 302 to an internal or cloud-metadata address is fetched, and its content is returned through the model pipeline. The API server binds `0.0.0.0` and runs without authentication by default, so any unauthenticated client of a vision-model deployment can reach internal services and metadata. Confirmed against the fetch code: a direct internal URL is blocked, but a redirect to the same internal target is followed and its bytes are returned.

### Details

`lmdeploy/vl/media/connection.py`:

```python
def _is_safe_url(url):           # ~line 25: resolves host via getaddrinfo, rejects non-global IPs
    ...
def _load_http_url(url):         # ~line 54
    session = requests.Session()
    session.max_redirects = 3
    if not _is_safe_url(url): raise ...     # ~line 56: validates ONLY the original URL
    resp = client.get(url, allow_redirects=True)   # ~line 68: follows redirects, no per-hop check
```

`requests` follows the `Location` of a 302 without re-running `_is_safe_url`, so an `http(s)://attacker/` URL whose host resolves to a global IP (passing the guard) can redirect to `http://127.0.0.1:.../` or `http://169.254.169.254/...`. Reached unauthenticated from `/v1/chat/completions`: a message `image_url.url` flows through `serve/openai/processors/multimodal.py` (~line 143) to `load_from_url` -> `_load_http_url`. Defaults (`serve/openai/api_server.py`): `server_name='0.0.0.0'` (~line 1445), `api_keys=None` (~line 1452), and the auth check is applied only when `api_keys is not None` (~line 1573).


### Reproduction


### PoC

The guard validates only the original URL, not redirect hops (`lmdeploy/vl/media/connection.py:56` validates the original; `:68` does `get(..., allow_redirects=True)`). Stand up an internal listener (e.g. `127.0.0.1:9000` serving a secret image) and a public redirector that returns `302 Location: http://127.0.0.1:9000/internal-secret`, then drive the functions:

```python
from lmdeploy.vl.media.connection import _is_safe_url, load_from_url
# control: a direct internal URL is blocked
print(_is_safe_url("http://127.0.0.1:9000/internal-secret"))   # (False, "Blocked non-global IP ...")
# bypass: a public host (resolves to a global IP, passes the guard) that 302-redirects internally
img = load_from_url("http://public.example:8080/start")        # client follows 302 -> 127.0.0.1:9000
# -> INTERNAL LISTENER HIT; the internal bytes are returned as an Image
```

Over HTTP (default `api_server.py`: `server_name` `0.0.0.0` at `:1445`, `api_keys` `None` at `:1452` = unauth): `POST /v1/chat/completions` with `image_url.url` set to the redirector reaches the internal target. Fix: `allow_redirects=False` and re-run `_is_safe_url` per `Location` (or pin the validated IP).

### Impact

An unauthenticated client of a vision-model lmdeploy server can coerce server-side requests to internal-only services and cloud instance-metadata endpoints by hosting a public URL that redirects there, bypassing the private-IP guard, and receive the response content through the image pipeline. This enables internal service access and cloud-metadata credential theft from the lmdeploy host on the default (0.0.0.0, no-auth) configuration.

### Remediation

Do not auto-follow redirects when fetching `image_url` (`allow_redirects=False`) and instead loop manually, re-running `_is_safe_url` on every `Location` and rejecting non-global resolutions; or pin the connection to the IP validated by `_is_safe_url` so a redirect cannot switch hosts. Also reject non-http(s) schemes (the `file://` loader has no containment) and consider requiring authentication by default.

### Environment

```Shell
Affected version: commit 648df3b
```

### Error traceback

```Shell

```

## 评论 (1)

### CUHKSZzxy · 2026-07-20

Hi, thanks for bringing this security issue to our attention. This will be resolved in

- https://github.com/InternLM/lmdeploy/pull/4734
