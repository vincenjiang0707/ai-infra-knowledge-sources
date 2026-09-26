# [Issue #3489] Orbax to huggingface conversion does not support half precision

source: https://github.com/AI-Hypercomputer/maxtext/issues/3489
state: closed | updated: 2026-04-02T02:32:03Z
labels: bug

## 正文

### Bug report

The old conversion script llama_mistral_mixtral_orbax_to_hf.py saved checkpoints in half precision.

The new checkpoint conversion script to_huggingface.py saves chackpoints in full precision which takes more disk storage space.


### Logs/Output

_No response_

### Environment Information

_No response_

### Additional Context

_No response_

## 评论 (3)

### RissyRan · 2026-03-30

Hi @shuningjin could you help check if your recent changes fix this? 

### shuningjin · 2026-03-31

[PR 3184](https://github.com/AI-Hypercomputer/maxtext/pull/3184) has updated `to_huggingface.py`. We can control the data type for checkpoint using the flag
```
# to_huggingface flag
weight_type=<bfloat16 | float32 (default)| float16>
```

Example command:
```
# to_huggingface
SCANNED_CKPT_PATH=gs://runner-maxtext-logs/to_maxtext_20260329/0/items # input maxtext path
HF_PATH=/tmp/qwen3_hf_20260329  # output HF path
python3 -m maxtext.checkpoint_conversion.to_huggingface \
src/maxtext/configs/base.yml \
model_name=qwen3-0.6b \
scan_layers=true load_parameters_path=$SCANNED_CKPT_PATH \
base_output_directory=$HF_PATH \
skip_jax_distributed_system=true attention=dot_product \
weight_dtype=bfloat16 # specify data type for saving
```

By examining the saved HF safetensor, the data type is set correctly
```
# load HF checkpoint with `safetensors.safe_open`
key | model.embed_tokens.weight | (151936, 1024) | torch.bfloat16 | <class 'torch.dtype'>
key | model.layers.0.input_layernorm.weight | (1024,) | torch.bfloat16 | <class 'torch.dtype'>
key | model.layers.0.mlp.down_proj.weight | (1024, 3072) | torch.bfloat16 | <class 'torch.dtype'>
....
```

@faith-wm: Could you check if this solves your issue? Thanks!

### faith-wm · 2026-04-02

Thanks, this works. 
