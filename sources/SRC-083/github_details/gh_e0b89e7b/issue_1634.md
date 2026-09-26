# [Issue #1634] Can't get llm_int8_skip_modules to work: 'Parameter' object has no attribute 'SCB'

source: https://github.com/bitsandbytes-foundation/bitsandbytes/issues/1634
state: closed | updated: 2026-04-03T15:18:00Z
labels: Bug

## 正文

I'm working with a RecurrentGemma model (alpindale/recurrentgemma-9b-it).
My desired result is quantizing the model to int8, but keeping the recurrent blocks (model.layers.X.temporal_block) unquantized.
Unfortunately setting `llm_int8_skip_modules=["temporal_block"]` doesn't work.
On loading the model, I get `AttributeError: 'Parameter' object has no attribute 'SCB'`.
You can reproduce it with this Colab: https://colab.research.google.com/drive/1NkgcXmuYJg0XqFWMuZA-ZwWDjgdsuCjr
I've also tried `llm_int8_skip_modules=["recurrent"]`, this yields the same error.
Also the library isn't broken; `llm_int8_skip_modules=["lm_head"]` works fine.
My initial thought is that I'm setting the option incorrectly, but I'm not even sure how to find the right setting.
Anyone have any thoughts on how to fix this?

## 评论 (5)

### tongprdn · 2025-07-31

I ran into the same issue while working on Gemma3 model. Trying to skip layers other than llm_head throws the same thing:
`AttributeError: 'Parameter' object has no attribute 'SCB'`


### jiangzihan · 2025-09-01

Me too. Do you know what the reason is and how to solve it?

### BenjaminBossan · 2025-10-20

Bumping this issue. Here is a small reproducer:

```python
from transformers import AutoModelForCausalLM, BitsAndBytesConfig

model_id = "facebook/opt-125m"
quant_config = BitsAndBytesConfig(load_in_8bit=True, llm_int8_skip_modules=["q_proj", "v_proj"])
model = AutoModelForCausalLM.from_pretrained(model_id, quantization_config=quant_config)
```

which results in:

```
Traceback (most recent call last):
  File "/home/name/work/forks/peft/foo.py", line 5, in <module>
    model = AutoModelForCausalLM.from_pretrained(model_id, quantization_config=quant_config)
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/name/work/forks/transformers/src/transformers/models/auto/auto_factory.py", line 385, in from_pretrained
    return model_class.from_pretrained(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/name/work/forks/transformers/src/transformers/modeling_utils.py", line 271, in _wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/home/name/work/forks/transformers/src/transformers/modeling_utils.py", line 4541, in from_pretrained
    accelerate_dispatch(model, hf_quantizer, device_map, offload_folder, offload_index, offload_buffers)
  File "/home/name/work/forks/transformers/src/transformers/integrations/accelerate.py", line 482, in accelerate_dispatch
    dispatch_model(model, **device_map_kwargs)
  File "/home/name/work/forks/accelerate/src/accelerate/big_modeling.py", line 355, in dispatch_model
    check_device_map(model, device_map)
  File "/home/name/work/forks/accelerate/src/accelerate/utils/modeling.py", line 1618, in check_device_map
    all_model_tensors = [name for name, _ in model.state_dict().items()]
                                             ^^^^^^^^^^^^^^^^^^
  File "/home/name/anaconda3/envs/peft/lib/python3.12/site-packages/torch/nn/modules/module.py", line 2260, in state_dict
    module.state_dict(
  File "/home/name/anaconda3/envs/peft/lib/python3.12/site-packages/torch/nn/modules/module.py", line 2257, in state_dict
    self._save_to_state_dict(destination, prefix, keep_vars)
  File "/home/name/anaconda3/envs/peft/lib/python3.12/site-packages/bitsandbytes/nn/modules.py", line 985, in _save_to_state_dict
    param_from_weight = getattr(self.weight, scb_name)
                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AttributeError: 'Parameter' object has no attribute 'SCB'
```

@matthewdouglas

### matthewdouglas · 2025-10-22

Hi all,

It's important to include `lm_head` when providing a custom `llm_int8_skip_modules`, as it won't be added in by default. It's especially important if the weights are tied.

I can reproduce this issue, but also work around it by adding "lm_head" back:

```python
from transformers import AutoModelForCausalLM, BitsAndBytesConfig

model_id = "facebook/opt-125m"
quant_config = BitsAndBytesConfig(load_in_8bit=True, llm_int8_skip_modules=["lm_head", "q_proj", "v_proj"])
model = AutoModelForCausalLM.from_pretrained(model_id, quantization_config=quant_config)
```

It does seem that the error UX needs improvement though. 


### BenjaminBossan · 2025-10-24

Thanks, this works indeed, although I'm not sure why the LM head must be skipped too.

My hope with this was to enable 8bit QLoRA FSDP training by excluding the LoRA target modules from quantization. If those are only a small subset of all layers, there could still be a memory gain compared to non-quantized LoRA. However, there were still int and float params being mixed, resulting in the infamous `Must flatten tensors with uniform dtype` error. For some reason, quantized and non-quantized linear layers always end up in the same shard (it's not even the LoRA layers that are problematic, the same happens without LoRA). I suspect it's caused by the auto-wrap policy, but no matter what policies I tried, it didn't work (could be due to `Trainer` or accelerate, I haven't checked a vanilla training loop).

Anyway, for me this resolves the original issue, I just mention this in case anyone else comes across this.
