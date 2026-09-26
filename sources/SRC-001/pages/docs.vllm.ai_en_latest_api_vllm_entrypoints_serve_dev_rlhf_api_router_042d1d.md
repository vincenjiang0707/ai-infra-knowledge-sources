source: https://docs.vllm.ai/en/latest/api/vllm/entrypoints/serve/dev/rlhf/api_router/
lastmod: 2026-09-24

#

`vllm.entrypoints.serve.dev.rlhf.api_router`

[¶](https://docs.vllm.ai#vllm.entrypoints.serve.dev.rlhf.api_router)

Functions:

-
–[abort_requests](https://docs.vllm.ai#vllm.entrypoints.serve.dev.rlhf.api_router.abort_requests)Abort in-flight requests without pausing the scheduler.

-
–[get_world_size](https://docs.vllm.ai#vllm.entrypoints.serve.dev.rlhf.api_router.get_world_size)Get the world size from the parallel config.

-
–[is_paused](https://docs.vllm.ai#vllm.entrypoints.serve.dev.rlhf.api_router.is_paused)Return the current pause status.

-
–[pause_generation](https://docs.vllm.ai#vllm.entrypoints.serve.dev.rlhf.api_router.pause_generation)Pause generation requests to allow weight updates.

-
–[resume_generation](https://docs.vllm.ai#vllm.entrypoints.serve.dev.rlhf.api_router.resume_generation)Resume generation after a pause.


##

`abort_requests(raw_request)`

`async`

[¶](https://docs.vllm.ai#vllm.entrypoints.serve.dev.rlhf.api_router.abort_requests)

Abort in-flight requests without pausing the scheduler.

Empty/missing `request_ids`

aborts all in-flight requests.

## Source code in `vllm/entrypoints/serve/dev/rlhf/api_router.py`


##

`get_world_size(raw_request, include_dp=Query(True))`

`async`

[¶](https://docs.vllm.ai#vllm.entrypoints.serve.dev.rlhf.api_router.get_world_size)

Get the world size from the parallel config.

Parameters:

-

(`raw_request`

[¶](https://docs.vllm.ai#vllm.entrypoints.serve.dev.rlhf.api_router.get_world_size(raw_request))`Request`

) –The incoming FastAPI request, used to reach the engine client on the app state.

-

(`include_dp`

[¶](https://docs.vllm.ai#vllm.entrypoints.serve.dev.rlhf.api_router.get_world_size(include_dp))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`Query(True)`

) –If True (default), returns the world size including data parallelism (TP * PP * DP). If False, returns the world size without data parallelism (TP * PP).


## Source code in `vllm/entrypoints/serve/dev/rlhf/api_router.py`


##

`is_paused(raw_request)`

`async`

[¶](https://docs.vllm.ai#vllm.entrypoints.serve.dev.rlhf.api_router.is_paused)

Return the current pause status.

## Source code in `vllm/entrypoints/serve/dev/rlhf/api_router.py`


##

`pause_generation(raw_request, mode='abort', wait_for_inflight_requests=Query(False), clear_cache=True)`

`async`

[¶](https://docs.vllm.ai#vllm.entrypoints.serve.dev.rlhf.api_router.pause_generation)

Pause generation requests to allow weight updates.

Parameters:

-

(`raw_request`

[¶](https://docs.vllm.ai#vllm.entrypoints.serve.dev.rlhf.api_router.pause_generation(raw_request))`Request`

) –The incoming FastAPI request, used to reach the engine client on the app state.

-

(`mode`

[¶](https://docs.vllm.ai#vllm.entrypoints.serve.dev.rlhf.api_router.pause_generation(mode))

, default:[Annotated](https://docs.python.org/3/library/typing.html#typing.Annotated)[PauseMode, Query()]`'abort'`

) –How to handle in-flight requests: -

`"abort"`

: Abort all in-flight requests immediately (default). -`"wait"`

: Wait for in-flight requests to complete. -`"keep"`

: Freeze requests in queue; they resume on /resume. -

(`wait_for_inflight_requests`

[¶](https://docs.vllm.ai#vllm.entrypoints.serve.dev.rlhf.api_router.pause_generation(wait_for_inflight_requests))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`Query(False)`

) –DEPRECATED. Use

`mode="wait"`

instead. -

(`clear_cache`

[¶](https://docs.vllm.ai#vllm.entrypoints.serve.dev.rlhf.api_router.pause_generation(clear_cache))

, default:[Annotated](https://docs.python.org/3/library/typing.html#typing.Annotated)[[bool](https://docs.python.org/3/builtins/functions.html#bool), Query()]`True`

) –DEPRECATED. Whether to clear KV/prefix caches after draining. Ignored when mode="keep".


## Source code in `vllm/entrypoints/serve/dev/rlhf/api_router.py`


##

`resume_generation(raw_request)`

`async`

[¶](https://docs.vllm.ai#vllm.entrypoints.serve.dev.rlhf.api_router.resume_generation)

Resume generation after a pause.