# [Issue #716] guidellm benchmark --help fails with vLLM >= 0.20.0 (and other CLI commands fail as well).

source: https://github.com/vllm-project/guidellm/issues/716
state: closed | updated: 2026-07-01T17:11:27Z
labels: 

## 正文

### Bug Description

After upgrading to vLLM >= 0.20.0, running:

```bash
guidellm benchmark --help
````

fails (and other CLI commands fail as well), as while it works correctly with earlier vLLM versions.


### Expected Behavior

The CLI works as before (starts successfully without errors) on vLLM >= 0.20.0, same as on earlier versions.

### Steps to Reproduce


```bash
pip install uv
uv pip install guidellm vllm
guidellm benchmark --help
```

### Operating System

Ubuntu 22.04

### Python Version

Python 3.12.13

### GuideLLM Version

0.6.0

### Installation Method

pip install guidellm

### Installation Details

_No response_

### Error Messages or Stack Traces

```shell
Traceback (most recent call last):
  File "/usr/local/bin/guidellm", line 4, in <module>
    from guidellm.__main__ import cli
  File "/usr/local/lib/python3.12/dist-packages/guidellm/__main__.py", line 36, in <module>
    from guidellm.backends import BackendType
  File "/usr/local/lib/python3.12/dist-packages/guidellm/backends/__init__.py", line 26, in <module>
    from .vllm_python import VLLMPythonBackend, VLLMResponseHandler
  File "/usr/local/lib/python3.12/dist-packages/guidellm/backends/vllm_python/__init__.py", line 8, in <module>
    from .vllm import VLLMPythonBackend
  File "/usr/local/lib/python3.12/dist-packages/guidellm/backends/vllm_python/vllm.py", line 41, in <module>
    from guidellm.extras.audio import _decode_audio
  File "/usr/local/lib/python3.12/dist-packages/guidellm/extras/audio.py", line 11, in <module>
    from torchcodec import AudioSamples
  File "/usr/local/lib/python3.12/dist-packages/torchcodec/__init__.py", line 12, in <module>
    from . import decoders, encoders, samplers, transforms  # noqa
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/torchcodec/decoders/__init__.py", line 7, in <module>
    from .._core import AudioStreamMetadata, VideoStreamMetadata
  File "/usr/local/lib/python3.12/dist-packages/torchcodec/_core/__init__.py", line 8, in <module>
    from ._metadata import (
  File "/usr/local/lib/python3.12/dist-packages/torchcodec/_core/_metadata.py", line 16, in <module>
    from torchcodec._core.ops import (
  File "/usr/local/lib/python3.12/dist-packages/torchcodec/_core/ops.py", line 109, in <module>
    ffmpeg_major_version, core_library_path = load_torchcodec_shared_libraries()
                                              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/torchcodec/_core/ops.py", line 76, in load_torchcodec_shared_libraries
    raise RuntimeError(
RuntimeError: Could not load libtorchcodec. Likely causes:
          1. FFmpeg is not properly installed in your environment. We support
             versions 4, 5, 6, 7, and 8, and we attempt to load libtorchcodec
             for each of those versions. Errors for versions not installed on
             your system are expected; only the error for your installed FFmpeg
             version is relevant. On Windows, ensure you've installed the
             "full-shared" version which ships DLLs.
          2. The PyTorch version (2.11.0+cu130) is not compatible with
             this version of TorchCodec. Refer to the version compatibility
             table:
             https://github.com/pytorch/torchcodec?tab=readme-ov-file#installing-torchcodec.
          3. Another runtime dependency; see exceptions below.

        The following exceptions were raised as we tried to load libtorchcodec:
        
[start of libtorchcodec loading traceback]
FFmpeg version 8:
Traceback (most recent call last):
  File "/usr/local/lib/python3.12/dist-packages/torch/_ops.py", line 1503, in load_library
    ctypes.CDLL(path)
  File "/usr/lib/python3.12/ctypes/__init__.py", line 379, in __init__
    self._handle = _dlopen(self._name, mode)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^
OSError: libavutil.so.60: cannot open shared object file: No such file or directory

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/usr/local/lib/python3.12/dist-packages/torchcodec/_core/ops.py", line 57, in load_torchcodec_shared_libraries
    torch.ops.load_library(core_library_path)
  File "/usr/local/lib/python3.12/dist-packages/torch/_ops.py", line 1505, in load_library
    raise OSError(f"Could not load this library: {path}") from e
OSError: Could not load this library: /usr/local/lib/python3.12/dist-packages/torchcodec/libtorchcodec_core8.so

FFmpeg version 7:
Traceback (most recent call last):
  File "/usr/local/lib/python3.12/dist-packages/torch/_ops.py", line 1503, in load_library
    ctypes.CDLL(path)
  File "/usr/lib/python3.12/ctypes/__init__.py", line 379, in __init__
    self._handle = _dlopen(self._name, mode)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^
OSError: libavutil.so.59: cannot open shared object file: No such file or directory

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/usr/local/lib/python3.12/dist-packages/torchcodec/_core/ops.py", line 57, in load_torchcodec_shared_libraries
    torch.ops.load_library(core_library_path)
  File "/usr/local/lib/python3.12/dist-packages/torch/_ops.py", line 1505, in load_library
    raise OSError(f"Could not load this library: {path}") from e
OSError: Could not load this library: /usr/local/lib/python3.12/dist-packages/torchcodec/libtorchcodec_core7.so

FFmpeg version 6:
Traceback (most recent call last):
  File "/usr/local/lib/python3.12/dist-packages/torch/_ops.py", line 1503, in load_library
    ctypes.CDLL(path)
  File "/usr/lib/python3.12/ctypes/__init__.py", line 379, in __init__
    self._handle = _dlopen(self._name, mode)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^
OSError: libavutil.so.58: cannot open shared object file: No such file or directory

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/usr/local/lib/python3.12/dist-packages/torchcodec/_core/ops.py", line 57, in load_torchcodec_shared_libraries
    torch.ops.load_library(core_library_path)
  File "/usr/local/lib/python3.12/dist-packages/torch/_ops.py", line 1505, in load_library
    raise OSError(f"Could not load this library: {path}") from e
OSError: Could not load this library: /usr/local/lib/python3.12/dist-packages/torchcodec/libtorchcodec_core6.so

FFmpeg version 5:
Traceback (most recent call last):
  File "/usr/local/lib/python3.12/dist-packages/torch/_ops.py", line 1503, in load_library
    ctypes.CDLL(path)
  File "/usr/lib/python3.12/ctypes/__init__.py", line 379, in __init__
    self._handle = _dlopen(self._name, mode)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^
OSError: libavutil.so.57: cannot open shared object file: No such file or directory

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/usr/local/lib/python3.12/dist-packages/torchcodec/_core/ops.py", line 57, in load_torchcodec_shared_libraries
    torch.ops.load_library(core_library_path)
  File "/usr/local/lib/python3.12/dist-packages/torch/_ops.py", line 1505, in load_library
    raise OSError(f"Could not load this library: {path}") from e
OSError: Could not load this library: /usr/local/lib/python3.12/dist-packages/torchcodec/libtorchcodec_core5.so

FFmpeg version 4:
Traceback (most recent call last):
  File "/usr/local/lib/python3.12/dist-packages/torch/_ops.py", line 1503, in load_library
    ctypes.CDLL(path)
  File "/usr/lib/python3.12/ctypes/__init__.py", line 379, in __init__
    self._handle = _dlopen(self._name, mode)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^
OSError: /usr/local/lib/python3.12/dist-packages/torchcodec/libtorchcodec_core4.so: undefined symbol: _ZN3c1013MessageLoggerC1EPKciib

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/usr/local/lib/python3.12/dist-packages/torchcodec/_core/ops.py", line 57, in load_torchcodec_shared_libraries
    torch.ops.load_library(core_library_path)
  File "/usr/local/lib/python3.12/dist-packages/torch/_ops.py", line 1505, in load_library
    raise OSError(f"Could not load this library: {path}") from e
OSError: Could not load this library: /usr/local/lib/python3.12/dist-packages/torchcodec/libtorchcodec_core4.so
[end of libtorchcodec loading traceback].
```

### Additional Context

_No response_

## 评论 (2)

### sjmonson · 2026-05-12

Sorry this issue got lost in my backlog. I was not able to reproduce as written, however my guess is that the commands were not run with a clean virtual environment since neither `vllm` nor `guidellm` include `torchcodec` by default. If you install GuideLLM with `guidellm[audio]` or `guidellm[all]` it will ensure the `torch` and `torchcodec` versions line up.

A secondary issue is that GuideLLM eagerly loads all dependencies which is why this fails at startup and not when torchcodec is used; #641 will address that problem.

### sjmonson · 2026-07-01

Closing since cannot reproduce. Please reopen if the problem is still occurring.
