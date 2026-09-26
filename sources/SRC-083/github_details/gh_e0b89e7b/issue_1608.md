# [Issue #1608] [AMD GPU installation] The Rocm-bitsandbytes installation issues

source: https://github.com/bitsandbytes-foundation/bitsandbytes/issues/1608
state: closed | updated: 2026-02-24T16:46:04Z
labels: ROCm

## 正文

### System Info

Issues: The installation of the latest multi-backend-refactor branch failed in the AMD GPU. While switching to the Rocm-bitsandbytes repo, by using the rocm_enabled_multi_backend branch, the installation was successfully. Could you please check if the right branch was selected, thanks so much!

Official Repo: 
https://github.com/bitsandbytes-foundation/bitsandbytes/tree/multi-backend-refactor

Test Environment: 
AMD MI300X GPU

Docker image: 
# Rocm6.4 is the latest version for the AMD Rocm release. 
docker pull rocm/pytorch:rocm6.4_ubuntu24.04_py3.12_pytorch_release_2.4.1


### Reproduction

How to reproduce:
Step by Step: 
# Rocm6.4 is the latest version for the AMD Rocm release. 
docker pull rocm/pytorch:rocm6.4_ubuntu24.04_py3.12_pytorch_release_2.4.1

docker run  -it --cap-add=SYS_PTRACE --security-opt seccomp=unconfined --device=/dev/kfd --device=/dev/dri -v /:/workspace  --group-add video --ipc=host  --name bitsandbytes01   rocm/pytorch:rocm6.4_ubuntu24.04_py3.12_pytorch_release_2.4.1

Inside the docker:
git clone -b multi-backend-refactor https://github.com/bitsandbytes-foundation/bitsandbytes.git && cd bitsandbytes/

# Compile & install
apt-get install -y build-essential cmake  
cmake -DCOMPUTE_BACKEND=hip -S .  
make
pip install -e .   

After installation done:
*******************************************
Successfully built bitsandbytes
Installing collected packages: bitsandbytes
  Attempting uninstall: bitsandbytes
    Found existing installation: bitsandbytes 1.0.0
    Uninstalling bitsandbytes-1.0.0:
      Successfully uninstalled bitsandbytes-1.0.0
Successfully installed bitsandbytes-1.0.0
**********************************************
Verify the installation once done.
 python -m bitsandbytes
*********************************************
root@93db47d5b637:/var/lib/jenkins/bitsandbytes# python -m bitsandbytes
Could not load bitsandbytes native library: /var/lib/jenkins/bitsandbytes/bitsandbytes/libbitsandbytes_rocm64.so: undefined symbol: _Z36__device_stub__kOptimizer32bit1StateI12hip_bfloat16Li2EEvPT_S2_PfS3_ffffffiffbi. If you use Intel CPU or XPU, please pip install intel_extension_for_pytorch
Traceback (most recent call last):
  File "/var/lib/jenkins/bitsandbytes/bitsandbytes/cextension.py", line 115, in <module>
    lib = get_native_library()
          ^^^^^^^^^^^^^^^^^^^^
  File "/var/lib/jenkins/bitsandbytes/bitsandbytes/cextension.py", line 86, in get_native_library
    dll = ct.cdll.LoadLibrary(str(binary_path))
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/conda/envs/py_3.12/lib/python3.12/ctypes/__init__.py", line 460, in LoadLibrary
    return self._dlltype(name)
           ^^^^^^^^^^^^^^^^^^^
  File "/opt/conda/envs/py_3.12/lib/python3.12/ctypes/__init__.py", line 379, in __init__
    self._handle = _dlopen(self._name, mode)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^
OSError: /var/lib/jenkins/bitsandbytes/bitsandbytes/libbitsandbytes_rocm64.so: undefined symbol: _Z36__device_stub__kOptimizer32bit1StateI12hip_bfloat16Li2EEvPT_S2_PfS3_ffffffiffbi

    ROCm Setup failed despite ROCm being available. Please run the following command to get more information:

    python -m bitsandbytes

    Inspect the output of the command and see if you can locate ROCm libraries. You might need to add them
    to your LD_LIBRARY_PATH. If you suspect a bug, please take the information from python -m bitsandbytes
    and open an issue at: https://github.com/bitsandbytes-foundation/bitsandbytes/issues

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++ BUG REPORT INFORMATION ++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++++++ OTHER +++++++++++++++++++++++++++
ROCm specs: rocm_version_string='64', rocm_version_tuple=(6, 4)
PyTorch settings found: ROCM_VERSION=64
The directory listed in your path is found to be non-existent: /opt/ompi/lib
The directory listed in your path is found to be non-existent: /opt/ompi
The directory listed in your path is found to be non-existent: /opt/ucx
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++ DEBUG INFO END ++++++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Checking that the library is importable and ROCm is callable...
Couldn't load the bitsandbytes library, likely due to missing binaries.
Please ensure bitsandbytes is properly installed.

For source installations, compile the binaries with `cmake -DCOMPUTE_BACKEND=hip -S .`.
See the documentation for more details if needed.

Trying a simple check anyway, but this will likely fail...
Traceback (most recent call last):
  File "/var/lib/jenkins/bitsandbytes/bitsandbytes/diagnostics/main.py", line 73, in main
    sanity_check()
  File "/var/lib/jenkins/bitsandbytes/bitsandbytes/diagnostics/main.py", line 42, in sanity_check
    adam.step()
  File "/opt/conda/envs/py_3.12/lib/python3.12/site-packages/torch/optim/optimizer.py", line 484, in wrapper
    out = func(*args, **kwargs)
          ^^^^^^^^^^^^^^^^^^^^^
  File "/opt/conda/envs/py_3.12/lib/python3.12/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/var/lib/jenkins/bitsandbytes/bitsandbytes/optim/optimizer.py", line 292, in step
    self.update_step(group, p, gindex, pindex)
  File "/opt/conda/envs/py_3.12/lib/python3.12/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/var/lib/jenkins/bitsandbytes/bitsandbytes/optim/optimizer.py", line 522, in update_step
    F.optimizer_update_32bit(
  File "/var/lib/jenkins/bitsandbytes/bitsandbytes/functional.py", line 1266, in optimizer_update_32bit
    return backends[g.device.type].optimizer_update_32bit(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/var/lib/jenkins/bitsandbytes/bitsandbytes/backends/cuda.py", line 780, in optimizer_update_32bit
    optim_func = str2optimizer32bit[optimizer_name][0]
                 ^^^^^^^^^^^^^^^^^^
NameError: name 'str2optimizer32bit' is not defined
Above we output some debug information.
Please provide this info when creating an issue via https://github.com/TimDettmers/bitsandbytes/issues/new/choose
WARNING: Please be sure to sanitize sensitive info from the output before posting it.
*******************************************************************************************

Debugging details:

If we use the latest /ROCm/bitsandbytes to install, the installation was successful. 

docker run  -it --cap-add=SYS_PTRACE --security-opt seccomp=unconfined --device=/dev/kfd --device=/dev/dri -v /:/workspace  --group-add video --ipc=host  --name bitsandbytes01   rocm/pytorch:rocm6.4_ubuntu24.04_py3.12_pytorch_release_2.4.1

Inside the docker: 

git clone -b rocm_enabled_multi_backend https://github.com/ROCm/bitsandbytes.git 

cd bitsandbytes
git checkout rocm_enabled_multi_backend
pip install -r requirements-dev.txt
cmake -DCOMPUTE_BACKEND=hip -S . #Use -DBNB_ROCM_ARCH="gfx90a;gfx942" to target specific gpu arch
make
pip install .

Verify the installation once done, 

python -m bitsandbytes  
*********************************************************************************************
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++ BUG REPORT INFORMATION ++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++++++ OTHER +++++++++++++++++++++++++++
ROCm specs: rocm_version_string='64', rocm_version_tuple=(6, 4)
PyTorch settings found: ROCM_VERSION=64
The directory listed in your path is found to be non-existent: /opt/ompi/lib
The directory listed in your path is found to be non-existent: /opt/ompi
The directory listed in your path is found to be non-existent: /opt/ucx
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++ DEBUG INFO END ++++++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Checking that the library is importable and ROCm is callable...
SUCCESS!
Installation was successful!
********************************************************

### Expected behavior

Could you please check the branch difference, so that the multi-backend-refactor could be installed successfully in the latest Rocm6.4 environment, thanks so much ! 

## 评论 (19)

### deep1401 · 2025-05-09

Facing the same error, wonder if you found a solution to this? I have gfx1100 arch of the GPU and cannot compile successfully on bare metal

### smCloudInTheSky · 2025-06-13

Got the same issue with AMD 790XTX within a devcontainer. 
if you need any logs from my install please say so I'll provide it/test anything if needed !

### TotallyTroll · 2025-07-17

With [latest release](https://github.com/bitsandbytes-foundation/bitsandbytes/releases/tag/continuous-release_main) support matrix shows that AMD GPUs (gfx1100) are now supported in Linux.
Yet when installing from release wheel - it uninstalls pytorch-rocm.
So, when I run 'python -m bitsandbytes' it shows next output:
```
================ bitsandbytes v0.47.0.dev0 =================
Platform: Linux-6.11.0-26-generic-x86_64-with-glibc2.39
  libc: glibc-2.39
Python: 3.10.18
PyTorch: 2.7.1+cu126
  CUDA: 12.6
  HIP: N/A
  XPU: N/A
Related packages:
  accelerate: 0.33.0
  diffusers: 0.25.0
  numpy: 2.2.6
  pip: 25.1.1
  peft: not found
  safetensors: 0.4.4
  transformers: 4.52.4
  triton: 3.3.1
  trl: not found
============================================================
PyTorch says CUDA is not available. Possible reasons:
1. CUDA driver not installed
2. Using a CPU-only PyTorch build
3. No GPU detected
```
How to install and use it properly with ROCm?

### matthewdouglas · 2025-07-17

@TotallyTroll 
You could try to install a ROCm PyTorch first, and then use `--no-deps` if the installation of bitsandbytes causes torch to inadvertently reinstall with a CUDA build.

```
pip install --force-reinstall torch==2.7.1 https://download.pytorch.org/whl/rocm6.3
pip install --no-deps --force-reinstall https://github.com/bitsandbytes-foundation/bitsandbytes/releases/download/continuous-release_main/bitsandbytes-1.33.7.preview-py3-none-manylinux_2_24_x86_64.whl
```

### TotallyTroll · 2025-07-18

@matthewdouglas 
It installs bitsandbytes but it doesn't work without deps:
```
python -m bitsandbytes
/tmp/tmpel2ghhcx/main.c:8:10: fatal error: Python.h: No such file or directory
    8 | #include <Python.h>
      |          ^~~~~~~~~~
compilation terminated.
And here goes not useful traceback...
```

### icefairy64 · 2025-07-23

@TotallyTroll - works fine for me using older official ROCm 6.3.4 Docker image:

```sh
$ podman run -it --rm --device /dev/kfd --device /dev/dri/renderD128 musubi-tuner:20250723-6.3.4 python3 -m bitsandbytes================ bitsandbytes v0.47.0.dev0 =================
Platform: Linux-6.14.11-300.fc42.x86_64-x86_64-with-glibc2.39
  libc: glibc-2.39
Python: 3.12.9
PyTorch: 2.4.0a0+git7cecbf6
  CUDA: N/A
  HIP: 6.3.42134-a9a80e791
  XPU: N/A
Related packages:
  accelerate: 1.6.0
  diffusers: 0.32.1
  numpy: 1.26.0
  pip: 25.0
  peft: not found
  safetensors: 0.4.5
  transformers: 4.46.3
  triton: 3.0.0
  trl: not found
============================================================
PyTorch settings found: ROCM_VERSION=63
Checking that the library is importable and ROCm is callable...
SUCCESS!
```

Notably, using images with ROCm 6.4+ fails:

```sh
$ podman run -it --rm --device /dev/kfd --device /dev/dri/renderD128 musubi-tuner:20250723-6.4.1 python3 -m bitsandbytes
bitsandbytes library load error: Configured ROCm binary not found at /opt/conda/envs/py_3.12/lib/python3.12/site-packages/bitsandbytes/libbitsandbytes_rocm64.so
 If you are using Intel CPU/XPU, please install intel_extension_for_pytorch to enable required ops
Traceback (most recent call last):
  File "/opt/conda/envs/py_3.12/lib/python3.12/site-packages/bitsandbytes/cextension.py", line 318, in <module>
    lib = get_native_library()
          ^^^^^^^^^^^^^^^^^^^^
  File "/opt/conda/envs/py_3.12/lib/python3.12/site-packages/bitsandbytes/cextension.py", line 282, in get_native_library
    raise RuntimeError(f"Configured {BNB_BACKEND} binary not found at {cuda_binary_path}")
RuntimeError: Configured ROCm binary not found at /opt/conda/envs/py_3.12/lib/python3.12/site-packages/bitsandbytes/libbitsandbytes_rocm64.so
================ bitsandbytes v0.47.0.dev0 =================
Platform: Linux-6.14.11-300.fc42.x86_64-x86_64-with-glibc2.39
  libc: glibc-2.39
Python: 3.12.10
PyTorch: 2.7.0+git77a7b6c
  CUDA: N/A
  HIP: 6.4.43482-0f2d60242
  XPU: N/A
Related packages:
  accelerate: 1.6.0
  diffusers: 0.32.1
  numpy: 1.26.2
  pip: 25.1.1
  peft: not found
  safetensors: 0.4.5
  transformers: 4.46.3
  triton: 3.3.0
  trl: not found
============================================================
PyTorch settings found: ROCM_VERSION=64
Library not found: /opt/conda/envs/py_3.12/lib/python3.12/site-packages/bitsandbytes/libbitsandbytes_rocm64.so.
Maybe you need to compile it from source? If you compiled from source, check that ROCm version
in PyTorch Settings matches your ROCm install. If not, reinstall PyTorch for your ROCm version
and rebuild bitsandbytes.
Checking that the library is importable and ROCm is callable...
Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "/opt/conda/envs/py_3.12/lib/python3.12/site-packages/bitsandbytes/__main__.py", line 4, in <module>
    main()
  File "/opt/conda/envs/py_3.12/lib/python3.12/site-packages/bitsandbytes/diagnostics/main.py", line 107, in main
    raise e
  File "/opt/conda/envs/py_3.12/lib/python3.12/site-packages/bitsandbytes/diagnostics/main.py", line 96, in main
    sanity_check()
  File "/opt/conda/envs/py_3.12/lib/python3.12/site-packages/bitsandbytes/diagnostics/main.py", line 40, in sanity_check
    adam.step()
  File "/opt/conda/envs/py_3.12/lib/python3.12/site-packages/torch/optim/optimizer.py", line 485, in wrapper
    out = func(*args, **kwargs)
          ^^^^^^^^^^^^^^^^^^^^^
  File "/opt/conda/envs/py_3.12/lib/python3.12/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/opt/conda/envs/py_3.12/lib/python3.12/site-packages/bitsandbytes/optim/optimizer.py", line 293, in step
    self.update_step(group, p, gindex, pindex)
  File "/opt/conda/envs/py_3.12/lib/python3.12/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/opt/conda/envs/py_3.12/lib/python3.12/site-packages/bitsandbytes/optim/optimizer.py", line 522, in update_step
    F.optimizer_update_32bit(
  File "/opt/conda/envs/py_3.12/lib/python3.12/site-packages/bitsandbytes/functional.py", line 1188, in optimizer_update_32bit
    torch.ops.bitsandbytes.optimizer_update_32bit(
  File "/opt/conda/envs/py_3.12/lib/python3.12/site-packages/torch/_ops.py", line 1158, in __call__
    return self._op(*args, **(kwargs or {}))
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/conda/envs/py_3.12/lib/python3.12/site-packages/torch/_compile.py", line 51, in inner
    return disable_fn(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/conda/envs/py_3.12/lib/python3.12/site-packages/torch/_dynamo/eval_frame.py", line 838, in _fn
    return fn(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^
  File "/opt/conda/envs/py_3.12/lib/python3.12/site-packages/torch/library.py", line 719, in func_no_dynamo
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/opt/conda/envs/py_3.12/lib/python3.12/site-packages/bitsandbytes/backends/cuda/ops.py", line 650, in _optimizer_update_32bit_impl
    optim_func(
  File "/opt/conda/envs/py_3.12/lib/python3.12/site-packages/bitsandbytes/cextension.py", line 263, in throw_on_call
    raise RuntimeError(f"{self.formatted_error}Native code method attempted to call: lib.{name}()")
RuntimeError: 
🚨 ROCm VERSION MISMATCH 🚨
Requested ROCm version:          6.4
Detected PyTorch ROCm version:   6.4
Available pre-compiled versions: 
  - 6.1
  - 6.2
  - 6.3

This means:
The version you're trying to use is NOT distributed with this package

Attempted to use bitsandbytes native library functionality but it's not available.

This typically happens when:
1. bitsandbytes doesn't ship with a pre-compiled binary for your ROCm version
2. The library wasn't compiled properly during installation from source

To make bitsandbytes work, the compiled library version MUST exactly match the linked ROCm version.
If your ROCm version doesn't have a pre-compiled binary, you MUST compile from source.

You can COMPILE FROM SOURCE as mentioned here:
   https://huggingface.co/docs/bitsandbytes/main/en/installation?backend=AMD+ROCm#amd-gpu
Original error: Configured ROCm binary not found at /opt/conda/envs/py_3.12/lib/python3.12/site-packages/bitsandbytes/libbitsandbytes_rocm64.so

🔍 Run this command for detailed diagnostics:
python -m bitsandbytes

If you've tried everything and still have issues:
1. Include ALL version info (operating system, bitsandbytes, pytorch, rocm, python)
2. Describe what you've tried in detail
3. Open an issue with this information:
   https://github.com/bitsandbytes-foundation/bitsandbytes/issues

Native code method attempted to call: lib.cadam32bit_grad_fp32()
```

### ai-nikolai · 2025-08-26

@TotallyTroll @matthewdouglas @icefairy64 - is there any update on this and any recommended way of building `bitsandbytes` from "source" on AMD?

### paulogonc · 2025-08-29

Same issue on my machine using Docker image: rocm/pytorch:rocm6.4.3_ubuntu24.04_py3.12_pytorch_release_2.6.0 and manual installation of this latest main release bitsandbytes-1.33.7.preview-py3-none-manylinux_2_24_x86_64.whl

### matthewdouglas · 2025-09-15

Hi everyone,

We do not build for ROCm 6.4+ yet, so it would be best for the time being to use ROCm 6.1-6.3 if you're installing from our preview wheels.

If you're building from source, you can clone the repo and build/install with:

```
cmake -DCOMPUTE_BACKEND=hip -DBNB_ROCM_ARCH="gfx90a;gfx942;gfx1100"
cmake --build .
pip install -e .
```

### deep1401 · 2025-09-16

Hi @matthewdouglas, 
I tried the command you provided but it kept doing a core dump on `python -m bitsandbytes`. 
I found this somewhere and this seems to be working for me:
```
git clone --recurse https://github.com/ROCm/bitsandbytes && cd bitsandbytes && git checkout rocm_enabled_multi_backend && pip install -r requirements-dev.txt && cmake -DCOMPUTE_BACKEND=hip -S . && make -j  && pip install -e .
```

### NO-ob · 2025-09-19

> Hi [@matthewdouglas](https://github.com/matthewdouglas), I tried the command you provided but it kept doing a core dump on `python -m bitsandbytes`. I found this somewhere and this seems to be working for me:
> 
> ```
> git clone --recurse https://github.com/ROCm/bitsandbytes && cd bitsandbytes && git checkout rocm_enabled_multi_backend && pip install -r requirements-dev.txt && cmake -DCOMPUTE_BACKEND=hip -S . && make -j  && pip install -e .
> ```

this didnt work i had to add -DBNB_ROCM_ARCH="gfx1100" to the cmake command to get the 8bit optimizers

### mrs83 · 2025-11-05

On the main branch:

```
python3 -m venv .venv
source .venv/bin/activate
pip install torch --index-url https://download.pytorch.org/whl/nightly/rocm7.0
git clone https://github.com/bitsandbytes-foundation/bitsandbytes.git && cd bitsandbytes/
cmake -DCOMPUTE_BACKEND=hip -S . -DBNB_ROCM_ARCH="gfx1100" -D CMAKE_PREFIX_PATH=/opt/rocm-7.1.0/lib/
make -j
pip install .
amd-smi
python3 -m bitsandbytes
```

```
+------------------------------------------------------------------------------+
| AMD-SMI 26.1.0+5df6c765      amdgpu version: 6.16.6   ROCm version: 7.1.0    |
| VBIOS version: 00107962                                                      |
| Platform: Linux Baremetal                                                    |
|-------------------------------------+----------------------------------------|
| BDF                        GPU-Name | Mem-Uti   Temp   UEC       Power-Usage |
| GPU  HIP-ID  OAM-ID  Partition-Mode | GFX-Uti    Fan               Mem-Usage |
|=====================================+========================================|
| 0000:c5:00.0    AMD Radeon Graphics | N/A        N/A   0             N/A/0 W |
|   0       0     N/A             N/A | N/A        N/A            179/98304 MB |
+-------------------------------------+----------------------------------------+
+------------------------------------------------------------------------------+
| Processes:                                                                   |
|  GPU        PID  Process Name          GTT_MEM  VRAM_MEM  MEM_USAGE     CU % |
|==============================================================================|
|  No running processes found                                                  |
+------------------------------------------------------------------------------+
```

```
================ bitsandbytes v0.49.0.dev0 =================
Platform: Linux-6.16.3-76061603-generic-x86_64-with-glibc2.39
  libc: glibc-2.39
Python: 3.12.3
PyTorch: 2.10.0.dev20251105+rocm7.0
  CUDA: N/A
  HIP: 7.0.2
  XPU: N/A
Related packages:
  accelerate: not found
  diffusers: not found
  numpy: 2.3.4
  pip: 24.0
  peft: not found
  safetensors: not found
  transformers: not found
  triton: 3.5.0
  trl: not found
============================================================
PyTorch settings found: ROCM_VERSION=70
Library not found: /home/ethicalabs/Workspace/BlossomTuneLLM/bitsandbytes/bitsandbytes/libbitsandbytes_rocm70.so.
Maybe you need to compile it from source? If you compiled from source, check that ROCm version
in PyTorch Settings matches your ROCm install. If not, reinstall PyTorch for your ROCm version
and rebuild bitsandbytes.
Checking that the library is importable and ROCm is callable...
Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "/home/ethicalabs/Workspace/BlossomTuneLLM/bitsandbytes/bitsandbytes/__main__.py", line 4, in <module>
    main()
  File "/home/ethicalabs/Workspace/BlossomTuneLLM/bitsandbytes/bitsandbytes/diagnostics/main.py", line 107, in main
    raise e
  File "/home/ethicalabs/Workspace/BlossomTuneLLM/bitsandbytes/bitsandbytes/diagnostics/main.py", line 96, in main
    sanity_check()
  File "/home/ethicalabs/Workspace/BlossomTuneLLM/bitsandbytes/bitsandbytes/diagnostics/main.py", line 40, in sanity_check
    adam.step()
  File "/home/ethicalabs/Workspace/BlossomTuneLLM/bitsandbytes/.venv/lib/python3.12/site-packages/torch/optim/optimizer.py", line 526, in wrapper
    out = func(*args, **kwargs)
          ^^^^^^^^^^^^^^^^^^^^^
  File "/home/ethicalabs/Workspace/BlossomTuneLLM/bitsandbytes/.venv/lib/python3.12/site-packages/torch/utils/_contextlib.py", line 124, in decorate_context
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/home/ethicalabs/Workspace/BlossomTuneLLM/bitsandbytes/bitsandbytes/optim/optimizer.py", line 291, in step
    self.update_step(group, p, gindex, pindex)
  File "/home/ethicalabs/Workspace/BlossomTuneLLM/bitsandbytes/.venv/lib/python3.12/site-packages/torch/utils/_contextlib.py", line 124, in decorate_context
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/home/ethicalabs/Workspace/BlossomTuneLLM/bitsandbytes/bitsandbytes/optim/optimizer.py", line 520, in update_step
    F.optimizer_update_32bit(
  File "/home/ethicalabs/Workspace/BlossomTuneLLM/bitsandbytes/bitsandbytes/functional.py", line 1179, in optimizer_update_32bit
    torch.ops.bitsandbytes.optimizer_update_32bit(
  File "/home/ethicalabs/Workspace/BlossomTuneLLM/bitsandbytes/.venv/lib/python3.12/site-packages/torch/_ops.py", line 1251, in __call__
    return self._op(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/ethicalabs/Workspace/BlossomTuneLLM/bitsandbytes/.venv/lib/python3.12/site-packages/torch/_compile.py", line 54, in inner
    return disable_fn(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/ethicalabs/Workspace/BlossomTuneLLM/bitsandbytes/.venv/lib/python3.12/site-packages/torch/_dynamo/eval_frame.py", line 1136, in _fn
    return fn(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^
  File "/home/ethicalabs/Workspace/BlossomTuneLLM/bitsandbytes/.venv/lib/python3.12/site-packages/torch/library.py", line 725, in func_no_dynamo
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/home/ethicalabs/Workspace/BlossomTuneLLM/bitsandbytes/bitsandbytes/backends/cuda/ops.py", line 650, in _optimizer_update_32bit_impl
    optim_func(
  File "/home/ethicalabs/Workspace/BlossomTuneLLM/bitsandbytes/bitsandbytes/cextension.py", line 263, in throw_on_call
    raise RuntimeError(f"{self.formatted_error}Native code method attempted to call: lib.{name}()")
RuntimeError:
🚨 ROCm VERSION MISMATCH 🚨
Requested ROCm version:          7.0
Detected PyTorch ROCm version:   7.0
Available pre-compiled versions:
  - 7.1

This means:
The version you're trying to use is NOT distributed with this package

Attempted to use bitsandbytes native library functionality but it's not available.

This typically happens when:
1. bitsandbytes doesn't ship with a pre-compiled binary for your ROCm version
2. The library wasn't compiled properly during installation from source

To make bitsandbytes work, the compiled library version MUST exactly match the linked ROCm version.
If your ROCm version doesn't have a pre-compiled binary, you MUST compile from source.

You can COMPILE FROM SOURCE as mentioned here:
   https://huggingface.co/docs/bitsandbytes/main/en/installation?backend=AMD+ROCm#amd-gpu
Original error: Configured ROCm binary not found at /home/ethicalabs/Workspace/BlossomTuneLLM/bitsandbytes/bitsandbytes/libbitsandbytes_rocm70.so

🔍 Run this command for detailed diagnostics:
python -m bitsandbytes

If you've tried everything and still have issues:
1. Include ALL version info (operating system, bitsandbytes, pytorch, rocm, python)
2. Describe what you've tried in detail
3. Open an issue with this information:
   https://github.com/bitsandbytes-foundation/bitsandbytes/issues

Native code method attempted to call: lib.cadam32bit_grad_fp32()
```

This is probably due to the pre-compiled pytorch version. I will try again by compiling pytorch as well. Unfortunately  bitsandbytes wheel is not available on PyTorch's https://download.pytorch.org/whl/nightly/rocm7.0

I also have difficulties to make this working in a project using `uv` as package manager (instead of pip). the pre-compiled wheel also doesn't work in my fresh PopOS 24.04 installation with ROCm 7.1 (after following AMD installation guide https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/quick-start.html). Any suggestion?

### mrs83 · 2025-11-06

I confirm this works with ROCm 7.0.

```
python3 -m venv .venv
source .venv/bin/activate
pip install torch --index-url https://download.pytorch.org/whl/nightly/rocm7.0
git clone https://github.com/bitsandbytes-foundation/bitsandbytes.git && cd bitsandbytes/
cmake -DCOMPUTE_BACKEND=hip -S .
make -j
pip install .
amd-smi
python3 -m bitsandbytes
```

### redo33 · 2025-12-22

I wonder how to compile bitsandbytes with rocm7 on Windows 11.

Thanks.

### rwfsmith · 2025-12-26

> I wonder how to compile bitsandbytes with rocm7 on Windows 11.
> 
> Thanks.

I've been trying to get this working, but it's not been very successful yet. I've gotten successful builds, but it returns junk data or blank lines when trying load a model in 4bit and perform the inference.

### rwfsmith · 2025-12-26

I just tried it again with the latest TheRock ROCm build and it... worked? Maybe? I'll run some more tests. 

### rwfsmith · 2025-12-26

I was able to load Qwen3 30B A3B Instruct 2507 and run some inference, although slowly. There's some odd versioning issues with the 7.10 preview and the TheRock builds, some things return the version as 7,2 and other things as 7.1, but seems to load fine after updating some of the libraries to work with windows and also to switch to using hipinfo to check the warpsize.

### rwfsmith · 2025-12-26

> I wonder how to compile bitsandbytes with rocm7 on Windows 11.
> 
> Thanks.

I don't think I have permission to create a branch, but here's the changes I (Claude Opus 4.5) made:

bitsandbytes-rocm-windows.patch
```
diff --git a/CMakeLists.txt b/CMakeLists.txt
index 922b04b..a0531f5 100644
--- a/CMakeLists.txt
+++ b/CMakeLists.txt
@@ -330,13 +330,20 @@ if(BUILD_HIP)
     find_package_and_print_version(hipsparse REQUIRED)
 
     ## hacky way of excluding hip::amdhip64 (with it linked many tests unexpectedly fail e.g. adam8bit because of inaccuracies)
-    set_target_properties(hip::host PROPERTIES INTERFACE_LINK_LIBRARIES "")
-    set_target_properties(hip-lang::host PROPERTIES INTERFACE_LINK_LIBRARIES "")
-    set(CMAKE_HIP_IMPLICIT_LINK_LIBRARIES "")
+    ## NOTE: On Windows, we need amdhip64 and rocblas for the HIP runtime symbols
+    if(NOT WIN32)
+        set_target_properties(hip::host PROPERTIES INTERFACE_LINK_LIBRARIES "")
+        set_target_properties(hip-lang::host PROPERTIES INTERFACE_LINK_LIBRARIES "")
+        set(CMAKE_HIP_IMPLICIT_LINK_LIBRARIES "")
+    endif()
 
     target_include_directories(bitsandbytes PRIVATE ${CMAKE_SOURCE_DIR} ${CMAKE_SOURCE_DIR}/include ${ROCM_PATH}/include /include)
     target_link_directories(bitsandbytes PRIVATE ${ROCM_PATH}/lib /lib)
     target_link_libraries(bitsandbytes PUBLIC roc::hipblas hip::hiprand roc::hipsparse)
+    if(WIN32)
+        find_package(rocblas REQUIRED)
+        target_link_libraries(bitsandbytes PUBLIC hip::amdhip64 roc::rocblas)
+    endif()
 
     target_compile_definitions(bitsandbytes PUBLIC BNB_USE_HIP)
     set_source_files_properties(${HIP_FILES} PROPERTIES LANGUAGE HIP)
@@ -365,13 +372,15 @@ endif()
 
 if(WIN32)
     set_target_properties(bitsandbytes PROPERTIES PREFIX "lib")
+    # On Windows, DLLs are RUNTIME outputs, not LIBRARY outputs
+    set_target_properties(bitsandbytes PROPERTIES RUNTIME_OUTPUT_DIRECTORY "${PROJECT_SOURCE_DIR}/bitsandbytes")
+    set_target_properties(bitsandbytes PROPERTIES RUNTIME_OUTPUT_DIRECTORY_RELEASE "${PROJECT_SOURCE_DIR}/bitsandbytes")
+    set_target_properties(bitsandbytes PROPERTIES RUNTIME_OUTPUT_DIRECTORY_DEBUG "${PROJECT_SOURCE_DIR}/bitsandbytes")
 endif()
 set_target_properties(bitsandbytes PROPERTIES OUTPUT_NAME ${BNB_OUTPUT_NAME})
 if(MSVC)
     set_target_properties(bitsandbytes PROPERTIES LIBRARY_OUTPUT_DIRECTORY_RELEASE "${PROJECT_SOURCE_DIR}/bitsandbytes")
     set_target_properties(bitsandbytes PROPERTIES LIBRARY_OUTPUT_DIRECTORY_DEBUG "${PROJECT_SOURCE_DIR}/bitsandbytes")
-    set_target_properties(bitsandbytes PROPERTIES RUNTIME_OUTPUT_DIRECTORY_RELEASE "${PROJECT_SOURCE_DIR}/bitsandbytes")
-    set_target_properties(bitsandbytes PROPERTIES RUNTIME_OUTPUT_DIRECTORY_DEBUG "${PROJECT_SOURCE_DIR}/bitsandbytes")
 endif()
 
 set_target_properties(bitsandbytes PROPERTIES LIBRARY_OUTPUT_DIRECTORY "${PROJECT_SOURCE_DIR}/bitsandbytes")
diff --git a/bitsandbytes/cuda_specs.py b/bitsandbytes/cuda_specs.py
index 71e7568..c4caf9b 100644
--- a/bitsandbytes/cuda_specs.py
+++ b/bitsandbytes/cuda_specs.py
@@ -1,6 +1,7 @@
 import dataclasses
 from functools import lru_cache
 import logging
+import platform
 import re
 import subprocess
 from typing import Optional
@@ -83,12 +84,21 @@ def get_rocm_gpu_arch() -> str:
     logger = logging.getLogger(__name__)
     try:
         if torch.version.hip:
-            result = subprocess.run(["rocminfo"], capture_output=True, text=True)
-            match = re.search(r"Name:\s+gfx([a-zA-Z\d]+)", result.stdout)
-            if match:
-                return "gfx" + match.group(1)
-            else:
+            if platform.system() == "Windows":
+                result = subprocess.run(["hipinfo.exe"], capture_output=True, text=True)
+                match = re.search(r"gcnArchName:\s+gfx([a-zA-Z\d]+)", result.stdout)
+                if match:
+                    return "gfx" + match.group(1)
+                
+                # Fallback or if hipinfo fails/not found
                 return "unknown"
+            else:
+                result = subprocess.run(["rocminfo"], capture_output=True, text=True)
+                match = re.search(r"Name:\s+gfx([a-zA-Z\d]+)", result.stdout)
+                if match:
+                    return "gfx" + match.group(1)
+                else:
+                    return "unknown"
         else:
             return "unknown"
     except Exception as e:
@@ -107,8 +117,17 @@ def get_rocm_warpsize() -> int:
     logger = logging.getLogger(__name__)
     try:
         if torch.version.hip:
-            result = subprocess.run(["rocminfo"], capture_output=True, text=True)
-            match = re.search(r"Wavefront Size:\s+([0-9]{2})\(0x[0-9]{2}\)", result.stdout)
+            if platform.system() == "Windows":           
+                result = subprocess.run(["hipinfo.exe"], capture_output=True, text=True)
+                match = re.search(r"Wavefront Size\s*:\s*(\d+)", result.stdout, re.IGNORECASE)
+                if match:
+                    return int(match.group(1))
+            
+                return 64 # Default if hipinfo fails
+            else:
+                result = subprocess.run(["rocminfo"], capture_output=True, text=True)
+                match = re.search(r"Wavefront Size:\s+([0-9]{2})\(0x[0-9]{2}\)", result.stdout)
+
             if match:
                 return int(match.group(1))
             else:
diff --git a/csrc/ops_hip.cuh b/csrc/ops_hip.cuh
index 4eb4462..06db029 100644
--- a/csrc/ops_hip.cuh
+++ b/csrc/ops_hip.cuh
@@ -11,7 +11,9 @@
 #include <cstdint>
 #include <iostream>
 #include <stdio.h>
+#ifndef _WIN32
 #include <unistd.h>
+#endif
 
 #include <common.h>
 #include <functional>
```


And the documentation


# Building bitsandbytes for ROCm on Windows

This guide describes how to build bitsandbytes for AMD ROCm on Windows using the PyTorch ROCm nightly builds.

## Prerequisites

1. **Python 3.12** with a virtual environment
2. **CMake 3.31+** installed and in PATH
3. **Ninja** build system installed and in PATH
4. **Visual Studio 2022** with C++ build tools (for Windows SDK and linker)
5. **Git** for cloning the repository

## Setup

### 1. Create and activate a virtual environment

```cmd
python -m venv .venv
.venv\Scripts\activate.bat
```

### 2. Install PyTorch with ROCm support for gfx1151

```cmd
pip install --index-url https://rocm.nightlies.amd.com/v2/gfx1151/ torch torchaudio torchvision
pip install --index-url https://rocm.nightlies.amd.com/v2/gfx1151/ "rocm[libraries,devel]"
```

### 3. Extract the devel package into the SDK core directory

The ROCm devel package installs as a separate tar archive that needs to be manually extracted:

```cmd
cd %VENV_PATH%\Lib\site-packages
tar -xf rocm_sdk_devel\_devel.tar --strip-components=1 -C _rocm_sdk_core --skip-old-files
```

This extracts the `_rocm_sdk_devel` subdirectory from the tar file into `_rocm_sdk_core`, skipping any files that already exist. This provides the CMake config files (hip-lang, hipblas, etc.) needed for the build.

### 4. Clone bitsandbytes and apply the Windows patch

```cmd
git clone https://github.com/bitsandbytes-foundation/bitsandbytes.git
cd bitsandbytes
git apply ..\bitsandbytes-rocm-windows.patch
```

## Build Commands

Run these commands from a **Developer Command Prompt for VS 2022** or a regular Command Prompt with the environment variables set.

### Set environment variables

Adjust the paths below to match your installation:

```cmd
set VENV_PATH=C:\projects\Unsloth\.venv
set ROCM_SDK=%VENV_PATH%\Lib\site-packages\_rocm_sdk_core

set HIPCXX=%ROCM_SDK%\lib\llvm\bin\clang++.exe
set HIP_PATH=%ROCM_SDK%
set HIP_PLATFORM=amd
set ROCM_PATH=%ROCM_SDK%
set CMAKE_PREFIX_PATH=%ROCM_SDK%\lib\cmake
set HIP_DEVICE_LIB_PATH=%ROCM_SDK%\lib\llvm\amdgcn\bitcode

set LIB=C:\Program Files (x86)\Windows Kits\10\Lib\10.0.22621.0\um\x64;C:\Program Files (x86)\Windows Kits\10\Lib\10.0.22621.0\ucrt\x64;C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Tools\MSVC\14.44.35207\lib\x64
set INCLUDE=C:\Program Files (x86)\Windows Kits\10\Include\10.0.22621.0\ucrt;C:\Program Files (x86)\Windows Kits\10\Include\10.0.22621.0\um;C:\Program Files (x86)\Windows Kits\10\Include\10.0.22621.0\shared;C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Tools\MSVC\14.44.35207\include
```

**Note:** Adjust the Windows SDK version (10.0.22621.0) and MSVC version (14.44.35207) to match your installation.

### Configure with CMake
Update -DCMAKE_HIP_ARCHITECTURES=gfx1151 to match your GPU architecture.

```cmd
cmake -G "Ninja" -DCOMPUTE_BACKEND=hip -S . -DCMAKE_HIP_FLAGS="-I%ROCM_SDK%/include -std=c++17" -DCMAKE_CXX_FLAGS="-std=c++17" -DBNB_ROCM_ARCH=gfx1151 -DCMAKE_HIP_ARCHITECTURES=gfx1151 -DCMAKE_CXX_COMPILER="%ROCM_SDK%/lib/llvm/bin/clang++.exe"
```

### Build

```cmd
cmake --build . --config Release
```

### Build wheel

```cmd
pip wheel . -w dist --no-deps
```

The wheel will be created in the `dist\` folder.

## Install

```cmd
pip install dist\bitsandbytes-0.49.1.dev0-cp312-cp312-win_amd64.whl
```

## Test

```cmd
python -c "import torch; import bitsandbytes as bnb; layer = bnb.nn.Linear4bit(512, 256, bias=False, compute_dtype=torch.float16, quant_type='nf4'); layer = layer.cuda(); x = torch.randn(1, 512, dtype=torch.float16, device='cuda'); y = layer(x); print('Success! Output shape:', y.shape)"
```

## Patch Summary

The patch makes the following changes:

### CMakeLists.txt
1. **Adds `amdhip64` and `rocblas` libraries for Windows** - The upstream intentionally excludes `hip::amdhip64` to avoid accuracy issues in tests, but this breaks linking on Windows since the HIP runtime symbols are required.
2. **Fixes DLL output directory for non-MSVC Windows builds** - Adds `RUNTIME_OUTPUT_DIRECTORY` settings for all Windows builds (not just MSVC), so the DLL is automatically placed in the `bitsandbytes/` folder.

### bitsandbytes/cuda_specs.py
- Uses `hipinfo.exe` instead of `rocminfo` on Windows to detect GPU architecture and wavefront size.

### csrc/ops_hip.cuh
- Conditionally includes `<unistd.h>` only on non-Windows platforms (it doesn't exist on Windows).

## Troubleshooting

### "HIP error: invalid argument" at runtime
- Ensure you're using a compatible PyTorch ROCm nightly from `https://rocm.nightlies.amd.com/v2/gfx1151/`
- Make sure the ROCm DLLs are in your PATH or in the same directory as the Python executable

### CMake can't find hip-lang-config.cmake
- Install the devel package: `pip install --index-url https://rocm.nightlies.amd.com/v2/gfx1151/ "rocm[devel]"`

### Linker errors about undefined symbols (hipMalloc, rocblas_create_handle, etc.)
- Ensure you applied the patch correctly - it adds the required `hip::amdhip64` and `roc::rocblas` libraries on Windows




I'm not really an expert in this stuff, I'm just a lowly .NET developer, so I probably can't help debug any issues, so good luck! 


### matthewdouglas · 2026-02-24

Hi all,

There's multiple issues being discussed here. Since we ship ROCm 6.2 - 7.2 binaries for Linux x86-64 starting in v0.49.0, I would recommend trying the latest release first. 

For issues relating to the ROCm version you build with being mismatched with the PyTorch version, we've merged #1878 which will be included in our next release.

On Windows we've merged #1846, but do not yet distribute this build, so it needs to be built from source.

If there's further problems please open a new issue. Thanks!
