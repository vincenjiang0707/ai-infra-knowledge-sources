# [Issue #1048] Reported latency percentiles exclude scheduler dispatch delay (coordinated omission)

source: https://github.com/vllm-project/guidellm/issues/1048
state: closed | updated: 2026-08-31T15:36:08Z
labels: 

## 正文

### Summary

When the scheduler cannot dispatch requests at the configured rate, the resulting backlog is excluded from every reported latency percentile.

Reported `request_latency` measures `request_end - request_start`, where `request_start` is when the client actually sent the request — not `targeted_start`, the time the load schedule intended it to be sent. The gap between the two is absorbed silently.

This is coordinated omission, the measurement error Gil Tene described for open-loop load generators: when the generator's own dispatch stalls, the resulting delay is never attributed to any request, so reported tail latency improves precisely when the system under test is falling behind. HdrHistogram corrects for it with `recordValueWithExpectedInterval`, and `wrk2` was written specifically to avoid it. The correction below is the same one, applied at the reporting layer.

### Reproduction

Uses only the shipped mock server. The server stays healthy for the whole run: ~190 ms service time, no server-side queueing. The client is the bottleneck.

Terminal 1:

```bash
guidellm mock-server --host 127.0.0.1 --port 8123 --model mock \
  --ttft-ms 100 --itl-ms 5 --output-tokens 16
```

Terminal 2:

```bash
guidellm run \
  --backend kind=openai_http,target=http://127.0.0.1:8123 \
  --profile kind=constant,rate=40,max_concurrency=4 \
  --constraint kind=max_duration,seconds=15 \
  --data kind=synthetic_text,prompt_tokens=32,output_tokens=16 \
  --tokenizer kind=huggingface_auto,model=tests/fixtures/tokenizers/minimal \
  --output kind=json,path=co.json
```

Comparing the reported percentiles against the same requests measured from `targeted_start` (n = 316, seconds):

| source | p50 | p95 | p99 |
| --- | --- | --- | --- |
| reported `request_latency` | 0.189 | 0.195 | 0.198 |
| `request_end - targeted_start` | 3.718 | 6.865 | 7.148 |

Reported p99 is 36x lower than the latency implied by the requested arrival schedule.

What the console shows for that run:

```
| Benchmark | Request Latency || TTFT         ||
| Strategy  | Sec             || ms           ||
|           | Mdn     | p95    | Mdn   | p95   |
|-----------|---------|--------|-------|-------|
| constant  | 0.2     | 0.2    | 110.5 | 115.8 |
```

The throughput table reports 20.0 req/s against a requested 40 req/s. The shortfall is not shown next to the requested rate, and no output mentions dispatch delay.

A control run at a sustainable rate (10 req/s, no concurrency cap) gives a mean dispatch delay of 0.003 s, so the effect above is not measurement noise.

### Where it comes from

`WorkerProcess._process_requests_loop` acquires the concurrency semaphore before asking the strategy for the next scheduled time:

https://github.com/vllm-project/guidellm/blob/963d1a15ad20337f41a28ab3b5e3ade6f73fb6d4/src/guidellm/scheduler/worker.py#L302-L303

The schedules themselves are correct. `AsyncConstantStrategy` and `AsyncPoissonStrategy` derive arrival times from a monotonic index/offset, so a stalled dispatch loop does not shift the schedule, and `targeted_start` remains the true intended arrival time. The data needed to detect this is already captured.

The omission is in the reporting layer:

- `GenerativeRequestStats.request_latency` = `request_end - request_start` ([request_stats.py#L103](https://github.com/vllm-project/guidellm/blob/963d1a15ad20337f41a28ab3b5e3ade6f73fb6d4/src/guidellm/schemas/request_stats.py#L103))
- `time_to_first_token_ms` = `first_token - request_start` ([request_stats.py#L162](https://github.com/vllm-project/guidellm/blob/963d1a15ad20337f41a28ab3b5e3ade6f73fb6d4/src/guidellm/schemas/request_stats.py#L162))
- `SchedulerMetrics.request_targeted_start_delay` does record `request_start - targeted_start`, but only as a running mean, with no distribution, and it is not printed by any console output.

For the run above that mean was 3.764 s, against a reported latency mean of 0.187 s.

### Why this is reachable on default settings

`sweep` is the default profile, and `SweepProfileArgs.max_concurrency` defaults to 512 ([sweep.py#L44](https://github.com/vllm-project/guidellm/blob/963d1a15ad20337f41a28ab3b5e3ade6f73fb6d4/src/guidellm/benchmark/profiles/sweep.py#L44)).

The cap binds hardest at the top of the sweep range, where the interpolated constant rates approach a throughput figure that was measured in closed-loop mode. An open-loop constant arrival process generally cannot sustain that rate, so the dispatch loop falls behind exactly in the region where tail latency matters most.

### Proposed fix

Surface the delay rather than redefine existing numbers:

1. Add a per-request dispatch delay and a targeted-start latency (`request_end - targeted_start`) to `GenerativeRequestStats`.
2. Expose both as `StatusDistributionSummary` on `GenerativeMetrics`, so they carry percentiles like every other metric.
3. Add them to the console latency table and the CSV output.

This change is purely additive. `request_latency`, `time_to_first_token_ms` and every other existing metric keep their current definitions and values, so historical comparisons and saved reports stay valid. The new fields are added alongside them, and new CSV columns are appended rather than inserted.

I am putting together a PR along these lines, including a regression test that asserts the delay stays near zero when the harness keeps up and grows when the cap binds. Happy to adjust the direction before I open it.


## 评论 (2)

### sjmonson · 2026-08-25

Hi, thanks for this issue. Its been on my TODO list to better surface scheduling delay so I look forward to your PR. I agree that it is better to define this as new metrics rather then rework the existing ones. One possible risk with this definition is concurrency driven workloads have a targeted start time of ASAP which will mean these metrics make no sense under `concurrent`, `throughput`, and `synchronous`. I prefer to omit metrics from the console output when they don't work under one of our core profiles.

### QHarshil · 2026-08-26

Thanks, that was a good catch and it changed how I approached this. Opened #1053.

Both metrics are out of the console latency table. I also went a step past that and gated them out of the compiled report. There is a new `SchedulingStrategy.defines_arrival_schedule` that is False for `synchronous`, `concurrent`, and `throughput`, and both metrics come back null for those instead of a zero-filled distribution. I went past console because `sweep` is the default profile and runs `throughput`, where every request targets the benchmark start time, so a default CSV would carry a `Scheduled Latency` column roughly equal to half the run duration. Someone reading the CSV never sees the docs caveat. If you would rather keep the raw values in the report and only suppress the console, that is a one property revert.

Two things I am unsure about.

I modelled applicability as a property of the strategy, but it is really a property of where a given request's `targeted_start` came from. A `trace` request with no relative timestamp falls back to the benchmark start and still gets counted, and multi-turn think time lands inside dispatch delay. Moving the signal onto `RequestTimings` per request would fix both and drop the branch in `GenerativeMetrics.compile()`, but it touches the worker dispatch path and adds a per-request field. Do you want that in this PR, or is the documented behaviour fine for now?

On naming, `request_dispatch_delay` is the same quantity as the existing `request_targeted_start_delay_avg`, just as a distribution over the measurement window instead of a running mean. I can rename it to `request_targeted_start_delay` so the two match if you prefer.

