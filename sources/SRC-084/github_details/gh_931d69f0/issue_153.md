# [Issue #153] Question with inference.

source: https://github.com/dropbox/hqq/issues/153
state: closed | updated: 2025-03-05T07:29:19Z
labels: 

## 正文

I'm using a code something like this
```
self.model = MiniCPMV.from_pretrained(model_path, trust_remote_code=True, torch_dtype=compute_type, attn_implementation=attn_implementation)
self.processor = MiniCPMVProcessor.from_pretrained(model_path, trust_remote_code=True)

quant_config = BaseQuantizeConfig(nbits=4, group_size=32, axis=0)

AutoHQQHFModel.quantize_model(self.model.llm, quant_config=quant_config, compute_dtype=compute_type, device=self.device)

HQQLinear.set_backend(HQQBackend.ATEN)
# prepare_for_inference(self.model.llm)

self.model.vpm = self.model.vpm.to(device=self.device, dtype=compute_type)
self.model.resampler = self.model.resampler.to(device=self.device, dtype=compute_type)

self.model = self.model.eval()
```

Does this code work properly using ATEN backend for inference? I commented the function `prepare_for_inference` becuase in the description this will use `PYTORCH` backend.

I'm a bit confused that in the README, if I don't use the function `prepare_for_inference` then it is ready for QLoRA not inference. But when use the function then it is ready for `PYTORCH`.  is this right?

## 评论 (2)

### mobicham · 2025-02-28

Do you wanna do QLoRA training or inference or both? 

*  `prepare_for_inference` is to optimize inference runtime with external kernels, it only supports `axis=1`
*  you can do inference with `axis=0` and `ATEN` backend but it's gonna be slow. 
* By default, as long as you don't call `prepare_for_inference` your model is ready for QLoRA training, regardless if it's `PYTORCH` or `ATEN` backend. 

Below you can find a code snippet which should work for both training + be ready for faster inference (+ the possibility to export to VLLM if the architecture is supported)

``` Python
compute_type = torch.bfloat16
self.model = MiniCPMV.from_pretrained(model_path, trust_remote_code=True, torch_dtype=compute_type, attn_implementation=attn_implementation)
self.processor = MiniCPMVProcessor.from_pretrained(model_path, trust_remote_code=True)

quant_config = BaseQuantizeConfig(nbits=4, group_size=64, axis=1)

AutoHQQHFModel.quantize_model(self.model.llm, quant_config=quant_config, compute_dtype=compute_type, device=self.device)
self.model.vpm = self.model.vpm.to(device=self.device, dtype=compute_type)
self.model.resampler = self.model.resampler.to(device=self.device, dtype=compute_type)

HQQLinear.set_backend(HQQBackend.PYTORCH_COMPILE) #Train a bit faster

#If you wanna train: add loras etc.
#PeftUtils.add_lora(self.model.llm, lora_params)

#If you wanna do faster inference
#prepare_for_inference(self.model.llm, backend="torchao_int4") 
```

### 2U1 · 2025-03-05

Sorry for the late response. 

Thanks for the clarity! It helped me a lot.

