# [Issue #4773] [Bug][v0.6.18rc9] Fatal Python error: Segmentation fault

source: https://github.com/flashinfer-ai/flashinfer/issues/4773
state: closed | updated: 2026-09-21T04:31:10Z
labels: needs-triage, ci: health

## 正文

## Summary
FlashInfer 0.6.18rc9 (eadfae36) CI reports a unknown infra affecting 1 failed job(s). The saved evidence covers B300 / cu130 in flashinfer-ci.

## CI environment

- Commit: eadfae36
- Branch: release-v0.6.18
- Pipeline: [#64780358](https://nv/flashinfer-ci/-/pipelines/64780358)
- Affected scope: 1 failed job(s)
- Failed jobs:
  - [unit_test_b300: [cu130]](https://nv/flashinfer-ci/-/jobs/413687941)

> tests/utils/test_logging_replay.py
> tests/gemm/test_mm_fp8.py

## Failure

```text
Thread 0x00007ffc398fc6c0 (most recent call first):
  File "/opt/conda/envs/flashinfer/lib/python3.10/threading.py", line 324 in wait
  File "/opt/conda/envs/flashinfer/lib/python3.10/threading.py", line 607 in wait
  File "/opt/conda/envs/flashinfer/lib/python3.10/site-packages/tqdm/_monitor.py", line 69 in run
  File "/opt/conda/envs/flashinfer/lib/python3.10/threading.py", line 1016 in _bootstrap_inner
  File "/opt/conda/envs/flashinfer/lib/python3.10/threading.py", line 973 in _bootstrap

Current thread 0x00007ffff7ca8740 (most recent call first):
  File "/workspace/flashinfer/flashinfer/trtllm_low_latency_gemm.py", line 126 in forward
  File "/workspace/flashinfer/flashinfer/autotuner/autotuner.py", line 737 in __call__
  File "/workspace/flashinfer/flashinfer/autotuner/autotuner.py", line 2177 in _profile_single_kernel
  File "/workspace/flashinfer/flashinfer/autotuner/autotuner.py", line 1788 in choose_one
  File "/workspace/flashinfer/flashinfer/trtllm_low_latency_gemm.py", line 196 in trtllm_low_latency_gemm
  File "/workspace/flashinfer/flashinfer/gemm/gemm_base.py", line 4738 in mm_fp8
  File "/workspace/flashinfer/flashinfer/api_logging.py", line 2513 in wrapper
  File "/workspace/flashinfer/flashinfer/api_logging.py", line 2333 in _auto_dump_wrapper
  File "/workspace/flashinfer/tests/utils/test_logging_replay.py", line 187 in test_mm_fp8_replay
  File "/opt/conda/envs/flashinfer/lib/python3.10/site-packages/_pytest/python.py", line 167 in pytest_pyfunc_call
  File "/opt/conda/envs/flashinfer/lib/python3.10/site-packages/pluggy/_callers.py", line 121 in _multicall
  File "/opt/conda/envs/flashinfer/lib/python3.10/site-packages/pluggy/_manager.py", line 120 in _hookexec
  File "/opt/conda/envs/flashinfer/lib/python3.10/site-packages/pluggy/_hooks.py", line 512 in __call__
  File "/opt/conda/envs/flashinfer/lib/python3.10/site-packages/_pytest/python.py", line 1707 in runtest
  File "/opt/conda/envs/flashinfer/lib/python3.10/site-packages/_pytest/runner.py", line 184 in pytest_runtest_call
  File "/opt/conda/envs/flashinfer/lib/python3.10/site-packages/pluggy/_callers.py", line 121 in _multicall
  File "/opt/conda/envs/flashinfer/lib/python3.10/site-packages/pluggy/_manager.py", line 120 in _hookexec
  File "/opt/conda/envs/flashinfer/lib/python3.10/site-packages/pluggy/_hooks.py", line 512 in __call__
  File "/opt/conda/envs/flashinfer/lib/python3.10/site-packages/_pytest/runner.py", line 250 in <lambda>
  File "/opt/conda/envs/flashinfer/lib/python3.10/site-packages/_pytest/runner.py", line 361 in from_call
  File "/opt/conda/envs/flashinfer/lib/python3.10/site-packages/_pytest/runner.py", line 249 in call_and_report
  File "/opt/conda/envs/flashinfer/lib/python3.10/site-packages/_pytest/runner.py", line 139 in runtestprotocol
  File "/opt/conda/envs/flashinfer/lib/python3.10/site-packages/_pytest/runner.py", line 118 in pytest_runtest_protocol
  File "/opt/conda/envs/flashinfer/lib/python3.10/site-packages/pluggy/_callers.py", line 121 in _multicall
  File "/opt/conda/envs/flashinfer/lib/python3.10/site-packages/pluggy/_manager.py", line 120 in _hookexec
  File "/opt/conda/envs/flashinfer/lib/python3.10/site-packages/pluggy/_hooks.py", line 512 in __call__
  File "/opt/conda/envs/flashinfer/lib/python3.10/site-packages/_pytest/main.py", line 408 in pytest_runtestloop
  File "/opt/conda/envs/flashinfer/lib/python3.10/site-packages/pluggy/_callers.py", line 121 in _multicall
  File "/opt/conda/envs/flashinfer/lib/python3.10/site-packages/pluggy/_manager.py", line 120 in _hookexec
  File "/opt/conda/envs/flashinfer/lib/python3.10/site-packages/pluggy/_hooks.py", line 512 in __call__
  File "/opt/conda/envs/flashinfer/lib/python3.10/site-packages/_pytest/main.py", line 384 in _main
  File "/opt/conda/envs/flashinfer/lib/python3.10/site-packages/_pytest/main.py", line 330 in wrap_session
  File "/opt/conda/envs/flashinfer/lib/python3.10/site-packages/_pytest/main.py", line 377 in pytest_cmdline_main
  File "/opt/conda/envs/flashinfer/lib/python3.10/site-packages/pluggy/_callers.py", line 121 in _multicall
  File "/opt/conda/envs/flashinfer/lib/python3.10/site-packages/pluggy/_manager.py", line 120 in _hookexec
  File "/opt/conda/envs/flashinfer/lib/python3.10/site-packages/pluggy/_hooks.py", line 512 in __call__
  File "/opt/conda/envs/flashinfer/lib/python3.10/site-packages/_pytest/config/__init__.py", line 229 in _main
  File "/opt/conda/envs/flashinfer/lib/python3.10/site-packages/_pytest/config/__init__.py", line 253 in _console_main
  File "/opt/conda/envs/flashinfer/lib/python3.10/site-packages/pytest/__main__.py", line 9 in <module>
  File "/opt/conda/envs/flashinfer/lib/python3.10/runpy.py", line 86 in _run_code
  File "/opt/conda/envs/flashinfer/lib/python3.10/runpy.py", line 196 in _run_module_as_main
```

## Reproduction

No reliable pytest node ID is available in the saved CI evidence; use the linked job log to recover the invocation.

## Case History
- 1 confirmed failure pipeline(s); first seen 2026-08-27, last seen 2026-08-27.
- 2026-08-27 — 0.6.18rc9 (eadfae36) — B300 / cu130 — [pipeline #64780358](https://nv/flashinfer-ci/-/pipelines/64780358) / [job](https://nv/flashinfer-ci/-/jobs/413687941)



## 评论 (1)

### bkryu · 2026-08-31

Closing issue as it pertains to an rc version of 0.6.18 and 0.6.18 has been released
