# [Issue #1715] Windows Compile is broken... i fixed it

source: https://github.com/Dao-AILab/flash-attention/issues/1715
state: open | updated: 2026-06-01T11:14:00Z
labels: 

## 正文

The windows compile with MSVC is broken since somewhere after the last official release (2.7.4post1).


## Problem:
When compiling on Windows with MSVC, the following error occurs:
```
error: namespace "cutlass::platform" has no member "is_unsigned_v"
static_assert(cutlass::platform::is_unsigned_v<Storage>, "...");
```
This happens because is_unsigned_v is a C++17 feature, that Cutlass is encapsulating in its platform namespace but only exposes when the C++ flag has been set. Currently the Flashatt setup doesn’t pass the flags on Windows in a way that the MSVC understands it.


## Root Cause
The compilation flags are not correctly set for MSVC compiler (and only gcc/clang style flags are passed), so that the namespace is not exposing the feature over the Cutlass include.

The compiler need the correct G++17 flag and the cpluplus flag so that Cutlass exposes the platform type here:

https://github.com/NVIDIA/cutlass/blob/dc4817921edda44a549197ff3a9dcf5df0636e7b/include/cutlass/platform/platform.h#L526

## Solution:
Cutlass needs to receive the c++17 flag AND `/Zc:__cplusplus` flag to enable the presentation of the internal types.

## fix:

i created a PR that refactors the flag settings and adds the correct flags. All it does is set the MSVC-style g++17 flag and add the __cplusplus flag to the compiler and to nvcc (to pass to the host compiler) under windows so Cutlass can see it. The linux code path is untouched. The flags are only set if the OS is windows and the `DISTUTILS_USE_SDK` environ var is set, which is meant to be used for MSVC, this way mingw or other compilers are not affected  on windows.
 
PR is #1716 




## 评论 (10)

### drew1two · 2025-07-06

I can confirm the issue, and I can confirm that this change fixed the issue for me  👍 Thank you @loscrossos 

### Wallawalla47 · 2025-07-08

I spent so many hours troubleshooting and adding the few lines from this PR made everything finally work!  Thank you!

### david-littlefield · 2025-07-24

# Flash Attention Installation Guide for Windows 10

This is how I successfully installed Flash Attention on Windows 10. I have an NVIDIA GeForce RTX 3090. I'm using Python 3.10.6. It took about two hours to compile.

Thanks to **loscrossos** for the PR fix: https://github.com/Dao-AILab/flash-attention/issues/1715

## Prerequisites

1. Install **CUDA Toolkit 12.8**
2. Install **cuDNN 9.1.0**

## Option 1: Pre-compiled Wheel
**Quick install for Python 3.10.6, Windows AMD64, CUDA 12.8:**

Download the pre-compiled wheel: [flash_attn-2.8.0.post2-cp310-cp310-win_amd64.whl](https://drive.google.com/file/d/1GphzG0A47w-0TH1wy3HgCSUNOc0sVr4t/view?usp=sharing)

```cmd
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu128
pip install path/to/flash_attn-2.8.0.post2-cp310-cp310-win_amd64.whl
```

## Option 2: Build from Source

### Step 1: Set up Python Environment

Open **Command Prompt** and enter the following commands:

```cmd
cd %USERPROFILE%\Desktop
mkdir Demo
cd Demo
python -m venv venv
%USERPROFILE%\Desktop\Demo\venv\Scripts\activate
python -m pip install --upgrade pip
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu128
pip install "numpy<2.0" packaging ninja wheel setuptools
```

### Step 2: Clone Flash Attention with PR Fix

```cmd
git clone https://github.com/Dao-AILab/flash-attention.git
cd flash-attention
git fetch origin pull/1716/head:pr-1716
git checkout pr-1716
```

### Step 3: Install Visual Studio 2022

1. Go to: https://visualstudio.microsoft.com/downloads/
2. Download **Visual Studio 2022 Community**
3. Select **Desktop development with C++**
4. Click **Individual components**
5. Make sure the following components are selected:
   - MSVC v143 - VS 2022 C++ x64/x86 build tools
   - Windows 10 SDK (or Windows 11 SDK)
   - C++ CMake tools for Windows
6. Click **Install**

### Step 4: Compile Flash Attention

Open **x64 Native Tools Command Prompt for VS 2022** and enter the following commands:

```cmd
cd %USERPROFILE%\Desktop\Demo\flash-attention
%USERPROFILE%\Desktop\Demo\venv\Scripts\activate
set CUDA_PATH=C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.8
set CUDA_HOME=C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.8
set PATH=C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.8\bin;%PATH%
git config --global --add safe.directory %CD%
set DISTUTILS_USE_SDK=1
set MAX_JOBS=4
pip install . --no-build-isolation
```

### raffaelemancuso · 2025-09-18

I think this should be closed. The PR has been merged @tridao 

### mozophe · 2025-10-07

Not entirely sure if it is merged yet. I was facing this issue using: pip install flash-attn --no-build-isolation on Windows 11. 

I used the above instructions and it worked. I was getting filename too long error after using above fix. , so I had to add: git config --system core.longpaths true

The code is compiling right now, though it's taking a long time. I read somewhere that it will take about an hour.

### loscrossos · 2025-10-07

the fix is merged.
conpilation depends on how much RAM you have.

on a 64GB machine it takes 2 hours with 100% usage of my 16 cores...

or you can use the precompiled wheela from my github :)

### mozophe · 2025-10-08

On windows 11, I was still getting following error when I used pip install flash-attn --no-build-isolation

``` powershell
error: namespace "cutlass::platform" has no member "is_unsigned_v"
static_assert(cutlass::platform::is_unsigned_v<Storage>, "...");
``` 
After using the above fix, the issue got resolved and I compiled successfully. 

Hence, the assumption that it's not merged yet.


### loscrossos · 2025-10-08

pip install gets the source code from pypi, which is an okder code version.
you need the latest code from this repo.

### Hunter-Will · 2026-06-01

What's the use of `DISTUTILS_USE_SDK` in line 225. I don't have this envir set on my win 11 and have to remove it from the `setup.py` to enable this fix.

### loscrossos · 2026-06-01

distutilsdk ist a variable that indicates you are using msvc. the fix is for msvc so you should not remove but use it.
the msvc env console uses/needs it

it ensures the code does not interfer with other windows compilers like mingw which might bow be conpatible with this code.
