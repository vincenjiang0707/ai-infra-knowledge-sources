source: https://docs.nvidia.com/dynamo/knowledge-base/concepts/fault-tolerance/request-cancellation-architecture
lastmod: 2026-09-24T19:58:16.636Z

# Request Cancellation Architecture

Cancel in-flight work across the Frontend and workers when a client disconnects.

This document describes how Dynamo implements request cancellation to cancel in-flight requests between Dynamo workers. Request cancellation allows in-flight requests to terminate early, saving computational resources that would otherwise be spent on responses that are no longer needed.

This is an internals reference covering the cancellation architecture, the `AsyncEngineContext`

trait, and its Python bindings. For the Prometheus metrics that track cancellations, see the [Metrics Catalog](https://docs.nvidia.com/dynamo/reference/observability/metrics-catalog#cancellation-and-rejection).

## How Cancellation Works

### Frontend Cancellation Detection

The frontend monitors each client connection for unexpected disconnects. When a client disconnects before the response is fully delivered, the frontend detects this and initiates cancellation. This covers two scenarios:

**Connection closed unexpectedly**— The client disconnects during request processing before response streaming begins.**Stream closed unexpectedly**— The client disconnects while an active SSE stream is delivering response tokens.

In both cases, the frontend cancels the request’s `AsyncEngineContext`

, which propagates cancellation to any linked child contexts on downstream workers.

### Worker Cancellation Detection

On the worker side, the runtime monitors the TCP connection from the frontend for cancellation signals. The worker detects cancellation in three scenarios:

**Control message received**— The frontend explicitly sent a cancellation control message.**TCP connection dropped**— The frontend disconnected without sending a control message (e.g., frontend crash or network failure).

When the worker receives a cancellation signal, it sets the corresponding state on the request’s `AsyncEngineContext`

. It is then up to the worker’s engine implementation to observe the cancellation (e.g., by checking `is_stopped()`

) and terminate processing accordingly. For details on implementing cancellation handling in a backend worker, see the [Backend Development Guide](https://docs.nvidia.com/dynamo/advanced-customizations/writing-custom-backends/writing-python-workers#request-cancellation).

### Cancellation Propagation

Cancellation propagates through multi-tier request chains via linked `AsyncEngineContext`

objects. When a parent context is cancelled, all linked child contexts are automatically cancelled as well. This ensures that when a client cancels a request at the frontend, all associated sub-requests on downstream workers are automatically cancelled, saving computational resources across the entire request pipeline.

## Metrics

Dynamo exposes Prometheus metrics to monitor request cancellations at both the frontend (`dynamo_frontend_model_cancellation_total`

) and runtime (`dynamo_component_cancellation_total`

) layers. For the full field catalog — types, labels, and example output — see [Cancellation and rejection](https://docs.nvidia.com/dynamo/reference/observability/metrics-catalog#cancellation-and-rejection) in the Metrics Catalog.

Note that the runtime metric records cancellation signals received by the worker, not whether the request was actually aborted at the engine level. It is up to the worker’s engine implementation to observe the cancellation (e.g., by checking `is_stopped()`

) and terminate processing accordingly.

## AsyncEngineContext Trait

At the core of Dynamo’s request cancellation system is the `AsyncEngineContext`

trait. This trait is associated with every request stream and provides lifecycle management for async operations, including stream identification, graceful shutdown capabilities, and immediate termination capabilities.

### Key Methods

#### Identification

: Returns the unique identifier for the stream. This ID is set by the user for request identification, and the same ID can be used for sub-requests to associate them with the original user request.`id()`


#### Status Checking

: Returns`is_stopped()`

`true`

if graceful cancellation has been requested via`stop_generating()`

. This represents a signal to the worker that the request has been cancelled and it should return early.: Returns`is_killed()`

`true`

if a hard stop has been issued via`kill()`

. This typically indicates that the network connection between client and server has been cut or an immediate termination is required.

#### Async Status Monitoring

: An async method that completes when the context becomes stopped. If already stopped, returns immediately.`stopped()`

: An async method that completes when the context becomes killed. If already killed, returns immediately.`killed()`


#### Cancellation Control

: The recommended method for cancelling a request. This informs the engine to stop producing results for the stream gracefully. This method is idempotent and does not invalidate results currently in the stream.`stop_generating()`

: Alias for`stop()`

`stop_generating()`

.: Extends`kill()`

`stop_generating()`

but also indicates a preference to terminate without draining remaining items in the stream. This is implementation-specific and may not be supported by all engines.

#### Child Request Management

: Links a child`link_child(child: Arc<dyn AsyncEngineContext>)`

`AsyncEngineContext`

to this context. When`stop_generating()`

,`stop()`

, or`kill()`

is called on the parent context, the same method is automatically called on all linked child contexts in the order they were linked. This is especially useful in disaggregated serving scenarios where a frontend receives cancellation notification and needs to cancel requests to workers, and the worker can then cancel its sub-requests (e.g., remote prefill operations).

### Thread Safety

The `AsyncEngineContext`

trait ensures thread-safety with `Send + Sync`

bounds, allowing safe concurrent access across multiple threads and async tasks.

## Python Bindings

The `AsyncEngineContext`

functionality is exposed to Python through the `Context`

class, which provides a largely one-to-one mapping from Rust methods to Python methods.

### Python Context Class

The Python `Context`

class wraps the Rust `AsyncEngineContext`

and exposes the following methods:

: Returns the unique identifier for the context`id()`

: Synchronous method equivalent to the Rust`is_stopped()`

`is_stopped()`

: Synchronous method equivalent to the Rust`is_killed()`

`is_killed()`

: Issues a stop generating signal, equivalent to the Rust method`stop_generating()`

: An async method that completes when the context becomes either killed or stopped, whichever happens first. This combines the functionality of the Rust`async_killed_or_stopped()`

`killed()`

and`stopped()`

async methods using`tokio::select!`

.

For a working example of request cancellation, see the [cancellation demo](https://github.com/ai-dynamo/dynamo/tree/v1.4.2/examples/custom_backend/cancellation/README.md).

### Context Usage in Python

The context is available optionally in both incoming and outgoing request scenarios:

#### Incoming Requests

For incoming requests, the generate method may optionally accept a `context`

argument after the `request`

argument. If the `context`

parameter is specified in the method signature, it will receive the context object of the incoming request. Request handlers can:

- Check for cancellation synchronously using
`context.is_stopped()`

before beginning expensive operations - Listen for cancellation asynchronously using
`await context.async_killed_or_stopped()`


Example:

#### Outgoing Requests

For outgoing requests, Python scripts may optionally provide a context object to outgoing runtime endpoint client router operations (such as `generate`

, `round_robin`

, `random`

, `direct`

methods) as a keyword argument. The script can cancel the outgoing request via the provided context object.

This is especially useful when child outgoing requests need to be cancelled when the parent incoming request is cancelled. In such cases, the script can simply pass the incoming context object to the outgoing request, automatically linking the cancellation behavior.

Example: