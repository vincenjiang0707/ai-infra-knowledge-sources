source: https://docs.nvidia.com/dynamo/zh-CN/v1.3.0/user-guides/observability-local/forward-pass-metrics-tracing
lastmod: 2026-09-23T23:30:39.914Z

# Forward Pass Metrics Tracing

Forward pass metrics (FPM) tracing is an opt-in, best-effort analysis stream.
It captures finalized FPM payloads in Dynamo’s Rust publication path immediately
before they are sent to the event plane. This covers relay-backed vLLM and
SGLang publishers as well as the direct publishers used by TensorRT-LLM and the
mocker. Persistence is additive: it does not replace, suppress, or reroute those
events. On supported vLLM and SGLang worker topologies, however,
`--fpm-trace`

(or its `DYN_FPM_TRACE=1`

environment equivalent) also activates
the existing backend FPM generation and relay path, so enabling tracing can
cause FPM events to begin publishing.

Enable tracing with the default sampled configuration:

The shared runtime option also provides `--no-fpm-trace`

, which overrides an
enabled `DYN_FPM_TRACE`

value for that worker.

Each worker writes its own files under `/tmp`

by default:

`<producer-id>`

is the worker’s runtime connection ID, sanitized for use in a
file name. Partitioning files by producer prevents workers on a shared volume
from writing to the same gzip segment.

`/tmp`

is convenient but ephemeral. Mount a host directory or persistent
volume and set `DYN_FPM_OUTPUT_PATH`

if traces must survive pod replacement.

## Configuration

The other variables do not enable tracing by themselves. An invalid value or an unwritable output path disables tracing only for that worker and produces a warning. Inference and normal FPM publication continue.

`--fpm-trace`

or `DYN_FPM_TRACE=1`

also enables the existing FPM generation
path for vLLM and SGLang. For vLLM, an explicit
`DYN_FORWARDPASS_METRIC_PORT`

wins; otherwise Dynamo uses port `20380`

. SGLang
uses its existing per-worker IPC endpoint. If vLLM has an incompatible custom
scheduler, Dynamo warns and continues serving without trace data from that
scheduler.

TensorRT-LLM and the mocker already use Dynamo’s direct FPM publisher on their
normal publication paths. For those publishers, `DYN_FPM_TRACE`

adds local
persistence but does not need to activate a Python backend relay.

Trace-based activation is limited to worker paths that construct a Dynamo FPM relay:

`DYN_FORWARDPASS_METRIC_PORT`

remains a separate legacy opt-in and takes
precedence when it is set, including on topologies where trace-based activation
is unsupported. It can enable backend FPM generation, but it does not add a
missing Dynamo relay, so an unsupported topology still does not produce a trace
file.

`DYN_FPM_BENCHMARK_OUTPUT_PATH`

remains a separate benchmark-only output and
is not used for live tracing.

## Capture Modes

In `sampled`

mode, Dynamo retains only the newest pending payload for each
`(namespace, component, worker_id, dp_rank)`

key. On each monotonic sampling
interval, it writes keys whose `counter_id`

changed. It does not repeat an
unchanged counter. Pending values are flushed during graceful shutdown.

In `full`

mode, Dynamo writes every valid payload that reaches the producer,
including idle heartbeats. This mode can generate substantially more data.
It intentionally has no record-rate cap: the bounded queue limits memory and
protects inference, but it does not limit storage traffic. Each active writer
flushes a non-empty batch on a one-second interval and can flush sooner when
its 1 MiB buffer fills, so I/O on a shared volume scales with the number and
activity of producers. Use the default sampled mode or node-local storage
unless the shared filesystem has been sized for the expected full-mode load.

Both modes are best effort. Producer enqueueing is nonblocking, and a bounded in-process queue drops trace records instead of delaying inference. The worker logs structured dropped-record counts when a trace consumer falls behind.

## Record Shape

Each line uses the shared gzip JSONL envelope. The `event`

object is the FPM
trace record; `observed_at_unix_ms`

is its absolute observation time. The
outer `timestamp`

is milliseconds elapsed since that writer started.

The nested `fpm`

object is the complete canonical payload. Use its
`worker_id`

, `dp_rank`

, and `counter_id`

together when checking continuity.
A gap in `counter_id`

can result from sampling, local queue pressure, an
upstream vLLM or SGLang ZMQ drop, a crash, or node loss. The trace is not a
durable event plane.

## Read and Size Traces

Decompress all segments for one output prefix in index order:

Replace `4192`

with the producer ID in the file name.

The roll threshold counts uncompressed JSONL bytes, while disk usage is the compressed gzip size. Measure representative records for capacity planning:

Estimate uncompressed bytes per day as:

At the default five-second sampling interval, one continuously changing rank
writes about 17,280 periodic rows per day, plus a possible graceful-shutdown
flush. For example, 600-byte rows are about 10.4 MB per rank per day before
compression. In `full`

mode, the rate follows the backend’s forward passes:
the same 600-byte row at 10 forward passes per second is about 518 MB per rank
per day before compression.

Rotation starts a new gzip file before adding a row that would cross the configured threshold. A single oversized row is written intact to an otherwise empty segment. After a new segment is written, Dynamo removes only the oldest files that exactly match that producer’s prefix. On restart, the next index is one greater than the highest matching existing index, even if there are gaps.

The segment limit applies independently to each producer. A shared persistent
volume can therefore contain up to `DYN_FPM_MAX_SEGMENTS`

files for every
currently or previously used producer ID. Use an external lifecycle policy to
remove stale producer sets.

## Kubernetes Storage

Set the output prefix inside a mounted volume. Existing Dynamo environment and volume-mount configuration is sufficient; no Dynamo Operator API change is required.

Graceful shutdown flushes records already accepted by the trace pipeline.
`SIGKILL`

, node loss, full queues, and upstream transport loss can still lose
records. Treat the files as operational telemetry for analysis, not as input
for planner warm-start or replay.