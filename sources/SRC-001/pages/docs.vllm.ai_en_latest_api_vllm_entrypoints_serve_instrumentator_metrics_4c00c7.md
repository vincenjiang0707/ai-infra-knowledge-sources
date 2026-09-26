source: https://docs.vllm.ai/en/latest/api/vllm/entrypoints/serve/instrumentator/metrics/
lastmod: 2026-09-24

#

`vllm.entrypoints.serve.instrumentator.metrics`

[¶](https://docs.vllm.ai#vllm.entrypoints.serve.instrumentator.metrics)

Functions:

-
–[attach_router](https://docs.vllm.ai#vllm.entrypoints.serve.instrumentator.metrics.attach_router)Mount prometheus metrics to a FastAPI app.


##

`_patch_instrumentator_route_walk()`

[¶](https://docs.vllm.ai#vllm.entrypoints.serve.instrumentator.metrics._patch_instrumentator_route_walk)

Make prometheus-fastapi-instrumentator's route walk tolerate routes without a `.path`

.

FastAPI >= 0.137 stores lazy `_IncludedRouter`

objects in `app.routes`

; these are `BaseRoute`

subclasses with no `.path`

attribute. The instrumentator's `_get_route_name`

(up to 8.0.0) reads `route.path`

unconditionally, so every request raises `AttributeError`

in the metrics middleware and the server returns 500 (e.g. `/health`

never goes ready). Skip path-less routes; this only affects the metric handler label, not request routing. Idempotent.

## Source code in `vllm/entrypoints/serve/instrumentator/metrics.py`


##

`attach_router(app)`

[¶](https://docs.vllm.ai#vllm.entrypoints.serve.instrumentator.metrics.attach_router)

Mount prometheus metrics to a FastAPI app.