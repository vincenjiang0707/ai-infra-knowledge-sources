# [Issue #3088] Bug:  Py_LIMITED_API=0x03080000 incompatible with Cython 3.3+

source: https://github.com/tile-ai/tilelang/issues/3088
state: closed | updated: 2026-08-26T19:24:50Z
labels: 

## 正文



## Description
The CMake build sets `-DPy_LIMITED_API=0x03080000` (Python 3.8 Limited API) for the Cython wrapper target (`tilelang_cython_wrapper`). Cython 3.3.0 introduced a strict compile-time check that requires `Py_LIMITED_API` to be at least `0x03090000` (Python 3.9):
tilelang_cython_wrapper.cpp:70:8: 

error: #error "Cython 3.3 requires the Python Limited API version to be 3.9 or greater."


This affects all current releases (tested 0.1.10, 0.1.12, 0.1.13).
## Steps to reproduce
1. Install Cython >= 3.3.0
2. Build tilelang from source (any recent tag)
3. Observe the `#error` from the generated Cython wrapper
## Suggested fix
Bump `Py_LIMITED_API` from `0x03080000` to `0x03090000` in the CMakeLists.txt where the Cython wrapper target is defined. Since tilelang already requires Python 3.9+, this should be a safe change.
## Workaround
Pin `cython<3.3.0` in build requirements.
## Environment
- tilelang: 0.1.10 / 0.1.12 / 0.1.13
- Cython: 3.3.0
- Python: 3.12
- GCC: 14 (gcc-toolset-14)
- OS: RHEL 9 (UBI9)

## 评论 (1)

### LeiWang1999 · 2026-08-26

closed as has been resolved via pr #3068 , will soon release version 0.1.14:)
