# [Issue #2578] Gateway double-wraps upstream error responses from vLLM/SGLang

source: https://github.com/vllm-project/aibrix/issues/2578
state: closed | updated: 2026-08-22T16:13:07Z
labels: 

## 正文

### 🐛 Describe the bug

When a request routed through the AIBrix gateway hits an upstream engine (vLLM / SGLang) that returns a non-200 status with a error body, the gateway re-wraps the entire upstream body as a plain string inside a freshly constructed error object. The result is a double-nested error that loses the upstream `type`, `param`, and `code` fields.

For example, upstream (vLLM / SGLang) returns:

```json
{
  "error": {
    "message": "top_p must be in (0, 1], got 2.0. (parameter=top_p, value=2.0)",
    "type": "BadRequestError",
    "param": "top_p",
    "code": 400
  }
}
```



But a client hitting the AIBrix gateway receives:

```json
{
  "error": {
    "code": null,
    "param": null,
    "message": "{\"error\":{\"message\":\"top_p must be in (0, 1], got 2.0. (parameter=top_p, value=2.0)\",\"type\":\"BadRequestError\",\"param\":\"top_p\",\"code\":400}}",
    "type": "invalid_request_error"
  }
}
```



The original `message`/`type`/`param`/`code` fields are embedded as an escaped JSON string inside `error.message`, while `error.code`/`error.param` are set to `null` and `error.type` is replaced with a status-code-derived generic value (`invalid_request_error`).

### Steps to Reproduce

1. Deploy AIBrix gateway routing to a vLLM or SGLang backend.
2. Send a request with an invalid sampling parameter, e.g.:

```bash
curl http://<aibrix-gateway>/v1/chat/completions \
  -H 'Content-Type: application/json' \
  -d '{
        "model": "<model>",
        "messages": [{"role": "user", "content": "hi"}],
        "top_p": 2.0
      }'
```

Observe the response: the upstream error body is double-nested inside `error.message` as a string, and `error.code`/`error.param` are `null`.

### Expected behavior

The client should receive the upstream error essentially as-is (preserving `message`, `type`, `param`, `code`), e.g.:

```json
{
  "error": {
    "message": "top_p must be in (0, 1], got 2.0. (parameter=top_p, value=2.0)",
    "type": "BadRequestError",
    "param": "top_p",
    "code": 400
  }
}
```

### Environment

- AIBrix version: 0.7.0
- Deployment environment: Kubernetes
- LLM(s): vLLM and/or SGLang
- Client library: OpenAI SDK / curl

## 评论 (5)

### googs1025 · 2026-08-19

This looks valid to me. The gateway appears to be treating the downstream error response body as a plain string and wrapping it again, instead of recognizing that vLLM/SGLang already returned an OpenAI-compatible `{"error": {...}}` object.

### Yang1032 · 2026-08-19

Got it. I’ll take a look and work on fixing this.

### Yang1032 · 2026-08-19

Hi @googs1025 @varungup90 ,

I ran into two inconsistencies and would like your input before finalizing the fix.

### 1. Upstream engines return errors in two different shapes

Some engines return the **nested** shape:

```json
{
  "error": {
    "message": "top_p must be in (0, 1], got 2.0.",
    "type": "BadRequestError",
    "param": "top_p",
    "code": 400
  }
}
```



Others return a **flat** shape (fields at top level):

```json
{
  "object": "error",
  "message": "max_new_tokens must be at least 0, got -1.",
  "type": "BadRequestError",
  "param": null,
  "code": 400
}
```

**Proposal:** normalize both to the **nested** format in the gateway (reshape the flat envelope into `{"error":{...}}`), so every upstream error a client sees has a single consistent shape.

### 2. `code` field semantics differ between upstream and aibrix's own errors

Upstream engines set `code` to an **integer HTTP status** (e.g. `400`). aibrix's own error responses use a **string** code (e.g. `"invalid_api_key"`), and in most cases `code` is `null`:

```json
{
  "error": {
    "code": null,
    "param": null,
    "message": "error processing request body",
    "type": "invalid_request_error"
  }
}
```

```json
{
  "error": {
    "code": "invalid_api_key",
    "param": null,
    "message": "Incorrect API key provided",
    "type": "authentication_error"
  }
}
```

**Proposal:** align aibrix's local error responses with the upstream convention so the `code` field has a consistent type across all errors (e.g. always emit an integer HTTP status in `code`).

Are these two proposals appropriate? Happy to implement either direction once confirmed.


### varungup90 · 2026-08-20

Thanks for digging into this, @Yang1032 — both good catches.

**1. Nested vs. flat upstream shapes**
Agreed, normalize to the nested `{"error": {...}}` form in the gateway. That's the shape OpenAI-compatible clients (and the OpenAI SDK) expect, so reshaping the flat envelope on the way through keeps behavior consistent regardless of which engine served the request.

**2. `code` field type**
I'd like to narrow this one. I don't think we should change the type of AIBrix's own error codes (e.g., `"invalid_api_key"`) from string to int — those are semantic codes, not HTTP statuses, and retyping them would be a breaking change for anyone parsing `error.code` today.

What I'd propose instead: leave AIBrix-native errors as they are, and just make sure that when we pass through an upstream engine's error (which already carries an integer HTTP status in `code`), we preserve that integer as-is rather than dropping/nulling it. So the type of `code` would legitimately vary by error source (int for passthrough upstream errors, string for AIBrix-native ones) — that's fine as long as it's documented, rather than forcing one type everywhere.

---

**Regarding the underlying double-wrap bug itself:**
The root cause is in `processLanguageResponse` in `gateway_rsp_body.go` — when the response body doesn't unmarshal into a recognized `OpenAIResponse` (i.e., `res.Model` is empty), the raw upstream body is used verbatim as the `message` field and re-wrapped via `generateErrorMessage`, without first checking whether the body is already an `{"error": {...}}` object. The fix should detect that shape (e.g., via `gjson.GetBytes(finalBody, "error")`, since `gjson` is already used elsewhere in this file) and pass its `message`/`type`/`param`/`code` through directly, falling back to the current wrap-as-string behavior only for genuinely non-JSON upstream bodies.

**One more thing worth flagging while you're in there:**
The fallback message at line 310 is built from `b.ResponseBody.GetBody()` (just the current chunk) rather than the reassembled `finalBody` buffer. If an error body ever spans multiple response chunks, only the last chunk would end up in the message. It is probably worth fixing in the same pass since it's the same code path.

### Yang1032 · 2026-08-20

Thanks — agreed. Keeping AIBrix error codes as-is is fine, no problem there. 
I'll take care of the `processLanguageResponse` double-wrap plus the `finalBody` chunk issue you flagged. 
