# [Issue #2441] [BUG] Triton conflict with other packages (eg: flash linear attention)

source: https://github.com/ModelCloud/GPTQModel/issues/2441
state: closed | updated: 2026-03-09T00:59:37Z
labels: bug

## 正文

**Describe the bug**

When building a model (specific code) using both fla-core and autoround+gptqmodel_marlin, the model builds correctly but when forward on the "other" package, if it uses triton, it triggers an error like:

```
  File "/home/vincent/miniconda3/envs/pt2.10/lib/python3.11/site-packages/fla/ops/gated_delta_rule/chunk.py", line 169, in forward
    q, q_rstd = l2norm_fwd(q)
                ^^^^^^^^^^^^^
  File "/home/vincent/miniconda3/envs/pt2.10/lib/python3.11/site-packages/fla/modules/l2norm.py", line 170, in l2norm_fwd
    l2norm_fwd_kernel[grid](
  File "/home/vincent/miniconda3/envs/pt2.10/lib/python3.11/site-packages/triton/runtime/jit.py", line 370, in <lambda>
    return lambda *args, **kwargs: self.run(grid=grid, warmup=False, *args, **kwargs)
                                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/vincent/miniconda3/envs/pt2.10/lib/python3.11/site-packages/gptqmodel/utils/nogil_patcher.py", line 234, in patched_run
    config, used_cached_result, bench_time = _get_config_for_key(self, key, args, kwargs)
                                             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/vincent/miniconda3/envs/pt2.10/lib/python3.11/site-packages/gptqmodel/utils/nogil_patcher.py", line 159, in _get_config_for_key
    with self._cache_lock:
         ^^^^^^^^^^^^^^^^
AttributeError: 'Autotuner' object has no attribute '_cache_lock'
```




**GPU Info**

Show output of:

```
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 590.44.01              Driver Version: 590.44.01      CUDA Version: 13.1     |
+-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA GeForce RTX 5090        On  |   00000000:09:00.0  On |                  N/A |
| 30%   39C    P5             31W /  575W |     110MiB /  32607MiB |     25%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+
|   1  NVIDIA GeForce RTX 4090        On  |   00000000:0A:00.0  On |                  Off |
| 30%   36C    P0             45W /  450W |     518MiB /  24564MiB |     10%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+

```

**Software Info**

Operation System/Version + Python Version

Show output of:
```
Name: GPTQModel
Version: 5.7.0
Summary: Production ready LLM model compression/quantization toolkit with hw accelerated inference support for both cpu/gpu via HF, vLLM, and SGLang.
Home-page: https://github.com/ModelCloud/GPTQModel
Author: 
Author-email: ModelCloud <qubitium@modelcloud.ai>
License-Expression: Apache-2.0
Location: /home/vincent/miniconda3/envs/pt2.10/lib/python3.11/site-packages
Requires: accelerate, datasets, device-smi, dill, hf_transfer, huggingface_hub, kernels, logbar, maturin, numpy, packaging, pillow, protobuf, pyarrow, pypcre, safetensors, threadpoolctl, tokenicer, torch, torchao, transformers
Required-by: 
---
Name: torch
Version: 2.10.0+cu130
Summary: Tensors and Dynamic neural networks in Python with strong GPU acceleration
Home-page: https://pytorch.org
Author: 
Author-email: PyTorch Team <packages@pytorch.org>
License: BSD-3-Clause
Location: /home/vincent/miniconda3/envs/pt2.10/lib/python3.11/site-packages
Requires: cuda-bindings, filelock, fsspec, jinja2, networkx, nvidia-cublas, nvidia-cuda-cupti, nvidia-cuda-nvrtc, nvidia-cuda-runtime, nvidia-cudnn-cu13, nvidia-cufft, nvidia-cufile, nvidia-curand, nvidia-cusolver, nvidia-cusparse, nvidia-cusparselt-cu13, nvidia-nccl-cu13, nvidia-nvjitlink, nvidia-nvshmem-cu13, nvidia-nvtx, sympy, triton, typing-extensions
Required-by: accelerate, auto-round, bitblas, bitsandbytes, entmax, eole, fla-core, flash_attn, GPTQModel, pytorch-lightning, torchmetrics, torchvision, unbabel-comet
---
Name: transformers
Version: 5.2.0
Summary: Transformers: the model-definition framework for state-of-the-art machine learning models in text, vision, audio, and multimodal models, for both inference and training.
Home-page: https://github.com/huggingface/transformers
Author: The Hugging Face team (past and future) with the help of all our contributors (https://github.com/huggingface/transformers/graphs/contributors)
Author-email: transformers@huggingface.co
License: Apache 2.0 License
Location: /home/vincent/miniconda3/envs/pt2.10/lib/python3.11/site-packages
Requires: huggingface-hub, numpy, packaging, pyyaml, regex, safetensors, tokenizers, tqdm, typer-slim
Required-by: auto-round, GPTQModel, TokeNicer, unbabel-comet
---
Name: accelerate
Version: 1.12.0
Summary: Accelerate
Home-page: https://github.com/huggingface/accelerate
Author: The HuggingFace team
Author-email: zach.mueller@huggingface.co
License: Apache
Location: /home/vincent/miniconda3/envs/pt2.10/lib/python3.11/site-packages
Requires: huggingface_hub, numpy, packaging, psutil, pyyaml, safetensors, torch
Required-by: auto-round, GPTQModel
---
Name: triton
Version: 3.6.0
Summary: A language and compiler for custom Deep Learning operations
Home-page: https://github.com/triton-lang/triton/
Author: Philippe Tillet
Author-email: phil@openai.com
License: 
Location: /home/vincent/miniconda3/envs/pt2.10/lib/python3.11/site-packages
Requires: 
Required-by: torch

```

**If you are reporting an inference bug of a post-quantized model, please post the content of `config.json` and `quantize_config.json`.**

**To Reproduce**

How to reproduce this bug if possible.

**Expected behavior**

A clear and concise description of what you expected to happen.

**Model/Datasets**

Make sure your model/dataset is downloadable (on HF for example) so we can reproduce your issue.

**Screenshots**

If applicable, add screenshots to help explain your problem.

**Additional context**

Add any other context about the problem here.


## 评论 (4)

### Qubitium · 2026-03-04

@vince62s Can you poat a script that can reproduce this? GPTQMODEL patches triton loading to fix threaded triton crashes but it appears multiple pkgs use triton and the order of triton code loading causing some inatances to be unpatched.


### vince62s · 2026-03-05

yes exactly the case, so there is only two ways of solving this:
1) the bad one, importing gptqmodel before everything in any case, (overkill)
2) applying the patch below (copilot helped me) just before importing autotround/gptqmodel modules

```
_marlin_preflight_done = False


def _preflight_marlin_import():
    """Import gptqmodel marlin and retroactively patch any pre-existing triton.Autotuner instances.

    gptqmodel's nogil_patcher replaces triton.Autotuner.__init__ and .run() with thread-safe
    versions.  The patched __init__ adds three instance attributes that the patched run()
    requires:

      _cache       – a dict alias for the existing ``cache`` dict (for lock-protected access)
      _cache_lock  – a threading.RLock() for cache serialisation across threads
      _cache_futures – a dict for in-flight autotuning work items

    Instances created before gptqmodel is imported (e.g. FLA's @triton.autotune kernels in
    fla/modules/convolution.py, or eole's own fused_moe.py kernels) are missing all three
    attributes.  When gptqmodel's background thread later calls the patched run(), it crashes
    on the first missing attribute.

    This function:
    1. Imports gptqmodel marlin (side effect: replaces Autotuner.__init__ and .run()).
    2. Walks all live Python objects via gc and fully back-fills the three attributes on any
       Autotuner instance that was created before the patch.

    Because the patching is retroactive and order-independent it works regardless of whether
    triton / FLA / eole's own triton kernels were imported before this function runs.

    A module-level flag ensures the gc scan executes at most once per process.

    Safe to call unconditionally: silently returns if gptqmodel is not installed or CUDA
    is unavailable.
    """
    global _marlin_preflight_done
    if _marlin_preflight_done:
        return
    if not cuda_is_available():
        return
    try:
        from auto_round_extension.cuda.gptqmodel_marlin import get_marlin_layer  # side effect: patches triton.Autotuner
    except ImportError:
        return

    # Retroactively apply the same attribute additions that gptqmodel's patched_init performs,
    # to every Autotuner instance that was created before the patch ran.
    try:
        from triton.runtime.autotuner import Autotuner

        for obj in gc.get_objects():
            if isinstance(obj, Autotuner) and not hasattr(obj, "_cache_lock"):
                # Mirror what gptqmodel's patched_init does for pre-existing instances:
                cache_map = getattr(obj, "cache", {})
                obj._cache = dict(cache_map)
                obj.cache = obj._cache
                obj._cache_lock = threading.RLock()
                obj._cache_futures = {}
    except (ImportError, AttributeError):
        pass

    _marlin_preflight_done = True
```

Hope this helps.

### Qubitium · 2026-03-06

@vince62s Looks like the only way is gptqmodel to expose an externally callable Tirton patch that you can call at the top of your script before all other pkg init/imports. Added to to do list. 

### Qubitium · 2026-03-09

Closed as completed. You can now import and directly call the patcher at the top of your script:

```py
  from gptqmodel import TritonPatch
  TritonPatch.apply()
```
