# [Issue #2538] [BUG] Offload to disk turtle model not working

source: https://github.com/ModelCloud/GPTQModel/issues/2538
state: closed | updated: 2026-03-18T20:52:29Z
labels: bug

## 正文

**Describe the bug**

I installed the latest main in order to test out quanting the new Qwen models, however when I tested with a known previously working script I had for GLM 4.6, it seems GPTQModel turtle model no longer works. It now attempts to load the whole model in CPU RAM which OOMs. I unfortunately forgot what version I used that worked with GLM4.6 with this script but it was some commit in December.

Also tried with Qwen 3.5 27B and I managed to load it due to having 512GB RAM, it then seems to create the offload folder, but the RAM usage stayed very high.

**GPU Info**

Show output of:

```
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 590.48.01              Driver Version: 590.48.01      CUDA Version: 13.1     |
+-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA RTX PRO 6000 Blac...    Off |   00000000:51:00.0 Off |                  Off |
| 30%   31C    P8             20W /  600W |      15MiB /  97887MiB |      0%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+
|   1  NVIDIA RTX PRO 6000 Blac...    Off |   00000000:C3:00.0 Off |                  Off |
| 30%   34C    P8             15W /  600W |      15MiB /  97887MiB |      0%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+

+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI              PID   Type   Process name                        GPU Memory |
|        ID   ID                                                               Usage      |
|=========================================================================================|
|    0   N/A  N/A          315292      G   /usr/lib/xorg/Xorg                        4MiB |
|    1   N/A  N/A          315292      G   /usr/lib/xorg/Xorg                        4MiB |
+-----------------------------------------------------------------------------------------+
```

**Software Info**

Ubuntu 24.04 Python 3.14t Pytorch 2.10.0 CUDA 12.9.1

Show output of:
```
Using Python 3.14.0 environment at: GPTQModel/.venv
Name: accelerate
Version: 1.13.0
Location: /home/arli/GPTQModel/GPTQModel/.venv/lib/python3.14t/site-packages
Requires: huggingface-hub, numpy, packaging, psutil, pyyaml, safetensors, torch
Required-by: gptqmodel
---
Name: gptqmodel
Version: 5.8.0
Location: /home/arli/GPTQModel/GPTQModel/.venv/lib/python3.14t/site-packages
Requires: accelerate, datasets, defuser, device-smi, dill, huggingface-hub, kernels, logbar, maturin, numpy, packaging, pillow, protobuf, pyarrow, pypcre, safetensors, setuptools, threadpoolctl, tokenicer, torch, torchao, transformers
Required-by:
---
Name: torch
Version: 2.10.0
Location: /home/arli/GPTQModel/GPTQModel/.venv/lib/python3.14t/site-packages
Requires: cuda-bindings, filelock, fsspec, jinja2, networkx, nvidia-cublas-cu12, nvidia-cuda-cupti-cu12, nvidia-cuda-nvrtc-cu12, nvidia-cuda-runtime-cu12, nvidia-cudnn-cu12, nvidia-cufft-cu12, nvidia-cufile-cu12, nvidia-curand-cu12, nvidia-cusolver-cu12, nvidia-cusparse-cu12, nvidia-cusparselt-cu12, nvidia-nccl-cu12, nvidia-nvjitlink-cu12, nvidia-nvshmem-cu12, nvidia-nvtx-cu12, setuptools, sympy, triton, typing-extensions
Required-by: accelerate, gptqmodel, torchvision
---
Name: transformers
Version: 5.3.0
Location: /home/arli/GPTQModel/GPTQModel/.venv/lib/python3.14t/site-packages
Requires: huggingface-hub, numpy, packaging, pyyaml, regex, safetensors, tokenizers, tqdm, typer
Required-by: defuser, gptqmodel
---
Name: triton
Version: 3.6.0
Location: /home/arli/GPTQModel/GPTQModel/.venv/lib/python3.14t/site-packages
Requires:
Required-by: torch
```

**If you are reporting an inference bug of a post-quantized model, please post the content of `config.json` and `quantize_config.json`.**

**To Reproduce**

Use latest main to try and quantize GPTQ, it will not use turtle model offloading.

With PYTHON_GIL=0 running this script:

```
import torch
from datasets import load_dataset
from gptqmodel import GPTQModel, QuantizeConfig
from transformers import AutoTokenizer
import json
import os

MODEL_ID = "/home/arli/models/GLM-4.6-Derestricted-v6"
DATASET_ID = "neuralmagic/LLM_compression_calibration"
DATASET_SPLIT = "train"
NUM_CALIBRATION_SAMPLES = 2048
SAVE_DIR = MODEL_ID + "-GPTQModel-Int4-Int8-Mixed"

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
    bits=4,
    group_size=128,
    sym=True,
    desc_act=False,
)

quant_config.dynamic = {
    r"-:.*embed_tokens.*": {},
    r"-:.*shared_head.*": {},
    r"-:.*shared_experts.*": {},
    r"-:.*lm_head.*": {},
    r"+:model[.]layers[.].*[.]self_attn[.].*": {"bits": 8},
    r"+:model[.]layers[.]([0-3]|89|9[0-2])[.].*": {"bits": 8},
}

model = GPTQModel.load(
    MODEL_ID,
    quantize_config=quant_config,
    trust_remote_code=True
)

model.quantize(
    calibration_dataset
)

model.save(SAVE_DIR)

print("Done!")

```

**Expected behavior**

It should offload model to a offload folder.

**Model/Datasets**

Make sure your model/dataset is downloadable (on HF for example) so we can reproduce your issue.

**Screenshots**

If applicable, add screenshots to help explain your problem.

**Additional context**

Add any other context about the problem here.


## 评论 (10)

### Qubitium · 2026-03-17

@Nero10578 There maybe regressions with offload support on main. Checking. @ZX-ModelCloud 

### ZX-ModelCloud · 2026-03-17

@Nero10578 
As a workaround, you can try using **Transformers v4.57.6**; it might resolve your issue.

### Nero10578 · 2026-03-17

> [@Nero10578](https://github.com/Nero10578) As a workaround, you can try using **Transformers v4.57.6**; it might resolve your issue.

This will work for Qwen 3.5 quantization? I haven't tried because I assumed we needed v5+ for Qwen 3.5. Will try and report back.

Edit: Okay yea it works for GLM 4.6 but not for Qwen 3.5 27B or 122B :( not sure what other framework even allows quantizing Qwen 3.5 at the moment.

Trying to quantize Qwen 3.5 27B eventually OOM on my GPU VRAM even though I have RTX Pro 6000 96GB.

### Qubitium · 2026-03-17

@Nero10578  This is a regression in Transformers 5.3. It is a chicken and egg problem. Qwen 3.5 is only part of 5.3.0 and 5.3.0 has bad cpu memory usage regression. We are working on it. 

### Nero10578 · 2026-03-17

> [@Nero10578](https://github.com/Nero10578) This is a regression in Transformers 5.3. It is a chicken and egg problem. Qwen 3.5 is only part of 5.3.0 and 5.3.0 has bad cpu memory usage regression. We are working on it.

I see yea. I think there were similar regressions with transformers v5 when axolotl upgraded to it. They ended up fixing it, but maybe there is some clue to be had there?

### Nero10578 · 2026-03-17

> [@Nero10578](https://github.com/Nero10578) This is a regression in Transformers 5.3. It is a chicken and egg problem. Qwen 3.5 is only part of 5.3.0 and 5.3.0 has bad cpu memory usage regression. We are working on it.

I think the new fix is broken on non MoE Qwen3.5 models? Defuser 0.11.0 from source doesn't recognize it?

```
Traceback (most recent call last):
  File "/home/arli/GPTQModel-v5/qwen.py", line 37, in <module>
    model = GPTQModel.load(
        MODEL_ID,
        quantize_config=quant_config,
        trust_remote_code=True
    )
  File "/home/arli/GPTQModel-v5/GPTQModel/.venv/lib/python3.14t/site-packages/gptqmodel/models/auto.py", line 386, in load
    m = cls.from_pretrained(
        model_id_or_path=model_id_or_path,
    ...<5 lines>...
        **kwargs,
    )
  File "/home/arli/GPTQModel-v5/GPTQModel/.venv/lib/python3.14t/site-packages/gptqmodel/models/auto.py", line 430, in from_pretrained
    return model_definition.from_pretrained(
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
        pretrained_model_id_or_path=model_id_or_path,
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    ...<3 lines>...
        **model_init_kwargs,
        ^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/arli/GPTQModel-v5/GPTQModel/.venv/lib/python3.14t/site-packages/gptqmodel/models/loader.py", line 175, in from_pretrained
    defuser.replace_fused_blocks(config.model_type)
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/arli/GPTQModel-v5/Defuser/defuser/__init__.py", line 21, in replace_fused_blocks
    return _replace_fused_blocks(*args, **kwargs)
  File "/home/arli/GPTQModel-v5/Defuser/defuser/defuser.py", line 40, in replace_fused_blocks
    cfg = MODEL_CONFIG[model_type]
          ~~~~~~~~~~~~^^^^^^^^^^^^
KeyError: 'qwen3_5'
```

### Qubitium · 2026-03-17

@Nero10578  Update `defuser` now and it should be fixed:

https://github.com/ModelCloud/Defuser/pull/24

pip install -U defuser

### Nero10578 · 2026-03-18

> [@Nero10578](https://github.com/Nero10578) Update `defuser` now and it should be fixed:
> 
> [ModelCloud/Defuser#24](https://github.com/ModelCloud/Defuser/pull/24)
> 
> pip install -U defuser

Can confirm it worked and quanted, however the resulting model seems to be non-runnable in vllm? I checked the config file and it is formatted different to the default Qwen 3.5 config. 

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

Also for GLM 4.6, I seem to have to use transformers 4.57.6 as with the latest transformers I get this error when trying to quant:

```
Traceback (most recent call last):------------------+---------------+---------------+--------------+---------+---------+-------+----------+--------------+-------------+                                       
  File "/home/arli/GPTQModel/final-glm355-quant.py", line 65, in <module>░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░| 0:02:32 / 0:58:16 [4/92] 4.3%
    model.quantize(                                                                                                                                                                                            
    ~~~~~~~~~~~~~~^                                                                                                                                                                                            
        calibration_dataset,                                                                                                                                                                                   
        ^^^^^^^^^^^^^^^^^^^^                                                                                                                                                                                   
    )                                                                                                                                                                                                          
    ^                                                                                                                                                                                                          
  File "/home/arli/GPTQModel/GPTQModel/.venv/lib/python3.14t/site-packages/gptqmodel/models/base.py", line 875, in quantize                                                                                    
    result = module_looper.loop(                                                                                                                                                                               
        backend=backend,                                                                                                                                                                                       
        failsafe=self.quantize_config.failsafe,                                                                                                                                                                
    )                                                                                                                                                                                                          
  File "/home/arli/GPTQModel/GPTQModel/.venv/lib/python3.14t/site-packages/gptqmodel/looper/module_looper.py", line 1395, in loop                                                                              
    return self._loop_impl(failsafe=failsafe, **kwargs)                                                                                                                                                        
           ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^                                                                                                                                                        
  File "/home/arli/GPTQModel/GPTQModel/.venv/lib/python3.14t/site-packages/torch/utils/_contextlib.py", line 124, in decorate_context                                                                          
    return func(*args, **kwargs)                                                                                                                                                                               
  File "/home/arli/GPTQModel/GPTQModel/.venv/lib/python3.14t/site-packages/gptqmodel/looper/module_looper.py", line 1500, in _loop_impl                                                                        
    run_layer_stage(                                                                                                                                                                                           
    ~~~~~~~~~~~~~~~^                                                                                                                                                                                           
        self,                                                                                                                                                                                                  
        ^^^^^                                                                                                                                                                                                  
    ...<9 lines>...                                                                                                                                                                                            
        logger=log,                                                                                                                                                                                            
        ^^^^^^^^^^^                                                                                                                                                                                            
    )                                                                                                                                                                                                          
    ^                                                                                                                                                                                                          
  File "/home/arli/GPTQModel/GPTQModel/.venv/lib/python3.14t/site-packages/gptqmodel/looper/stage_layer.py", line 222, in run_layer_stage                                                                      
    subset_result = run_subset_stage(                                                                                                                                                                          
        looper=looper,                                                                                                                                                                                         
    ...<22 lines>...                                                                                                                                                                                           
        subset_event_cb=looper._subset_event_dispatch,
    )
  File "/home/arli/GPTQModel/GPTQModel/.venv/lib/python3.14t/site-packages/gptqmodel/looper/stage_subset.py", line 686, in run_subset_stage
    processed_results, new_layer_inputs = _run_single_subset_pass(
                                          ~~~~~~~~~~~~~~~~~~~~~~~^
        **common_args,
        ^^^^^^^^^^^^^^
    ...<2 lines>...
        return_outputs=True,
		 )
    ^
  File "/home/arli/GPTQModel/GPTQModel/.venv/lib/python3.14t/site-packages/gptqmodel/looper/stage_subset.py", line 198, in _run_single_subset_pass
    forward_outputs = looper._run_forward_batches(
        module=module,
    ...<17 lines>...
        preserve_module_devices=preserve_devices,
    )
  File "/home/arli/GPTQModel/GPTQModel/.venv/lib/python3.14t/site-packages/gptqmodel/looper/module_looper.py", line 856, in _run_forward_batches
    return self._run_forward_batches_single(
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
        module=module,
        ^^^^^^^^^^^^^^
    ...<16 lines>...
        preserve_module_devices=preserve_module_devices,
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/arli/GPTQModel/GPTQModel/.venv/lib/python3.14t/site-packages/gptqmodel/looper/module_looper.py", line 991, in _run_forward_batches_single
    module_output = module(*layer_input, **additional_inputs)
  File "/home/arli/GPTQModel/GPTQModel/.venv/lib/python3.14t/site-packages/transformers/modeling_layers.py", line 93, in __call__
    return super().__call__(*args, **kwargs)
           ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
  File "/home/arli/GPTQModel/GPTQModel/.venv/lib/python3.14t/site-packages/torch/nn/modules/module.py", line 1776, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
           ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
  File "/home/arli/GPTQModel/GPTQModel/.venv/lib/python3.14t/site-packages/torch/nn/modules/module.py", line 1787, in _call_impl
    return forward_call(*args, **kwargs)
  File "/home/arli/GPTQModel/GPTQModel/.venv/lib/python3.14t/site-packages/transformers/models/glm4_moe/modeling_glm4_moe.py", line 472, in forward
    hidden_states = self.mlp(hidden_states)
  File "/home/arli/GPTQModel/GPTQModel/.venv/lib/python3.14t/site-packages/torch/nn/modules/module.py", line 1776, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
           ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
  File "/home/arli/GPTQModel/GPTQModel/.venv/lib/python3.14t/site-packages/torch/nn/modules/module.py", line 1787, in _call_impl
    return forward_call(*args, **kwargs)
  File "/home/arli/GPTQModel/GPTQModel/.venv/lib/python3.14t/site-packages/defuser/modeling/unfused_moe/glm4_moe.py", line 59, in forward
    topk_indices, topk_weights = self.gate(hidden_states)
    ^^^^^^^^^^^^^^^^^^^^^^^^^^
ValueError: too many values to unpack (expected 2)
```

### Qubitium · 2026-03-18

@Nero10578  Please open new issues. This conversion is no longer applicable to the closed issue. Hard for me to track new issues/regressions. 

### Nero10578 · 2026-03-18

> [@Nero10578](https://github.com/Nero10578) Please open new issues. This conversion is no longer applicable to the closed issue. Hard for me to track new issues/regressions.

Sorry let me do that. 
