source: https://docs.vllm.ai/en/latest/api/vllm/config/scheduler/
lastmod: 2026-09-24

#

`vllm.config.scheduler`

[¶](https://docs.vllm.ai#vllm.config.scheduler)

Classes:

-
–[SchedulerConfig](https://docs.vllm.ai#vllm.config.scheduler.SchedulerConfig)Scheduler configuration.


##

`SchedulerConfig`

[¶](https://docs.vllm.ai#vllm.config.scheduler.SchedulerConfig)

Scheduler configuration.

Methods:

-
–[compute_hash](https://docs.vllm.ai#vllm.config.scheduler.SchedulerConfig.compute_hash)WARNING: Whenever a new field is added to this config,

-
–[default_factory](https://docs.vllm.ai#vllm.config.scheduler.SchedulerConfig.default_factory)Create a

`SchedulerConfig`

with default values for its`InitVar`

s.

Attributes:

-
([async_scheduling](https://docs.vllm.ai#vllm.config.scheduler.SchedulerConfig.async_scheduling)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)| NoneIf set to False, disable async scheduling. Async scheduling helps to

-
([disable_chunked_mm_input](https://docs.vllm.ai#vllm.config.scheduler.SchedulerConfig.disable_chunked_mm_input)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)If set to true and chunked prefill is enabled, we do not want to

-
([disable_hybrid_kv_cache_manager](https://docs.vllm.ai#vllm.config.scheduler.SchedulerConfig.disable_hybrid_kv_cache_manager)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)| NoneIf set to True, KV cache manager will allocate the same size of KV cache

-
([enable_chunked_prefill](https://docs.vllm.ai#vllm.config.scheduler.SchedulerConfig.enable_chunked_prefill)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)If True, prefill requests can be chunked based

-
([encoder_cache_size](https://docs.vllm.ai#vllm.config.scheduler.SchedulerConfig.encoder_cache_size)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Multimodal encoder cache size, only used in V1.

-
([is_multimodal_model](https://docs.vllm.ai#vllm.config.scheduler.SchedulerConfig.is_multimodal_model)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)True if the model is multimodal.

-
([long_prefill_token_threshold](https://docs.vllm.ai#vllm.config.scheduler.SchedulerConfig.long_prefill_token_threshold)

) –[int](https://docs.python.org/3/builtins/functions.html#int)For chunked prefill, a request is considered long if the prompt is

-
([long_prefill_token_threshold_adaptive](https://docs.vllm.ai#vllm.config.scheduler.SchedulerConfig.long_prefill_token_threshold_adaptive)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Floor the effective long prefill token threshold at a fair share of

-
([max_num_active_seqs](https://docs.vllm.ai#vllm.config.scheduler.SchedulerConfig.max_num_active_seqs)

) –[int](https://docs.python.org/3/builtins/functions.html#int)| NoneMaximum number of requests the scheduler admits into RUNNING.

-
([max_num_batched_tokens](https://docs.vllm.ai#vllm.config.scheduler.SchedulerConfig.max_num_batched_tokens)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Maximum number of tokens that can be processed in a single iteration.

-
([max_num_encoder_input_tokens](https://docs.vllm.ai#vllm.config.scheduler.SchedulerConfig.max_num_encoder_input_tokens)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Multimodal encoder compute budget, only used in V1.

-
([max_num_queued_reqs](https://docs.vllm.ai#vllm.config.scheduler.SchedulerConfig.max_num_queued_reqs)

) –[int](https://docs.python.org/3/builtins/functions.html#int)| NoneMaximum number of requests that can be in-flight (waiting or running)

-
([max_num_queued_tokens](https://docs.vllm.ai#vllm.config.scheduler.SchedulerConfig.max_num_queued_tokens)

) –[int](https://docs.python.org/3/builtins/functions.html#int)| NoneMaximum total prompt tokens of requests currently in the prefill

-
([max_num_scheduled_tokens](https://docs.vllm.ai#vllm.config.scheduler.SchedulerConfig.max_num_scheduled_tokens)

) –[int](https://docs.python.org/3/builtins/functions.html#int)| NoneMaximum number of tokens that the scheduler may issue in a single iteration.

-
([max_num_seqs](https://docs.vllm.ai#vllm.config.scheduler.SchedulerConfig.max_num_seqs)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Maximum number of sequences to be processed in a single iteration.

-
([policy](https://docs.vllm.ai#vllm.config.scheduler.SchedulerConfig.policy)`SchedulerPolicy`

) –The scheduling policy to use:

-
([prefill_schedule_interval](https://docs.vllm.ai#vllm.config.scheduler.SchedulerConfig.prefill_schedule_interval)

) –[int](https://docs.python.org/3/builtins/functions.html#int)For data-parallel deployments, only admit new prefill requests

-
([runner_type](https://docs.vllm.ai#vllm.config.scheduler.SchedulerConfig.runner_type)`RunnerType`

) –The runner type to launch for the model.

-
([scheduler_cls](https://docs.vllm.ai#vllm.config.scheduler.SchedulerConfig.scheduler_cls)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)|[type](https://docs.python.org/3/builtins/functions.html#type)[[object](https://docs.python.org/3/builtins/functions.html#object)] | NoneThe scheduler class to use. "vllm.v1.core.sched.scheduler.Scheduler" is

-
([scheduler_reserve_full_isl](https://docs.vllm.ai#vllm.config.scheduler.SchedulerConfig.scheduler_reserve_full_isl)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)If True, the scheduler checks whether the full input sequence length

-
([stream_interval](https://docs.vllm.ai#vllm.config.scheduler.SchedulerConfig.stream_interval)

) –[int](https://docs.python.org/3/builtins/functions.html#int)The interval (or buffer size) for streaming in terms of token length.

-
([watermark](https://docs.vllm.ai#vllm.config.scheduler.SchedulerConfig.watermark)

) –[float](https://docs.python.org/3/builtins/functions.html#float)Fraction of total KV cache blocks to keep free (the watermark) when


## Source code in `vllm/config/scheduler.py`


|
|

###

`async_scheduling = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.scheduler.SchedulerConfig.async_scheduling)

If set to False, disable async scheduling. Async scheduling helps to avoid gaps in GPU utilization, leading to better latency and throughput.

###

`disable_chunked_mm_input = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.scheduler.SchedulerConfig.disable_chunked_mm_input)

If set to true and chunked prefill is enabled, we do not want to partially schedule a multimodal item. Only used in V1 This ensures that if a request has a mixed prompt (like text tokens TTTT followed by image tokens IIIIIIIIII) where only some image tokens can be scheduled (like TTTTIIIII, leaving IIIII), it will be scheduled as TTTT in one step and IIIIIIIIII in the next.

###

`disable_hybrid_kv_cache_manager = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.scheduler.SchedulerConfig.disable_hybrid_kv_cache_manager)

If set to True, KV cache manager will allocate the same size of KV cache for all attention layers even if there are multiple type of attention layers like full attention and sliding window attention. If set to None, the default value will be determined based on the environment and starting configuration.

###

`enable_chunked_prefill = True`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.scheduler.SchedulerConfig.enable_chunked_prefill)

If True, prefill requests can be chunked based on the remaining `max_num_batched_tokens`

.

The default value here is mainly for convenience when testing. In real usage, this should be set in `EngineArgs.create_engine_config`

.

###

`encoder_cache_size = Field(init=False)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.scheduler.SchedulerConfig.encoder_cache_size)

Multimodal encoder cache size, only used in V1.

NOTE: This is not currently configurable. It will be overridden by max_num_batched_tokens in case max multimodal embedding size is larger.

###

`is_multimodal_model = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.scheduler.SchedulerConfig.is_multimodal_model)

True if the model is multimodal.

###

`long_prefill_token_threshold = Field(default=0, ge=0)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.scheduler.SchedulerConfig.long_prefill_token_threshold)

For chunked prefill, a request is considered long if the prompt is longer than this number of tokens. 0 disables the cap (default).

The cap is not applied when the request is the only one in the batch, since there is no other request for it to starve.

###

`long_prefill_token_threshold_adaptive = Field(default=False)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.scheduler.SchedulerConfig.long_prefill_token_threshold_adaptive)

Floor the effective long prefill token threshold at a fair share of the token budget: max_num_batched_tokens divided by the number of queued and running requests. Only applies when long_prefill_token_threshold is nonzero.

###

`max_num_active_seqs = Field(default=None, ge=1)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.scheduler.SchedulerConfig.max_num_active_seqs)

Maximum number of requests the scheduler admits into RUNNING.

`max_num_seqs`

sizes the model runner (per-request buffers and CUDA graph capture) and is also the default admission limit. Setting this lowers only the number of requests that may occupy RUNNING, so decode batches stay smaller without shrinking runner or graph capacity. Must be `<= max_num_seqs`

. `None`

(default) keeps current behavior.

###

`max_num_batched_tokens = Field(default=DEFAULT_MAX_NUM_BATCHED_TOKENS, ge=1)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.scheduler.SchedulerConfig.max_num_batched_tokens)

Maximum number of tokens that can be processed in a single iteration.

The default value here is mainly for convenience when testing. In real usage, this should be set in `EngineArgs.create_engine_config`

.

###

`max_num_encoder_input_tokens = Field(init=False)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.scheduler.SchedulerConfig.max_num_encoder_input_tokens)

Multimodal encoder compute budget, only used in V1.

NOTE: This is not currently configurable. It will be overridden by max_num_batched_tokens in case max multimodal embedding size is larger.

###

`max_num_queued_reqs = Field(default=None, ge=0)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.scheduler.SchedulerConfig.max_num_queued_reqs)

Maximum number of requests that can be in-flight (waiting or running) at the same time, or None for no limit. When the limit is reached, new requests are rejected with HTTP 503 so the client can retry on another instance. This bounds vLLM's otherwise unbounded request queue and is primarily a coarse capacity valve.

Unlike `max_num_seqs`

, which applies per data-parallel rank, this limit is enforced in the API server process and counts in-flight requests across all DP ranks it routes to. Size it as roughly `data_parallel_size * max_num_seqs`

plus the desired queue depth if it should not bind before per-rank admission does.

###

`max_num_queued_tokens = Field(default=None, ge=0)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.scheduler.SchedulerConfig.max_num_queued_tokens)

Maximum total prompt tokens of requests currently in the prefill phase, or None for no limit. When the limit is reached, new requests are rejected with HTTP 503.

This is a TTFT QoS mechanism: by setting it to `target_TTFT * prefill_throughput`

you reject requests when the prefill backlog would exceed the latency target. In a disaggregated prefill-decode setup this maps directly to the prefill pool's capacity.

Like `max_num_queued_reqs`

, this limit is enforced in the API server process and covers the prefill backlog across all DP ranks it routes to, so `prefill_throughput`

in the formula above is the aggregate throughput of the deployment.

Note: the count is conservative. A partially prefilled request still contributes its full `prompt_len`

until it transitions out of the prefill phase, because the scheduler's per-iteration `num_computed_tokens`

progress is not propagated to the API server process during prefill (`EngineCoreOutput`

is only emitted once the request starts producing tokens). Similarly, prefix-cache hits (`num_cached_tokens`

) are only known to the OutputProcessor after prefill completes. This overestimates the real backlog, causing earlier rejection than strictly necessary — the safe direction for QoS. The impact is limited to long prompts under chunked prefill; short prompts that prefill in a single iteration are unaffected.

###

`max_num_scheduled_tokens = Field(default=None, ge=0)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.scheduler.SchedulerConfig.max_num_scheduled_tokens)

Maximum number of tokens that the scheduler may issue in a single iteration.

This is usually equal to max_num_batched_tokens, but can be smaller in cases when the model might append tokens into the batch (such as speculative decoding). Defaults to max_num_batched_tokens.

###

`max_num_seqs = Field(default=DEFAULT_MAX_NUM_SEQS, ge=1)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.scheduler.SchedulerConfig.max_num_seqs)

Maximum number of sequences to be processed in a single iteration.

The default value here is mainly for convenience when testing. In real usage, this should be set in `EngineArgs.create_engine_config`

.

###

`policy = 'fcfs'`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.scheduler.SchedulerConfig.policy)

The scheduling policy to use:

- "fcfs" means first come first served, i.e. requests are handled in order of arrival.
- "priority" means requests are handled based on given priority (lower value means earlier handling) and time of arrival deciding any ties).

###

`prefill_schedule_interval = Field(default=1, ge=1)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.scheduler.SchedulerConfig.prefill_schedule_interval)

For data-parallel deployments, only admit new prefill requests once every N engine steps, aligned across DP ranks, to better balance per-step forward-pass times.

###

`runner_type = 'generate'`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.scheduler.SchedulerConfig.runner_type)

The runner type to launch for the model.

###

`scheduler_cls = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.scheduler.SchedulerConfig.scheduler_cls)

The scheduler class to use. "vllm.v1.core.sched.scheduler.Scheduler" is the default scheduler. Can be a class directly or the path to a class of form "mod.custom_class".

###

`scheduler_reserve_full_isl = True`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.scheduler.SchedulerConfig.scheduler_reserve_full_isl)

If True, the scheduler checks whether the full input sequence length fits in the KV cache before admitting a new request, rather than only checking the first chunk. Prevents over-admission and KV cache thrashing with chunked prefill.

###

`stream_interval = Field(default=1, ge=1)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.scheduler.SchedulerConfig.stream_interval)

The interval (or buffer size) for streaming in terms of token length. A smaller value (1) makes streaming smoother by sending each token immediately, while a larger value (e.g., 10) reduces host overhead and may increase throughput by batching multiple tokens before sending.

###

`watermark = Field(default=0.0, ge=0.0, lt=1.0)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.scheduler.SchedulerConfig.watermark)

Fraction of total KV cache blocks to keep free (the watermark) when admitting waiting or preempted requests into the running queue. This headroom helps avoid frequent KV cache eviction and the resulting repeated preemption of requests when GPU memory is scarce. Must be in the range [0.0, 1.0); 0.0 (the default) disables the watermark.

###

`_skip_none_validation(value, handler)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.config.scheduler.SchedulerConfig._skip_none_validation)

Skip validation if the value is `None`

when initialisation is delayed.

## Source code in `vllm/config/scheduler.py`


###

`compute_hash()`

[¶](https://docs.vllm.ai#vllm.config.scheduler.SchedulerConfig.compute_hash)

WARNING: Whenever a new field is added to this config, ensure that it is included in the factors list if it affects the computation graph.

Provide a hash that uniquely identifies all the configs that affect the structure of the computation graph from input ids/embeddings to the final hidden states, excluding anything before input ids/embeddings and after the final hidden states.

## Source code in `vllm/config/scheduler.py`


###

`default_factory(**kwargs)`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.config.scheduler.SchedulerConfig.default_factory)

Create a `SchedulerConfig`

with default values for its `InitVar`

s.