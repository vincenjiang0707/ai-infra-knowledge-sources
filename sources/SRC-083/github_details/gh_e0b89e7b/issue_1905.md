# [Issue #1905] CUDA SETUP ERROR: Missing dependency: libnvJitLink.so.13 - Google Colab

source: https://github.com/bitsandbytes-foundation/bitsandbytes/issues/1905
state: closed | updated: 2026-06-05T14:01:05Z
labels: CUDA Setup

## 正文

### System Info


Trying to install bitsandbytes to run Qwen on Google Colab.

Running into errors when I install : **CUDA SETUP ERROR: Missing dependency: libnvJitLink.so.13**

below is the output when I run:

`!python -m bitsandbytes`

```
bitsandbytes library load error: libnvJitLink.so.13: cannot open shared object file: No such file or directory
Traceback (most recent call last):
  File "/usr/local/lib/python3.12/dist-packages/bitsandbytes/cextension.py", line 320, in <module>
    lib = get_native_library()
          ^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/bitsandbytes/cextension.py", line 298, in get_native_library
    dll = ct.cdll.LoadLibrary(str(binary_path))
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/ctypes/__init__.py", line 460, in LoadLibrary
    return self._dlltype(name)
           ^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/ctypes/__init__.py", line 379, in __init__
    self._handle = _dlopen(self._name, mode)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^
OSError: libnvJitLink.so.13: cannot open shared object file: No such file or directory
=================== bitsandbytes v0.49.2 ===================
Platform: Linux-6.6.113+-x86_64-with-glibc2.35
  libc: glibc-2.35
Python: 3.12.13
PyTorch: 2.11.0+cu130
  CUDA: 13.0
  HIP: N/A
  XPU: N/A
Related packages:
  accelerate: 1.13.0
  diffusers: 0.37.0
  numpy: 2.0.2
  pip: 24.1.2
  peft: 0.18.1
  safetensors: 0.7.0
  transformers: 5.3.0
  triton: 3.6.0
  trl: not found
============================================================
PyTorch settings found: CUDA_VERSION=130, Highest Compute Capability: (7, 5).
Checking that the library is importable and CUDA is callable...
Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "/usr/local/lib/python3.12/dist-packages/bitsandbytes/__main__.py", line 4, in <module>
    main()
  File "/usr/local/lib/python3.12/dist-packages/bitsandbytes/diagnostics/main.py", line 107, in main
    raise e
  File "/usr/local/lib/python3.12/dist-packages/bitsandbytes/diagnostics/main.py", line 96, in main
    sanity_check()
  File "/usr/local/lib/python3.12/dist-packages/bitsandbytes/diagnostics/main.py", line 40, in sanity_check
    adam.step()
  File "/usr/local/lib/python3.12/dist-packages/torch/optim/optimizer.py", line 533, in wrapper
    out = func(*args, **kwargs)
          ^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/torch/utils/_contextlib.py", line 124, in decorate_context
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/bitsandbytes/optim/optimizer.py", line 328, in step
    self.update_step(group, p, gindex, pindex)
  File "/usr/local/lib/python3.12/dist-packages/torch/utils/_contextlib.py", line 124, in decorate_context
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/bitsandbytes/optim/optimizer.py", line 557, in update_step
    F.optimizer_update_32bit(
  File "/usr/local/lib/python3.12/dist-packages/bitsandbytes/functional.py", line 1235, in optimizer_update_32bit
    torch.ops.bitsandbytes.optimizer_update_32bit(
  File "/usr/local/lib/python3.12/dist-packages/torch/_ops.py", line 1269, in __call__
    return self._op(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/torch/_compile.py", line 54, in inner
    return disable_fn(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/eval_frame.py", line 1263, in _fn
    return fn(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/torch/library.py", line 751, in func_no_dynamo
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/bitsandbytes/backends/cuda/ops.py", line 654, in _optimizer_update_32bit_impl
    optim_func(
  File "/usr/local/lib/python3.12/dist-packages/bitsandbytes/cextension.py", line 269, in throw_on_call
    raise RuntimeError(f"{self.formatted_error}Native code method attempted to call: lib.{name}()")
RuntimeError: 
🚨 CUDA SETUP ERROR: Missing dependency: libnvJitLink.so.13 🚨

CUDA 13.x runtime libraries were not found in the LD_LIBRARY_PATH.

To fix this, make sure that:
1. You have installed CUDA 13.x toolkit on your system
2. The CUDA runtime libraries are in your LD_LIBRARY_PATH

You can add them with (and persist the change by adding the line to your .bashrc):
   export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/path/to/cuda-13.x/                    lib64

Original error: libnvJitLink.so.13: cannot open shared object file: No such file or directory

🔍 Run this command for detailed diagnostics:
python -m bitsandbytes

If you've tried everything and still have issues:
1. Include ALL version info (operating system, bitsandbytes, pytorch, cuda, python)
2. Describe what you've tried in detail
3. Open an issue with this information:
   https://github.com/bitsandbytes-foundation/bitsandbytes/issues
```





### Reproduction

Colab link: [https://colab.research.google.com/drive/1qqHcVG7Y8ktloXtnhrjSm1ectdg7CT-m?usp=sharing](url)

### Expected behavior

I had been using this setup for sometime:

```
 !pip install -U "transformers>=4.44.0" "accelerate>=0.32.0" "bitsandbytes>=0.49.1" "torch>=2.3.0" "safetensors>=0.4.0" "torchvision" "torchaudio"

 import os, sys
 print("✅ Packages upgraded. Restarting runtime...")
 os.execv(sys.executable, ['python'] + sys.argv)
```

These ran without any issues but I guess colab has assigned me a new container which is not cooperating with this setup.

## 评论 (4)

### matthewdouglas · 2026-03-25

Hi,

From a timing perspective, I think  issue here is that earlier in this week PyTorch 2.11 was released. Previous versions of PyTorch would install a CUDA 12.x build and its associated dependencies by default. In PyTorch 2.11, the default installation is now the CUDA 13.0 build. It's not necessarily the colab container update.

In Colab by default it looks like PyTorch 2.10.0+cu128 was preinstalled. The log shows:

>   Attempting uninstall: torch
    Found existing installation: torch 2.10.0+cu128
    Uninstalling torch-2.10.0+cu128:
      Successfully uninstalled torch-2.10.0+cu128

So you are upgrading from torch 2.10.0+cu128 to torch 2.11.0+cu130. During this process some of the torch 2.10.0+cu128 dependencies are being left behind and that's causing a conflict, particularly because these are CUDA 12.x dependencies. You can see these with `!pip list | grep nvidia`.

For this specific issue you can do any of the following:
* Uninstall the CUDA 12 dependencies. Particularly `!pip uinstall nvidia-nvjitlink-cu12` should get you past this point, though you may still have other conflicts.
  * There's other libraries preinstalled on Colab with CUDA 12 dependencies that could break here, but you may not be using them anyway, so YMMV.
* Keep torch 2.10.0+cu128 instead, i.e. specify "torch==2.10.0" in your `pip install` command.
* Upgrade to torch 2.11.0+cu128 instead of 2.11.0+cu130
  * Add `--index-url https://download.pytorch.org/whl/cu128` to your `pip install -U` command.

Hope this helps!

### tanvircr7 · 2026-03-25

```
!pip uninstall -y torch torchvision torchaudio
!pip install -U \
  "torch==2.11.0" \
  "torchvision==0.26.0" \
  "torchaudio==2.11.0" \
  --index-url https://download.pytorch.org/whl/cu128
```

installed torch 2.11 with with 12.8 CUDA wheels
and It worked! I'll have to pay closer attention to the logs from now on. Thank you!

### sumpster · 2026-03-28

For what its worth: It looks like they changed the location of the lib in CUDA 13:

~/.local/lib/python3.12/site-packages/nvidia/nvjitlink/lib/libnvJitLink.so.12
~/.local/lib/python3.12/site-packages/nvidia/cu13/lib/libnvJitLink.so.13

When adding the new path to LD_LIBRARY_PATH `python -m bitsandbytes` reports success.

### arthurshelby3210-sudo · 2026-06-05

Coded for Colab
```
import os
import glob
import subprocess

# Step 1: Find where libnvJitLink.so.13 is hiding
search_paths = [
    "/usr/local/lib/python*/dist-packages/nvidia/**/libnvJitLink.so.13",
    "/usr/local/lib/python*/site-packages/nvidia/**/libnvJitLink.so.13",
    "/root/.local/lib/python*/site-packages/nvidia/**/libnvJitLink.so.13",
]

found_paths = []
for pattern in search_paths:
    found_paths.extend(glob.glob(pattern, recursive=True))

# Also try a system find command
try:
    result = subprocess.run(
        ["find", "/usr/local", "-name", "libnvJitLink.so.13"],
        capture_output=True, text=True, timeout=10
    )
    if result.stdout.strip():
        found_paths.extend(result.stdout.strip().split("\n"))
except Exception:
    pass

# Step 2: Add the directory to LD_LIBRARY_PATH
if found_paths:
    lib_dir = os.path.dirname(found_paths[0])
    old_ld = os.environ.get("LD_LIBRARY_PATH", "")
    os.environ["LD_LIBRARY_PATH"] = f"{lib_dir}:{old_ld}" if old_ld else lib_dir
    print(f"✅ Found libnvJitLink.so.13 at: {found_paths[0]}")
    print(f"✅ Added to LD_LIBRARY_PATH: {lib_dir}")
else:
    print("❌ libnvJitLink.so.13 not found. Installing...")
    # Step 3: If not found, install the CUDA 13 nvjitlink package
    subprocess.run(["pip", "install", "-q", "nvidia-nvjitlink-cu13"], check=True)
    
    # Re-search after install
    found_paths = glob.glob(
        "/usr/local/lib/python*/dist-packages/nvidia/**/libnvJitLink.so.13",
        recursive=True
    )
    if found_paths:
        lib_dir = os.path.dirname(found_paths[0])
        os.environ["LD_LIBRARY_PATH"] = f"{lib_dir}:{os.environ.get('LD_LIBRARY_PATH', '')}"
        print(f"✅ Installed and added: {lib_dir}")

# Step 4: Verify bitsandbytes can see it
print("\n--- bitsandbytes diagnostic ---")
subprocess.run(["python", "-m", "bitsandbytes"])
```
