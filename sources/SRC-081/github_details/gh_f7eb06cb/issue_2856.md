# [Issue #2856] [BUG] pip install Failed building wheel for pypcre: "unistd.h" : No such file or directory

source: https://github.com/ModelCloud/GPTQModel/issues/2856
state: closed | updated: 2026-05-06T05:02:15Z
labels: bug

## 正文

**Describe the bug**

I was unable to install pypcre via pip because the pypcre compilation failed on Windows. I have VS 2022 and VS 2026 Insiders on my computer, and C++ desktop development is installed on both.

**GPU Info**

```
Wed May  6 03:15:11 2026
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 595.79                 Driver Version: 595.79         CUDA Version: 13.2     |
+-----------------------------------------+------------------------+----------------------+
| GPU  Name                  Driver-Model | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA GeForce RTX 2070      WDDM  |   00000000:01:00.0  On |                  N/A |
| N/A   50C    P0             29W /  115W |     651MiB /   8192MiB |      1%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+

+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI              PID   Type   Process name                        GPU Memory |
|        ID   ID                                                               Usage      |
|=========================================================================================|
|    0   N/A  N/A            2596    C+G   ...ode-win32-x64-1.96.1\Code.exe      N/A      |
|    0   N/A  N/A            8044    C+G   ...y\StartMenuExperienceHost.exe      N/A      |
|    0   N/A  N/A           13588    C+G   ...ffice\root\Office16\EXCEL.EXE      N/A      |
|    0   N/A  N/A           15488    C+G   ...5n1h2txyewy\TextInputHost.exe      N/A      |
|    0   N/A  N/A           15544    C+G   C:\Windows\explorer.exe               N/A      |
|    0   N/A  N/A           19072    C+G   ...h_cw5n1h2txyewy\SearchApp.exe      N/A      |
|    0   N/A  N/A           19408    C+G   ...Chrome\Application\chrome.exe      N/A      |
|    0   N/A  N/A           21900    C+G   ...yb3d8bbwe\WindowsTerminal.exe      N/A      |
|    0   N/A  N/A           25824    C+G   ...Chrome\Application\chrome.exe      N/A      |
|    0   N/A  N/A           26000    C+G   ...xyewy\ShellExperienceHost.exe      N/A      |
|    0   N/A  N/A           28220    C+G   ...Chrome\Application\chrome.exe      N/A      |
+-----------------------------------------------------------------------------------------+
```

**Software Info**

Windows10 x64 + Python 3.13.12 (tags/v3.13.12:1cbe481, Feb  3 2026, 18:22:25) [MSC v.1944 64 bit (AMD64)] on win32

```
WARNING: Ignoring invalid distribution ~orch (D:\ComfyUI_windows_portable\python_embeded\Lib\site-packages)
WARNING: Package(s) not found: gptqmodel, triton
Name: torch
Version: 2.11.0+cu130
Summary: Tensors and Dynamic neural networks in Python with strong GPU acceleration
Home-page: https://pytorch.org
Author:
Author-email: PyTorch Team <packages@pytorch.org>
License: BSD-3-Clause
Location: D:\ComfyUI_windows_portable\python_embeded\Lib\site-packages
Requires: filelock, fsspec, jinja2, networkx, setuptools, sympy, typing-extensions
Required-by: accelerate, autoawq, bitsandbytes, kornia, spandrel, torchdiffeq, torchsde, torchvision
---
Name: transformers
Version: 5.8.0
Summary: Transformers: the model-definition framework for state-of-the-art machine learning models in text, vision, audio, and multimodal models, for both inference and training.
Home-page: https://github.com/huggingface/transformers
Author: The Hugging Face team (past and future) with the help of all our contributors (https://github.com/huggingface/transformers/graphs/contributors)
Author-email: transformers@huggingface.co
License: Apache 2.0 License
Location: D:\ComfyUI_windows_portable\python_embeded\Lib\site-packages
Requires: huggingface-hub, numpy, packaging, pyyaml, regex, safetensors, tokenizers, tqdm, typer
Required-by: autoawq, comfyui-manager
---
Name: accelerate
Version: 1.13.0
Summary: Accelerate
Home-page: https://github.com/huggingface/accelerate
Author: The Hugging Face team
Author-email: transformers@huggingface.co
License: Apache
Location: D:\ComfyUI_windows_portable\python_embeded\Lib\site-packages
Requires: huggingface_hub, numpy, packaging, psutil, pyyaml, safetensors, torch
Required-by: autoawq
```

**If you are reporting an inference bug of a post-quantized model, please post the content of `config.json` and `quantize_config.json`.**

**To Reproduce**

Just use pip install

```powershel
PS D:\ComfyUI_windows_portable> .\python_embeded\python.exe -m pip install gptqmodel
WARNING: Ignoring invalid distribution ~orch (D:\ComfyUI_windows_portable\python_embeded\Lib\site-packages)
Collecting gptqmodel
  Using cached gptqmodel-7.0.0.tar.gz (979 kB)
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Requirement already satisfied: accelerate>=1.13.0 in .\python_embeded\Lib\site-packages (from gptqmodel) (1.13.0)
Collecting numpy==2.2.6 (from gptqmodel)
  Downloading numpy-2.2.6-cp313-cp313-win_amd64.whl.metadata (60 kB)
Requirement already satisfied: torch>=2.8.0 in .\python_embeded\Lib\site-packages (from gptqmodel) (2.11.0+cu130)
Requirement already satisfied: safetensors>=0.7.0 in .\python_embeded\Lib\site-packages (from gptqmodel) (0.7.0)
Requirement already satisfied: transformers>=5.4.0 in .\python_embeded\Lib\site-packages (from gptqmodel) (5.8.0)
Collecting threadpoolctl>=3.6.0 (from gptqmodel)
  Downloading threadpoolctl-3.6.0-py3-none-any.whl.metadata (13 kB)
Requirement already satisfied: packaging>=24.2 in .\python_embeded\Lib\site-packages (from gptqmodel) (26.0)
Collecting device-smi>=0.5.5 (from gptqmodel)
  Downloading device_smi-0.5.6.tar.gz (18 kB)
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Collecting protobuf>=7.34.0 (from gptqmodel)
  Downloading protobuf-7.34.1-cp310-abi3-win_amd64.whl.metadata (595 bytes)
Requirement already satisfied: pillow>=11.3.0 in .\python_embeded\Lib\site-packages (from gptqmodel) (12.2.0)
Collecting pypcre>=0.3.2 (from gptqmodel)
  Using cached pypcre-0.3.2.tar.gz (121 kB)
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Collecting tokenicer>=0.0.13 (from gptqmodel)
  Downloading tokenicer-0.0.13.tar.gz (14 kB)
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Collecting logbar>=0.4.3 (from gptqmodel)
  Downloading logbar-0.4.3.tar.gz (97 kB)
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Requirement already satisfied: jinja2>=3.1.0 in .\python_embeded\Lib\site-packages (from gptqmodel) (3.1.6)
Collecting ninja>=1.13.0 (from gptqmodel)
  Using cached ninja-1.13.0-py3-none-win_amd64.whl.metadata (5.1 kB)
Collecting maturin>=1.9.4 (from gptqmodel)
  Downloading maturin-1.13.1-py3-none-win_amd64.whl.metadata (16 kB)
Collecting datasets>=3.6.0 (from gptqmodel)
  Downloading datasets-4.8.5-py3-none-any.whl.metadata (19 kB)
Collecting pyarrow>=21.0 (from gptqmodel)
  Downloading pyarrow-24.0.0-cp313-cp313-win_amd64.whl.metadata (3.0 kB)
Collecting dill>=0.3.8 (from gptqmodel)
  Downloading dill-0.4.1-py3-none-any.whl.metadata (10 kB)
Collecting torchao>=0.16.0 (from gptqmodel)
  Downloading torchao-0.17.0-py3-none-any.whl.metadata (20 kB)
Collecting defuser>=0.0.20 (from gptqmodel)
  Downloading defuser-0.0.21.tar.gz (63 kB)
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Requirement already satisfied: psutil in .\python_embeded\Lib\site-packages (from accelerate>=1.13.0->gptqmodel) (7.2.2)
Requirement already satisfied: pyyaml in .\python_embeded\Lib\site-packages (from accelerate>=1.13.0->gptqmodel) (6.0.3)
Requirement already satisfied: huggingface_hub>=0.21.0 in .\python_embeded\Lib\site-packages (from accelerate>=1.13.0->gptqmodel) (1.9.2)
Requirement already satisfied: filelock in .\python_embeded\Lib\site-packages (from datasets>=3.6.0->gptqmodel) (3.25.2)
Collecting pandas (from datasets>=3.6.0->gptqmodel)
  Downloading pandas-3.0.2-cp313-cp313-win_amd64.whl.metadata (19 kB)
Requirement already satisfied: requests>=2.32.2 in .\python_embeded\Lib\site-packages (from datasets>=3.6.0->gptqmodel) (2.33.1)
Requirement already satisfied: httpx<1.0.0 in .\python_embeded\Lib\site-packages (from datasets>=3.6.0->gptqmodel) (0.28.1)
Requirement already satisfied: tqdm>=4.66.3 in .\python_embeded\Lib\site-packages (from datasets>=3.6.0->gptqmodel) (4.67.3)
Collecting xxhash (from datasets>=3.6.0->gptqmodel)
  Downloading xxhash-3.7.0-cp313-cp313-win_amd64.whl.metadata (13 kB)
Collecting multiprocess<0.70.20 (from datasets>=3.6.0->gptqmodel)
  Downloading multiprocess-0.70.19-py313-none-any.whl.metadata (7.5 kB)
Collecting fsspec<=2026.2.0,>=2023.1.0 (from fsspec[http]<=2026.2.0,>=2023.1.0->datasets>=3.6.0->gptqmodel)
  Downloading fsspec-2026.2.0-py3-none-any.whl.metadata (10 kB)
Requirement already satisfied: aiohttp!=4.0.0a0,!=4.0.0a1 in .\python_embeded\Lib\site-packages (from fsspec[http]<=2026.2.0,>=2023.1.0->datasets>=3.6.0->gptqmodel) (3.13.5)
Requirement already satisfied: anyio in .\python_embeded\Lib\site-packages (from httpx<1.0.0->datasets>=3.6.0->gptqmodel) (4.13.0)
Requirement already satisfied: certifi in .\python_embeded\Lib\site-packages (from httpx<1.0.0->datasets>=3.6.0->gptqmodel) (2026.2.25)
Requirement already satisfied: httpcore==1.* in .\python_embeded\Lib\site-packages (from httpx<1.0.0->datasets>=3.6.0->gptqmodel) (1.0.9)
Requirement already satisfied: idna in .\python_embeded\Lib\site-packages (from httpx<1.0.0->datasets>=3.6.0->gptqmodel) (3.11)
Requirement already satisfied: h11>=0.16 in .\python_embeded\Lib\site-packages (from httpcore==1.*->httpx<1.0.0->datasets>=3.6.0->gptqmodel) (0.16.0)
Requirement already satisfied: hf-xet<2.0.0,>=1.4.3 in .\python_embeded\Lib\site-packages (from huggingface_hub>=0.21.0->accelerate>=1.13.0->gptqmodel) (1.4.3)
Requirement already satisfied: typer in .\python_embeded\Lib\site-packages (from huggingface_hub>=0.21.0->accelerate>=1.13.0->gptqmodel) (0.24.1)
Requirement already satisfied: typing-extensions>=4.1.0 in .\python_embeded\Lib\site-packages (from huggingface_hub>=0.21.0->accelerate>=1.13.0->gptqmodel) (4.15.0)
Requirement already satisfied: aiohappyeyeballs>=2.5.0 in .\python_embeded\Lib\site-packages (from aiohttp!=4.0.0a0,!=4.0.0a1->fsspec[http]<=2026.2.0,>=2023.1.0->datasets>=3.6.0->gptqmodel) (2.6.1)
Requirement already satisfied: aiosignal>=1.4.0 in .\python_embeded\Lib\site-packages (from aiohttp!=4.0.0a0,!=4.0.0a1->fsspec[http]<=2026.2.0,>=2023.1.0->datasets>=3.6.0->gptqmodel) (1.4.0)
Requirement already satisfied: attrs>=17.3.0 in .\python_embeded\Lib\site-packages (from aiohttp!=4.0.0a0,!=4.0.0a1->fsspec[http]<=2026.2.0,>=2023.1.0->datasets>=3.6.0->gptqmodel) (26.1.0)
Requirement already satisfied: frozenlist>=1.1.1 in .\python_embeded\Lib\site-packages (from aiohttp!=4.0.0a0,!=4.0.0a1->fsspec[http]<=2026.2.0,>=2023.1.0->datasets>=3.6.0->gptqmodel) (1.8.0)
Requirement already satisfied: multidict<7.0,>=4.5 in .\python_embeded\Lib\site-packages (from aiohttp!=4.0.0a0,!=4.0.0a1->fsspec[http]<=2026.2.0,>=2023.1.0->datasets>=3.6.0->gptqmodel) (6.7.1)
Requirement already satisfied: propcache>=0.2.0 in .\python_embeded\Lib\site-packages (from aiohttp!=4.0.0a0,!=4.0.0a1->fsspec[http]<=2026.2.0,>=2023.1.0->datasets>=3.6.0->gptqmodel) (0.4.1)
Requirement already satisfied: yarl<2.0,>=1.17.0 in .\python_embeded\Lib\site-packages (from aiohttp!=4.0.0a0,!=4.0.0a1->fsspec[http]<=2026.2.0,>=2023.1.0->datasets>=3.6.0->gptqmodel) (1.23.0)
Requirement already satisfied: MarkupSafe>=2.0 in .\python_embeded\Lib\site-packages (from jinja2>=3.1.0->gptqmodel) (3.0.3)
Requirement already satisfied: charset_normalizer<4,>=2 in .\python_embeded\Lib\site-packages (from requests>=2.32.2->datasets>=3.6.0->gptqmodel) (3.4.7)
Requirement already satisfied: urllib3<3,>=1.26 in .\python_embeded\Lib\site-packages (from requests>=2.32.2->datasets>=3.6.0->gptqmodel) (2.6.3)
Requirement already satisfied: setuptools<82 in .\python_embeded\Lib\site-packages (from torch>=2.8.0->gptqmodel) (81.0.0)
Requirement already satisfied: sympy>=1.13.3 in .\python_embeded\Lib\site-packages (from torch>=2.8.0->gptqmodel) (1.14.0)
Requirement already satisfied: networkx>=2.5.1 in .\python_embeded\Lib\site-packages (from torch>=2.8.0->gptqmodel) (3.6.1)
Requirement already satisfied: mpmath<1.4,>=1.1.0 in .\python_embeded\Lib\site-packages (from sympy>=1.13.3->torch>=2.8.0->gptqmodel) (1.3.0)
Requirement already satisfied: colorama in .\python_embeded\Lib\site-packages (from tqdm>=4.66.3->datasets>=3.6.0->gptqmodel) (0.4.6)
Requirement already satisfied: regex>=2025.10.22 in .\python_embeded\Lib\site-packages (from transformers>=5.4.0->gptqmodel) (2026.4.4)
Requirement already satisfied: tokenizers<=0.23.0,>=0.22.0 in .\python_embeded\Lib\site-packages (from transformers>=5.4.0->gptqmodel) (0.22.2)
Collecting python-dateutil>=2.8.2 (from pandas->datasets>=3.6.0->gptqmodel)
  Using cached python_dateutil-2.9.0.post0-py2.py3-none-any.whl.metadata (8.4 kB)
Collecting tzdata (from pandas->datasets>=3.6.0->gptqmodel)
  Downloading tzdata-2026.2-py2.py3-none-any.whl.metadata (1.4 kB)
Collecting six>=1.5 (from python-dateutil>=2.8.2->pandas->datasets>=3.6.0->gptqmodel)
  Downloading six-1.17.0-py2.py3-none-any.whl.metadata (1.7 kB)
Requirement already satisfied: click>=8.2.1 in .\python_embeded\Lib\site-packages (from typer->huggingface_hub>=0.21.0->accelerate>=1.13.0->gptqmodel) (8.3.2)
Requirement already satisfied: shellingham>=1.3.0 in .\python_embeded\Lib\site-packages (from typer->huggingface_hub>=0.21.0->accelerate>=1.13.0->gptqmodel) (1.5.4)
Requirement already satisfied: rich>=12.3.0 in .\python_embeded\Lib\site-packages (from typer->huggingface_hub>=0.21.0->accelerate>=1.13.0->gptqmodel) (14.3.3)
Requirement already satisfied: annotated-doc>=0.0.2 in .\python_embeded\Lib\site-packages (from typer->huggingface_hub>=0.21.0->accelerate>=1.13.0->gptqmodel) (0.0.4)
Requirement already satisfied: markdown-it-py>=2.2.0 in .\python_embeded\Lib\site-packages (from rich>=12.3.0->typer->huggingface_hub>=0.21.0->accelerate>=1.13.0->gptqmodel) (4.0.0)
Requirement already satisfied: pygments<3.0.0,>=2.13.0 in .\python_embeded\Lib\site-packages (from rich>=12.3.0->typer->huggingface_hub>=0.21.0->accelerate>=1.13.0->gptqmodel) (2.20.0)
Requirement already satisfied: mdurl~=0.1 in .\python_embeded\Lib\site-packages (from markdown-it-py>=2.2.0->rich>=12.3.0->typer->huggingface_hub>=0.21.0->accelerate>=1.13.0->gptqmodel) (0.1.2)
Downloading numpy-2.2.6-cp313-cp313-win_amd64.whl (12.6 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 12.6/12.6 MB 7.2 MB/s  0:00:02
Downloading datasets-4.8.5-py3-none-any.whl (528 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 529.0/529.0 kB 20.2 MB/s  0:00:00
Downloading dill-0.4.1-py3-none-any.whl (120 kB)
Downloading fsspec-2026.2.0-py3-none-any.whl (202 kB)
Downloading multiprocess-0.70.19-py313-none-any.whl (156 kB)
Downloading maturin-1.13.1-py3-none-win_amd64.whl (10.2 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 10.2/10.2 MB 16.6 MB/s  0:00:00
Using cached ninja-1.13.0-py3-none-win_amd64.whl (309 kB)
Downloading protobuf-7.34.1-cp310-abi3-win_amd64.whl (437 kB)
Downloading pyarrow-24.0.0-cp313-cp313-win_amd64.whl (27.3 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 27.3/27.3 MB 14.8 MB/s  0:00:01
Downloading threadpoolctl-3.6.0-py3-none-any.whl (18 kB)
Downloading torchao-0.17.0-py3-none-any.whl (1.2 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.2/1.2 MB 39.2 MB/s  0:00:00
Downloading pandas-3.0.2-cp313-cp313-win_amd64.whl (9.7 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 9.7/9.7 MB 15.3 MB/s  0:00:00
Using cached python_dateutil-2.9.0.post0-py2.py3-none-any.whl (229 kB)
Downloading six-1.17.0-py2.py3-none-any.whl (11 kB)
Downloading tzdata-2026.2-py2.py3-none-any.whl (349 kB)
Downloading xxhash-3.7.0-cp313-cp313-win_amd64.whl (31 kB)
Building wheels for collected packages: gptqmodel, defuser, device-smi, logbar, pypcre, tokenicer
  Building wheel for gptqmodel (pyproject.toml) ... done
  Created wheel for gptqmodel: filename=gptqmodel-7.0.0-py3-none-any.whl size=1168474 sha256=3c8457b6a49498b3ccdb056e81ef049af97de1908c896975bb62b9b6643ceaa5
  Stored in directory: c:\users\username\appdata\local\pip\cache\wheels\a9\b6\e4\1eeb41af1956941985ea5d9f0d8aa83338eda97b280f2aab95
  Building wheel for defuser (pyproject.toml) ... done
  Created wheel for defuser: filename=defuser-0.0.21-py3-none-any.whl size=52095 sha256=898764278b9919d8ca183ea577f541817bac737bbb7af797a872c8e70e59c6f1
  Stored in directory: c:\users\username\appdata\local\pip\cache\wheels\7d\f5\27\c29bb9bf8692ab9bb9229a811e02ed4f01b433ad8b47b199b4
  Building wheel for device-smi (pyproject.toml) ... done
  Created wheel for device-smi: filename=device_smi-0.5.6-py3-none-any.whl size=20255 sha256=fe7a4ed88f01053471cfd7749727e0d42ad0d110ac2ead973bdb84119daf5528
  Stored in directory: c:\users\username\appdata\local\pip\cache\wheels\a3\d0\fa\ed3b5d91e5543b052d0071a09a305e76ebac6e8f964bb79225
  Building wheel for logbar (pyproject.toml) ... done
  Created wheel for logbar: filename=logbar-0.4.3-py3-none-any.whl size=74150 sha256=d370de409c1b18fec8a83bda4bf19cae5de44b54054a8cbc3b0d197634f782d1
  Stored in directory: c:\users\username\appdata\local\pip\cache\wheels\a7\ce\28\83bf67cf2bde249350c7b7b3c13690af3f73bb62a82eba0556
  Building wheel for pypcre (pyproject.toml) ... error
  error: subprocess-exited-with-error

  × Building wheel for pypcre (pyproject.toml) did not run successfully.
  │ exit code: 1
  ╰─> [143 lines of output]
      閫傜敤浜\x8e .NET Framework MSBuild 鐗堟湰 17.14.10+8b8e13593

      Found CMake candidates:
        - C:\Users\username\AppData\Local\Temp\pip-build-env-6p29avd0\overlay\Scripts\cmake.exe
        - D:\Python39\Scripts\cmake.exe
      Validated CMake executable at C:\Users\username\AppData\Local\Temp\pip-build-env-6p29avd0\overlay\Scripts\cmake.exe
      Using CMake at C:\Users\username\AppData\Local\Temp\pip-build-env-6p29avd0\overlay\Scripts\cmake.exe
      -- Selecting Windows SDK version 10.0.26100.0 to target Windows 10.0.19045.
      -- Could NOT find BZip2 (missing: BZIP2_LIBRARIES BZIP2_INCLUDE_DIR)
      -- Could NOT find ZLIB (missing: ZLIB_LIBRARY ZLIB_INCLUDE_DIR)
      -- Could NOT find Readline (missing: READLINE_INCLUDE_DIR READLINE_LIBRARY)
      -- Could NOT find Editline (missing: EDITLINE_INCLUDE_DIR EDITLINE_LIBRARY)
      --
      --
      -- PCRE2-10.46 configuration summary:
      --
      --   Install prefix .................... : C:/Program Files/PCRE2
      --   C compiler ........................ : E:/Microsoft Visual Studio/Visual Studio 2022 Professional/VC/Tools/MSVC/14.44.35207/bin/Hostx64/x64/cl.exe
      --   C compiler flags (Debug) .......... : /DWIN32 /D_WINDOWS /Zi /Ob0 /Od /RTC1
      --   C compiler flags (Release) ........ : /DWIN32 /D_WINDOWS /O2 /Ob2 /DNDEBUG
      --   C compiler flags (MinSizeRel) ..... : /DWIN32 /D_WINDOWS /O1 /Ob1 /DNDEBUG
      --   C compiler flags (RelWithDebInfo) . : /DWIN32 /D_WINDOWS /Zi /O2 /Ob1 /DNDEBUG
      --
      --   Build configurations .............. : Debug;Release;MinSizeRel;RelWithDebInfo
      --   Build 8 bit PCRE2 library ......... : ON
      --   Build 16 bit PCRE2 library ........ : OFF
      --   Build 32 bit PCRE2 library ........ : OFF
      --   Include debugging code ............ : IfDebugBuild
      --   Enable JIT compiling support ...... : ON
      --   Use SELinux allocator in JIT ...... : IGNORE
      --   Enable Unicode support ............ : ON
      --   Newline char/sequence ............. : LF
      --   \R matches only ANYCRLF ........... : OFF
      --   \C is disabled .................... : OFF
      --   EBCDIC coding ..................... : OFF
      --   EBCDIC coding with NL=0x25 ........ : OFF
      --   Rebuild char tables ............... : OFF
      --   Internal link size ................ : 2
      --   Maximum variable lookbehind ....... : 255
      --   Parentheses nest limit ............ : 250
      --   Heap limit ........................ : 20000000
      --   Match limit ....................... : 10000000
      --   Match depth limit ................. : MATCH_LIMIT
      --   Build shared libs ................. : OFF
      --   Build static libs ................. : ON
      --      with PIC enabled ............... : OFF
      --   Build pcre2grep ................... : OFF
      --   Enable JIT in pcre2grep ........... : ON
      --   Enable callouts in pcre2grep ...... : ON
      --   Enable callout fork in pcre2grep .. : ON
      --   Buffer size for pcre2grep ......... : 20480
      --   Build tests (implies pcre2test .... : OFF
      --                and pcre2grep)
      --   Link pcre2grep with libz .......... : Library not found
      --   Link pcre2grep with libbz2 ........ : Library not found
      --   Link pcre2test with libeditline ... : Library not found
      --   Link pcre2test with libreadline ... : Library not found
      --   Support Valgrind .................. : OFF
      --   Use %zu and %td ................... : AUTO
      --   Install MSVC .pdb files ........... : OFF
      --
      -- Configuring done (0.6s)
      -- Generating done (0.2s)
      -- Build files have been written to: C:/Users/username/AppData/Local/Temp/pip-install-lleg8fiu/pypcre_b7eb9664f770482f9f4799f88ff62c95/pcre_ext/pcre2-10.46/build
      閫傜敤浜\x8e .NET Framework MSBuild 鐗堟湰 17.14.10+8b8e13593

      E:\Microsoft Visual Studio\Visual Studio 2022 Professional\MSBuild\Microsoft\VC\v170\Microsoft.CppBuild.targets(548,5): warning MSB8029: 涓\xad闂寸洰褰曟垨杈撳嚭鐩\xae褰曟棤娉曢┗鐣欏湪涓存椂鐩\xae褰曚笅锛屽洜涓鸿繖鍙\xaf鑳戒細瀵艰嚧澧為噺鐢熸垚鍑虹幇闂\xae棰樸\x80\x82 [C:\Users\username\AppData\Local\Temp\pip-install-lleg8fiu\pypcre_b7eb9664f770482f9f4799f88ff62c95\pcre_ext\pcre2-10.46\build\ZERO_CHECK.vcxproj]
        1>Checking Build System
      E:\Microsoft Visual Studio\Visual Studio 2022 Professional\MSBuild\Microsoft\VC\v170\Microsoft.CppBuild.targets(548,5): warning MSB8029: 涓\xad闂寸洰褰曟垨杈撳嚭鐩\xae褰曟棤娉曢┗鐣欏湪涓存椂鐩\xae褰曚笅锛屽洜涓鸿繖鍙\xaf鑳戒細瀵艰嚧澧為噺鐢熸垚鍑虹幇闂\xae棰樸\x80\x82 [C:\Users\username\AppData\Local\Temp\pip-install-lleg8fiu\pypcre_b7eb9664f770482f9f4799f88ff62c95\pcre_ext\pcre2-10.46\build\pcre2-8-static.vcxproj]
        Building Custom Rule C:/Users/username/AppData/Local/Temp/pip-install-lleg8fiu/pypcre_b7eb9664f770482f9f4799f88ff62c95/pcre_ext/pcre2-10.46/CMakeLists.txt
        pcre2_auto_possess.c
        pcre2_chartables.c
        pcre2_chkdint.c
        pcre2_compile.c
        pcre2_compile_class.c
        pcre2_config.c
        pcre2_context.c
        pcre2_convert.c
        pcre2_dfa_match.c
        pcre2_error.c
        pcre2_extuni.c
        pcre2_find_bracket.c
        pcre2_jit_compile.c
        pcre2_maketables.c
        pcre2_match.c
        pcre2_match_data.c
        pcre2_newline.c
        pcre2_ord2utf.c
        pcre2_pattern_info.c
        pcre2_script_run.c
        姝ｅ湪鐢熸垚浠ｇ爜...
        姝ｅ湪缂栬瘧...
        pcre2_serialize.c
        pcre2_string_utils.c
        pcre2_study.c
        pcre2_substitute.c
        pcre2_substring.c
        pcre2_tables.c
        pcre2_ucd.c
        pcre2_valid_utf.c
        pcre2_xclass.c
        姝ｅ湪鐢熸垚浠ｇ爜...
        pcre2-8-static.vcxproj -> C:\Users\username\AppData\Local\Temp\pip-install-lleg8fiu\pypcre_b7eb9664f770482f9f4799f88ff62c95\pcre_ext\pcre2-10.46\build\Release\pcre2-8-static.lib
      E:\Microsoft Visual Studio\Visual Studio 2022 Professional\MSBuild\Microsoft\VC\v170\Microsoft.CppBuild.targets(548,5): warning MSB8029: 涓\xad闂寸洰褰曟垨杈撳嚭鐩\xae褰曟棤娉曢┗鐣欏湪涓存椂鐩\xae褰曚笅锛屽洜涓鸿繖鍙\xaf鑳戒細瀵艰嚧澧為噺鐢熸垚鍑虹幇闂\xae棰樸\x80\x82 [C:\Users\username\AppData\Local\Temp\pip-install-lleg8fiu\pypcre_b7eb9664f770482f9f4799f88ff62c95\pcre_ext\pcre2-10.46\build\pcre2-posix-static.vcxproj]
        Building Custom Rule C:/Users/username/AppData/Local/Temp/pip-install-lleg8fiu/pypcre_b7eb9664f770482f9f4799f88ff62c95/pcre_ext/pcre2-10.46/CMakeLists.txt
        pcre2posix.c
        pcre2-posix-static.vcxproj -> C:\Users\username\AppData\Local\Temp\pip-install-lleg8fiu\pypcre_b7eb9664f770482f9f4799f88ff62c95\pcre_ext\pcre2-10.46\build\Release\pcre2-posix-static.lib
      E:\Microsoft Visual Studio\Visual Studio 2022 Professional\MSBuild\Microsoft\VC\v170\Microsoft.CppBuild.targets(548,5): warning MSB8029: 涓\xad闂寸洰褰曟垨杈撳嚭鐩\xae褰曟棤娉曢┗鐣欏湪涓存椂鐩\xae褰曚笅锛屽洜涓鸿繖鍙\xaf鑳戒細瀵艰嚧澧為噺鐢熸垚鍑虹幇闂\xae棰樸\x80\x82 [C:\Users\username\AppData\Local\Temp\pip-install-lleg8fiu\pypcre_b7eb9664f770482f9f4799f88ff62c95\pcre_ext\pcre2-10.46\build\ALL_BUILD.vcxproj]
        Building Custom Rule C:/Users/username/AppData/Local/Temp/pip-install-lleg8fiu/pypcre_b7eb9664f770482f9f4799f88ff62c95/pcre_ext/pcre2-10.46/CMakeLists.txt
      flag_check.c
      flag_check.c
      PyPcre build: using CMake executable at C:\Users\username\AppData\Local\Temp\pip-build-env-6p29avd0\overlay\Scripts\cmake.exe (cmake version 4.3.2)
      PyPcre: using cached CPython headers at C:\Users\username\AppData\Local\Temp\pip-install-lleg8fiu\pypcre_b7eb9664f770482f9f4799f88ff62c95\pcre_ext\python_headers\Python-3.13.12\Include
      build config: {'include_dirs': ['C:\\Users\\username\\AppData\\Local\\Temp\\pip-install-lleg8fiu\\pypcre_b7eb9664f770482f9f4799f88ff62c95\\pcre_ext\\python_headers\\Python-3.13.12\\Include', 'C:\\Users\\username\\AppData\\Local\\Temp\\pip-install-lleg8fiu\\pypcre_b7eb9664f770482f9f4799f88ff62c95\\pcre_ext\\pcre2-10.46\\src'], 'library_dirs': ['C:\\Users\\username\\AppData\\Local\\Temp\\pip-install-lleg8fiu\\pypcre_b7eb9664f770482f9f4799f88ff62c95\\pcre_ext\\pcre2-10.46\\build\\Release'], 'libraries': [], 'extra_compile_args': ['/std:c11', '/experimental:c11atomics'], 'extra_link_args': ['C:\\Users\\username\\AppData\\Local\\Temp\\pip-install-lleg8fiu\\pypcre_b7eb9664f770482f9f4799f88ff62c95\\pcre_ext\\pcre2-10.46\\build\\Release\\pcre2-8-static.lib'], 'define_macros': [('PCRE2_STATIC', '1')]}
      running bdist_wheel
      running build
      running build_py
      creating build\lib.win-amd64-cpython-313
      copying setup_utils.py -> build\lib.win-amd64-cpython-313
      creating build\lib.win-amd64-cpython-313\pcre
      copying pcre\cache.py -> build\lib.win-amd64-cpython-313\pcre
      copying pcre\error.py -> build\lib.win-amd64-cpython-313\pcre
      copying pcre\flags.py -> build\lib.win-amd64-cpython-313\pcre
      copying pcre\pcre.py -> build\lib.win-amd64-cpython-313\pcre
      copying pcre\re_compat.py -> build\lib.win-amd64-cpython-313\pcre
      copying pcre\threads.py -> build\lib.win-amd64-cpython-313\pcre
      copying pcre\_stdlib_re.py -> build\lib.win-amd64-cpython-313\pcre
      copying pcre\__init__.py -> build\lib.win-amd64-cpython-313\pcre
      running egg_info
      writing PyPcre.egg-info\PKG-INFO
      writing dependency_links to PyPcre.egg-info\dependency_links.txt
      writing top-level names to PyPcre.egg-info\top_level.txt
      reading manifest file 'PyPcre.egg-info\SOURCES.txt'
      reading manifest template 'MANIFEST.in'
      adding license file 'LICENSE'
      writing manifest file 'PyPcre.egg-info\SOURCES.txt'
      running build_ext
      building 'pcre_ext_c' extension
      creating build\temp.win-amd64-cpython-313\Release\pcre_ext
      "E:\Microsoft Visual Studio\18\Insiders\VC\Tools\MSVC\14.51.36231\bin\HostX86\x64\cl.exe" /c /nologo /O2 /W3 /GL /DNDEBUG /MD -DPCRE2_STATIC=1 -IC:\Users\username\AppData\Local\Temp\pip-install-lleg8fiu\pypcre_b7eb9664f770482f9f4799f88ff62c95\pcre_ext\python_headers\Python-3.13.12\Include -IC:\Users\username\AppData\Local\Temp\pip-install-lleg8fiu\pypcre_b7eb9664f770482f9f4799f88ff62c95\pcre_ext\pcre2-10.46\src -ID:\ComfyUI_windows_portable\python_embeded\include -ID:\ComfyUI_windows_portable\python_embeded\Include "-IE:\Microsoft Visual Studio\18\Insiders\VC\Tools\MSVC\14.51.36231\include" "-IE:\Microsoft Visual Studio\18\Insiders\VC\Tools\MSVC\14.51.36231\ATLMFC\include" "-IE:\Microsoft Visual Studio\18\Insiders\VC\Auxiliary\VS\include" "-IE:\Windows Kits\10\include\10.0.26100.0\ucrt" "-IE:\Windows Kits\10\\include\10.0.26100.0\\um" "-IE:\Windows Kits\10\\include\10.0.26100.0\\shared" "-IE:\Windows Kits\10\\include\10.0.26100.0\\winrt" "-IE:\Windows Kits\10\\include\10.0.26100.0\\cppwinrt" "-IC:\Program Files (x86)\Windows Kits\NETFXSDK\4.8\include\um" /Tcpcre_ext/cache.c /Fobuild\temp.win-amd64-cpython-313\Release\pcre_ext\cache.obj /std:c11 /experimental:c11atomics
      cache.c
      C:\Users\username\AppData\Local\Temp\pip-install-lleg8fiu\pypcre_b7eb9664f770482f9f4799f88ff62c95\pcre_ext\python_headers\Python-3.13.12\Include\Python.h(45): fatal error C1083: Cannot open include file: “unistd.h”: No such file or directory
      error: command 'E:\\Microsoft Visual Studio\\18\\Insiders\\VC\\Tools\\MSVC\\14.51.36231\\bin\\HostX86\\x64\\cl.exe' failed with exit code 2
      [end of output]

  note: This error originates from a subprocess, and is likely not a problem with pip.
  ERROR: Failed building wheel for pypcre
  Building wheel for tokenicer (pyproject.toml) ... done
  Created wheel for tokenicer: filename=tokenicer-0.0.13-py3-none-any.whl size=16499 sha256=01aff1804fff829ffec335849ac3ed75a62271cd8a5eaf4da7ec2cb714886186
  Stored in directory: c:\users\username\appdata\local\pip\cache\wheels\2c\f9\5c\b2299b657b7f8b0a6fc15090e35685f116c6ce7205ebf172e7
Successfully built gptqmodel defuser device-smi logbar tokenicer
Failed to build pypcre

[notice] A new release of pip is available: 26.1 -> 26.1.1
[notice] To update, run: D:\ComfyUI_windows_portable\python_embeded\python.exe -m pip install --upgrade pip
error: failed-wheel-build-for-install

× Failed to build installable wheels for some pyproject.toml based projects
╰─> pypcre
PS D:\ComfyUI_windows_portable>
```

**Expected behavior**

pip install gptqmodel properly, or provide a pre-build .whl file for Windows



## 评论 (2)

### CSY-ModelCloud · 2026-05-06

i can't reproduce this on Windows 10. but i notice you are using python embed version. can you try latest full version of python 3.13?

latest link is:

https://www.python.org/downloads/release/python-31313/

### tp1415926535 · 2026-05-06

> i can't reproduce this on Windows 10. but i notice you are using python embed version. can you try latest full version of python 3.13?
> 
> latest link is:
> 
> https://www.python.org/downloads/release/python-31313/

You're right. Before, aside from the embedded package, I didn't have Python 3.13 installed on my system—only versions like 3.14 and 3.10. Now I installed Python 3.13 on my system, ran `pip install pypcre`, and it worked fine. Then I ran it again using the embedded Python, and suddenly it worked without any issues. Of course, gptqmodel installed without any issues as well.  

Well, that's strange, but it's fixed now.
