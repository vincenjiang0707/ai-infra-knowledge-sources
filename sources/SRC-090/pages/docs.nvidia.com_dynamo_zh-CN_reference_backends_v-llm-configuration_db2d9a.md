source: https://docs.nvidia.com/dynamo/zh-CN/reference/backends/v-llm-configuration
lastmod: 2026-09-23T23:30:39.914Z

vLLM Configuration (DynamoVllmConfig)


vLLM Configuration (DynamoVllmConfig)

Field reference for the Dynamo-specific CLI flags and environment variables of the vLLM backend wrapper.

`DynamoVllmConfig`

holds the Dynamo-specific configuration for the vLLM backend (`python -m dynamo.vllm`

). Every field, type, default, and choice on this page comes from the [ DynamoVllmArgGroup and DynamoVllmConfig](https://github.com/ai-dynamo/dynamo/blob/v1.4.2/components/src/dynamo/vllm/backend_args.py) definitions. For features and operational details, see the


[vLLM Reference Guide](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/backends/v-llm/reference-guide).

These are **only** the Dynamo wrapper flags. The vLLM backend also accepts every native vLLM `EngineArgs`

argument (`--model`

, `--tensor-parallel-size`

, `--max-model-len`

, and so on) in the same command, plus the cross-cutting [Dynamo Runtime](https://docs.nvidia.com/dynamo/reference/components/runtime-configuration) flags (`--namespace`

, `--endpoint`

, and others). Except for the native KV event and KV transfer sections below, this page covers neither — only the vLLM-specific `DYN_VLLM_*`

surface.

## How the config is loaded

Each field is both a CLI flag and an environment variable. The CLI flag takes precedence; the environment variable is the fallback. Boolean fields are negatable — `--headless`

sets it on, `--no-headless`

sets it off.

## Native KV event configuration

`--kv-events-config`

and `--enable-prefix-caching`

are native vLLM engine arguments rather than `DynamoVllmConfig`

fields, but they determine whether a worker publishes the cache events used by event-driven KV-aware routing.

Starting the frontend with `--router-mode kv`

does not configure event publishing on vLLM workers. Enable publishing explicitly on every aggregated or prefill worker whose cache state the router should track.

The `endpoint`

value is the base ZeroMQ port. vLLM assigns each data-parallel rank the port at `base port + data-parallel rank`

. When multiple workers share a host or network namespace, reserve one port per rank and choose base ports whose resulting ranges do not overlap.

If workers do not publish KV events, configure the frontend with `--no-router-kv-events`

for prediction-based KV routing or `--load-aware`

for load-only routing.

## Native KV transfer configuration

`--kv-transfer-config`

is a native vLLM engine argument rather than a `DynamoVllmConfig`

field, so it has no `DYN_VLLM_*`

environment variable. It selects the KV connector that moves cache blocks between prefill and decode workers.

A worker started with `--disaggregation-mode prefill`

must be passed `--kv-transfer-config`

explicitly. Without it, the worker raises a `ValueError`

during argument parsing and never starts. All non-prefill modes — `agg`

, `pd`

, `decode`

, and `encode`

— do not enforce this check.

The value is a JSON object. For NIXL-based prefill/decode disaggregation:

Only the prefill worker is required to set it, but both halves of a NIXL pair must agree on a connector for transfers to succeed. Pass the same `--kv-transfer-config`

value to the decode worker, as the [disaggregated vLLM launch script](https://github.com/ai-dynamo/dynamo/blob/v1.4.2/examples/backends/vllm/launch/disagg.sh) does.

The earlier `--connector`

flag is no longer accepted by the vLLM backend. Setting it — on the command line or through the `DYN_CONNECTOR`

environment variable — raises a `ValueError`

during argument parsing. The message depends on the value:

- An active connector, such as
`--connector nixl`

or`DYN_CONNECTOR=nixl`

, reports the equivalent`--kv-transfer-config`

JSON to use instead. `--connector none`

or`--connector null`

reports that the flag is no longer needed, because no connector is already the default. There is no equivalent value to migrate to, so none is shown.`DYN_CONNECTOR`

set to an empty or whitespace-only value reports that the variable is no longer supported, without an equivalent value.

## Worker role and disaggregation

These flags control which role this worker plays in a disaggregated deployment. The default when no `--disaggregation-mode`

is set is aggregated (`agg`

).

Worker disaggregation mode. `agg`

(default when unset) runs a combined aggregated prefill+decode worker. `pd`

is a legacy alias for `agg`

. `prefill`

and `decode`

split the pipeline for prefill/decode disaggregation. `encode`

starts a multimodal encode-only worker.

`prefill`

additionally requires the native `--kv-transfer-config`

argument — see [Native KV transfer configuration](https://docs.nvidia.com/dynamo/reference/backends/v-llm-configuration#native-kv-transfer-configuration).

Environment variable: `DYN_VLLM_DISAGGREGATION_MODE`


Run in headless mode for multi-node tensor-parallel or pipeline-parallel deployments. Secondary nodes run vLLM workers only with no Dynamo endpoints. See the vLLM multi-node data parallel documentation for details.

Environment variable: `DYN_VLLM_HEADLESS`


## Tokenizer and multimodal

Use vLLM’s tokenizer for pre- and post-processing. This bypasses Dynamo’s preprocessor; only the `/v1/chat/completions`

endpoint will be available through the Dynamo frontend.

Environment variable: `DYN_VLLM_USE_TOKENIZER`


Enable multimodal processing. Combine it with `--disaggregation-mode=encode`

, `--disaggregation-mode=pd`

, `--disaggregation-mode=prefill`

, or `--disaggregation-mode=decode`

to select a disaggregated multimodal role. Use the default `agg`

mode for aggregated multimodal serving.

Environment variable: `DYN_VLLM_ENABLE_MULTIMODAL`


Enable routing to separate encoder workers for multimodal processing.

Environment variable: `DYN_VLLM_ROUTE_TO_ENCODER`


Prompt template used to construct the final multimodal prompt sent to the model. The literal `<prompt>`

token is replaced with the user’s text at inference time; `<image>`

marks where the image placeholder appears. Update this template to match your model’s expected format.

Environment variable: `DYN_VLLM_MM_PROMPT_TEMPLATE`


Enable frontend decoding of multimodal images. Images are decoded in the Rust frontend and transferred to the backend via NIXL RDMA, bypassing in-engine HTTP fetch and decode.

Environment variable: `DYN_VLLM_FRONTEND_DECODING`


## Embedding

Embedding transfer mode used between encode and decode workers. `local`

keeps embeddings on the local file system. `nixl-write`

and `nixl-read`

transfer them over NIXL RDMA (writer-initiated or reader-initiated, respectively).

Environment variable: `DYN_VLLM_EMBEDDING_TRANSFER_MODE`


Run as a text-embedding worker. The vLLM engine must be started with `--runner pooling`

. KV-event publishing, KV router registration, and `InstrumentedScheduler`

injection are all skipped, as they do not apply to pooling models.

Environment variable: `DYN_VLLM_EMBEDDING_WORKER`


## Other

Enable reinforcement-learning training support. Selects RL-friendly vLLM defaults for token-in/token-out (TITO) workloads and per-token logprob parity. Mirrors `--enable-rl`

on the SGLang backend.

Environment variable: `DYN_ENABLE_RL`


Enable GMS (GPU Memory Service) shadow/standby mode. Shadow engines skip KV cache allocation at startup, automatically pause after initialization, and resume on demand when the active engine dies. Requires `--load-format=gms`

.

Environment variable: `DYN_VLLM_GMS_SHADOW_MODE`


## Benchmarking

These flags control the self-benchmark sweep that runs on startup before the worker begins accepting production requests.

The sweep does not walk a fixed grid of sample counts. Each axis is derived from the engine’s own limits — CUDA-graph axes include every `{capture size, capture size + 1}`

boundary and then continue geometrically to the engine limit, and KV-read axes use complete power-of-two block ladders plus their exact feasible maxima. The flags below are per-axis *sample limits* applied to those derived axes: if an axis has more points than its limit allows, points are selected uniformly across the sorted axis while the endpoints are retained. Raising a limit therefore measures more of the same axis; it does not change the axis itself.

Run a self-benchmark on startup before accepting requests. Sweeps prefill input sequence lengths (ISLs) and/or decode `(context_length × batch_size)`

operating points, collecting `ForwardPassMetrics`

at each point.

Environment variable: `DYN_BENCHMARK_MODE`


JSON file of explicit pure prefill and decode benchmark points, applied uniformly to every data-parallel rank. The file is read and normalized once before the vLLM workers start, then the same contents are forwarded to every rank.

The file completely replaces generated grid sampling for the phases selected by `--benchmark-mode`

, so all of the sample-limit flags below — and the deprecated granularity flags — are ignored when it is set. Setting it without `--benchmark-mode`

raises a `ValueError`

.

Environment variable: `DYN_BENCHMARK_POINTS_FILE`


Maximum number of iteration-total prefill new-token samples. Must be at least 2, so that both endpoints of the axis are always retained.

Environment variable: `DYN_PREFILL_MAX_NEW_TOKEN_SAMPLES`


Maximum number of iteration-total prefill KV-read-token samples, applied for each `(new tokens, batch size)`

pair. Sampling always retains zero and the feasible maximum. Must be at least 2.

Environment variable: `DYN_PREFILL_MAX_KV_READ_TOKEN_SAMPLES`


Maximum number of iteration-total decode KV-read-token samples, applied for each batch size. Sampling always retains the minimum and the feasible maximum. Must be at least 2.

Environment variable: `DYN_DECODE_MAX_KV_READ_TOKEN_SAMPLES`


Maximum number of decode batch-size samples over the CUDA-graph-aware axis. Sampling always retains the minimum and the feasible maximum. Must be at least 2.

Environment variable: `DYN_DECODE_MAX_BATCH_SIZE_SAMPLES`


Maximum number of prefill request-batch-size samples for each new-token point. Unlike the limits above, this one keeps the first N values of the sorted power-of-two-plus-legal-maximum axis rather than sampling uniformly, so the default of 3 selects `[1, 2, 4]`

when all three are legal. Must be positive.

Environment variable: `DYN_PREFIX_MAX_BATCH_SIZE_SAMPLES`


Number of warmup iterations to run before benchmark measurement begins.

Environment variable: `DYN_BENCHMARK_WARMUP_ITERATIONS`


File path where benchmark results are written in JSON format.

Environment variable: `DYN_BENCHMARK_OUTPUT_PATH`


Soft limit, in seconds, for the self-benchmark. Reaching it does not fail worker startup: the iteration being measured finishes, the partial results collected so far are returned, and engine startup continues. A bounded cleanup grace still fails closed if no result is written at all. Must be positive.

Environment variable: `DYN_BENCHMARK_TIMEOUT`


## Deprecated

These flags are retained for backward compatibility and will be removed in a future release. Each is mapped to its replacement at startup with a deprecation warning.

**Deprecated** — accepted for compatibility with older ModelExpress manifests only. The vLLM ModelExpress plugin reads its own configuration.

Environment variable: `MODEL_EXPRESS_URL`


The five `--benchmark-*-granularity`

flags below are the previous names for the benchmark sampling limits. They are read only when `--benchmark-mode`

is set and `--benchmark-points-file`

is not; otherwise they are ignored entirely, and none of the translation, range checking, or deprecation warnings described here takes place. Under those conditions each is translated to its replacement at startup, with a deprecation warning, and is accepted in the range 1 to 1024; a value outside it raises a `ValueError`

. Because the four uniform-sampling limits need both endpoints of their axis, a legacy value of `1`

maps to `2`

for those flags.

With `--benchmark-mode`

set and no points file, passing a legacy flag together with its replacement raises a `ValueError`

at startup — `cannot combine --benchmark-decode-length-granularity with --decode-max-kv-read-token-samples`

, and likewise for each of the other pairs. Migrate to the replacement rather than setting both. All five are ignored when `--benchmark-points-file`

is set.

**Deprecated** — use `--prefill-max-new-token-samples`

instead.

Environment variable: `DYN_BENCHMARK_PREFILL_GRANULARITY`


**Deprecated** — use `--prefill-max-kv-read-token-samples`

instead.

Environment variable: `DYN_BENCHMARK_PREFILL_KV_READ_GRANULARITY`


**Deprecated** — use `--prefix-max-batch-size-samples`

instead. This is the one legacy flag whose replacement does not sample uniformly, so a legacy value of `1`

is carried across unchanged.

Environment variable: `DYN_BENCHMARK_PREFILL_BATCH_GRANULARITY`


**Deprecated** — use `--decode-max-kv-read-token-samples`

instead.

Environment variable: `DYN_BENCHMARK_DECODE_LENGTH_GRANULARITY`


**Deprecated** — use `--decode-max-batch-size-samples`

instead.

Environment variable: `DYN_BENCHMARK_DECODE_BATCH_GRANULARITY`


## Validation rules

`--embedding-worker`

is only valid with`--disaggregation-mode=agg`

(or the default aggregated mode) and cannot be combined with`--enable-multimodal`

or`--benchmark-mode`

.