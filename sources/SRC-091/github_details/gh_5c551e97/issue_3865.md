# [Issue #3865] [Feature] Provide collect_env.py script for automatic environment reporting in bug issues

source: https://github.com/LMCache/LMCache/issues/3865
state: closed | updated: 2026-09-25T01:46:37Z
labels: stale

## 正文

**Label**
`[Feature]`

**Summary**
Provide a `collect_env.py` script (or built-in CLI command) to automatically collect and format all relevant environment information for bug reproduction reports, eliminating manual copy-paste of dependency versions.

**Details**
Currently, when users submit bug issues to reproduce LMCache behavior, they must manually fill in environment details such as:

- LMCache version (e.g., `0.4.5`)
- Integration versions (`lmcache_vllm`, `lmcache_sglang`)
- Backend versions (vLLM, SGLang, Dynamo)
- Python version
- CUDA / GPU info
- OS and platform
- Git commit hash (if running from source)
- LMCache YAML config

This is error-prone and inconsistent. Many issues lack critical version info, slowing down triage. A single script that collects all of this and outputs GitHub-ready Markdown would standardize reproduction reports and reduce friction for both reporters and maintainers.

**Steps / Reproduction (if applicable)**
1. User encounters a bug and wants to file an issue.
2. User runs `python -m lmcache.collect_env` (or `python collect_env.py` from repo).
3. Script auto-detects:
   - `lmcache.__version__`
   - `vllm.__version__` / `sglang.__version__`
   - PyTorch / CUDA / GPU names
   - Python & OS info
   - Git commit (if inside LMCache repo)
   - Active LMCache config file content (if `LMCACHE_CONFIG_FILE` is set)
4. Script prints Markdown block ready to paste into issue template under "Environment" or "To Reproduce".

**Expected Outcome / Goal**
- A single command outputs a pre-formatted Markdown block containing all environment metadata.
- Reduces issue filing time from ~5 minutes of manual copy-paste to &lt;10 seconds.
- Improves issue quality and reproducibility for maintainers.
- Can be referenced in the bug report template (e.g., "Run `python -m lmcache.collect_env` and paste output below").

**Actual Outcome (if applicable)**
No such script exists. Users manually type versions, often omitting critical fields (e.g., exact commit hash, vLLM/SGLang version mismatch, CUDA driver vs. runtime version).

**Additional Context**
- Reference implementation: vLLM's [`collect_env.py`](https://github.com/vllm-project/vllm/blob/main/collect_env.py) which is widely used across the ecosystem.
- The script should be lightweight (no heavy imports unless needed) and safe to run in any environment (WSL2, bare metal, containers).
- Suggested CLI: `python -m lmcache.collect_env` or `lmcache-collect-env`.
- Optional: Add `--json` flag for programmatic CI / automation use.

## 评论 (6)

### fengxiaohu · 2026-06-24

#3720 or we can use cli intead of shell script


### deng451e · 2026-06-24

this is good idea for cli usage, looking forward to the pr. 

### fengxiaohu · 2026-06-25

I can contribute this. @deng451e 


### fengxiaohu · 2026-06-25

I check the  bug report template,https://github.com/LMCache/LMCache/issues/1768.
here are plans(without CLI just scripts).

see PR #3874 

# LMCache Environment Reporting Script Plan

**Summary**
Create only an importable/runnable environment collection script for LMCache. No CLI command, no `pyproject.toml` entry point, and no CLI docs integration.

**Key Changes**
- Create `lmcache/collect_env.py`.
- Support running with:
  - `python -m lmcache.collect_env`
  - `python lmcache/collect_env.py`
- Include public helpers:
  - `get_env_info()`
  - `pretty_str(envinfo)`
  - `get_pretty_env_info()`
  - `main()`
- Adapt vLLM/PyTorch-style reporting for LMCache:
  - System info: OS, libc, Python, platform, CPU, GCC, Clang, CMake.
  - PyTorch info: version, debug build, CUDA/HIP/XPU build/runtime state.
  - Accelerator info: CUDA GPU, Nvidia driver, cuDNN, ROCm/HIP/MIOpen, XPU/SYCL where available.
  - LMCache info: LMCache version/commit if available, detected package state, relevant build/env flags.
  - Relevant packages from `pip list`/`conda list`.
  - Sanitized environment variables for `LMCACHE`, `TORCH`, `PYTORCH`, `CUDA`, `NCCL`, `NIXL`, `ROCM`, `HIP`, `CUDNN`, `OMP_`, `MKL_`, `SYCL`, `ONEAPI`, `ZE_`, etc.
- Filter env vars containing secret-like terms such as `secret`, `token`, `api`, `access`, `password`, `key`, or `credential`.

**Tests**
- Add `tests/test_collect_env.py` only.
- Cover:
  - Script does not raise when optional commands are unavailable.
  - Secret-like env vars are excluded.
  - LMCache diagnostic env vars are included.
  - `get_pretty_env_info()` returns required report sections.
  - `main()` prints a usable report.

**Verification**
- Run:
  - `pytest -xvs tests/test_collect_env.py`
  - `ruff check lmcache/collect_env.py tests/test_collect_env.py`
- No docs build is required because this revision does not change docs.


### github-actions[bot] · 2026-08-25

This issue has been automatically marked as stale because it has not had activity within 60 days. It will be automatically closed if no further activity occurs within 30 days.

### github-actions[bot] · 2026-09-25

This issue has been automatically closed due to inactivity. Please feel free to reopen if you feel it is still relevant!
