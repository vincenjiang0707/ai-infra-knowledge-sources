# [Issue #1625] [BUG] RuntimeError: b_q_weight type is not kInt

source: https://github.com/ModelCloud/GPTQModel/issues/1625
state: open | updated: 2026-01-26T14:36:45Z
labels: bug

## 正文

**Describe the bug**

qwen3-30B-A3B-GPTQ-INT4 
**GPU Info**

Show output of:
INFO  ENV: Auto setting PYTORCH_CUDA_ALLOC_CONF='expandable_segments:True' for memory saving.
INFO  ENV: Auto setting CUDA_DEVICE_ORDER=PCI_BUS_ID for correctness.          
Detected gptqmodel and auto-gptq, will use gptqmodel
INFO   Kernel: Auto-selection: adding candidate MarlinQuantLinear            
loss_type=None was set in the config but it is unrecognised.Using the default loss: ForCausalLMLoss.
Detected gptqmodel and auto-gptq, will use gptqmodel
Some weights of the model checkpoint at /mnt/user/ai_00328713/tenant-home_speed/Model/Qwen3/Qwen3-30B-A3B-GPTQ-Int4 were not used when initializing Qwen3MoeForCausalLM: ['model.layers.0.mlp.gate.weight', 'model.layers.1.mlp.gate.weight', 'model.layers.10.mlp.gate.weight', 'model.layers.11.mlp.gate.weight', 'model.layers.12.mlp.gate.weight', 'model.layers.13.mlp.gate.weight', 'model.layers.14.mlp.gate.weight', 'model.layers.15.mlp.gate.weight', 'model.layers.16.mlp.gate.weight', 'model.layers.17.mlp.gate.weight', 'model.layers.18.mlp.gate.weight', 'model.layers.19.mlp.gate.weight', 'model.layers.2.mlp.gate.weight', 'model.layers.20.mlp.gate.weight', 'model.layers.21.mlp.gate.weight', 'model.layers.22.mlp.gate.weight', 'model.layers.23.mlp.gate.weight', 'model.layers.24.mlp.gate.weight', 'model.layers.25.mlp.gate.weight', 'model.layers.26.mlp.gate.weight', 'model.layers.27.mlp.gate.weight', 'model.layers.28.mlp.gate.weight', 'model.layers.29.mlp.gate.weight', 'model.layers.3.mlp.gate.weight', 'model.layers.30.mlp.gate.weight', 'model.layers.31.mlp.gate.weight', 'model.layers.32.mlp.gate.weight', 'model.layers.33.mlp.gate.weight', 'model.layers.34.mlp.gate.weight', 'model.layers.35.mlp.gate.weight', 'model.layers.36.mlp.gate.weight', 'model.layers.37.mlp.gate.weight', 'model.layers.38.mlp.gate.weight', 'model.layers.39.mlp.gate.weight', 'model.layers.4.mlp.gate.weight', 'model.layers.40.mlp.gate.weight', 'model.layers.41.mlp.gate.weight', 'model.layers.42.mlp.gate.weight', 'model.layers.43.mlp.gate.weight', 'model.layers.44.mlp.gate.weight', 'model.layers.45.mlp.gate.weight', 'model.layers.46.mlp.gate.weight', 'model.layers.47.mlp.gate.weight', 'model.layers.5.mlp.gate.weight', 'model.layers.6.mlp.gate.weight', 'model.layers.7.mlp.gate.weight', 'model.layers.8.mlp.gate.weight', 'model.layers.9.mlp.gate.weight']
- This IS expected if you are initializing Qwen3MoeForCausalLM from the checkpoint of a model trained on another task or with another architecture (e.g. initializing a BertForSequenceClassification model from a BertForPreTraining model).
- This IS NOT expected if you are initializing Qwen3MoeForCausalLM from the checkpoint of a model that you expect to be exactly identical (initializing a BertForSequenceClassification model from a BertForSequenceClassification model).
Some weights of Qwen3MoeForCausalLM were not initialized from the model checkpoint at /mnt/user/ai_00328713/tenant-home_speed/Model/Qwen3/Qwen3-30B-A3B-GPTQ-Int4 and are newly initialized: ['model.layers.0.mlp.gate.g_idx', 'model.layers.0.mlp.gate.qweight', 'model.layers.0.mlp.gate.qzeros', 'model.layers.0.mlp.gate.scales', 'model.layers.1.mlp.gate.g_idx', 'model.layers.1.mlp.gate.qweight', 'model.layers.1.mlp.gate.qzeros', 'model.layers.1.mlp.gate.scales', 'model.layers.10.mlp.gate.g_idx', 'model.layers.10.mlp.gate.qweight', 'model.layers.10.mlp.gate.qzeros', 'model.layers.10.mlp.gate.scales', 'model.layers.11.mlp.gate.g_idx', 'model.layers.11.mlp.gate.qweight', 'model.layers.11.mlp.gate.qzeros', 'model.layers.11.mlp.gate.scales', 'model.layers.12.mlp.gate.g_idx', 'model.layers.12.mlp.gate.qweight', 'model.layers.12.mlp.gate.qzeros', 'model.layers.12.mlp.gate.scales', 'model.layers.13.mlp.gate.g_idx', 'model.layers.13.mlp.gate.qweight', 'model.layers.13.mlp.gate.qzeros', 'model.layers.13.mlp.gate.scales', 'model.layers.14.mlp.gate.g_idx', 'model.layers.14.mlp.gate.qweight', 'model.layers.14.mlp.gate.qzeros', 'model.layers.14.mlp.gate.scales', 'model.layers.15.mlp.gate.g_idx', 'model.layers.15.mlp.gate.qweight', 'model.layers.15.mlp.gate.qzeros', 'model.layers.15.mlp.gate.scales', 'model.layers.16.mlp.gate.g_idx', 'model.layers.16.mlp.gate.qweight', 'model.layers.16.mlp.gate.qzeros', 'model.layers.16.mlp.gate.scales', 'model.layers.17.mlp.gate.g_idx', 'model.layers.17.mlp.gate.qweight', 'model.layers.17.mlp.gate.qzeros', 'model.layers.17.mlp.gate.scales', 'model.layers.18.mlp.gate.g_idx', 'model.layers.18.mlp.gate.qweight', 'model.layers.18.mlp.gate.qzeros', 'model.layers.18.mlp.gate.scales', 'model.layers.19.mlp.gate.g_idx', 'model.layers.19.mlp.gate.qweight', 'model.layers.19.mlp.gate.qzeros', 'model.layers.19.mlp.gate.scales', 'model.layers.2.mlp.gate.g_idx', 'model.layers.2.mlp.gate.qweight', 'model.layers.2.mlp.gate.qzeros', 'model.layers.2.mlp.gate.scales', 'model.layers.20.mlp.gate.g_idx', 'model.layers.20.mlp.gate.qweight', 'model.layers.20.mlp.gate.qzeros', 'model.layers.20.mlp.gate.scales', 'model.layers.21.mlp.gate.g_idx', 'model.layers.21.mlp.gate.qweight', 'model.layers.21.mlp.gate.qzeros', 'model.layers.21.mlp.gate.scales', 'model.layers.22.mlp.gate.g_idx', 'model.layers.22.mlp.gate.qweight', 'model.layers.22.mlp.gate.qzeros', 'model.layers.22.mlp.gate.scales', 'model.layers.23.mlp.gate.g_idx', 'model.layers.23.mlp.gate.qweight', 'model.layers.23.mlp.gate.qzeros', 'model.layers.23.mlp.gate.scales', 'model.layers.24.mlp.gate.g_idx', 'model.layers.24.mlp.gate.qweight', 'model.layers.24.mlp.gate.qzeros', 'model.layers.24.mlp.gate.scales', 'model.layers.25.mlp.gate.g_idx', 'model.layers.25.mlp.gate.qweight', 'model.layers.25.mlp.gate.qzeros', 'model.layers.25.mlp.gate.scales', 'model.layers.26.mlp.gate.g_idx', 'model.layers.26.mlp.gate.qweight', 'model.layers.26.mlp.gate.qzeros', 'model.layers.26.mlp.gate.scales', 'model.layers.27.mlp.gate.g_idx', 'model.layers.27.mlp.gate.qweight', 'model.layers.27.mlp.gate.qzeros', 'model.layers.27.mlp.gate.scales', 'model.layers.28.mlp.gate.g_idx', 'model.layers.28.mlp.gate.qweight', 'model.layers.28.mlp.gate.qzeros', 'model.layers.28.mlp.gate.scales', 'model.layers.29.mlp.gate.g_idx', 'model.layers.29.mlp.gate.qweight', 'model.layers.29.mlp.gate.qzeros', 'model.layers.29.mlp.gate.scales', 'model.layers.3.mlp.gate.g_idx', 'model.layers.3.mlp.gate.qweight', 'model.layers.3.mlp.gate.qzeros', 'model.layers.3.mlp.gate.scales', 'model.layers.30.mlp.gate.g_idx', 'model.layers.30.mlp.gate.qweight', 'model.layers.30.mlp.gate.qzeros', 'model.layers.30.mlp.gate.scales', 'model.layers.31.mlp.gate.g_idx', 'model.layers.31.mlp.gate.qweight', 'model.layers.31.mlp.gate.qzeros', 'model.layers.31.mlp.gate.scales', 'model.layers.32.mlp.gate.g_idx', 'model.layers.32.mlp.gate.qweight', 'model.layers.32.mlp.gate.qzeros', 'model.layers.32.mlp.gate.scales', 'model.layers.33.mlp.gate.g_idx', 'model.layers.33.mlp.gate.qweight', 'model.layers.33.mlp.gate.qzeros', 'model.layers.33.mlp.gate.scales', 'model.layers.34.mlp.gate.g_idx', 'model.layers.34.mlp.gate.qweight', 'model.layers.34.mlp.gate.qzeros', 'model.layers.34.mlp.gate.scales', 'model.layers.35.mlp.gate.g_idx', 'model.layers.35.mlp.gate.qweight', 'model.layers.35.mlp.gate.qzeros', 'model.layers.35.mlp.gate.scales', 'model.layers.36.mlp.gate.g_idx', 'model.layers.36.mlp.gate.qweight', 'model.layers.36.mlp.gate.qzeros', 'model.layers.36.mlp.gate.scales', 'model.layers.37.mlp.gate.g_idx', 'model.layers.37.mlp.gate.qweight', 'model.layers.37.mlp.gate.qzeros', 'model.layers.37.mlp.gate.scales', 'model.layers.38.mlp.gate.g_idx', 'model.layers.38.mlp.gate.qweight', 'model.layers.38.mlp.gate.qzeros', 'model.layers.38.mlp.gate.scales', 'model.layers.39.mlp.gate.g_idx', 'model.layers.39.mlp.gate.qweight', 'model.layers.39.mlp.gate.qzeros', 'model.layers.39.mlp.gate.scales', 'model.layers.4.mlp.gate.g_idx', 'model.layers.4.mlp.gate.qweight', 'model.layers.4.mlp.gate.qzeros', 'model.layers.4.mlp.gate.scales', 'model.layers.40.mlp.gate.g_idx', 'model.layers.40.mlp.gate.qweight', 'model.layers.40.mlp.gate.qzeros', 'model.layers.40.mlp.gate.scales', 'model.layers.41.mlp.gate.g_idx', 'model.layers.41.mlp.gate.qweight', 'model.layers.41.mlp.gate.qzeros', 'model.layers.41.mlp.gate.scales', 'model.layers.42.mlp.gate.g_idx', 'model.layers.42.mlp.gate.qweight', 'model.layers.42.mlp.gate.qzeros', 'model.layers.42.mlp.gate.scales', 'model.layers.43.mlp.gate.g_idx', 'model.layers.43.mlp.gate.qweight', 'model.layers.43.mlp.gate.qzeros', 'model.layers.43.mlp.gate.scales', 'model.layers.44.mlp.gate.g_idx', 'model.layers.44.mlp.gate.qweight', 'model.layers.44.mlp.gate.qzeros', 'model.layers.44.mlp.gate.scales', 'model.layers.45.mlp.gate.g_idx', 'model.layers.45.mlp.gate.qweight', 'model.layers.45.mlp.gate.qzeros', 'model.layers.45.mlp.gate.scales', 'model.layers.46.mlp.gate.g_idx', 'model.layers.46.mlp.gate.qweight', 'model.layers.46.mlp.gate.qzeros', 'model.layers.46.mlp.gate.scales', 'model.layers.47.mlp.gate.g_idx', 'model.layers.47.mlp.gate.qweight', 'model.layers.47.mlp.gate.qzeros', 'model.layers.47.mlp.gate.scales', 'model.layers.5.mlp.gate.g_idx', 'model.layers.5.mlp.gate.qweight', 'model.layers.5.mlp.gate.qzeros', 'model.layers.5.mlp.gate.scales', 'model.layers.6.mlp.gate.g_idx', 'model.layers.6.mlp.gate.qweight', 'model.layers.6.mlp.gate.qzeros', 'model.layers.6.mlp.gate.scales', 'model.layers.7.mlp.gate.g_idx', 'model.layers.7.mlp.gate.qweight', 'model.layers.7.mlp.gate.qzeros', 'model.layers.7.mlp.gate.scales', 'model.layers.8.mlp.gate.g_idx', 'model.layers.8.mlp.gate.qweight', 'model.layers.8.mlp.gate.qzeros', 'model.layers.8.mlp.gate.scales', 'model.layers.9.mlp.gate.g_idx', 'model.layers.9.mlp.gate.qweight', 'model.layers.9.mlp.gate.qzeros', 'model.layers.9.mlp.gate.scales']
You should probably TRAIN this model on a down-stream task to be able to use it for predictions and inference.
Traceback (most recent call last):
  File "/tmp/pycharm_project_245/pycharm/code/查看qwen3-gptq模型量化.py", line 8, in <module>
    model = AutoModelForCausalLM.from_pretrained(
  File "/mnt/user/ai_00328713/tenant-home_speed/shard/yangkang/testvenv/lib/python3.10/site-packages/transformers/models/auto/auto_factory.py", line 571, in from_pretrained
    return model_class.from_pretrained(
  File "/mnt/user/ai_00328713/tenant-home_speed/shard/yangkang/testvenv/lib/python3.10/site-packages/transformers/modeling_utils.py", line 279, in _wrapper
    return func(*args, **kwargs)
  File "/mnt/user/ai_00328713/tenant-home_speed/shard/yangkang/testvenv/lib/python3.10/site-packages/transformers/modeling_utils.py", line 4478, in from_pretrained
    hf_quantizer.postprocess_model(model, config=config)
  File "/mnt/user/ai_00328713/tenant-home_speed/shard/yangkang/testvenv/lib/python3.10/site-packages/transformers/quantizers/base.py", line 238, in postprocess_model
    return self._process_model_after_weight_loading(model, **kwargs)
  File "/mnt/user/ai_00328713/tenant-home_speed/shard/yangkang/testvenv/lib/python3.10/site-packages/transformers/quantizers/quantizer_gptq.py", line 111, in _process_model_after_weight_loading
    model = self.optimum_quantizer.post_init_model(model)
  File "/mnt/user/ai_00328713/tenant-home_speed/shard/yangkang/testvenv/lib/python3.10/site-packages/optimum/gptq/quantizer.py", line 738, in post_init_model
    model = gptq_post_init(model, use_act_order=self.desc_act)
  File "/mnt/user/ai_00328713/tenant-home_speed/shard/yangkang/testvenv/lib/python3.10/site-packages/gptqmodel/utils/model.py", line 689, in hf_gptqmodel_post_init
    return gptqmodel_post_init(model, use_act_order, quantize_config, max_input_length)
  File "/mnt/user/ai_00328713/tenant-home_speed/shard/yangkang/testvenv/lib/python3.10/site-packages/gptqmodel/utils/model.py", line 809, in gptqmodel_post_init
    submodule.post_init()
  File "/mnt/user/ai_00328713/tenant-home_speed/shard/yangkang/testvenv/lib/python3.10/site-packages/gptqmodel/nn_modules/qlinear/marlin.py", line 385, in post_init
    marlin_qweight = gptqmodel_marlin_kernels.gptq_marlin_repack(
RuntimeError: b_q_weight type is not kInt

Process finished with exit code 1
```
nvidia-smi
```

**Software Info**

Operation System/Version + Python Version

Name: gptqmodel
Version: 2.2.0
Summary: Production ready LLM model compression/quantization toolkit with hw accelerated inference support for both cpu/gpu via HF, vLLM, and SGLang.
Home-page: https://github.com/ModelCloud/GPTQModel
Author: ModelCloud
Author-email: qubitium@modelcloud.ai
License: Apache 2.0
Location: /mnt/user/ai_00328713/tenant-home_speed/shard/yangkang/testvenv/lib/python3.10/site-packages
Requires: accelerate, datasets, device-smi, hf-transfer, huggingface-hub, logbar, numpy, packaging, pillow, protobuf, random-word, safetensors, threadpoolctl, tokenicer, torch, transformers
Required-by: 
---
Name: torch
Version: 2.6.0
Summary: Tensors and Dynamic neural networks in Python with strong GPU acceleration
Home-page: https://pytorch.org/
Author: PyTorch Team
Author-email: packages@pytorch.org
License: BSD-3-Clause
Location: /mnt/user/ai_00328713/tenant-home_speed/shard/yangkang/testvenv/lib/python3.10/site-packages
Requires: filelock, fsspec, jinja2, networkx, nvidia-cublas-cu12, nvidia-cuda-cupti-cu12, nvidia-cuda-nvrtc-cu12, nvidia-cuda-runtime-cu12, nvidia-cudnn-cu12, nvidia-cufft-cu12, nvidia-curand-cu12, nvidia-cusolver-cu12, nvidia-cusparse-cu12, nvidia-cusparselt-cu12, nvidia-nccl-cu12, nvidia-nvjitlink-cu12, nvidia-nvtx-cu12, sympy, triton, typing-extensions
Required-by: accelerate, auto_gptq, autoawq, bitsandbytes, compressed-tensors, deepspeed, flash_attn, flashinfer-python, gptqmodel, llmcompressor, optimum, outlines, peft, torchaudio, torchvision, vllm, xformers, xgrammar
---
Name: transformers
Version: 4.51.3
Summary: State-of-the-art Machine Learning for JAX, PyTorch and TensorFlow
Home-page: https://github.com/huggingface/transformers
Author: The Hugging Face team (past and future) with the help of all our contributors (https://github.com/huggingface/transformers/graphs/contributors)
Author-email: transformers@huggingface.co
License: Apache 2.0 License
Location: /mnt/user/ai_00328713/tenant-home_speed/shard/yangkang/testvenv/lib/python3.10/site-packages
Requires: filelock, huggingface-hub, numpy, packaging, pyyaml, regex, requests, safetensors, tokenizers, tqdm
Required-by: auto_gptq, autoawq, compressed-tensors, gptqmodel, llmcompressor, optimum, peft, tokenicer, trl, vllm, xgrammar
---
Name: accelerate
Version: 1.7.0
Summary: Accelerate
Home-page: https://github.com/huggingface/accelerate
Author: The HuggingFace team
Author-email: zach.mueller@huggingface.co
License: Apache
Location: /mnt/user/ai_00328713/tenant-home_speed/shard/yangkang/testvenv/lib/python3.10/site-packages
Requires: huggingface-hub, numpy, packaging, psutil, pyyaml, safetensors, torch
Required-by: auto_gptq, autoawq, gptqmodel, llmcompressor, peft, trl
---
Name: triton
Version: 3.2.0
Summary: A language and compiler for custom Deep Learning operations
Home-page: https://github.com/triton-lang/triton/
Author: Philippe Tillet
Author-email: phil@openai.com
License: 
Location: /mnt/user/ai_00328713/tenant-home_speed/shard/yangkang/testvenv/lib/python3.10/site-packages
Requires: 
Required-by: autoawq, torch, xgrammar


config.json
{
  "architectures": [
    "Qwen3MoeForCausalLM"
  ],
  "attention_bias": false,
  "attention_dropout": 0.0,
  "bos_token_id": 151643,
  "decoder_sparse_step": 1,
  "eos_token_id": 151645,
  "head_dim": 128,
  "hidden_act": "silu",
  "hidden_size": 2048,
  "initializer_range": 0.02,
  "intermediate_size": 6144,
  "max_position_embeddings": 40960,
  "max_window_layers": 48,
  "mlp_only_layers": [],
  "model_type": "qwen3_moe",
  "moe_intermediate_size": 768,
  "norm_topk_prob": true,
  "num_attention_heads": 32,
  "num_experts": 128,
  "num_experts_per_tok": 8,
  "num_hidden_layers": 48,
  "num_key_value_heads": 4,
  "output_router_logits": false,
  "quantization_config": {
    "bits": 4,
    "checkpoint_format": "gptq",
    "damp_percent": 0.01,
    "desc_act": false,
    "group_size": 128,
    "model_file_base_name": null,
    "model_name_or_path": null,
    "quant_method": "gptq",
    "static_groups": false,
    "sym": true,
    "true_sequential": true
  },
  "rms_norm_eps": 1e-06,
  "rope_scaling": null,
  "rope_theta": 1000000.0,
  "router_aux_loss_coef": 0.001,
    "sliding_window": null,
  "tie_word_embeddings": false,
  "torch_dtype": "float16",
  "transformers_version": "4.51.3",
  "use_cache": true,
  "use_sliding_window": false,
  "vocab_size": 151936
}


quantize_config.json
{
  "bits": 4,
  "group_size": 128,
  "damp_percent": 0.01,
  "desc_act": false,
  "static_groups": false,
  "sym": true,
  "true_sequential": true,
  "model_name_or_path": null,
  "model_file_base_name": null,
  "quant_method": "gptq",
  "checkpoint_format": "gptq"
}






## 评论 (4)

### Qubitium · 2025-06-03

@wumaotegan  Please test `main` branch. 

### wumaotegan · 2025-06-03

> [@wumaotegan](https://github.com/wumaotegan) Please test `main` branch.

I tried the main branch, but the same error still occurred. I'm using the Transformers library to load the Qwen3-30B-A3B-GPTQ-Int4 model, and the error occurs during inference. I plan to use PEFT for SFT later on, but currently, even the basic inference script fails to run correctly.

` from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "/mnt/user/ai_00328713/tenant-home_speed/Model/Qwen3/Qwen3-30B-A3B-GPTQ-Int4"

model = AutoModelForCausalLM.from_pretrained(
    model_name,
    device_map="cuda:5"
)
tokenizer = AutoTokenizer.from_pretrained(model_name)


prompt = "Give me a short introduction to large language models."
messages = [
    {"role": "system", "content": "You are Qwen, created by Alibaba Cloud. You are a helpful assistant."},
    {"role": "user", "content": prompt},
]
text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True,
)
model_inputs = tokenizer([text], return_tensors="pt").to(model.device)

generated_ids = model.generate(
    **model_inputs,
    max_new_tokens=512,
)
generated_ids = [
    output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
]

response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0] `


### zhang8473 · 2025-06-12

same error

### ChenRuiwei · 2026-01-26

same error
