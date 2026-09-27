# [Issue #210] How to generate awq quantized model for llava-1.5-7b-hf

source: https://github.com/mit-han-lab/llm-awq/issues/210
state: open | updated: 2024-11-01T11:16:18Z
labels: 

## 正文

I'm trying to quantize llava-1.5 according to the `readme.md` with the following scripts, and tells:`AttributeError: 'LlavaConfig' object has no attribute 'mm_vision_tower'`. 
It seems like the llava model downloaded from [llava-hf/llava-1.5-7b-hf](https://huggingface.co/llava-hf/llava-1.5-7b-hf/tree/main) combines the `llm, vision_tower, mm_projector` into one, instead of in three parts (VILA1.5-3b is this format). What should i do to solve this problems? Looking forward to your replies.

### softwares version
```shell
llm-awq commit-id: dd8e14826c0784ee37dc3a6f7f8253e6f8fc7214
VILA commit-id: 0085724ca3363dc62eaa0d7ef1a30ad20df5c8da
transformers              4.36.2
torch                     2.3.1
```

### script
```shell
model_name=llava-1.5-7b-hf

python -m awq.entry --model_path /data/model/${model_name} \
    --w_bit 4 --q_group_size 128 \
    --run_awq \
    --dump_awq /home/chenxiaotao03/model/awq/awq_cache/${model_name}-w4-g128.pt
```
### detail error logs
```shell
/home/chenxiaotao03/miniconda3/envs/awq/lib/python3.10/site-packages/transformers/utils/generic.py:441: UserWarning: torch.utils._pytree._register_pytree_node is deprecated. Please use torch.utils._pytree.register_pytree_node instead.
  _torch_pytree._register_pytree_node(
/home/chenxiaotao03/miniconda3/envs/awq/lib/python3.10/site-packages/transformers/utils/generic.py:309: UserWarning: torch.utils._pytree._register_pytree_node is deprecated. Please use torch.utils._pytree.register_pytree_node instead.
  _torch_pytree._register_pytree_node(
Quantization config: {'zero_point': True, 'q_group_size': 128}
* Building model /data/model/llava-1.5-7b-hf
Traceback (most recent call last):
  File "/home/chenxiaotao03/Reposities/VILA/llava/model/builder.py", line 252, in prepare_config_for_eval
    config.vision_tower_cfg = config.mm_vision_tower
  File "/home/chenxiaotao03/miniconda3/envs/awq/lib/python3.10/site-packages/transformers/configuration_utils.py", line 265, in __getattribute__
    return super().__getattribute__(key)
AttributeError: 'LlavaConfig' object has no attribute 'mm_vision_tower'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/chenxiaotao03/miniconda3/envs/awq/lib/python3.10/runpy.py", line 196, in _run_module_as_main
    return _run_code(code, main_globals, None,
  File "/home/chenxiaotao03/miniconda3/envs/awq/lib/python3.10/runpy.py", line 86, in _run_code
    exec(code, run_globals)
  File "/home/chenxiaotao03/Reposities/llm-awq/awq/entry.py", line 311, in <module>
    main()
  File "/home/chenxiaotao03/Reposities/llm-awq/awq/entry.py", line 251, in main
    model, enc = build_model_and_enc(args.model_path)
  File "/home/chenxiaotao03/Reposities/llm-awq/awq/entry.py", line 100, in build_model_and_enc
    enc, model, image_processor, context_len = load_pretrained_model(
  File "/home/chenxiaotao03/Reposities/VILA/llava/model/builder.py", line 161, in load_pretrained_model
    prepare_config_for_eval(config, kwargs)
  File "/home/chenxiaotao03/Reposities/VILA/llava/model/builder.py", line 254, in prepare_config_for_eval
    raise ValueError(f"Invalid configuration! Cannot find vision_tower in config:\n{config}")
ValueError: Invalid configuration! Cannot find vision_tower in config:
LlavaConfig {
  "_name_or_path": "/data/model/llava-1.5-7b-hf",
  "architectures": [
    "LlavaForConditionalGeneration"
  ],
  "ignore_index": -100,
  "image_token_index": 32000,
  "model_type": "llava",
  "pad_token_id": 32001,
  "projector_hidden_act": "gelu",
  "resume_path": "/data/model/llava-1.5-7b-hf",
  "text_config": {
    "_name_or_path": "lmsys/vicuna-7b-v1.5",
    "architectures": [
      "LlamaForCausalLM"
    ],
    "max_position_embeddings": 4096,
    "model_type": "llama",
    "rms_norm_eps": 1e-05,
    "torch_dtype": "float16",
    "vocab_size": 32064
  },
  "tie_word_embeddings": false,
  "torch_dtype": "float16",
  "transformers_version": "4.36.2",
  "vision_config": {
    "hidden_size": 1024,
    "image_size": 336,
    "intermediate_size": 4096,
    "model_type": "clip_vision_model",
    "num_attention_heads": 16,
    "num_hidden_layers": 24,
    "patch_size": 14,
    "projection_dim": 768,
    "vocab_size": 32000
  },
  "vision_feature_layer": -2,
  "vision_feature_select_strategy": "default",
  "vocab_size": 32064
}
```


## 评论 (1)

### ShobhaRajanna · 2024-11-01

> I'm trying to quantize llava-1.5 according to the `readme.md` with the following scripts, and tells:`AttributeError: 'LlavaConfig' object has no attribute 'mm_vision_tower'`. It seems like the llava model downloaded from [llava-hf/llava-1.5-7b-hf](https://huggingface.co/llava-hf/llava-1.5-7b-hf/tree/main) combines the `llm, vision_tower, mm_projector` into one, instead of in three parts (VILA1.5-3b is this format). What should i do to solve this problems? Looking forward to your replies.
> 
> ### softwares version
> ```shell
> llm-awq commit-id: dd8e14826c0784ee37dc3a6f7f8253e6f8fc7214
> VILA commit-id: 0085724ca3363dc62eaa0d7ef1a30ad20df5c8da
> transformers              4.36.2
> torch                     2.3.1
> ```
> 
> ### script
> ```shell
> model_name=llava-1.5-7b-hf
> 
> python -m awq.entry --model_path /data/model/${model_name} \
>     --w_bit 4 --q_group_size 128 \
>     --run_awq \
>     --dump_awq /home/chenxiaotao03/model/awq/awq_cache/${model_name}-w4-g128.pt
> ```
> 
> ### detail error logs
> ```shell
> /home/chenxiaotao03/miniconda3/envs/awq/lib/python3.10/site-packages/transformers/utils/generic.py:441: UserWarning: torch.utils._pytree._register_pytree_node is deprecated. Please use torch.utils._pytree.register_pytree_node instead.
>   _torch_pytree._register_pytree_node(
> /home/chenxiaotao03/miniconda3/envs/awq/lib/python3.10/site-packages/transformers/utils/generic.py:309: UserWarning: torch.utils._pytree._register_pytree_node is deprecated. Please use torch.utils._pytree.register_pytree_node instead.
>   _torch_pytree._register_pytree_node(
> Quantization config: {'zero_point': True, 'q_group_size': 128}
> * Building model /data/model/llava-1.5-7b-hf
> Traceback (most recent call last):
>   File "/home/chenxiaotao03/Reposities/VILA/llava/model/builder.py", line 252, in prepare_config_for_eval
>     config.vision_tower_cfg = config.mm_vision_tower
>   File "/home/chenxiaotao03/miniconda3/envs/awq/lib/python3.10/site-packages/transformers/configuration_utils.py", line 265, in __getattribute__
>     return super().__getattribute__(key)
> AttributeError: 'LlavaConfig' object has no attribute 'mm_vision_tower'
> 
> During handling of the above exception, another exception occurred:
> 
> Traceback (most recent call last):
>   File "/home/chenxiaotao03/miniconda3/envs/awq/lib/python3.10/runpy.py", line 196, in _run_module_as_main
>     return _run_code(code, main_globals, None,
>   File "/home/chenxiaotao03/miniconda3/envs/awq/lib/python3.10/runpy.py", line 86, in _run_code
>     exec(code, run_globals)
>   File "/home/chenxiaotao03/Reposities/llm-awq/awq/entry.py", line 311, in <module>
>     main()
>   File "/home/chenxiaotao03/Reposities/llm-awq/awq/entry.py", line 251, in main
>     model, enc = build_model_and_enc(args.model_path)
>   File "/home/chenxiaotao03/Reposities/llm-awq/awq/entry.py", line 100, in build_model_and_enc
>     enc, model, image_processor, context_len = load_pretrained_model(
>   File "/home/chenxiaotao03/Reposities/VILA/llava/model/builder.py", line 161, in load_pretrained_model
>     prepare_config_for_eval(config, kwargs)
>   File "/home/chenxiaotao03/Reposities/VILA/llava/model/builder.py", line 254, in prepare_config_for_eval
>     raise ValueError(f"Invalid configuration! Cannot find vision_tower in config:\n{config}")
> ValueError: Invalid configuration! Cannot find vision_tower in config:
> LlavaConfig {
>   "_name_or_path": "/data/model/llava-1.5-7b-hf",
>   "architectures": [
>     "LlavaForConditionalGeneration"
>   ],
>   "ignore_index": -100,
>   "image_token_index": 32000,
>   "model_type": "llava",
>   "pad_token_id": 32001,
>   "projector_hidden_act": "gelu",
>   "resume_path": "/data/model/llava-1.5-7b-hf",
>   "text_config": {
>     "_name_or_path": "lmsys/vicuna-7b-v1.5",
>     "architectures": [
>       "LlamaForCausalLM"
>     ],
>     "max_position_embeddings": 4096,
>     "model_type": "llama",
>     "rms_norm_eps": 1e-05,
>     "torch_dtype": "float16",
>     "vocab_size": 32064
>   },
>   "tie_word_embeddings": false,
>   "torch_dtype": "float16",
>   "transformers_version": "4.36.2",
>   "vision_config": {
>     "hidden_size": 1024,
>     "image_size": 336,
>     "intermediate_size": 4096,
>     "model_type": "clip_vision_model",
>     "num_attention_heads": 16,
>     "num_hidden_layers": 24,
>     "patch_size": 14,
>     "projection_dim": 768,
>     "vocab_size": 32000
>   },
>   "vision_feature_layer": -2,
>   "vision_feature_select_strategy": "default",
>   "vocab_size": 32064
> }
> ```

have you resolved this?

