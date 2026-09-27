# [Issue #1955] [ROCm] gfx1201 (Navi 48) support - compilation guide and known issues

source: https://github.com/bitsandbytes-foundation/bitsandbytes/issues/1955
state: closed | updated: 2026-07-08T23:34:15Z
labels: 

## 正文

### System Info

## bitsandbytes ROCm 編譯
 
### 踩坑 1：pip 安裝的版本不支援 ROCm
 
直接 `pip install bitsandbytes` 安裝的版本沒有 ROCm backend，必須從源碼編譯。
 
### 踩坑 2：multi-backend-refactor 分支有 bug
 
`multi-backend-refactor` 分支編譯出的 `.so` 缺少 `kOptimizer32bit1StateI12hip_bfloat16Li2E` 符號，導致 undefined symbol 錯誤。必須用 main 分支。
 
### 踩坑 3：gfx1153 無效 target ID
 
ROCm 6.3 的 CMake 模組內建了一個無效的 target `gfx1153`，必須在 cmake 前設定環境變數覆蓋：
 
```bash
export AMDGPU_TARGETS="gfx1201"
```
 
### 正確的編譯步驟
 
```bash
cd ~
git clone https://github.com/bitsandbytes-foundation/bitsandbytes.git
cd bitsandbytes
 
export PATH=/opt/rocm/bin:/usr/local/bin:$PATH
export AMDGPU_TARGETS="gfx1201"
 
cmake -DCOMPUTE_BACKEND=hip \
      -DCMAKE_BUILD_TYPE=Release \
      -DCMAKE_HIP_ARCHITECTURES="gfx1201" \
      -S . -B build
 
cmake --build build -j$(nproc)
pip3.11 install -e . --no-cache-dir
 
# 驗證
python3.11 -c "import bitsandbytes as bnb; print(bnb.__version__)"
```
 
### 踩坑 4：editable install 路徑問題
 
`pip install -e .` 之後，`bitsandbytes.__path__` 可能指向上層目錄而非模組目錄，導致 import 失敗。
 
解決方法：手動加入 PYTHONPATH：
 
```bash
echo 'export PYTHONPATH=/root/bitsandbytes:$PYTHONPATH' >> ~/.bashrc
```
 
### 踩坑 5：BNB_BACKEND 環境變數
 
推論時需要明確告知 bitsandbytes 使用 ROCm backend：
 
```python
import os
os.environ['BNB_BACKEND'] = 'rocm'
```
 
---

### Reproduction

## Environment

- **GPU**: AMD Radeon AI PRO R9700 (Navi 48 / gfx1201 / 32GB VRAM)
- **Host**: Proxmox VE 9.0.3 (LXC Container, Ubuntu 22.04)
- **ROCm**: 6.3.0
- **Python**: 3.11.15
- **PyTorch**: 2.9.1+rocm6.3
- **bitsandbytes**: 0.50.0.dev0 (compiled from source)

## Problem

pip-installed bitsandbytes has no ROCm backend for gfx1201 (Navi 48).
Must compile from source. Several issues encountered during compilation.

## Issue 1: gfx1153 invalid target ID

ROCm 6.3 CMake module includes `gfx1153` which is an invalid target ID,
causing cmake to fail:
clang++: error: invalid target ID 'gfx1153'

**Fix**: Set environment variable before cmake:

```bash
export AMDGPU_TARGETS="gfx1201"
```

## Issue 2: multi-backend-refactor branch missing symbol

Compiling from `multi-backend-refactor` branch produces a `.so` missing
`kOptimizer32bit1StateI12hip_bfloat16Li2E` symbol:
OSError: undefined symbol: _Z36__device_stub__kOptimizer32bit1StateI12hip_bfloat16Li2E...

**Fix**: Use `main` branch instead.

## Working Compilation Steps for gfx1201

```bash
git clone https://github.com/bitsandbytes-foundation/bitsandbytes.git
cd bitsandbytes

export AMDGPU_TARGETS="gfx1201"
export PATH=/opt/rocm/bin:$PATH

cmake -DCOMPUTE_BACKEND=hip \
      -DCMAKE_BUILD_TYPE=Release \
      -DCMAKE_HIP_ARCHITECTURES="gfx1201" \
      -S . -B build

cmake --build build -j$(nproc)
pip install -e .
```

## Issue 3: editable install path problem

After `pip install -e .`, `bitsandbytes.__path__` points to parent directory
instead of module directory, causing import to fail silently.

**Fix**:
```bash
export PYTHONPATH=/root/bitsandbytes:$PYTHONPATH
```

## Issue 4: BNB_BACKEND not auto-detected

Even with ROCm available, must explicitly set:
```python
import os
os.environ['BNB_BACKEND'] = 'rocm'
```

## Verification

```bash
python3 -c "
import sys
sys.path.insert(0, '/root/bitsandbytes')
import bitsandbytes as bnb
print(bnb.__version__)
print(bnb.supported_torch_devices)
"
# Output: 0.50.0.dev0
```

### Expected behavior

bitsandbytes should automatically detect ROCm backend and support gfx1201 (Navi 48) 
without requiring manual compilation from source or manual PYTHONPATH configuration.

Ideally:
1. pip install bitsandbytes should include ROCm support for gfx1201
2. AMDGPU_TARGETS should be auto-detected during cmake
3. BNB_BACKEND should be auto-detected when ROCm is available

## 评论 (5)

### Kaihui-AMD · 2026-05-26

Hi @UFO0506,
Thanks for the detailed writeup. A few clarifications based on testing on the same hardware (R9700 / gfx1201, ROCm 7.2.3):
Issue 1 (gfx1153): This affects ROCm 6.3.x only. On ROCm 7.2.x the compiler accepts gfx1153 without error and gfx1201 is already in bitsandbytes' default architecture list, so no AMDGPU_TARGETS override is needed.

Issue 3 (editable install path): Not reproducible on current main with ROCm 7.2.3 — bitsandbytes.__path__ points correctly to the module directory after pip install -e ..

Issue 4 (BNB_BACKEND): os.environ['BNB_BACKEND'] = 'rocm' has no effect — bitsandbytes doesn't read this env var. The backend auto-detects via torch.version.hip, no manual setting needed.

### UFO0506 · 2026-05-26

Hi @Kaihui-AMD,

Thank you for testing on the same hardware and providing those clarifications!

I've updated the guide based on your feedback:
- Marked AMDGPU_TARGETS, PYTHONPATH, and BNB_BACKEND workarounds as ROCm 6.3-only
- Added a ROCm 7.2.3 simplified path where most workarounds are no longer needed
- Added a version comparison table so users can quickly see what applies to them

Hoping this helps other R9700 users skip the painful parts. Thanks again! 🙏

### UFO0506 · 2026-05-26

<html>
<body>
<!--StartFragment--><html><head></head><body><h1>AMD Radeon AI PRO R9700 (gfx1201) ROCm 訓練環境完整踩坑紀錄</h1>
<blockquote>
<p>作者：UFO Homelab<br>
環境：Proxmox VE 9.0.3 + LXC Container + ROCm 6.3 → 7.2.3 + LLaMA-Factory<br>
模型：Qwen2.5-Coder-32B-Instruct QLoRA 4bit<br>
目的：讓後來的 R9700 用戶不用重踩相同的坑</p>
</blockquote>
<blockquote>
<p><strong>感謝 AMD 工程師 @chejh-amd 和 @Kaihui-AMD 在 GitHub issue 上提供的寶貴回饋與修正。</strong></p>
</blockquote>
<hr>
<h2>⚡ 速查：ROCm 版本對照</h2>

項目 | ROCm 6.3 | ROCm 7.2.3+
-- | -- | --
gfx1201 官方支援 | 部分 | ✅ 完整
AMDGPU_TARGETS 需要手動設定 | ✅ 需要 | ❌ 不需要
bitsandbytes PYTHONPATH 需要手動設定 | ✅ 需要 | ❌ 不需要
BNB_BACKEND 環境變數有效 | ✅ 需要 | ❌ 無效（自動偵測）
flash-attn composable_kernel | ❌ 編譯失敗 | ❌ 仍失敗
SDPA（AOTriton）加速 | ❌ 不支援 | ✅ 支援
訓練速度（32B QLoRA） | ~147 t/s | ~323 t/s


<hr>
<h2>十二、致謝</h2>
<p>感謝以下 AMD 工程師在 GitHub issue 上提供技術指引與修正：</p>
<ul>
<li><strong>@chejh-amd</strong>：指出 flash-attn 的正確替代方案（SDPA + AOTriton），並建議升級至 ROCm 7.2。</li>
<li><strong>@Kaihui-AMD</strong>：在相同硬體（R9700 / gfx1201 / ROCm 7.2.3）上驗證，並指出 ROCm 7.2.3 已修復多個 workaround。</li>
</ul>
<hr>
<p><em>整理自 2026 年 5 月的實際踩坑經驗</em><br>
<em>AMD Radeon AI PRO R9700 / gfx1201 / ROCm 6.3 → 7.2.3 / LLaMA-Factory 0.9.5</em></p></body></html><!--EndFragment-->
</body>
</html>

### sstamenk · 2026-07-07

Few comments regarding the points raised here:

1. ROCm 6.3 doesn't support gfx1151 or gfx1201. For a compatibility matrix with ROCm versions and their supported GPU architectures check [installation-from-pypirocm-pip](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/main/docs/source/installation.mdx#installation-from-pypirocm-pip). Consider upgrading your ROCm to a newer version.
2. `multi-backend-refactor` is deprecated and was used to originally enable the ROCm backend support. The up-to-date branch is `main`
3. `BNB_BACKEND` is not an environment variable that can be overridden by the user.

@matthewdouglas I recommend closing this issue as none of the points raised here are relevant. Consider reopening if the user is still experiencing issues with newer ROCm versions.

### matthewdouglas · 2026-07-08

I agree with @sstamenk here, and will close this issue. Our current PyPI wheels do target gfx1201 if you're using PyTorch built with ROCm 6.4+, so you shouldn't necessarily need to build from source.

The one concession I can give here is that maybe the default `AMDGPU_TARGETS` could be better auto-detected, especially to avoid setting it to include unsupported targets on older toolchains. But to be honest, I think it won't be long before we drop support for building with ROCm < 6.4 anyway, and in the meantime the workaround is to set it manually.

Please open a new issue if there's further problems with the latest bitsandbytes release or building from source from the `main` branch.
