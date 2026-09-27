# [Issue #175] skip_modules in HQQConfig doesn't skip quantizing modules

source: https://github.com/dropbox/hqq/issues/175
state: closed | updated: 2026-03-18T20:58:07Z
labels: 

## 正文

Hi,

I am trying to use HQQ Config to quantize a pythia-410m model. I want to specifically not quantize the MLP modules in it.. I am using the HQQConfig implementation in the transformers library as follows:

    skip_mods = ["dense_h_to_4h","dense_4h_to_h"]
    print(skip_mods)
    quant_config = HqqConfig(nbits=8, skip_modules = skip_mods)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        quantization_config=quant_config,
        device_map=device,
        dtype=torch.float16
    )

However, it still quantizes the MLP modules when I print the model. 

Here's the printed model after quantization:

GPTNeoXForCausalLM(
  (gpt_neox): GPTNeoXModel(
    (embed_in): Embedding(50304, 1024)
    (emb_dropout): Dropout(p=0.0, inplace=False)
    (layers): ModuleList(
      (0-23): 24 x GPTNeoXLayer(
        (input_layernorm): LayerNorm((1024,), eps=1e-05, elementwise_affine=True)
        (post_attention_layernorm): LayerNorm((1024,), eps=1e-05, elementwise_affine=True)
        (post_attention_dropout): Dropout(p=0.0, inplace=False)
        (post_mlp_dropout): Dropout(p=0.0, inplace=False)
        (attention): GPTNeoXSdpaAttention(
          (rotary_emb): GPTNeoXRotaryEmbedding()
          (query_key_value): HQQLinear(in_features=1024, out_features=3072, bias=True)
          (dense): HQQLinear(in_features=1024, out_features=1024, bias=True)
          (attention_dropout): Dropout(p=0.0, inplace=False)
        )
        (mlp): GPTNeoXMLP(
          (dense_h_to_4h): HQQLinear(in_features=1024, out_features=4096, bias=True)
          (dense_4h_to_h): HQQLinear(in_features=4096, out_features=1024, bias=True)
          (act): GELUActivation()
        )
      )
    )
    (final_layer_norm): LayerNorm((1024,), eps=1e-05, elementwise_affine=True)
    (rotary_emb): GPTNeoXRotaryEmbedding()
  )
  (embed_out): HQQLinear(in_features=1024, out_features=50304, bias=False)
)

Could someone please help!

## 评论 (4)

### mobicham · 2026-03-18

Hi @rishi2019194 , this seems more of a transformers issue. What is the model so I can try to debug?

### rishi2019194 · 2026-03-18

Hi @mobicham , the model is - EleutherAI/pythia-410m-deduped. But the same issue is happening for all model sizes in the Pythia models

### mobicham · 2026-03-18

Okay, seems like transformers broke support for HQQ. You can bypass it and use this: 
```Python
import torch
from transformers import AutoModelForCausalLM
from hqq.core.quantize import *

model_name = "EleutherAI/pythia-410m-deduped"
skip_mods = ["dense_h_to_4h", "dense_4h_to_h"]
quant_config = BaseQuantizeConfig(nbits=8, group_size=128) 
compute_dtype = torch.float16  
model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=compute_dtype)

def patch_linear(linear_layer, quant_config):
    hqq_layer = HQQLinear(linear_layer, 
                          quant_config=quant_config,
                          compute_dtype=compute_dtype,
                          device='cuda')

    return hqq_layer

#Quantize
def quantize(model, quant_config, skip_modules):                                                                                                    
    for name, module in model.named_modules():                                                                                                      
        if isinstance(module, torch.nn.Linear) and not any(s in name for s in skip_modules):                                                        
            if "." in name:                                                                                                                         
                parent_name, attr = name.rsplit(".", 1)                                                                                             
                parent = model.get_submodule(parent_name)                                                                                           
            else:                                                                                                                                   
                parent = model                                                                                                                      
                attr = name                                                                                                                         
            setattr(parent, attr, patch_linear(module, quant_config))      
    model = model.to(device=device, dtype=compute_dtype)                                                                         
    return model   

model = quantize(model, quant_config, skip_mods)

with torch.no_grad():
    _ = model(torch.ones((1, 128), dtype=torch.int32, device='cuda'))
```

### rishi2019194 · 2026-03-18

Thanks a lot @mobicham. This turnaround works perfectly! Hopefully the transformers library owners can correct the issue soon!
