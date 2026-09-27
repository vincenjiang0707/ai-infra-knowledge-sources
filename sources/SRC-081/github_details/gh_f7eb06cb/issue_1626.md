# [Issue #1626] [BUG] Failure to Install

source: https://github.com/ModelCloud/GPTQModel/issues/1626
state: open | updated: 2026-03-13T10:34:36Z
labels: bug

## 正文

**Describe the bug**

Failure to install with either uv or pip on 1x H100 SXM4 rented from Runpod

**GPU Info**

Show output of:

```
Mon Jun  9 20:57:27 2025
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 550.127.05             Driver Version: 550.127.05     CUDA Version: 12.4     |
|-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA A100-SXM4-80GB          On  |   00000000:8A:00.0 Off |                    0 |
| N/A   26C    P0             61W /  400W |       1MiB /  81920MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+

+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI        PID   Type   Process name                              GPU Memory |
|        ID   ID                                                               Usage      |
|=========================================================================================|
|  No running processes found                                                             |
+-----------------------------------------------------------------------------------------+
root@609a11f8691c:/AutoGPTQ#
```

**Software Info**

Runpod docker image: runpod/pytorch:2.1.0-py3.10-cuda11.8.0-devel-ubuntu22.04

```
pip show gptqmodel torch transformers accelerate triton
WARNING: Package(s) not found: gptqmodel
Name: torch
Version: 2.1.0+cu118
Summary: Tensors and Dynamic neural networks in Python with strong GPU acceleration
Home-page: https://pytorch.org/
Author: PyTorch Team
Author-email: packages@pytorch.org
License: BSD-3
Location: /usr/local/lib/python3.10/dist-packages
Requires: filelock, fsspec, jinja2, networkx, sympy, triton, typing-extensions
Required-by: accelerate, auto-gptq, peft, torchaudio, torchvision
---
Name: transformers
Version: 4.52.4
Summary: State-of-the-art Machine Learning for JAX, PyTorch and TensorFlow
Home-page: https://github.com/huggingface/transformers
Author: The Hugging Face team (past and future) with the help of all our contributors (https://github.com/huggingface/transformers/graphs/contributors)
Author-email: transformers@huggingface.co
License: Apache 2.0 License
Location: /usr/local/lib/python3.10/dist-packages
Requires: filelock, huggingface-hub, numpy, packaging, pyyaml, regex, requests, safetensors, tokenizers, tqdm
Required-by: auto-gptq, peft
---
Name: accelerate
Version: 1.7.0
Summary: Accelerate
Home-page: https://github.com/huggingface/accelerate
Author: The HuggingFace team
Author-email: zach.mueller@huggingface.co
License: Apache
Location: /usr/local/lib/python3.10/dist-packages
Requires: huggingface-hub, numpy, packaging, psutil, pyyaml, safetensors, torch
Required-by: auto-gptq, peft
---
Name: triton
Version: 2.1.0
Summary: A language and compiler for custom Deep Learning operations
Home-page: https://github.com/openai/triton/
Author: Philippe Tillet
Author-email: phil@openai.com
License:
Location: /usr/local/lib/python3.10/dist-packages
Requires: filelock
Required-by: torch
```

**If you are reporting an inference bug of a post-quantized model, please post the content of `config.json` and `quantize_config.json`.**

**To Reproduce**

1. Rent 1x A100 SXM from Runpod with the shown image
2. uv pip install -v gptqmodel --no-build-isolation --system
3. observe failure

**Expected behavior**

Successful install

**Additional context**

output logs:
```
DEBUG uv 0.7.12

DEBUG Searching for default Python interpreter in virtual environments

DEBUG Found `cpython-3.10.12-linux-x86_64-gnu` at `/usr/bin/python` (first executable in the search path)

DEBUG Ignoring Python interpreter at `/usr/bin/python`: system interpreter not explicitly requested

DEBUG Ignoring Python interpreter at `/usr/bin/python3`: system interpreter not explicitly requested

DEBUG Ignoring Python interpreter at `/usr/bin/python3.10`: system interpreter not explicitly requested

error: No virtual environment found; run `uv venv` to create an environment, or pass `--system` to install into a non-virtual environment

root@609a11f8691c:/# uv pip install -v gptqmodel --no-build-isolation --system

DEBUG uv 0.7.12

DEBUG Searching for default Python interpreter in search path

DEBUG Found `cpython-3.10.12-linux-x86_64-gnu` at `/usr/bin/python` (first executable in the search path)

Using Python 3.10.12 environment at: /usr

DEBUG Acquired lock for `/usr`

DEBUG At least one requirement is not satisfied: gptqmodel

DEBUG Using request timeout of 30s

DEBUG Solving with installed Python version: 3.10.12

DEBUG Solving with target Python version: >=3.10.12

DEBUG Adding direct dependency: gptqmodel*

DEBUG No cache entry for: https://pypi.org/simple/gptqmodel/

DEBUG Searching for a compatible version of gptqmodel (*)

DEBUG Selecting: gptqmodel==2.2.0 [compatible] (gptqmodel-2.2.0.tar.gz)

DEBUG Acquired lock for `/root/.cache/uv/sdists-v9/pypi/gptqmodel/2.2.0`

DEBUG No cache entry for: https://files.pythonhosted.org/packages/b6/d5/1bf44ba82226e3f81e875415a0c27ab786d2fc0d4bbdde67d797eebb3266/gptqmodel-2.2.0.tar.gz

DEBUG Downloading source distribution: gptqmodel==2.2.0

DEBUG No `pyproject.toml` available for: gptqmodel==2.2.0

DEBUG Found static `PKG-INFO` for: gptqmodel==2.2.0

DEBUG Released lock at `/root/.cache/uv/sdists-v9/pypi/gptqmodel/2.2.0/.lock`

DEBUG Tried 1 versions: gptqmodel 1

DEBUG marker environment resolution took 0.161s

Resolved 1 package in 162ms

DEBUG Identified uncached distribution: gptqmodel==2.2.0

DEBUG Unnecessary package: babel==2.13.1

DEBUG Unnecessary package: jinja2==3.1.2

DEBUG Unnecessary package: markupsafe==2.1.2

DEBUG Unnecessary package: pillow==9.3.0

DEBUG Unnecessary package: pyyaml==6.0.1

DEBUG Unnecessary package: pygments==2.16.1

DEBUG Unnecessary package: send2trash==1.8.2

DEBUG Unnecessary package: anyio==4.0.0

DEBUG Unnecessary package: argon2-cffi==23.1.0

DEBUG Unnecessary package: argon2-cffi-bindings==21.2.0

DEBUG Unnecessary package: arrow==1.3.0

DEBUG Unnecessary package: asttokens==2.4.1

DEBUG Unnecessary package: async-lru==2.0.4

DEBUG Unnecessary package: attrs==23.1.0

DEBUG Unnecessary package: beautifulsoup4==4.12.2

DEBUG Unnecessary package: bleach==6.1.0

DEBUG Unnecessary package: certifi==2022.12.7

DEBUG Unnecessary package: cffi==1.16.0

DEBUG Unnecessary package: charset-normalizer==2.1.1

DEBUG Unnecessary package: comm==0.2.0

DEBUG Unnecessary package: debugpy==1.8.0

DEBUG Unnecessary package: decorator==5.1.1

DEBUG Unnecessary package: defusedxml==0.7.1

DEBUG Unnecessary package: entrypoints==0.4

DEBUG Unnecessary package: exceptiongroup==1.1.3

DEBUG Unnecessary package: executing==2.0.1

DEBUG Unnecessary package: fastjsonschema==2.18.1

DEBUG Unnecessary package: filelock==3.9.0

DEBUG Unnecessary package: fqdn==1.5.1

DEBUG Unnecessary package: fsspec==2023.4.0

DEBUG Unnecessary package: idna==3.4

DEBUG Unnecessary package: ipykernel==6.26.0

DEBUG Unnecessary package: ipython==8.17.2

DEBUG Unnecessary package: ipython-genutils==0.2.0

DEBUG Unnecessary package: ipywidgets==8.1.1

DEBUG Unnecessary package: isoduration==20.11.0

DEBUG Unnecessary package: jedi==0.19.1

DEBUG Unnecessary package: json5==0.9.14

DEBUG Unnecessary package: jsonpointer==2.4

DEBUG Unnecessary package: jsonschema==4.19.2

DEBUG Unnecessary package: jsonschema-specifications==2023.7.1

DEBUG Unnecessary package: jupyter-archive==3.4.0

DEBUG Unnecessary package: jupyter-client==7.4.9

DEBUG Unnecessary package: jupyter-contrib-core==0.4.2

DEBUG Unnecessary package: jupyter-contrib-nbextensions==0.7.0

DEBUG Unnecessary package: jupyter-core==5.5.0

DEBUG Unnecessary package: jupyter-events==0.9.0

DEBUG Unnecessary package: jupyter-highlight-selected-word==0.2.0

DEBUG Unnecessary package: jupyter-lsp==2.2.0

DEBUG Unnecessary package: jupyter-nbextensions-configurator==0.6.3

DEBUG Unnecessary package: jupyter-server==2.10.0

DEBUG Unnecessary package: jupyter-server-terminals==0.4.4

DEBUG Unnecessary package: jupyterlab==4.0.8

DEBUG Unnecessary package: jupyterlab-pygments==0.2.2

DEBUG Unnecessary package: jupyterlab-server==2.25.0

DEBUG Unnecessary package: jupyterlab-widgets==3.0.9

DEBUG Unnecessary package: lxml==4.9.3

DEBUG Unnecessary package: matplotlib-inline==0.1.6

DEBUG Unnecessary package: mistune==3.0.2

DEBUG Unnecessary package: mpmath==1.3.0

DEBUG Unnecessary package: nbclassic==1.0.0

DEBUG Unnecessary package: nbclient==0.9.0

DEBUG Unnecessary package: nbconvert==7.11.0

DEBUG Unnecessary package: nbformat==5.9.2

DEBUG Unnecessary package: nest-asyncio==1.5.8

DEBUG Unnecessary package: networkx==3.0

DEBUG Unnecessary package: notebook==6.5.5

DEBUG Unnecessary package: notebook-shim==0.2.3

DEBUG Unnecessary package: numpy==1.24.1

DEBUG Unnecessary package: overrides==7.4.0

DEBUG Unnecessary package: packaging==23.2

DEBUG Unnecessary package: pandocfilters==1.5.0

DEBUG Unnecessary package: parso==0.8.3

DEBUG Unnecessary package: pexpect==4.8.0

DEBUG Preserving seed package: pip==23.3.1

DEBUG Unnecessary package: platformdirs==3.11.0

DEBUG Unnecessary package: prometheus-client==0.18.0

DEBUG Unnecessary package: prompt-toolkit==3.0.39

DEBUG Unnecessary package: psutil==5.9.6

DEBUG Unnecessary package: ptyprocess==0.7.0

DEBUG Unnecessary package: pure-eval==0.2.2

DEBUG Unnecessary package: pycparser==2.21

DEBUG Unnecessary package: python-dateutil==2.8.2

DEBUG Unnecessary package: python-json-logger==2.0.7

DEBUG Unnecessary package: pyzmq==24.0.1

DEBUG Unnecessary package: referencing==0.30.2

DEBUG Unnecessary package: requests==2.31.0

DEBUG Unnecessary package: rfc3339-validator==0.1.4

DEBUG Unnecessary package: rfc3986-validator==0.1.1

DEBUG Unnecessary package: rpds-py==0.12.0

DEBUG Preserving seed package: setuptools==68.2.2

DEBUG Unnecessary package: sniffio==1.3.0

DEBUG Unnecessary package: soupsieve==2.5

DEBUG Unnecessary package: stack-data==0.6.3

DEBUG Unnecessary package: sympy==1.12

DEBUG Unnecessary package: terminado==0.17.1

DEBUG Unnecessary package: tinycss2==1.2.1

DEBUG Unnecessary package: tomli==2.0.1

DEBUG Unnecessary package: torch==2.1.0+cu118

DEBUG Unnecessary package: torchaudio==2.1.0+cu118

DEBUG Unnecessary package: torchvision==0.16.0+cu118

DEBUG Unnecessary package: tornado==6.3.3

DEBUG Unnecessary package: traitlets==5.13.0

DEBUG Unnecessary package: triton==2.1.0

DEBUG Unnecessary package: types-python-dateutil==2.8.19.14

DEBUG Unnecessary package: typing-extensions==4.4.0

DEBUG Unnecessary package: uri-template==1.3.0

DEBUG Unnecessary package: urllib3==1.26.13

DEBUG Preserving seed package: uv==0.7.12

DEBUG Unnecessary package: wcwidth==0.2.9

DEBUG Unnecessary package: webcolors==1.13

DEBUG Unnecessary package: webencodings==0.5.1

DEBUG Unnecessary package: websocket-client==1.6.4

DEBUG Preserving seed package: wheel==0.41.3

DEBUG Unnecessary package: widgetsnbextension==4.0.9

DEBUG Acquired lock for `/root/.cache/uv/sdists-v9/pypi/gptqmodel/2.2.0`

DEBUG Found fresh response for: https://files.pythonhosted.org/packages/b6/d5/1bf44ba82226e3f81e875415a0c27ab786d2fc0d4bbdde67d797eebb3266/gptqmodel-2.2.0.tar.gz

   Building gptqmodel==2.2.0

DEBUG Building: gptqmodel==2.2.0

DEBUG Proceeding without build isolation

DEBUG Calling `setuptools.build_meta:__legacy__.build_wheel("/root/.cache/uv/builds-v0/.tmp4UofWE", {}, None)`

DEBUG conda_cuda_include_dir /usr/lib/python3/dist-packages/nvidia/cuda_runtime/include

DEBUG running bdist_wheel

DEBUG Traceback (most recent call last):

DEBUG   File "<string>", line 11, in <module>

DEBUG   File "/usr/local/lib/python3.10/dist-packages/setuptools/build_meta.py", line 434, in build_wheel

DEBUG     return self._build_with_temp_dir(

DEBUG   File "/usr/local/lib/python3.10/dist-packages/setuptools/build_meta.py", line 419, in _build_with_temp_dir

DEBUG     self.run_setup()

DEBUG   File "/usr/local/lib/python3.10/dist-packages/setuptools/build_meta.py", line 507, in run_setup

DEBUG     super(_BuildMetaLegacyBackend, self).run_setup(setup_script=setup_script)

DEBUG   File "/usr/local/lib/python3.10/dist-packages/setuptools/build_meta.py", line 341, in run_setup

DEBUG     exec(code, locals())

DEBUG   File "<string>", line 344, in <module>

DEBUG   File "/usr/local/lib/python3.10/dist-packages/setuptools/__init__.py", line 103, in setup

DEBUG     return distutils.core.setup(**attrs)

DEBUG   File "/usr/local/lib/python3.10/dist-packages/setuptools/_distutils/core.py", line 185, in setup

DEBUG     return run_commands(dist)

DEBUG   File "/usr/local/lib/python3.10/dist-packages/setuptools/_distutils/core.py", line 201, in run_commands

DEBUG     dist.run_commands()

DEBUG   File "/usr/local/lib/python3.10/dist-packages/setuptools/_distutils/dist.py", line 969, in run_commands

DEBUG     self.run_command(cmd)

DEBUG   File "/usr/local/lib/python3.10/dist-packages/setuptools/dist.py", line 989, in run_command

DEBUG     super().run_command(command)

DEBUG   File "/usr/local/lib/python3.10/dist-packages/setuptools/_distutils/dist.py", line 988, in run_command

DEBUG     cmd_obj.run()

DEBUG   File "<string>", line 315, in run

DEBUG   File "/usr/local/lib/python3.10/dist-packages/torch/__init__.py", line 1833, in __getattr__

DEBUG     raise AttributeError(f"module '{__name__}' has no attribute '{name}'")

DEBUG AttributeError: module 'torch' has no attribute 'xpu'

DEBUG Released lock at `/root/.cache/uv/sdists-v9/pypi/gptqmodel/2.2.0/.lock`

  x Failed to build `gptqmodel==2.2.0`

  |-> The build backend returned an error

  `-> Call to `setuptools.build_meta:__legacy__.build_wheel` failed (exit status: 1)



      [stdout]

      conda_cuda_include_dir /usr/lib/python3/dist-packages/nvidia/cuda_runtime/include

      running bdist_wheel



      [stderr]

      Traceback (most recent call last):

        File "<string>", line 11, in <module>

        File "/usr/local/lib/python3.10/dist-packages/setuptools/build_meta.py", line 434, in build_wheel

          return self._build_with_temp_dir(

        File "/usr/local/lib/python3.10/dist-packages/setuptools/build_meta.py", line 419, in _build_with_temp_dir

          self.run_setup()

        File "/usr/local/lib/python3.10/dist-packages/setuptools/build_meta.py", line 507, in run_setup

          super(_BuildMetaLegacyBackend, self).run_setup(setup_script=setup_script)

        File "/usr/local/lib/python3.10/dist-packages/setuptools/build_meta.py", line 341, in run_setup

          exec(code, locals())

        File "<string>", line 344, in <module>

        File "/usr/local/lib/python3.10/dist-packages/setuptools/__init__.py", line 103, in setup

          return distutils.core.setup(**attrs)

        File "/usr/local/lib/python3.10/dist-packages/setuptools/_distutils/core.py", line 185, in setup

          return run_commands(dist)

        File "/usr/local/lib/python3.10/dist-packages/setuptools/_distutils/core.py", line 201, in run_commands

          dist.run_commands()

        File "/usr/local/lib/python3.10/dist-packages/setuptools/_distutils/dist.py", line 969, in run_commands

          self.run_command(cmd)

        File "/usr/local/lib/python3.10/dist-packages/setuptools/dist.py", line 989, in run_command

          super().run_command(command)

        File "/usr/local/lib/python3.10/dist-packages/setuptools/_distutils/dist.py", line 988, in run_command

          cmd_obj.run()

        File "<string>", line 315, in run

        File "/usr/local/lib/python3.10/dist-packages/torch/__init__.py", line 1833, in __getattr__

          raise AttributeError(f"module '{__name__}' has no attribute '{name}'")

      AttributeError: module 'torch' has no attribute 'xpu'



      hint: This usually indicates a problem with the package or the build environment.

DEBUG Released lock at `/tmp/uv-ce9cd633bb00c47d.lock`

root@609a11f8691c:/#
```

## 评论 (3)

### e-p-armstrong · 2025-06-09

Fails with normal pip install too


### e-p-armstrong · 2025-06-09

Seems to be fixable by commenting out the "torch.xpu.is_available()" if branch in setup.py

### AaronDinesh · 2026-03-13

I also am not able to install the gptqmodel package the way it is described in the readme because the pip package fails to build.
