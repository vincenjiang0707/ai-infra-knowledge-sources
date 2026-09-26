source: https://docs.vllm.ai/en/latest/api/vllm/engine/protocol/
lastmod: 2026-09-24

#

`vllm.engine.protocol`

[¶](https://docs.vllm.ai#vllm.engine.protocol)

Classes:

-
–[EngineClient](https://docs.vllm.ai#vllm.engine.protocol.EngineClient)Protocol class for Clients to Engine.

-
–[StreamingInput](https://docs.vllm.ai#vllm.engine.protocol.StreamingInput)Input data for a streaming generation request.


##

`EngineClient`

[¶](https://docs.vllm.ai#vllm.engine.protocol.EngineClient)

Bases: [ABC](https://docs.python.org/3/library/abc.html#abc.ABC)

Protocol class for Clients to Engine.

Methods:

-
–[abort](https://docs.vllm.ai#vllm.engine.protocol.EngineClient.abort)Abort a request.

-
–[add_lora](https://docs.vllm.ai#vllm.engine.protocol.EngineClient.add_lora)Load a new LoRA adapter into the engine for future requests.

-
–[check_admission](https://docs.vllm.ai#vllm.engine.protocol.EngineClient.check_admission)Reject the request up front if it would exceed queue limits.

-
–[check_health](https://docs.vllm.ai#vllm.engine.protocol.EngineClient.check_health)Raise if unhealthy.

-
–[collective_rpc](https://docs.vllm.ai#vllm.engine.protocol.EngineClient.collective_rpc)Perform a collective RPC call to the given path.

-
–[encode](https://docs.vllm.ai#vllm.engine.protocol.EngineClient.encode)Generate outputs for a request from a pooling model.

-
–[finish_weight_update](https://docs.vllm.ai#vllm.engine.protocol.EngineClient.finish_weight_update)Finish the weight update and set its version if provided.

-
–[generate](https://docs.vllm.ai#vllm.engine.protocol.EngineClient.generate)Generate outputs for a request.

-
–[get_kv_event_sources](https://docs.vllm.ai#vllm.engine.protocol.EngineClient.get_kv_event_sources)KV-event publisher config of each engine, keyed by DP rank.

-
–[get_status](https://docs.vllm.ai#vllm.engine.protocol.EngineClient.get_status)Get fault tolerance status of all engines.

-
–[get_supported_tasks](https://docs.vllm.ai#vllm.engine.protocol.EngineClient.get_supported_tasks)Get supported tasks.

-
–[get_weight_version](https://docs.vllm.ai#vllm.engine.protocol.EngineClient.get_weight_version)Return the latest committed weight version.

-
–[handle_fault](https://docs.vllm.ai#vllm.engine.protocol.EngineClient.handle_fault)Send fault tolerance instruction to the engine.

-
–[init_weight_transfer_engine](https://docs.vllm.ai#vllm.engine.protocol.EngineClient.init_weight_transfer_engine)Initialize weight transfer for RL training.

-
–[is_paused](https://docs.vllm.ai#vllm.engine.protocol.EngineClient.is_paused)Return whether the engine is currently paused.

-
–[is_sleeping](https://docs.vllm.ai#vllm.engine.protocol.EngineClient.is_sleeping)Check whether the engine is sleeping.

-
–[notify_kv_transfer_request_rejected](https://docs.vllm.ai#vllm.engine.protocol.EngineClient.notify_kv_transfer_request_rejected)Notify the engine that a KV-transfer request was rejected before

-
–[pause_generation](https://docs.vllm.ai#vllm.engine.protocol.EngineClient.pause_generation)Pause new generation/encoding requests.

-
–[release_kv_cache_memory](https://docs.vllm.ai#vllm.engine.protocol.EngineClient.release_kv_cache_memory)Discard KV cache physical GPU memory. Requires a completed pause.

-
–[reset_encoder_cache](https://docs.vllm.ai#vllm.engine.protocol.EngineClient.reset_encoder_cache)Reset the encoder cache.

-
–[reset_mm_cache](https://docs.vllm.ai#vllm.engine.protocol.EngineClient.reset_mm_cache)Reset the multi-modal cache.

-
–[reset_prefix_cache](https://docs.vllm.ai#vllm.engine.protocol.EngineClient.reset_prefix_cache)Reset the prefix cache and optionally any configured connector cache.

-
–[resume_generation](https://docs.vllm.ai#vllm.engine.protocol.EngineClient.resume_generation)Resume accepting generation/encoding requests.

-
–[scale_elastic_ep](https://docs.vllm.ai#vllm.engine.protocol.EngineClient.scale_elastic_ep)Scale the engine.

-
–[shutdown](https://docs.vllm.ai#vllm.engine.protocol.EngineClient.shutdown)Shutdown the engine with optional timeout.

-
–[sleep](https://docs.vllm.ai#vllm.engine.protocol.EngineClient.sleep)Sleep the engine.

-
–[start_draft_weight_update](https://docs.vllm.ai#vllm.engine.protocol.EngineClient.start_draft_weight_update)Start a new weight update targeting the speculative draft model.

-
–[start_profile](https://docs.vllm.ai#vllm.engine.protocol.EngineClient.start_profile)Start profiling the engine.

-
–[start_weight_update](https://docs.vllm.ai#vllm.engine.protocol.EngineClient.start_weight_update)Start a new weight update.

-
–[stop_profile](https://docs.vllm.ai#vllm.engine.protocol.EngineClient.stop_profile)Stop profiling the engine.

-
–[update_weight_version](https://docs.vllm.ai#vllm.engine.protocol.EngineClient.update_weight_version)Set the weight version without updating weights.

-
–[update_weights](https://docs.vllm.ai#vllm.engine.protocol.EngineClient.update_weights)Batched weight update for RL training.

-
–[wake_up](https://docs.vllm.ai#vllm.engine.protocol.EngineClient.wake_up)Wake up the engine.


## Source code in `vllm/engine/protocol.py`


|
|

###

`abort(request_id)`

`abstractmethod`

`async`

[¶](https://docs.vllm.ai#vllm.engine.protocol.EngineClient.abort)

Abort a request.

Parameters:

###

`add_lora(lora_request)`

`abstractmethod`

`async`

[¶](https://docs.vllm.ai#vllm.engine.protocol.EngineClient.add_lora)

###

`check_admission(n=1, request_id=None)`

[¶](https://docs.vllm.ai#vllm.engine.protocol.EngineClient.check_admission)

Reject the request up front if it would exceed queue limits.

Called before a response is started so that overload rejections can carry an HTTP status, which is not possible once a streaming response has begun. Engines without admission control accept everything.

Parameters:

-

(`n`

[¶](https://docs.vllm.ai#vllm.engine.protocol.EngineClient.check_admission(n))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)`1`

) –Number of sequences the request will occupy.

-

(`request_id`

[¶](https://docs.vllm.ai#vllm.engine.protocol.EngineClient.check_admission(request_id))

, default:[str](https://docs.python.org/3/builtins/stdtypes.html#str)| None`None`

) –Request id, used for logging only.


Raises:

-
`GracefulHTTPError`

–If the request cannot be admitted.


## Source code in `vllm/engine/protocol.py`


###

`check_health()`

`abstractmethod`

`async`

[¶](https://docs.vllm.ai#vllm.engine.protocol.EngineClient.check_health)

###

`collective_rpc(method, timeout=None, args=(), kwargs=None)`

`async`

[¶](https://docs.vllm.ai#vllm.engine.protocol.EngineClient.collective_rpc)

Perform a collective RPC call to the given path.

###

`encode(prompt, pooling_params, request_id, lora_request=None, trace_headers=None, priority=0, tokenization_kwargs=None, reasoning_ended=None)`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.engine.protocol.EngineClient.encode)

Generate outputs for a request from a pooling model.

## Source code in `vllm/engine/protocol.py`


###

`finish_weight_update(weight_version=None)`

`async`

[¶](https://docs.vllm.ai#vllm.engine.protocol.EngineClient.finish_weight_update)

###

`generate(prompt, sampling_params, request_id, *, prompt_text=None, lora_request=None, tokenization_kwargs=None, trace_headers=None, priority=0, data_parallel_rank=None, session_id=None, kv_hints=None, reasoning_ended=None, reasoning_parser_kwargs=None)`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.engine.protocol.EngineClient.generate)

Generate outputs for a request.

## Source code in `vllm/engine/protocol.py`


###

`get_kv_event_sources()`

[¶](https://docs.vllm.ai#vllm.engine.protocol.EngineClient.get_kv_event_sources)

###

`get_status()`

`async`

[¶](https://docs.vllm.ai#vllm.engine.protocol.EngineClient.get_status)

###

`get_supported_tasks()`

`async`

[¶](https://docs.vllm.ai#vllm.engine.protocol.EngineClient.get_supported_tasks)

###

`get_weight_version()`

`async`

[¶](https://docs.vllm.ai#vllm.engine.protocol.EngineClient.get_weight_version)

###

`handle_fault(fault_tolerance_request)`

`async`

[¶](https://docs.vllm.ai#vllm.engine.protocol.EngineClient.handle_fault)

###

`init_weight_transfer_engine(init_request)`

`async`

[¶](https://docs.vllm.ai#vllm.engine.protocol.EngineClient.init_weight_transfer_engine)

###

`is_paused()`

`abstractmethod`

`async`

[¶](https://docs.vllm.ai#vllm.engine.protocol.EngineClient.is_paused)

###

`is_sleeping()`

`abstractmethod`

`async`

[¶](https://docs.vllm.ai#vllm.engine.protocol.EngineClient.is_sleeping)

###

`notify_kv_transfer_request_rejected(request_id, kv_transfer_params, *, data_parallel_rank=None)`

`abstractmethod`

`async`

[¶](https://docs.vllm.ai#vllm.engine.protocol.EngineClient.notify_kv_transfer_request_rejected)

Notify the engine that a KV-transfer request was rejected before engine admission, so connector-side cleanup can run (e.g. free prefill blocks pinned on the P node).

## Source code in `vllm/engine/protocol.py`


###

`pause_generation(*, mode='abort', wait_for_inflight_requests=False, clear_cache=True)`

`abstractmethod`

`async`

[¶](https://docs.vllm.ai#vllm.engine.protocol.EngineClient.pause_generation)

Pause new generation/encoding requests.

Parameters:

-

(`mode`

[¶](https://docs.vllm.ai#vllm.engine.protocol.EngineClient.pause_generation(mode))`PauseMode`

, default:`'abort'`

) –How to handle in-flight requests: -

`"abort"`

: Abort all in-flight requests immediately and return partial results with "abort" reason (default). -`"wait"`

: Wait for in-flight requests to complete. -`"keep"`

: Freeze requests in queue; they resume on :meth:`resume_generation`

. -

(`wait_for_inflight_requests`

[¶](https://docs.vllm.ai#vllm.engine.protocol.EngineClient.pause_generation(wait_for_inflight_requests))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`False`

) –DEPRECATED. Use

`mode="wait"`

instead. -

(`clear_cache`

[¶](https://docs.vllm.ai#vllm.engine.protocol.EngineClient.pause_generation(clear_cache))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`True`

) –DEPRECATED. Whether to clear KV and prefix caches after draining.


## Source code in `vllm/engine/protocol.py`


###

`release_kv_cache_memory()`

`abstractmethod`

`async`

[¶](https://docs.vllm.ai#vllm.engine.protocol.EngineClient.release_kv_cache_memory)

###

`reset_encoder_cache()`

`abstractmethod`

`async`

[¶](https://docs.vllm.ai#vllm.engine.protocol.EngineClient.reset_encoder_cache)

###

`reset_mm_cache()`

`abstractmethod`

`async`

[¶](https://docs.vllm.ai#vllm.engine.protocol.EngineClient.reset_mm_cache)

###

`reset_prefix_cache(reset_running_requests=False, reset_connector=False)`

`abstractmethod`

`async`

[¶](https://docs.vllm.ai#vllm.engine.protocol.EngineClient.reset_prefix_cache)

Reset the prefix cache and optionally any configured connector cache.

###

`resume_generation()`

`abstractmethod`

`async`

[¶](https://docs.vllm.ai#vllm.engine.protocol.EngineClient.resume_generation)

###

`scale_elastic_ep(new_data_parallel_size, drain_timeout=300)`

`async`

[¶](https://docs.vllm.ai#vllm.engine.protocol.EngineClient.scale_elastic_ep)

###

`shutdown(timeout=None)`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.engine.protocol.EngineClient.shutdown)

###

`sleep(level=1, mode='abort')`

`abstractmethod`

`async`

[¶](https://docs.vllm.ai#vllm.engine.protocol.EngineClient.sleep)

###

`start_draft_weight_update()`

`async`

[¶](https://docs.vllm.ai#vllm.engine.protocol.EngineClient.start_draft_weight_update)

###

`start_profile()`

`abstractmethod`

`async`

[¶](https://docs.vllm.ai#vllm.engine.protocol.EngineClient.start_profile)

###

`start_weight_update()`

`async`

[¶](https://docs.vllm.ai#vllm.engine.protocol.EngineClient.start_weight_update)

###

`stop_profile()`

`abstractmethod`

`async`

[¶](https://docs.vllm.ai#vllm.engine.protocol.EngineClient.stop_profile)

###

`update_weight_version(new_version)`

`async`

[¶](https://docs.vllm.ai#vllm.engine.protocol.EngineClient.update_weight_version)

###

`update_weights(request)`

`async`

[¶](https://docs.vllm.ai#vllm.engine.protocol.EngineClient.update_weights)

##

`StreamingInput`

`dataclass`

[¶](https://docs.vllm.ai#vllm.engine.protocol.StreamingInput)

Input data for a streaming generation request.

This is used with generate() to support multi-turn streaming sessions where inputs are provided via an async generator.