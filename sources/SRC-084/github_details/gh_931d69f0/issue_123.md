# [Issue #123] slow loading process of pretrained model for finetuning in transformers

source: https://github.com/dropbox/hqq/issues/123
state: closed | updated: 2024-10-16T11:37:05Z
labels: 

## 正文

Hi, I just meet a problem while loading pretrained model. The time cost is so large. 

Here is some part of my code:

```
from transformers import HqqConfig
quant_config = HqqConfig(nbits=4, group_size=64, quant_zero=False, quant_scle=False, axis=0)
model = transformers.AutoModelForCausalLm.from_pretrained(
       "internlm2-chat-20b",
       trust_remote_code =True,
        quantization_config=quant_config
)
```

when I try to do inference, the loading process is quickly( 2-3 mins),  however, the time cost is so large (about 3-4 hours) during finetuning. I do not find enough docs to learn how use. Would you mind give some suggestions?

## 评论 (4)

### mobicham · 2024-10-14

Hi, sorry I don't understand exactly the problem, what is slow? The model loading or the actual fine-tuning?
- If the model loading is slow, try to limit the number of threads via `OMP_NUM_THREAD = X` where x is the number of your cpu cores.
- If the model fine-tuning is slow, you need to set the right backend for training:
* `axis=0`: use `HQQLinear.set_backend(HQQBackend.ATEN)` but note that there's no efficient kernels for fast inference with `axis=0`
* `axis=1`: use `HQQLinear.set_backend(HQQBackend.PYTORCH_COMPILE)`

### jiaqiw09 · 2024-10-15

thanks your response, it's helful! I just find out the reseaon for time cost in loading. The weights is loaded and quantized in cpu before moved to gpu. While I use "device_map=auto", it seems load and quant processes are done in gpus, which make it faster.

However, it results in  another question. If I want to do ddp training in gpu with transformers, the only way is "HqqConfig", while quant process is done after loading and  it's done in cpu. I can not use device_map as I want to do ddp training. 

Would you mind giving some suggestion? 

Besides, I find following code in instruction is useful and fast, but I want to achieve it all in transformers without importing hqq libs.
```
#Load the model on CPU
from transformers import AutoModelForCausalLM
model = AutoModelForCausalLM.from_pretrained(model_id, torch_dtype=compute_dtype)

#Quantize
from hqq.models.hf.base import AutoHQQHFModel
quant_config = BaseQuantizeConfig(nbits=4, group_size=64) 
AutoHQQHFModel.quantize_model(model, quant_config=quant_config, compute_dtype=compute_dtype, device=device)
```


### mobicham · 2024-10-15

Oh I see, maybe it makes sense to raise this issue in transformers or peft ? Since this repo doesn't implement the transformer based features. 

Normally for both quantizing via the hqq lib or transformers, quantization is done on the gpu not the cpu. The only difference is that in transformers via `HqqConfig` it's first loading each layer to the cpu from disk then dispatching to the gpu and quantization is done on the gpu, while with the hqq lib via `AutoHQQHFModel` it first loads the whole model on cpu then dispatches and quantizes on the GPU. 

So my question is, since you just need to quantize the model first in the beginning, why can't you just quantize the model once and save it via `.save_pretrained` then load it later so you don't have to quantize every time?
Also, why do you need `HqqConfig` again later once you have already quantized the model?

### jiaqiw09 · 2024-10-16

thanks for your suggestion. It helps me a lot.
