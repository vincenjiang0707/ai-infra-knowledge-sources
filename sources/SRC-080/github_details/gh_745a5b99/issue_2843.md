# [Issue #2843] [Bug]: GPTQ modifier error in llm-compressor

source: https://github.com/vllm-project/llm-compressor/issues/2843
state: closed | updated: 2026-09-09T16:04:45Z
labels: bug

## 正文

### ⚙️ Your current environment

When I tried to quantize a Qwen-2.5-14B model using llm-compressor from FP16 to INT8-W8A8(SmoothQuant), it went all good but when I tried to serve it using VLLM, I received an error:

ValueError: {'actorder': static}

 (Note: I know the fix is updated in the ct latest version but just sharing the fixes that helped me)

### 🐛 Describe the bug

VLLM is not able to load the quantized model because the config consists of {actorder=True} because of GPTQ modifier and I have two simple solutions:

1) Just change in the config manually or through script ,{Actorder= False/None}  and try to serve it using VLLM and no issues.

2)It is because of ct , so try to upgrade the ct version and you don't face any issues and It will resolve the issue because the bug is resolved in the ct newer version and not updated in the latest version of vllm.

So, try to use these 2 fixes until we receive the newer version of vllm.


### 🛠️ Steps to reproduce

Quantize Qwen2.5-14B using llm-compressor with SmoothQuant W8A8.
Save the quantized model.
Try to serve the model using VLLM script or openai compatible endpoint
Observe the failure during model loading.

## 评论 (8)

### brian-dellabetta · 2026-06-22

Hi @Pavan6136 , what version of CT? vllm is currently [pinned to 0.17.0](https://github.com/vllm-project/vllm/blob/main/requirements/common.txt#L42)

### dsikka · 2026-06-23

@Pavan6136 do you mind sharing your unchanged compressed config and your script to generate the model?

### Pavan6136 · 2026-06-27

> Hi [@Pavan6136](https://github.com/Pavan6136) , what version of CT? vllm is currently [pinned to 0.17.0](https://github.com/vllm-project/vllm/blob/main/requirements/common.txt#L42)

Hi @brian-dellabetta ,Sorry for late reply.But My version of ct is 0.17.1 . The default version of ct when I installed vllm didn't work and when I upgraded the ct to 0.17.1 it worked.


### Pavan6136 · 2026-06-27

> [@Pavan6136](https://github.com/Pavan6136) do you mind sharing your unchanged compressed config and your script to generate the model?

@dsikka , Sure, Sorry for the late reply.I can't share the exact file because it is in my work ec2 instance, but I can share the script that generated the model.You can run the script and check the config for exact info.

But my compressed config.json contains:
"quantization_config":{
"config_groups": {
"group_0":{
 "format": "int-quantised",
"input_activations": {
"actorder": True,
"block"structure":....
..........

**Script to generate the model:**
`import os
import time
from datetime import datetime
from pathlib import Path

import torch
from datasets import Dataset
from transformers import AutoModelForCausalLM, AutoTokenizer

from llmcompressor import oneshot
from llmcompressor.modifiers.quantization import GPTQModifier
from llmcompressor.modifiers.transform.smoothquant import SmoothQuantModifier

# Optional: helps reduce CUDA memory fragmentation
os.environ["PYTORCH_CUDA_ALLOC_CONF"] = "expandable_segments:True"

# Update these paths for your local environment
MODEL_PATH = Path("/path/to/model")
OUTPUT_PATH = Path("/path/to/output")
CALIBRATION_FILE = Path("/path/to/calibration_data.txt")

NUM_CALIBRATION_SAMPLES = 128
MAX_SEQUENCE_LENGTH = 1024


def load_calibration_data(path: Path):
    """Load calibration samples from a text file."""

    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    samples = [
        line
        for line in text.splitlines()
        if line.strip() and len(line.split()) > 20
    ]

    return samples[:NUM_CALIBRATION_SAMPLES]


calibration_data = load_calibration_data(CALIBRATION_FILE)

print(f"Calibration samples: {len(calibration_data)}")
assert len(calibration_data) >= NUM_CALIBRATION_SAMPLES, (
    f"Need at least {NUM_CALIBRATION_SAMPLES} calibration samples."
)

print(f"Started at: {datetime.now()}")
start = time.time()

model = AutoModelForCausalLM.from_pretrained(
    MODEL_PATH,
    device_map="auto",
    torch_dtype=torch.float16,
)

tokenizer = AutoTokenizer.from_pretrained(
    MODEL_PATH,
    trust_remote_code=True,
)

dataset = Dataset.from_dict({"text": calibration_data})


def tokenize(batch):
    return tokenizer(
        batch["text"],
        truncation=True,
        max_length=MAX_SEQUENCE_LENGTH,
        padding=False,
        add_special_tokens=False,
    )


dataset = dataset.map(
    tokenize,
    batched=True,
    remove_columns=["text"],
)

recipe = [
    SmoothQuantModifier(smoothing_strength=0.8),
    GPTQModifier(
        targets="Linear",
        scheme="W8A8",
        ignore=["lm_head"],
    ),
]

oneshot(
    model=model,
    dataset=dataset,
    recipe=recipe,
    max_seq_length=MAX_SEQUENCE_LENGTH,
    num_calibration_samples=NUM_CALIBRATION_SAMPLES,
)

elapsed = time.time() - start
print(f"Load and quantization time: {elapsed / 60:.1f} minutes")

model.save_pretrained(
    OUTPUT_PATH,
    save_compressed=True,
)
tokenizer.save_pretrained(OUTPUT_PATH)

print(f"Quantized model saved to: {OUTPUT_PATH}")`


After running this, you can check the quantization config, which includes the actorder as true and We can't serve it using VLLM. If we manually remove it or upgrade the ct version, then we can serve it using VLLM.

Please, reach out if any additional info is needed... :)




### kylesayrs · 2026-07-07

Nothing in your compression script indicates to me that activation ordering is being used. Perhaps you accidentally used a base model that was already quantized?

Your behavior described with 0.17 vs 0.17.1 is also interesting, as nothing related to activation ordering landed between those two changes.

### Pavan6136 · 2026-07-14

Thanks @kylesayrs . A few clarifications:

The base model was not pre-quantized. I used the stock [Qwen2.5-14B-Instruct] — its config.json has no quantization_config block. I am sure that it is the base model and not quantized model(can check it with size itself).The actorder field only appeared in the output after running my SmoothQuant + GPTQModifier(scheme="W8A8") recipe.

In my output config, actorder: True shows up and is exactly what vLLM chokes on with ValueError: {'actorder': static}.[ don't know the reason]

On the version behavior — you're right that no activation-ordering logic changed between 0.17.0 and 0.17.1. The difference I saw was purely on the serving/deserialization side: vLLM's pinned compressed-tensors==0.17.0 rejects the config, while bumping only compressed-tensors to 0.17.1 lets it load. So it seems to be a validator tolerance change, not a recipe change.

If it's expected that a plain W8A8 recipe should never write actorder at all, that suggests it's being emitted/serialized somewhere it shouldn't. According to my knowledge the GPTQ modifier is the reason to generate the actorder variable and not the SmoothQuant algo.

Please correct me if I am wrong.



### Pavan6136 · 2026-09-07

@kylesayrs @dsikka : I think this is the reason for my error and also why the ct upgrade works:

The failure comes from `compressed-tensors`, not vLLM. The validator `QuantizationArgs.validate_model_after` in `src/compressed_tensors/quantization/quant_args.py` raises:

```
pydantic_core._pydantic_core.ValidationError: 1 validation error for VllmConfig
Value error, Must use group or tensor_group quantization strategy in order to apply activation ordering
[input_value={'actorder': 'static', ...}]
```

Our SmoothQuant checkpoint (`Qwen2.5-14B-Instruct-1M-SmoothQuant`, W8A8, per-**channel** strategy) carries `actorder: "static"` in `quantization_config`. In the **old** `compressed-tensors` version bundled in our env, the validator rejected *any* non-null `actorder` on a non-group strategy, and the `ActivationOrdering` enum had only `GROUP` (no `WEIGHT`/`STATIC`). So the inert `static` value tripped the guard.

The error message text — `"...in order to apply activation ordering"` (no word "group" before "activation ordering") — confirms it is the pre-fix code path.

**Fix / reference:** PR [vllm-project/compressed-tensors#682 — "Restrict group activation ordering to group quantization strategies"](https://github.com/vllm-project/compressed-tensors/pull/682), first shipped in **v0.16.0** ([release notes](https://github.com/vllm-project/compressed-tensors/releases/tag/0.16.0)). It:
- narrows the check to `actorder == ActivationOrdering.GROUP` (see the `# validate activation ordering and strategy` block in [quant_args.py @ 0.18.0](https://github.com/vllm-project/compressed-tensors/blob/0.18.0/src/compressed_tensors/quantization/quant_args.py)), and
- adds `WEIGHT`/`STATIC` to `ActivationOrdering` with alias `"static" → "weight"`, so `static` no longer maps to group ordering.

Related earlier change: PR [#556 — "Update quantization strategy validation for actorder"](https://github.com/vllm-project/compressed-tensors/pull/556) (v0.14.0).

**Resolution:** upgrade `compressed-tensors` to ≥ 0.16.0 (verified working with `pip install compressed-tensors==0.17.1 --no-deps`).



### kylesayrs · 2026-09-09

@Pavan6136 I'm glad you were able to find a resolution! Closing this for now, feel free to reopen!
