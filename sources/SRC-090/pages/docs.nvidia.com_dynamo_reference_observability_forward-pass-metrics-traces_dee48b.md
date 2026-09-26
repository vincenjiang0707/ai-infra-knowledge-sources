source: https://docs.nvidia.com/dynamo/reference/observability/forward-pass-metrics-traces
lastmod: 2026-09-24T19:58:16.636Z

# Forward Pass Metrics Trace Reference

Forward Pass Metrics (FPM) tracing persists finalized FPM payloads immediately before the Rust publication path sends them to the event plane. Persistence does not replace or reroute event-plane publication.

## Configuration

The configuration variables do not enable tracing by themselves. An invalid value or unwritable output path disables tracing only for that worker and emits a warning. Inference and normal FPM publication continue.

`DYN_FORWARDPASS_METRIC_PORT`

remains a separate legacy backend-generation opt-in and takes
precedence when set. It cannot add a missing Dynamo relay to an unsupported topology.
`DYN_FPM_BENCHMARK_OUTPUT_PATH`

is benchmark-only and is not used for live tracing.

## Supported Topologies

For vLLM, an explicit `DYN_FORWARDPASS_METRIC_PORT`

wins; otherwise trace activation uses port
`20380`

. SGLang uses its existing per-worker IPC endpoint.

## Capture Modes

In `sampled`

mode, Dynamo retains the newest pending payload for each
`(namespace, component, worker_id, dp_rank)`

key. At each monotonic interval it writes keys whose
`counter_id`

changed. It does not repeat an unchanged counter, and it flushes pending values during
graceful shutdown.

In `full`

mode, Dynamo writes every valid payload, including idle heartbeats. Each writer flushes a
non-empty batch every second and can flush sooner when its 1 MiB buffer fills. Producer enqueueing is
nonblocking in both modes; a bounded queue drops trace records instead of delaying inference.

## File and Retention Semantics

The default files are:

The producer ID is the sanitized runtime connection ID. Rotation counts uncompressed JSONL bytes. A single oversized row is written intact to an otherwise empty segment. After rolling, Dynamo removes only the oldest files that exactly match that producer’s prefix. On restart, the next index is one greater than the highest matching index.

`DYN_FPM_MAX_SEGMENTS`

applies independently to every producer, including producer IDs left by old
worker instances.

## Capacity Planning

The roll threshold counts uncompressed JSONL bytes; disk usage is the compressed gzip size. Estimate uncompressed daily volume with:

At the default five-second interval, one continuously changing rank writes about 17,280 periodic
rows per day, plus a possible shutdown flush. A 600-byte row is about 10.4 MB per rank per day before
compression. In `full`

mode, the same row at 10 forward passes per second is about 518 MB per rank
per day.

## Record Schema

Each line uses the shared gzip JSONL envelope:

`observed_at_unix_ms`

is the absolute observation time. The outer `timestamp`

is milliseconds since
the writer started. The nested `fpm`

object is the canonical payload. A `counter_id`

gap can result
from sampling, local queue pressure, an upstream ZMQ drop, a crash, or node loss.