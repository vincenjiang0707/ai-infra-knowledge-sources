# [Issue #150] Is T5 model supported ?

source: https://github.com/dropbox/hqq/issues/150
state: closed | updated: 2025-04-09T10:57:23Z
labels: 

## 正文

I've created and save quantized version like this:

    quant_config = HqqConfig(nbits=4, group_size=64)

    model = T5EncoderModel.from_pretrained(
        '/storage/Models/FLUX.1-dev/',
        torch_dtype=torch.bfloat16,
        subfolder = "text_encoder_2",

    )

    model.save_pretrained(
        "./quantized_pipeline/",
        safe_serialization=True  # Use safetensors format
    )
    
    
During inference I create flux pipeline:

        text_encoder_2 = T5EncoderModel.from_pretrained(
            self.model_config.path,
            subfolder="text_encoder_2",
            torch_dtype=torch.bfloat16,
            device_map="cuda"
        )


        self.pipeline: FluxPipeline = FluxPipeline.from_pretrained(
            self.model_config.path,
            torch_dtype=torch.bfloat16,
            local_files_only=True,
            text_encoder_2=text_encoder_2
        )    
    
    
    
But when I actually start inference I always get this error:


  File "/home/szwagros/anaconda3/envs/image/lib/python3.11/site-packages/accelerate/hooks.py", line 170, in new_forward
    output = module._old_forward(*args, **kwargs)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/szwagros/anaconda3/envs/image/lib/python3.11/site-packages/transformers/models/t5/modeling_t5.py", line 339, in forward
    forwarded_states = self.DenseReluDense(forwarded_states)
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/szwagros/anaconda3/envs/image/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/szwagros/anaconda3/envs/image/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
    return forward_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/szwagros/anaconda3/envs/image/lib/python3.11/site-packages/accelerate/hooks.py", line 170, in new_forward
    output = module._old_forward(*args, **kwargs)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/szwagros/anaconda3/envs/image/lib/python3.11/site-packages/transformers/models/t5/modeling_t5.py", line 316, in forward
    isinstance(self.wo.weight, torch.Tensor)
               ^^^^^^^^^^^^^^
  File "/home/szwagros/anaconda3/envs/image/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1931, in __getattr__
    raise AttributeError(
AttributeError: 'HQQLinear' object has no attribute 'weight'


Is it because T5 is not supported or am I doing something wrong ?



## 评论 (8)

### mobicham · 2025-02-18

Hi! This is a transformers question since you are using HQQ via the transformers lib, so I don't know exactly what's going on.
Is this happening when you quantize the model on-the-fly too or only when you save and load ?

### szwagros · 2025-02-18

Yes - error shows in both cases: when loading already quantized model and when quantizing it on-the-fly. But you are right that it may be more of an issue in transformers lib. There was similar problem while back with different model - https://github.com/huggingface/transformers/issues/30727.  

### mobicham · 2025-02-18

That fix should have fixed this issue too since it's independent of the model actually. 
Are you fine with loading the whole model on RAM first or you need lazy loading ? 

### szwagros · 2025-02-18

I'm not sure I understand the question :) Do you mean T5 or Flux pipeline ?

### mobicham · 2025-02-18

Are you fine with loading the whole T5 model on cpu first then quantize it to run on the GPU later?

### szwagros · 2025-02-18

Yes I'm fine with that. 

### mobicham · 2025-02-18

Then you can load it on CPU, and quantize the linear layers and dispatch to gpu via `HQQLinear()` and it should work 

### mobicham · 2025-02-18

> Then you can load it on CPU, and quantize the linear layers and dispatch to gpu via `HQQLinear()` and it should work

Something like this:
```Python
def quantize_model(model, quant_config, compute_dtype, device = 'cuda:0'):
    from hqq.core.quantize import HQQLinear, BaseQuantizeConfig

    #Patch
    def _patch_linear(model):
        for name, layer in model.named_children():
            if isinstance(layer, (torch.nn.Linear)):
                layer = HQQLinear(layer, quant_config=quant_config, compute_dtype=compute_dtype, device=device)
                setattr(model, name, layer)
            else:
                _patch_linear(layer)

    _patch_linear(model)

    #Nove the rest to the right device
    model = model.to(device=device, dtype=compute_dtype)

    #Autoname 
    for name, module in model.named_modules():
        module.name = name

quantize_model(model, BaseQuantizeConfig(nbits=4, group_size=64), torch.bfloat16)
```
