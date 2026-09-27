# [Issue #1890] Build incorrectly parses the ROCm version string from torch.version.hip -> 7.12 becomes 82

source: https://github.com/bitsandbytes-foundation/bitsandbytes/issues/1890
state: closed | updated: 2026-03-09T16:14:37Z
labels: 

## 正文

### System Info

I have an issue with building and installing bitsandbytes. 
The bitsandbytes library incorrectly parses the ROCm version string from torch.version.hip, leading to a mismatch between the detected version and the actual ROCm version used by PyTorch. This causes the library loader to search for a non-existent .so file (e.g., libbitsandbytes_rocm82.so instead of libbitsandbytes_rocm712.so), resulting in a runtime error. 
This is issue exists when installing via pip or building from git repo. 

Pull Request: https://github.com/bitsandbytes-foundation/bitsandbytes/pull/1889
The fix is simply change get_cuda_version_string() in bitsandbytes/cuda_specs.py.
` return f"{major * 10 + minor}"` to `return f"{major}{minor}"`.



```
`(theRock) root@abab8722a4ad:/workspace# pip install bitsandbytes
Collecting bitsandbytes
  Using cached bitsandbytes-0.49.2-py3-none-manylinux_2_24_x86_64.whl.metadata (10 kB)
Requirement already satisfied: torch<3,>=2.3 in /opt/theRock/lib/python3.12/site-packages (from bitsandbytes) (2.12.0a0+rocm7.12.0a20260304)
Requirement already satisfied: numpy>=1.17 in /opt/theRock/lib/python3.12/site-packages (from bitsandbytes) (2.4.2)
Requirement already satisfied: packaging>=20.9 in /opt/theRock/lib/python3.12/site-packages (from bitsandbytes) (26.0)
Requirement already satisfied: filelock in /opt/theRock/lib/python3.12/site-packages (from torch<3,>=2.3->bitsandbytes) (3.24.2)
Requirement already satisfied: typing-extensions>=4.10.0 in /opt/theRock/lib/python3.12/site-packages (from torch<3,>=2.3->bitsandbytes) (4.15.0)
Requirement already satisfied: setuptools<82 in /opt/theRock/lib/python3.12/site-packages (from torch<3,>=2.3->bitsandbytes) (81.0.0)
Requirement already satisfied: sympy>=1.13.3 in /opt/theRock/lib/python3.12/site-packages (from torch<3,>=2.3->bitsandbytes) (1.14.0)
Requirement already satisfied: networkx>=2.5.1 in /opt/theRock/lib/python3.12/site-packages (from torch<3,>=2.3->bitsandbytes) (3.6.1)
Requirement already satisfied: jinja2 in /opt/theRock/lib/python3.12/site-packages (from torch<3,>=2.3->bitsandbytes) (3.1.6)
Requirement already satisfied: fsspec>=0.8.5 in /opt/theRock/lib/python3.12/site-packages (from torch<3,>=2.3->bitsandbytes) (2026.2.0)
Requirement already satisfied: rocm==7.12.0a20260304 in /opt/theRock/lib/python3.12/site-packages (from rocm[libraries]==7.12.0a20260304->torch<3,>=2.3->bitsandbytes) (7.12.0a20260304)
Requirement already satisfied: triton==3.6.0+gitadd9159a.rocm7.12.0a20260304 in /opt/theRock/lib/python3.12/site-packages (from torch<3,>=2.3->bitsandbytes) (3.6.0+gitadd9159a.rocm7.12.0a20260304)
Requirement already satisfied: rocm-sdk-core==7.12.0a20260304 in /opt/theRock/lib/python3.12/site-packages (from rocm==7.12.0a20260304->rocm[libraries]==7.12.0a20260304->torch<3,>=2.3->bitsandbytes) (7.12.0a20260304)
Requirement already satisfied: rocm-sdk-libraries-gfx110X-all==7.12.0a20260304 in /opt/theRock/lib/python3.12/site-packages (from rocm[libraries]==7.12.0a20260304->torch<3,>=2.3->bitsandbytes) (7.12.0a20260304)
Requirement already satisfied: mpmath<1.4,>=1.1.0 in /opt/theRock/lib/python3.12/site-packages (from sympy>=1.13.3->torch<3,>=2.3->bitsandbytes) (1.3.0)
Requirement already satisfied: MarkupSafe>=2.0 in /opt/theRock/lib/python3.12/site-packages (from jinja2->torch<3,>=2.3->bitsandbytes) (3.0.3)
Using cached bitsandbytes-0.49.2-py3-none-manylinux_2_24_x86_64.whl (60.7 MB)
Installing collected packages: bitsandbytes
Successfully installed bitsandbytes-0.49.2
(theRock) root@abab8722a4ad:/workspace# python
Python 3.12.3 (main, Jan 22 2026, 20:57:42) [GCC 13.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import bitsandbytes
bitsandbytes library load error: Configured ROCm binary not found at /opt/theRock/lib/python3.12/site-packages/bitsandbytes/libbitsandbytes_rocm82.so
Traceback (most recent call last):
  File "/opt/theRock/lib/python3.12/site-packages/bitsandbytes/cextension.py", line 320, in <module>
    lib = get_native_library()
          ^^^^^^^^^^^^^^^^^^^^
  File "/opt/theRock/lib/python3.12/site-packages/bitsandbytes/cextension.py", line 288, in get_native_library
    raise RuntimeError(f"Configured {BNB_BACKEND} binary not found at {cuda_binary_path}")
RuntimeError: Configured ROCm binary not found at /opt/theRock/lib/python3.12/site-packages/bitsandbytes/libbitsandbytes_rocm82.so
`
```


### Reproduction

#Use theRock Rocm libraries and pytorch
```
pip install --index-url https://rocm.nightlies.amd.com/v2/gfx110X-all/ "rocm[libraries,devel]"
pip install --index-url https://rocm.nightlies.amd.com/v2/gfx110X-all/ torch torchaudio torchvision
pip install bitsandbytes
python - <<'PYTHON'
# Import the bitsandbytes module
import bitsandbytes as bnb
PYTHON
```


### Expected behavior

Should import bitsandbytes from the correct file.

## 评论 (1)

### matthewdouglas · 2026-03-09

Thanks! Closing as #1889 has been merged to fix.
