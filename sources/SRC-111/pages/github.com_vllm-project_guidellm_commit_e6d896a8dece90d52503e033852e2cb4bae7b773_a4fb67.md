source: https://github.com/vllm-project/guidellm/commit/e6d896a8dece90d52503e033852e2cb4bae7b773

You signed in with another tab or window. Reload to refresh your session.You signed out in another tab or window. Reload to refresh your session.You switched accounts on another tab or window. Reload to refresh your session.Dismiss alert

Copy file name to clipboardExpand all lines: docs/en/getting-started/benchmark.md

+1-1Lines changed: 1 addition & 1 deletion

Display the source diff

Display the rich diff

Original file line number

Diff line number

Diff line change

@@ -262,7 +262,7 @@ guidellm run \

262

262

263

263

The data parameter `time_scale` acts as a scaling factor for the intervals between trace events after wait and pack caps: `1.0` preserves the original timing, `2.0` doubles the intervals and runs twice as long, and `0.5` halves the intervals and runs twice as fast. Wait caps (`max_wait`, `max_session_wait`, `min_concurrent_sessions`) are applied in original trace seconds before `time_scale`.

264

264

265

-

Raise parallelism with `min_concurrent_sessions`. Use `copies` when the packed dataset is not large enough to sustain that load for the whole benchmark. `copies` replays the full packed trace sequentially: the next pass starts at the previous pass's last scheduled request. It does not overlay duplicate conversations on the same timestamps. Synthetic data traces re-salt the synthetic data to ensure cache-unique conversations for the copies.

265

+

Raise parallelism with `min_concurrent_sessions`. Use `copies` when the packed dataset is not large enough to sustain that load for the whole benchmark. By default (`copy_offset=1`) `copies` replays the full packed trace sequentially: the next pass starts at the previous pass's last scheduled request. `copy_offset` can overlay or gap copies relative to that prior span. Synthetic data traces re-salt the synthetic data to ensure cache-unique conversations for the copies.

266

266

267

267

Strategically choose between increasing parallelism and affecting request timings for your use case. Higher parallelism increases concurrent simultaneous requests, and increases the chance of cache evictions affecting your benchmark.

Copy file name to clipboardExpand all lines: docs/en/guides/trace_replay.md

+2-1Lines changed: 2 additions & 1 deletion

Display the source diff

Display the rich diff

Original file line number

Diff line number

Diff line change

@@ -56,6 +56,7 @@ All trace formats can accept the following optional data arguments:

56

56

|`max_session_wait`| unset | Maximum idle in original trace seconds from the previous session's last request to this session |

57

57

|`min_concurrent_sessions`| unset | Pack sessions so at least this many overlap during steady state |

58

58

|`copies`| 1 | Sequential full-dataset replays; pass k+1 starts at pass k's last scheduled request |

59

+

|`copy_offset`| 1.0 | Where the next copy starts relative to the prior span: 0 at the start, 1 at the end, >1 a gap |

59

60

60

61

These are passed through the `--data` argument like below:

61

62

@@ -70,7 +71,7 @@ guidellm run \

70

71

71

72

`trace_synthetic` and `mooncake` replay each row as an independent, single-request conversation. Rows are sorted by timestamp and keep their offsets from the first request in the trace. Prompts are generated as rows are consumed, and Mooncake hash IDs remain shared across rows within one `copies` pass. Use `max_session_wait` to cap gaps between these independent requests; `max_wait` only caps gaps within multi-request conversations, such as WEKA sessions.

72

73

73

-

Raise parallelism with `min_concurrent_sessions`, wait caps, and `time_scale` first. Use `copies` only when that packed pass is too short for the benchmark (`max_duration` / `max_requests`). `copies` replays the entire packed dataset back-to-back; it does not run duplicate conversations at the same timestamp. The next pass's first request is scheduled at the previous pass's last request timestamp (timeline concatenation, not a wait for the last generated token). Hash-id formats (`mooncake`, `weka`) use a separately salted global token-block table per pass so later passes do not reuse earlier tokens and inflate prefix-cache hits.

74

+

Raise parallelism with `min_concurrent_sessions`, wait caps, and `time_scale` first. Use `copies` only when that packed pass is too short for the benchmark (`max_duration` / `max_requests`). By default (`copy_offset=1`) `copies` replays the entire packed dataset back-to-back: the next pass starts at the previous pass's last request timestamp. `copy_offset=0` starts at the prior pass's first timestamp; values between 0 and 1 interpolate; values above 1 add a gap. Hash-id formats (`mooncake`, `weka`) use a separately salted global token-block table per pass so later passes do not reuse earlier tokens and inflate prefix-cache hits.

## 0 commit comments