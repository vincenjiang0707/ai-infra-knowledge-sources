source: https://docs.nvidia.com/dynamo/zh-CN/reference/api/python/_core
lastmod: 2026-09-23T23:30:39.914Z

dynamo._core


dynamo._core

Rust-backed distributed runtime, KV router, and endpoint bindings.

`dynamo._core`

publishes 81 classes and 16 functions. Source: `lib/bindings/python/src/dynamo/_core.pyi`


###### AicEngineConfig (class)


AIC model/backend identity used by native forward-pass estimates.

`lib/bindings/python/src/dynamo/_core.pyi#L1742`


**Public methods**

**init**

No summary available.

###### AicPerfConfig (class)


No summary available.

`lib/bindings/python/src/dynamo/_core.pyi#L1721`


**Public methods**

**init**

No summary available.

###### ApproxKvIndexer (class)


An approximate KV Indexer that doesn’t receive KV cache events from workers. Instead, it relies on routing decisions with TTL-based expiration and pruning to estimate which blocks are cached on which workers.

This is useful when:

- Backend engines don’t emit KV events
- You want to reduce event processing overhead
- Lower routing accuracy is acceptable

`lib/bindings/python/src/dynamo/_core.pyi#L1067`


**Public methods**

**init**

Create an `ApproxKvIndexer`

object

**Parameters**

The component to associate with this indexer

The KV cache block size

TTL for blocks in seconds (default: 120.0)

#### find_matches_for_request

Return the overlapping scores of workers for the given token ids.

**Parameters**

List of token IDs to find matches for

Optional LoRA adapter name for adapter-aware matching

**Returns**

`OverlapScores`

— OverlapScores containing worker matching scores and frequencies

#### block_size

Return the block size of the ApproxKvIndexer.

**Returns**

`int`

— The KV cache block size

#### process_routing_decision_for_request

Notify the indexer that a token sequence has been routed to a specific worker.

This updates the indexer’s internal state to track which blocks are likely cached on which workers based on routing decisions.

**Parameters**

List of token IDs that were routed

The worker ID the request was routed to

The data parallel rank (default: 0)

###### Block (class)


A KV cache block

`lib/bindings/python/src/dynamo/_core.pyi#L2689`


**Public methods**

#### to_list

Get a list of layers

###### BlockList (class)


A list of KV cache blocks

`lib/bindings/python/src/dynamo/_core.pyi#L2739`


**Public methods**

#### to_list

Get a list of blocks

###### BlockManager (class)


A KV cache block manager

`lib/bindings/python/src/dynamo/_core.pyi#L2776`


**Public methods**

**init**

Create a `BlockManager`

object

## Parameters:

worker_id: int The worker ID for this block manager num_layer: int Number of layers in the model page_size: int Page size for blocks inner_dim: int Inner dimension size dtype: Optional[str] Data type (e.g., ‘fp16’, ‘bf16’, ‘fp32’), defaults to ‘fp16’ if None host_num_blocks: Optional[int] Number of host blocks to allocate, None means no host blocks device_num_blocks: Optional[int] Number of device blocks to allocate, None means no device blocks device_id: int CUDA device ID, defaults to 0

#### allocate_host_blocks_blocking

Allocate a list of host blocks (blocking call)

## Parameters:

count: int Number of blocks to allocate

## Returns:

BlockList List of allocated blocks

#### allocate_host_blocks

Allocate a list of host blocks

## Parameters:

count: int Number of blocks to allocate

## Returns:

BlockList List of allocated blocks

#### allocate_device_blocks_blocking

Allocate a list of device blocks (blocking call)

## Parameters:

count: int Number of blocks to allocate

## Returns:

BlockList List of allocated blocks

#### allocate_device_blocks

Allocate a list of device blocks

## Parameters:

count: int Number of blocks to allocate

## Returns:

BlockList List of allocated blocks

###### Cancelled (class)


###### CannotConnect (class)


###### Client (class)


A client capable of calling served instances of an endpoint

`lib/bindings/python/src/dynamo/_core.pyi#L287`


**Public methods**

#### instance_ids

Get list of current instance IDs.

**Returns**

`List[int]`

— A list of currently available instance IDs

#### instances

Get a snapshot of the current instances with full transport details.

Like `instance_ids()`

, the result is a snapshot of the watched
instance set; pair with `wait_for_instances()`

to block until
instances exist.

**Returns**

`List[Instance]`

— A list of`Instance`

for the currently available instances,`List[Instance]`

— across all transports (TCP, NATS, …).

#### wait_for_instances

Wait for instances to be available for work and return their IDs.

**Returns**

`List[int]`

— A list of instance IDs that are available for work

#### wait_for_instance_by_runtime_data

Wait for exactly one instance whose MDC runtime_data contains the given string value.

#### random

Pick a random instance of the endpoint and issue the request

#### round_robin

Pick the next instance of the endpoint in a round-robin fashion

#### direct

Pick a specific instance of the endpoint

#### generate

Generate a response from the endpoint

###### ConnectionTimeout (class)


###### Context (class)


Context wrapper around AsyncEngineContext for Python bindings. Provides tracing and cancellation capabilities for request handling.

`lib/bindings/python/src/dynamo/_core.pyi#L459`


**Public methods**

**init**

Create a new Context instance.

**Parameters**

Optional request ID. If None, a default ID will be generated.

Optional propagated metadata map.

#### is_stopped

Check if the context has been stopped (synchronous).

**Returns**

`bool`

— True if the context is stopped, False otherwise.

#### is_killed

Check if the context has been killed (synchronous).

**Returns**

`bool`

— True if the context is killed, False otherwise.

#### stop_generating

Issue a stop generating signal to the context.

#### id

Get the context ID.

**Returns**

`str`

— The context identifier string.

#### detached

Create a context with a fresh cancellation controller and request ID while preserving trace parentage and a metadata snapshot.

#### async_killed_or_stopped

Asynchronously wait until the context is killed or stopped.

**Returns**

`asyncio.Future[bool]`

— True when the context is killed or stopped.

#### notify_first_token

Fire the first-token signal so the framework can release any deferred `engine.abort()`

. Idempotent; no-op on non-decode requests. Engines normally don’t need this — the framework auto-fires on the first non-empty chunk in the response stream.

#### trace_headers

Build W3C trace headers for propagating to downstream inference engines.

**Returns**

`Optional[dict[str, str]]`

—`{"traceparent": "00-<trace_id>-<span_id>-<flags>"}`

when this`Optional[dict[str, str]]`

— request carries trace context,`None`

otherwise. Also emits`tracestate`

,`Optional[dict[str, str]]`

—`x-request-id`

,`request-id`

when upstream propagated them.`Optional[dict[str, str]]`

— Forward unchanged to the inference engine’s`trace_headers`

kwarg.

#### current_span

Handle on the framework’s `engine.generate`

span. Use it to `set_attribute`

/ `add_event`

/ `set_status`

on the parent span. Returns a silent no-op proxy when no parent was plumbed in (test contexts) or the OTel bridge isn’t installed.

Engines normally reach this through
`dynamo.common.backend.telemetry.current_span(context)`

.

#### start_span

Open a child span under `engine.generate`

with a dynamic name. The returned `SpanProxy`

is a context manager — the span ends on `__exit__`

/ `close()`

/ drop.

Engines normally reach this through
`dynamo.common.backend.telemetry.start_span(context, name)`

.

###### ContextMetadata (class)


Live mutable view over propagated context metadata.

`lib/bindings/python/src/dynamo/_core.pyi#L441`


**Public methods**

#### get

No summary available.

#### pop

No summary available.

#### keys

No summary available.

#### values

No summary available.

#### items

No summary available.

#### clear

No summary available.

#### copy

No summary available.

###### Disconnected (class)


###### DistributedRuntime (class)


The runtime object for dynamo applications

`lib/bindings/python/src/dynamo/_core.pyi#L57`


**Public methods**

#### endpoint

Get an endpoint directly by path.

**Parameters**

Endpoint path in format ‘namespace.component.endpoint’ or ‘dyn://namespace.component.endpoint’

**Returns**

`Endpoint`

— The requested endpoint

**Raises**

`ValueError`

— If path format is invalid (not 3 parts separated by dots)`Exception`

— If namespace or component creation fails

endpoint = runtime.endpoint(“demo.backend.generate”) endpoint = runtime.endpoint(“dyn://demo.backend.generate”)

#### shutdown

Shutdown the runtime by triggering the cancellation token

#### set_health_status

Explicitly set the system-level health status (Ready / NotReady).

#### register_engine_route

Register an async callback for /engine/{route_name} on the system status server.

**Parameters**

The route path (e.g., “control/start_profile” creates /engine/control/start_profile)

Async function with signature: async def(body: dict) -> dict

async def start_profile(body: dict) -> dict: await engine.start_profile(**body) return {“status”: “ok”, “message”: “Profiling started”}

runtime.register_engine_route(“control/start_profile”, start_profile)

The callback receives the JSON request body as a dict and should return a dict that will be serialized as the JSON response.

For GET requests or empty bodies, an empty dict {} is passed.

###### DynamoException (class)


###### Endpoint (class)


An Endpoint is a single API endpoint

`lib/bindings/python/src/dynamo/_core.pyi#L143`


**Public methods**

#### serve_endpoint

Serve an endpoint discoverable by all connected clients at `{{ namespace }}/components/{{ component_name }}/endpoints/{{ endpoint_name }}`


**Parameters**

The request handler function

Whether to wait for inflight requests to complete during shutdown (default: True)

Optional list of metrics labels to add to the metrics

Optional dict containing the health check request payload that will be used to verify endpoint health

#### serve_bidirectional_endpoint

Serve a bidirectional (streaming-input, streaming-output) endpoint.

The handler is an async generator function — `async def generate(request_stream)`

or `async def generate(request_stream, context)`

— so calling it returns an async iterator of response frames
directly (it is not awaited). `request_stream`

is a
`PyAsyncRequestStream`

yielding inbound frames as JSON-like Python
objects; the generator yields response frames as JSON-like Python
objects.

Request-stream end (when `__anext__`

raises `StopAsyncIteration`

)
is not a cancellation signal: the caller has merely stopped sending
input. The engine must keep yielding response chunks until it
chooses to return or observes `context.is_stopped()`

.

**Parameters**

The async generator factory described above

Whether to wait for inflight requests to complete during shutdown (default: True)

Optional list of metrics labels to add to the metrics

#### client

Create a `Client`

capable of calling served instances of this endpoint.

By default this uses round-robin routing when `router_mode`

is not provided.

#### connection_id

Opaque unique ID for this worker. May change over worker lifetime.

#### unregister_endpoint_instance

Unregister this endpoint instance from discovery.

This removes the endpoint from the instances bucket, preventing the router from sending requests to this worker. Use this when a worker is sleeping and should not receive any requests.

#### register_endpoint_instance

Re-register this endpoint instance to discovery.

This adds the endpoint back to the instances bucket, allowing the router to send requests to this worker again. Use this when a worker wakes up and should start receiving requests.

###### EngineCapacity (class)


###### EngineCapacityRequest (class)


Request shape and SLA policy for find_engine_capacity_rps.

`lib/bindings/python/src/dynamo/_core.pyi#L1799`


**Public methods**

**init**

No summary available.

###### EngineConfig (class)


###### EnginePerfLimits (class)


Engine limits used by engine-level helper queries and default correction bounds.

`lib/bindings/python/src/dynamo/_core.pyi#L1766`


**Public methods**

**init**

No summary available.

###### EngineShutdown (class)


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

###### Instance (class)


A read-only view of a single registered instance of an endpoint, wrapping a snapshot of the runtime `Instance`

. `str(instance)`

yields `"namespace/component/endpoint/instance_id"`

.

###### InvalidArgument (class)


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

###### KvIndexer (class)


A KV Indexer that tracks KV Events emitted by workers. Events include add_block and remove_block.

`lib/bindings/python/src/dynamo/_core.pyi#L1029`


**Public methods**

**init**

Create a `KvIndexer`

object

#### find_matches

Find prefix matches for the given sequence of block hashes.

**Parameters**

List of block hashes to find matches for

**Returns**

`OverlapScores`

— OverlapScores containing worker matching scores and frequencies

#### find_matches_for_request

Return the overlapping scores of workers for the given token ids.

#### block_size

Return the block size of the KV Indexer.

###### KvRemovedEventInput (class)


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

###### KvStoredEventInput (class)


###### KvbmRequest (class)


A request for KV cache

`lib/bindings/python/src/dynamo/_core.pyi#L2880`


**Public methods**

**init**

No summary available.

###### Layer (class)


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

###### MockEngineArgs (class)


###### ModelCardInstanceId (class)


Unique identifier for a worker instance: namespace, component, endpoint and instance_id. The instance_id is not currently exposed in the Python bindings.

`lib/bindings/python/src/dynamo/_core.pyi#L383`


**Public methods**

#### triple

Triple of namespace, component and endpoint this worker is serving.

###### ModelDeploymentCard (class)


A model deployment card is a collection of model information

`lib/bindings/python/src/dynamo/_core.pyi#L819`


**Public methods**

#### to_json_str

Serialize the model deployment card to a JSON string.

#### from_json_str

Deserialize a model deployment card from a JSON string.

#### model_type

Return the model type of this deployment card.

#### source_path

Return the source path of this deployment card.

#### local_dir

Resolved metadata directory (post-`download_config`

). Raises ValueError if the path contains non-UTF-8 bytes.

#### name

Return the model name.

#### runtime_config

Return the runtime configuration as a dict.

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

###### OptimizationTarget (class)


###### OverlapScores (class)


A collection of prefix matching scores of workers for a given token ids. ‘scores’ is a map of worker id to the score which is the number of matching blocks.

###### PlannerDecision (class)


A request from planner to client to perform a scaling action. Fields: num_prefill_workers, num_decode_workers, decision_id. -1 in any of those fields mean not set, usually because planner hasn’t decided anything yet. Call VirtualConnectorClient.complete(event) when action is completed.

###### PyAsyncRequestStream (class)


Python-visible inbound iterator handed to bidirectional engine handlers as the first positional argument. Yields request frames as JSON-like Python objects.

Request-stream end is not a cancellation signal: when this iterator
raises `StopAsyncIteration`

, the caller has merely stopped sending
input. The engine should keep yielding response chunks until it
chooses to return or observes `context.is_stopped()`

.

###### PyRuntimeMetrics (class)


Helper class for registering Prometheus metrics callbacks on an Endpoint.

Provides utilities for integrating external metrics (e.g., from vLLM, SGLang, TensorRT-LLM).

`lib/bindings/python/src/dynamo/prometheus_metrics.pyi#L12`


**Public methods**

#### register_prometheus_expfmt_callback

Register a Python callback that returns Prometheus exposition text. The returned text will be appended to the /metrics endpoint output.

This allows you to integrate external Prometheus metrics (e.g. from vLLM) directly into the endpoint’s metrics output.

**Parameters**

A callable that takes no arguments and returns a string in Prometheus text exposition format

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

###### ReasoningConfig (class)


No summary available.

`lib/bindings/python/src/dynamo/_core.pyi#L2031`


**Public methods**

**init**

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

###### RustEnginePerfModel (class)


Engine-level performance model backed by AIC forward-pass modeling.

`lib/bindings/python/src/dynamo/_core.pyi#L1823`


**Public methods**

#### best_available

Build from all available inputs; explicit AIC config is preferred, then engine args, then regression-only.

#### from_regression

Build a regression-only model that learns from observed FPM wall times.

#### from_native

Build a strict native AIC model; unsupported AIC configs raise an error.

#### estimate_forward_pass_time

Estimate one scheduled forward-pass iteration in seconds from current-version FPMs.

#### tune_with_fpms

Tune with current-version observed FPMs: outer list is iterations, inner list is attention-DP ranks.

#### diagnostics

Return AIC diagnostics as a JSON string.

#### get_min_correction_factor

Return the minimum ready native correction factor, or None if no factor is ready.

#### get_max_correction_factor

Return the maximum ready native correction factor, or None if no factor is ready.

#### get_avg_correction_factor

Return the average ready native correction factor, or None if no factor is ready.

#### get_queued_prefill_time

Estimate queued prefill drain time; adjust queued tokens outside the shim for KV reuse.

#### get_scheduled_decode_itl

Estimate scheduled decode ITL in seconds; aggregated workers include scheduled or learned average prefill load.

#### find_engine_capacity_rps

Search sustainable per-engine RPS; inspect eligible to see whether eligible SLA metrics passed.

###### RustEnginePerfOptions (class)


Online tuning options for RustEnginePerfModel.

`lib/bindings/python/src/dynamo/_core.pyi#L1781`


**Public methods**

**init**

No summary available.

###### SelectionCacheConfig (class)


Bounds for the in-flight selection cache. Each field defaults to the service default when omitted.

`lib/bindings/python/src/dynamo/_core.pyi#L713`


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

###### SelectionServiceError (class)


Raised by `SelectionService`

for selector failures that are not malformed input.

###### SglangArgs (class)


No summary available.

`lib/bindings/python/src/dynamo/_core.pyi#L2040`


**Public methods**

**init**

No summary available.

###### SpanProxy (class)


Unified span handle returned by `Context.current_span()`

(the framework auto-span) and `Context.start_span()`

(child spans). Mirrors the OTel `Span`

API: `set_attribute`

/ `add_event`

/ `set_status`

. Usable as a Python context manager (closes on `__exit__`

). All methods are silent no-ops when the underlying span is absent.

`lib/bindings/python/src/dynamo/_core.pyi#L612`


**Public methods**

#### set_attribute

Set an attribute on the span. Any key is accepted; OTel imposes no pre-declaration constraint.

#### add_event

Emit a structured event on the span.

#### set_status

Set the span’s status. `status`

is `"ok"`

or `"error"`

; `description`

is optional context (typically a short error name).

#### close

End the underlying span (child spans only — no-op for the auto-span). Idempotent.

###### StreamIncomplete (class)


###### TransportType (class)


A read-only view of an instance’s transport, wrapping the runtime `TransportType`

. `kind`

is the transport variant (“tcp” / “nats_tcp”) and `address`

is its (transport-specific) address. The address format is not a stable parse target.

###### TrtllmArgs (class)


No summary available.

`lib/bindings/python/src/dynamo/_core.pyi#L2052`


**Public methods**

**init**

No summary available.

###### Unknown (class)


###### VirtualConnectorClient (class)


How a client discovers planner requests and marks them complete

`lib/bindings/python/src/dynamo/_core.pyi#L3272`


**Public methods**

**init**

No summary available.

#### get

No summary available.

#### complete

No summary available.

#### wait

Blocks until there is a new decision to fetch using ‘get’

###### VirtualConnectorCoordinator (class)


Internal planner virtual connector component

`lib/bindings/python/src/dynamo/_core.pyi#L3248`


**Public methods**

**init**

No summary available.

#### async_init

Call this before using the object

#### read_state

Get the current values. Most for test / debug.

#### update_scaling_decision

No summary available.

#### wait_for_scaling_completion

No summary available.

#### is_scaling_ready

Return whether the client acknowledged the current scaling decision.

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

###### backend (class)


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


###### get_reasoning_parser_names (function)


###### get_tool_parser_names (function)


###### log_message (function)


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

###### resolve_routing_image_token_id (function)


Routing-side image-placeholder token id for a model, resolved with the same per-family logic the frontend’s MM-aware KV routing uses. Returns None when the model isn’t in the MM-routing registry or its config can’t be read. Only present when the bindings are built with the `mm-routing`

feature.

###### run_input (function)


Start an engine, connect it to an input, and run until stopped.

`frontend_route_extensions`

supplies additional HTTP routes to the
frontend (HTTP input only); see `FrontendRoute`

.

###### run_kv_indexer (function)


###### run_mocker_synthetic_trace_replay (function)


Replay a synthetic mocker workload without requiring a trace file.

`sla_ttft_ms`

/ `sla_itl_ms`

/ `sla_e2e_ms`

are the goodput SLA bounds
(offline replay only); when any is set the report carries `goodput_*`

keys
classifying SLA-satisfying requests.

`scaling_policy`

is an optional offline callback implementing
`initial_tick_ms() -> float`

and `on_tick(snapshot) -> dict`

. Passing a
policy in online mode raises `ValueError`

.

###### run_mocker_trace_replay (function)


Replay mocker trace files and return the simulation report.

Supports aggregated or disaggregated engine configurations.

When `report_jsonl_path`

is provided (offline disagg replay only), one
JSON object per request is written to that path. Each line includes
arrival/admit/token timestamps, input/output lengths, the full per-token
ITL series, and prefill/decode worker indices.

`sla_ttft_ms`

/ `sla_itl_ms`

/ `sla_e2e_ms`

are the goodput SLA bounds
(offline replay only). When any is set, the report carries `goodput_*`

keys
classifying SLA-satisfying requests; with none set, goodput is omitted.

`scaling_policy`

is an optional offline callback implementing
`initial_tick_ms() -> float`

and `on_tick(snapshot) -> dict`

. Passing a
policy in online mode raises `ValueError`

.

###### run_select_service (function)


Run the Dynamo selection service with the given arguments.

###### run_slot_tracker (function)


Run the KV router slot tracker with the given arguments.

###### unregister_model (function)


Unregister a model from the discovery system.

If lora_name is provided, unregisters a LoRA adapter instead of a base model.