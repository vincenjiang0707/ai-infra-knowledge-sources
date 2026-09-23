# [Issue #4944] [Bug] TurboMind SIGSEGV crash-loop triggered by session_len truncation path (deterministic libc offset across 3 crashes)

source: https://github.com/InternLM/lmdeploy/issues/4944
state: open | updated: 2026-09-08T07:22:01Z
labels: 

## 正文

## Describe the bug

`lmdeploy serve api_server` (TurboMind backend) crashes with **SIGSEGV (general protection fault)** three times within ~21 minutes, always right after the engine logs the `total sequence length ... exceeds session_len ...` truncation warning. All three crashes fault at the **exact same offset relative to `libc.so.6`'s load base** (`+0x898`), captured via kernel `dmesg`:

```
[Tue Sep  8 10:05:32 2026] traps: lmdeploy[3838286] general protection fault ip:7f8304036898 sp:7f7fde7fa710 error:0 in libc.so.6[7f8304036000+195000]
[Tue Sep  8 10:22:12 2026] traps: lmdeploy[1527189] general protection fault ip:7f4d7fb5e898 sp:7f4a4affb710 error:0 in libc.so.6[7f4d7fb5e000+195000]
[Tue Sep  8 10:27:21 2026] traps: lmdeploy[1529722] general protection fault ip:7fb473700898 sp:7fb13dff9710 error:0 in libc.so.6[7fb473700000+195000]
```

`0x36898-0x36000 = 0x898`, `0xb5e898-0xb5e000 = 0x898`, `0x700898-0x700000 = 0x898` — identical offset every time, i.e. the same code path is deterministically hit, not random memory corruption.

Right before each crash, the container log shows the same `session_len` truncation warning **with the exact same total sequence length (248117 tokens)**:

```
[TM][WARN][0908.02:22:32.413606][engine.cc:402] ID 14: total sequence length (248117 + 32000) exceeds `session_len` (262144), `max_new_tokens` is truncated to 14027
[TM][WARN][0908.02:24:23.961176][engine.cc:402] ID  0: total sequence length (248117 + 32000) exceeds `session_len` (262144), `max_new_tokens` is truncated to 14027
[TM][WARN][0908.02:29:48.526816][engine.cc:402] ID  2: total sequence length (248117 + 32000) exceeds `session_len` (262144), `max_new_tokens` is truncated to 14027
```

The token count (248117) is identical across all three occurrences — this is the **same client request being retried** by an upstream gateway/client after each 500, not three independent long-context requests. Each retry re-triggers the truncation path and crashes the process again, forming a crash loop (Docker `restart: unless-stopped` brings the container back up, the client retries, it dies again).

Container `docker events` confirms `exitCode=139` (128+11=SIGSEGV) for both observed deaths, with `execDuration` showing the **second crash occurred in under 1 second after the container restarted** (997ms), i.e. the very first request served after restart immediately reproduced the fault:

```
... container die ... execDuration=907573 ... exitCode=139 ...   (first crash, ~15min uptime)
... container start ...
... container die ... execDuration=997 ... exitCode=139 ...      (second crash, <1s after restart)
... container start ...
```
(third crash ~3m46s after that restart, same fault signature via dmesg)

No Python-level traceback appears in container stdout for any of the three crashes — consistent with a native (C++/libc) segfault that bypasses Python's exception handling entirely.

## Related existing issues

This looks like the same underlying defect class as:
- #2099 (open, unassigned follow-up) — `total sequence length (2357+30419) exceeds session_len (32776)` warning immediately followed by a core-dump crash.
- #4021 (closed, no visible fix/discussion) — `total sequence length (66+1982) exceeds session_len (2048)` warning immediately followed by `CUDA runtime error: misaligned address` at `LlamaBatch.cc:1153`, with `--enable-prefix-caching` enabled (same as our deployment).

Neither issue reached a confirmed root cause. This report adds: (1) a newer LMDeploy version (0.15.0) where the bug still reproduces, (2) a deterministic fault signature (identical libc offset across independent occurrences) rather than a single anecdotal crash, and (3) confirmation that it's reproducible by simply retrying the *same* request that hit the truncation path — a single specific token count (248117) reliably kills the engine every time.

## Reproduction

We don't yet have the exact prompt content (it belongs to an end user's live coding-agent session and wasn't captured before the client abandoned/reset it), only the resulting total sequence length. We're filing this now with what we captured live, and can follow up with a minimal repro if we manage to reconstruct a request that hits `session_len` truncation deterministically. If anyone with knowledge of the truncation code path (`engine.cc:402` and whatever queues/allocates the truncated generation afterward) wants to inspect the corresponding logic, the two prior issues plus this one strongly suggest the bug lives in how a truncated `max_new_tokens` is handled after the warning is logged, not in prompt processing itself.

Environment/config known to reproduce:
- `--session-len 262144`, `--max-prefill-token-num 4096`, `--cache-max-entry-count 0.9`, `--enable-prefix-caching`, `--tp 4`, `--max-batch-size 4`, `--max-concurrent-requests 4`, `--backend turbomind`
- A request whose `prompt_tokens + requested max_tokens` exceeds `session_len` by a wide margin (here: 248117 + 32000 vs. limit 262144, i.e. request asked for far more headroom than available, triggering a large truncation from 32000 → 14027).

## Environment

- LMDeploy: `0.15.0` (`pip show lmdeploy` inside container)
- Docker image: `openmmlab/lmdeploy:v0.15.0-cu12.8` (`sha256:c5778456f48f0aed77f2505280d0a5afcd9458c141c49000a6edc3d793c96c65`)
- Backend: TurboMind
- PyTorch: `2.10.0+cu128`, CUDA runtime `12.8`
- GPU: 4× Tesla V100-SXM2-16GB, driver `580.178.04`
- Host OS: Ubuntu 22.04.5 LTS (container), Linux kernel host (`dmesg` capture)
- Model: `cyankiwi/Qwen3.8-27B-AWQ-INT4` — `Qwen3_5ForConditionalGeneration`, Dense, 64-layer hybrid (linear:full attention = 3:1), `compressed-tensors` `pack-quantized` format, `group_size=32`, W4A16
- `--tp 4` (tensor parallel across all 4 GPUs)

## Additional context

The engine was under sustained load (KV cache regularly at 90-99% utilization) in the hours around the crash, but the crash signature correlates strongly with the specific over-limit request/truncation event, not with KV cache pressure in general — we saw the same 90%+ KV cache utilization at other times with no crash.

Happy to provide full container logs / `dmesg` output / `docker inspect` dumps if useful.


## 评论 (1)

### zambalee · 2026-09-08

## Update: appears fixed in v0.17.0-cu12.8

We upgraded this deployment from `v0.15.0-cu12.8` to `v0.17.0-cu12.8` (same model, same flags otherwise) and re-tested.

Right before the upgrade window, the bug fired again independently on v0.15.0 in production (same fault signature — identical libc.so.6 offset `+0x898` as the original three crashes above), confirming this is an actively-recurring issue for us, not a one-off.

After upgrading to v0.17.0, we constructed 4 synthetic requests deliberately shaped to hit the same code path: prompt_tokens close to `session_len` (245512–248571, same order of magnitude as our original 248117 crash) plus `max_tokens=32000`, which reliably triggers the `total sequence length ... exceeds session_len ... max_new_tokens is truncated` warning. All 4 requests hit that exact log line and then **completed normally** (`HTTP 200`, `finish_reason: stop`) — container `RestartCount` stayed at 0 throughout, and `dmesg` showed no new general-protection-fault entries.

We can't rule out that our synthetic requests aren't byte-identical to whatever real request originally crashed the engine (we never captured the exact original prompt content), so this isn't a 100% certain fix confirmation — but it's a meaningful signal that whatever regressed the truncation path between 0.15.0 and 0.17.0 may have been fixed along the way. We'll keep monitoring production traffic and report back if it recurs on 0.17.0.

Environment for this test: same as above except `openmmlab/lmdeploy:v0.17.0-cu12.8`, 4× Tesla V100-SXM2-16GB, `--tp 4`.

