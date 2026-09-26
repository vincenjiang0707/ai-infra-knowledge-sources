# [Issue #2799] Flash Attention install with Triton backend replaces preinstalled Triton no matter what.

source: https://github.com/Dao-AILab/flash-attention/issues/2799
state: open | updated: 2026-08-18T05:57:14Z
labels: 

## 正文

Some context here, my GPU is an AMD Radeon AI PRO R9700. This GPU requires a specific build of Triton (currently, triton-3.7.0+git1bff1d9d.rocm7.13.0a20260416 from https://rocm.nightlies.amd.com/v2/gfx120X-all/) for use with ComfyUI. The problem is that Flash Attention quietly (atleast in the command stdout) pulls AITER as a git submodule in the setup.py, the default build of which will replace your preinstalled Triton with "3.7.1". I would recommend passing "AITER_USE_SYSTEM_TRITON=1" to the AITER build if Triton is detected as already being installed.

I believe the relevant code in setup.py is this: (although I may be wrong)
```python
if ROCM_BACKEND == "triton":
        if os.path.isdir(".git"):
            subprocess.run(["git", "submodule", "update", "--init", "third_party/aiter"], check=True)
        else:
            assert os.path.isdir("third_party/aiter"), (
                "third_party/aiter is missing, please use source distribution or git clone"
            )
        subprocess.run(
            [sys.executable, "-m", "pip", "install", "--no-build-isolation", "third_party/aiter"],
            check=True,
        )
```

Steps to recreate:
1. Install any Triton version besides 3.7.1.
2. Run the recommended command: `FLASH_ATTENTION_TRITON_AMD_ENABLE="TRUE" pip install --no-build-isolation .`
3. Check the current Triton version. (`pip list | grep triton` or similar command)

## 评论 (2)

### HimeLexie · 2026-08-16

Relevant documentation from AITER:
<img width="858" height="236" alt="Image" src="https://github.com/user-attachments/assets/a9ffc5c3-9304-40e2-9be1-412ed5030acf" />

### liminfei-amd · 2026-08-18

I reproduced the replacement path on current main and opened #2806 with a fix that preserves an installed Triton when FlashAttention installs vendored AITER. Explicit replacement and fresh-install behavior remain available, and the installation examples now document both choices. This complements #2720, which reuses an installed AITER package instead of the vendored copy.
