# [Issue #1939] HOW To:  Quantization: Qwen/Qwen3-VL-30B-A3B-Instruct  AWQ

source: https://github.com/vllm-project/llm-compressor/issues/1939
state: closed | updated: 2026-08-18T01:41:55Z
labels: qwen, awq

## 正文


Script:


```
import base64
from io import BytesIO
import torch
from datasets import load_dataset
from transformers import Qwen3VLMoeForConditionalGeneration, AutoProcessor
from llmcompressor import oneshot
from llmcompressor.modifiers.awq import AWQModifier
from llmcompressor.utils import dispatch_for_generation

MODEL_ID = "Qwen/Qwen3-VL-30B-A3B-Instruct"
OUTPUT_DIR = MODEL_ID.split("/")[-1] + "-AWQ-W4A16"

model = Qwen3VLMoeForConditionalGeneration.from_pretrained(
    MODEL_ID,
    torch_dtype="auto",
    device_map="auto",
    trust_remote_code=True,
)
processor = AutoProcessor.from_pretrained(MODEL_ID, trust_remote_code=True)

DATASET_ID = "lmms-lab/flickr30k"
NUM_CALIBRATION_SAMPLES = 256
DATASET_SPLIT = f"test[:{NUM_CALIBRATION_SAMPLES}]"
MAX_SEQUENCE_LENGTH = 1024

ds = load_dataset(DATASET_ID, split=DATASET_SPLIT)
ds = ds.shuffle(seed=42)

def preprocess_and_tokenize(example):
    buffered = BytesIO()
    example["image"].save(buffered, format="PNG")
    encoded_image = base64.b64encode(buffered.getvalue())
    base64_image = f"data:image;base64,{encoded_image.decode('utf-8')}"
    messages = [{"role": "user", "content": [{"type": "image", "image": base64_image}, {"type": "text", "text": "What does the image show?"}]}]
    text = processor.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
    inputs = processor(
        text=[text],
        images=[example["image"]],
        padding=False,
        max_length=MAX_SEQUENCE_LENGTH,
        truncation=True,
    )
    return inputs

ds = ds.map(preprocess_and_tokenize, remove_columns=ds.column_names)

def data_collator(batch):
    assert len(batch) == 1
    return {key: torch.tensor(value) for key, value in batch[0].items()}

recipe = AWQModifier(
    targets="Linear",
    scheme="W4A16",
    ignore=["re:.*lm_head", "re:.*visual.*", "re:.*mlp.gate$"],
    duo_scaling=False,
)

oneshot(
    model=model,
    processor=processor,
    recipe=recipe,
    dataset=ds,
    max_seq_length=MAX_SEQUENCE_LENGTH,
    num_calibration_samples=NUM_CALIBRATION_SAMPLES,
    data_collator=data_collator,
    pipeline="sequential",
)

dispatch_for_generation(model)

messages = [{
    "role": "user",
    "content": [
        {"type": "image", "image": "http://images.cocodataset.org/train2017/000000231895.jpg"},
        {"type": "text", "text": "Please describe the animal in this image\n"},
    ],
}]

prompt = processor.apply_chat_template(messages, add_generation_prompt=True)
inputs = processor(
    text=[prompt],
    images=["http://images.cocodataset.org/train2017/000000231895.jpg"],
    padding=False,
    max_length=MAX_SEQUENCE_LENGTH,
    truncation=True,
    return_tensors="pt",
).to("cuda")

output = model.generate(**inputs, max_new_tokens=100)
processor.decode(output[0], skip_special_tokens=True)

model.save_pretrained(OUTPUT_DIR)
processor.save_pretrained(OUTPUT_DIR)
```

root@308ee78b4020:~# export TOKENIZERS_PARALLELISM=false
root@308ee78b4020:~# python3 te.py 
```
`torch_dtype` is deprecated! Use `dtype` instead!
Loading checkpoint shards: 100%|███████████████████████████████████████████████████████████████████████████████████████| 13/13 [00:10<00:00,  1.23it/s]
2025-10-16T09:33:02.908921+0000 | reset | INFO - Compression lifecycle reset
2025-10-16T09:33:02.917289+0000 | _create_default_logger | INFO - Logging all LLM Compressor modifier-level logs to sparse_logs/16-10-2025_09.33.02.log
2025-10-16T09:33:02.917643+0000 | from_modifiers | INFO - Creating recipe from modifiers
2025-10-16T09:33:02.985165+0000 | on_initialize | INFO - No AWQModifier.mappings provided, inferring from model...
2025-10-16T09:33:02.985360+0000 | get_layer_mappings_from_architecture | INFO - Architecture Qwen3VLMoeForConditionalGeneration not found in mappings. Using default mappings: [AWQMapping(smooth_layer='re:.*input_layernorm$', balance_layers=['re:.*q_proj$', 're:.*k_proj$', 're:.*v_proj$']), AWQMapping(smooth_layer='re:.*v_proj$', balance_layers=['re:.*o_proj$']), AWQMapping(smooth_layer='re:.*post_attention_layernorm$', balance_layers=['re:.*gate_proj$', 're:.*up_proj$']), AWQMapping(smooth_layer='re:.*up_proj$', balance_layers=['re:.*down_proj$'])]
Resolving mapping 1/4 (0 skipped): : 48it [00:00, 4149.27it/s]
Resolving mapping 2/4 (47 skipped): : 48it [00:00, 8543.10it/s]
Resolving mapping 3/4 (0 skipped): : 48it [00:00, 5982.96it/s]
0it [00:00, ?it/s]
2025-10-16T09:33:03.014494+0000 | initialize | INFO - Compression lifecycle initialized for 1 modifiers
2025-10-16T09:33:53.253637+0000 | trace_subgraphs | WARNING - Expected 75 subgraphs, but only traced 49. This is likely due to having wrapped code which calls sequential targets
Preparing cache: 100%|███████████████████████████████████████████████████████████████████████████████████████████████| 256/256 [00:31<00:00,  8.22it/s]
(1/49): Calibrating:   0%|                                                                                                     | 0/256 [00:00<?, ?it/s]
Traceback (most recent call last):
  File "/usr/local/lib/python3.12/dist-packages/llmcompressor/pipelines/sequential/helpers.py", line 73, in forward
    outputs = forward_fn(*args, **kwargs)
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<string>", line 19, in forward
  File "Qwen3VLMoeModel_7739583652820_autowrapped", line 33, in wrapped_2
  File "/usr/local/lib/python3.12/dist-packages/transformers/models/qwen3_vl_moe/modeling_qwen3_vl_moe.py", line 1227, in get_image_features
    image_embeds, deepstack_image_embeds = self.visual(pixel_values, grid_thw=image_grid_thw)
                                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/torch/nn/modules/module.py", line 1773, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/torch/nn/modules/module.py", line 1784, in _call_impl
    return forward_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/transformers/models/qwen3_vl_moe/modeling_qwen3_vl_moe.py", line 769, in forward
    pos_embeds = self.fast_pos_embed_interpolate(grid_thw)
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/transformers/models/qwen3_vl_moe/modeling_qwen3_vl_moe.py", line 738, in fast_pos_embed_interpolate
    pos_embeds = self.pos_embed(idx_tensor) * weight_tensor[:, :, None]
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/torch/nn/modules/module.py", line 1773, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/torch/nn/modules/module.py", line 1784, in _call_impl
    return forward_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/accelerate/hooks.py", line 170, in new_forward
    args, kwargs = module._hf_hook.pre_forward(module, *args, **kwargs)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/compressed_tensors/utils/offload.py", line 574, in keep_onload_pre_forward
    ret = original_pre_forward(self, module, *args, **kwargs)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/accelerate/hooks.py", line 369, in pre_forward
    return send_to_device(args, self.execution_device), send_to_device(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/accelerate/utils/operations.py", line 169, in send_to_device
    return honor_type(
           ^^^^^^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/accelerate/utils/operations.py", line 81, in honor_type
    return type(obj)(generator)
           ^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/accelerate/utils/operations.py", line 170, in <genexpr>
    tensor, (send_to_device(t, device, non_blocking=non_blocking, skip_keys=skip_keys) for t in tensor)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/accelerate/utils/operations.py", line 153, in send_to_device
    return tensor.to(device, non_blocking=non_blocking)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
NotImplementedError: Cannot copy out of meta tensor; no data!

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/root/te.py", line 58, in <module>
    oneshot(
  File "/usr/local/lib/python3.12/dist-packages/llmcompressor/entrypoints/oneshot.py", line 330, in oneshot
    one_shot()
  File "/usr/local/lib/python3.12/dist-packages/llmcompressor/entrypoints/oneshot.py", line 158, in __call__
    self.apply_recipe_modifiers(
  File "/usr/local/lib/python3.12/dist-packages/llmcompressor/entrypoints/oneshot.py", line 201, in apply_recipe_modifiers
    pipeline(
  File "/usr/local/lib/python3.12/dist-packages/llmcompressor/pipelines/sequential/pipeline.py", line 104, in __call__
    subgraph.forward(model, **inputs)
  File "/usr/local/lib/python3.12/dist-packages/llmcompressor/pipelines/sequential/helpers.py", line 75, in forward
    raise RuntimeError(
RuntimeError: Raised an exception during execution of the following code:
1 
2 torch.fx._symbolic_trace.wrap("transformers_models_qwen3_vl_moe_modeling_qwen3_vl_moe_wrapped_0")
3 torch.fx._symbolic_trace.wrap("transformers_models_qwen3_vl_moe_modeling_qwen3_vl_moe_wrapped_1")
4 torch.fx._symbolic_trace.wrap("transformers_models_qwen3_vl_moe_modeling_qwen3_vl_moe_wrapped_2")
5 torch.fx._symbolic_trace.wrap("transformers_models_qwen3_vl_moe_modeling_qwen3_vl_moe_wrapped_3")
6 torch.fx._symbolic_trace.wrap("transformers_models_qwen3_vl_moe_modeling_qwen3_vl_moe_wrapped_5")
7 torch.fx._symbolic_trace.wrap("transformers_models_qwen3_vl_moe_modeling_qwen3_vl_moe_wrapped_4")
8 torch.fx._symbolic_trace.wrap("transformers_models_qwen3_vl_moe_modeling_qwen3_vl_moe_wrapped_6")
9 torch.fx._symbolic_trace.wrap("transformers_models_qwen3_vl_moe_modeling_qwen3_vl_moe_wrapped_7")
10 torch.fx._symbolic_trace.wrap("transformers_models_qwen3_vl_moe_modeling_qwen3_vl_moe_wrapped_8")
11 torch.fx._symbolic_trace.wrap("transformers_models_qwen3_vl_moe_modeling_qwen3_vl_moe_wrapped_9")
12 torch.fx._symbolic_trace.wrap("transformers_models_qwen3_vl_moe_modeling_qwen3_vl_moe_wrapped_10")
13 torch.fx._symbolic_trace.wrap("transformers_models_qwen3_vl_moe_modeling_qwen3_vl_moe_wrapped_11")
14 
15 def forward(self, input_ids : torch.Tensor, attention_mask : torch.Tensor, pixel_values : torch.Tensor, image_grid_thw : torch.Tensor):
16     wrapped_0 = transformers_models_qwen3_vl_moe_modeling_qwen3_vl_moe_wrapped_0(input_ids, None);  wrapped_0 = None
17     wrapped_1 = transformers_models_qwen3_vl_moe_modeling_qwen3_vl_moe_wrapped_1(input_ids, None)
18     getitem = wrapped_1[0];  wrapped_1 = None
19     wrapped_2 = transformers_models_qwen3_vl_moe_modeling_qwen3_vl_moe_wrapped_2(image_grid_thw, None, input_ids, getitem, pixel_values);  getitem = pixel_values = None
20     getitem_1 = wrapped_2[0]
21     getitem_2 = wrapped_2[1]
22     getitem_3 = wrapped_2[2];  getitem_3 = None
23     getitem_4 = wrapped_2[3]
24     getitem_5 = wrapped_2[4];  wrapped_2 = None
25     wrapped_3 = transformers_models_qwen3_vl_moe_modeling_qwen3_vl_moe_wrapped_3(getitem_1, input_ids, getitem_5, None, None, None);  getitem_1 = getitem_5 = None
26     getitem_6 = wrapped_3[0]
27     getitem_7 = wrapped_3[1]
28     getitem_8 = wrapped_3[2]
29     getitem_9 = wrapped_3[3];  getitem_9 = None
30     getitem_10 = wrapped_3[4];  wrapped_3 = None
31     wrapped_5 = transformers_models_qwen3_vl_moe_modeling_qwen3_vl_moe_wrapped_5(getitem_6, attention_mask, None, image_grid_thw, input_ids, getitem_8, None, None, None);  getitem_6 = image_grid_thw = input_ids = None
32     wrapped_6 = transformers_models_qwen3_vl_moe_modeling_qwen3_vl_moe_wrapped_4(None, getitem_8);  wrapped_6 = None
33     wrapped_7 = transformers_models_qwen3_vl_moe_modeling_qwen3_vl_moe_wrapped_6(None, getitem_8);  getitem_8 = None
34     wrapped_4 = transformers_models_qwen3_vl_moe_modeling_qwen3_vl_moe_wrapped_7(getitem_2, getitem_7, None, getitem_4, getitem_10, None);  getitem_2 = getitem_7 = getitem_4 = getitem_10 = None
35     getitem_20 = wrapped_5[0];  getitem_20 = None
36     getitem_21 = wrapped_5[1];  getitem_21 = None
37     getitem_22 = wrapped_5[2];  getitem_22 = None
38     getitem_23 = wrapped_5[3];  getitem_23 = None
39     getitem_24 = wrapped_5[4]
40     getitem_25 = wrapped_5[5];  getitem_25 = None
41     getitem_26 = wrapped_5[6];  getitem_26 = None
42     getitem_27 = wrapped_5[7];  getitem_27 = None
43     getitem_28 = wrapped_5[8];  wrapped_5 = getitem_28 = None
44     getitem_29 = wrapped_7[0];  wrapped_7 = None
45     getitem_11 = wrapped_4[0]
46     getitem_12 = wrapped_4[1];  getitem_12 = None
47     getitem_13 = wrapped_4[2];  getitem_13 = None
48     getitem_14 = wrapped_4[3];  getitem_14 = None
49     getitem_15 = wrapped_4[4];  getitem_15 = None
50     getitem_16 = wrapped_4[5];  getitem_16 = None
51     getitem_17 = wrapped_4[6];  getitem_17 = None
52     getitem_18 = wrapped_4[7];  getitem_18 = None
53     getitem_19 = wrapped_4[8];  wrapped_4 = None
54     wrapped_8 = transformers_models_qwen3_vl_moe_modeling_qwen3_vl_moe_wrapped_8(None, getitem_29, None)
55     getitem_30 = wrapped_8[0]
56     getitem_31 = wrapped_8[1];  wrapped_8 = getitem_31 = None
57     wrapped_9 = transformers_models_qwen3_vl_moe_modeling_qwen3_vl_moe_wrapped_9(getitem_30, getitem_29, getitem_24);  getitem_24 = None
58     getitem_32 = wrapped_9[0];  wrapped_9 = None
59     wrapped_10 = transformers_models_qwen3_vl_moe_modeling_qwen3_vl_moe_wrapped_10(getitem_32);  getitem_32 = None
60     getitem_33 = wrapped_10[0]
61     getitem_34 = wrapped_10[1];  wrapped_10 = None
62     model_language_model_rotary_emb = self.model.language_model.rotary_emb(getitem_29, getitem_33);  getitem_33 = None
63     wrapped_11 = transformers_models_qwen3_vl_moe_modeling_qwen3_vl_moe_wrapped_11(attention_mask, getitem_30, getitem_29, None, getitem_34);  attention_mask = None
64     model_language_model_layers_0 = getattr(self.model.language_model.layers, "0")(getitem_29, attention_mask = wrapped_11, position_ids = getitem_34, past_key_values = None, cache_position = getitem_30, position_embeddings = model_language_model_rotary_emb);  getitem_29 = None
65     return {'getitem_11': getitem_11, 'getitem_19': getitem_19, 'getitem_30': getitem_30, 'getitem_34': getitem_34, 'model_language_model_rotary_emb': model_language_model_rotary_emb, 'wrapped_11': wrapped_11, 'model_language_model_layers_0': model_language_model_layers_0}
66     
```
I don't know where to start anymore, I always end up at the same point.

I'm on RunPod with an 80GB A100.

## 评论 (68)

### JartX · 2025-10-16

https://github.com/vllm-project/llm-compressor/pull/1930

After applying the changes it seems to have started calibrating, thanks!

### JartX · 2025-10-16

Hi can you help me? 
@ronantakizawa 

(49/49): Propagating: 100%|████████████████████████████████████████████████████████████████████████████████████████| 256/256 [00:00<00:00, 1321.68it/s]
Smoothing: 0it [00:00, ?it/s]
Calibrating weights: 192it [00:00, 235.43it/s]
2025-10-16T11:43:48.505168+0000 | finalize | INFO - Compression lifecycle finalized for 1 modifiers
2025-10-16T11:43:48.665492+0000 | get_model_compressor | INFO - skip_sparsity_compression_stats set to True. Skipping sparsity compression statistic calculations. No sparsity compressor will be applied.
Compressing model: 192it [00:04, 39.95it/s]
2025-10-16T11:44:29.624372+0000 | get_model_compressor | INFO - skip_sparsity_compression_stats set to True. Skipping sparsity compression statistic calculations. No sparsity compressor will be applied.
Compressing model: 192it [00:00, 962.67it/s]

but without compression

Original model size 57gb
Compressed 57Gb

### brian-dellabetta · 2025-10-16

I will try this tomorrow. 

Duplicate of #1914 

Possibly related to #1571 

### JartX · 2025-10-16

@brian-dellabetta
This is the only Awq model that loads me in rocm rdna3: https://huggingface.co/QuantTrio/Qwen3-VL-30B-A3B-Instruct-AWQ

### JartX · 2025-10-16

Hi @brian-dellabetta many thanks for your time

```
import base64
from io import BytesIO
import torch
from datasets import load_dataset
from transformers import Qwen3VLMoeForConditionalGeneration, AutoProcessor
from llmcompressor import oneshot
from llmcompressor.modifiers.awq import AWQModifier
from llmcompressor.modeling import replace_modules_for_calibration

MODEL_ID = "Qwen/Qwen3-VL-30B-A3B-Instruct"
OUTPUT_DIR = MODEL_ID.split("/")[-1] + "-AWQ-W4A16"

model = Qwen3VLMoeForConditionalGeneration.from_pretrained(
    MODEL_ID,
    torch_dtype=torch.bfloat16,
    device_map=None,
    trust_remote_code=True,
)
processor = AutoProcessor.from_pretrained(MODEL_ID, trust_remote_code=True)

model = replace_modules_for_calibration(model)

DATASET_ID = "lmms-lab/flickr30k"
NUM_CALIBRATION_SAMPLES = 256
DATASET_SPLIT = f"test[:{NUM_CALIBRATION_SAMPLES}]"
MAX_SEQUENCE_LENGTH = 1024

ds = load_dataset(DATASET_ID, split=DATASET_SPLIT)
ds = ds.shuffle(seed=42)

def preprocess_and_tokenize(example):
    buffered = BytesIO()
    example["image"].save(buffered, format="PNG")
    encoded_image = base64.b64encode(buffered.getvalue())
    base64_image = f"data:image;base64,{encoded_image.decode('utf-8')}"
    messages = [{
        "role": "user",
        "content": [
            {"type": "image", "image": base64_image},
            {"type": "text", "text": "What does the image show?"}
        ]
    }]
    text = processor.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True
    )
    inputs = processor(
        text=[text],
        images=[example["image"]],
        padding=False,
        max_length=MAX_SEQUENCE_LENGTH,
        truncation=True,
    )
    return inputs

ds = ds.map(preprocess_and_tokenize, remove_columns=ds.column_names)

def data_collator(batch):
    assert len(batch) == 1
    return {key: torch.tensor(value) for key, value in batch[0].items()}

recipe = AWQModifier(
    targets="Linear",
    scheme="W4A16",
    ignore=["re:.*lm_head", "re:.*visual.*", "re:.*mlp.gate$"],
    duo_scaling=False,
)

oneshot(
    model=model,
    processor=processor,
    recipe=recipe,
    dataset=ds,
    max_seq_length=MAX_SEQUENCE_LENGTH,
    num_calibration_samples=NUM_CALIBRATION_SAMPLES,
    data_collator=data_collator,
    pipeline="sequential",
)

model.save_pretrained(OUTPUT_DIR, save_compressed=True)
processor.save_pretrained(OUTPUT_DIR)


```
its generate config:

https://pastebin.com/yvY5XEMN

bvut is very different than:

https://huggingface.co/QuantTrio/Qwen3-VL-30B-A3B-Instruct-AWQ/raw/main/config.json

Right now the only quantization I can load into rocm rdna3 is awq quanttrio, and I can't replicate it, to fit and then quantize


### JartX · 2025-10-16

@Jun-Howie

### brian-dellabetta · 2025-10-16

Hi @JartX , the config.json will look completely different than the one in https://huggingface.co/QuantTrio/Qwen3-VL-30B-A3B-Instruct-AWQ/raw/main/config.json. It is specific to the `quantization_config.quant_method` field, which is `compressed-tensors` for us and `awq` for this model, which I believe means AutoAWQ was used to create it. See #1909  for more info

### BenasdTW · 2025-10-16

> It is specific to the `quantization_config.quant_method` field, which is `compressed-tensors` for us and `awq` for this model, which I believe means AutoAWQ was used to create it

After inspecting the `config.json`, it seems to resemble other quantized models produced by `AutoAWQ`.
However, the `AutoAWQ` GitHub repository was archived and has not been maintained since long before the `Qwen3-VL` model was released.

### JartX · 2025-10-17

@brian-dellabetta @BenasdTW many thanks for your answer this code quantize the model:

```
import base64
from io import BytesIO
import torch
from datasets import load_dataset
from transformers import Qwen3VLMoeForConditionalGeneration, AutoProcessor
from llmcompressor import oneshot
from llmcompressor.modifiers.awq import AWQModifier
from llmcompressor.modeling import replace_modules_for_calibration

MODEL_ID = "Qwen/Qwen3-VL-30B-A3B-Instruct"
OUTPUT_DIR = MODEL_ID.split("/")[-1] + "-AWQ-W8A16"

model = Qwen3VLMoeForConditionalGeneration.from_pretrained(
    MODEL_ID,
    torch_dtype=torch.bfloat16,
    device_map=None,
    trust_remote_code=True,
)
processor = AutoProcessor.from_pretrained(MODEL_ID, trust_remote_code=True)
model = replace_modules_for_calibration(model)

DATASET_ID = "lmms-lab/flickr30k"
NUM_CALIBRATION_SAMPLES = 256
DATASET_SPLIT = f"test[:{NUM_CALIBRATION_SAMPLES}]"
MAX_SEQUENCE_LENGTH = 1024

ds = load_dataset(DATASET_ID, split=DATASET_SPLIT)
ds = ds.shuffle(seed=42)

def preprocess_and_tokenize(example):
    buffered = BytesIO()
    example["image"].save(buffered, format="PNG")
    encoded_image = base64.b64encode(buffered.getvalue())
    base64_image = f"data:image;base64,{encoded_image.decode('utf-8')}"
    messages = [{
        "role": "user",
        "content": [
            {"type": "image", "image": base64_image},
            {"type": "text", "text": "What does the image show?"}
        ]
    }]
    text = processor.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True
    )
    inputs = processor(
        text=[text],
        images=[example["image"]],
        padding=False,
        max_length=MAX_SEQUENCE_LENGTH,
        truncation=True,
    )
    return inputs

ds = ds.map(preprocess_and_tokenize, remove_columns=ds.column_names)

def data_collator(batch):
    assert len(batch) == 1
    return {key: torch.tensor(value) for key, value in batch[0].items()}

recipe = AWQModifier(
    ignore=["re:.*lm_head", "re:.*visual.*", "re:.*mlp.gate$","re:.*mlp.shared_expert_gate$"],
    duo_scaling=False,
    config_groups={
        "group_0": {
            "targets": ["Linear"],
            "input_activations": None,
            "output_activations": None,
            "weights": {
                "num_bits": 8,
                "type": "int",
                "symmetric": True,
                "strategy": "group",
                "group_size": 32,
                "observer": "mse",
            }
        }
    }
)

oneshot(
    model=model,
    processor=processor,
    recipe=recipe,
    dataset=ds,
    max_seq_length=MAX_SEQUENCE_LENGTH,
    num_calibration_samples=NUM_CALIBRATION_SAMPLES,
    data_collator=data_collator,
    pipeline="sequential",
)

model.save_pretrained(OUTPUT_DIR, save_compressed=True)
processor.save_pretrained(OUTPUT_DIR)

```

### JartX · 2025-10-17

https://github.com/vllm-project/llm-compressor/issues/1914
@ZanePoe using transformers==4.57.1

### JartX · 2025-10-17

> > It is specific to the `quantization_config.quant_method` field, which is `compressed-tensors` for us and `awq` for this model, which I believe means AutoAWQ was used to create it
> 
> After inspecting the `config.json`, it seems to resemble other quantized models produced by `AutoAWQ`. However, the `AutoAWQ` GitHub repository was archived and has not been maintained since long before the `Qwen3-VL` model was released.

Thanks for the answer. I was confused because I didn't see awq in the quant_method. How is it identified internally? When quantifying with GPTmodel, autoround, or AutoAwq, does the quant_method change

### JartX · 2025-10-17

@brian-dellabetta @dsikka 

the quant_config
{
"architectures": [
"Qwen3VLMoeForConditionalGeneration"
],
"dtype": "bfloat16",
"image_token_id": 151655,
"model_type": "qwen3_vl_moe",
"quantization_config": {
"config_groups": {
"group_0": {
"format": "pack-quantized",
"input_activations": null,
"output_activations": null,
"targets": [
"Linear"
],
"weights": {
"actorder": null,
"block_structure": null,
"dynamic": false,
"group_size": 32,
"num_bits": 8,
"observer": "mse",
"observer_kwargs": {},
"strategy": "group",
"symmetric": true,
"type": "int"
}
}
},
"format": "pack-quantized",
"global_compression_ratio": null,
"ignore": [
"model.visual.blocks.0.attn.qkv",
"model.visual.blocks.0.attn.proj",
"model.visual.blocks.0.mlp.linear_fc1",
"model.visual.blocks.0.mlp.linear_fc2",
"model.visual.blocks.1.attn.qkv",
"model.visual.blocks.1.attn.proj",
"model.visual.blocks.1.mlp.linear_fc1",
"model.visual.blocks.1.mlp.linear_fc2",
"model.visual.blocks.2.attn.qkv",
"model.visual.blocks.2.attn.proj",
"model.visual.blocks.2.mlp.linear_fc1",
"model.visual.blocks.2.mlp.linear_fc2",
"model.visual.blocks.3.attn.qkv",
"model.visual.blocks.3.attn.proj",
"model.visual.blocks.3.mlp.linear_fc1",
"model.visual.blocks.3.mlp.linear_fc2",
"model.visual.blocks.4.attn.qkv",
"model.visual.blocks.4.attn.proj",
"model.visual.blocks.4.mlp.linear_fc1",
"model.visual.blocks.4.mlp.linear_fc2",
"model.visual.blocks.5.attn.qkv",
"model.visual.blocks.5.attn.proj",
"model.visual.blocks.5.mlp.linear_fc1",
"model.visual.blocks.5.mlp.linear_fc2",
"model.visual.blocks.6.attn.qkv",
"model.visual.blocks.6.attn.proj",
"model.visual.blocks.6.mlp.linear_fc1",
"model.visual.blocks.6.mlp.linear_fc2",
"model.visual.blocks.7.attn.qkv",
"model.visual.blocks.7.attn.proj",
"model.visual.blocks.7.mlp.linear_fc1",
"model.visual.blocks.7.mlp.linear_fc2",
"model.visual.blocks.8.attn.qkv",
"model.visual.blocks.8.attn.proj",
"model.visual.blocks.8.mlp.linear_fc1",
"model.visual.blocks.8.mlp.linear_fc2",
"model.visual.blocks.9.attn.qkv",
"model.visual.blocks.9.attn.proj",
"model.visual.blocks.9.mlp.linear_fc1",
"model.visual.blocks.9.mlp.linear_fc2",
"model.visual.blocks.10.attn.qkv",
"model.visual.blocks.10.attn.proj",
"model.visual.blocks.10.mlp.linear_fc1",
"model.visual.blocks.10.mlp.linear_fc2",
"model.visual.blocks.11.attn.qkv",
"model.visual.blocks.11.attn.proj",
"model.visual.blocks.11.mlp.linear_fc1",
"model.visual.blocks.11.mlp.linear_fc2",
"model.visual.blocks.12.attn.qkv",
"model.visual.blocks.12.attn.proj",
"model.visual.blocks.12.mlp.linear_fc1",
"model.visual.blocks.12.mlp.linear_fc2",
"model.visual.blocks.13.attn.qkv",
"model.visual.blocks.13.attn.proj",
"model.visual.blocks.13.mlp.linear_fc1",
"model.visual.blocks.13.mlp.linear_fc2",
"model.visual.blocks.14.attn.qkv",
"model.visual.blocks.14.attn.proj",
"model.visual.blocks.14.mlp.linear_fc1",
"model.visual.blocks.14.mlp.linear_fc2",
"model.visual.blocks.15.attn.qkv",
"model.visual.blocks.15.attn.proj",
"model.visual.blocks.15.mlp.linear_fc1",
"model.visual.blocks.15.mlp.linear_fc2",
"model.visual.blocks.16.attn.qkv",
"model.visual.blocks.16.attn.proj",
"model.visual.blocks.16.mlp.linear_fc1",
"model.visual.blocks.16.mlp.linear_fc2",
"model.visual.blocks.17.attn.qkv",
"model.visual.blocks.17.attn.proj",
"model.visual.blocks.17.mlp.linear_fc1",
"model.visual.blocks.17.mlp.linear_fc2",
"model.visual.blocks.18.attn.qkv",
"model.visual.blocks.18.attn.proj",
"model.visual.blocks.18.mlp.linear_fc1",
"model.visual.blocks.18.mlp.linear_fc2",
"model.visual.blocks.19.attn.qkv",
"model.visual.blocks.19.attn.proj",
"model.visual.blocks.19.mlp.linear_fc1",
"model.visual.blocks.19.mlp.linear_fc2",
"model.visual.blocks.20.attn.qkv",
"model.visual.blocks.20.attn.proj",
"model.visual.blocks.20.mlp.linear_fc1",
"model.visual.blocks.20.mlp.linear_fc2",
"model.visual.blocks.21.attn.qkv",
"model.visual.blocks.21.attn.proj",
"model.visual.blocks.21.mlp.linear_fc1",
"model.visual.blocks.21.mlp.linear_fc2",
"model.visual.blocks.22.attn.qkv",
"model.visual.blocks.22.attn.proj",
"model.visual.blocks.22.mlp.linear_fc1",
"model.visual.blocks.22.mlp.linear_fc2",
"model.visual.blocks.23.attn.qkv",
"model.visual.blocks.23.attn.proj",
"model.visual.blocks.23.mlp.linear_fc1",
"model.visual.blocks.23.mlp.linear_fc2",
"model.visual.blocks.24.attn.qkv",
"model.visual.blocks.24.attn.proj",
"model.visual.blocks.24.mlp.linear_fc1",
"model.visual.blocks.24.mlp.linear_fc2",
"model.visual.blocks.25.attn.qkv",
"model.visual.blocks.25.attn.proj",
"model.visual.blocks.25.mlp.linear_fc1",
"model.visual.blocks.25.mlp.linear_fc2",
"model.visual.blocks.26.attn.qkv",
"model.visual.blocks.26.attn.proj",
"model.visual.blocks.26.mlp.linear_fc1",
"model.visual.blocks.26.mlp.linear_fc2",
"model.visual.merger.linear_fc1",
"model.visual.merger.linear_fc2",
"model.visual.deepstack_merger_list.0.linear_fc1",
"model.visual.deepstack_merger_list.0.linear_fc2",
"model.visual.deepstack_merger_list.1.linear_fc1",
"model.visual.deepstack_merger_list.1.linear_fc2",
"model.visual.deepstack_merger_list.2.linear_fc1",
"model.visual.deepstack_merger_list.2.linear_fc2",
"model.language_model.layers.0.mlp.gate",
"model.language_model.layers.1.mlp.gate",
"model.language_model.layers.2.mlp.gate",
"model.language_model.layers.3.mlp.gate",
"model.language_model.layers.4.mlp.gate",
"model.language_model.layers.5.mlp.gate",
"model.language_model.layers.6.mlp.gate",
"model.language_model.layers.7.mlp.gate",
"model.language_model.layers.8.mlp.gate",
"model.language_model.layers.9.mlp.gate",
"model.language_model.layers.10.mlp.gate",
"model.language_model.layers.11.mlp.gate",
"model.language_model.layers.12.mlp.gate",
"model.language_model.layers.13.mlp.gate",
"model.language_model.layers.14.mlp.gate",
"model.language_model.layers.15.mlp.gate",
"model.language_model.layers.16.mlp.gate",
"model.language_model.layers.17.mlp.gate",
"model.language_model.layers.18.mlp.gate",
"model.language_model.layers.19.mlp.gate",
"model.language_model.layers.20.mlp.gate",
"model.language_model.layers.21.mlp.gate",
"model.language_model.layers.22.mlp.gate",
"model.language_model.layers.23.mlp.gate",
"model.language_model.layers.24.mlp.gate",
"model.language_model.layers.25.mlp.gate",
"model.language_model.layers.26.mlp.gate",
"model.language_model.layers.27.mlp.gate",
"model.language_model.layers.28.mlp.gate",
"model.language_model.layers.29.mlp.gate",
"model.language_model.layers.30.mlp.gate",
"model.language_model.layers.31.mlp.gate",
"model.language_model.layers.32.mlp.gate",
"model.language_model.layers.33.mlp.gate",
"model.language_model.layers.34.mlp.gate",
"model.language_model.layers.35.mlp.gate",
"model.language_model.layers.36.mlp.gate",
"model.language_model.layers.37.mlp.gate",
"model.language_model.layers.38.mlp.gate",
"model.language_model.layers.39.mlp.gate",
"model.language_model.layers.40.mlp.gate",
"model.language_model.layers.41.mlp.gate",
"model.language_model.layers.42.mlp.gate",
"model.language_model.layers.43.mlp.gate",
"model.language_model.layers.44.mlp.gate",
"model.language_model.layers.45.mlp.gate",
"model.language_model.layers.46.mlp.gate",
"model.language_model.layers.47.mlp.gate",
"lm_head"
],
"kv_cache_scheme": null,
"quant_method": "compressed-tensors",
"quantization_status": "compressed",
"sparsity_config": {},
"transform_config": {},
"version": "0.12.3.a20251013"
},
"text_config": {
"attention_bias": false,
"attention_dropout": 0.0,
"bos_token_id": 151643,
"decoder_sparse_step": 1,
"dtype": "bfloat16",
"eos_token_id": 151645,
"head_dim": 128,
"hidden_act": "silu",
"hidden_size": 2048,
"initializer_range": 0.02,
"intermediate_size": 6144,
"max_position_embeddings": 262144,
"mlp_only_layers": [],
"model_type": "qwen3_vl_moe_text",
"moe_intermediate_size": 768,
"norm_topk_prob": true,
"num_attention_heads": 32,
"num_experts": 128,
"num_experts_per_tok": 8,
"num_hidden_layers": 48,
"num_key_value_heads": 4,
"rms_norm_eps": 1e-06,
"rope_scaling": {
"mrope_interleaved": true,
"mrope_section": [
24,
20,
20
],
"rope_type": "default"
},
"rope_theta": 5000000,
"router_aux_loss_coef": 0.001,
"use_cache": true,
"vocab_size": 151936
},
"tie_word_embeddings": false,
"transformers_version": "4.57.0",
"video_token_id": 151656,
"vision_config": {
"deepstack_visual_indexes": [
8,
16,
24
],
"depth": 27,
"dtype": "bfloat16",
"hidden_act": "gelu_pytorch_tanh",
"hidden_size": 1152,
"in_channels": 3,
"initializer_range": 0.02,
"intermediate_size": 4304,
"model_type": "qwen3_vl_moe",
"num_heads": 16,
"num_position_embeddings": 2304,
"out_hidden_size": 2048,
"patch_size": 16,
"spatial_merge_size": 2,
"temporal_patch_size": 2
},
"vision_end_token_id": 151653,
"vision_start_token_id": 151652
}

the script:
```

import base64
from io import BytesIO
import torch
from datasets import load_dataset
from transformers import Qwen3VLMoeForConditionalGeneration, AutoProcessor
from llmcompressor import oneshot
from llmcompressor.modifiers.awq import AWQModifier
from llmcompressor.modeling import replace_modules_for_calibration
from llmcompressor.utils import dispatch_for_generation

MODEL_ID = "Qwen/Qwen3-VL-30B-A3B-Instruct"
OUTPUT_DIR = MODEL_ID.split("/")[-1] + "-AWQ-W8A16-mse-sym-false"

model = Qwen3VLMoeForConditionalGeneration.from_pretrained(
MODEL_ID,
torch_dtype=torch.bfloat16,
device_map=None,
trust_remote_code=True,
)
processor = AutoProcessor.from_pretrained(MODEL_ID, trust_remote_code=True)

model = replace_modules_for_calibration(model)

DATASET_ID = "lmms-lab/flickr30k"
NUM_CALIBRATION_SAMPLES = 256
DATASET_SPLIT = f"test[:{NUM_CALIBRATION_SAMPLES}]"
MAX_SEQUENCE_LENGTH = 1024

ds = load_dataset(DATASET_ID, split=DATASET_SPLIT)
ds = ds.shuffle(seed=42)

def preprocess_and_tokenize(example):
buffered = BytesIO()
example["image"].save(buffered, format="PNG")
encoded_image = base64.b64encode(buffered.getvalue())
base64_image = f"data:image;base64,{encoded_image.decode('utf-8')}"
messages = [{
"role": "user",
"content": [
{"type": "image", "image": base64_image},
{"type": "text", "text": "What does the image show?"}
]
}]
text = processor.apply_chat_template(
messages,
tokenize=False,
add_generation_prompt=True
)
inputs = processor(
text=[text],
images=[example["image"]],
padding=False,
max_length=MAX_SEQUENCE_LENGTH,
truncation=True,
)
return inputs

ds = ds.map(preprocess_and_tokenize, remove_columns=ds.column_names)

def data_collator(batch):
assert len(batch) == 1
return {key: torch.tensor(value) for key, value in batch[0].items()}

recipe = AWQModifier(
ignore=["re:.*lm_head", "re:.visual.", "re:.*mlp.gate$"],
duo_scaling=True,
config_groups={
"group_0": {
"targets": ["Linear"],
"input_activations": None,
"output_activations": None,
"weights": {
"actorder": None,
"block_structure": None,
"dynamic": False,
"group_size": 32,
"num_bits": 8,
"observer": "mse",
"observer_kwargs": {},
"strategy": "group",
"symmetric": True,
"type": "int"
}
}
}
)

oneshot(
model=model,
processor=processor,
recipe=recipe,
dataset=ds,
max_seq_length=MAX_SEQUENCE_LENGTH,
num_calibration_samples=NUM_CALIBRATION_SAMPLES,
data_collator=data_collator,
pipeline="sequential",
)

model.save_pretrained(OUTPUT_DIR, save_compressed=True)
processor.save_pretrained(OUTPUT_DIR)
```

The error:

vllm1-1 | (Worker_TP3 pid=234) INFO 10-17 16:33:43 [compressed_tensors_moe.py:146] Using CompressedTensorsWNA16MoEMethod
Loading safetensors checkpoint shards: 0% 0/8 [00:00<?, ?it/s](Worker_TP0 pid=231) ERROR 10-17 16:33:43 [multiproc_executor.py:623] WorkerProc failed to start.
vllm1-1 | (Worker_TP0 pid=231) ERROR 10-17 16:33:43 [multiproc_executor.py:623] Traceback (most recent call last):
vllm1-1 | (Worker_TP0 pid=231) ERROR 10-17 16:33:43 [multiproc_executor.py:623] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/executor/multiproc_executor.py", line 597, in worker_main
vllm1-1 | (Worker_TP0 pid=231) ERROR 10-17 16:33:43 [multiproc_executor.py:623] worker = WorkerProc(*args, **kwargs)
vllm1-1 | (Worker_TP0 pid=231) ERROR 10-17 16:33:43 [multiproc_executor.py:623] ^^^^^^^^^^^^^^^^^^^^^^^^^^^
vllm1-1 | (Worker_TP0 pid=231) ERROR 10-17 16:33:43 [multiproc_executor.py:623] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/executor/multiproc_executor.py", line 456, in init
vllm1-1 | (Worker_TP0 pid=231) ERROR 10-17 16:33:43 [multiproc_executor.py:623] self.worker.load_model()
vllm1-1 | (Worker_TP0 pid=231) ERROR 10-17 16:33:43 [multiproc_executor.py:623] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/worker/gpu_worker.py", line 229, in load_model
vllm1-1 | (Worker_TP0 pid=231) ERROR 10-17 16:33:43 [multiproc_executor.py:623] self.model_runner.load_model(eep_scale_up=eep_scale_up)
vllm1-1 | (Worker_TP0 pid=231) ERROR 10-17 16:33:43 [multiproc_executor.py:623] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/worker/gpu_model_runner.py", line 2880, in load_model
vllm1-1 | (Worker_TP0 pid=231) ERROR 10-17 16:33:43 [multiproc_executor.py:623] self.model = model_loader.load_model(
vllm1-1 | (Worker_TP0 pid=231) ERROR 10-17 16:33:43 [multiproc_executor.py:623] ^^^^^^^^^^^^^^^^^^^^^^^^
vllm1-1 | (Worker_TP0 pid=231) ERROR 10-17 16:33:43 [multiproc_executor.py:623] File "/usr/local/lib/python3.12/dist-packages/vllm/model_executor/model_loader/base_loader.py", line 55, in load_model
vllm1-1 | (Worker_TP0 pid=231) ERROR 10-17 16:33:43 [multiproc_executor.py:623] self.load_weights(model, model_config)
vllm1-1 | (Worker_TP0 pid=231) ERROR 10-17 16:33:43 [multiproc_executor.py:623] File "/usr/local/lib/python3.12/dist-packages/vllm/model_executor/model_loader/default_loader.py", line 300, in load_weights
vllm1-1 | (Worker_TP0 pid=231) ERROR 10-17 16:33:43 [multiproc_executor.py:623] loaded_weights = model.load_weights(
vllm1-1 | (Worker_TP0 pid=231) ERROR 10-17 16:33:43 [multiproc_executor.py:623] ^^^^^^^^^^^^^^^^^^^
vllm1-1 | (Worker_TP0 pid=231) ERROR 10-17 16:33:43 [multiproc_executor.py:623] File "/usr/local/lib/python3.12/dist-packages/vllm/model_executor/models/qwen3_vl.py", line 1771, in load_weights
vllm1-1 | (Worker_TP0 pid=231) ERROR 10-17 16:33:43 [multiproc_executor.py:623] return loader.load_weights(weights, mapper=self.hf_to_vllm_mapper)
vllm1-1 | (Worker_TP0 pid=231) ERROR 10-17 16:33:43 [multiproc_executor.py:623] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
vllm1-1 | (Worker_TP0 pid=231) ERROR 10-17 16:33:43 [multiproc_executor.py:623] File "/usr/local/lib/python3.12/dist-packages/vllm/model_executor/models/utils.py", line 318, in load_weights
vllm1-1 | (Worker_TP0 pid=231) ERROR 10-17 16:33:43 [multiproc_executor.py:623] autoloaded_weights = set(self._load_module("", self.module, weights))
vllm1-1 | (Worker_TP0 pid=231) ERROR 10-17 16:33:43 [multiproc_executor.py:623] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
vllm1-1 | (Worker_TP0 pid=231) ERROR 10-17 16:33:43 [multiproc_executor.py:623] File "/usr/local/lib/python3.12/dist-packages/vllm/model_executor/models/utils.py", line 272, in _load_module
vllm1-1 | (Worker_TP0 pid=231) ERROR 10-17 16:33:43 [multiproc_executor.py:623] yield from self._load_module(
vllm1-1 | (Worker_TP0 pid=231) ERROR 10-17 16:33:43 [multiproc_executor.py:623] File "/usr/local/lib/python3.12/dist-packages/vllm/model_executor/models/utils.py", line 245, in _load_module
vllm1-1 | (Worker_TP0 pid=231) ERROR 10-17 16:33:43 [multiproc_executor.py:623] loaded_params = module_load_weights(weights)
vllm1-1 | (Worker_TP0 pid=231) ERROR 10-17 16:33:43 [multiproc_executor.py:623] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
vllm1-1 | (Worker_TP0 pid=231) ERROR 10-17 16:33:43 [multiproc_executor.py:623] File "/usr/local/lib/python3.12/dist-packages/vllm/model_executor/models/qwen3_moe.py", line 755, in load_weights
vllm1-1 | (Worker_TP0 pid=231) ERROR 10-17 16:33:43 [multiproc_executor.py:623] return loader.load_weights(weights)
vllm1-1 | (Worker_TP0 pid=231) ERROR 10-17 16:33:43 [multiproc_executor.py:623] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
vllm1-1 | (Worker_TP0 pid=231) ERROR 10-17 16:33:43 [multiproc_executor.py:623] File "/usr/local/lib/python3.12/dist-packages/vllm/model_executor/models/utils.py", line 318, in load_weights
vllm1-1 | (Worker_TP0 pid=231) ERROR 10-17 16:33:43 [multiproc_executor.py:623] autoloaded_weights = set(self._load_module("", self.module, weights))
vllm1-1 | (Worker_TP0 pid=231) ERROR 10-17 16:33:43 [multiproc_executor.py:623] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
vllm1-1 | (Worker_TP0 pid=231) ERROR 10-17 16:33:43 [multiproc_executor.py:623] File "/usr/local/lib/python3.12/dist-packages/vllm/model_executor/models/utils.py", line 272, in _load_module
vllm1-1 | (Worker_TP0 pid=231) ERROR 10-17 16:33:43 [multiproc_executor.py:623] yield from self._load_module(
vllm1-1 | (Worker_TP0 pid=231) ERROR 10-17 16:33:43 [multiproc_executor.py:623] File "/usr/local/lib/python3.12/dist-packages/vllm/model_executor/models/utils.py", line 245, in _load_module
vllm1-1 | (Worker_TP0 pid=231) ERROR 10-17 16:33:43 [multiproc_executor.py:623] loaded_params = module_load_weights(weights)
vllm1-1 | (Worker_TP0 pid=231) ERROR 10-17 16:33:43 [multiproc_executor.py:623] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
vllm1-1 | (Worker_TP0 pid=231) ERROR 10-17 16:33:43 [multiproc_executor.py:623] File "/usr/local/lib/python3.12/dist-packages/vllm/model_executor/models/qwen3_vl_moe.py", line 272, in load_weights
vllm1-1 | (Worker_TP0 pid=231) ERROR 10-17 16:33:43 [multiproc_executor.py:623] param = params_dict[name_mapped]
vllm1-1 | (Worker_TP0 pid=231) ERROR 10-17 16:33:43 [multiproc_executor.py:623] ~~~~~~~~~~~^^^^^^^^^^^^^
vllm1-1 | (Worker_TP0 pid=231) ERROR 10-17 16:33:43 [multiproc_executor.py:623] KeyError: 'layers.19.mlp.experts.w2_weight_zero_point'
Loading safetensors checkpoint shards: 0% 0/8 [00:00<?, ?it/s]
vllm1-1 | (Worker_TP2 pid=233) INFO 10-17 16:33:43 [multiproc_executor.py:584] Parent process exited, terminating worker
vllm1-1 | (Worker_TP0 pid=231) INFO 10-17 16:33:43 [multiproc_executor.py:584] Parent process exited, terminating worker
vllm1-1 | (Worker_TP1 pid=232) INFO 10-17 16:33:43 [multiproc_executor.py:584] Parent process exited, terminating worker
vllm1-1 | (Worker_TP3 pid=234) INFO 10-17 16:33:43 [multiproc_executor.py:584] Parent process exited, terminating worker
vllm1-1 | [rank0]:[W1017 16:33:43.229670474 ProcessGroupNCCL.cpp:1538] Warning: WARNING: destroy_process_group() was not called before program exit, which can leak resources. For more info, please see https://pytorch.org/docs/stable/distributed.html#shutdown (function operator())
vllm1-1 | (EngineCore_DP0 pid=159) ERROR 10-17 16:33:44 [core.py:792] EngineCore failed to start.
vllm1-1 | (EngineCore_DP0 pid=159) ERROR 10-17 16:33:44 [core.py:792] Traceback (most recent call last):
vllm1-1 | (EngineCore_DP0 pid=159) ERROR 10-17 16:33:44 [core.py:792] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/engine/core.py", line 783, in run_engine_core
vllm1-1 | (EngineCore_DP0 pid=159) ERROR 10-17 16:33:44 [core.py:792] engine_core = EngineCoreProc(*args, **kwargs)
vllm1-1 | (EngineCore_DP0 pid=159) ERROR 10-17 16:33:44 [core.py:792] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
vllm1-1 | (EngineCore_DP0 pid=159) ERROR 10-17 16:33:44 [core.py:792] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/engine/core.py", line 555, in __init__
vllm1-1 | (EngineCore_DP0 pid=159) ERROR 10-17 16:33:44 [core.py:792] super().__init__(
vllm1-1 | (EngineCore_DP0 pid=159) ERROR 10-17 16:33:44 [core.py:792] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/engine/core.py", line 105, in __init__
vllm1-1 | (EngineCore_DP0 pid=159) ERROR 10-17 16:33:44 [core.py:792] self.model_executor = executor_class(vllm_config)
vllm1-1 | (EngineCore_DP0 pid=159) ERROR 10-17 16:33:44 [core.py:792] ^^^^^^^^^^^^^^^^^^^^^^^^^^^
vllm1-1 | (EngineCore_DP0 pid=159) ERROR 10-17 16:33:44 [core.py:792] File "/usr/local/lib/python3.12/dist-packages/vllm/executor/executor_base.py", line 54, in __init__
vllm1-1 | (EngineCore_DP0 pid=159) ERROR 10-17 16:33:44 [core.py:792] self._init_executor()
vllm1-1 | (EngineCore_DP0 pid=159) ERROR 10-17 16:33:44 [core.py:792] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/executor/multiproc_executor.py", line 113, in _init_executor
vllm1-1 | (EngineCore_DP0 pid=159) ERROR 10-17 16:33:44 [core.py:792] self.workers = WorkerProc.wait_for_ready(unready_workers)
vllm1-1 | (EngineCore_DP0 pid=159) ERROR 10-17 16:33:44 [core.py:792] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
vllm1-1 | (EngineCore_DP0 pid=159) ERROR 10-17 16:33:44 [core.py:792] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/executor/multiproc_executor.py", line 535, in wait_for_ready
vllm1-1 | (EngineCore_DP0 pid=159) ERROR 10-17 16:33:44 [core.py:792] raise e from None
vllm1-1 | (EngineCore_DP0 pid=159) ERROR 10-17 16:33:44 [core.py:792] Exception: WorkerProc initialization failed due to an exception in a background process. See stack trace for root cause.
vllm1-1 | (EngineCore_DP0 pid=159) Process EngineCore_DP0:
vllm1-1 | (EngineCore_DP0 pid=159) Traceback (most recent call last):
vllm1-1 | (EngineCore_DP0 pid=159) File "/usr/lib/python3.12/multiprocessing/process.py", line 314, in _bootstrap
vllm1-1 | (EngineCore_DP0 pid=159) self.run()
vllm1-1 | (EngineCore_DP0 pid=159) File "/usr/lib/python3.12/multiprocessing/process.py", line 108, in run
vllm1-1 | (EngineCore_DP0 pid=159) self._target(*self._args, **self._kwargs)
vllm1-1 | (EngineCore_DP0 pid=159) File "/usr/local/lib/python3.12/dist-packages/vllm/v1/engine/core.py", line 796, in run_engine_core
vllm1-1 | (EngineCore_DP0 pid=159) raise e
vllm1-1 | (EngineCore_DP0 pid=159) File "/usr/local/lib/python3.12/dist-packages/vllm/v1/engine/core.py", line 783, in run_engine_core
vllm1-1 | (EngineCore_DP0 pid=159) engine_core = EngineCoreProc(*args, **kwargs)
vllm1-1 | (EngineCore_DP0 pid=159) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
vllm1-1 | (EngineCore_DP0 pid=159) File "/usr/local/lib/python3.12/dist-packages/vllm/v1/engine/core.py", line 555, in __init__
vllm1-1 | (EngineCore_DP0 pid=159) super().__init__(
vllm1-1 | (EngineCore_DP0 pid=159) File "/usr/local/lib/python3.12/dist-packages/vllm/v1/engine/core.py", line 105, in __init__
vllm1-1 | (EngineCore_DP0 pid=159) self.model_executor = executor_class(vllm_config)
vllm1-1 | (EngineCore_DP0 pid=159) ^^^^^^^^^^^^^^^^^^^^^^^^^^^
vllm1-1 | (EngineCore_DP0 pid=159) File "/usr/local/lib/python3.12/dist-packages/vllm/executor/executor_base.py", line 54, in __init__
vllm1-1 | (EngineCore_DP0 pid=159) self._init_executor()
vllm1-1 | (EngineCore_DP0 pid=159) File "/usr/local/lib/python3.12/dist-packages/vllm/v1/executor/multiproc_executor.py", line 113, in _init_executor
vllm1-1 | (EngineCore_DP0 pid=159) self.workers = WorkerProc.wait_for_ready(unready_workers)
vllm1-1 | (EngineCore_DP0 pid=159) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
vllm1-1 | (EngineCore_DP0 pid=159) File "/usr/local/lib/python3.12/dist-packages/vllm/v1/executor/multiproc_executor.py", line 535, in wait_for_ready
vllm1-1 | (EngineCore_DP0 pid=159) raise e from None
vllm1-1 | (EngineCore_DP0 pid=159) Exception: WorkerProc initialization failed due to an exception in a background process. See stack trace for root cause.
vllm1-1 | (APIServer pid=1) Traceback (most recent call last):
vllm1-1 | (APIServer pid=1) File "/usr/local/bin/vllm", line 7, in
vllm1-1 | (APIServer pid=1) sys.exit(main())
vllm1-1 | (APIServer pid=1) ^^^^^^
vllm1-1 | (APIServer pid=1) File "/usr/local/lib/python3.12/dist-packages/vllm/entrypoints/cli/main.py", line 73, in main
vllm1-1 | (APIServer pid=1) args.dispatch_function(args)
vllm1-1 | (APIServer pid=1) File "/usr/local/lib/python3.12/dist-packages/vllm/entrypoints/cli/serve.py", line 62, in cmd
vllm1-1 | (APIServer pid=1) uvloop.run(run_server(args))
vllm1-1 | (APIServer pid=1) File "/usr/local/lib/python3.12/dist-packages/uvloop/init.py", line 109, in run
vllm1-1 | (APIServer pid=1) return __asyncio.run(
vllm1-1 | (APIServer pid=1) ^^^^^^^^^^^^^^
vllm1-1 | (APIServer pid=1) File "/usr/lib/python3.12/asyncio/runners.py", line 195, in run
vllm1-1 | (APIServer pid=1) return runner.run(main)
vllm1-1 | (APIServer pid=1) ^^^^^^^^^^^^^^^^
vllm1-1 | (APIServer pid=1) File "/usr/lib/python3.12/asyncio/runners.py", line 118, in run
vllm1-1 | (APIServer pid=1) return self._loop.run_until_complete(task)
vllm1-1 | (APIServer pid=1) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
vllm1-1 | (APIServer pid=1) File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
vllm1-1 | (APIServer pid=1) File "/usr/local/lib/python3.12/dist-packages/uvloop/init.py", line 61, in wrapper
vllm1-1 | (APIServer pid=1) return await main
vllm1-1 | (APIServer pid=1) ^^^^^^^^^^
vllm1-1 | (APIServer pid=1) File "/usr/local/lib/python3.12/dist-packages/vllm/entrypoints/openai/api_server.py", line 1917, in run_server
vllm1-1 | (APIServer pid=1) await run_server_worker(listen_address, sock, args, **uvicorn_kwargs)
vllm1-1 | (APIServer pid=1) File "/usr/local/lib/python3.12/dist-packages/vllm/entrypoints/openai/api_server.py", line 1933, in run_server_worker
vllm1-1 | (APIServer pid=1) async with build_async_engine_client(
vllm1-1 | (APIServer pid=1) ^^^^^^^^^^^^^^^^^^^^^^^^^^
vllm1-1 | (APIServer pid=1) File "/usr/lib/python3.12/contextlib.py", line 210, in aenter
vllm1-1 | (APIServer pid=1) return await anext(self.gen)
vllm1-1 | (APIServer pid=1) ^^^^^^^^^^^^^^^^^^^^^
vllm1-1 | (APIServer pid=1) File "/usr/local/lib/python3.12/dist-packages/vllm/entrypoints/openai/api_server.py", line 191, in build_async_engine_client
vllm1-1 | (APIServer pid=1) async with build_async_engine_client_from_engine_args(
vllm1-1 | (APIServer pid=1) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
vllm1-1 | (APIServer pid=1) File "/usr/lib/python3.12/contextlib.py", line 210, in aenter
vllm1-1 | (APIServer pid=1) return await anext(self.gen)
vllm1-1 | (APIServer pid=1) ^^^^^^^^^^^^^^^^^^^^^
vllm1-1 | (APIServer pid=1) File "/usr/local/lib/python3.12/dist-packages/vllm/entrypoints/openai/api_server.py", line 238, in build_async_engine_client_from_engine_args
vllm1-1 | (APIServer pid=1) async_llm = AsyncLLM.from_vllm_config(
vllm1-1 | (APIServer pid=1) ^^^^^^^^^^^^^^^^^^^^^^^^^^
vllm1-1 | (APIServer pid=1) File "/usr/local/lib/python3.12/dist-packages/vllm/utils/init.py", line 1336, in inner
vllm1-1 | (APIServer pid=1) return fn(*args, **kwargs)
vllm1-1 | (APIServer pid=1) ^^^^^^^^^^^^^^^^^^^
vllm1-1 | (APIServer pid=1) File "/usr/local/lib/python3.12/dist-packages/vllm/v1/engine/async_llm.py", line 208, in from_vllm_config
vllm1-1 | (APIServer pid=1) return cls(
vllm1-1 | (APIServer pid=1) ^^^^
vllm1-1 | (APIServer pid=1) File "/usr/local/lib/python3.12/dist-packages/vllm/v1/engine/async_llm.py", line 130, in init
vllm1-1 | (APIServer pid=1) self.engine_core = EngineCoreClient.make_async_mp_client(
vllm1-1 | (APIServer pid=1) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
vllm1-1 | (APIServer pid=1) File "/usr/local/lib/python3.12/dist-packages/vllm/v1/engine/core_client.py", line 121, in make_async_mp_client
vllm1-1 | (APIServer pid=1) return AsyncMPClient(*client_args)
vllm1-1 | (APIServer pid=1) ^^^^^^^^^^^^^^^^^^^^^^^^^^^
vllm1-1 | (APIServer pid=1) File "/usr/local/lib/python3.12/dist-packages/vllm/v1/engine/core_client.py", line 807, in init
vllm1-1 | (APIServer pid=1) super().init(
vllm1-1 | (APIServer pid=1) File "/usr/local/lib/python3.12/dist-packages/vllm/v1/engine/core_client.py", line 468, in init
vllm1-1 | (APIServer pid=1) with launch_core_engines(vllm_config, executor_class, log_stats) as (
vllm1-1 | (APIServer pid=1) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
vllm1-1 | (APIServer pid=1) File "/usr/lib/python3.12/contextlib.py", line 144, in exit
vllm1-1 | (APIServer pid=1) next(self.gen)
vllm1-1 | (APIServer pid=1) File "/usr/local/lib/python3.12/dist-packages/vllm/v1/engine/utils.py", line 816, in launch_core_engines
vllm1-1 | (APIServer pid=1) wait_for_engine_startup(
vllm1-1 | (APIServer pid=1) File "/usr/local/lib/python3.12/dist-packages/vllm/v1/engine/utils.py", line 873, in wait_for_engine_startup
vllm1-1 | (APIServer pid=1) raise RuntimeError(
vllm1-1 | (APIServer pid=1) RuntimeError: Engine core initialization failed. See root cause above. Failed core proc(s): {}



### dsikka · 2025-10-17

@JartX Can you post your model to the hf hub?
The output from vLLM is complaining about a zerop-point however, it seems like your model is symmetric.
I can take a closer look but this may be a vllm issue.

### dsikka · 2025-10-17

Hi @JartX 

The Qwen3 VL 30B is an MoE with a slightly strange structure. 
In order for you to properly run quantization on it (and then run the model in vLLM) you'll need to replace some of the expert layers as they are currently 3D.

<img width="738" height="84" alt="Image" src="https://github.com/user-attachments/assets/0751b222-4151-41d4-9adf-d4165dac3220" />

Can you try the following script, updating it to use AWQ? I would use llmcompressor main for this.
https://github.com/vllm-project/llm-compressor/blob/main/examples/quantization_w4a4_fp4/qwen3_vl_moe_w4a4_fp4.py

### JartX · 2025-10-17

@dsikka 
You're going to laugh, but I'm just switching from sequential to datafree haha, after reviewing the comment that cpatonn posted yesterday.
If it doesn't work, I'll still upload it and publish the full script, and when it works, thank you very much for being there.

### dsikka · 2025-10-17

@JartX ok datafree will only work with like fp8 and you’ll still need the replacement code like in the example I sent.


But give it a shot! Ping us on the vllm slack if that’s faster 

### JartX · 2025-10-17

@dsikka
```
import torch
from datasets import load_dataset
from transformers import AutoProcessor, Qwen3VLMoeForConditionalGeneration

from llmcompressor import oneshot
from llmcompressor.modeling import replace_modules_for_calibration
from llmcompressor.modifiers.awq import AWQModifier
from llmcompressor.utils import dispatch_for_generation

# NOTE: Requires a minimum of transformers 4.57.0

MODEL_ID = "Qwen/Qwen3-VL-30B-A3B-Instruct"

# Load model.
model = Qwen3VLMoeForConditionalGeneration.from_pretrained(
    MODEL_ID, 
    torch_dtype=torch.bfloat16,
    device_map=None,
    trust_remote_code=True
)
processor = AutoProcessor.from_pretrained(MODEL_ID, trust_remote_code=True)
model = replace_modules_for_calibration(model)

DATASET_ID = "neuralmagic/calibration"
NUM_CALIBRATION_SAMPLES = 256
MAX_SEQUENCE_LENGTH = 8192

ds = load_dataset(DATASET_ID, name="LLM", split=f"train[:{NUM_CALIBRATION_SAMPLES}]")
ds = ds.shuffle(seed=42)


def preprocess_function(example):
    messages = []
    for message in example["messages"]:
        messages.append(
            {
                "role": message["role"],
                "content": [{"type": "text", "text": message["content"]}],
            }
        )

    return processor.apply_chat_template(
        messages,
        return_tensors="pt",
        padding=False,
        truncation=True,
        max_length=MAX_SEQUENCE_LENGTH,
        tokenize=True,
        add_special_tokens=False,
        return_dict=True,
        add_generation_prompt=False,
    )


ds = ds.map(preprocess_function, batched=False, remove_columns=ds.column_names)


def data_collator(batch):
    assert len(batch) == 1
    return {
        key: (
            torch.tensor(value)
            if key != "pixel_values"
            else torch.tensor(value, dtype=torch.bfloat16).squeeze(0)
        )
        for key, value in batch[0].items()
    }


# Configure AWQ quantization with smoothing and balancing
recipe = AWQModifier(
    ignore=[
        're:.*embed_tokens', 
        're:.*input_layernorm$', 
        're:.*mlp[.]gate$', 
        're:.*post_attention_layernorm$', 
        're:.*norm$', 
        're:model[.]visual.*',
        're:visual.*',
        'lm_head'
    ],
    mappings=[
        {
            "smooth_layer": "re:.*input_layernorm$",
            "balance_layers": ['re:.*q_proj$', 're:.*k_proj$', 're:.*v_proj$']
        },
        {
            "smooth_layer": "re:.*v_proj$",
            "balance_layers": ['re:.*o_proj$']
        },
        {
            "smooth_layer": "re:.*post_attention_layernorm$",
            "balance_layers": ['re:.*gate_proj$', 're:.*up_proj$']
        },
        {
            "smooth_layer": "re:.*up_proj$",
            "balance_layers": ['re:.*down_proj$']
        }
    ],
    duo_scaling=True,
    config_groups={
        "group_0": {
            "targets": ["Linear"],
            "weights": {
                "num_bits": 8,
                "type": "int",
                "symmetric": True,
                "group_size": 32,
                "strategy": "group",
                "block_structure": None,
                "dynamic": False,
                "actorder": None,
                "observer": "mse",
                "observer_kwargs": {}
            },
            "input_activations": None,
            "output_activations": None,
            "format": None
        }
    }
)

# Apply AWQ quantization.
oneshot(
    model=model,
    processor=processor,
    recipe=recipe,
    dataset=ds,
    max_seq_length=MAX_SEQUENCE_LENGTH,
    num_calibration_samples=NUM_CALIBRATION_SAMPLES,
    data_collator=data_collator,
    pipeline="datafree",
)

print("========== SAMPLE GENERATION ==============")
dispatch_for_generation(model)
input_ids = processor(text="Hello my name is", return_tensors="pt").input_ids.to("cuda")
output = model.generate(input_ids, max_new_tokens=20)
print(processor.decode(output[0]))
print("==========================================")

# Save to disk in compressed-tensors format.
SAVE_DIR = MODEL_ID.rstrip("/").split("/")[-1] + "-AWQ-W8A16-mse-sym"
model.save_pretrained(SAVE_DIR, save_compressed=True)
processor.save_pretrained(SAVE_DIR)
```

**Works!**

The point:
pipeline="datafree",


Preparation:

git clone https://github.com/vllm-project/llm-compressor.git

cd llm-compressor

pip install -e .

pip install transformers==4.57.0
export TOKENIZERS_PARALLELISM=false

cd .. 

nano quant.py (with the code of script)
python quant.py


### JartX · 2025-10-17

@dsikka @brian-dellabetta

Would you be so kind as to let me do the pr with the example code?

The model:

https://huggingface.co/jart25/Qwen3-VL-30B-A3B-Instruct-AWQ-8bit/tree/main

### dsikka · 2025-10-17

Hi @JartX - awq without data will perform very poorly. We can take a look into your example but you shouldn’t be using the data free pipeline.

### JartX · 2025-10-17

@dsikka okays! What I don't understand is why it loads with datafree and not without it. Could you please try to explain this to me? I might be overdoing it, but... how do you internally identify whether it's awq or gptq if there's no reference to it in the config?

### dsikka · 2025-10-17

Yeah we’ll need to investigate. We’ll get back to you soon 

### JartX · 2025-10-18

> Yeah we’ll need to investigate. We’ll get back to you soon

@dsikka 

You're right, can quant with sequential and work

Script that works with seq

```
import torch
from datasets import load_dataset
from transformers import AutoProcessor, Qwen3VLMoeForConditionalGeneration

from llmcompressor import oneshot
from llmcompressor.modeling import replace_modules_for_calibration
from llmcompressor.modifiers.awq import AWQModifier
from llmcompressor.utils import dispatch_for_generation

# NOTE: Requires a minimum of transformers 4.57.0

MODEL_ID = "Qwen/Qwen3-VL-30B-A3B-Instruct"

# Load model.
model = Qwen3VLMoeForConditionalGeneration.from_pretrained(
    MODEL_ID, 
    torch_dtype=torch.bfloat16,
    device_map=None,
    trust_remote_code=True
)
processor = AutoProcessor.from_pretrained(MODEL_ID, trust_remote_code=True)
model = replace_modules_for_calibration(model)

DATASET_ID = "neuralmagic/calibration"
NUM_CALIBRATION_SAMPLES = 256
MAX_SEQUENCE_LENGTH = 8192

ds = load_dataset(DATASET_ID, name="LLM", split=f"train[:{NUM_CALIBRATION_SAMPLES}]")
ds = ds.shuffle(seed=42)


def preprocess_function(example):
    messages = []
    for message in example["messages"]:
        messages.append(
            {
                "role": message["role"],
                "content": [{"type": "text", "text": message["content"]}],
            }
        )

    return processor.apply_chat_template(
        messages,
        return_tensors="pt",
        padding=False,
        truncation=True,
        max_length=MAX_SEQUENCE_LENGTH,
        tokenize=True,
        add_special_tokens=False,
        return_dict=True,
        add_generation_prompt=False,
    )


ds = ds.map(preprocess_function, batched=False, remove_columns=ds.column_names)


def data_collator(batch):
    assert len(batch) == 1
    return {
        key: (
            torch.tensor(value)
            if key != "pixel_values"
            else torch.tensor(value, dtype=torch.bfloat16).squeeze(0)
        )
        for key, value in batch[0].items()
    }


# Configure AWQ quantization with smoothing and balancing
recipe = AWQModifier(
    ignore=[
        're:.*embed_tokens', 
        're:.*input_layernorm$', 
        're:.*mlp[.]gate$', 
        're:.*post_attention_layernorm$', 
        're:.*norm$', 
        're:model[.]visual.*',
        're:visual.*',
        'lm_head'
    ],
    mappings=[
        {
            "smooth_layer": "re:.*input_layernorm$",
            "balance_layers": ['re:.*q_proj$', 're:.*k_proj$', 're:.*v_proj$']
        },
        {
            "smooth_layer": "re:.*v_proj$",
            "balance_layers": ['re:.*o_proj$']
        },
        {
            "smooth_layer": "re:.*post_attention_layernorm$",
            "balance_layers": ['re:.*gate_proj$', 're:.*up_proj$']
        },
        {
            "smooth_layer": "re:.*up_proj$",
            "balance_layers": ['re:.*down_proj$']
        }
    ],
    duo_scaling=True,
    config_groups={
        "group_0": {
            "targets": ["Linear"],
            "weights": {
                "num_bits": 8,
                "type": "int",
                "symmetric": True,
                "group_size": 32,
                "strategy": "group",
                "block_structure": None,
                "dynamic": False,
                "actorder": None,
                "observer": "mse",
                "observer_kwargs": {}
            },
            "input_activations": None,
            "output_activations": None,
            "format": None
        }
    }
)

# Apply AWQ quantization.
oneshot(
    model=model,
    processor=processor,
    recipe=recipe,
    dataset=ds,
    max_seq_length=MAX_SEQUENCE_LENGTH,
    num_calibration_samples=NUM_CALIBRATION_SAMPLES,
    data_collator=data_collator,

)

print("========== SAMPLE GENERATION ==============")
dispatch_for_generation(model)
input_ids = processor(text="Hello my name is", return_tensors="pt").input_ids.to("cuda")
output = model.generate(input_ids, max_new_tokens=20)
print(processor.decode(output[0]))
print("==========================================")

# Save to disk in compressed-tensors format.
SAVE_DIR = MODEL_ID.rstrip("/").split("/")[-1] + "-AWQ-W8A16-mse-seq"
model.save_pretrained(SAVE_DIR, save_compressed=True)
processor.save_pretrained(SAVE_DIR)
```

Script that not work

```
import base64
from io import BytesIO
import torch
from datasets import load_dataset
from transformers import Qwen3VLMoeForConditionalGeneration, AutoProcessor
from llmcompressor import oneshot
from llmcompressor.modifiers.awq import AWQModifier
from llmcompressor.modeling import replace_modules_for_calibration

MODEL_ID = "Qwen/Qwen3-VL-30B-A3B-Instruct"
OUTPUT_DIR = MODEL_ID.split("/")[-1] + "-AWQ-W8A16-mse-sym-true"

model = Qwen3VLMoeForConditionalGeneration.from_pretrained(
    MODEL_ID,
    torch_dtype=torch.bfloat16,
    device_map=None,
    trust_remote_code=True,
)
processor = AutoProcessor.from_pretrained(MODEL_ID, trust_remote_code=True)

model = replace_modules_for_calibration(model)

DATASET_ID = "lmms-lab/flickr30k"
NUM_CALIBRATION_SAMPLES = 256
DATASET_SPLIT = f"test[:{NUM_CALIBRATION_SAMPLES}]"
MAX_SEQUENCE_LENGTH = 1024

ds = load_dataset(DATASET_ID, split=DATASET_SPLIT)
ds = ds.shuffle(seed=42)

def preprocess_and_tokenize(example):
    buffered = BytesIO()
    example["image"].save(buffered, format="PNG")
    encoded_image = base64.b64encode(buffered.getvalue())
    base64_image = f"data:image;base64,{encoded_image.decode('utf-8')}"
    messages = [{
        "role": "user",
        "content": [
            {"type": "image", "image": base64_image},
            {"type": "text", "text": "What does the image show?"}
        ]
    }]
    text = processor.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True
    )
    inputs = processor(
        text=[text],
        images=[example["image"]],
        padding=False,
        max_length=MAX_SEQUENCE_LENGTH,
        truncation=True,
    )
    return inputs

ds = ds.map(preprocess_and_tokenize, remove_columns=ds.column_names)

def data_collator(batch):
    assert len(batch) == 1
    return {key: torch.tensor(value) for key, value in batch[0].items()}

recipe = AWQModifier(
    ignore=[
        're:.*embed_tokens',
        're:.*input_layernorm$',
        're:.*mlp[.]gate$',
        're:.*post_attention_layernorm$',
        're:.*norm$',
        're:model[.]visual.*',
        'lm_head'
    ],
    duo_scaling=True,
    mappings=[
        {
            "smooth_layer": "re:.*input_layernorm$",
            "balance_layers": ['re:.*q_proj$', 're:.*k_proj$', 're:.*v_proj$']
        },
        {
            "smooth_layer": "re:.*v_proj$",
            "balance_layers": ['re:.*o_proj$']
        },
        {
            "smooth_layer": "re:.*post_attention_layernorm$",
            "balance_layers": ['re:.*gate_proj$', 're:.*up_proj$']
        },
        {
            "smooth_layer": "re:.*up_proj$",
            "balance_layers": ['re:.*down_proj$']
        }
    ],
    config_groups={
        "group_0": {
            "targets": ["Linear"],
            "input_activations": None,
            "output_activations": None,
            "weights": {
                "actorder": None,
                "block_structure": None,
                "dynamic": False,
                "group_size": 32,
                "num_bits": 8,
                "observer": "mse",
                "observer_kwargs": {},
                "strategy": "group",
                "symmetric": True,
                "type": "int"
            },
            "format": None
        }
    }
)

oneshot(
    model=model,
    processor=processor,
    recipe=recipe,
    dataset=ds,
    max_seq_length=MAX_SEQUENCE_LENGTH,
    num_calibration_samples=NUM_CALIBRATION_SAMPLES,
    data_collator=data_collator,
)

model.save_pretrained(OUTPUT_DIR, save_compressed=True)
processor.save_pretrained(OUTPUT_DIR)

print(f"Modelo cuantizado guardado en: {OUTPUT_DIR}")
```


### dsikka · 2025-10-18

HI @JartX - glad you got it to work. Is the only difference the dataset you're using?

I just tried the example with the flickr30k  dataset / processing you were trying and I now also get the same failure. The failure specifically is coming from transformers so there may be a mismatch in the flickr30k processing and what is needed by the Qwen3 VL Model. @kylesayrs is there anything that stands out to you as being incorrect in the data processing?

@JartX  I would encourage you to put up an AWQ example that worked for you to share it with the rest of the community! The `neuralmagic/calibration` is a standard dataset we often use to calibrate our models so I am glad that was able to work.


### JartX · 2025-10-18

@dsikka complete model and code here:
https://huggingface.co/jart25/Qwen3-VL-30B-A3B-Instruct-AWQ-8bit

### dsikka · 2025-10-18

@JartX do you mind putting up a PR with your AWQ example script?

### JartX · 2025-10-18

@dsikka Of course, where should I put it? Is here okay with you?
https://github.com/vllm-project/llm-compressor/tree/main/examples/awq

### dsikka · 2025-10-18

@JartX perfect! Thank you!

### JartX · 2025-10-18

@dsikka published

### kylesayrs · 2025-10-20

Unfortunately, the core issue here is that the qwen3_moe_vl vision tower does not properly support offloading for the vision model. 

```
Traceback (most recent call last):
   ...

    pos_embeds = self.fast_pos_embed_interpolate(grid_thw)
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/transformers/models/qwen3_vl_moe/modeling_qwen3_vl_moe.py", line 738, in fast_pos_embed_interpolate
    pos_embeds = self.pos_embed(idx_tensor) * weight_tensor[:, :, None]
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^
  ...

  File "/usr/local/lib/python3.12/dist-packages/accelerate/utils/operations.py", line 153, in send_to_device
    return tensor.to(device, non_blocking=non_blocking)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
NotImplementedError: Cannot copy out of meta tensor; no data!
```

This issue is caused by this line in transformers:

https://github.com/huggingface/transformers/blob/bf0bce8d5fcbabcde86e63c2634e87ef8c2614dc/src/transformers/models/qwen3_vl_moe/modeling_qwen3_vl_moe.py#L704

EDIT: I meant to post this one
https://github.com/huggingface/transformers/blob/v4.57.1/src/transformers/models/qwen3_vl_moe/modeling_qwen3_vl_moe.py#L736

### kylesayrs · 2025-10-20

You can avoid triggering this bug by using a text-only dataset that does not trigger the vision tower, but this will lead to a sub-optimal quality of calibration and compression.

I'll post an example of how to patch this model. After that, @JartX could you please update your example to use a vision dataset like flickr?

### JartX · 2025-10-20

> Puedes evitar que se active este error utilizando un conjunto de datos de solo texto que no active la torre de visión, pero esto generará una calidad subóptima de calibración y compresión.
> 
> Publicaré un ejemplo de cómo parchar este modelo. Después,[@JartX](https://github.com/JartX)¿Podrías actualizar tu ejemplo para utilizar un conjunto de datos de visión como Flickr?

Sure!

### JartX · 2025-10-20

@kylesayrs I’ll also re-quantize the models with AWQ. Once you have it ready, just let me know, please :)

If the vision layers are ignored during quantization, does the quality also decrease? Thank you very much for your reply.



### kylesayrs · 2025-10-20

@JartX Could you please run this example and verify that it works for you? If it does, feel free to update your PR with the patch and updated example and we'll merge it!

https://github.com/vllm-project/llm-compressor/compare/kylesayrs/patch-qwen3_moe_vl

### JartX · 2025-10-20

@kylesayrs 
Sure, I'll give you an answer between today and tomorrow. Would you be so kind as to answer my question? Thank you very much :)

### JartX · 2025-10-20

@kylesayrs If it works, you could upload it directly to my branch, and then it will appear that we have both collaborated 😃

### kylesayrs · 2025-10-20

> If the vision layers are ignored during quantization, does the quality also decrease?

Sorry for missing this! The answer is that quantizing the vision tower will make the model run very slightly faster, but **decreases** model accuracy. However, the speed up is so small, we often skip quantizing the vision tower so that we can get better accuracy recovery.

Calibrating with the vision tower (and a vision dataset) is good, because then the model will activate in the same way it would during deployment. However, quantizing the vision tower is often not worth the accuracy loss, so we skip it.

### JartX · 2025-10-20

@kylesayrs 

Okay, if I understand correctly, even though the visual layers are ignored using:

ignore=[
"re:.*embed_tokens",
"re:.*input_layernorm$",
"re:.*mlp[.]gate$",
"re:.*post_attention_layernorm$",
"re:.*norm$",
"re:model[.]visual.*",
"re:visual.*",
"lm_head",
],

but the vision tower is independent and must be calibrated anyway, so that there is internal consistency. Many thanks for your time :)

### kylesayrs · 2025-10-20

> but the vision tower is independent and must be calibrated anyway

I think you have the right idea, but more precisely: it's less important to calibrate **with** the vision tower, and more important to **use the vision tower to calibrate the language model**. The vision tower is not quantized, so calibrating it is not important, but using a vision dataset which activates the vision tower is important, that way the language model can be calibrated with vision inputs.

### JartX · 2025-10-20

@kylesayrs  Thank you, now I understand correctly :)

### JartX · 2025-10-20

@kylesayrs I had to reduce the samples to 192, they don't even fit in https://console.runpod.io/deploy?gpu=RTX+PRO+6000&count=1&template=runpod-torch-v280 with 96gb of vram

### brian-dellabetta · 2025-10-20

> [@kylesayrs](https://github.com/kylesayrs) I had to reduce the samples to 192, they don't even fit in https://console.runpod.io/deploy?gpu=RTX+PRO+6000&count=1&template=runpod-torch-v280 with 96gb of vram

@JartX  you can try `offload_device=torch.device("cpu")` to reduce memory requirements. this should be particularly helpful for MoE models -- https://github.com/vllm-project/llm-compressor/blob/main/src/llmcompressor/modifiers/awq/base.py#L123

### JartX · 2025-10-20

Hi @brian-dellabetta thanks for the tip but, I have tried it, but the cost of the runpod in time was unaffordable, almost 30 minutes per layer VS if it fits in GPU 3 minutes per layer, the official script will keep the 256, but to test the calibration I would say that 192 is enough

### JartX · 2025-10-21

@kylesayrs 
https://huggingface.co/jart25/Qwen3-VL-30B-A3B-Instruct-AWQ-8bit-TEST

The quantized model Works, but wait...

From: https://github.com/vllm-project/vllm
I have a compiled image from October 14th, and another one from yesterday, October 20th. Everything works fine on the 14th, but with the code from October 20th, when I upload an image of an invoice, the model tells me it's a cake. It always talks about Chinese food. I'm freaking out, please help me out. xD

### JartX · 2025-10-21

@kylesayrs Please note that this now happens with all the models that were there, not just the one generated with your script xD

### JartX · 2025-10-21

@kylesayrs 
if I send the image with curl, without guidance, the model seems to work. We always talk about vllm as of 2025-10-14.The model with a text-only datasheet works in both cases.

With your patch: https://huggingface.co/jart25/Qwen3-VL-30B-A3B-Instruct-AWQ-8bit-TEST with flirck datashet

Withour your patch: https://huggingface.co/jart25/Qwen3-VL-30B-A3B-Instruct-AWQ-8bit



### JartX · 2025-10-21

Revert: https://github.com/vllm-project/vllm/pull/27106 and now the text-only quantified model interprets images correctly again, no longer thinking that an invoice is a cake.

### kylesayrs · 2025-10-22

@JartX Nice! Yeah, whether models need to be calibrated with vision datasets is an active research question. Our research team has quantized vision models with text-only datasets and still maintained good performance on vision tasks, so I'm glad to see that that is the case here.

If you end up running vision evals against your model, feel free to post the results here for others to see! You can also add them to the README.md in another contribution in the same folder as your PR.

### bialykostek · 2025-10-29

Hi! 
I'm not sure if I understood correctly, but at this point no one was able to use images dataset in AWQ quantization? I'm trying to achieve the same but I've encountered similar problems to ones described in this thread: `NotImplementedError: Cannot copy out of meta tensor; no data!`. Using https://github.com/ronantakizawa/llm-compressor I was able to run sequential calibration pipeline with images and save compressed model, however later I'm not able to run model with vLLM due to `KeyError: 'layers.0.mlp.experts.w2_weight_zero_point'`. 
I'm stuck here, has anyone made any further progress?
Thanks! 
PS: I was able to finetune this model, if someone needs I can share notebook :) My model has been trained for very specific OCR-like task, that's why I want to use my dataset for calibration.

### JartX · 2025-10-29

@bialykostek  Would you be so kind as to share how you did it? Does it also work with structured outputs?

### bialykostek · 2025-10-29

Sure!
Finetune notebook - based on Unslosh tutorial (I used RunPod H100 SXM): https://drive.google.com/file/d/1z84Ls_edWAVzrt6-XaI42lpSkr2YoP9_/view?usp=sharing
Quantization notebook (I used RunPod RTX PRO 6000 WK): https://drive.google.com/file/d/19DNJDXlhYNaIhZnh4Suoa8rN9_JGDqRD/view?usp=sharing

In my case output is structured YAML - performance and accuracy of this model is amazing.

### JartX · 2025-10-29

@bialykostek remove the files!!!!!! check the tokenizer token

### JartX · 2025-10-29

And the structured outputs? Works fine? After quantize with images data dont works me

### bialykostek · 2025-10-29

Thanks, i didn't notice it. What exactly do you mean by structured output? My dataset is: system prompt explaining task, user prompt "Extract data", image and as assistant output yaml with all the data to extract. Works perfect for me. Even after quantization with text-only dataset, it still works but accuracy is slightly lower. 

### ComistryMo · 2025-11-07

@bialykostek Hello, Can you run sequential calibration pipeline with images, then run model with vLLM now? I also want to do awq on Qwen3VL with images and texts.

### bialykostek · 2025-11-07

@ComistryMo unfortunately, I didn't have time for further investigation. For the moment I'm using model calibrated with text-only dataset, but output precision has dropped. Hopefully, the mentioned problem with metatensors will be fixed. https://github.com/vllm-project/llm-compressor/pull/1930 this was closed because as mentioned problem was fixed in the newest version of torch - I've tried with 2.9 with no luck :(

### ComistryMo · 2025-11-21

> [@ComistryMo](https://github.com/ComistryMo) unfortunately, I didn't have time for further investigation. For the moment I'm using model calibrated with text-only dataset, but output precision has dropped. Hopefully, the mentioned problem with metatensors will be fixed. [#1930](https://github.com/vllm-project/llm-compressor/pull/1930) this was closed because as mentioned problem was fixed in the newest version of torch - I've tried with 2.9 with no luck :(

I successfully completed the awq with image-text dataset on Qwen3vl-30B-A3B, by using the patch mentioned in the issue. I did some test and accuracy remained high with negligible degradation

### bialykostek · 2025-11-21

@ComistryMo congratulations!! Can you please share code or notebook you used? 

### JartX · 2025-11-21

@bialykostek @ComistryMo Hi both! Does the combination of structured output and image response work for you? If it's quantized with text only, it responds; if it's quantized with both text and image, it doesn't respond.

Hey! @bialykostek Long time no see! haha ​​It's great to see you here

### bialykostek · 2025-11-21

@JartX hi again :) yes, in my case structured output works, but I've finetunned the model first (on 1k images + yaml labels). My input is image of receipt and output is YAML with details. Works great for me. Quantization lowers precision of OCR but output structure is always correct 

### JartX · 2025-11-21

@bialykostek Would you be so kind as to send me the Python code, even without providing the datasheet? Thank you very much :)

### JartX · 2025-11-21

@bialykostek with this patch?

https://github.com/vllm-project/llm-compressor/compare/kylesayrs/patch-qwen3_moe_vl

### bialykostek · 2025-11-21

> Sure! Finetune notebook - based on Unslosh tutorial (I used RunPod H100 SXM): https://drive.google.com/file/d/1z84Ls_edWAVzrt6-XaI42lpSkr2YoP9_/view?usp=sharing Quantization notebook (I used RunPod RTX PRO 6000 WK): https://drive.google.com/file/d/19DNJDXlhYNaIhZnh4Suoa8rN9_JGDqRD/view?usp=sharing
> 
> In my case output is structured YAML - performance and accuracy of this model is amazing.

I've used those notebooks, the model I've created with those is in production now and doing pretty good and stable job. I didn't used patched version because there was error when running it with vLLM, so it was quantized using original lib and text only calibration dataset. @ComistryMo did you manage to run quantized model using vLLM? Which patch did you use?

### JartX · 2025-11-22

```
vllm1-1  | (APIServer pid=1) Traceback (most recent call last):
vllm1-1  | (APIServer pid=1)   File "/usr/local/bin/vllm", line 10, in <module>
vllm1-1  | (APIServer pid=1)     sys.exit(main())
vllm1-1  | (APIServer pid=1)              ^^^^^^
vllm1-1  | (APIServer pid=1)   File "/usr/local/lib/python3.12/dist-packages/vllm/entrypoints/cli/main.py", line 73, in main
vllm1-1  | (APIServer pid=1)     args.dispatch_function(args)
vllm1-1  | (APIServer pid=1)   File "/usr/local/lib/python3.12/dist-packages/vllm/entrypoints/cli/serve.py", line 60, in cmd
vllm1-1  | (APIServer pid=1)     uvloop.run(run_server(args))
vllm1-1  | (APIServer pid=1)   File "/usr/local/lib/python3.12/dist-packages/uvloop/__init__.py", line 96, in run
vllm1-1  | (APIServer pid=1)     return __asyncio.run(
vllm1-1  | (APIServer pid=1)            ^^^^^^^^^^^^^^
vllm1-1  | (APIServer pid=1)   File "/usr/lib/python3.12/asyncio/runners.py", line 195, in run
vllm1-1  | (APIServer pid=1)     return runner.run(main)
vllm1-1  | (APIServer pid=1)            ^^^^^^^^^^^^^^^^
vllm1-1  | (APIServer pid=1)   File "/usr/lib/python3.12/asyncio/runners.py", line 118, in run
vllm1-1  | (APIServer pid=1)     return self._loop.run_until_complete(task)
vllm1-1  | (APIServer pid=1)            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
vllm1-1  | (APIServer pid=1)   File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
vllm1-1  | (APIServer pid=1)   File "/usr/local/lib/python3.12/dist-packages/uvloop/__init__.py", line 48, in wrapper
vllm1-1  | (APIServer pid=1)     return await main
vllm1-1  | (APIServer pid=1)            ^^^^^^^^^^
vllm1-1  | (APIServer pid=1)   File "/usr/local/lib/python3.12/dist-packages/vllm/entrypoints/openai/api_server.py", line 2028, in run_server
vllm1-1  | (APIServer pid=1)     await run_server_worker(listen_address, sock, args, **uvicorn_kwargs)
vllm1-1  | (APIServer pid=1)   File "/usr/local/lib/python3.12/dist-packages/vllm/entrypoints/openai/api_server.py", line 2047, in run_server_worker
vllm1-1  | (APIServer pid=1)     async with build_async_engine_client(
vllm1-1  | (APIServer pid=1)                ^^^^^^^^^^^^^^^^^^^^^^^^^^
vllm1-1  | (APIServer pid=1)   File "/usr/lib/python3.12/contextlib.py", line 210, in __aenter__
vllm1-1  | (APIServer pid=1)     return await anext(self.gen)
vllm1-1  | (APIServer pid=1)            ^^^^^^^^^^^^^^^^^^^^^
vllm1-1  | (APIServer pid=1)   File "/usr/local/lib/python3.12/dist-packages/vllm/entrypoints/openai/api_server.py", line 196, in build_async_engine_client
vllm1-1  | (APIServer pid=1)     async with build_async_engine_client_from_engine_args(
vllm1-1  | (APIServer pid=1)                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
vllm1-1  | (APIServer pid=1)   File "/usr/lib/python3.12/contextlib.py", line 210, in __aenter__
vllm1-1  | (APIServer pid=1)     return await anext(self.gen)
vllm1-1  | (APIServer pid=1)            ^^^^^^^^^^^^^^^^^^^^^
vllm1-1  | (APIServer pid=1)   File "/usr/local/lib/python3.12/dist-packages/vllm/entrypoints/openai/api_server.py", line 222, in build_async_engine_client_from_engine_args
vllm1-1  | (APIServer pid=1)     vllm_config = engine_args.create_engine_config(usage_context=usage_context)
vllm1-1  | (APIServer pid=1)                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
vllm1-1  | (APIServer pid=1)   File "/usr/local/lib/python3.12/dist-packages/vllm/engine/arg_utils.py", line 1772, in create_engine_config
vllm1-1  | (APIServer pid=1)     config = VllmConfig(
vllm1-1  | (APIServer pid=1)              ^^^^^^^^^^^
vllm1-1  | (APIServer pid=1)   File "/usr/local/lib/python3.12/dist-packages/pydantic/_internal/_dataclasses.py", line 121, in __init__
vllm1-1  | (APIServer pid=1)     s.__pydantic_validator__.validate_python(ArgsKwargs(args, kwargs), self_instance=s)
vllm1-1  | (APIServer pid=1) pydantic_core._pydantic_core.ValidationError: 2 validation errors for VllmConfig
vllm1-1  | (APIServer pid=1) scale_dtype
vllm1-1  | (APIServer pid=1)   Extra inputs are not permitted [type=extra_forbidden, input_value=None, input_type=NoneType]
vllm1-1  | (APIServer pid=1)     For further information visit https://errors.pydantic.dev/2.12/v/extra_forbidden
vllm1-1  | (APIServer pid=1) zp_dtype
vllm1-1  | (APIServer pid=1)   Extra inputs are not permitted [type=extra_forbidden, input_value=None, input_type=NoneType]
vllm1-1  | (APIServer pid=1)     For further information visit https://errors.pydantic.dev/2.12/v/extra_forbidden
```

https://www.diffchecker.com/C4vMRr1Q/

Fail at validation caused by:

`"zp_dtype": null`
` "scale_dtype": null,`


in config.json
on quant

removing it all works
@bialykostek 

### JartX · 2025-11-22

```
import base64
from io import BytesIO
import torch
from datasets import load_dataset
from transformers import Qwen3VLMoeForConditionalGeneration, AutoProcessor
from transformers.models.qwen3_vl_moe import Qwen3VLMoeVisionModel
from llmcompressor import oneshot
from llmcompressor.modifiers.awq import AWQModifier
from llmcompressor.modeling import replace_modules_for_calibration
from llmcompressor.modeling.patches import fast_pos_embed_interpolate

MODEL_ID = "Qwen/Qwen3-VL-30B-A3B-Instruct"
OUTPUT_DIR = MODEL_ID.split("/")[-1] + "-AWQ-W4A16-TOWER"

Qwen3VLMoeVisionModel.fast_pos_embed_interpolate = fast_pos_embed_interpolate

model = Qwen3VLMoeForConditionalGeneration.from_pretrained(
    MODEL_ID,
    torch_dtype=torch.bfloat16,
    device_map=None,
    trust_remote_code=True,
)
processor = AutoProcessor.from_pretrained(MODEL_ID, trust_remote_code=True)
model = replace_modules_for_calibration(model)

DATASET_ID = "lmms-lab/flickr30k"
NUM_CALIBRATION_SAMPLES = 256
DATASET_SPLIT = f"test[:{NUM_CALIBRATION_SAMPLES}]"
MAX_SEQUENCE_LENGTH = 1024

ds = load_dataset(DATASET_ID, split=DATASET_SPLIT)
ds = ds.shuffle(seed=42)

def preprocess_and_tokenize(example):
    buffered = BytesIO()
    example["image"].save(buffered, format="PNG")
    encoded_image = base64.b64encode(buffered.getvalue())
    base64_image = f"data:image;base64,{encoded_image.decode('utf-8')}"
    messages = [{
        "role": "user",
        "content": [
            {"type": "image", "image": base64_image},
            {"type": "text", "text": "What does the image show?"}
        ]
    }]
    text = processor.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True
    )
    inputs = processor(
        text=[text],
        images=[example["image"]],
        padding=False,
        max_length=MAX_SEQUENCE_LENGTH,
        truncation=True,
    )
    return inputs

ds = ds.map(preprocess_and_tokenize, remove_columns=ds.column_names)

def data_collator(batch):
    assert len(batch) == 1
    return {key: torch.tensor(value) for key, value in batch[0].items()}

recipe = AWQModifier(
    ignore=["re:.*lm_head", "re:.*visual.*", "re:.*mlp.gate$","re:.*mlp.shared_expert_gate$"],
    duo_scaling=False,
    config_groups={
        "group_0": {
            "targets": ["Linear"],
            "input_activations": None,
            "output_activations": None,
            "weights": {
                "num_bits": 4,
                "type": "int",
                "symmetric": True,
                "strategy": "group",
                "group_size": 32,
                "observer": "mse",
            }
        }
    }
)

oneshot(
    model=model,
    processor=processor,
    recipe=recipe,
    dataset=ds,
    max_seq_length=MAX_SEQUENCE_LENGTH,
    num_calibration_samples=NUM_CALIBRATION_SAMPLES,
    data_collator=data_collator,
    pipeline="sequential",
)

model.save_pretrained(OUTPUT_DIR, save_compressed=True)
processor.save_pretrained(OUTPUT_DIR)
```

The script with the patch of @kylesayrs on https://github.com/vllm-project/llm-compressor/tree/37cfe8ec141e5246b5decbf4d8f9d411c492866c

### JartX · 2025-11-22

@kylesayrs With your monkeypatch, by removing the two values ​​I mentioned, in the exact llmcompressor commit I posted, I can verify that quantization with images worked correctly and that it started correctly in the latest vllm images: vllm-rocm:251119

### ComistryMo · 2025-11-24

> > Sure! Finetune notebook - based on Unslosh tutorial (I used RunPod H100 SXM): https://drive.google.com/file/d/1z84Ls_edWAVzrt6-XaI42lpSkr2YoP9_/view?usp=sharing Quantization notebook (I used RunPod RTX PRO 6000 WK): https://drive.google.com/file/d/19DNJDXlhYNaIhZnh4Suoa8rN9_JGDqRD/view?usp=sharing
> > In my case output is structured YAML - performance and accuracy of this model is amazing.
> 
> I've used those notebooks, the model I've created with those is in production now and doing pretty good and stable job. I didn't used patched version because there was error when running it with vLLM, so it was quantized using original lib and text only calibration dataset. [@ComistryMo](https://github.com/ComistryMo) did you manage to run quantized model using vLLM? Which patch did you use?

Hello friend. Apologies for the late reply.

I actually used the method described here: https://github.com/vllm-project/llm-compressor/issues/1939#issuecomment-3566308801. Removing those two parameters allowed me to run it in vLLM, and the results were fine. Hope it works for you as well. The patch: https://github.com/vllm-project/llm-compressor/compare/kylesayrs/patch-qwen3_moe_vl. 

### bialykostek · 2025-12-01

@ComistryMo @JartX guys thank you so much!!!! It works! I used the https://github.com/vllm-project/llm-compressor/compare/kylesayrs/patch-qwen3_moe_vl patch and removed two parameters, works perfect.

Thanks once again!

### gxaurab · 2026-08-18

Original model size 57gb
Compressed 57Gb

I got the same error but turns out I wasn't saving the quantized model and original (uncompressed ) was being saved. 

    model.save_pretrained(
        args.out,
        save_compressed=True,
        quantization_format=fmt,
    )

