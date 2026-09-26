# [Issue #3069] [Bug]: Cannot dispatch MOE correctly if using naming `w1,w3` or `block_sparse_moe`

source: https://github.com/vllm-project/llm-compressor/issues/3069
state: open | updated: 2026-09-02T12:24:19Z
labels: bug

## 正文

### ⚙️ Your current environment

<details>
<summary>The output of <code>python collect_env.py</code></summary>

```text
Your output of `python collect_env.py` here
```

</details>


### 🐛 Describe the bug

I'm working on running mix-precision MXFP4 for MOE and MXFP8 for others Linears, and find below issues:
1. CT cannot handle `w1, w3` naming for MOE (deepseek V4) 
2. CT cannot detect `block_sparse_moe` naming for MOE (minimax m2.7)

I can workaround it by adding `RoutedExperts` in the targets field, but wonder whether you can fix it.


[        # RoutedExperts was made by combining multiple Linears so need to
        # make sure quantization config for Linear can target it
        quant_config._add_fused_moe_to_target_scheme_map()
        unfused_names = [
            layer_name + proj_name
            for proj_name in [".0.gate_proj", ".0.up_proj", ".0.down_proj"]
        ]](https://github.com/vllm-project/vllm/blob/df3b3422b495a33fd10d0b2f06c051144d6bb2c2/vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe/compressed_tensors_moe.py#L35-L38)

### 🛠️ Steps to reproduce

https://huggingface.co/INCModel/DeepSeek-V4-Flash-MXFP4-Mixed-CT-AutoRound

<img width="803" height="362" alt="Image" src="https://github.com/user-attachments/assets/84a39a71-fcf1-41aa-a663-231efa9faf1d" />

By removing `RoutedExperts` in the targets field, the mode loading fails.

## 评论 (7)

### dsikka · 2026-08-21

Can you explain what you’re trying to do generally? You should be able to target the RoutedExperts in your ignore list. 

### xin3he · 2026-08-24

Hi @dsikka Thank you for the quick responce.
Yes, I can work with `RoutedExperts` module type in my target list.
However, in the ideal user case, MOE for different layers might have different data type (MXFP4/MXFP8). 
So I expect the precision dispatch logic could handle mix-precision with module name only.

### xin3he · 2026-08-24

In my use case, all MOE layer names are contained in the target list, but the precision dispatch cannot work well without setting `RoutedExperts`. 
That's why I mark it as a bug.

### dsikka · 2026-08-24

Please share your full Python scripts so that we can look through them 

### xin3he · 2026-09-02

I reproduced the same issue end-to-end with a small public Mixtral model. This
case demonstrates that the problem can be a **silent incorrect dispatch**, not
necessarily a loading exception.

### Environment

- GPU: NVIDIA B200, compute capability 10.0
- vLLM: `0.28.0`
- vLLM commit: `f25c580af15986f7ccdaaf7639c15896e04cf384`
- llmcompressor: `0.13.0`
- compressed-tensors: `0.18.0`
- transformers: `5.14.1`
- torch: `2.13.0+cu130`
- Model: `TitanML/tiny-mixtral`

### Reproduction

```python
import json
from pathlib import Path

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

from llmcompressor import oneshot
from llmcompressor.modifiers.quantization import QuantizationModifier
from llmcompressor.utils import load_context
from vllm import LLM, SamplingParams


MODEL_ID = "TitanML/tiny-mixtral"
OUTPUT_DIR = Path("tiny-mixtral-mxfp4-ct")

# llm-compressor linearizes Mixtral experts to:
# model.layers.N.mlp.experts.E.{gate,up,down}_proj
with load_context():
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_ID,
        dtype=torch.float32,
        device_map="cpu",
    )

tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)

recipe = QuantizationModifier(
    targets=r"re:.*mlp\.experts\.[0-9]+\.(gate|up|down)_proj$",
    scheme="MXFP4",
    ignore=[],
)

oneshot(model=model, recipe=recipe)

model.save_pretrained(OUTPUT_DIR, save_compressed=True)
tokenizer.save_pretrained(OUTPUT_DIR)

# The exported checkpoint contains packed MXFP4 expert tensors, for example:
# model.layers.0.block_sparse_moe.experts.0.gate_proj.weight_packed
# model.layers.0.block_sparse_moe.experts.0.gate_proj.weight_scale
# model.layers.0.block_sparse_moe.experts.0.up_proj.weight_packed
# model.layers.0.block_sparse_moe.experts.0.down_proj.weight_packed

llm = LLM(
    model=str(OUTPUT_DIR),
    max_model_len=128,
    max_num_seqs=1,
    enforce_eager=True,
    gpu_memory_utilization=0.5,
)
llm.generate(
    ["The capital of France is"],
    SamplingParams(temperature=0.0, max_tokens=4),
)
```

The quantization stage matched and compressed 48 expert linear layers:

```text
Applying quantization config: 100%|██████████| 48/48
Compressing model: 100%|████████████████████| 48/48
```

The exported config contains:

```json
{
  "targets": [
    "re:.*mlp\\.experts\\.[0-9]+\\.(gate|up|down)_proj$"
  ],
  "format": "mxfp4-pack-quantized"
}
```

The checkpoint contains 96 expert tensors (`weight_packed` plus `weight_scale`)
and is approximately 360 MiB.

### Actual result

vLLM recognizes the checkpoint-level quantization as compressed-tensors, but
the routed experts are silently dispatched to an unquantized BF16 backend:

```text
quantization=compressed-tensors
Using FlashInfer TRTLLM Unquantized MoE backend
Using TrtLlmBf16ExpertsMonolithic MoE backend
Model loading took 0.47 GiB memory
```

No exception was raised in this small Mixtral case. This makes the issue
particularly difficult to detect: the model loads and generates, but its
packed MXFP4 experts are not dispatched to an MXFP4 method.

### Workaround

Appending `"RoutedExperts"` to the existing targets fixes dispatch:

```python
config_path = OUTPUT_DIR / "config.json"
config = json.loads(config_path.read_text())
targets = config["quantization_config"]["config_groups"]["group_0"]["targets"]
targets.append("RoutedExperts")
config_path.write_text(json.dumps(config, indent=2) + "\n")
```

After applying the workaround, the same checkpoint selects the expected
backend:

```text
Using CutlassExpertsMxfp4 for MXFP4 MoE
Using MoEPrepareAndFinalizeNoDPEPModular
Using CutlassExpertsMxfp4
Model loading took 0.23 GiB memory
```

### Suspected root cause

`CompressedTensorsMoEMethod.get_moe_method()` currently constructs lookup names
using hard-coded suffixes:

```python
unfused_names = [
    layer_name + proj_name
    for proj_name in [".0.gate_proj", ".0.up_proj", ".0.down_proj"]
]
```

For Mixtral, the vLLM runtime layer prefix contains
`block_sparse_moe.experts`, while llm-compressor's linearized/exported targets
contain `mlp.experts`. The three lookups therefore return `None`, causing
`UnquantizedFusedMoEMethod` to be selected.

`RoutedExperts` already stores architecture-specific checkpoint names through
`ckpt_gate_proj_name`, `ckpt_down_proj_name`, and `ckpt_up_proj_name`, but the
compressed-tensors scheme dispatch does not use those fields.

This appears to be the same root cause as the reported `w1/w3` and
`block_sparse_moe` cases. Dispatch should account for architecture-specific
MoE names, or llm-compressor should include `RoutedExperts` automatically in
the exported targets.

### xin3he · 2026-09-02

Correction for the Mixtral reproduction:

The failure is not caused by the `down_proj` suffix. During quantization,
llm-compressor linearizes Mixtral experts under:

`model.layers.N.mlp.experts.E.{gate,up,down}_proj`

and records that path in `quantization_config`.

When saving, the model/checkpoint conversion restores the Mixtral container
path, producing tensors under:

`model.layers.N.block_sparse_moe.experts.E.{gate,up,down}_proj`

vLLM also constructs the `RoutedExperts` layer with the prefix:

`model.layers.N.block_sparse_moe.experts`

Therefore, the hard-coded CT lookups for
`layer_name + ".0.{gate,up,down}_proj"` are internally consistent with the
projection names, but they do not match the exported config because
`block_sparse_moe.experts != mlp.experts`.

The `w1/w3` case is a related but separate projection-name mismatch.
Both cases indicate that MoE dispatch should not rely on one hard-coded
module path representation. Adding `RoutedExperts` works because it matches
the runtime module class independently of checkpoint/container naming.

### xin3he · 2026-09-02

I noticed that LLMC maintains a mapping to map MOEs to `mlp.experts` and `gate_proj, up_proj, down_proj` names. However, it also requires a remapping in vLLM. 
New models, such as https://huggingface.co/thinkingmachines/Inkling-Small, use special modeling file and skip the remapping in vLLM.
Following the original naming could be a more robost solution.
