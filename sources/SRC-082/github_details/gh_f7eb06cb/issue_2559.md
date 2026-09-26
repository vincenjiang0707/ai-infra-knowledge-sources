# [Issue #2559] [BUG] Qwen3.5 quanting works but unusable model in vllm? Wrong config format?

source: https://github.com/ModelCloud/GPTQModel/issues/2559
state: closed | updated: 2026-04-07T20:50:24Z
labels: bug

## 正文

**Describe the bug**

Can confirm it worked and quanted, however the resulting model seems to be non-runnable in vllm? I checked the config file and it is formatted different to the default Qwen 3.5 config?

```
{
  "architectures": [
    "Qwen3_5ForCausalLM"
  ],
  "attention_bias": false,
  "attention_dropout": 0.0,
  "attn_output_gate": true,
  "bos_token_id": null,
  "dtype": "bfloat16",
  "eos_token_id": 248044,
  "full_attention_interval": 4,
  "head_dim": 256,
  "hidden_act": "silu",
  "hidden_size": 5120,
  "initializer_range": 0.02,
  "intermediate_size": 17408,
  "layer_types": [
    "linear_attention",
    "linear_attention",
    "linear_attention",
    "full_attention",
    "linear_attention",
    "linear_attention",
    "linear_attention",
    "full_attention",
    "linear_attention",
    "linear_attention",
    "linear_attention",
    "full_attention",
    "linear_attention",
    "linear_attention",
    "linear_attention",
    "full_attention",
    "linear_attention",
    "linear_attention",
    "linear_attention",
    "full_attention",
    "linear_attention",
    "linear_attention",
    "linear_attention",
    "full_attention",
    "linear_attention",
    "linear_attention",
    "linear_attention",
    "full_attention",
    "linear_attention",
    "linear_attention",
    "linear_attention",
    "full_attention",
    "linear_attention",
    "linear_attention",
    "linear_attention",
    "full_attention",
    "linear_attention",
    "linear_attention",
    "linear_attention",
    "full_attention",
    "linear_attention",
    "linear_attention",
    "linear_attention",
    "full_attention",
	"linear_attention",
    "linear_attention",
    "linear_attention",
    "full_attention",
    "linear_attention",
    "linear_attention",
    "linear_attention",
    "full_attention",
    "linear_attention",
    "linear_attention",
    "linear_attention",
    "full_attention",
    "linear_attention",
    "linear_attention",
    "linear_attention",
    "full_attention",
    "linear_attention",
    "linear_attention",
    "linear_attention",
    "full_attention"
  ],
  "linear_conv_kernel_dim": 4,
  "linear_key_head_dim": 128,
  "linear_num_key_heads": 16,
  "linear_num_value_heads": 48,
  "linear_value_head_dim": 128,
  "mamba_ssm_dtype": "float32",
  "max_position_embeddings": 262144,
  "mlp_only_layers": [],
  "model_type": "qwen3_5_text",
  "mtp_num_hidden_layers": 1,
  "mtp_use_dedicated_embeddings": false,
  "num_attention_heads": 24,
  "num_hidden_layers": 64,
  "num_key_value_heads": 4,
  "pad_token_id": 248044,
  "partial_rotary_factor": 0.25,
  "quantization_config": {
    "bits": 8,
    "checkpoint_format": "gptq",
    "desc_act": false,
    "format": "gptq",
    "group_size": 128,
    "lm_head": false,
    "meta": {
      "act_group_aware": true,
      "auto_forward_data_parallel": true,
      "damp_auto_increment": 0.01,
      "damp_percent": 0.05,
      "failsafe": {
        "smooth": null,
        "strategy": "rtn",
        "threshold": "0.5%"
      },
      "gc_mode": "interval",
      "gptaq": null,
      "hessian": {
        "chunk_bytes": null,
        "chunk_size": null,
        "staging_dtype": "float32"
      },
	  },
      "mock_quantization": false,
      "mse": 0.0,
      "offload_to_disk": true,
      "offload_to_disk_path": "./gptqmodel_offload/hqdpgrum-rkaakpxx/",
      "pack_impl": "cpu",
      "quantizer": [
        "gptqmodel:5.8.0"
      ],
      "static_groups": false,
      "true_sequential": true,
      "uri": "https://github.com/modelcloud/gptqmodel",
      "vram_strategy": "exclusive",
      "wait_for_submodule_finalizers": false
    },
    "pack_dtype": "int32",
    "quant_method": "gptq",
    "sym": true
  },
  "rms_norm_eps": 1e-06,
  "rope_parameters": {
    "mrope_interleaved": true,
    "mrope_section": [
      11,
      11,
      10
    ],
    "partial_rotary_factor": 0.25,
    "rope_theta": 10000000,
    "rope_type": "default"
  },
  "tie_word_embeddings": false,
  "transformers_version": "5.3.0",
  "use_cache": true,
  "vocab_size": 248320
}
```

**To Reproduce**

Quantize with the following script:

```
import torch
from datasets import load_dataset
from gptqmodel import GPTQModel, QuantizeConfig
from transformers import AutoTokenizer
import json
import os

MODEL_ID = "/home/arli/models/Qwen3.5-27B-Derestricted" 
DATASET_ID = "neuralmagic/LLM_compression_calibration"
DATASET_SPLIT = "train"
NUM_CALIBRATION_SAMPLES = 2048
SAVE_DIR = MODEL_ID + "-GPTQModel-Int8"

tokenizer = AutoTokenizer.from_pretrained(MODEL_ID, trust_remote_code=True)
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
calibration_dataset = [example["text"] for example in ds]

quant_config = QuantizeConfig(
    bits=8,
    group_size=128,
    sym=True,
    desc_act=False
)

print(f"Loading model from {MODEL_ID}...")
model = GPTQModel.load(
    MODEL_ID,
    quantize_config=quant_config,
    trust_remote_code=True
)

print("Starting quantization...")
model.quantize(
    calibration_dataset
)

print(f"Saving model to {SAVE_DIR}...")
model.save(SAVE_DIR)

print("Done!")

```

Run vllm with the command:

```
vllm serve /home/arli/models/Qwen3.5-27B-Derestricted-GPTQ-Int8 --port 8000 \
--tensor-parallel-size 1 \
--max-model-len 32768 --max-num-seqs 32 --gpu-memory-utilization 0.92 \
--reasoning-parser qwen3 --enable-auto-tool-choice --tool-call-parser qwen3_coder \
--served-model-name test \
--mm-encoder-tp-mode data \
--mm-processor-cache-type shm \
--enable-prefix-caching
```

Tried vllm release 0.17.0, latest vllm main and even this PR https://github.com/vllm-project/vllm/pull/37019
Result:
```
(vllm) (base) arli@arli-super-server:~/vllm$ ./test.sh 
(APIServer pid=642117) INFO 03-17 16:31:56 [utils.py:292] 
(APIServer pid=642117) INFO 03-17 16:31:56 [utils.py:292]        █     █     █▄   ▄█
(APIServer pid=642117) INFO 03-17 16:31:56 [utils.py:292]  ▄▄ ▄█ █     █     █ ▀▄▀ █  version 0.17.0rc1.dev201+g6bbd67824
(APIServer pid=642117) INFO 03-17 16:31:56 [utils.py:292]   █▄█▀ █     █     █     █  model   /home/arli/models/Qwen3.5-27B-Derestricted-GPTQModel-Int8
(APIServer pid=642117) INFO 03-17 16:31:56 [utils.py:292]    ▀▀  ▀▀▀▀▀ ▀▀▀▀▀ ▀     ▀
(APIServer pid=642117) INFO 03-17 16:31:56 [utils.py:292] 
(APIServer pid=642117) INFO 03-17 16:31:56 [utils.py:228] non-default args: {'model_tag': '/home/arli/models/Qwen3.5-27B-Derestricted-GPTQModel-Int8', 'enable_auto_tool_choice': True, 'tool_call_parser': 'qwen3_coder', 'model': '/home/arli/models/Qwen3.5-27B-Derestricted-GPTQModel-Int8', 'max_model_len': 131072, 'served_model_name': ['test'], 'reasoning_parser': 'qwen3', 'tensor_parallel_size': 2, 'gpu_memory_utilization': 0.92, 'enable_prefix_caching': True, 'mm_processor_cache_type': 'shm', 'mm_encoder_tp_mode': 'data', 'max_num_seqs': 24}
(APIServer pid=642117) Unrecognized keys in `rope_parameters` for 'rope_type'='default': {'mrope_section', 'mrope_interleaved'}
(APIServer pid=642117) Unrecognized keys in `rope_parameters` for 'rope_type'='default': {'mrope_section', 'mrope_interleaved'}
(APIServer pid=642117) INFO 03-17 16:31:56 [model.py:531] Resolved architecture: Qwen3_5ForCausalLM
(APIServer pid=642117) INFO 03-17 16:31:56 [model.py:1554] Using max model len 131072
(APIServer pid=642117) INFO 03-17 16:31:56 [gptq_marlin.py:229] The model is convertible to gptq_marlin during runtime. Using gptq_marlin kernel.
(APIServer pid=642117) INFO 03-17 16:31:56 [scheduler.py:231] Chunked prefill is enabled with max_num_batched_tokens=8192.
(APIServer pid=642117) WARNING 03-17 16:31:56 [config.py:384] Mamba cache mode is set to 'align' for Qwen3_5ForCausalLM by default when prefix caching is enabled
(APIServer pid=642117) INFO 03-17 16:31:56 [config.py:404] Warning: Prefix caching in Mamba cache 'align' mode is currently enabled. Its support for Mamba layers is experimental. Please report any issues you may observe.
(APIServer pid=642117) INFO 03-17 16:31:56 [config.py:224] Setting attention block size to 400 tokens to ensure that attention page size is >= mamba page size.
(APIServer pid=642117) INFO 03-17 16:31:56 [config.py:255] Padding mamba page size by 0.25% to ensure that mamba page size and attention page size are exactly equal.
(APIServer pid=642117) INFO 03-17 16:31:56 [vllm.py:754] Asynchronous scheduling is enabled.
(APIServer pid=642117) Traceback (most recent call last):
(APIServer pid=642117)   File "/home/arli/vllm-main/vllm/.venv/bin/vllm", line 10, in <module>
(APIServer pid=642117)     sys.exit(main())
(APIServer pid=642117)              ^^^^^^
(APIServer pid=642117)   File "/home/arli/vllm-main/vllm/vllm/entrypoints/cli/main.py", line 75, in main
(APIServer pid=642117)     args.dispatch_function(args)
(APIServer pid=642117)   File "/home/arli/vllm-main/vllm/vllm/entrypoints/cli/serve.py", line 113, in cmd
(APIServer pid=642117)     uvloop.run(run_server(args))
(APIServer pid=642117)   File "/home/arli/vllm-main/vllm/.venv/lib/python3.12/site-packages/uvloop/__init__.py", line 96, in run
(APIServer pid=642117)     return __asyncio.run(
(APIServer pid=642117)            ^^^^^^^^^^^^^^
(APIServer pid=642117)   File "/usr/lib/python3.12/asyncio/runners.py", line 194, in run
(APIServer pid=642117)     return runner.run(main)
(APIServer pid=642117)            ^^^^^^^^^^^^^^^^
(APIServer pid=642117)   File "/usr/lib/python3.12/asyncio/runners.py", line 118, in run
(APIServer pid=642117)     return self._loop.run_until_complete(task)
(APIServer pid=642117)            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=642117)   File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
(APIServer pid=642117)   File "/home/arli/vllm-main/vllm/.venv/lib/python3.12/site-packages/uvloop/__init__.py", line 48, in wrapper
(APIServer pid=642117)     return await main
(APIServer pid=642117)            ^^^^^^^^^^
(APIServer pid=642117)   File "/home/arli/vllm-main/vllm/vllm/entrypoints/openai/api_server.py", line 642, in run_server
(APIServer pid=642117)     await run_server_worker(listen_address, sock, args, **uvicorn_kwargs)
(APIServer pid=642117)   File "/home/arli/vllm-main/vllm/vllm/entrypoints/openai/api_server.py", line 656, in run_server_worker
(APIServer pid=642117)     async with build_async_engine_client(
(APIServer pid=642117)   File "/usr/lib/python3.12/contextlib.py", line 210, in __aenter__
(APIServer pid=642117)     return await anext(self.gen)
(APIServer pid=642117)            ^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=642117)   File "/home/arli/vllm-main/vllm/vllm/entrypoints/openai/api_server.py", line 101, in build_async_engine_client
(APIServer pid=642117)     async with build_async_engine_client_from_engine_args(
(APIServer pid=642117)   File "/usr/lib/python3.12/contextlib.py", line 210, in __aenter__
(APIServer pid=642117)     return await anext(self.gen)
(APIServer pid=642117)            ^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=642117)   File "/home/arli/vllm-main/vllm/vllm/entrypoints/openai/api_server.py", line 142, in build_async_engine_client_from_engine_args
(APIServer pid=642117)     async_llm = AsyncLLM.from_vllm_config(
(APIServer pid=642117)                 ^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=642117)   File "/home/arli/vllm-main/vllm/vllm/v1/engine/async_llm.py", line 225, in from_vllm_config
(APIServer pid=642117)     return cls(
(APIServer pid=642117)            ^^^^
(APIServer pid=642117)   File "/home/arli/vllm-main/vllm/vllm/v1/engine/async_llm.py", line 135, in __init__
(APIServer pid=642117)     self.renderer = renderer = renderer_from_config(self.vllm_config)
(APIServer pid=642117)                                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=642117)   File "/home/arli/vllm-main/vllm/vllm/renderers/registry.py", line 89, in renderer_from_config
(APIServer pid=642117)     return RENDERER_REGISTRY.load_renderer(
(APIServer pid=642117)            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=642117)   File "/home/arli/vllm-main/vllm/vllm/renderers/registry.py", line 63, in load_renderer
(APIServer pid=642117)     return renderer_cls.from_config(config, tokenizer_kwargs)
(APIServer pid=642117)            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=642117)   File "/home/arli/vllm-main/vllm/vllm/renderers/hf.py", line 607, in from_config
(APIServer pid=642117)     return cls(config, tokenizer)
(APIServer pid=642117)            ^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=642117)   File "/home/arli/vllm-main/vllm/vllm/renderers/hf.py", line 614, in __init__
(APIServer pid=642117)     super().__init__(config, tokenizer)
(APIServer pid=642117)   File "/home/arli/vllm-main/vllm/vllm/renderers/base.py", line 94, in __init__
(APIServer pid=642117)     self.mm_processor = mm_registry.create_processor(
(APIServer pid=642117)                         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=642117)   File "/home/arli/vllm-main/vllm/vllm/multimodal/registry.py", line 214, in create_processor
(APIServer pid=642117)     return factories.build_processor(ctx, cache=cache)
(APIServer pid=642117)            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=642117)   File "/home/arli/vllm-main/vllm/vllm/multimodal/registry.py", line 95, in build_processor
(APIServer pid=642117)     return self.processor(info, dummy_inputs_builder, cache=cache)
(APIServer pid=642117)            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=642117)   File "/home/arli/vllm-main/vllm/vllm/multimodal/processing/processor.py", line 989, in __init__
(APIServer pid=642117)     self.data_parser = self.info.get_data_parser()
(APIServer pid=642117)                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=642117)   File "/home/arli/vllm-main/vllm/vllm/model_executor/models/qwen3_vl.py", line 643, in get_data_parser
(APIServer pid=642117)     self.get_hf_config().vision_config.spatial_merge_size,
(APIServer pid=642117)     ^^^^^^^^^^^^^^^^^^^^
(APIServer pid=642117)   File "/home/arli/vllm-main/vllm/vllm/model_executor/models/qwen3_5.py", line 114, in get_hf_config
(APIServer pid=642117)     return self.ctx.get_hf_config(Qwen3_5Config)
(APIServer pid=642117)            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=642117)   File "/home/arli/vllm-main/vllm/vllm/multimodal/processing/context.py", line 139, in get_hf_config
(APIServer pid=642117)     raise TypeError(
(APIServer pid=642117) TypeError: Invalid type of HuggingFace config. Expected type: <class 'vllm.transformers_utils.configs.qwen3_5.Qwen3_5Config'>, but found type: <class 'transformers.models.qwen3_5.configuration_qwen3_5.Qwen3_5TextConfig'>
```

**Expected behavior**

Quanted model should run in vllm just fine.

**Model/Datasets**

[Quanted model](https://huggingface.co/OwenArli/broken-quant-GPTQModel)

## 评论 (19)

### Nero10578 · 2026-03-18

Does GPTQModel somehow strip away the vision parts of the model?

### arkerwu · 2026-03-19

same issue

### Qubitium · 2026-03-19

@Nero10578  You need to isolate `vllm` out-of-the-picture first. Does the quantized model inference correclty with `gptqmodel`?


### arkerwu · 2026-03-19

> [@Nero10578](https://github.com/Nero10578) You need to isolate `vllm` out-of-the-picture first. Does the quantized model inference correclty with `gptqmodel`?

It works with gptqmodel for inference, but not with vllm.

### Qubitium · 2026-03-19

@arkerwu @arkerwu  Output the original model `config.json`. and the quantized model's `config.json`.  do a `diff` and post the diff here. 

### Nero10578 · 2026-03-19

I have never done a diff in a github comment, is it just doing this? Seems to me quanting it turns it into text only model which vllm does not expect.

```diff
-  "architectures": ["Qwen3_5ForConditionalGeneration"],
+  "architectures": ["Qwen3_5ForCausalLM"],
-  "model_type": "qwen3_5",
+  "model_type": "qwen3_5_text",

-  "image_token_id": 248056,
-  "video_token_id": 248057,
-  "vision_end_token_id": 248054,
-  "vision_start_token_id": 248053,
-  "vision_config": { ... },

+  "bos_token_id": null,
+  "pad_token_id": 248044,
+  "quantization_config": {
+    "bits": 8,
+    "checkpoint_format": "gptq",
+    "quant_method": "gptq",
+    ...
+  },

-  "transformers_version": "4.57.0.dev0",
+  "transformers_version": "5.3.0",
```


Original model config.json:

```
{
    "architectures": [
        "Qwen3_5ForConditionalGeneration"
    ],
    "image_token_id": 248056,
    "model_type": "qwen3_5",
    "text_config": {
        "attention_bias": false,
        "attention_dropout": 0.0,
        "attn_output_gate": true,
        "dtype": "bfloat16",
        "eos_token_id": 248044,
        "full_attention_interval": 4,
        "head_dim": 256,
        "hidden_act": "silu",
        "hidden_size": 5120,
        "initializer_range": 0.02,
        "intermediate_size": 17408,
        "layer_types": [
            "linear_attention",
            "linear_attention",
            "linear_attention",
            "full_attention",
            "linear_attention",
            "linear_attention",
            "linear_attention",
            "full_attention",
            "linear_attention",
            "linear_attention",
            "linear_attention",
            "full_attention",
            "linear_attention",
            "linear_attention",
            "linear_attention",
            "full_attention",
            "linear_attention",
            "linear_attention",
            "linear_attention",
            "full_attention",
            "linear_attention",
            "linear_attention",
            "linear_attention",
            "full_attention",
            "linear_attention",
            "linear_attention",
            "linear_attention",
            "full_attention",
            "linear_attention",
            "linear_attention",
            "linear_attention",
            "full_attention",
            "linear_attention",
            "linear_attention",
            "linear_attention",
            "full_attention",
            "linear_attention",
            "linear_attention",
            "linear_attention",
            "full_attention",
            "linear_attention",
            "linear_attention",
            "linear_attention",
            "full_attention",
            "linear_attention",
            "linear_attention",
            "linear_attention",
            "full_attention",
            "linear_attention",
            "linear_attention",
            "linear_attention",
            "full_attention",
            "linear_attention",
            "linear_attention",
            "linear_attention",
            "full_attention",
            "linear_attention",
            "linear_attention",
            "linear_attention",
            "full_attention",
            "linear_attention",
            "linear_attention",
            "linear_attention",
            "full_attention"
        ],
        "linear_conv_kernel_dim": 4,
        "linear_key_head_dim": 128,
        "linear_num_key_heads": 16,
        "linear_num_value_heads": 48,
        "linear_value_head_dim": 128,
        "max_position_embeddings": 262144,
        "mlp_only_layers": [],
        "model_type": "qwen3_5_text",
        "mtp_num_hidden_layers": 1,
        "mtp_use_dedicated_embeddings": false,
        "num_attention_heads": 24,
        "num_hidden_layers": 64,
        "num_key_value_heads": 4,
        "rms_norm_eps": 1e-06,
        "use_cache": true,
        "vocab_size": 248320,
        "mamba_ssm_dtype": "float32",
        "rope_parameters": {
            "mrope_interleaved": true,
            "mrope_section": [
                11,
                11,
                10
            ],
            "rope_type": "default",
            "rope_theta": 10000000,
            "partial_rotary_factor": 0.25
        }
    },
    "tie_word_embeddings": false,
    "transformers_version": "4.57.0.dev0",
    "video_token_id": 248057,
    "vision_config": {
        "deepstack_visual_indexes": [],
        "depth": 27,
        "hidden_act": "gelu_pytorch_tanh",
        "hidden_size": 1152,
        "in_channels": 3,
        "initializer_range": 0.02,
        "intermediate_size": 4304,
        "model_type": "qwen3_5",
        "num_heads": 16,
        "num_position_embeddings": 2304,
        "out_hidden_size": 5120,
        "patch_size": 16,
        "spatial_merge_size": 2,
        "temporal_patch_size": 2
    },
    "vision_end_token_id": 248054,
    "vision_start_token_id": 248053
}
```

Quanted model config.json:
```
{
  "architectures": [
    "Qwen3_5ForCausalLM"
  ],
  "attention_bias": false,
  "attention_dropout": 0.0,
  "attn_output_gate": true,
  "bos_token_id": null,
  "dtype": "bfloat16",
  "eos_token_id": 248044,
  "full_attention_interval": 4,
  "head_dim": 256,
  "hidden_act": "silu",
  "hidden_size": 5120,
  "initializer_range": 0.02,
  "intermediate_size": 17408,
  "layer_types": [
    "linear_attention",
    "linear_attention",
    "linear_attention",
    "full_attention",
    "linear_attention",
    "linear_attention",
    "linear_attention",
    "full_attention",
    "linear_attention",
    "linear_attention",
    "linear_attention",
    "full_attention",
    "linear_attention",
    "linear_attention",
    "linear_attention",
    "full_attention",
    "linear_attention",
    "linear_attention",
    "linear_attention",
    "full_attention",
    "linear_attention",
    "linear_attention",
    "linear_attention",
    "full_attention",
    "linear_attention",
    "linear_attention",
    "linear_attention",
    "full_attention",
    "linear_attention",
    "linear_attention",
    "linear_attention",
    "full_attention",
    "linear_attention",
    "linear_attention",
    "linear_attention",
    "full_attention",
    "linear_attention",
    "linear_attention",
    "linear_attention",
    "full_attention",
    "linear_attention",
    "linear_attention",
    "linear_attention",
    "full_attention",
    "linear_attention",
    "linear_attention",
    "linear_attention",
    "full_attention",
    "linear_attention",
    "linear_attention",
    "linear_attention",
    "full_attention",
    "linear_attention",
    "linear_attention",
    "linear_attention",
    "full_attention",
    "linear_attention",
    "linear_attention",
    "linear_attention",
    "full_attention",
    "linear_attention",
    "linear_attention",
    "linear_attention",
    "full_attention"
  ],
  "linear_conv_kernel_dim": 4,
  "linear_key_head_dim": 128,
  "linear_num_key_heads": 16,
  "linear_num_value_heads": 48,
  "linear_value_head_dim": 128,
  "mamba_ssm_dtype": "float32",
  "max_position_embeddings": 262144,
  "mlp_only_layers": [],
  "model_type": "qwen3_5_text",
  "mtp_num_hidden_layers": 1,
  "mtp_use_dedicated_embeddings": false,
  "num_attention_heads": 24,
  "num_hidden_layers": 64,
  "num_key_value_heads": 4,
  "pad_token_id": 248044,
  "partial_rotary_factor": 0.25,
  "quantization_config": {
    "bits": 8,
    "checkpoint_format": "gptq",
    "desc_act": false,
    "format": "gptq",
    "group_size": 128,
    "lm_head": false,
    "meta": {
      "act_group_aware": true,
      "auto_forward_data_parallel": true,
      "damp_auto_increment": 0.01,
      "damp_percent": 0.05,
      "failsafe": {
        "smooth": null,
        "strategy": "rtn",
        "threshold": "0.5%"
      },
      "gc_mode": "interval",
      "gptaq": null,
      "hessian": {
        "chunk_bytes": null,
        "chunk_size": null,
        "staging_dtype": "float32"
      },
      "mock_quantization": false,
      "mse": 0.0,
      "offload_to_disk": true,
      "offload_to_disk_path": "./gptqmodel_offload/hqdpgrum-rkaakpxx/",
      "pack_impl": "cpu",
      "quantizer": [
        "gptqmodel:5.8.0"
      ],
      "static_groups": false,
      "true_sequential": true,
      "uri": "https://github.com/modelcloud/gptqmodel",
      "vram_strategy": "exclusive",
      "wait_for_submodule_finalizers": false
    },
    "pack_dtype": "int32",
    "quant_method": "gptq",
    "sym": true
  },
  "rms_norm_eps": 1e-06,
  "rope_parameters": {
    "mrope_interleaved": true,
    "mrope_section": [
      11,
      11,
      10
    ],
    "partial_rotary_factor": 0.25,
    "rope_theta": 10000000,
    "rope_type": "default"
  },
  "tie_word_embeddings": false,
  "transformers_version": "5.3.0",
  "use_cache": true,
  "vocab_size": 248320
}
```



### Qubitium · 2026-03-19

@Nero10578  What is this model on HF exactly? `Qwen3.5-27B-Derestricted`. Do you have hf link to the model and the actual base model this modfiied model is based on?


### Nero10578 · 2026-03-19

> [@Nero10578](https://github.com/Nero10578) What is this model on HF exactly? `Qwen3.5-27B-Derestricted`. Do you have hf link to the model and the actual base model this modfiied model is based on?

Oh this is my model here: https://huggingface.co/ArliAI/Qwen3.5-27B-Derestricted

Base model is Qwen3.5 27B but its the same effect because I only modify the weights for abliteration.

### arkerwu · 2026-03-19

[Qwen3.5-27B config](https://huggingface.co/Qwen/Qwen3.5-27B/blob/main/config.json)
Quanted model config.json:
{
  "architectures": [
    "Qwen3_5ForCausalLM"
  ],
  "attention_bias": false,
  "attention_dropout": 0.0,
  "attn_output_gate": true,
  "bos_token_id": null,
  "dtype": "float16",
  "eos_token_id": 248044,
  "full_attention_interval": 4,
  "head_dim": 256,
  "hidden_act": "silu",
  "hidden_size": 5120,
  "initializer_range": 0.02,
  "intermediate_size": 17408,
  "layer_types": [
    "linear_attention",
    "linear_attention",
    "linear_attention",
    "full_attention",
    "linear_attention",
    "linear_attention",
    "linear_attention",
    "full_attention",
    "linear_attention",
    "linear_attention",
    "linear_attention",
    "full_attention",
    "linear_attention",
    "linear_attention",
    "linear_attention",
    "full_attention",
    "linear_attention",
    "linear_attention",
    "linear_attention",
    "full_attention",
    "linear_attention",
    "linear_attention",
    "linear_attention",
    "full_attention",
    "linear_attention",
    "linear_attention",
    "linear_attention",
    "full_attention",
    "linear_attention",
    "linear_attention",
    "linear_attention",
    "full_attention",
    "linear_attention",
    "linear_attention",
    "linear_attention",
    "full_attention",
    "linear_attention",
    "linear_attention",
    "linear_attention",
    "full_attention",
    "linear_attention",
    "linear_attention",
    "linear_attention",
    "full_attention",
    "linear_attention",
    "linear_attention",
    "linear_attention",
    "full_attention",
    "linear_attention",
    "linear_attention",
    "linear_attention",
    "full_attention",
    "linear_attention",
    "linear_attention",
    "linear_attention",
    "full_attention",
    "linear_attention",
    "linear_attention",
    "linear_attention",
    "full_attention",
    "linear_attention",
    "linear_attention",
    "linear_attention",
    "full_attention"
  ],
  "linear_conv_kernel_dim": 4,
  "linear_key_head_dim": 128,
  "linear_num_key_heads": 16,
  "linear_num_value_heads": 48,
  "linear_value_head_dim": 128,
  "mamba_ssm_dtype": "float32",
  "max_position_embeddings": 262144,
  "mlp_only_layers": [],
  "model_type": "qwen3_5_text",
  "mtp_num_hidden_layers": 1,
  "mtp_use_dedicated_embeddings": false,
  "num_attention_heads": 24,
  "num_hidden_layers": 64,
  "num_key_value_heads": 4,
  "pad_token_id": 248044,
  "partial_rotary_factor": 0.25,
  "quantization_config": {
    "bits": 4,
    "checkpoint_format": "gptq",
    "desc_act": false,
    "format": "gptq",
    "group_size": 128,
    "lm_head": false,
    "meta": {
      "act_group_aware": true,
      "auto_forward_data_parallel": true,
      "damp_auto_increment": 0.01,
      "damp_percent": 0.05,
      "failsafe": {
        "smooth": null,
        "strategy": "rtn",
        "threshold": "0.5%"
      },
      "gc_mode": "interval",
      "gptaq": null,
      "hessian": {
        "chunk_bytes": null,
        "chunk_size": null,
        "staging_dtype": "float32"
      },
      "mock_quantization": false,
      "mse": 0.0,
      "offload_to_disk": true,
      "offload_to_disk_path": "./gptqmodel_offload/wopltmtn-ryqqkieq/",
      "pack_impl": "cpu",
      "quantizer": [
        "gptqmodel:5.8.0"
      ],
      "static_groups": false,
      "true_sequential": true,
      "uri": "https://github.com/modelcloud/gptqmodel",
      "vram_strategy": "exclusive",
      "wait_for_submodule_finalizers": false
    },
    "pack_dtype": "int32",
    "quant_method": "gptq",
    "sym": true
  },
  "rms_norm_eps": 1e-06,
  "rope_parameters": {
    "mrope_interleaved": true,
    "mrope_section": [
      11,
      11,
      10
    ],
    "partial_rotary_factor": 0.25,
    "rope_theta": 10000000,
    "rope_type": "default"
  },
  "tie_word_embeddings": false,
  "transformers_version": "5.3.0",
  "use_cache": true,
  "vocab_size": 248320
}


### arkerwu · 2026-03-19

I tried the official Qwen3.5-9B and 27B, and the results were the same; the quantized config file structure is different from the original version.

### ZX-ModelCloud · 2026-03-23

Please use the latest code and try again, [PR#2588](https://github.com/ModelCloud/GPTQModel/pull/2588) fixes the vLLM loading issue.

### djaffer · 2026-04-07

Qwen3_5ForCausalLM is not right value it adds in config I think it should be the Qwen3_5ForConditionalGeneration. I see on other GPTQ that are there.

### Qubitium · 2026-04-07

@ZX-ModelCloud 

### ZX-ModelCloud · 2026-04-07

> Qwen3_5ForCausalLM is not right value it adds in config I think it should be the Qwen3_5ForConditionalGeneration. I see on other GPTQ that are there.

This issue has been fixed. Please install the latest version of GPTQModel, or install it directly from the latest source code.

### djaffer · 2026-04-07

```
from datasets import load_dataset
from gptqmodel import GPTQModel, QuantizeConfig
from transformers import AutoTokenizer

model_id = "Qwen/Qwen3.5-4b"
quant_path = "./quantized/qwen3.5-4b-gptq-4bit"

# 1. Initialize Tokenizer (This was missing!)
print("Loading tokenizer...")
tokenizer = AutoTokenizer.from_pretrained(model_id, use_fast=True)

# 2. Load and Prepare Calibration Data
print("Loading calibration data...")
raw_data = load_dataset(
    "allenai/c4",
    data_files="en/c4-train.00001-of-01024.json.gz",
    split="train"
).select(range(256))["text"]

# Quantization requires tokenized data (tensors), not raw text strings
print("Tokenizing calibration data...")


# 3. Setup Quantization Config
quant_config = QuantizeConfig(
bits=4,
group_size=128,
sym=True,
desc_act=False,
)

# 4. Load Unquantized Model
print("Loading unquantized model into memory...")
model = GPTQModel.load(model_id, quantize_config=quant_config,trust_remote_code=True,
)

calibration_data = []
for text in raw_data:
    encoded = tokenizer(text, return_tensors="pt")
    
    # We cast it to a plain dictionary to bypass the BatchEncoding type error
    calibration_data.append({
        "input_ids": encoded["input_ids"],
        "attention_mask": encoded["attention_mask"]
    })
model.quantize(calibration_data, batch_size=2)

```

Quantizing self_attn.q_proj in layer ['p' to ||]        [3 of 31] | 0:13:45 / 

RuntimeError                              Traceback (most recent call last)
Cell In[5], [line 1](vscode-notebook-cell:?execution_count=5&line=1)
----> [1](vscode-notebook-cell:?execution_count=5&line=1) model.quantize(calibration_data, batch_size=2)
      2 print("Quantization complete. Saving quantized model...")

File /anaconda/envs/azureml_py310_sdkv2/lib/python3.10/site-packages/gptqmodel/models/base.py:843, in BaseQModel.quantize(self, calibration, calibration_concat_size, calibration_sort, batch_size, tokenizer, backend, adapter, adapter_calibration_dataset, calibration_data_min_length, calibration_concat_separator)
    839     if calibration is None:
    840         raise ValueError(
    841             "Calibration dataset is required unless a weight-only quantize config is configured."
    842         )
--> [843](https://vscode-remote+amlext-002b-002fsubscriptions-002f00728089-002d1f0e-002d420a-002d8637-002d5749015bdc93-002fresourcegroups-002fct-002deast-002fproviders-002fmicrosoft-002emachinelearningservices-002fworkspaces-002fdanish-002d4201-002fcomputes-002fcttraning.vscode-resource.vscode-cdn.net/anaconda/envs/azureml_py310_sdkv2/lib/python3.10/site-packages/gptqmodel/models/base.py:843)     result = self._quantize_with_calibration(
    844         calibration=calibration,
    845         calibration_concat_size=calibration_concat_size,
    846         calibration_sort=calibration_sort,
    847         batch_size=batch_size,
    848         backend=backend,
    849         adapter_calibration_dataset=adapter_calibration_dataset,
    850         calibration_concat_separator=calibration_concat_separator,
    851     )
    853 timer = getattr(self, "quant_region_timer", None)
    854 if timer is not None:

File /anaconda/envs/azureml_py310_sdkv2/lib/python3.10/site-packages/gptqmodel/models/base.py:1003, in BaseQModel._quantize_with_calibration(self, calibration, calibration_concat_size, calibration_sort, batch_size, backend, adapter_calibration_dataset, calibration_concat_separator)
    996 gc_context = (
...
    101 )
    102 attn_output = attn_output.transpose(1, 2).contiguous()
    104 return attn_output, None

RuntimeError: The size of tensor a (7921) must match the size of tensor b (2) at non-singleton dimension 2

### Qubitium · 2026-04-07

@djaffer  Show me your `git log` for gptqmodel `main` and `pip show gptqmodel` so we can confirm what commit/version you have. 

### djaffer · 2026-04-07

Im using from pip. It is a notebook. Why do you need git log.

### Qubitium · 2026-04-07

@djaffer  Because the fix for this bug is fixed on `main` branch not pypi release. 

### djaffer · 2026-04-07

Well that's is the issue then. It said 2 days ago so i thought it got in. I will wait for you to release the package. Please just update here.
