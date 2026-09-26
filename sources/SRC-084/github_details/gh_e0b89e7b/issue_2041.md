# [Issue #2041] get_gaudi_sw_version() hangs indefinitely on Windows — module-level subprocess.run with shell pipe to grep

source: https://github.com/bitsandbytes-foundation/bitsandbytes/issues/2041
state: open | updated: 2026-08-17T18:15:23Z
labels: Duplicate, Windows, Proposing to Close

## 正文

### System Info

- OS: Windows 11
- Python: 3.12.10 (embedded / python_embeded, ComfyUI portable)
- bitsandbytes: < 0.49.1>
- torch: 2.11.0+cu130
- GPU: NVIDIA RTX 5090 (32GB), driver 610.74
- No Intel Gaudi / Habana hardware present

### Reproduction

On Windows, importing bitsandbytes hangs indefinitely and intermittently.

Minimal reproducer:

    python -c "import bitsandbytes"

`backends/utils.py` executes this at module level:

    output = subprocess.run(
        "pip list | grep habana-torch-plugin",
        shell=True, text=True, capture_output=True,
    )
    ...
    GAUDI_SW_VER = get_gaudi_sw_version()

Three issues on Windows:
1. `grep` does not exist. cmd.exe still spawns `pip list`, whose output is piped nowhere.
2. No `timeout=` argument, so the call can block forever.
3. It runs at import time, freezing the entire host process with no traceback.

faulthandler dump of the hung thread:

    File "threading.py", line 1169 in _wait_for_tstate_lock
    File "threading.py", line 1149 in join
    File "subprocess.py", line 1628 in _communicate
    File "subprocess.py", line 1209 in communicate
    File "subprocess.py", line 550 in run
    File "bitsandbytes/backends/utils.py", line 71 in get_gaudi_sw_version
    File "bitsandbytes/backends/utils.py", line 84 in <module>
    File "bitsandbytes/backends/default/ops.py", line 9 in <module>
    File "bitsandbytes/__init__.py", line 19 in <module>

Impact: silent, intermittent startup freeze of ComfyUI. No exception, no log
output, no traceback. Isolating this took several hours.

### Expected behavior

Importing bitsandbytes should never block. Detecting optional Habana/Gaudi
software should not shell out at import time, and should fail fast when the
hardware is absent.

Suggested fix — query package metadata instead of spawning a shell. Same
result, no subprocess, cross-platform:

    def get_gaudi_sw_version():
        from importlib.metadata import PackageNotFoundError, version as _pkg_version
        try:
            return version.parse(_pkg_version("habana-torch-plugin"))
        except PackageNotFoundError:
            return None

I have this patch running locally and it resolves the hang (5/5 clean starts,
previously ~50% failure rate). Happy to open a PR.

## 评论 (1)

### matthewdouglas · 2026-08-17

Hi,

This should have been resolved with #1910 and is included in bitsandbytes>=0.50.0. Please try with the latest release.
