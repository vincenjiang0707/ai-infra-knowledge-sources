# [Issue #2637] Bare tarfile.extractall into Predictable Cache During Build in flash-attention

source: https://github.com/Dao-AILab/flash-attention/issues/2637
state: closed | updated: 2026-07-12T17:55:57Z
labels: 

## 正文

## Summary

flash-attention's `hopper/setup.py` downloads NVIDIA toolchain archives (nvcc, ptxas) from NVIDIA CDN during build and extracts them with bare `tarfile.extractall(path=tmp_path)` into a predictable, user-home-rooted cache directory (`~/.flashattn/nvidia/<name>`) with no tar member filtering, no symlink validation, and a check-then-extract TOCTOU on the cache path.

A local attacker who pre-plants a symlink at `~/.flashattn/nvidia/nvcc` before `pip install flash-attn` (from source) causes `extractall` to write NVIDIA toolchain binaries through the symlink to an attacker-chosen directory — achieving arbitrary file write with the victim's privileges at build time.

## Affected Component

- **Repository**: <https://github.com/Dao-AILab/flash-attention>
- **File**: `hopper/setup.py`
- **Vulnerable function**: `download_and_copy()` (line 405-429)
- **Version**: latest main (as of 2026-06-09), including the FA4/hopper branch

### Realistic scenarios

| Scenario | Feasibility |
|---|---|
| Shared multi-user GPU build server | High — common in ML teams |
| CI/CD with shared home / persistent cache | High — `~/.flashattn` persists between jobs |
| Compromised lower-privilege service on same host | Medium — pre-plants symlink before victim builds |

## Vulnerability Details

### Vulnerable function: `download_and_copy()` (line 405-429)

```python
def download_and_copy(name, src_func, dst_path, version, url_func):
    flashattn_cache_path = get_flashattn_cache_path()          # ~/.flashattn
    ...
    tmp_path = os.path.join(flashattn_cache_path, "nvidia", name)  # ~/.flashattn/nvidia/nvcc
    ...
    src_path = os.path.join(tmp_path, src_path)
    download = not os.path.exists(src_path)                    # ← check (follows symlink)
    if download:
        file = tarfile.open(fileobj=open_url(url), mode="r|*")
        file.extractall(path=tmp_path)                         # ← bare extractall, no filter
    os.makedirs(os.path.split(dst_path)[0], exist_ok=True)
    ...
    shutil.copy(src_path, dst_path)                            # also copies from symlink-resolved path
```

### Cache path predictability

```python
def get_flashattn_cache_path():
    user_home = os.getenv("FLASH_ATTENTION_HOME") or os.getenv("HOME")
    return os.path.join(user_home, ".flashattn")   # ~/.flashattn — fully predictable
```

Cache path: `~/.flashattn/nvidia/nvcc` and `~/.flashattn/nvidia/ptxas` — known, stable, no randomization.

### No guards

- No `os.path.islink(tmp_path)` check
- No `os.makedirs(tmp_path, exist_ok=False)` (atomic creation)
- No `tarfile` extraction filter (`filter='data'` or member name validation)
- No integrity verification on extracted files (beyond what HTTPS provides for transport)

### Call site (line 472-480)

```python
download_and_copy(
    "nvcc", nvcc_src, nvcc_dst, NVIDIA_TOOLCHAIN_VERSION["nvcc"],
    lambda system, arch, version:
        f"https://developer.download.nvidia.com/compute/cuda/redist/cuda_nvcc/{system}-{arch}/cuda_nvcc-{system}-{arch}-{version}-archive.tar.xz",
)
download_and_copy(
    "ptxas", ...
)
```

Triggered during `pip install flash-attn` from source (Hopper/Blackwell builds) when CUDA ≥ 12.3 toolchain is needed.

## Attack Chain

1. Attacker creates `~/.flashattn/nvidia/nvcc` → symlink to `/target/dir` (e.g., victim's `~/.local/bin/`)
2. Victim runs `pip install flash-attn` (from source, on CUDA machine)
3. `download_and_copy("nvcc", ...)` checks `os.path.exists(src_path)` → False (target is empty)
4. Downloads legitimate NVIDIA nvcc tar from CDN
5. `file.extractall(path=tmp_path)` — `tmp_path` is symlink → writes nvcc binaries to attacker-chosen location
6. Impact: attacker-controlled location now contains executable binaries (or overwrites existing ones)

## Proof of Concept 

```python
import os, tarfile, io, tempfile
from pathlib import Path
FAKE_HOME = Path(tempfile.mkdtemp())
ATTACKER_TARGET = Path(tempfile.mkdtemp())
flashattn_cache = FAKE_HOME / ".flashattn"
tmp_path = flashattn_cache / "nvidia" / "nvcc"
tmp_path.parent.mkdir(parents=True, exist_ok=True)
os.symlink(str(ATTACKER_TARGET), str(tmp_path))
tar_buf = io.BytesIO()
with tarfile.open(fileobj=tar_buf, mode="w:xz") as tf:
    info = tarfile.TarInfo(name="cuda_nvcc-linux-x86_64-12.6.85-archive/bin/nvcc")
    data = b"#!/bin/bash\necho pwned"
    info.size = len(data)
    info.mode = 0o755
    tf.addfile(info, io.BytesIO(data))
tar_buf.seek(0)
file = tarfile.open(fileobj=tar_buf, mode="r|*")
file.extractall(path=str(tmp_path))  
assert (ATTACKER_TARGET / "cuda_nvcc-linux-x86_64-12.6.85-archive" / "bin" / "nvcc").exists()
```

## Suggested Fix

```python
def download_and_copy(name, src_func, dst_path, version, url_func):
    ...
    tmp_path = os.path.join(flashattn_cache_path, "nvidia", name)

    # Refuse symlinks
    if os.path.islink(tmp_path):
        raise RuntimeError(f"Refusing to extract to symlink: {tmp_path}")

    os.makedirs(tmp_path, exist_ok=True)

    src_path = os.path.join(tmp_path, src_path)
    download = not os.path.exists(src_path)
    if download:
        file = tarfile.open(fileobj=open_url(url), mode="r|*")
        # Use filter on Python 3.12+
        if hasattr(tarfile, 'data_filter'):
            file.extractall(path=tmp_path, filter='data')
        else:
            file.extractall(path=tmp_path)
    ...
```


## 评论 (1)

### AAtomical · 2026-06-10

#2641 
