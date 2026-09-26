source: https://docs.nvidia.com/dynamo/reference/api/python/llm
lastmod: 2026-09-24T19:58:16.636Z

# dynamo.llm

High-level LLM primitives for building request pipelines.

`dynamo.llm`

publishes 36 classes and 10 functions. Source: `lib/bindings/python/src/dynamo/llm/__init__.py`


###### AicPerfConfig (class)


No summary available.

`lib/bindings/python/src/dynamo/_core.pyi#L1721`


**Public methods**

**init**

No summary available.

###### EngineType (class)


###### EntrypointArgs (class)


Settings to connect an input to a worker and run them. Use by `dynamo run`

.

`lib/bindings/python/src/dynamo/_core.pyi#L3163`


**Public methods**

**init**

Create EntrypointArgs.

**Parameters**

The type of engine to use

Path to the model directory on disk

Model name or dynamo endpoint (e.g. ‘dyn://namespace.component.endpoint’)

Optional endpoint ID

Optional path to a prompt template file

Optional router configuration

Optional KV cache block size

HTTP host to bind to

HTTP port to bind to

HTTP metrics port (for gRPC service)

TLS certificate path (PEM format)

TLS key path (PEM format)

Optional path to mocker engine arguments JSON

Typed mocker engine arguments

Optional runtime configuration for discovery registration

Dynamo namespace for model discovery scoping

Optional namespace prefix

Whether this is a prefill worker

Whether this is a decode worker (disaggregated); pairs with a prefill peer for readiness

Maximum number of request migrations (0=disabled)

Optional max sequence length for migration

Optional Python chat completions engine factory callback

Optional AIC perf-model configuration for default KV routing

Optional Prometheus metrics prefix override

Optional Anthropic Messages API override

Optional Anthropic preamble stripping override

Optional streaming tool dispatch override

Optional streaming reasoning dispatch override

Optional tokenizer backend override (“default” or “fastokens”)

###### FpmDirectPublisher (class)


Direct Forward Pass Metrics publisher used by in-process producers such as the TRT-LLM adapter. The underlying Rust publisher owns per-DP-rank serialization tasks (each with its own 1s idle heartbeat timer) and a single event-plane publisher task. Python callers do not manage heartbeat: when `publish`

is not called for `IDLE_HEARTBEAT_INTERVAL`

(1.0s, matching vLLM’s `HEARTBEAT_INTERVAL`

), the Rust side emits a zeroed snapshot on that rank’s channel.

`lib/bindings/python/src/dynamo/_core.pyi#L1284`


**Public methods**

**init**

Create a publisher with `dp_size`

per-DP-rank channels.

**Parameters**

Dynamo component endpoint (provides runtime + discovery).

Unique worker identifier stamped on every emitted FPM.

Number of DP ranks to allocate channels for. Use `1`

when attention DP is disabled.

#### publish

Publish one iteration’s FPM snapshot for the given DP rank.

All parameters are keyword-only on the Python side: adjacent ints
with similar units (`scheduled_*`

vs `queued_*`

, `*_prefill_*`

vs `*_decode_*`

) cannot be distinguished by the type system, so
a transposition would silently corrupt every published snapshot.

Variance fields (var_prefill_length, var_decode_kv_tokens, var_queued_prefill_length, var_queued_decode_kv_tokens) are defaulted to 0.0 per the MVP scope; a follow-up PR can add Welford-based variance computation.

#### shutdown

Shut down the publisher and its per-rank serialization tasks.

###### FpmEventRelay (class)


Relay that bridges ForwardPassMetrics from a local raw ZMQ PUB socket (InstrumentedScheduler in EngineCore child process) to the Dynamo event plane with automatic discovery registration.

`lib/bindings/python/src/dynamo/_core.pyi#L1257`


**Public methods**

**init**

Create a relay.

**Parameters**

Dynamo component endpoint (provides runtime + discovery).

Local ZMQ PUB address to subscribe to (e.g., “tcp://127.0.0.1:20380”).

#### shutdown

Shut down the relay task.

###### FpmEventSubscriber (class)


Subscriber for ForwardPassMetrics from the Dynamo event plane. Auto-discovers engine publishers via the discovery plane.

Two mutually exclusive usage modes:

**recv mode**(default): call`recv()`

to pull individual messages.**tracking mode**: call`start_tracking()`

once, then poll`get_recent_stats()`

to retrieve the latest FPM bytes keyed by`(worker_id, dp_rank)`

. Stale entries are cleaned up when workers are removed (via discovery watch).

`lib/bindings/python/src/dynamo/_core.pyi#L1347`


**Public methods**

**init**

Create a subscriber that auto-discovers FPM publishers.

No background tasks are started until `recv()`

or
`start_tracking()`

is called.

**Parameters**

Dynamo component endpoint (provides runtime + discovery).

#### recv

Blocking receive of the next message (raw msgspec bytes). Releases the GIL while waiting.

On the first call a background subscriber task is spawned (recv mode).
Cannot be used after `start_tracking()`

.

**Returns**

`Optional[bytes]`

— Raw msgspec payload, or None if the stream is closed.

#### start_tracking

Start background tracking of the latest FPM per (worker_id, dp_rank).

Spawns two background tasks:

- Event consumption: subscribes to FPM events, extracts the composite key (worker_id, dp_rank) from the msgpack payload, stores latest raw bytes in an internal map.
- MDC discovery watch: monitors ComponentModels for the target component. When a model is removed, all entries whose worker_id matches the removed instance_id are purged.

After calling this, `recv()`

will raise RuntimeError.

#### get_recent_stats

Return the latest FPM bytes for every tracked (worker_id, dp_rank).

Cleanup of removed engines is handled by the MDC discovery watch
task spawned by `start_tracking()`

.

Raises RuntimeError if `start_tracking()`

has not been called.

**Returns**

`dict[tuple[str, int], bytes]`

— dict mapping`(worker_id, dp_rank)`

to raw msgspec bytes.`dict[tuple[str, int], bytes]`

— Decode each value with`forward_pass_metrics.decode(data)`

.

#### get_model_cards

Snapshot of model deployment cards keyed by worker id.

The snapshot is filtered against the known-workers set so entries
for already-removed workers are not returned. Values are the raw
`ModelDeploymentCard`

serialized as a JSON string; callers parse
whichever fields they need (e.g. `runtime_config`

,
`display_name`

).

Raises RuntimeError if `start_tracking()`

has not been called.

**Returns**

`dict[str, str]`

— dict mapping`worker_id`

to`card_json`

(JSON string).

#### shutdown

Shut down the subscriber (all background tasks).

###### FrontendExtensionContext (class)


Read-only, live view of frontend state passed to extension route handlers.

Handlers receive this and answer from current state. The surface is intentionally narrow (typed read-only accessors only); it does not expose the internal service state.

`lib/bindings/python/src/dynamo/_core.pyi#L2501`


**Public methods**

#### is_ready

Whether the HTTP service has finished startup and is ready to serve.

#### is_cancelled

Whether the frontend is shutting down (draining).

#### has_any_ready_model

Whether at least one model is registered and ready to serve.

#### is_model_ready_to_serve

Whether the named model is registered and ready to serve.

#### model_display_names

Sorted display names of all registered models.

#### serving_ready_display_names

Sorted display names of models ready to serve.

###### FrontendResponse (class)


Explicit status-code override returned by a `FrontendRoute`

handler.

Return this to set a non-200 status (e.g. `FrontendResponse(503, body)`

);
return a plain JSON-serializable value for the default 200.

`lib/bindings/python/src/dynamo/_core.pyi#L2554`


**Public methods**

**init**

No summary available.

###### FrontendRoute (class)


A trusted extension route served on the Dynamo HTTP frontend.

Currently restricted to static-path `GET`

routes. `handler`

is a
synchronous callable that receives a `FrontendExtensionContext`

and
returns a JSON-serializable body (implies HTTP 200) or a `FrontendResponse`

to set the status code. Async handlers and path parameters are rejected at
construction.

`lib/bindings/python/src/dynamo/_core.pyi#L2533`


**Public methods**

**init**

No summary available.

###### HttpAsyncEngine (class)


An async engine for a distributed Dynamo http service. This is an extension of the python based AsyncEngine that handles HttpError exceptions from Python and converts them to the Rust version of HttpError

###### HttpError (class)


No summary available.

`lib/bindings/python/src/dynamo/llm/exceptions.py#L25`


**Public methods**

**init**

No summary available.

###### HttpService (class)


A HTTP service for dynamo applications. It is a OpenAI compatible http ingress into the Dynamo Distributed Runtime.

`lib/bindings/python/src/dynamo/_core.pyi#L1440`


**Public methods**

**init**

Create a new HTTP service.

**Parameters**

Optional port number to bind the service to (default: 8080)

#### run

Run the HTTP service.

**Parameters**

DistributedRuntime instance for token management

#### shutdown

Shutdown the HTTP service by cancelling its internal token.

###### KserveGrpcService (class)


A gRPC service implementing the KServe protocol for dynamo applications. Provides model management for completions, chat completions, and tensor-based models.

`lib/bindings/python/src/dynamo/_core.pyi#L1490`


**Public methods**

**init**

Create a new KServe gRPC service.

**Parameters**

Optional port number to bind the service to

Optional host address to bind the service to

#### add_completions_model

Register a completions model with the service.

**Parameters**

The model name

The model checksum

The async engine to handle requests

#### add_chat_completions_model

Register a chat completions model with the service.

**Parameters**

The model name

The model checksum

The async engine to handle requests

#### add_tensor_model

Register a tensor-based model with the service.

**Parameters**

The model name

The model checksum

The async engine to handle requests

Optional runtime-resolved worker metadata

Optional tensor protocol model metadata

#### remove_completions_model

Remove a completions model from the service.

**Parameters**

The model name to remove

#### remove_chat_completions_model

Remove a chat completions model from the service.

**Parameters**

The model name to remove

#### remove_tensor_model

Remove a tensor model from the service.

**Parameters**

The model name to remove

#### list_chat_completions_models

List all registered chat completions models.

**Returns**

`List[str]`

— List of model names

#### list_completions_models

List all registered completions models.

**Returns**

`List[str]`

— List of model names

#### list_tensor_models

List all registered tensor models.

**Returns**

`List[str]`

— List of model names

#### run

Run the KServe gRPC service.

**Parameters**

DistributedRuntime instance for token management

#### shutdown

Shutdown the KServe gRPC service by cancelling its internal token.

###### KvEventPublisher (class)


A KV event publisher will publish KV events corresponding to the component.

`lib/bindings/python/src/dynamo/_core.pyi#L1155`


**Public methods**

**init**

Create a `KvEventPublisher`

object.

When zmq_endpoint is provided, the publisher subscribes to a ZMQ socket for incoming engine events (e.g. from SGLang/vLLM) and relays them to NATS.

When zmq_endpoint is None, events are pushed manually via publish_batch, publish_stored, or publish_removed.

**Parameters**

The endpoint to extract component information from for event publishing

Optional worker ID override. Use None to infer from endpoint.

The KV block size (must be > 0)

The data parallel rank (defaults to 0)

Enable worker-local KV indexer

Optional ZMQ endpoint for relay mode (e.g. “tcp://127.0.0.1:5557”)

ZMQ topic to subscribe to (defaults to "" when zmq_endpoint is set)

Cross-list batching timeout in milliseconds. None/0 flushes at each submitted source-list boundary.

KV event ownership endpoint; defaults to endpoint.

#### publish_stored

Publish a KV stored event.

Event IDs are managed internally by the publisher using a monotonic counter.

**Parameters**

List of token IDs

Number of tokens per block

List of block hashes (signed 64-bit integers)

Optional parent hash (signed 64-bit integer)

Optional list of multimodal info for each block. Each item is either None or a dict with “mm_objects” key containing a list of {“mm_hash”: int, “offsets”: [[start, end], …]} dicts.

Optional LoRA adapter name for adapter-aware block hashing.

Optional Eagle mode flag. When true, stored blocks are
reconstructed using overlapping `kv_block_size + 1`

token windows.

#### publish_removed

Publish a KV removed event.

Event IDs are managed internally by the publisher using a monotonic counter.

**Parameters**

List of block hashes to remove (signed 64-bit integers)

#### publish_batch

Publish an ordered list of KV events as one processor input.

The complete list is validated before it is enqueued. Compatible events are coalesced while preserving source order and the processor’s existing block-count limits.

#### shutdown

Shuts down the event publisher, stopping any background tasks.

###### KvRouter (class)


A KV-aware router that performs intelligent routing based on KV cache overlap.

`lib/bindings/python/src/dynamo/_core.pyi#L2913`


**Public methods**

**init**

Create a new KvRouter instance.

**Parameters**

The endpoint to connect to for routing requests

The KV cache block size

Configuration for the KV router

Optional AIC perf-model config for effective prefill load tracking

#### generate

Generate text using the KV-aware router.

**Parameters**

Input token IDs

Model name to use for generation

Optional stop conditions for generation

Optional sampling configuration

Optional output configuration

Optional router configuration override

Optional worker ID to route to directly. If set, the request will be sent to this specific worker and router states will be updated accordingly.

Optional data parallel rank to route to. If set along with worker_id, the request will be routed to the specific (worker_id, dp_rank) pair. If only dp_rank is set, the router will select the best worker but force routing to the specified dp_rank.

Optional extra request arguments to include in the PreprocessedRequest.

Optional block-level multimodal metadata aligned to request blocks. Backward-compatible shortcut; this is converted to mm_routing_info with routing_token_ids=token_ids.

Optional multimodal payload map to preserve image/video data for downstream model execution.

Optional structured routing-only multimodal payload (e.g., {“routing_token_ids”: […], “block_mm_infos”: […]}) used by router selection without changing execution token_ids.

Optional request routing constraints used to constrain or prefer tainted workers.

Maximum number of responses buffered by the Python adapter. Set to 0 for demand-driven direct Python consumption; negative values are rejected.

**Returns**

`AsyncIterator[JsonLike]`

— An async iterator yielding generation responses

- If worker_id is set, the request bypasses KV matching and routes directly to the specified worker while still updating router states.
- dp_rank allows targeting a specific data parallel replica when workers have multiple replicas (data_parallel_size > 1).
- This is different from query_instance_id which doesn’t route the request.

#### generate_from_request

Generate from a preprocessed request dict (PreprocessedRequest format).

Accepts a full request dict with token_ids, model, stop_conditions, etc. Set response_buffer_size to 0 for demand-driven direct Python consumption; negative values are rejected. Returns an async iterator yielding generation responses.

#### best_worker

Find the best matching worker for the given tokens.

**Parameters**

List of token IDs to find matches for

Optional router configuration override

Optional request ID. If provided, router states will be updated to track this request (active blocks, lifecycle events). If not provided, this is a query-only operation that doesn’t affect state.

Whether to record the selected worker in the router’s
approximate indexer. This is only meaningful when
`use_kv_events=False`

and is independent from lifecycle
state tracking via `request_id`

.

Optional block-level multimodal metadata aligned to request blocks. When provided, this is used in block hash computation to enable MM-aware worker selection.

Optional cache namespace used in block hash computation.

Requested policy family, or an exact explicit class. Missing, unknown, and ordinary physical-class names use the configured default family before cache-bucket resolution.

**Returns**

`Tuple[int, int, int]`

— A tuple of (worker_id, dp_rank, overlap_blocks) where: - worker_id: The ID of the best matching worker - dp_rank: The data parallel rank of the selected worker - overlap_blocks: The number of overlapping blocks found

#### get_potential_loads

Get potential prefill and decode loads for all workers.

**Parameters**

List of token IDs to evaluate

Optional block-level multimodal metadata aligned to request blocks. When provided, this is used in hash computation for MM-aware potential-load estimation.

Optional LoRA adapter name used in block hash computation.

**Returns**

`List[Dict[str, int]]`

— A list of dictionaries, each containing: - worker_id: The worker ID - dp_rank: The data parallel rank - potential_prefill_tokens: Number of tokens that would need prefill - potential_decode_blocks: Number of blocks currently in decode phase - active_requests: Number of active requests tracked on the worker

Each (worker_id, dp_rank) pair is returned as a separate entry. If you need aggregated loads per worker_id, sum the values manually.

#### get_overlap_scores

Get per-worker KV overlap by storage tier.

**Parameters**

List of token IDs to evaluate.

Optional router configuration override for score-credit fields.

Optional block-level multimodal metadata aligned to request blocks.

Optional LoRA adapter name for adapter-aware matching.

Whether to query the configured shared cache.

**Returns**

`Dict[str, Any]`

— A dictionary containing block_size, num_blocks, shared_cache, and`Dict[str, Any]`

— workers. Each worker row is keyed by worker_id and dp_rank and`Dict[str, Any]`

— reports device, host-pinned, disk, and shared-cache overlap blocks.

#### dump_events

Dump all events from the KV router’s indexer.

**Returns**

`str`

— A JSON string containing all indexer events

#### mark_prefill_complete

Mark prefill as completed for a request.

This signals that the request has finished its prefill phase and is now in the decode phase. Used to update router state for accurate load tracking.

**Parameters**

The ID of the request that completed prefill

This is typically called automatically by the router when using the
`generate()`

method. Only call this manually if you’re using
`best_worker()`

with `request_id`

for custom routing.

#### free

Free a request by its ID, signaling the router to release resources.

This should be called when a request completes to update the router’s tracking of active blocks and ensure accurate load balancing.

**Parameters**

The ID of the request to free

This is typically called automatically by the router when using the
`generate()`

method. Only call this manually if you’re using
`best_worker()`

with `request_id`

for custom routing.

###### KvRouterConfig (class)


Values for KV router

`lib/bindings/python/src/dynamo/_core.pyi#L1900`


**Public methods**

**init**

Create a KV router configuration.

**Parameters**

Deprecated positional/keyword alias for prefill_load_scale. When present, it takes precedence over prefill_load_scale; a value of 0 also sets overlap_score_credit to 0.

Finite, non-negative credit multiplier for device-local prefix overlap (default: 1.0). Values above 1.0 give device overlap extra credit and can make adjusted prefill cost negative.

Scale for adjusted prompt-side prefill load after cache-hit credits (default: 1.0)

Experimental block-equivalent decode cost added for each active request on a candidate worker (default: 0.0)

Credit multiplier for host-pinned cache hits (default: 0.75)

Credit multiplier for disk/external cache hits (default: 0.25)

Temperature for normalized worker sampling via softmax (default: 0.0)

Whether to use KV events from workers (default: True)

Enable replica synchronization (default: False)

Track active blocks for load balancing (default: True)

Track output blocks during generation (default: False). When enabled, the router adds placeholder blocks as tokens are generated and applies fractional decay based on progress toward expected output sequence length (agent_hints.osl in nvext).

Assume KV cache reuse when tracking active blocks (default: True). When True, computes actual block hashes. When False, generates random hashes.

Include prompt-side prefill tokens in active load accounting (default: True).

Tracking identity algorithm, “public-xxh3-v1” or “keyed-xxh3-v1” (default: “public-xxh3-v1”).

File containing exactly 32 raw provider-key bytes. Required only for keyed tracking mode.

Provider-managed key epoch mixed into keyed scope derivation. Required only for keyed tracking mode.

Prompt-side prefill load model (default: “none”). “none” keeps static prompt load accounting. “aic” decays the oldest active prefill request using AIC-predicted duration.

TTL for blocks in seconds when not using KV events (default: 120.0)

Optional queue threshold fraction for prefill token capacity (default: None). Requests are queued if all workers exceed this fraction of max_num_batched_tokens. Enables priority scheduling via request priority hints. Set a numeric value to enable queueing.

Startup-only policy-family and cache-bucket queue YAML path. When omitted, router_queue_threshold and router_queue_policy define one synthetic policy class.

Number of KV indexer worker threads (default: 4). When > 1, uses a concurrent radix tree with a thread pool, including for approximate routing when KV events are disabled.

Scheduling policy for the router queue (default: “fcfs”). “fcfs”: first-come first-served with priority bumps — optimizes tail TTFT. “lcfs”: last-come first-served with priority bumps — intentionally worsens tail behavior for policy comparisons. “wspt”: weighted shortest processing time (Smith’s rule) — optimizes average TTFT.

Query a remote KV indexer served from the worker component (default: False).

Serve this router’s local indexer from the worker component (default: False).

Credit multiplier for shared cache hits beyond the device prefix (default: 0.0).

External shared KV cache type, “none” or “hicache” (default: “none”).

Enables predict-on-route when set. This TTL applies to entries in the local side indexer and requires use_kv_events=True. Set to None to disable. Independent of router_ttl_secs, which covers pure approximate mode.

#### from_json

No summary available.

#### copy

No summary available.

#### with_overrides

No summary available.

###### LoRADownloader (class)


Unified interface for LoRA downloading and caching (local file:// and S3 s3:// URIs).

`lib/bindings/python/src/dynamo/_core.pyi#L2450`


**Public methods**

**init**

No summary available.

#### download_if_needed

No summary available.

#### get_cache_path

No summary available.

#### is_cached

No summary available.

#### validate_cached

No summary available.

#### uri_to_cache_key

No summary available.

###### MediaDecoder (class)


Media decoder for image and video preprocessing.

`lib/bindings/python/src/dynamo/_core.pyi#L2463`


**Public methods**

**init**

No summary available.

#### enable_image

No summary available.

###### MediaFetcher (class)


Media fetcher for loading remote image/video URLs.

`lib/bindings/python/src/dynamo/_core.pyi#L2470`


**Public methods**

**init**

No summary available.

#### user_agent

No summary available.

#### allow_direct_ip

No summary available.

#### allow_direct_port

No summary available.

#### allowed_media_domains

No summary available.

#### timeout_ms

No summary available.

###### ModelCardInstanceId (class)


Unique identifier for a worker instance: namespace, component, endpoint and instance_id. The instance_id is not currently exposed in the Python bindings.

`lib/bindings/python/src/dynamo/_core.pyi#L383`


**Public methods**

#### triple

Triple of namespace, component and endpoint this worker is serving.

###### ModelInput (class)


What type of request this model needs: Text, Tokens or Tensor

###### ModelRuntimeConfig (class)


A model runtime configuration is a collection of runtime information

`lib/bindings/python/src/dynamo/_core.pyi#L854`


**Public methods**

**init**

No summary available.

#### set_engine_specific

Set an engine-specific runtime configuration value

#### get_engine_specific

Get an engine-specific runtime configuration value

#### set_structural_tag_mode

Set structural tag mode (“off” or “on”).

#### set_structural_tag_scope

Set structural tag scope (“auto” or “always”).

#### set_structural_tag_schema

Set structural tag schema mode (“auto” or “strict”).

#### set_disaggregated_endpoint

Set the disaggregated endpoint for the model

###### ModelType (class)


OpenAI-style surfaces supported by a model.

Values are Chat, Completions, Embedding, Classify, Pooling, TensorBased, Images, Audios, Videos, Realtime, and Empty (no OpenAI surface).

`lib/bindings/python/src/dynamo/_core.pyi#L1635`


**Public methods**

#### supports_chat

Return True if this model type supports chat.

#### supports_embedding

Return True if this model type supports /v1/embeddings.

#### supports_classify

Return True if this model type supports /v1/classify.

#### supports_pooling

Return True if this model type supports /v1/pooling.

###### MultimodalEmbeddingCachePublisher (class)


A publisher for multimodal encode-worker cache state.

`lib/bindings/python/src/dynamo/_core.pyi#L683`


**Public methods**

**init**

Create a `MultimodalEmbeddingCachePublisher`

object.

#### create_endpoint

Initialize event-plane publishing for multimodal cache state.

**Parameters**

The endpoint to extract component information from.

#### publish_delta

Publish an incremental cache mutation for this worker.

**Parameters**

Newly cached embedding keys.

Cache keys no longer present on the worker.

###### OverlapScores (class)


A collection of prefix matching scores of workers for a given token ids. ‘scores’ is a map of worker id to the score which is the number of matching blocks.

###### PythonAsyncEngine (class)


Bridge a Python async generator onto Dynamo’s AsyncEngine interface.

`lib/bindings/python/src/dynamo/_core.pyi#L1470`


**Public methods**

**init**

Wrap a Python generator and event loop for use with Dynamo services.

###### RadixTree (class)


A RadixTree that tracks KV cache blocks and can find prefix matches for sequences.

Thread-safe: operations route to a dedicated background thread and long calls release the Python GIL.

`lib/bindings/python/src/dynamo/_core.pyi#L960`


**Public methods**

**init**

Create a new RadixTree instance.

#### find_matches

Find prefix matches for the given sequence of block hashes.

**Parameters**

List of block hashes to find matches for

If True, stop searching after finding the first match

**Returns**

`OverlapScores`

— OverlapScores containing worker matching scores and frequencies

#### apply_event

Apply a KV cache event to update the RadixTree state.

**Parameters**

ID of the worker that generated the event

Serialized KV cache event as bytes

**Raises**

`ValueError`

— If the event bytes cannot be deserialized

#### remove_worker

Remove all blocks associated with a specific worker.

**Parameters**

ID of the worker to remove

#### clear_all_blocks

Clear all blocks for a specific worker.

**Parameters**

ID of the worker whose blocks should be cleared

#### dump_tree_as_events

Dump the current RadixTree state as a list of JSON-serialized KV cache events.

**Returns**

`List[str]`

— List of JSON-serialized KV cache events as strings

###### RoutedEngine (class)


No summary available.

`lib/bindings/python/src/dynamo/llm/__init__.py#L64`


**Public methods**

#### generate

No summary available.

###### RouterConfig (class)


How to route the request

`lib/bindings/python/src/dynamo/_core.pyi#L1692`


**Public methods**

**init**

Create a RouterConfig.

**Parameters**

The router mode (RoundRobin, Random, KV, Direct, LeastLoaded, or DeviceAwareWeighted)

Optional KV router configuration (used when mode is KV)

Threshold percentage (0.0-1.0) for decode blocks busy detection

Literal token count threshold for prefill busy detection

Fraction of max_num_batched_tokens for busy detection

Deprecated and ignored. Routing topology and readiness come from registered worker types.

Router-local session-affinity idle TTL in seconds.

###### RouterMode (class)


Router mode for load balancing requests across workers

###### RouterQueueLimitExceeded (class)


###### RoutingConstraints (class)


Request-side routing constraints.

`required_taints`

is a hard eligibility filter.
`preferred_taints`

maps taint -> signed weight.
Positive weights prefer matching workers, negative weights avoid them,
and `0.0`

is neutral. Matching weights are summed and squashed with
`tanh`

, so opposite preferences cancel before Dynamo converts the
bounded bias into a strictly positive score multiplier.

`lib/bindings/python/src/dynamo/_core.pyi#L913`


**Public methods**

**init**

No summary available.

###### SelectionService (class)


In-process handle to a runtime-free Dynamo selection core.

`lib/bindings/python/src/dynamo/_core.pyi#L727`


**Public methods**

**init**

Create a selection service. `indexer_threads`

sizes the KV indexer pool.

#### shutdown

Stop the service: cancel KV-event listeners and scheduling so that in-flight and queued selections fail fast.

The KV indexer thread pool is released when the handle is dropped. Idempotent, and also runs automatically on drop.

#### upsert_worker

Upsert a worker and subscribe to its live KV events; returns its catalog record.

#### delete_worker

Remove a worker and tear down its KV-event listener; returns its catalog record.

#### list_workers

List catalog records, optionally filtered by model and routing group.

#### ready

Readiness: whether at least one worker is schedulable, plus catalog state.

#### overlap_scores

Per-worker KV-overlap scores for a prompt.

#### select

Select the best worker by KV-overlap + load, without booking.

#### select_and_reserve

Select the best worker and book its load.

#### create_reservation

Book a request’s load against a worker, keyed by `selection_id`

.

Without a `worker_id`

, replays the matching `select`

’s cached
selection (same model/routing-group), booked under `selection_id`

;
other request fields are ignored. With a `worker_id`

and the prompt,
books explicitly under `selection_id`

on that worker and discards any
cached selection for the id. `selection_id`

is required.

#### prefill_complete

Mark a reservation’s prefill complete; its load shifts prefill -> decode.

#### add_output_block

Record one decode output block for a reservation, advancing its decode load.

#### free_reservation

Free a finished reservation, releasing its tracked load.

#### loads

Current per-model active load (pending counts + per-worker potential loads).

#### potential_loads

Per-worker potential loads for a prompt, without booking.

###### WorkerMetricsPublisher (class)


A metrics publisher will provide metrics to the router for load monitoring.

`lib/bindings/python/src/dynamo/_core.pyi#L644`


**Public methods**

**init**

Create a `WorkerMetricsPublisher`

object

#### create_endpoint

Initialize event-plane publishing for worker metrics. Must be awaited.

Extracts component information from the endpoint to set up metrics publishing on the endpoint-scoped event subject used for routing decisions.

**Parameters**

The endpoint to extract component information from for metrics publishing

#### publish

Publish worker metrics for load monitoring.

**Parameters**

Data parallel rank of the worker (None defaults to 0)

Optional scheduler-compatible decode-block signal

Optional authoritative total KV blocks currently in use

###### WorkerType (class)


Processing stage a worker handles.

Each worker has exactly one role; values are not combinable. Use the
`needs`

argument on register_model to express dependencies in DNF form
(a list of alternative AND-sets) — for example, an encode worker that
needs (Prefill AND Decode) OR a single Aggregated peer is expressed as
`[[WorkerType.Prefill, WorkerType.Decode], [WorkerType.Aggregated]]`

.

###### compute_block_hash_for_seq (function)


Compute block hashes for a sequence of tokens, optionally including multimodal metadata.

When block_mm_infos is provided, the mm_hashes are included in the hash computation to ensure that blocks with identical tokens but different multimodal objects produce different hashes.

**Parameters**

List of token IDs

Size of each block in tokens

Optional per-block multimodal metadata. Each element corresponds to a block and should be None or a dict with structure: { “mm_objects”: [ { “mm_hash”: int, # Hash of the MM object } ] }

Optional LoRA adapter name for adapter-aware block hashing.

Optional Eagle mode flag. When true, hashes use overlapping
`kv_block_size + 1`

token windows with `kv_block_size`

stride.

**Returns**

`List[int]`

— List of block hashes (one per block)

>>> tokens = [1, 2, 3, 4] * 8 # 32 tokens = 1 block >>> mm_info = { … “mm_objects”: [{ … “mm_hash”: 0xDEADBEEF, … }] … } >>> hashes = compute_block_hash_for_seq(tokens, 32, [mm_info])

###### fetch_model (function)


Download a model from Hugging Face, returning its local path. If `ignore_weights`

is True, only fetches tokenizer and config files. Example: `model_path = await fetch_model("Qwen/Qwen3-0.6B")`


###### lora_name_to_id (function)


Generate a deterministic integer ID from a LoRA name using blake3 hash.

###### make_engine (function)


###### register_model (function)


Attach the model at path to the given endpoint, and advertise it as model_type. LoRA Registration: The `lora_name`

and `base_model_path`

parameters must be provided together or not at all. Providing only one of these parameters will raise a ValueError. - `lora_name`

: The served model name for the LoRA model - `base_model_path`

: Path to the base model that the LoRA extends

For TensorBased models (using ModelInput.Tensor), HuggingFace downloads are skipped
and a minimal model card is registered directly. Use model_path as the display name
for these models. Pass tensor protocol metadata through `tensor_model_config`

.

Model serving readiness:
`worker_type`

and `needs`

describe the worker’s processing stage and
peer dependencies. `needs`

is a DNF list — each inner list is an
AND-set, the outer list is OR. `worker_type`

is required; backends
declare it literally at each call site.

When `ignore_weights`

is true, remote HuggingFace model resolution skips
weight files and downloads only the metadata needed for registration.

###### run_input (function)


Start an engine, connect it to an input, and run until stopped.

`frontend_route_extensions`

supplies additional HTTP routes to the
frontend (HTTP input only); see `FrontendRoute`

.

###### run_kv_indexer (function)


###### run_select_service (function)


Run the Dynamo selection service with the given arguments.

###### run_slot_tracker (function)


Run the KV router slot tracker with the given arguments.

###### unregister_model (function)


Unregister a model from the discovery system.

If lora_name is provided, unregisters a LoRA adapter instead of a base model.