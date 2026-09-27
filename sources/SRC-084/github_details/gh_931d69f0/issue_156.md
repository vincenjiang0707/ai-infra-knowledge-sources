# [Issue #156] issues loading quantized model from hugginface repo

source: https://github.com/dropbox/hqq/issues/156
state: closed | updated: 2025-03-27T00:48:16Z
labels: 

## 正文


I tried following the [example](https://huggingface.co/mobiuslabsgmbh/CLIP-ViT-H-14-laion2B-2bit_g16_s128-HQQ) for zeroshot classification.

However, I get errors when trying to load the quantized model. Below are the details:

model_visual = HQQtimm.from_quantized("mobiuslabsgmbh/CLIP-ViT-H-14-laion2B-2bit_g16_s128-HQQ")



`---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Cell In[16], line 4
      1 from hqq.engine.timm import HQQtimm
      2 #model_visual = HQQtimm.from_quantized("mobiuslabsgmbh/CLIP-ViT-H-14-laion2B-2bit_g16_s128-HQQ")
      3 #cache_path = "/root/.cache/huggingface/hub/models--laion--CLIP-ViT-H-14-laion2B-s32B-b79K/snapshots/1c2b8495b28150b8a4922ee1c8edee224c284c0c/open_clip_model.safetensors"
----> 4 model_visual = HQQtimm.from_quantized("mobiuslabsgmbh/CLIP-ViT-H-14-laion2B-2bit_g16_s128-HQQ")

File /usr/local/lib/python3.8/dist-packages/hqq/engine/base.py:87, in HQQWrapper.from_quantized(cls, save_dir_or_hub, compute_dtype, device, cache_dir, adapter)
     84 arch_key = cls._get_arch_key_from_save_dir(save_dir)
     85 cls._check_arch_support(arch_key)
---> 87 model = cls._get_hqq_class(arch_key).from_quantized(
     88     save_dir,
     89     compute_dtype=compute_dtype,
     90     device=device,
     91     cache_dir=cache_dir,
     92     adapter=adapter,
     93 )
     95 cls._make_quantizable(model, quantized=True)
     96 return model

File /usr/local/lib/python3.8/dist-packages/hqq/models/base.py:476, in BaseHQQModel.from_quantized(cls, save_dir_or_hub, compute_dtype, device, cache_dir, adapter, **kwargs)
    473 save_dir = cls.try_snapshot_download(save_dir_or_hub, cache_dir)
    475 # Load model from config
--> 476 model = cls.create_model(save_dir, kwargs)
    478 # Track save directory
    479 model.save_dir = save_dir

TypeError: create_model() takes 2 positional arguments but 3 were given`


Any suggestions regarding this issue? I'd appreciate it if anyone could point me in the right direction.

## 评论 (6)

### mobicham · 2025-03-24

@jxs094 sorry I forgot to mention that but that example is deprecated. You should use the model via transformers: https://github.com/mobiusml/hqq/?tab=readme-ov-file#transformers-

### jxs094 · 2025-03-25

> [@jxs094](https://github.com/jxs094) sorry I forgot to mention that but that example is deprecated. You should use the model via transformers: https://github.com/mobiusml/hqq/?tab=readme-ov-file#transformers-

I see. That makes sense, because the errors disappeared when I installed v1.2.

Per your recommendations, I tried the following after installing the latest vesion:

AutoHQQHFModel.from_quantized("mobiuslabsgmbh/CLIP-ViT-H-14-laion2B-2bit_g16_s128-HQQ")

`---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Cell In[10], line 13
      9 save_dir = './open_clip_quantized' 
     11 #AutoHQQHFModel.quantize_model(model, quant_config=quant_config, compute_dtype=compute_dtype, device=device)
---> 13 AutoHQQHFModel.from_quantized("mobiuslabsgmbh/CLIP-ViT-H-14-laion2B-2bit_g16_s128-HQQ")

File /usr/local/lib/python3.10/dist-packages/hqq/models/base.py:476, in BaseHQQModel.from_quantized(cls, save_dir_or_hub, compute_dtype, device, cache_dir, adapter, **kwargs)
    473 save_dir = cls.try_snapshot_download(save_dir_or_hub, cache_dir)
    475 # Load model from config
--> 476 model = cls.create_model(save_dir, kwargs)
    478 # Track save directory
    479 model.save_dir = save_dir

File /usr/local/lib/python3.10/dist-packages/hqq/models/hf/base.py:33, in BaseHQQHFModel.create_model(cls, save_dir, kwargs)
     31 # Todo: add support for other auto models
     32 archs = config.architectures
---> 33 if len(archs) == 1:
     34     if ("CausalLM" in archs[0]):
     35         auto_class = transformers.AutoModelForCausalLM

TypeError: object of type 'NoneType' has no len()`


Still gives me an error.  I am not really familiar with how to work with this.

I think an example would help me greatly.


### mobicham · 2025-03-25

Oh no sorry, I mean you should use the CLIP model via transformers, that quantized model is deprecated. So you need to quantize the model via the transformers library, something like this:

```Python
from transformers import AutoModelForCausalLM, HqqConfig

# All linear layers will use the same quantization config
quant_config = HqqConfig(nbits=4, group_size=64)

# Load and quantize
model_id = `laion/CLIP-ViT-H-14-laion2B-s32B-b79K`
model = AutoModelForCausalLM.from_pretrained(
    model_id, 
    torch_dtype=torch.float16, 
    device_map="cuda", 
    quantization_config=quant_config
)
```

Otherwise, if you still want to use that timm model, you can use an older version of `hqq == 0.1.0`


### jxs094 · 2025-03-26

> Oh no sorry, I mean you should use the CLIP model via transformers, that quantized model is deprecated. So you need to quantize the model via the transformers library, something like this:
> 
> from transformers import AutoModelForCausalLM, HqqConfig
> 
> # All linear layers will use the same quantization config
> quant_config = HqqConfig(nbits=4, group_size=64)
> 
> # Load and quantize
> model_id = `laion/CLIP-ViT-H-14-laion2B-s32B-b79K`
> model = AutoModelForCausalLM.from_pretrained(
>     model_id, 
>     torch_dtype=torch.float16, 
>     device_map="cuda", 
>     quantization_config=quant_config
> )
> Otherwise, if you still want to use that timm model, you can use an older version of `hqq == 0.1.0`

I see. I get it now. However, I don't believe the model's configuration is supported.

This is the output message I get when I run your example with the latest hqq:

---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
Cell In[12], line 12
     10 # Load and quantize
     11 model_id = 'laion/CLIP-ViT-H-14-laion2B-s32B-b79K'
---> 12 model = AutoModelForCausalLM.from_pretrained(
     13     model_id,
     14     torch_dtype=torch.float16, 
     15     device_map="cuda", 
     16     quantization_config=quant_config
     17 )

File /usr/local/lib/python3.10/dist-packages/transformers/models/auto/auto_factory.py:576, in _BaseAutoModelClass.from_pretrained(cls, pretrained_model_name_or_path, *model_args, **kwargs)
    572     model_class = _get_model_class(config, cls._model_mapping)
    573     return model_class.from_pretrained(
    574         pretrained_model_name_or_path, *model_args, config=config, **hub_kwargs, **kwargs
    575     )
--> 576 raise ValueError(
    577     f"Unrecognized configuration class {config.__class__} for this kind of AutoModel: {cls.__name__}.\n"
    578     f"Model type should be one of {', '.join(c.__name__ for c in cls._model_mapping.keys())}."
    579 )

ValueError: Unrecognized configuration class <class 'transformers.models.clip.configuration_clip.CLIPConfig'> for this kind of AutoModel: AutoModelForCausalLM.
Model type should be one of AriaTextConfig, BambaConfig, BartConfig, BertConfig, BertGenerationConfig, BigBirdConfig, BigBirdPegasusConfig, BioGptConfig, BlenderbotConfig, BlenderbotSmallConfig, BloomConfig, CamembertConfig, LlamaConfig, CodeGenConfig, CohereConfig, Cohere2Config, CpmAntConfig, CTRLConfig, Data2VecTextConfig, DbrxConfig, DiffLlamaConfig, ElectraConfig, Emu3Config, ErnieConfig, FalconConfig, FalconMambaConfig, FuyuConfig, GemmaConfig, Gemma2Config, Gemma3Config, Gemma3TextConfig, GitConfig, GlmConfig, GotOcr2Config, GPT2Config, GPT2Config, GPTBigCodeConfig, GPTNeoConfig, GPTNeoXConfig, GPTNeoXJapaneseConfig, GPTJConfig, GraniteConfig, GraniteMoeConfig, GraniteMoeSharedConfig, HeliumConfig, JambaConfig, JetMoeConfig, LlamaConfig, MambaConfig, Mamba2Config, MarianConfig, MBartConfig, MegaConfig, MegatronBertConfig, MistralConfig, MixtralConfig, MllamaConfig, MoshiConfig, MptConfig, MusicgenConfig, MusicgenMelodyConfig, MvpConfig, NemotronConfig, OlmoConfig, Olmo2Config, OlmoeConfig, OpenLlamaConfig, OpenAIGPTConfig, OPTConfig, PegasusConfig, PersimmonConfig, PhiConfig, Phi3Config, PhimoeConfig, PLBartConfig, ProphetNetConfig, QDQBertConfig, Qwen2Config, Qwen2MoeConfig, RecurrentGemmaConfig, ReformerConfig, RemBertConfig, RobertaConfig, RobertaPreLayerNormConfig, RoCBertConfig, RoFormerConfig, RwkvConfig, Speech2Text2Config, StableLmConfig, Starcoder2Config, TransfoXLConfig, TrOCRConfig, WhisperConfig, XGLMConfig, XLMConfig, XLMProphetNetConfig, XLMRobertaConfig, XLMRobertaXLConfig, XLNetConfig, XmodConfig, ZambaConfig, Zamba2Config.

I reckon I have better chances with the older versions for that particular CLIP config.

I appreciate your prompt responses!

### mobicham · 2025-03-26

Something like this, but you need to find a clip model supporting transformers:

```Python
import requests
import torch
from PIL import Image
from transformers import AutoModel, AutoProcessor, HqqConfig

model_id = "Bingsu/clip-vit-large-patch14-ko"
processor = AutoProcessor.from_pretrained(model_id)

quant_config = HqqConfig(nbits=4, group_size=64, axis=0, skip_modules=['text_model'])
model = AutoModel.from_pretrained(model_id, 
                                 torch_dtype=torch.bfloat16,
                                 device_map="cuda:0",
                                 quantization_config=quant_config,
                                 low_cpu_mem_usage=True)

url = "http://images.cocodataset.org/val2017/000000039769.jpg"
image = Image.open(requests.get(url, stream=True).raw)
inputs = processor(text=["고양이 두 마리", "개 두 마리"], images=image, return_tensors="pt", padding=True)
with torch.inference_mode():
    outputs = model(**inputs)
logits_per_image = outputs.logits_per_image
probs = logits_per_image.softmax(dim=1)
```

### jxs094 · 2025-03-27

> Something like this, but you need to find a clip model supporting transformers:
> 
> import requests
> import torch
> from PIL import Image
> from transformers import AutoModel, AutoProcessor, HqqConfig
> 
> model_id = "Bingsu/clip-vit-large-patch14-ko"
> processor = AutoProcessor.from_pretrained(model_id)
> 
> quant_config = HqqConfig(nbits=4, group_size=64, axis=0, skip_modules=['text_model'])
> model = AutoModel.from_pretrained(model_id, 
>                                  torch_dtype=torch.bfloat16,
>                                  device_map="cuda:0",
>                                  quantization_config=quant_config,
>                                  low_cpu_mem_usage=True)
> 
> url = "http://images.cocodataset.org/val2017/000000039769.jpg"
> image = Image.open(requests.get(url, stream=True).raw)
> inputs = processor(text=["고양이 두 마리", "개 두 마리"], images=image, return_tensors="pt", padding=True)
> with torch.inference_mode():
>     outputs = model(**inputs)
> logits_per_image = outputs.logits_per_image
> probs = logits_per_image.softmax(dim=1)

I am happy to report that I can run your code with the latest version without any issues. When I runyour example, I get the correct output as below:
```
tensor([[23.1250, 17.2500]], dtype=torch.bfloat16)
tensor([[0.9961, 0.0028]], dtype=torch.bfloat16)
```

I tried another model from [the HF official documentation](https://huggingface.co/docs/transformers/en/model_doc/clip).
It also runs as expected without any issues.

```
import requests
import torch
from PIL import Image
#import HF transformers related stuff
from transformers import AutoModel, AutoProcessor, HqqConfig

model_id = "openai/clip-vit-base-patch32"
processor = AutoProcessor.from_pretrained(model_id)

quant_config = HqqConfig(nbits=4, group_size=64, axis=0, skip_modules=['text_model'])

model = AutoModel.from_pretrained(model_id, 
                                 torch_dtype=torch.bfloat16,
                                 device_map="cuda:0",
                                 quantization_config=quant_config,
                                 low_cpu_mem_usage=True)

url = "http://images.cocodataset.org/val2017/000000039769.jpg"
image = Image.open(requests.get(url, stream=True).raw)

inputs = processor(text=["a photo of a cat", "a photo of a dog"], images=image, return_tensors="pt", padding=True)

with torch.inference_mode():
    outputs = model(**inputs)

logits_per_image = outputs.logits_per_image
print(logits_per_image)
probs = logits_per_image.softmax(dim=1)
print(probs)
```
the output
```
tensor([[23.6250, 18.1250]], dtype=torch.bfloat16)
tensor([[0.9961, 0.0041]], dtype=torch.bfloat16)
```

I think the examples gave me a pretty good idea of how to use HQQ.

Thank you so much for being so helpful!

