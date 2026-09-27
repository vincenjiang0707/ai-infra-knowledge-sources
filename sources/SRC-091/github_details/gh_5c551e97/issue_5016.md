# [Issue #5016] [RFC] Add Rust raw-block I/O performance and observability metrics

source: https://github.com/LMCache/LMCache/issues/5016
state: open | updated: 2026-09-17T14:46:37Z
labels: 

## 正文

## Summary

Add a small set of low-overhead I/O counters to the Rust raw-block backend and expose them through the existing `RawBlockCore.report_status()` path.

This RFC only covers basic counters and gauges. Latency histograms can be discussed separately after the counters are implemented and benchmarked.

## Motivation

The Rust raw-block backend supports POSIX I/O, `io_uring`, NVMe `io_uring_cmd`, fixed buffers, and bounce buffers. Existing Rust counters are mainly used internally for batch completion and shutdown.

Today it is difficult to answer:

- How many reads/writes and bytes reached the device?
- How many physical I/Os failed?
- How many I/Os are currently in flight or waiting in the Rust queue?
- How often are bounce buffers or registered fixed buffers used?

Python task metrics cannot reliably provide these values because submission, completion, and buffer-path selection happen inside Rust.

## Proposed metrics

Counters are cumulative for the lifetime of the raw-block device. Gauges represent current state.

### I/O throughput and failures

| Metric | Type | Description |
|---|---|---|
| `read_operations` | Counter | Physical reads submitted to POSIX/io_uring. |
| `write_operations` | Counter | Physical writes submitted to POSIX/io_uring. |
| `read_bytes` | Counter | Physical read bytes submitted. |
| `write_bytes` | Counter | Physical write bytes submitted. |
| `completed_operations` | Counter | Physical I/Os completed successfully. |
| `failed_operations` | Counter | Physical I/Os completed with an error. |

The counting unit is physical I/O because it reflects the actual work submitted to the device.

### Concurrency and queue pressure

| Metric | Type | Description |
|---|---|---|
| `in_flight_operations` | Gauge | Submitted physical I/Os that have not completed. |
| `peak_in_flight_operations` | Gauge | Maximum in-flight operations during the device lifetime. |
| `queued_operations` | Gauge | Operations waiting in the Rust io_uring userspace queue. Zero for POSIX. |
| `peak_queued_operations` | Gauge | Maximum queued operations during the device lifetime. |
| `queue_full_events` | Counter | Times submission had to wait or retry because the ring had no capacity. |

The existing Rust `in_flight_count` should be reused instead of maintaining a second definition.

### Buffer path

| Metric | Type | Description |
|---|---|---|
| `bounce_operations` | Counter | Physical I/Os using an aligned bounce buffer. |
| `bounce_bytes` | Counter | Bytes transferred through bounce buffers. |
| `fixed_buffer_operations` | Counter | Physical I/Os using registered io_uring fixed buffers. |
| `fixed_buffer_bytes` | Counter | Bytes transferred through registered fixed buffers. |

These metrics show whether the expected zero-copy path is actually being used.

## Status integration

The existing status path is:

```text
RawBlockDevice -> RawBlockCore.report_status()
               -> RawBlockL2Adapter.report_status()
               -> MP server info API / observability system
```

The Rust binding should provide an internal snapshot method used by `RawBlockCore.report_status()`. This RFC does not require a new public `get_stats()` API.

`RawBlockCore.report_status()` already exposes configuration and state such as:

- `device_path`
- `use_odirect`
- `enable_zero_copy`
- `io_engine`
- `iouring_queue_depth`
- `use_uring_cmd`
- `inflight_io_count`

The proposed Rust counters should be added under a nested field, for example:

```python
{
    # Existing RawBlockCore status fields...
    "rust_io": {
        "read_operations": 120,
        "write_operations": 80,
        "read_bytes": 503316480,
        "write_bytes": 335544320,
        "completed_operations": 199,
        "failed_operations": 1,
        "in_flight_operations": 0,
        "peak_in_flight_operations": 64,
        "queued_operations": 0,
        "peak_queued_operations": 30,
        "queue_full_events": 2,
        "bounce_operations": 12,
        "bounce_bytes": 50331648,
        "fixed_buffer_operations": 150,
        "fixed_buffer_bytes": 629145600,
    },
}
```

Counters remain cumulative. No `reset_stats()` API is proposed. Monitoring systems can calculate interval rates and deltas from cumulative values.

The current MP raw-block configuration creates one `RawBlockCore` and one device per adapter. Therefore the initial status snapshot naturally has per-adapter/per-device scope, without adding a device label or aggregation layer.

## Out of scope

### Transfer splitting metrics

`io_uring_cmd` transfer splitting currently happens in Python `RawBlockCore`; Rust receives the resulting chunks as independent submissions. Splitting is also largely determined by static configuration and device limits.

Therefore `split_operations` and `split_chunks` are not part of this Rust metrics proposal. If they become useful, they should be added separately in Python.

### Latency histograms

Latency measurement is deferred to a follow-up proposal. The first implementation should establish low-cost counters and provide data for deciding whether queue, device, or end-to-end latency histograms are needed.

## Implementation notes

- Store counters in an `Arc<RawBlockIoStats>` shared with the io_uring worker.
- Use `AtomicU64` with relaxed ordering for hot-path counters.
- Do not acquire a mutex or allocate memory only to update a metric.
- Record submission only after an operation is actually submitted.
- Record completion exactly once for every submitted operation.
- Pre-submission validation errors are not physical I/O failures.
- Live-gauge decrements must not underflow.
- Statistics must never change I/O behavior or cause an I/O request to fail.
- Rust should only produce a snapshot; OTel/Prometheus export remains in Python.
- Device paths, batch IDs, keys, PIDs, error messages, and errno values must not become metric labels.

## Testing and performance

Tests should cover:

- POSIX and io_uring read/write counters;
- successful and failed completion accounting;
- in-flight returning to zero after completion;
- queued and peak-queued accounting;
- bounce-buffer and fixed-buffer paths;
- concurrent counter updates;
- inclusion in `RawBlockCore.report_status()` and `RawBlockL2Adapter.report_status()`.

Before enabling the counters by default, benchmark them on a representative io_uring workload. Suggested acceptance target: less than 2% throughput regression, with no metrics-only locks or allocations in the I/O hot path.

## Questions for reviewers

1. Is physical submitted I/O the right unit for operation and byte counters?
2. Is any proposed first-version counter unnecessary or missing?
3. Should the counters be enabled by default after the overhead benchmark passes?
4. Should `completed_operations` and `failed_operations` remain combined, or be separated into read/write outcomes?


## 评论 (6)

### yangyang233333 · 2026-09-08

Hi @3xdevv, @nayeonikim, @daegyu94, @zhengfeihe, @ankit-sam, and @DongDongJu — you have contributed to the Rust raw-block I/O path, including batching, bounce buffers, FDP/`uring_cmd`, worker wakeups, io_uring, and the original backend implementation.

Could you please share any suggestions on this proposal, especially:

1. Is this first-version metric set small enough for the Rust I/O hot path?
2. Are physical submitted I/Os the right unit for operation/byte counters?
3. Are there important io_uring, `uring_cmd`, bounce-buffer, or fixed-buffer signals missing?
4. Are there implementation points where atomic counter updates could noticeably affect performance?

The intention is to keep the first implementation limited to inexpensive counters/gauges and leave latency histograms for a separate follow-up. Thanks!


### zhengfeihe · 2026-09-08

Thanks for the detailed RFC. Several thoughts :

* Please extend the existing `report_status()` path rather than add get_stats(), as it already powers our observability system. It feeds into the MP server’s info API and exposes most of the proposed snapshot metadata.
* We don’t need `reset_stats()`. Counters should be cumulative.
* split_operations / split_chunks would have to be counted in Python, where splitting happens . Rust only sees independent submissions. (I also don't think these are really runtime metrics: splitting is mostly deterministic, decided by static config, so the counters would just measure a constant.)
* For raw block adapter, right now it's per device per adapter 


### yangyang233333 · 2026-09-08

Thanks @zhengfeihe — I checked the current implementation and agree with these points:

- `RawBlockCore.report_status()` already feeds `RawBlockL2Adapter.report_status()` and the MP server status path, so the RFC now extends that path instead of proposing a separate public `get_stats()` API.
- I removed `reset_stats()`; the counters are now lifetime-cumulative.
- I removed `split_operations` / `split_chunks` from the Rust proposal. The `io_uring_cmd` chunking loop is currently in Python `RawBlockCore`, so Rust only sees independent physical submissions. Any future split metric should live in Python.
- I clarified that the current MP raw-block adapter owns one `RawBlockCore` / device, so the initial snapshot is naturally per adapter/device and does not need aggregation or a device label.

I also removed duplicate configuration metadata from the proposed Rust snapshot because `report_status()` already exposes it. The issue body has been updated accordingly. Thanks for the guidance!


### DongDongJu · 2026-09-08

Hello @yangyang233333,
Thanks for your great suggestion.

I want to make sure few things.

- The existing `in_flight_count` does not match the proposed definition.

It increments before entering the Rust userspace queue, so it includes queued requests. 
It also decrements on SQE-build failure, fatal submission failure, and shutdown cancellation which is not only device completion. 
Reusing it as “submitted physical I/Os that have not completed” would misreport device concurrency. 

Please either expose this as outstanding requests, including queued work, or separately track submitted I/O. 
Keep the existing lifecycle counter’s behavior intact.

- Define whether an operation means a Rust request or an individual I/O attempt.

Regular io_uring resubmits short completions, and POSIX loops over partial reads/writes. 
Counting each submission but only the final request completion would mix two units. 

For example, an 8 KiB read completing as 4 KiB plus a 4 KiB retry produces two submissions and 12 KiB of requested bytes, while transferring 8 KiB. 

Backend I/O attempts are a reasonable unit, but call the bytes submitted bytes, not achieved device throughput. 
These counters also cannot establish the actual hardware-command count. 
Please specify partial submission, retry, and pre-submission failure accounting explicitly.

- Keep the default-on decision tied to a sufficiently sensitive benchmark.

Relaxed atomics still have update costs. 
Include small-I/O/high-IOPS and concurrent-submitter cases alongside representative KV-cache transfers, with status polling enabled. Compare throughput, CPU consumption, and tail latency.
Lifetime peaks could be deferred if their update cost is measurable.

Otherwise, Plz ping me when you make the PR for this.


### DongDongJu · 2026-09-08

and good to ping in slack too. 
Please join #sig-storage channel in slack.

### nayeonikim · 2026-09-17

Hi @yangyang233333, thanks for the proposal!

The v1 metric set looks good to me. I think separating read and write failures would also be useful, since the corresponding operation counters are already separated. failed_read_operations / failed_write_operations could make the status easier to interpret.
