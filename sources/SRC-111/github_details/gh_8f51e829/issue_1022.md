# [Issue #1022] Default `mp_context_type="fork"` segfaults all workers on macOS (supported platform); actionable hint was removed from the error message

source: https://github.com/vllm-project/guidellm/issues/1022
state: closed | updated: 2026-08-13T16:48:27Z
labels: good first issue, priority-high

## 正文

## Summary

On macOS, `guidellm run` fails immediately with every worker dying on signal 11. The cause is that `mp_context_type` defaults to `"fork"` unconditionally, overriding CPython's macOS default of `spawn`. The documented fix (`GUIDELLM__MP_CONTEXT_TYPE=spawn`) works perfectly — but the error message no longer points at it, so the failure looks like a hard crash rather than a one-variable configuration issue.

macOS is listed as a supported platform (`README.md`, `docs/getting-started/install.md`: *"Operating System: Linux or MacOS"*), so filing this as a defect rather than a platform limitation.

I could not find an existing issue that reports this. #559 is related but proposes a *global* switch to `forkserver` and does not mention macOS; it would not obviously close this.

## Environment

| | |
|---|---|
| guidellm | 0.7.3 |
| OS | macOS 26.5.2 (build 25F84) |
| Chip | Apple M4 Pro (arm64) |
| Python | 3.13.5 |
| platform | `macOS-26.5.2-arm64-arm-64bit-Mach-O` |
| torch / transformers / sanic | 2.13.0 / 5.15.0 / 25.12.1 |

Installed into a clean isolated environment via `uv run --no-project --with "guidellm==0.7.3"`.

## Reproduction

Terminal 1 — mock server (this part works fine; it doesn't use the worker group):

```bash
guidellm mock-server --host 127.0.0.1 --port 8012 --model gpt2 \
  --workers 4 --ttft-ms 5 --itl-ms 1 --output-tokens 16
```

Terminal 2 — benchmark against it:

```bash
guidellm run \
  --backend "kind=openai_http,target=http://127.0.0.1:8012" \
  --data "kind=synthetic_text,prompt_tokens=32,output_tokens=16" \
  --profile "kind=constant,rate=8" \
  --constraint "kind=max_duration,seconds=5" \
  --output "kind=json"
```

## Actual behaviour

Exit code 1, no output file produced. All ten workers die simultaneously:

```
File ".../guidellm/scheduler/worker_group.py", line 273, in create_processes
    raise RuntimeError(f"Worker process group startup failed: {detail}")
RuntimeError: Worker process group startup failed: Worker process 525 died unexpectedly
(signal 11); Worker process 526 died unexpectedly (signal 11); Worker process 527 died
unexpectedly (signal 11); ... Check system logs for details
```

## Expected behaviour

Either the benchmark runs, or the error names the setting that fixes it.

## Root cause

`src/guidellm/settings.py:93` sets the default with no platform branch:

```python
mp_context_type: Literal["spawn", "fork", "forkserver"] | None = "fork"
```

and `src/guidellm/scheduler/worker_group.py:188` consumes it directly:

```python
self.mp_context = get_context(settings.mp_context_type)
```

CPython changed the macOS default to `spawn` in 3.8 because `fork()` is unsafe there (Objective-C runtime initialisation across `fork()` without `exec()`); this default reverts that.

## Confirmed fix

```bash
GUIDELLM__MP_CONTEXT_TYPE=spawn guidellm run ...   # exit 0, benchmark completes, JSON written
```

Verified on the exact repro above — same command, same machine, only the env var added.

## The part that makes this hard to diagnose

The fix *is* documented, in `docs/guides/troubleshooting.md` under "macOS worker crash (signal 11)" (added in #860, thank you). But commit `06707a1d` ("Removed suggested action in failed sub-process message") stripped the inline hint out of the runtime error, so on 0.7.x the message ends at `"Check system logs for details"`.

The result is that the one place a user is guaranteed to be looking — the traceback — no longer mentions the variable that fixes it. Ten simultaneous SIGSEGVs read as a serious native crash, not a config default, so the natural next step is to go debugging rather than to go read the troubleshooting guide.

## Suggested fixes, in increasing order of ambition

1. **Restore the hint in the error.** Smallest possible change; recovers most of the lost diagnosability. Something like: `... Check system logs for details. On macOS, try GUIDELLM__MP_CONTEXT_TYPE=spawn (see docs/guides/troubleshooting.md).`
2. **Make the default platform-conditional** — `"fork"` on Linux, `"spawn"` on Darwin. Keeps the measured `fork` startup advantage on the platform where it's safe, and makes the supported platform work out of the box. (Distinct from #559, which proposes `forkserver` everywhere; both could land.)
3. **Warn at startup** when `mp_context_type == "fork"` on a non-Linux platform.

Happy to open a PR for (1) or (2) if you'd like — just say which you'd prefer.


## 评论 (2)

### sjmonson · 2026-08-12

Hey thinks for this issue. We haven't moved off of fork due to some startup performance issues which [we are working to solve](https://github.com/vllm-project/guidellm/pull/1016). In the meantime I think (1) and (2) are reasonable fixes. Looking into it I think for (2) the MP context should always be `spawn` on MacOS so if you want to contribute a fix just add a simple check where its set.

### nightcityblade · 2026-08-13

Hi, I'd like to work on the maintainer-approved macOS spawn check and restore the actionable error hint. I'll submit a focused PR shortly.
