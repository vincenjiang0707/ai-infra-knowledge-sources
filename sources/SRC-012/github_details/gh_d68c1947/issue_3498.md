# [Issue #3498] [Bug] macos - libtvm.dylib not found

source: https://github.com/mlc-ai/mlc-llm/issues/3498
state: closed | updated: 2026-07-21T21:49:07Z
labels: bug

## 正文

## 🐛 Bug
mlc-llm libtvm.dylib not found
```
❯ python -c "import mlc_llm; print(mlc_llm)"
Traceback (most recent call last):
  File "<string>", line 1, in <module>
  File "/Users/.../miniconda3/envs/mlc-chat-venv/lib/python3.11/site-packages/mlc_llm/__init__.py", line 8, in <module>
    from . import protocol, serve
  File "/Users/.../miniconda3/envs/mlc-chat-venv/lib/python3.11/site-packages/mlc_llm/serve/__init__.py", line 4, in <module>
    from .. import base
  File "/Users/.../miniconda3/envs/mlc-chat-venv/lib/python3.11/site-packages/mlc_llm/base.py", line 47, in <module>
    _LIB, _LIB_PATH = _load_mlc_llm_lib()
                      ^^^^^^^^^^^^^^^^^^^
  File "/Users/.../miniconda3/envs/mlc-chat-venv/lib/python3.11/site-packages/mlc_llm/base.py", line 24, in _load_mlc_llm_lib
    return ctypes.CDLL(lib_path[0]), lib_path[0]
           ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/.../miniconda3/envs/mlc-chat-venv/lib/python3.11/ctypes/__init__.py", line 376, in __init__
    self._handle = _dlopen(self._name, mode)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^
OSError: dlopen(/Users/.../miniconda3/envs/mlc-chat-venv/lib/python3.11/site-packages/mlc_llm/libmlc_llm_module.dylib, 0x0006): Library not loaded: @rpath/libtvm.dylib
  Referenced from: <29EF7201-8531-34DA-9200-D3EE146D81DF> /Users/.../miniconda3/envs/mlc-chat-venv/lib/python3.11/site-packages/mlc_llm/libmlc_llm_module.dylib
  Reason: tried: '/Users/.../miniconda3/envs/mlc-chat-venv/lib/python3.11/site-packages/mlc_llm/libtvm.dylib' (no such file), '/Users/.../miniconda3/envs/mlc-chat-venv/lib/python3.11/site-packages/mlc_llm/libtvm.dylib' (no such file), '/Users/.../miniconda3/envs/mlc-chat-venv/lib/python3.11/lib-dynload/../../libtvm.dylib' (no such file), '/Users/.../miniconda3/envs/mlc-chat-venv/bin/../lib/libtvm.dylib' (no such file), '/usr/local/lib/libtvm.dylib' (no such file), '/usr/lib/libtvm.dylib' (no such file, not in dyld cache)
```

## To Reproduce

Steps to reproduce the behavior:

`conda create -n mlc-chat-venv "llvmdev>=15" "cmake=3.26.4" git python=3.11`
`python -m pip install --pre -U -f https://mlc.ai/wheels mlc-llm-nightly-cpu mlc-ai-nightly-cpu`
`pip install pytest`
<!-- If you have a code sample, error messages, stack traces, please provide it here as well -->


## Environment
 - Operating system (e.g. Ubuntu/Windows/MacOS/...): MacOS
 - TVM Hash Tag (`python -c "import tvm; print('\n'.join(f'{k}: {v}' for k, v in tvm.support.libinfo().items()))"`, applicable if you compile models):
```
❯ python -c "import tvm; print('\n'.join(f'{k}: {v}' for k, v in tvm.support.libinfo().items()))"
Traceback (most recent call last):
  File "<string>", line 1, in <module>
AttributeError: module 'tvm.support' has no attribute 'libinfo'
(mlc-chat-venv)
```
 - Any other relevant information:

## Additional context

<!-- Add any other context about the problem here. -->


## 评论 (4)

### gengisb · 2026-05-31

+1 to this

### hjhsggy · 2026-06-01

+1 to this

### MaoxinYee · 2026-06-04

+1 to this
OSError: libtvm.so: cannot open shared object file: No such file or directory in Linux 

### farukerdem34 · 2026-07-21

+1
