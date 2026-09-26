# [Issue #2310] FA4 Installation and Usage instructions both fail; ModuleNotFoundError: No module named 'flash_attn.cute'

source: https://github.com/Dao-AILab/flash-attention/issues/2310
state: open | updated: 2026-05-30T14:15:32Z
labels: 

## 正文

Hi, thanks for releasing FA4.

I tried following the readme. Installation fails:

```
pip install flash-attn-4
Defaulting to user installation because normal site-packages is not writeable
ERROR: Ignored the following yanked versions: 0.0.1
ERROR: Could not find a version that satisfies the requirement flash-attn-4 (from versions: 4.0.0b3, 4.0.0b4)

[notice] A new release of pip is available: 25.2 -> 26.0.1
[notice] To update, run: python3 -m pip install --upgrade pip
ERROR: No matching distribution found for flash-attn-4
```

So I specified an explicit version; this is fine:

```
pip install flash-attn-4==4.0.0b4
Installing collected packages: cuda-pathfinder, apache-tvm-ffi, cuda-bindings, torch-c-dlpack-ext, cuda-python, nvidia-cutlass-dsl-libs-base, nvidia-cutlass-dsl, quack-kernels, flash-attn-4
Successfully installed apache-tvm-ffi-0.1.9 cuda-bindings-13.1.1 cuda-pathfinder-1.4.0 cuda-python-13.1.1 flash-attn-4-4.0.0b4 nvidia-cutlass-dsl-4.4.1 nvidia-cutlass-dsl-libs-base-4.4.1 quack-kernels-0.2.10 torch-c-dlpack-ext-0.1.5
```

Then I tried importing FA4:

```
python -c 'from flash_attn.cute import flash_attn_func'
Traceback (most recent call last):
  File "<string>", line 1, in <module>
ModuleNotFoundError: No module named 'flash_attn.cute'
```

FA4 is indeed installed in this env:

```
pip show flash-attn-4
Name: flash-attn-4
Version: 4.0.0b4
Summary: Flash Attention CUTE (CUDA Template Engine) implementation
Home-page: https://github.com/Dao-AILab/flash-attention
Author: Tri Dao
Author-email: 
License: BSD 3-Clause License
Location: /home/alex/.local/lib/python3.10/site-packages
Requires: apache-tvm-ffi, einops, nvidia-cutlass-dsl, quack-kernels, setuptools, torch, torch-c-dlpack-ext, typing_extensions
Required-by: 


pip show flash-attn-3
Name: flash_attn_3
Version: 3.0.0b1
Summary: FlashAttention-3
Home-page: 
Author: 
Author-email: 
License: 
Location: /usr/local/lib/python3.10/dist-packages
Requires: einops, ninja, packaging, torch
Required-by: 

pip show flash-attn
Name: flash_attn
Version: 2.7.4.post1
Summary: Flash Attention: Fast and Memory-Efficient Exact Attention
Home-page: https://github.com/Dao-AILab/flash-attention
Author: Tri Dao
Author-email: tri@tridao.me
License: 
Location: /usr/local/lib/python3.10/dist-packages
Requires: einops, torch
Required-by:
```

The problem is that FA2 (`/usr/local/lib/python3.10/dist-packages/flash_attn`) is found with higher priority.  
This has an `__init__.py`, which prevents its being used as a namespace package as FA4 expects.

Consequently I am reduced to using this pretty horrible code:

```python
try:
    from flash_attn.cute import (
        flash_attn_func,
        flash_attn_varlen_func,
    )
except ImportError:
    # Coreweave'2 FA2 (flash_attn) in dist_packages is found first
    # FA4 (flash_attn.cute) only works if flash_attn can be treated as a namespace package (no __init__.py)
    # but FA2 does not follow this convention
    import importlib.util
    import site
    import sys
    from pathlib import Path

    def find_fa4_cute():
        search_paths = [
            site.getusersitepackages(),
            *site.getsitepackages(),
        ]
        for base in search_paths:
            candidate = Path(base) / "flash_attn" / "cute" / "__init__.py"
            if candidate.exists():
                return candidate
        raise FileNotFoundError("flash_attn.cute not found in any site-packages")

    spec = importlib.util.spec_from_file_location("flash_attn.cute", find_fa4_cute())
    module = importlib.util.module_from_spec(spec)
    sys.modules["flash_attn.cute"] = module
    spec.loader.exec_module(module)

    flash_attn_func = module.flash_attn_func
    flash_attn_varlen_func = module.flash_attn_varlen_func
```

The worst part of this is that I have no symbol-navigation to view what are the arguments of `flash_attn_func` and `flash_attn_varlen_func`; it completely blinds me.

<img width="299" height="129" alt="Image" src="https://github.com/user-attachments/assets/45d78b1b-9299-4e42-a43a-ac4ca59377a4" />

## 评论 (10)

### gugarosa · 2026-03-06

This uninstall prior to FA4 installation solved the very same issue for me: https://github.com/NVIDIA/cutlass/issues/3001#issuecomment-3845717812

### Birch-san · 2026-03-06

uninstalling packages from dist-packages is not a great solution for me.

### gugarosa · 2026-03-06

In that case, you can force the proper path to the package with `PYTHONPATH` and pass along your command line. It is usually wrapped with an extra `python_packages` in the `site-packages/nvidia_cutlass_dsl` of your installation.

### donglixp · 2026-03-11

  image: nvidia/pytorch:26.02-py3
  registry: nvcr.io

This docker can reproduce the above issue.

### tridao · 2026-03-11

hmm idk how to avoid preinstalled FA2 being loaded without modifying PYTHONPATH or uninstalling.
@drisspg any idea on this one?

### drisspg · 2026-03-11

Let me take a look

### Chuge0335 · 2026-03-18

same error

### christopher5106 · 2026-03-30

Same error


### conceptofmind · 2026-05-09

Running into the same error. CUDA/13. GH200 ARM.

### SRagy · 2026-05-30

Adding --pre flag worked for me on the install `pip install --pre "flash-attn-4[cu13]"`
