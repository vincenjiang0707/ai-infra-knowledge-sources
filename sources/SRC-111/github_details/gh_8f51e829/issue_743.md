# [Issue #743] Streaming error responses are not recognized as errors

source: https://github.com/vllm-project/guidellm/issues/743
state: closed | updated: 2026-06-18T14:44:15Z
labels: 

## 正文

### Bug Description

When the backend server returns an error via streaming SSE messages (HTTP 200 with `data: {"error": {...}}` followed by `data: [DONE]`), guidellm treats the generation as successful rather than failed. This happens because the initial HTTP connection succeeds (status 200), and the error is only conveyed through the stream body — which guidellm does not inspect for error payloads.

Services like vLLM use this pattern (e.g., `create_streaming_error_response`) to report errors mid-stream after the connection is already established. A typical error stream looks like:

```
data: {"error": {"message": "TimeoutError", "type": "GatewayTimeout", "code": 504}}

data: [DONE]
```

Because guidellm ignores the error payload, the reported metrics are misleading:
- **TTFT** and **ITL** are reported as `0` (no actual content was streamed)
- **Token counts** show the expected/requested numbers rather than actual output
- **Words** and **characters** are reported as `0`

### Expected Behavior

Streaming responses that contain an `"error"` key should be recognized as failures. The generation should be marked as errored/aborted, and metrics (TTFT, ITL, token counts) should reflect that no valid output was produced.

A more robust approach would follow vLLM's `ErrorResponse` / `ErrorInfo` schema to parse and surface the error details (message, type, code, param) to the caller.

**Error vs. incomplete**: One point worth discussion is whether a streaming error response should be classified as an error or as an incomplete request. From the HTTP perspective, the connection succeeded (status 200), but the stream body conveys an error. Treating it as an explicit error may be most natural when the error is the first (and only) streaming message. However, classifying it as incomplete has an advantage in cases where the server successfully generated part of the response before the error occurred — the already-streamed tokens could still be recorded rather than discarded entirely.

### Steps to Reproduce

1. Configure guidellm to use an OpenAI-compatible backend that returns streaming errors (e.g., vLLM with a gateway timeout)
2. Submit a generation request that causes a server-side timeout or other error after the stream begins
3. Observe that guidellm reports the request as successful with zero words/characters but non-zero token counts

### Operating System

Ubuntu 24.04

### Python Version

Python 3.12.3

### GuideLLM Version

0.6.0

### Installation Method

pip install guidellm[recommended]

### Installation Details

_No response_

### Error Messages or Stack Traces

```shell

```

### Additional Context

**vLLM reference:** vLLM defines its streaming error response format as:

```python
class ErrorInfo(OpenAIBaseModel):
    message: str
    type: str
    param: str | None = None
    code: int

class ErrorResponse(OpenAIBaseModel):
    error: ErrorInfo
```

And serializes it via `create_streaming_error_response()` which produces a JSON line with the structure `{"error": {"message": "...", "type": "...", "code": ...}}`.

**Temporary workaround**:

```diff
diff --git a/src/guidellm/backends/openai/request_handlers.py b/src/guidellm/backends/openai/request_handlers.py
index b6e9780..68e0f0b 100644
--- a/src/guidellm/backends/openai/request_handlers.py
+++ b/src/guidellm/backends/openai/request_handlers.py
@@ -10,6 +10,7 @@ extract usage metrics, and convert results into standardized GenerationResponse.
 
 from __future__ import annotations
 
+import asyncio
 import base64
 from typing import Any, Protocol, cast
 
@@ -563,6 +564,9 @@ class ChatCompletionsRequestHandler(TextCompletionsRequestHandler):
         if not (data := self.extract_line_data(line)):
             return None if data is None else 0
 
+        if "error" in data:
+            raise asyncio.CancelledError
+
         if "id" in data and self.streaming_response_id is None:
             self.streaming_response_id = data["id"]
```

## 评论 (1)

### sjmonson · 2026-05-26

Can you retest this from main? We landed a fix recently (in #712) to check status on each streaming response and in our testing that catches this error.
