# [Issue #2656] [Bug]: I encountered an issue while quantizing Kimi-K2.5 from BF16 to W4AFP8

source: https://github.com/vllm-project/llm-compressor/issues/2656
state: closed | updated: 2026-08-28T01:23:58Z
labels: bug, stale

## 正文

### ⚙️ Your current environment

<details>from compressed_tensors.offload import dispatch_model
from datasets import load_dataset
from transformers import AutoModelForCausalLM, AutoTokenizer,AutoConfig

from llmcompressor import oneshot
from llmcompressor.modifiers.quantization import GPTQModifier

# Select model and load it.
model_id = "/data/Kimi-K2-5-bf16"
config = AutoConfig.from_pretrained(model_id,trust_remote_code=True)
if hasattr(config, "vision_config"):
    config.vision_config._attn_implementation = "eager"
    config.vision_config.attn_implementation = "eager"
print(f"Loading model: {model_id}")
model = AutoModelForCausalLM.from_pretrained(model_id, torch_dtype="auto",trust_remote_code=True,config=config,device_map="balanced",offload_folder="/item/offload",)
tokenizer = AutoTokenizer.from_pretrained(model_id,trust_remote_code=True)

# Select calibration dataset.
DATASET_ID = "/workspace/data/ultrachat_200k"
DATASET_SPLIT = "train_sft"

# Select number of samples. 512 samples is a good place to start.
# Increasing the number of samples can improve accuracy.
NUM_CALIBRATION_SAMPLES = 4
MAX_SEQUENCE_LENGTH = 128

# Load dataset and preprocess.
ds = load_dataset(DATASET_ID, split=f"{DATASET_SPLIT}[:{NUM_CALIBRATION_SAMPLES}]")
ds = ds.shuffle(seed=42)


def preprocess(example):
    return {
        "text": tokenizer.apply_chat_template(
            example["messages"],
            tokenize=False,
        )
    }


ds = ds.map(preprocess)


# Tokenize inputs.
def tokenize(sample):
    return tokenizer(
        sample["text"],
        padding=False,
        max_length=MAX_SEQUENCE_LENGTH,
        truncation=True,
        add_special_tokens=False,
    )


ds = ds.map(tokenize, remove_columns=ds.column_names)

# Configure the quantization algorithm to run.
# W4AFP8 scheme: 4-bit integer weights (group 128) + FP8 dynamic per-token activations
recipe = GPTQModifier(targets="Linear", scheme="W4AFP8", ignore=[
            "lm_head",
            "re:.*self_attn.*",
            "re:.*shared_experts.*",
            "re:.*mlp\\.(gate|up|gate_up|down)_proj.*",
            "re:.*vision_tower.*"
        ],sequential_targets=["Linear"])

# Apply algorithms.
oneshot(
    model=model,
    dataset=ds,
    recipe=recipe,
    max_seq_length=MAX_SEQUENCE_LENGTH,
    num_calibration_samples=NUM_CALIBRATION_SAMPLES,
    trust_remote_code_model=True,
)

# Confirm generations of the quantized model look sane.
# print("\n\n")
# print("========== SAMPLE GENERATION ==============")
# dispatch_model(model)
# sample = tokenizer("Hello my name is", return_tensors="pt")
# sample = {key: value.to(model.device) for key, value in sample.items()}
# output = model.generate(**sample, max_new_tokens=100)
# print(tokenizer.decode(output[0]))
# print("==========================================\n\n")

# Save to disk compressed.
# Use quantization_format="pack-quantized" for vLLM compatibility
SAVE_DIR =  "/data/Kimi-K2.5-w4afp8"
model.save_pretrained(
    SAVE_DIR, save_compressed=True, quantization_format="pack-quantized"
)
tokenizer.save_pretrained(SAVE_DIR)

<summary>The output of <code>python collect_env.py</code></summary>

```text
Your output of `python collect_env.py` here
```

</details>
NotImplementedError: Cannot copy out of meta tensor; no data!

### 🐛 Describe the bug

When quantizing Kimi-K2.5 to W4AFP8 on 8 H20 GPUs, I ran into an issue. It seems that some weights were loaded onto the meta device. During calibration, at the final layer, it throws the error:
NotImplementedError: Cannot copy out of meta tensor; no data!

### 🛠️ Steps to reproduce

(69607/69610): Propagating: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 8/8 [00:00<00:00, 846.67it/s]
(69608/69610): Calibrating: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 8/8 [00:00<00:00, 530.27it/s]
2026-04-26T02:39:08.256875-0700 | compress_module_list | INFO - Quantizing language_model.model.layers.60.mlp.experts.383.down_proj using 8.0 samples
2026-04-26T02:39:08.732228-0700 | compress | METRIC - time 0.48s
2026-04-26T02:39:08.732840-0700 | compress | METRIC - error 58.60
2026-04-26T02:39:08.733033-0700 | compress | METRIC - GPU 0 | usage: 51.12% | total memory: 102.6 GB
2026-04-26T02:39:08.733066-0700 | compress | METRIC - GPU 1 | usage: 68.42% | total memory: 102.6 GB
2026-04-26T02:39:08.733088-0700 | compress | METRIC - GPU 2 | usage: 68.42% | total memory: 102.6 GB
2026-04-26T02:39:08.733109-0700 | compress | METRIC - GPU 3 | usage: 68.42% | total memory: 102.6 GB
2026-04-26T02:39:08.733126-0700 | compress | METRIC - GPU 4 | usage: 68.42% | total memory: 102.6 GB
2026-04-26T02:39:08.733142-0700 | compress | METRIC - GPU 5 | usage: 68.42% | total memory: 102.6 GB
2026-04-26T02:39:08.733157-0700 | compress | METRIC - GPU 6 | usage: 68.42% | total memory: 102.6 GB
2026-04-26T02:39:08.733171-0700 | compress | METRIC - GPU 7 | usage: 68.42% | total memory: 102.6 GB
2026-04-26T02:39:08.733443-0700 | compress | METRIC - Compressed module size: 29.704192 MB
(69608/69610): Propagating: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 8/8 [00:00<00:00, 851.22it/s]
(69609/69610): Calibrating: 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 8/8 [00:02<00:00,  3.41it/s]
2026-04-26T02:39:11.095005-0700 | compress_module_list | INFO - Quantizing language_model.lm_head using 8.0 samples
2026-04-26T02:39:18.236338-0700 | compress | METRIC - time 7.14s
2026-04-26T02:39:18.237531-0700 | compress | METRIC - error 20468.06
2026-04-26T02:39:18.237742-0700 | compress | METRIC - GPU 0 | usage: 64.68% | total memory: 102.6 GB
2026-04-26T02:39:18.237776-0700 | compress | METRIC - GPU 1 | usage: 68.42% | total memory: 102.6 GB
2026-04-26T02:39:18.237796-0700 | compress | METRIC - GPU 2 | usage: 68.42% | total memory: 102.6 GB
2026-04-26T02:39:18.237812-0700 | compress | METRIC - GPU 3 | usage: 68.42% | total memory: 102.6 GB
2026-04-26T02:39:18.237827-0700 | compress | METRIC - GPU 4 | usage: 68.42% | total memory: 102.6 GB
2026-04-26T02:39:18.237840-0700 | compress | METRIC - GPU 5 | usage: 68.42% | total memory: 102.6 GB
2026-04-26T02:39:18.237854-0700 | compress | METRIC - GPU 6 | usage: 68.42% | total memory: 102.6 GB
2026-04-26T02:39:18.237868-0700 | compress | METRIC - GPU 7 | usage: 68.42% | total memory: 102.6 GB
2026-04-26T02:39:18.246538-0700 | compress | METRIC - Compressed module size: 2376.33536 MB
(69609/69610): Propagating:   0%|                                                                                                                                                                                                                                  | 0/8 [00:00<?, ?it/s]
Traceback (most recent call last):
  File "/workspace/llm-compressor-0.10.0.1/examples/quantization_w4a8_fp8/kimi-w4afp8.py", line 69, in <module>
    oneshot(
  File "/usr/local/lib/python3.12/dist-packages/llmcompressor/entrypoints/oneshot.py", line 411, in oneshot
    one_shot()
  File "/usr/local/lib/python3.12/dist-packages/llmcompressor/entrypoints/oneshot.py", line 188, in __call__
    self.apply_recipe_modifiers(
  File "/usr/local/lib/python3.12/dist-packages/llmcompressor/entrypoints/oneshot.py", line 239, in apply_recipe_modifiers
    pipeline(
  File "/usr/local/lib/python3.12/dist-packages/llmcompressor/pipelines/independent/pipeline.py", line 45, in __call__
    pipeline(model, dataloader, dataset_args)
  File "/usr/local/lib/python3.12/dist-packages/llmcompressor/pipelines/sequential/helpers.py", line 565, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/llmcompressor/pipelines/sequential/pipeline.py", line 176, in __call__
    activations.update(batch_idx, output)
  File "/usr/local/lib/python3.12/dist-packages/llmcompressor/pipelines/cache.py", line 129, in update
    intermediates = {k: self._offload_value(v, device) for k, v in values.items()}
                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/llmcompressor/pipelines/cache.py", line 260, in _offload_value
    offloaded = value.to(device=offload_device)
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/llmcompressor/pipelines/cache.py", line 329, in __torch_dispatch__
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/torch/_ops.py", line 841, in __call__
    return self._op(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^
NotImplementedError: Cannot copy out of meta tensor; no data!


## 评论 (6)

### fanshao123456 · 2026-04-26

```python
from compressed_tensors.offload import dispatch_model
from datasets import load_dataset
from transformers import AutoModelForCausalLM, AutoTokenizer,AutoConfig

from llmcompressor import oneshot
from llmcompressor.modifiers.quantization import GPTQModifier

model_id = "/data/Kimi-K2-5-bf16"
config = AutoConfig.from_pretrained(model_id,trust_remote_code=True)
if hasattr(config, "vision_config"):
    config.vision_config._attn_implementation = "eager"
    config.vision_config.attn_implementation = "eager"
print(f"Loading model: {model_id}")
model = AutoModelForCausalLM.from_pretrained(model_id, torch_dtype="auto",trust_remote_code=True,config=config,device_map="balanced",offload_folder="/item/offload",)
tokenizer = AutoTokenizer.from_pretrained(model_id,trust_remote_code=True)


DATASET_ID = "/workspace/data/ultrachat_200k"
DATASET_SPLIT = "train_sft"


NUM_CALIBRATION_SAMPLES = 4
MAX_SEQUENCE_LENGTH = 128


ds = load_dataset(DATASET_ID, split=f"{DATASET_SPLIT}[:{NUM_CALIBRATION_SAMPLES}]")
ds = ds.shuffle(seed=42)


def preprocess(example):
    return {
        "text": tokenizer.apply_chat_template(
            example["messages"],
            tokenize=False,
        )
    }


ds = ds.map(preprocess)



def tokenize(sample):
    return tokenizer(
        sample["text"],
        padding=False,
        max_length=MAX_SEQUENCE_LENGTH,
        truncation=True,
        add_special_tokens=False,
    )


ds = ds.map(tokenize, remove_columns=ds.column_names)


recipe = GPTQModifier(targets="Linear", scheme="W4AFP8", ignore=[
            "lm_head",
            "re:.*self_attn.*",
            "re:.*shared_experts.*",
            "re:.*mlp\\.(gate|up|gate_up|down)_proj.*",
            "re:.*vision_tower.*"
        ],sequential_targets=["Linear"])


oneshot(
    model=model,
    dataset=ds,
    recipe=recipe,
    max_seq_length=MAX_SEQUENCE_LENGTH,
    num_calibration_samples=NUM_CALIBRATION_SAMPLES,
    trust_remote_code_model=True,
)


SAVE_DIR =  "/data/Kimi-K2.5-w4afp8"
model.save_pretrained(
    SAVE_DIR, save_compressed=True, quantization_format="pack-quantized"
)
tokenizer.save_pretrained(SAVE_DIR)
```

### brian-dellabetta · 2026-04-27

Hi @fanshao123456 , this may be because you are using `sequential_targets=["Linear"]` which in my experience is a little more brittle than using the decoder layer. you could sanity check by removing `sequential_targets` as an input to oneshot and using a very small calibration dataset.

I am working on kimi k2.6 support, will report back here on how it goes

### fanshao123456 · 2026-04-28

> Hi [@fanshao123456](https://github.com/fanshao123456) , this may be because you are using `sequential_targets=["Linear"]` which in my experience is a little more brittle than using the decoder layer. you could sanity check by removing `sequential_targets` as an input to oneshot and using a very small calibration dataset.
> 
> I am working on kimi k2.6 support, will report back here on how it goes

Thank you very much for your reply. I’ve also identified that the issue is related to sequential_targets. I tried setting the parameters as follows:

sequential_targets=[
    "re:.*layers\\.[0-9]+",
    "re:.*mlp\\.experts\\.[0-9]+",
    # "Linear"
]

However, this leads to OOM. When I add offload_hessians=True, it no longer runs out of memory, but becomes extremely slow. I’m not sure whether this is a viable solution. Looking forward to your reply.

### brian-dellabetta · 2026-04-28

Yeah, this will definitely be a challenge to run GPTQ on such a large model. Some options:
- Since you have 8 GPUs, try with distributed data parallel (DDP). See example [here](https://github.com/vllm-project/llm-compressor/blob/main/examples/awq/llama_example_ddp.py). This can make things faster, but you will probably still have to offload the hessians which get accumulated in the pipeline. Otherwise you will likely still struggle with OOMs.
- Try a less complicated modifier like [autoround](https://github.com/vllm-project/llm-compressor/tree/main/examples/autoround) or [imatrix](https://github.com/vllm-project/llm-compressor/tree/7a52e9e24558bbb4cf8c3a47c0eda630ea6e64be/examples/imatrix). They don't require accumulating hessians, though they aren't set up for parallelization like GPTQ/AWQ are.
- Calibrated compression is less important for such a large model, we often publish quantized very large models with good recovery without needing GPTQ/AWQ. For `W4AFP8` scheme you could just use QuantizationModifier without a calibration dataset, and see if that works well before trying calibrated flows.


### github-actions[bot] · 2026-07-28

This issue has been automatically marked as stale because it has not had any activity within 90 days. It will be automatically closed if no further activity occurs within 30 days. Leave a comment if you feel this issue should remain open. Thank you!

### github-actions[bot] · 2026-08-28

This issue has been automatically closed due to inactivity. Please feel free to reopen if you feel it is still relevant. Thank you!
