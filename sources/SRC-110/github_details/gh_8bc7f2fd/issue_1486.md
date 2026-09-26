# [Issue #1486] HumanEval / LiveCodeBench local code-execution scoring silently returns 0 on Windows

source: https://github.com/modelscope/evalscope/issues/1486
state: closed | updated: 2026-07-15T10:48:53Z
labels: 

## 正文

On Windows, time_limit() in evalscope/benchmarks/humaneval/utils.py calls signal.setitimer(signal.ITIMER_REAL, ...) / signal.SIGALRM, which don't exist on Windows. Entering the context raises AttributeError, which is caught by the except BaseException around exec() and recorded as failed: ..., so every sample scores as failed and pass@k aggregates to 0 with no error surfaced. The outer process-level timeout (p.join(timeout+1) + p.kill()) already enforces the time limit, so the inner signal-based timeout is redundant on Windows and can be platform-guarded without losing the limit. evalscope/benchmarks/live_code_bench/testing_util.py has the same pattern. Reproduced on Windows 11. Happy to open a PR with a platform guard + a small test.

## 评论 (2)

### Yunnglin · 2026-07-14

Thanks for the detailed report. This is related to earlier Windows local code-execution issues: #595 for LiveCodeBench and #733 for HumanEval. At that time the workaround was to use Linux/WSL, and later we added sandbox-based code execution as the recommended path.

Your proposed platform guard is still useful for the native local execution path. Please feel free to open a PR. It would be great to cover both the HumanEval `setitimer`/`SIGALRM` path and all LiveCodeBench `signal.alarm()` usages, while keeping the current signal-based timeout behavior on POSIX platforms.


### toffee-desuwa · 2026-07-14

Thanks @Yunnglin, that makes sense — the sandbox path is the right default, and the platform guard is just for the native local-execution path. I'm already working on a PR for it. It covers both the HumanEval setitimer/SIGALRM path and all LiveCodeBench signal.alarm() usages, keeps the existing signal-based timeout behavior unchanged on POSIX, and adds regressions for the native path on platforms without POSIX interval timers. I'll open it shortly.
