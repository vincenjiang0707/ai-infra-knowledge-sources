source: https://docs.vllm.ai/en/latest/api/vllm/entrypoints/serve/elastic_ep/middleware/
lastmod: 2026-09-24

Middleware that checks if the model is currently scaling and returns a 503 Service Unavailable response if it is.

This middleware applies to all HTTP requests and prevents processing when the model is in a scaling state.

## Source code in `vllm/entrypoints/serve/elastic_ep/middleware.py`


| class ScalingMiddleware:
"""Middleware that checks if the model is currently scaling and
returns a 503 Service Unavailable response if it is.
This middleware applies to all HTTP requests and prevents
processing when the model is in a scaling state.
"""
def __init__(self, app: ASGIApp) -> None:
self.app = app
def __call__(self, scope: Scope, receive: Receive, send: Send) -> Awaitable[None]:
if scope["type"] != "http":
return self.app(scope, receive, send)
# Check global scaling state
if get_scaling_elastic_ep():
# Return 503 Service Unavailable response
response = JSONResponse(
content={
"error": "The model is currently scaling. Please try again later."
},
status_code=503,
)
return response(scope, receive, send)
return self.app(scope, receive, send)
|