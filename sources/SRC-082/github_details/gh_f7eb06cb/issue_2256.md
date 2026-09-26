# [Issue #2256] [BUG] Trouble updating to versions that depend on pypcre

source: https://github.com/ModelCloud/GPTQModel/issues/2256
state: closed | updated: 2026-01-12T05:16:45Z
labels: bug

## 正文

**Describe the bug**

```
/home/user/anaconda3/envs/pony56two/bin../lib/gcc/x86_64-conda-linux-gnu/11.2.0/../../../../x86_64-conda-linux-gnu/bin/ld: /usr/lib/i386-linux-gnu/libpcre2-8.so.0: error adding symbols: file in wrong format
      collect2: error: ld returned 1 exit status
      error: command '/home/user/anaconda3/envs/pony56two/bin/x86_64-conda-linux-gnu-cc' failed with exit code 1
      [end of output]
  
  note: This error originates from a subprocess, and is likely not a problem with pip.
  ERROR: Failed building wheel for pypcre
Failed to build pypcre
WARNING: Ignoring invalid distribution ~vidia-cublas-cu12 (/home/user/anaconda3/envs/pony56two/lib/python3.12/site-packages)
WARNING: Ignoring invalid distribution ~vidia-cublas-cu12 (/home/user/anaconda3/envs/pony56two/lib/python3.12/site-packages)
error: failed-wheel-build-for-install

× Failed to build installable wheels for some pyproject.toml based projects
╰─> pypcre
```
I get this every time I try to install pypcre via pip. I am in a conda environment with gxx_linux-64==14.3.0 but if I try to upgrade to 15 I get the following:
```
conda install -c anaconda --override-channels gxx_linux-64==15.2.0
Channels:
 - anaconda
Platform: linux-64
Collecting package metadata (repodata.json): done
Solving environment: failed

LibMambaUnsatisfiableError: Encountered problems while solving:
  - nothing provides __win needed by cuda-12.4.1-h382c6e5_0

Could not solve for environment specs
The following packages are incompatible
├─ __cuda is requested and can be installed;
├─ cuda is installable with the potential options
│  ├─ cuda 12.4.1 would require
│  │  └─ cuda-toolkit 12.4.1.*  with the potential options
│  │     ├─ cuda-toolkit 12.4.1 would require
│  │     │  └─ cuda-compiler 12.4.1.*  with the potential options
│  │     │     ├─ cuda-compiler 12.4.1 would require
│  │     │     │  └─ gxx_linux-64 11.2.0.* , which can be installed;
│  │     │     └─ cuda-compiler 12.4.1 would require
│  │     │        └─ __win, which is missing on the system;
│  │     └─ cuda-toolkit [12.4.1|12.8.1] would require
│  │        └─ __win, which is missing on the system;
│  ├─ cuda 12.8.1 would require
│  │  └─ cuda-toolkit 12.8.1.*  with the potential options
│  │     ├─ cuda-toolkit [12.4.1|12.8.1], which cannot be installed (as previously explained);
│  │     └─ cuda-toolkit 12.8.1 would require
│  │        └─ cuda-compiler 12.8.1.*  with the potential options
│  │           ├─ cuda-compiler 12.8.1 would require
│  │           │  └─ cuda-nvcc 12.8.93.* , which requires
│  │           │     └─ cuda-nvcc_linux-64 12.8.93.* , which requires
│  │           │        └─ cuda-nvcc-tools 12.8.93.* , which requires
│  │           │           └─ gcc_impl_linux-64 >=6,<15.0a0 , which can be installed;
│  │           └─ cuda-compiler 12.8.1 would require
│  │              └─ cxx-compiler with the potential options
│  │                 ├─ cxx-compiler 1.11.0 would require
│  │                 │  └─ gxx_linux-64 14.3.0.* , which can be installed;
│  │                 └─ cxx-compiler [1.9.0|1.9.1] would require
│  │                    └─ gxx_linux-64 11.2.0.* , which can be installed;
│  ├─ cuda 13.0.2 would require
│  │  └─ cuda-toolkit 13.0.2.* , which requires
│  │     └─ cuda-nvml-dev 13.0.87.* , which requires
│  │        └─ cuda-version >=13.0,<13.1.0a0 , which requires
│  │           └─ __cuda >=13 , which conflicts with any installable versions previously reported;
│  └─ cuda [12.4.1|12.8.1] would require
│     └─ __win, which is missing on the system;
└─ gxx_linux-64 15.2.0  is not installable because it requires
   └─ gcc_linux-64 [15.2.0 h1ca4c6b_11|15.2.0 h1ca4c6b_12], which requires
      └─ gcc_impl_linux-64 15.2.0.* , which conflicts with any installable versions previously reported.
```
I have libpcre2 installed on the system as well.

It's the same whether I install from source or not. I'd like to get the updates from the new version but this is stopping me from doing so. Is this import absolutely necessary? I've been advocating for this repo to become the new standard for hf for AWQ but I feel like imports with clumsy compatibility like this are gonna really hamper that.

**GPU Info**

Show output of:

```
nvidia-smi
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 570.172.08             Driver Version: 570.172.08     CUDA Version: 12.8     |
|-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA GeForce RTX 4090        On  |   00000000:01:00.0  On |                  Off |
|  0%   31C    P8             15W /  500W |    1503MiB /  24564MiB |      0%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+
                                                                                         
+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI              PID   Type   Process name                        GPU Memory |
|        ID   ID                                                               Usage      |
|=========================================================================================|
|    0   N/A  N/A            4557      G   /usr/lib/xorg/Xorg                      541MiB |
|    0   N/A  N/A            4852      G   /usr/bin/gnome-shell                     65MiB |
|    0   N/A  N/A            5601      G   ...bin/snapd-desktop-integration         44MiB |
|    0   N/A  N/A          835538      G   ...share/Steam/ubuntu12_32/steam         38MiB |
|    0   N/A  N/A          835725      G   ./steamwebhelper                         36MiB |
|    0   N/A  N/A          835764    C+G   ...am/ubuntu12_64/steamwebhelper         14MiB |
|    0   N/A  N/A         3230364      G   .../7423/usr/lib/firefox/firefox        332MiB |
+-----------------------------------------------------------------------------------------+
```

**Software Info**

Operation System/Version + Python Version
linux-x64 (Ubuntu 22.04.5 LTS)
python version 3.12

Show output of:
```
$ pip show gptqmodel torch transformers accelerate triton
WARNING: Ignoring invalid distribution ~vidia-cublas-cu12 (/home/ambrose/anaconda3/envs/pony56two/lib/python3.12/site-packages)
WARNING: Package(s) not found: gptqmodel
Name: torch
Version: 2.9.1
Summary: Tensors and Dynamic neural networks in Python with strong GPU acceleration
Home-page: https://pytorch.org
Author: 
Author-email: PyTorch Team <packages@pytorch.org>
License: BSD-3-Clause
Location: /home/ambrose/anaconda3/envs/pony56two/lib/python3.12/site-packages
Requires: filelock, fsspec, jinja2, networkx, nvidia-cublas-cu12, nvidia-cuda-cupti-cu12, nvidia-cuda-nvrtc-cu12, nvidia-cuda-runtime-cu12, nvidia-cudnn-cu12, nvidia-cufft-cu12, nvidia-cufile-cu12, nvidia-curand-cu12, nvidia-cusolver-cu12, nvidia-cusparse-cu12, nvidia-cusparselt-cu12, nvidia-nccl-cu12, nvidia-nvjitlink-cu12, nvidia-nvshmem-cu12, nvidia-nvtx-cu12, setuptools, sympy, triton, typing-extensions
Required-by: accelerate, autoawq, autoawq_kernels, deepspeed, flash_attn, liger_kernel, lm_eval, optimum, peft, sentence-transformers, torchvision
---
Name: transformers
Version: 4.56.1
Summary: State-of-the-art Machine Learning for JAX, PyTorch and TensorFlow
Home-page: https://github.com/huggingface/transformers
Author: The Hugging Face team (past and future) with the help of all our contributors (https://github.com/huggingface/transformers/graphs/contributors)
Author-email: transformers@huggingface.co
License: Apache 2.0 License
Location: /home/ambrose/anaconda3/envs/pony56two/lib/python3.12/site-packages
Requires: filelock, huggingface-hub, numpy, packaging, pyyaml, regex, requests, safetensors, tokenizers, tqdm
Required-by: autoawq, lm_eval, optimum, peft, sentence-transformers, tokenicer, trl
---
Name: accelerate
Version: 1.10.1
Summary: Accelerate
Home-page: https://github.com/huggingface/accelerate
Author: The HuggingFace team
Author-email: zach.mueller@huggingface.co
License: Apache
Location: /home/ambrose/anaconda3/envs/pony56two/lib/python3.12/site-packages
Requires: huggingface_hub, numpy, packaging, psutil, pyyaml, safetensors, torch
Required-by: autoawq, lm_eval, peft, trl
---
Name: triton
Version: 3.5.1
Summary: A language and compiler for custom Deep Learning operations
Home-page: https://github.com/triton-lang/triton/
Author: Philippe Tillet
Author-email: phil@openai.com
License: 
Location: /home/ambrose/anaconda3/envs/pony56two/lib/python3.12/site-packages
Requires: 
Required-by: autoawq, liger_kernel, torch
```

**To Reproduce**

pip install gptqmodel

## 评论 (6)

### Qubitium · 2025-12-11

> /usr/lib/i386-linux-gnu/libpcre2-8.so.0: error adding symbols: file in wrong format

You installed the wrong version of libpcre2. Most likely you are on x86_64 but the ld linker is usinga i386 version of the lib.

You need to remove all the i386 libs. some pkg on your host os is forcing i386 libs to be installed. This happens sometimes.

pypcre is ci tested on all major systems including macos/windows but we haven no plans to add i386 support. 

### Qubitium · 2025-12-12

@ambroser53  addition setup serrors regarding license property compat and recent pip/setuptools are also fixed on main. We will releaes 5.6.2 patch release today. Please pull main and try again. This is separate from your linker trying to link to a i386 pcre error. 

### Qubitium · 2025-12-12

https://github.com/ModelCloud/GPTQModel/releases/tag/v5.6.2

v5.6.2 is releasing snow. 

@ambroser53 Please check if you are able to fix your env's i386 linking issue.  

### Qubitium · 2025-12-15

@ambroser53  We have fixed this issue at the source. https://github.com/ModelCloud/GPTQModel/releases/tag/v5.6.4

Please do `pip install -U pypcre` and it should work now. Updated pypcre fixed resolution of `multi-arch` libs where both i386 and x86_64 libs are installed. 

### remixer-dec · 2026-01-12

I've had this in my Dockerfile:
`/opt/venv-universal/bin/pip install --no-cache-dir -v gptqmodel[auto_round] --no-build-isolation`
Haven't rebuilt it since November. 

It crashes:
<details>
<pre>
stdout: #11 8.246 Collecting pypcre>=0.2.9 (from gptqmodel[auto_round])
stdout: #11 8.276   Downloading pypcre-0.2.9.tar.gz (118 kB)
stdout: #11 8.278      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 118.5/118.5 kB 79.9 MB/s eta 0:00:00
stdout: #11 8.289   Preparing metadata (pyproject.toml): started
stdout: #11 8.290   Running command Preparing metadata (pyproject.toml)
stdout: #11 8.375   Traceback (most recent call last):
stdout: #11 8.375     File "/opt/venv-universal/lib/python3.11/site-packages/setuptools/_distutils/spawn.py", line 87, in spawn
stdout: #11 8.375       subprocess.check_call(cmd, env=_inject_macos_ver(env))
stdout: #11 8.375     File "/opt/conda/lib/python3.11/subprocess.py", line 408, in check_call
stdout: #11 8.378       retcode = call(*popenargs, **kwargs)
stdout: #11 8.378                 ^^^^^^^^^^^^^^^^^^^^^^^^^^
stdout: #11 8.378     File "/opt/conda/lib/python3.11/subprocess.py", line 389, in call
stdout: #11 8.378       with Popen(*popenargs, **kwargs) as p:
stdout: #11 8.378            ^^^^^^^^^^^^^^^^^^^^^^^^^^^
stdout: #11 8.378     File "/opt/conda/lib/python3.11/subprocess.py", line 1026, in __init__
stdout: #11 8.378       self._execute_child(args, executable, preexec_fn, close_fds,
stdout: #11 8.378     File "/opt/conda/lib/python3.11/subprocess.py", line 1955, in _execute_child
stdout: #11 8.378       raise child_exception_type(errno_num, err_msg, err_filename)
stdout: #11 8.378   FileNotFoundError: [Errno 2] No such file or directory: 'gcc'
</pre>
</details>
Is GCC now required to be installed in the image for the library?
4.2.5 is the latest version that does not require it

### Qubitium · 2026-01-12

@remixer-dec Please create a new issue and present your exact docker file config so we can reproduce.  
