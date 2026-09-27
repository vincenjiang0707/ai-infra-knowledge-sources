# [Issue #152] vLLM api server patching

source: https://github.com/dropbox/hqq/issues/152
state: closed | updated: 2025-06-12T17:21:01Z
labels: 

## 正文

Congrats on the vLLM update!

The current [example](https://github.com/mobiusml/hqq/blob/master/examples/vllm.py) shows how to run gemlite backend with the `LLM` class by applying the patch in the same process. However, this approach doesn't work if a user wants to run the openai compatible api server of vLLM with the `MQLLMEngine` which is generally more suitable for production loads. 

To use that engine with the openai api server we need to directly patch the vLLM [engine.py](https://github.com/vllm-project/vllm/blob/main/vllm/engine/multiprocessing/engine.py) the reason for this is that it is using the `spawn` method to create a child process [here](https://github.com/vllm-project/vllm/blob/b2c3fc5d65485bfed796ee11c2a019d70357ad10/vllm/entrypoints/openai/api_server.py#L192-L204). 


Here is my simple script to apply the patch into the `engine.py`. I am not sure how you would like to incorporate this but wanted to share.

```python
import sys,re
from pathlib import Path

# Find vllm package location
vllm_location = None
for p in sys.path:
    engine_path = Path(p)/"vllm/engine/multiprocessing/engine.py"
    if engine_path.exists(): vllm_location = engine_path; break
if vllm_location is None: raise Exception("Could not find vllm engine.py")
content = vllm_location.read_text()

patch = """
from hqq.utils.vllm import set_vllm_hqq_backend, VLLM_HQQ_BACKEND
set_vllm_hqq_backend(backend=VLLM_HQQ_BACKEND.GEMLITE)

from gemlite.triton_kernels.config import set_autotune
autotune_dict = dict(
    GEMV = False,
    GEMV_REVSPLITK = False,
    GEMV_SPLITK    = False,
    GEMM_SPLITK    = False,
    GEMM           = False,
    EXHAUSTIVE     = False,
    USE_CUDA_GRAPH = False
)
set_autotune(autotune_dict)
"""

# Find last import statement
import_matches = list(re.finditer(r'^(?:from|import)\s+.*$', content, re.MULTILINE))
if not import_matches: raise Exception("No import statements found")
last_import_pos = import_matches[-1].end()

# Insert patch after last import
new_content = content[:last_import_pos] + "\n" + patch + content[last_import_pos:]

# Backup original
backup_path = vllm_location.parent/"engine.py.bak"
if not backup_path.exists(): vllm_location.rename(backup_path)

# Write patched version
vllm_location.write_text(new_content)

print(f"Patched {vllm_location}")
print(f"Backup saved to {backup_path}")
```

## 评论 (4)

### mobicham · 2025-02-21

Thanks Kerem! We internally use vllm with ray via `LLM`, but this could be useful for people using via the openai api server indeed, unless they do it manually in `engine.py` !
Maybe we can put it in `examples/vllm_opanaiserver.py` or something? 

### KeremTurgutlu · 2025-02-22

Sounds good, if you are fine with it to be added as an example I can do that and maybe we can add a little note in the readme for those who want to use the api server in vLLM. By the way is there a reason for you to prefer ray? Native vLLM fastapi server had been working fine for us so far but would love to learn more about ray's advantages. Thanks!

### mobicham · 2025-02-22

Sounds good to me, feel free to do a PR!

It's because we support different backends, not just vllm, since we also need to run other non-llm models.
We have the SDK code open-source by the way: https://github.com/mobiusml/aana_sdk

### mobicham · 2025-06-12

Closing this since now we have support via torchao: https://github.com/vllm-project/vllm/pull/19265
