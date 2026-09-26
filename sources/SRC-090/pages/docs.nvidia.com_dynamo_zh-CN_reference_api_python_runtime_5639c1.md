source: https://docs.nvidia.com/dynamo/zh-CN/reference/api/python/runtime
lastmod: 2026-09-23T23:30:39.914Z

# dynamo.runtime

Decorators and re-exports for defining Dynamo workers and endpoints.

`dynamo.runtime`

publishes 7 classes and 10 functions. Source: `lib/bindings/python/src/dynamo/runtime/__init__.py`


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

###### LogHandler (class)


Custom logging handler that sends log messages to the Rust env_logger

`lib/bindings/python/src/dynamo/runtime/logging.py#L28`


**Public methods**

#### emit

Emit a log record

###### PyAsyncRequestStream (class)


Python-visible inbound iterator handed to bidirectional engine handlers as the first positional argument. Yields request frames as JSON-like Python objects.

Request-stream end is not a cancellation signal: when this iterator
raises `StopAsyncIteration`

, the caller has merely stopped sending
input. The engine should keep yielding response chunks until it
chooses to return or observes `context.is_stopped()`

.

###### VllmColorFormatter (class)


Formatter that matches Rust tracing’s compact colored output style.

Used for vLLM logs routed through a StreamHandler (bypassing the Rust bridge) so that VLLM_LOGGING_LEVEL is respected independently of DYN_LOG while still producing visually consistent colored output.

`lib/bindings/python/src/dynamo/runtime/logging.py#L65`


**Public methods**

#### format

No summary available.

###### configure_dynamo_logging (function)


A single place to configure logging for Dynamo.

###### configure_logger (function)


Called once to configure the Python logger to use the LogHandler

###### configure_sglang_logging (function)


SGLang allows us to create a custom logging config file

###### configure_vllm_logging (function)


Configure vLLM logging for the main process and subprocesses.

Main process: replaces vLLM’s StreamHandler with a new StreamHandler that uses VllmColorFormatter and writes directly to stderr. This bypasses the Rust LogHandler bridge so that VLLM_LOGGING_LEVEL is respected independently of DYN_LOG (the Rust bridge filters based on DYN_LOG).

Subprocesses (EngineCore, workers): use vLLM’s DEFAULT_LOGGING_CONFIG (StreamHandler to stderr) since the Rust runtime is not initialized there. Setting VLLM_CONFIGURE_LOGGING=1 without VLLM_LOGGING_CONFIG_PATH causes vLLM to use its built-in default config in spawned subprocesses.

The dyn_level param is kept for signature compatibility but does not control the vLLM logger level. Use VLLM_LOGGING_LEVEL env var instead.

###### construct_formatter_prefix (function)


###### dynamo_endpoint (function)


###### dynamo_worker (function)


Decorator that creates a DistributedRuntime and passes it to the worker function.

**Parameters**

Deprecated. NATS enablement is now determined automatically from the event-plane configuration. This parameter is accepted for backwards compatibility but will be removed in a future release.

###### get_bool_env_var (function)


###### log_level_mapping (function)


The DYN_LOG variable is set using “debug” or “trace” or “info. This function maps those to the appropriate logging level and defaults to INFO if the variable is not set or a bad value.

###### python_log_level_mapping (function)


Return the lowest Python level enabled by a Rust-style DYN_LOG filter.