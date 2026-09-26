# [Issue #3149] [Bug]: Failed save leaves model in temporary Accelerate offload state

source: https://github.com/vllm-project/llm-compressor/issues/3149
state: closed | updated: 2026-09-09T15:58:25Z
labels: 

## 正文

### Environment

CPU-only WSL Linux 6.6.87.2, Python 3.12.3, torch 2.11.0+cpu, Transformers 5.15.0.

Source-built llm-compressor `8f96fe61feb501b98c2f1c61de2053b50f8d8534` and compressed-tensors `099fa98fea7f3533a8e304a081795a1136ef67c0`. Shallow local builds report `0.1.dev1+g8f96fe6.d20260908` and `0.1.dev1+g099fa98.d20260908`; these are not published release versions. Packages were installed in isolated targets. The first diagnostic used Transformers 5.14.1; I subsequently repeated it with the declared minimum 5.15.0 and observed the same result.

### Bug

`modify_save_pretrained` converts CT offloading to Accelerate for saving, but calls `from_accelerate(model)` only on the success path. A save-side exception after conversion leaves the live model in that temporary representation.

Below, an invalid output directory triggers a real `NotADirectoryError` while writing `recipe.yaml`. Transformers logs that the path is a file and returns before that wrapper metadata operation. The bug reported here is missing offload restoration, not the expected rejection of an invalid output path.

Observed:

| State | CT parameter caches | Accelerate hooks |
| --- | ---: | ---: |
| Before save | 20 | 0 |
| After failed save | 0 | 20 |
| After explicit `from_accelerate` | 13 | 0 |

The initial fixture also offloads empty modules, so the restored cache count need not be exactly 20. After explicit recovery, forward logits matched the original exactly. I am not claiming weight corruption or that forward inference necessarily fails before recovery.

### Reproduction (no model download or GPU)

```python
import tempfile
from pathlib import Path
import torch
from transformers import LlamaConfig, LlamaForCausalLM
from compressed_tensors.offload import OffloadCache, offload_module, from_accelerate
from llmcompressor.transformers.compression.compressed_tensors_utils import modify_save_pretrained

def state(model):
    return (
        sum(isinstance(m._parameters, OffloadCache) for m in model.modules()),
        sum(hasattr(m, '_hf_hook') for m in model.modules()),
    )

torch.manual_seed(42)
model = LlamaForCausalLM(LlamaConfig(
    vocab_size=32, hidden_size=16, intermediate_size=32,
    num_hidden_layers=1, num_attention_heads=2, num_key_value_heads=2,
    max_position_embeddings=32, tie_word_embeddings=False,
)).eval()
for module in model.modules():
    offload_module(module, 'cpu', 'cpu')
modify_save_pretrained(model)
print('before:', state(model))
with tempfile.TemporaryDirectory() as directory:
    target = Path(directory) / 'not-a-directory'
    target.write_text('sentinel')
    try:
        model.save_pretrained(target, save_compressed=False)
    except OSError as error:
        print(type(error).__name__, error)
    print('after failure:', state(model))
    from_accelerate(model)
    print('after explicit recovery:', state(model))
```

### Scope / proposed follow-up

The successful-save restoration was introduced in #2403. #2788 concerns a different failure inside restoration itself (multiple offload directories), rather than the restoration call being skipped. I searched related save/restoration issues and PRs but may have missed ongoing work.

I'd be interested in adding exception-safe restoration and focused regressions if this is available. I have not started an implementation. Please confirm the expected contract and assignment first: after successful conversion, should all save/metadata failures attempt restoration while preserving the original error?

Distributed handling needs explicit care: `from_accelerate` broadcasts the device map, and save uses source-rank-only operations plus the timeout context's barriers. CPU single-process evidence does not establish a distributed fix; all-rank collective ordering and recovery failure semantics must be tested before claiming support.

Investigation and reproduction were AI-assisted. No full suite, quantized GPU, real disk-full, or multi-rank failure test is claimed. This is a focused existing-save-path issue, not an implementation of #3131.

### Update: real two-rank CPU/Gloo reproduction

Subsequently ran the same tiny-model setup under `torch.distributed.run --standalone --nproc-per-node=2`, initializing Gloo with a 5-second default-group timeout after constructing/offloading each model. An independent 20-second Gloo control group gathered results after the save exception, keeping rank 0 alive while rank 1 completed its failing collective. No production functions were patched. An outer 50-second timeout was not reached; the diagnostic completed normally after capturing both expected exceptions.

- Rank 0: `NotADirectoryError` writing `recipe.yaml`, leaving 0 CT caches / 20 Accelerate hooks.
- Rank 1: `save_pretrained_wrapper -> from_accelerate -> dist.broadcast_object_list -> broadcast -> work.wait` raises `RuntimeError: Timed out waiting 5000ms for recv operation to complete`. It has already removed its Accelerate hooks but not redispatched CT caches (0 / 0).

This supersedes only the earlier lack of multi-rank evidence: a CPU/Gloo failure is now reproduced. It does not establish NCCL/GPU behavior or prove a fix. Both ranks were kept alive through the control-group result gathering, so this was not a connection-closed error caused by early source-process termination.


## 评论 (4)

### Roderick-Wu · 2026-09-08

Hi @LOGO127, I think this might be a useful fix. In practice this bug doesn't do much since if an error occurs then the process dies. But I suppose in a case such as the attached example, the format remaining unchanged is more correct behavior How about something just like this?

```python
def modify_save_pretrained(model:PreTrainedModel):

...

                    text_config = model.config.get_text_config()
                    has_mtp = getattr(text_config, "num_mtp_layers", 0) or getattr(
                        text_config, "mtp_num_hidden_layers", 0
                    )
                    if has_mtp:
                        save_mtp_tensors_to_checkpoint(model.name_or_path, save_dir)

            finally:
                    # convert back from accelerate to restore model to original form
                    from_accelerate(model)
```

### LOGO127 · 2026-09-08

Thanks for looking into this, @Roderick-Wu! A small `try/finally` around the save and metadata operations after successful `to_accelerate(model)` makes sense to me. I'll keep the scope to restoring the live model's offload representation, without claiming weight corruption or broad training impact.

Could you assign this issue to me if you're happy with that scope, as requested by the contributing guide? For validation, I propose the existing tiny-model CPU failure case, a successful-save/reload control, and the two-rank Gloo case, since `from_accelerate` participates in a collective. I'll also check that the original save error remains visible when restoration succeeds, and explicitly report any cleanup-failure limitation. No GPU/NCCL validation is claimed.

This work is AI-assisted with Codex; I'll review and validate the change before submitting a PR. Thank you!


### kylesayrs · 2026-09-09

Is there actually a need to restore the model is the save fails? In most cases, sample generation is skipped or not possible because of model size.

If needed, this could be done outside of the save pretrained function
```python
try:
    model.from_pretrained(...)
finally:
    from_accelerate(model)
```


### kylesayrs · 2026-09-09

See https://github.com/vllm-project/llm-compressor/pull/3151#issuecomment-5604822737
