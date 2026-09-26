source: https://docs.nvidia.com/dynamo/v1.3.0/components/frontend/python-route-extensions
lastmod: 2026-09-24T19:58:16.636Z

# Python Route Extensions

Python route extensions let an external package register additional HTTP routes on the Dynamo frontend, served on the same port as the OpenAI-compatible API — without a custom binary or a from-source build.

Extensions are **opt-in**: the frontend only loads a provider you explicitly select on the command line. A selection is either a **name** registered under the `dynamo.frontend.routes`

entry-point group (preferred for packaged plugins) or a direct ** module:function** path (handy for quick/ad-hoc use). Extensions add routes; they cannot override a built-in route (a duplicate method+path is rejected at startup).

The initial contract is intentionally narrow: **static-path GET routes** with a synchronous handler. Path parameters (

`/{id}`

), wildcards, non-`GET`

methods, and `async def`

handlers are rejected at construction. This surface can grow later without breaking existing extensions.## Minimal example

**1. Write a route provider.** A provider is a callable that returns a `FrontendRoute`

(or an iterable of them). Each handler is synchronous, receives a `FrontendExtensionContext`

, and returns a JSON-serializable body (HTTP 200) or a `FrontendResponse`

to set the status code.

**2. Register it as an entry point** under the `dynamo.frontend.routes`

group. The entry-point name (here `hello-world`

) is what you pass on the command line.

**3. Install the package** so the entry point is discoverable:

**4. Launch the frontend** with the extension selected:

**5. Call the route:**

## Quick / ad-hoc: `module:function`


For development or a one-off deployment where packaging a plugin is overkill, pass a `module:function`

path directly instead of a registered name — no `pyproject.toml`

or install required, as long as the module is importable (e.g. on `PYTHONPATH`

):

A registered entry-point name always takes precedence; the path fallback only applies when the value is not a registered name and contains `:`

.

## Handler contract

-
**Route:**`GET`

only, static path (no`{param}`

/`*wildcard`

) — enforced at`FrontendRoute`

construction. -
**Signature:**`handler(ctx: FrontendExtensionContext)`

— synchronous.`async def`

handlers are rejected at construction. -
**Return:**a JSON-serializable value (implies`200`

), or`FrontendResponse(status_code, body)`

to set the status. Ordinary tuples serialize as JSON arrays — use`FrontendResponse`

for status overrides: -
**Live state:**`FrontendExtensionContext`

exposes the current frontend state so responses reflect models registering/draining at runtime — e.g.`ctx.has_any_ready_model()`

,`ctx.serving_ready_display_names()`

,`ctx.is_model_ready_to_serve(name)`

,`ctx.is_ready()`

. -
**Keep handlers fast and non-blocking.**Handlers run on a small, dedicated thread pool (isolated from the inference tokenization pool), so a slow handler degrades only other extension routes, not inference. Still, the pool is small and GIL-serialized: a handler that exceeds ~30s is treated as hung and its request returns`503`

, and a saturated pool sheds new extension requests with`503`

. Do not block on network/disk or run heavy compute inline.

## Notes

- Select multiple extensions by repeating
`--frontend-route-extension`

(or via a**whitespace-separated**`DYN_FRONTEND_ROUTE_EXTENSIONS`

). Names are de-duplicated. - Passing an unknown name fails fast and lists the available registered extensions.
- Extensions apply to the HTTP frontend only.