# [Issue #310] undefined symbol

source: https://github.com/NVIDIA/nccl-tests/issues/310
state: closed | updated: 2025-05-23T10:58:56Z
labels: 

## 正文

# python tests/test_intranode.py
....

miniconda3/lib/python3.9/site-packages/deep_ep-1.0.0+d5ca449-py3.9-linux-x86_64.egg/deep_ep_cpp.cpython-39-x86_64-linux-gnu.so: undefined symbol: _ZNSt15__exception_ptr13exception_ptr9_M_addrefEv

## 评论 (1)

### AddyLaddy · 2025-05-21

Why do you believe this is an issue with nccl-tests ?

