source: https://docs.nvidia.com/dynamo/reference/api/python/common
lastmod: 2026-09-24T19:58:16.636Z

# dynamo.common

`dynamo.common`

publishes 49 classes and 28 functions. Source: `components/src/dynamo/common/__init__.py`


###### AbstractEmbeddingReceiver (class)


Abstract base class for a receiver of precomputed embeddings from the encode worker.

`components/src/dynamo/common/multimodal/embedding_transfer.py#L83`


**Public methods**

#### receive_embeddings

Abstract method to receive precomputed embeddings for a given request ID.

**Parameters**

The TransferRequest object containing information to receive embeddings.

**Returns**

`int`

— A tuple containing the tensor ID and the received embeddings as a torch.Tensor.`torch.Tensor`

— Caller should invoke release_tensor(tensor_id) when the tensor is no longer needed to free up resources.

#### release_tensor

Abstract method to indicate that the tensor associated with the ID is no longer in use. Args: tensor_id: The ID of the tensor to release.

###### AbstractEmbeddingSender (class)


Abstract base class for a sender of precomputed embeddings to the downstream worker.

`components/src/dynamo/common/multimodal/embedding_transfer.py#L114`


**Public methods**

#### send_embeddings

Abstract method to send precomputed embeddings for a given request ID.

**Parameters**

A torch.Tensor of the embeddings to send.

A boolean indicating whether the embeddings should be staged for the transfer,

Returns: A tuple containing the TransferRequest object and an awaitable that can be awaited to indicate the send is completed.

###### AiohttpClient (class)


aiohttp-backed concrete client.

`components/src/dynamo/common/http/aiohttp_client.py#L28`


**Public methods**

**init**

No summary available.

#### close

No summary available.

###### AsyncEncoderCache (class)


Async wrapper with request coalescing over MultimodalEmbeddingCacheManager.

Provides async get_or_compute that deduplicates concurrent requests for the same key, ensuring only one encoding runs at a time per key.

Thread Safety: This class is NOT thread-safe. It is designed to run within a single asyncio event loop. All access must be from the same thread.

`components/src/dynamo/common/multimodal/async_encoder_cache.py#L45`


**Public methods**

**init**

Initialize the async encoder cache.

**Parameters**

Underlying MultimodalEmbeddingCacheManager for storage.

#### get

Synchronous get from underlying cache.

**Parameters**

Cache key.

**Returns**

`Optional[CachedEmbedding]`

— Cached embedding or None if not found.

#### get_or_compute

Get from cache or compute with request coalescing.

If the key is in cache, returns immediately. If another coroutine is already computing this key, waits for that result. Otherwise, computes and caches the result.

**Parameters**

Cache key (typically content hash).

Async function to compute the embedding if not cached.

**Returns**

`CachedEmbedding`

— The cached or computed embedding.

**Raises**

`Exception`

— Re-raises any exception from compute_fn.

###### AudioLoader (class)


Async audio loader for multimodal pipelines.

Delegates URL fetching and decoding to vLLM’s `MediaConnector`

+
`AudioMediaIO`

so that the exact same loading logic runs whether the
request arrives via `vllm serve`

or through Dynamo. Returns
`(waveform, sample_rate)`

tuples at the native sample rate — vLLM’s
model-specific `MultiModalDataParser`

handles resampling and channel
normalization downstream.

Also supports the NIXL decoded variant for frontend-decoded audio transferred via RDMA.

`components/src/dynamo/common/multimodal/audio_loader.py#L74`


**Public methods**

**init**

No summary available.

#### load_audio

Load audio from a URL and return a (waveform, sample_rate) tuple.

Supports http(s), data: URIs, file:// paths, and bare filesystem paths. Audio is loaded at the native sample rate — no resampling is performed.

#### load_audio_batch

Load a batch of audio files from multimodal data items.

Supports two paths:

- Url variant: Download and decode audio via vLLM’s MediaConnector
- Decoded variant: Read pre-decoded audio via NIXL RDMA (requires enable_frontend_decoding=True)

**Returns**

`List[tuple[np.ndarray, float]]`

— List of (waveform, sample_rate) tuples.

###### BaseEngine (class)


Abstract base for all engines — the modality-agnostic lifecycle.

`Worker`

drives every engine through the same lifecycle regardless of
modality; only the request/response shape of `generate`

differs.
That method is therefore declared on the modality-specific subclasses
(`LLMEngine`

for token-based inference, `RawEngine`

for
raw non-token media generation), not here.

Lifecycle:

- from_args(argv) — parse CLI args, return (engine, WorkerConfig)
- start() — start the engine, return EngineConfig metadata. After start() returns, generate() MUST be ready to accept calls. Worker begins serving immediately after start().
- generate() — called for each request (concurrent calls expected)
- abort() — called when a request is cancelled (optional, default no-op)
- cleanup() — called once on shutdown, release all resources

`components/src/dynamo/common/backend/engine.py#L151`


**Public methods**

#### from_args

Parse CLI args and construct the engine (not yet started).

**Parameters**

Command-line arguments. `None`

means `sys.argv[1:]`

.

**Returns**

`tuple[BaseEngine, WorkerConfig]`

— A`(engine, worker_config)`

pair.

#### start

Start the engine and return registration metadata.

After this returns the engine MUST be ready to accept `generate()`

calls. `Worker`

will register the model and begin serving
immediately.

`worker_id`

is an opaque, runtime-allocated unique identifier for
this worker. It is stable from `start()`

onward for the worker’s
lifetime and unique across replicas in the cluster. Engines that
need a per-worker key for cluster-wide bookkeeping should derive it
from this value rather than hashing host/pid or asking operators for a
CLI override. The internal mechanism (discovery instance ID) is not
part of the contract — engines should treat it as opaque.

#### abort

Abort an in-flight request (optional, default no-op).

Called by Worker when the client disconnects or the request is cancelled. Override to release engine resources (KV cache, scheduler slots, etc.).

`context.metadata`

in this callback reflects the original
propagated request metadata snapshot. Mutations made to
`context.metadata`

during `generate`

are not visible here.

#### is_quiescent

Whether in-flight KV transfers are done, so `cleanup`

may release GPU memory. The Rust `Worker`

polls this on prefill workers between the grace period and `cleanup`

:

`True`

— quiescent; exit the drain loop now.`False`

— busy; poll again next tick.`None`

— no introspection (default); poll until the drain budget (`DYN_PREFILL_DRAIN_TIMEOUT_S`

) expires. Never frees KV early.

Aggregated/decode workers are never polled. Override only if the engine can observe transfer completion.

#### cleanup

Release all engine resources.

`Worker`

guarantees:

`cleanup()`

runs after a successful`start()`

on shutdown — the common case.`cleanup()`

also runs after`start()`

raised, on the partial state the engine may have allocated before failing (inner LLM handle, sockets, background tasks). Implementations**must**be null-safe: guard each resource with an`is None`

check so a partially constructed engine can be released without raising.`cleanup()`

is**not**called when`start()`

was never invoked (e.g. pre-start shutdown). Engines whose constructors allocate resources should release them via`__del__`

/ context-manager semantics rather than rely on`cleanup()`

.

`cleanup()`

is never invoked concurrently with `start()`

or
another `cleanup()`

— `Worker`

’s state machine serializes
those transitions. The conformance kit asserts that a second
`cleanup()`

call after a successful first is a safe no-op.

#### register_prometheus

Bridge a vendor-prefixed Prometheus registry into the runtime’s `/metrics`

output via `metrics.add_expfmt_callback`

. Default no-op. See `dynamo.common.backend.metrics`

for helpers. Do not retain `metrics`

past return.

Framework-owned lifecycle + per-rank gauges
(`dynamo_component_{cleanup_time_seconds,drain_time_seconds,model_load_time_seconds,total_blocks,gpu_cache_usage_percent,kv_cache_hit_rate}`

)
are owned and registered by the framework Rust-side — they do NOT
require the engine to implement this method.

#### component_metrics_dp_ranks

Declare the data-parallel ranks this engine publishes per-rank snapshots for. Empty (default) opts out.

Stable for the engine’s lifetime. `Worker`

constructs a
`SnapshotPublisher`

sized to these ranks and hands it
back via `attach_snapshot_publisher`

. The engine then
calls `publisher.publish(rank, snap)`

from its stat-logger
thread — event-driven, no polling.

`ComponentSnapshot.kv_cache_hit_rate`

is tri-state:
`None`

means “no data yet” or “no prefix cache” (gauge
skipped), `0.0`

is a legitimate measurement (zero hits).

#### attach_snapshot_publisher

Framework hands the engine the Rust-owned `SnapshotPublisher`

once, after `setup_metrics`

constructed it from `component_metrics_dp_ranks`

. Stash the reference; call `publisher.publish(rank, snap)`

from your stat-logger thereafter.

Only invoked when `component_metrics_dp_ranks`

returns
non-empty. Default is no-op so engines that opt out don’t need
to override.

#### health_check_payload

Canary payload the runtime sends through `generate`

when the endpoint is idle. Return `None`

(default) to disable active probing. `Worker`

calls this once after `start`

and resolves `DYN_HEALTH_CHECK_PAYLOAD`

/ `--health-check-payload`

overrides on top.

#### supported_controls

Return the set of engine-control capability keys this engine supports.

Controls are semantic operations on the engine’s serving lifecycle. Engines advertise the keys they implement.

#### engine_control

Handle one advertised engine-control request.

#### supported_updates

Return the set of engine-update capability keys this engine supports.

Updates are a sibling surface to `supported_controls`

for
operations that mutate engine-managed assets rather than the engine’s
serving lifecycle. Engines advertise the keys they implement.

#### engine_update

Handle one advertised engine-update request.

#### on_endpoint_ready

Receive the runtime serving `Endpoint`

once, before serving begins.

Default no-op. Engines that publish their own discovery records stash
it for use from `engine_update`

. `Worker`

calls this exactly
once; a raised exception is fatal to startup.

###### DiffusionEngine (class)


A `RawEngine`

for diffusion-family generation (image/video via VisualGen, DiffGenerator). Names the family only — non-diffusion raw modalities (e.g. TTS audio) subclass `RawEngine`

directly. Routing keys off `RawEngine`

, so any subclass uses the raw adapter.

###### DisaggregationMode (class)


###### EmbeddingTransferMode (class)


###### EngineConfig (class)


Registration metadata returned by an engine’s `start`

.

The neutral fields (`model`

, `served_model_name`

, `runtime_data`

)
apply to every modality; token-pipeline metadata lives in the optional
`llm`

sub-record, which raw media engines leave `None`

.

`components/src/dynamo/common/backend/engine.py#L134`


**Public methods**

**init**

No summary available.

###### EngineHealthMonitorConfig (class)


No summary available.

`components/src/dynamo/common/engine_monitor.py#L40`


**Public methods**

#### from_env

No summary available.

**init**

No summary available.

###### ForwardPassMetrics (class)


Per-iteration metrics emitted by InstrumentedScheduler.

One message is emitted per scheduler iteration (one per forward pass). An idle heartbeat (all zeros, wall_time=0) is emitted once when the engine transitions from active to idle.

###### GenerateChunk (class)


Single chunk yielded by `LLMEngine.generate()`

.

Every chunk must include `token_ids`

and `index`

.
Use `index=0`

for single-choice responses. The final chunk must
additionally include `finish_reason`

; `completion_usage`

is
optional (the OpenAI frontend aggregates it when present, and
matches the Rust `Option<CompletionUsage>`

/
`skip_serializing_if = "Option::is_none"`

semantics).

Prefill terminals carry `disaggregated_params`

for the
PrefillRouter to forward to the decode peer. When the caller
requested logprobs, chunks may also carry `log_probs`

and
`top_logprobs`

aligned to `token_ids`

— see
`dynamo.common.backend.logprobs`

.

Encode terminals carry `encoder_result`

(an opaque object the
frontend forwards onto the downstream
`PreprocessedRequest.encoder_result`

). Construct with
`dynamo.common.backend.multimodal.encoder_terminal_chunk`

.

###### GenerateRequest (class)


Inbound request dict passed to `LLMEngine.generate()`

.

`token_ids`

is always present (set by the Rust preprocessor).
The remaining groups are optional — engines should access them
defensively with `.get(key, {})`

.

Disaggregated-serving keys (`prefill_result`

, `bootstrap_info`

)
are set by the frontend’s PrefillRouter on decode requests; engines
read them via `dynamo.common.backend.disagg`

helpers.

Multimodal keys (`multi_modal_data`

, `mm_processor_kwargs`

,
`mm_routing_info`

) are populated by the frontend preprocessor when
the request carries media. `encoder_result`

is set by the
frontend when forwarding a request from an Encode worker
to a downstream Prefill/Aggregated peer; engines read it via
`dynamo.common.backend.multimodal.require_encoder_result`

. All
four are object-shaped (`dict`

) by contract.

`model`

carries the requested model name (set by the Rust
preprocessor). Engines that support dynamic LoRA read it to route a
request to a loaded adapter.

###### HttpClient (class)


Backend-neutral HTTP client.

Subclasses own a backend-specific session/client singleton on the
instance. Callers reach the public surface via `fetch_bytes`

and the unified exception classes above; the concrete backend type
is invisible past instantiation.

`components/src/dynamo/common/http/base.py#L50`


**Public methods**

**init**

No summary available.

#### fetch_bytes

Fetch `url`

and return the response body.

Single-shot: no retries. Raises one of the unified exception classes above; callers never see native httpx/aiohttp classes.

`policy=None`

: use the backend’s built-in redirect handling.

`policy`

set: follow redirects manually and revalidate each
hop against the policy via `url_validator.validate_url`

.
This is the SSRF-safe path; raises `UrlValidationError`

if any hop fails or the chain exceeds `_MAX_REDIRECTS`

.

#### close

Close the backend session/client. Idempotent.

###### HttpConnectionError (class)


Network-layer failure: DNS, refused, reset, half-close.

###### HttpError (class)


###### HttpStatusError (class)


Server responded with a non-2xx status.

`components/src/dynamo/common/http/base.py#L40`


**Public methods**

**init**

No summary available.

###### HttpTimeoutError (class)


###### HttpxClient (class)


httpx-backed concrete client.

`components/src/dynamo/common/http/httpx_client.py#L36`


**Public methods**

**init**

No summary available.

#### close

No summary available.

###### ImageLoader (class)


No summary available.

`components/src/dynamo/common/multimodal/image_loader.py#L59`


**Public methods**

**init**

Initialize the ImageLoader with caching, HTTP settings, and optional NIXL config for receiving frontend decoding.

**Parameters**

Maximum number of images to store in the in-memory LRU cache. Defaults to CACHE_SIZE_MAXIMUM.

Timeout in seconds for HTTP requests when fetching remote images. Defaults to 30.0 seconds.

If True, enables NIXL RDMA for transferring decoded images directly from frontend memory, bypassing standard network transport. Defaults to False.

Policy for validating URLs. Defaults to UrlValidationPolicy.from_env().

#### load_image

No summary available.

#### load_image_batch

Load a batch of images from multimodal data items.

Supports three paths:

- Url variant: Download and decode image from URL (default)
- Decoded variant: Read pre-decoded image via NIXL RDMA (requires enable_frontend_decoding=True)
- UuidOnly variant: Preserve an aligned empty slot for backend cache lookup when preserve_uuid_slots=True

**Parameters**

List of multimodal data items for images

Allow UUID-only items and preserve their positions as None. This is enabled only by backends that resolve such slots.

**Returns**

`list[Any]`

— Loaded images, with None for UUID-only cache slots

**Raises**

`HttpStatusError`

— If any image fails with an HTTP status error (e.g. 415 Unsupported Media Type); the status is preserved so the frontend returns the correct client-error code instead of 500.`UrlValidationError`

— If a media URL is rejected by the SSRF policy; preserved as a ValueError so the frontend returns a 4xx, not 500.`Exception`

— If any image fails to load for any other reason`ValueError`

— If enable_frontend_decoding=True but nixl_connector is None`ValueError`

— If a UUID-only slot is received without opting in

###### LLMEngine (class)


Abstract base for token-based inference engines.

The token pipeline: the Rust preprocessor tokenizes the prompt and sets
`token_ids`

on the request; `generate`

yields token chunks that
the Rust postprocessor detokenizes. Registered with
`ModelInput.Tokens`

and served through the token request adapter.

`components/src/dynamo/common/backend/engine.py#L344`


**Public methods**

#### generate

Yield streaming response chunks for a single request.

Called concurrently for multiple in-flight requests.

Each chunk: `{"token_ids": [...], "index": 0}`

Final chunk must include: `{"token_ids": [...], "index": 0, "finish_reason": "...", "completion_usage": {...}}`


#### kv_event_sources

KV event sources, one per data-parallel rank. Default opts out of KV-aware routing. `Worker`

calls once after `start`

.

#### logits_processor_spec

Return backend-neutral logits-processor activation data.

The default opts out. An engine that overrides this method resolves
and caches the specification during startup, then passes it to
`logits_processors_for_request`

from `generate`

. The
engine integration remains responsible for realizing each entry into
its inference library’s processor type.

###### LlmRegistration (class)


Token-pipeline registration metadata (KV cache, data-parallel layout, disaggregation bootstrap). Set by `LLMEngine`

s; `RawEngine`

s leave `EngineConfig.llm`

`None`

. A `None`

field isn’t advertised (the router falls back to its defaults).

`components/src/dynamo/common/backend/engine.py#L108`


**Public methods**

**init**

No summary available.

###### LoRAInfo (class)


Metadata for a loaded LoRA adapter.

`components/src/dynamo/common/lora/manager.py#L123`


**Public methods**

**init**

No summary available.

###### LoRAManager (class)


Minimal Python wrapper around Rust core with extension points.

The manager uses the Rust-based LoRADownloader for local, S3, and Hugging Face sources, and allows registering custom Python sources for other protocols.

`components/src/dynamo/common/lora/manager.py#L36`


**Public methods**

**init**

Initialize LoRA manager.

**Parameters**

Optional custom cache path. If not provided, uses DYN_LORA_PATH env var.

#### register_custom_source

Register a custom Python source for a URI scheme.

**Parameters**

URI scheme without ”://” (e.g., “hf” for hf:// URIs)

LoRA source implementing LoRASourceProtocol

#### download_lora

Download LoRA if needed, return local path.

The source is inferred from the URI scheme:

- file:// -> Local filesystem (Rust)
- s3:// -> S3 (Rust)
- hf:// -> Hugging Face Hub (Rust)
- Custom schemes -> Registered Python sources

**Parameters**

Source URI (file://, s3://, hf://, or custom scheme)

**Returns**

`Dict[str, Any]`

— Dictionary with: - status: “success” or “error” - local_path: Local path to LoRA (if successful) - message: Error message (if error)

#### is_cached

Check if LoRA is already cached locally.

###### LoRASourceProtocol (class)


Protocol for custom Python LoRA sources. Users can implement this to add custom sources.

`components/src/dynamo/common/lora/manager.py#L21`


**Public methods**

#### download

Download LoRA to dest_path, return actual path

#### exists

Check if LoRA exists in this source

###### LocalEmbeddingReceiver (class)


Receiver that reads embeddings from a local file path provided in the serialized request.

`components/src/dynamo/common/multimodal/embedding_transfer.py#L203`


**Public methods**

**init**

No summary available.

#### receive_embeddings

Receive precomputed embeddings for a given request ID.

**Parameters**

The TransferRequest object containing information to receive embeddings for.

**Returns**

`int`

— A tuple containing the tensor ID and the received embeddings as a torch.Tensor.`torch.Tensor`

— Caller should invoke release_tensor(tensor_id) when the tensor is no longer needed to free up resources.

#### release_tensor

Indicate that the tensor associated with the ID is no longer in use.

**Parameters**

The ID of the tensor to release.

###### LocalEmbeddingSender (class)


Sender that saves embeddings to a local file and sends the file path as the serialized request.

`components/src/dynamo/common/multimodal/embedding_transfer.py#L136`


**Public methods**

**init**

No summary available.

#### save_embeddings_to_file

Save the embeddings to a local file and return the file path.

**Parameters**

A unique key for the embeddings.

A torch.Tensor of the embeddings to save.

Returns: The file path where the embeddings are saved.

#### send_embeddings

Send precomputed embeddings for a given request ID.

**Parameters**

A torch.Tensor of the embeddings to send.

A boolean indicating whether the embeddings should be staged for the transfer,

Returns: A tuple containing the TransferRequest object and an awaitable that can be awaited to indicate the send is completed.

###### MetadataUploader (class)


No summary available.

`components/src/dynamo/common/metadata_upload.py#L141`


**Public methods**

#### from_settings

No summary available.

#### from_backend_request

No summary available.

#### upload_choice

No summary available.

**init**

No summary available.

###### MultimodalEmbeddingCacheManager (class)


LRU cache for encoder embeddings.

Stores tensors keyed by content hash with automatic eviction when capacity is exceeded.

Thread Safety: This class is NOT thread-safe. It is designed to run within a single thread (e.g., an asyncio event loop). All access must be from the same thread to avoid race conditions. This is intentional to keep the implementation simple and avoid locking overhead.

`components/src/dynamo/common/memory/multimodal_embedding_cache_manager.py#L43`


**Public methods**

**init**

Initialize the encoder cache.

**Parameters**

Maximum cache capacity in bytes.

#### get

Get a cached embedding from the cache.

If found, the entry is moved to the end (most recently used).

**Parameters**

Cache key (typically content hash).

**Returns**

`Optional[CachedEmbedding]`

— The cached embedding, or None if not found.

#### keys

Return the current cache keys in LRU order.

#### set

No summary available.

#### set_with_delta

Store a cached embedding in the cache.

If the key already exists, the old value is replaced. If adding the entry would exceed capacity, LRU entries are evicted. If the tensor itself is larger than capacity, it is not stored.

**Parameters**

Cache key (typically content hash).

CachedEmbedding to cache.

**Returns**

`CacheMutation`

— CacheMutation describing whether the entry was stored plus the`CacheMutation`

— authoritative add/remove delta caused by this mutation.

###### NixlReadEmbeddingReceiver (class)


NIXL READ based embedding transfer receiver.

Uses nixl_connect.Connector which now natively provides a shared singleton Connection (NIXL agent) and reference-counted Remote agent lifecycle.

`components/src/dynamo/common/multimodal/embedding_transfer.py#L852`


**Public methods**

**init**

No summary available.

#### receive_embeddings

Receive precomputed embeddings for a given request ID.

**Parameters**

The TransferRequest object containing information to receive embeddings for.

**Returns**

`int`

— A tuple containing the tensor ID and the received embeddings as a torch.Tensor.`torch.Tensor`

— Caller should invoke release_tensor(tensor_id) when the tensor is no longer needed to free up resources.

#### release_tensor

Indicate that the tensor associated with the ID is no longer in use.

**Parameters**

The ID of the tensor to release.

###### NixlReadEmbeddingSender (class)


NIXL READ based embedding transfer sender.

Uses nixl_connect.Connector which now natively provides a shared singleton Connection (NIXL agent) and reference-counted Remote agent lifecycle.

`components/src/dynamo/common/multimodal/embedding_transfer.py#L795`


**Public methods**

**init**

No summary available.

#### send_embeddings

Send precomputed embeddings.

**Parameters**

A torch.Tensor of the embeddings to send.

A boolean indicating whether the embeddings should be staged for the transfer,

Returns: A tuple containing the TransferRequest object and an awaitable that can be awaited to indicate the send is completed.

###### NixlWriteEmbeddingReceiver (class)


Counter part of ‘NixlWriteEmbeddingSender’, see ‘NixlWriteEmbeddingSender’ for details. The receiver manages a ring buffer for sender to write the embeddings into, and respond to the sender’s transfer request with the buffer information for the WRITE transfer.

`components/src/dynamo/common/multimodal/embedding_transfer.py#L635`


**Public methods**

**init**

No summary available.

#### receive_embeddings

Receive precomputed embeddings for a given request ID.

**Parameters**

The TransferRequest object containing information to receive embeddings for.

Maximum time to wait for the transfer to complete before raising a TimeoutError.

**Returns**

`int`

— A tuple containing the tensor ID and the received embeddings as a torch.Tensor.`torch.Tensor`

— Caller should invoke release_tensor(tensor_id) when the tensor is no longer needed to free up resources.

#### release_tensor

Indicate that the tensor associated with the ID is no longer in use.

**Parameters**

The ID of the tensor to release.

###### NixlWriteEmbeddingSender (class)


NIXL WRITE-based implementation of the embedding sender interface.

Designed for scenarios where the sender transmits dynamically allocated tensors. Because these tensors allocation is external to the sender, NIXL memory registration will perform on each send request. The receiver will manage a pre-allocated buffer, so its NIXL metadata is consistent once initialized. In such acenarios, let sender initiate the WRITE operations requires minimal metadata exchange.

Protocol:

- Record the receiver NIXL metadata, this is done:

- Implicitly through the first transfer request as fallback if the metadata hasn’t been recorded.
- [REMOVED] Explicitly through add_agent() API before calling send_embeddings(). The receiver provides get_agent_metadata() API to return its NIXL metadata. This complicates the implementation and add extra responsiblity on the caller side, will revisit the necessity if metadata exchange overhead is significant.

- The sender prepares the embeddings and produces a TransferRequest containing sender contact and tensor metadata (shape, dtype, size, etc).
- The receiver responds with (optional) receiver contact, target tensor metadata (buffer address, device, etc) and done signal through NIXL notification.
- The sender performs a NIXL WRITE to push the data into the receiver’s buffer.

`components/src/dynamo/common/multimodal/embedding_transfer.py#L376`


**Public methods**

**init**

No summary available.

#### send_embeddings

Send precomputed embeddings.

**Parameters**

A torch.Tensor of the embeddings to send.

A boolean indicating whether the embeddings should be staged for the transfer,

Returns: A tuple containing the TransferRequest object and an awaitable that can be awaited to indicate the send is completed.

###### NvCreateVideoRequest (class)


Request for video generation (/v1/videos endpoint).

Matches Rust NvCreateVideoRequest in lib/llm/src/protocols/openai/videos.rs.

`components/src/dynamo/common/protocols/video_protocol.py#L50`


###### NvVideosResponse (class)


Response structure for video generation.

Matches Rust NvVideosResponse in lib/llm/src/protocols/openai/videos.rs.

`components/src/dynamo/common/protocols/video_protocol.py#L107`


###### OnceLock (class)


No summary available.

`components/src/dynamo/common/lora/once.py#L15`


**Public methods**

**init**

No summary available.

#### get_or_init

No summary available.

#### get

No summary available.

###### QueuedRequestMetrics (class)


Metrics for requests waiting in the queue (not scheduled this iteration).

All token counts here are raw totals — prefix cache effects are unknown until a request is actually scheduled.

###### RLAdminValidationError (class)


Validation error whose message can be returned directly to RL clients.

###### RLRouteRegistry (class)


Registry for worker RL admin route descriptors.

`components/src/dynamo/common/rl/admin.py#L88`


**Public methods**

**init**

No summary available.

#### add_route

No summary available.

#### add_routes

No summary available.

#### describe

No summary available.

#### dispatch

No summary available.

#### dispatch_stream

No summary available.

###### RawEngine (class)


Engines for raw, non-token generation (image, video, audio).

Named for the *contract*, not a use case: unlike `LLMEngine`

there
is no token pipeline — the frontend forwards the OpenAI-shaped request as a
JSON object and `generate`

yields the response object(s) directly.
Registered with `ModelInput.Text`

and served through the raw request
adapter (no tokenization or KV cache). The `dict`

contract is
modality-neutral, so a new media modality is a new engine, not a new
framework path; one engine may serve several modalities. Yield one
(terminal) object, or intermediate progress objects ending with a terminal
one. Subclasses like `DiffusionEngine`

add no contract.

`components/src/dynamo/common/backend/engine.py#L394`


**Public methods**

#### generate

Yield response object(s) for a single raw-media request.

`request`

is the raw OpenAI-shaped request body (see
`RawRequest`

); yield the response body object(s) (see
`RawResponseChunk`

). For non-streaming modalities yield exactly
one (terminal) object; for streaming modalities yield intermediate
progress objects ending with the terminal one.

###### ScheduledRequestMetrics (class)


Metrics for requests scheduled in this iteration

###### TransferRequest (class)


Data class for transfer requests containing necessary information for embedding transfer.

`components/src/dynamo/common/multimodal/embedding_transfer.py#L73`


###### UnsupportedFpmVersionError (class)


Raised when a ForwardPassMetrics message has an unrecognised version.

###### VideoData (class)


Video data in response.

Matches Rust VideoData in lib/llm/src/protocols/openai/videos.rs.

`components/src/dynamo/common/protocols/video_protocol.py#L91`


###### VideoLoader (class)


No summary available.

`components/src/dynamo/common/multimodal/video_loader.py#L89`


**Public methods**

**init**

No summary available.

#### load_video

No summary available.

#### load_video_batch

No summary available.

###### WelfordAccumulator (class)


Welford’s online algorithm for count / sum / population-variance.

Numerically stable single-pass computation — avoids catastrophic cancellation that sum-of-squares can suffer with large values.

Usage

`components/src/dynamo/common/forward_pass_metrics.py#L48`


**Public methods**

**init**

No summary available.

#### add

No summary available.

#### variance

No summary available.

###### Worker (class)


Drive the Rust `Worker`

for a single engine instance.

Accepts any `BaseEngine`

— an `LLMEngine`

(token pipeline)
or a `DiffusionEngine`

(raw media pipeline). The request adapter is
selected from the engine kind (`raw=isinstance(engine, RawEngine)`

);
`WorkerConfig.model_input`

is validated against that kind.

`components/src/dynamo/common/backend/worker.py#L217`


**Public methods**

**init**

No summary available.

#### run

No summary available.

###### WorkerConfig (class)


No summary available.

`components/src/dynamo/common/backend/worker.py#L101`


**Public methods**

#### from_runtime_config

Build from any object that carries DynamoRuntimeConfig fields.

**init**

No summary available.

###### add_config_dump_args (function)


Add arguments to the parser to dump the config to a file.

**Parameters**

The parser to add the arguments to

`components/src/dynamo/common/config_dump/config_dumper.py#L159`


###### close_http_client (function)


Close the active singleton. Idempotent. Safe across resets.

Clears the resolved client so a fresh env-var reading happens on
the next call (primarily useful in tests that vary
`DYN_HTTP_BACKEND`

).

###### decode (function)


Decode a ForwardPassMetrics message, returning None for unknown versions.

Returns None (and logs a warning) if the message cannot be decoded or carries a version this code does not understand, so callers can simply skip unsupported messages without crashing.

###### dump_config (function)


Dump the configuration to a file or stdout.

If dump_config_to is not provided, the config will be logged to stdout at VERBOSE level.

**Parameters**

Optional path to dump the config to. If None, logs to stdout.

The configuration object to dump (must be JSON-serializable).

`components/src/dynamo/common/config_dump/config_dumper.py#L72`


###### encode (function)


###### env_bool (function)


Parse a boolean environment variable using Dynamo’s common true values.

###### fetch_bytes (function)


Singleton-backed convenience wrapper over `HttpClient.fetch_bytes`

.

###### fetch_model (function)


###### fetch_model_in_subprocess (function)


Fetch a model in a short-lived process before snapshotting.

###### first_endpoint_response (function)


Return the first response from an async-generator endpoint handler.

The generator is explicitly closed before returning so handlers that hold resources across their yield (e.g. load_lora/unload_lora holding a per-LoRA lock) release them promptly rather than waiting for garbage collection.

###### get_config_dump (function)


Collect comprehensive config information about a backend instance.

**Parameters**

Any JSON-serializable object containing the backend configuration.

Optional dict of additional information to include in the dump.

**Returns**

`str`

— JSON string containing comprehensive information.

Returns error information if collection fails, ensuring some diagnostic data is always available.

`components/src/dynamo/common/config_dump/config_dumper.py#L108`


###### get_default_client (function)


Return the process-wide singleton client, instantiating on first call.

###### get_environment_vars (function)


Get relevant environment variables based on prefixes.

**Parameters**

List of environment variable prefixes to capture. If None, uses DEFAULT_ENV_PREFIXES.

If False, redacts values of potentially sensitive variables. Default is False for security.

Set of specific variable names to include regardless of prefix.

**Returns**

`Dict[str, str]`

— Dictionary of environment variable names to values.`Dict[str, str]`

— Sensitive values are replaced with “<REDACTED>” unless include_sensitive is True.

**Examples**

###### get_fs (function)


Initialize fsspec filesystem for the given URL.

**Parameters**

The URL of the filesystem to initialize. e.g. s3://bucket, gs://bucket, file:///local/path

**Returns**

`DirFileSystem`

— The initialized DirFileSystem wrapper for the filesystem.`DirFileSystem`

— fs.fs.protocol to get the protocol of the filesystem`DirFileSystem`

— fs.path to get the bucket or root path`DirFileSystem`

— path to the object in the filesystem - f”{fs.fs.protocol}://{fs.path}/{path}”

###### get_gpu_info (function)


Get GPU information if available.

**Returns**

`Optional[Dict[str, Any]]`

— Dictionary containing GPU details if available, None otherwise.`Optional[Dict[str, Any]]`

— Attempts to use nvidia-smi via subprocess with XML output format.

This is a best-effort function and returns None if GPU info cannot be obtained.

###### get_lora_manager (function)


Return the LoRAManager singleton, or None when DYN_LORA_ENABLED is unset.

Initializes on first call. Initialization errors propagate to the caller — OnceLock does not cache failures, so subsequent calls will retry.

###### get_media_url (function)


Build a public URL for a file stored in the media filesystem.

**Parameters**

The DirFileSystem returned by `get_fs()`

.

Relative path within the filesystem (e.g. “videos/req-id.mp4”).

Optional CDN / proxy base URL. When set, the returned URL is
`{base_url}/{storage_path}`

. When *None*, the URL is constructed
from the filesystem’s protocol and root path.

**Returns**

`str`

— Public URL string for the uploaded file.

###### get_native_offloading_capacity_tokens (function)


Read native offloading capacity from a worker’s runtime metadata.

###### get_runtime_info (function)


Get Python runtime information.

**Returns**

`Dict[str, Any]`

— Dictionary containing Python version, executable path, and command-line arguments.

Gracefully handles errors by returning partial information.

###### get_system_info (function)


Get comprehensive system information.

**Returns**

`Dict[str, Any]`

— Dictionary containing platform, architecture, processor, hostname,`Dict[str, Any]`

— and operating system details.

Gracefully handles errors by returning partial information.

###### main (function)


###### native_offloading_capacity (function)


Build runtime metadata from an authoritative backend token capacity.

###### register_encoder (function)


Decorator to register custom encoders for specific types.

Usage: @register_encoder(MyClass) def encode_my_class(obj: MyClass): return {“field”: obj.field}

`components/src/dynamo/common/config_dump/config_dumper.py#L209`


###### register_rl_routes (function)


Register worker system routes and optionally expose route descriptors.

###### require_lora_load_request (function)


###### require_lora_unload_request (function)


###### run (function)


###### upload_to_fs (function)


Upload bytes to the media filesystem and return the public URL.

This is the canonical helper for all backends (vLLM, SGLang, TRT-LLM) to store generated images/videos and produce a response URL.

**Parameters**

The DirFileSystem returned by `get_fs()`

.

Relative path within the filesystem (e.g. “images/req-id/file.png”).

Raw bytes to upload.

Optional CDN / proxy base URL for URL rewriting.

**Returns**

`str`

— Public URL string for the uploaded file.