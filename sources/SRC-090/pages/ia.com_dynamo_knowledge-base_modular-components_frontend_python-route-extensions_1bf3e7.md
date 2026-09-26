source: https://docs.nvidia.com/dynamo/knowledge-base/modular-components/frontend/python-route-extensions
lastmod: 2026-09-24T19:58:16.636Z

# Python Route Extensions

Python route extensions let an external package register additional HTTP routes on the Dynamo Frontend. The routes use the same port as the OpenAI-compatible API and do not require a custom binary or source build.

Extensions are opt-in. The Frontend loads only the providers selected with
`--frontend-route-extension`

or `DYN_FRONTEND_ROUTE_EXTENSIONS`

. A selection can be either:

- A name registered under the
`dynamo.frontend.routes`

entry-point group, recommended for packaged extensions. - A direct
`module:function`

path for development or one-off deployments.

Extensions add routes but cannot override built-in routes. A duplicate method and path combination causes Frontend startup to fail.

Python route extensions currently support synchronous handlers on static-path `GET`

routes only.
Path parameters, wildcards, other HTTP methods, and asynchronous handlers are rejected.

## Add a route extension

### Define a route provider

A provider is a callable that returns a `FrontendRoute`

or an iterable of routes. Each synchronous
handler receives a `FrontendExtensionContext`

and returns either:

- A JSON-serializable body, which produces HTTP 200.
- A
`FrontendResponse`

with an explicit status code and body.

### Register the provider

For an installable package, register the provider under the `dynamo.frontend.routes`

entry-point
group. The entry-point name is the value passed to the Frontend.

Install the package so the entry point is discoverable:

### Start the Frontend

Select the registered provider by name:

The equivalent environment-variable form is:

Call the added route:

The response is:

## Load an importable provider directly

For development or a one-off deployment, pass an importable `module:function`

path. The module must
be importable, for example by being available on `PYTHONPATH`

.

A registered entry-point name takes precedence. The `module:function`

fallback applies only when no
registered name matches and the value contains `:`

.

## Return a custom status

Return `FrontendResponse`

when a handler needs a status other than HTTP 200:

`FrontendExtensionContext`

provides a read-only view of live Frontend state through these methods:

`is_ready()`

`is_cancelled()`

`has_any_ready_model()`

`is_model_ready_to_serve(name)`

`model_display_names()`

`serving_ready_display_names()`


## Handler limits

Handlers execute in a small, dedicated thread pool, separate from inference tokenization. Keep them fast and non-blocking:

- A handler that exceeds 30 seconds returns HTTP 503.
- A saturated extension pool rejects new requests with the configured overload status code, HTTP 529 by default.
- Handler failures return HTTP 500.
- Network, disk, or compute-heavy operations can block other extension routes because Python handlers contend for the Global Interpreter Lock (GIL).

## Load multiple providers

Repeat `--frontend-route-extension`

to load multiple providers:

For the environment variable, use whitespace-separated values:

Provider names are de-duplicated. An unknown name fails startup and reports the available registered extensions.

For the complete flag and handler contract reference, see
[Frontend Configuration Reference](https://docs.nvidia.com/dynamo/reference/components/frontend-configuration#python-route-extensions).