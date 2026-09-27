# [Issue #1498] Cannot load pre-quantized Janus Pro 7B

source: https://github.com/bitsandbytes-foundation/bitsandbytes/issues/1498
state: closed | updated: 2026-02-21T20:34:20Z
labels: Bug, Medium Priority, Medium Risk, Model Support

## 正文

### System Info

Windows 11 Home
x64
python 3.11.9

env:
```bash
accelerate==1.3.0
attrdict==2.0.1
bitsandbytes==0.45.1
certifi==2024.12.14
charset-normalizer==3.4.1
colorama==0.4.6
einops==0.8.0
filelock==3.13.1
fsspec==2024.6.1
huggingface-hub==0.28.0
idna==3.10
-e git+https://github.com/deepseek-ai/Janus.git@a74a59f8a9084b78c7760c955037503b9b55b862#egg=janus
Jinja2==3.1.4
MarkupSafe==2.1.5
mpmath==1.3.0
networkx==3.3
numpy==2.1.2
packaging==24.2
pillow==11.0.0
psutil==6.1.1
PyYAML==6.0.2
regex==2024.11.6
requests==2.32.3
safetensors==0.5.2
sentencepiece==0.2.0
six==1.17.0
sympy==1.13.1
timm==1.0.14
tokenizers==0.21.0
torch==2.6.0+cu124
torchaudio==2.6.0+cu124
torchvision==0.21.0+cu124
tqdm==4.67.1
transformers==4.48.1
typing_extensions==4.12.2
urllib3==2.3.0
```


### Reproduction

#### Clone the Janus repo:
https://github.com/deepseek-ai/Janus . The rest of the examples are run from the root of that repo.


#### Download and run quantized model:
```python
from transformers import AutoModelForCausalLM
from janus.models import MultiModalityCausalLM

model_path = "neilmehta24/janus-pro-7b-4bit"

vl_gpt: MultiModalityCausalLM = AutoModelForCausalLM.from_pretrained(
    model_path, trust_remote_code=True
)
```

#### Error:
```
  File "C:\Users\windo\neil\Janus\load_janus_pro.py", line 21, in <module>
    vl_gpt: MultiModalityCausalLM = AutoModelForCausalLM.from_pretrained(
                                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\windo\neil\Janus\.venv\Lib\site-packages\transformers\models\auto\auto_factory.py", line 564, in from_pretrained
    return model_class.from_pretrained(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\windo\neil\Janus\.venv\Lib\site-packages\transformers\modeling_utils.py", line 4224, in from_pretrained
    ) = cls._load_pretrained_model(
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\windo\neil\Janus\.venv\Lib\site-packages\transformers\modeling_utils.py", line 4794, in _load_pretrained_model
    new_error_msgs, offload_index, state_dict_index = _load_state_dict_into_meta_model(
                                                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\windo\neil\Janus\.venv\Lib\site-packages\transformers\modeling_utils.py", line 875, in _load_state_dict_into_meta_model
    hf_quantizer.create_quantized_param(model, param, param_name, param_device, state_dict, unexpected_keys)
  File "C:\Users\windo\neil\Janus\.venv\Lib\site-packages\transformers\quantizers\quantizer_bnb_4bit.py", line 226, in create_quantized_param
    new_value = bnb.nn.Params4bit.from_prequantized(
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\windo\neil\Janus\.venv\Lib\site-packages\bitsandbytes\nn\modules.py", line 280, in from_prequantized
    self.quant_state = QuantState.from_dict(qs_dict=quantized_stats, device=device)
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\windo\neil\Janus\.venv\Lib\site-packages\bitsandbytes\functional.py", line 756, in from_dict
    raise ValueError(
ValueError: There should be exactly one `quant_state` item with ending from ['bitsandbytes__fp4', 'bitsandbytes__nf4'].
Detected ['aligner.layers.0.weight.quant_state.bitsandbytes__fp4', 'gen_aligner.layers.0.weight.quant_state.bitsandbytes__fp4'].

```

#### Here are the keys in qs_dict at the source of the error:
```
dict_keys(['aligner.layers.0.weight.absmax', 'aligner.layers.0.weight.quant_map', 'aligner.layers.0.weight.quant_state.bitsandbytes__fp4', 'gen_aligner.layers.0.weight.absmax', 'gen_aligner.layers.0.weight.quant_map', 'gen_aligner.layers.0.weight.quant_state.bitsandbytes__fp4'])
```

#### For reference, the original config.json:
https://huggingface.co/deepseek-ai/Janus-Pro-7B/blob/main/config.json

#### the quantized config.json:
https://huggingface.co/neilmehta24/janus-pro-7b-4bit/blob/main/config.json

#### the model upload code:
```python
from transformers import AutoModelForCausalLM
from janus.models import MultiModalityCausalLM

model_path = "deepseek-ai/Janus-Pro-7B"

quantization_config = dict(load_in_4bit=True)
vl_gpt: MultiModalityCausalLM = AutoModelForCausalLM.from_pretrained(
    model_path, trust_remote_code=True, quantization_config=quantization_config, torch_dtype="auto"
)
vl_gpt.push_to_hub("janus-pro-7b-4bit")
```

### Notes:
- The model runs just fine when it's quantized without being saved.
- Seems like it's a shortcoming when writing the config file or validating the keys? Especially since the model runs just fine when quantized on-the-fly.

### Expected behavior

I would expect the model to load, since it can load and quantize just fine when it has access to the full weights.

## 评论 (1)

### TimDettmers · 2026-02-21

Closing this issue. The error occurs because the Janus Pro model architecture has multiple independently quantized sub-models (aligner and gen_aligner) whose quant state keys end up in the same dict when saving pre-quantized weights. The `QuantState.from_dict` code expects exactly one quant state suffix per dict, which doesn't hold for this model's structure.

Since the model works correctly when quantized on-the-fly, this is a model-specific serialization edge case rather than a general bitsandbytes bug. If you need to save and reload the quantized model, consider saving/loading the quantized state for each sub-model separately, or using the on-the-fly quantization path.
