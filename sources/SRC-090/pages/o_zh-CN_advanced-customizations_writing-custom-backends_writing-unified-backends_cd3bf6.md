source: https://docs.nvidia.com/dynamo/zh-CN/advanced-customizations/writing-custom-backends/writing-unified-backends
lastmod: 2026-09-23T23:30:39.914Z

# Writing Unified Backends

Dynamo’s unified backend path lets custom engines implement Dynamo’s shared backend lifecycle contract. The engine owns inference; Dynamo owns runtime registration, request serving, cancellation monitoring, signal handling, drain, and graceful shutdown.

Use this path for new token-in-token-out engines unless you need a feature that is still outside the unified contract.

## Choose an Implementation Language

Both unified implementations follow the same shape:

The framework handles model registration, endpoint serving, cancellation plumbing, and shutdown behavior around that engine contract.

## What the Unified Contract Covers

The shared contract provides:

- aggregated token-in-token-out inference
- disaggregated serving modes for supported engines
- model registration through Dynamo discovery
- request cancellation
- structured backend errors
- graceful shutdown and drain hooks

Use the lower-level Python worker path when your integration must own endpoint registration, request handling, or the request payload directly.

After you implement the backend, package it into a runtime image with
[Runtime Containers](https://docs.nvidia.com/dynamo/advanced-customizations/writing-custom-backends/runtime-containers). For Kubernetes deployment, place the
custom backend in a `DynamoGraphDeployment`

and follow the
[Model Deployment](https://docs.nvidia.com/dynamo/kubernetes/model-deployment/introduction).

###### Python

###### Rust

## Python Implementation

This guide covers the unified backend infrastructure in
[ dynamo.common.backend](https://github.com/ai-dynamo/dynamo/tree/v1.4.2/components/src/dynamo/common/backend):
a shared

`LLMEngine`

abstract base class (ABC), a runtime-owned `Worker`

, and a
sample implementation. For the Rust version of the same contract, use the Rust
tab. To own endpoint registration and request handling directly, use
[Writing Python Workers](https://docs.nvidia.com/dynamo/advanced-customizations/writing-custom-backends/writing-python-workers).

This guide walks through building a Python backend for an inference
engine that plugs into Dynamo’s distributed runtime via
`dynamo.common.backend`

. A “unified backend” is a Python entry point
that implements the shared `LLMEngine`

ABC and lets the framework own
runtime lifecycle (signal handling, model registration, graceful
shutdown, cancellation monitoring) — your code just owns inference.

Your backend lives in its own package and **does not need to be part
of the dynamo repository**. It depends on `ai-dynamo`

from PyPI (or
the git source) and imports `dynamo.common.backend`

. The steps below
assume you’re starting a fresh package in your own repo.

The reference example is the **sample engine** at
[ sample_engine.py](https://github.com/ai-dynamo/dynamo/blob/v1.4.2/components/src/dynamo/common/backend/sample_engine.py)
— a complete, runnable implementation. Read it alongside this guide.

**Where to look for what:**

- This guide — step-by-step walkthrough for someone starting a new backend from scratch.
— authoritative method-by-method contract.`LLMEngine`

ABC docstrings[Package README](https://github.com/ai-dynamo/dynamo/blob/v1.4.2/components/src/dynamo/common/backend/README.md)— in-tree reference:`GenerateRequest`

/`GenerateChunk`

field definitions, cancellation contract, full`DynamoException`

table, and file index.

### Python: What you are building

A backend is two things:

**An engine class**that subclasses`LLMEngine`

— owns the model, accepts preprocessed token requests, streams output chunks.**A**— a three-line shim that hands the engine class to`main.py`

entry point`run()`

from`dynamo.common.backend.run`

, which drives the lifecycle.

The `dynamo.common.backend`

package handles everything else: signal
handling, distributed runtime setup, model registration with
discovery, the serving loop, graceful shutdown, cancellation
monitoring, and error chain wrapping. (The lifecycle state machine
actually lives in Rust; `dynamo.common.backend.Worker`

is a thin
Python shim over it.)

### Python prerequisites

- Python 3.11 or newer.
`dynamo`

uses`typing.Required`

, which is 3.11+. - NATS and etcd reachable for end-to-end runs. The dynamo repo’s
`deploy/docker-compose.yml`

brings up both in one command if you don’t already have them running. `uv`

or`pip`

for installing dependencies.- Familiarity with
`async`

Python (`asyncio`

, async generators) and`argparse`

.

### Python Step 1: Create the package

Minimal `pyproject.toml`

:

For a bleeding-edge dependency on the dynamo source tree, install the runtime wheel from a clone:

[Maturin](https://github.com/PyO3/maturin) is the Rust-Python bindings build tool. The `patchelf`

extra lets maturin patch native extension library paths during the build.

Building the wheel needs a Rust toolchain plus `clang`

, `cmake`

,
`protobuf-compiler`

, and `libssl-dev`

.

### Python Step 2: Subclass `LLMEngine`


In `src/my_backend/engine.py`

, declare a class that subclasses
`LLMEngine`

and owns whatever state your engine needs. Construction
must be cheap and side-effect-free — heavy work goes in `start()`

.

`GenerateRequest`

and `GenerateChunk`

are `TypedDict`

s describing the
shared shape — see Step 4 for the fields.

### Python Step 3: Implement `from_args`


`from_args`

is a classmethod factory that parses CLI args and returns
`(engine, WorkerConfig)`

. The engine is constructed but **not
started**.

`from_args`

is `async`

to match the ABC; you can `await`

from it if
your CLI parsing reads config from a file or hits an API. Most
backends don’t need to.

For backends that already have a `DynamoRuntimeConfig`

-shaped
config object (e.g. one derived from an existing engine’s own
config), prefer the
`WorkerConfig.from_runtime_config(runtime_cfg, model_name=...)`

helper — it pulls the shared discovery / request-plane / parser
fields off the config in one line.

### Python Step 4: Implement `LLMEngine`

methods

The ABC has three required methods (`start`

, `generate`

, `cleanup`

)
plus two with default no-op implementations (`abort`

, `drain`

).

#### Python: `start()`


Start the engine and return `EngineConfig`

metadata. After this
returns, `generate()`

MUST be ready for concurrent calls.

`worker_id`

is an opaque per-worker identifier — most engines ignore
it. Backends needing a stable cluster-wide key (e.g. a
disaggregation machine ID) should derive from it instead of
hashing host/pid or asking operators for a CLI override.

Every `EngineConfig`

field except `model`

is optional. `None`

means
“don’t advertise”; KV-aware routing falls back to round-robin when KV
fields are unset.

#### Python: `generate()`


An async generator that yields `GenerateChunk`

dicts for a single
request. Called concurrently for multiple in-flight requests.

**Contract** (chunk shape is defined by the `GenerateChunk`

TypedDict
— see
[Request / Response Types](https://github.com/ai-dynamo/dynamo/blob/v1.4.2/components/src/dynamo/common/backend/README.md#request--response-types)
in the package README for the field reference):

- Every chunk carries
`token_ids`

and`index`

(use`0`

for single choice). - The final chunk additionally carries
`finish_reason`

and`completion_usage`

. - The framework’s cancellation monitor calls
`engine.abort(context)`

when the client disconnects or cancels; your loop should also poll`context.is_stopped()`

between yields and exit cleanly with a`finish_reason="cancelled"`

chunk.

Finish reason normalization (`"abort"`

→ `"cancelled"`

, etc.) is
handled by the Rust layer — emit whatever your engine uses
natively.

#### Python: Custom logits processors (optional)

Override `logits_processor_spec()`

to expose backend-neutral activation data.
Resolve and cache the specification during startup, call
`logits_processors_for_request()`

for each request, and construct fresh
inference-library processor instances from the returned entries. The worker
does not realize these entries automatically.

Import `LogitsProcessorSpec`

, `ForcedTokenSequenceSpec`

,
`PythonProcessorSpec`

, and the serialization helpers from
`dynamo.common.backend.engine`

. A generation-only specification runs on
aggregated and decode workers but not prefill or encode workers.
`ForcedTokenSequenceSpec`

can cross a JSON request boundary;
`PythonProcessorSpec`

contains a live factory and cannot be serialized.

#### Python: Engine management (optional)

Advertise lifecycle operations with `supported_controls()`

and implement each
operation in `engine_control(name, body)`

. The worker registers advertised
names at `POST /engine/control/<name>`

.

Use the separate `supported_updates()`

and `engine_update(name, body)`

methods
for operations that mutate engine-managed assets. These register at
`POST /engine/update/<name>`

. Both capability sets are empty by default, and
request and response bodies are JSON objects.

Override `on_endpoint_ready(endpoint)`

when a later management operation needs
the serving endpoint. The worker invokes this hook once after the endpoint
exists and before discovery registration or request serving.

#### Python: `abort(context)`

— optional

Called by the framework only when the client disconnects or the request is cancelled. NOT called on silent stream drops. Override to release engine-side resources (KV slots, scheduler entries, remote schedulers):

For cleanup that must run on every drop path — including silent
drops — use a `try/finally`

or a context manager inside `generate`

,
not `abort`

. The sample engine doesn’t override `abort`

because it
has no engine-side state to release; the default is a no-op.

#### Python: `drain()`

— optional

Runs once before shutdown, after the discovery unregister + grace-period sleep, while NATS/etcd are still alive. Use it for backend-side draining that must complete before transport teardown (e.g. in-flight NIXL KV transfers on prefill workers). Default is no-op.

#### Python: `cleanup()`


Two real requirements, both pinned by the Rust-side conformance kit:

**Null-safe against partial**If`start()`

failure.`start()`

raises partway through, fields you allocate incrementally may still be`None`

.`cleanup()`

must guard each resource (`if self._engine is not None: …`

) so the post-failure call doesn’t crash on half-initialized state.**Idempotent.**A second call after a successful first must return cleanly without re-entering teardown.

The Rust `Worker`

drives both: it calls `cleanup()`

after `start()`

returns Ok on shutdown, and the conformance kit (`run_conformance`

)
additionally calls `cleanup()`

on a never-started engine and twice in a
row, failing your tests with `CleanupWithoutStartFailed`

/
`SecondCleanupFailed`

if either invariant breaks. The guarded
single-shot pattern below covers both:

#### Python: Metrics and Prometheus (optional)

Unified backends have two metrics surfaces.

Use `register_prometheus(metrics)`

to bridge vendor-prefixed Prometheus
families into the worker’s `/metrics`

output. The framework owns the
`metrics`

handle; do not retain it after the method returns.

Use `component_metrics_dp_ranks()`

plus
`attach_snapshot_publisher(publisher)`

when the engine can push per-rank
`ComponentSnapshot`

values for `dynamo_component_*`

gauges and the
router’s `kv_used_blocks`

signal:

Keep the rank list stable for the engine lifetime. `Worker`

invokes
`attach_snapshot_publisher()`

only when the rank list is non-empty and
`WorkerConfig.enable_kv_routing`

is enabled. `register_prometheus()`

still
runs when `enable_kv_routing=False`

.

A typical engine pushes per-rank snapshots from its own stats callback
(a stat logger, scheduler hook, or dedicated poll thread) and bridges
its vendor-prefixed metric families through `register_prometheus()`

.

#### Python: KV event publishing (optional)

Unified backends declare KV event sources; the framework constructs and owns
the `KvEventPublisher`

instances. Do not instantiate `KvEventPublisher`

directly from a unified `LLMEngine`

. Instead, implement
`kv_event_sources()`

and return one source for each data-parallel rank hosted
by the worker.

Rust backends use the equivalent `LLMEngine::kv_event_sources()`

trait method;
see [Rust Step 4](https://docs.nvidia.com/dynamo/advanced-customizations/writing-custom-backends/writing-unified-backends#rust-step-4-implement-the-llmengine-trait) and the
[ LLMEngine trait](https://github.com/ai-dynamo/dynamo/blob/v1.4.2/lib/backend-common/src/engine.rs).

Use `ZmqSource`

when the engine already emits Dynamo-compatible KV events on a
ZMQ socket:

Use `PushSource`

when the engine needs a live publisher object and drives
`publish_stored()`

/ `publish_removed()`

from its own event thread:

KV event publishers require `EngineConfig.llm.kv_cache_block_size`

. If the
engine declares sources but does not return a block size, `Worker`

skips KV
event publishers because the router cannot map token IDs to cache blocks.
`WorkerConfig.enable_kv_routing=False`

is the operator-level kill switch; when
it is disabled, the worker does not call `kv_event_sources()`

.

Keep rank ownership stable for the engine lifetime. DP-capable engines should
also advertise the same rank shape in `EngineConfig.llm.data_parallel_size`

and
`data_parallel_start_rank`

so router-forced `dp_rank`

values line up with the
published event streams.

`PushSource`

engines own cleanup of their event producer. Stop publisher
threads or tasks in `cleanup()`

before returning, and do not publish after
cleanup begins.

### Python Step 5: Write `main.py`


Three lines.

`run`

installs signal handlers, builds the distributed runtime,
calls `engine.start(worker_id)`

with a runtime-allocated identifier,
registers the model with discovery, serves the endpoint, and runs the
graceful-shutdown orchestrator on SIGTERM/SIGINT.

Pair this with the `[project.scripts]`

entry from Step 1’s
`pyproject.toml`

so `my-backend ...`

works as a console command.

### Python Step 6: Errors and logging

**Errors**: the framework wraps non-`DynamoException`

errors raised
from `generate()`

(or lifecycle methods) as `Unknown`

. For typed
error reporting, raise a `DynamoException`

subclass directly from
[ dynamo.llm.exceptions](https://github.com/ai-dynamo/dynamo/blob/v1.4.2/components/src/dynamo/common/backend/README.md#error-handling)
— it propagates unchanged through the Rust bridge:

The package README has the full table of exception types and which
lifecycle phase raises which one. Engine-init failures should raise
`EngineShutdown`

from `start()`

. Cleanup shouldn’t normally raise —
log and swallow if a subsystem fails.

**Logging**: keep levels consistent across unified backends so
operators see the same surface regardless of which engine they’re
running:

`logger.info`

— lifecycle milestones (engine init complete, serving started, engine shutdown).`logger.debug`

— per-request events (request abort, cancellation).`logger.warning`

— recoverable problems (empty outputs, unexpected finish reasons).`logger.error`

— unrecoverable failures only.

The framework also configures `dynamo.runtime.logging`

for you; you
just call `logger = logging.getLogger(__name__)`

at the top of your
module and use it.

### Python Step 7: Test your engine

Install the dev extras (`pytest`

, `pytest-asyncio`

) declared in Step 1:

The sample engine has a unit-test
[suite](https://github.com/ai-dynamo/dynamo/blob/v1.4.2/components/src/dynamo/common/backend/tests/test_engine.py)
that you can copy as a starting point. The shape of a useful test:

Cover the happy path, cancellation, and any backend-specific edge
cases (stop tokens, max-tokens cap, empty prompt). Three to five
focused tests is plenty — the framework already pins the lifecycle
state machine and cancellation contract with Rust-side tests in
`lib/backend-common`

.

### Python Step 8: Run it locally

Three moving parts need to come up: NATS + etcd (discovery and the event/request planes), the Dynamo frontend (HTTP → backend discovery), and your backend.

Then send a request:

A successful response has non-empty `choices[0].message.content`

and a `finish_reason`

of `stop`

or `length`

.
`jq -e '.choices[0].finish_reason'`

is a good one-liner for a CI
smoke test.

If your backend looks silent, set `DYN_LOG=info`

(or
`DYN_LOG=debug,dynamo=debug`

for finer scoping) before launching —
the framework configures `tracing`

from `DYN_LOG`

.

### Python reference: sample engine

[ sample_engine.py](https://github.com/ai-dynamo/dynamo/blob/v1.4.2/components/src/dynamo/common/backend/sample_engine.py)
is the canonical minimal reference. Run it as-is:

It generates rotating token IDs with no ML dependencies, so it’s a useful stand-in for AIPerf / end-to-end pipeline smoke tests. Lift these patterns:

`from_args`

parses CLI args and returns`(engine, WorkerConfig)`

with no awaits.`start()`

returns an`EngineConfig`

whose KV fields are illustrative but not load-bearing (no real KV cache).`generate()`

polls`context.is_stopped()`

between yields and emits a`cancelled`

terminal on observation.`cleanup()`

is a no-op because the engine holds no resources.

### Python checklist

Before shipping:

-
`LLMEngine`

subclassed;`from_args`

returns`(engine, WorkerConfig)`

. -
`start()`

returns`EngineConfig`

with at least a non-empty`model`

. -
`generate()`

polls`context.is_stopped()`

between yields and emits a`"cancelled"`

terminal on observation. - Final chunk has
`finish_reason`

and`completion_usage`

. - Typed
`DynamoException`

subclasses used for error reporting where the category matters. -
`cleanup()`

releases all engine resources. - Logging levels match the standards in Step 6.

### Python see also

— authoritative contract.`LLMEngine`

ABC[Package README](https://github.com/ai-dynamo/dynamo/blob/v1.4.2/components/src/dynamo/common/backend/README.md)— lifecycle, error model, and request/response contract.[Sample engine](https://github.com/ai-dynamo/dynamo/blob/v1.4.2/components/src/dynamo/common/backend/sample_engine.py)— example user guide.- Rust tab on this page — the Rust counterpart, same contract, lower-level.