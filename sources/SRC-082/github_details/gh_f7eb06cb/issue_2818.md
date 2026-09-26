# [Issue #2818] [BUG] type object 'BACKEND' has no attribute 'EXLLAMA_V1'

source: https://github.com/ModelCloud/GPTQModel/issues/2818
state: closed | updated: 2026-05-06T20:28:37Z
labels: bug

## 正文

On the PEFT nightly CI, one of the GPTQmodel tests is failing because a base GPTQ model cannot be loaded:

```python
from transformers import AutoModelForCausalLM
model_id = "ModelCloud/Llama-3.2-1B-gptqmodel-ci-4bit"
model = AutoModelForCausalLM.from_pretrained(model_id)
```

The error is:

```
  File "/home/name/work/forks/peft/foo.py", line 5, in <module>
    model = AutoModelForCausalLM.from_pretrained(model_id)#, device_map="auto")
  File "/home/name/work/forks/transformers/src/transformers/models/auto/auto_factory.py", line 387, in from_pretrained
    return model_class.from_pretrained(
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~^
        pretrained_model_name_or_path, *model_args, config=config, **hub_kwargs, **kwargs
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/name/work/forks/transformers/src/transformers/modeling_utils.py", line 4184, in from_pretrained
    hf_quantizer.postprocess_model(
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
        model
        ^^^^^
    )  # usually a no-op but sometimes needed, e.g to remove the quant config when dequantizing
    ^
  File "/home/name/work/forks/transformers/src/transformers/quantizers/base.py", line 194, in postprocess_model
    return self._process_model_after_weight_loading(model, **kwargs)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
  File "/home/name/work/forks/transformers/src/transformers/quantizers/quantizer_gptq.py", line 98, in _process_model_after_weight_loading
    model = self.optimum_quantizer.post_init_model(model)
  File "/home/name/anaconda3/envs/peft/lib/python3.13/site-packages/optimum/gptq/quantizer.py", line 672, in post_init_model
    if self.desc_act and self.backend == BACKEND.EXLLAMA_V1 and self.max_input_length is not None:
```

This is with `GPTQmodel==6.0.3` and `torch==2.10.0` on a 4090 GPU.

## 评论 (2)

### Qubitium · 2026-04-23

@BenjaminBossan  Fixing now. Will push PR to `optimum`. This caused by latest gptqmodel dropping (hard deprecating) exallmaa v1 kernel .

### BenjaminBossan · 2026-05-06

Can this issue be closed?
