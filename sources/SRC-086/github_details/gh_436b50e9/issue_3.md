# [Issue #3] Roadmap

source: https://github.com/FasterDecoding/Medusa/issues/3
state: open | updated: 2024-01-24T14:00:19Z
labels: documentation

## 正文

# Roadmap

## Functionality
- [x] #36
- [x] #39 
- [ ] Distill from any model without access to the original training data
- [ ] Batched inference
- [ ] Fine-grained KV cache management

## Integration
### Local Deployment
- [ ] #33
- [ ] #32
- [ ] #35
### Serving
- [ ] [vllm](https://github.com/vllm-project/vllm)
- [ ] [TGI](https://github.com/huggingface/text-generation-inference)
- [ ] [lightllm](https://github.com/ModelTC/lightllm)

## Research
- [x] #34
- [ ] Optimize the tree-based attention to reduce additional computation
- [ ] Improve the acceptance scheme to generate more diverse sequences

## 评论 (15)

### JianbangZ · 2023-09-12

Looks like a promising roadmap. I think llama.cpp support should be held a higher priority

### Kimiko-AI · 2023-09-13

Agree, that faster t/s is really important for llamacpp users.

### yhyu13 · 2023-09-13

Would love to you Medusa be as a plugin of ooba's textgen webui for medusa head models 

### yhyu13 · 2023-09-13

Would Medusa compatible with GPTQ quantized models?

Specifically, two Medusa heads fine-tuned on unquantized and quantized model, would they be the same? Or can they be swapped？

### ctlllll · 2023-09-13

> Would Medusa compatible with GPTQ quantized models?
> 
> Specifically, two Medusa heads fine-tuned on unquantized and quantized model, would they be the same? Or can they be swapped？

We didn't try this, but we can make an analogy to the 33B model we trained with `bitsandbytes`'s 8-bit quantized base model, where the difference seems to be minor. Yet, more investigation is needed :)

### aiapprentice101 · 2023-09-18

Please consider supporting quantized models, like GPTQ, AWQ, etc

### ctlllll · 2023-09-18

> Please consider supporting quantized models, like GPTQ, AWQ, etc

Thanks for the suggestion. Those models should be easily integrated just by loading the base model in those formats. We are trying to integrate Medusa into frameworks that the speed actually benefits from quantization, e.g., mlc-llm, llama.cpp.

### JianbangZ · 2023-09-18

> > Please consider supporting quantized models, like GPTQ, AWQ, etc
> 
> Thanks for the suggestion. Those models should be easily integrated just by loading the base model in those formats. We are trying to integrate Medusa into frameworks that the speed actually benefits from quantization, e.g., mlc-llm, llama.cpp.

Exciting. Is there a timeline for llama.cpp support? your best guess?

### ctlllll · 2023-09-18

> > > Please consider supporting quantized models, like GPTQ, AWQ, etc
> > 
> > 
> > Thanks for the suggestion. Those models should be easily integrated just by loading the base model in those formats. We are trying to integrate Medusa into frameworks that the speed actually benefits from quantization, e.g., mlc-llm, llama.cpp.
> 
> Exciting. Is there a timeline for llama.cpp support? your best guess?

We'll start with MLC-LLM first as it's more user-friendly for integration. For llama.cpp, we currently don't have the bandwidth to do it and it would be greatly appreciated if there were volunteers who could help us with it :)

### ctlllll · 2023-09-18

*🎉 Exciting News! 🎉*

We are thrilled to announce that we have received an award from [Chai Research](https://twitter.com/tianle_cai/status/1703891335147897341)! While the monetary value may not be substantial, we are dedicating it as a token of our appreciation for the invaluable contributions made by our community. The funds will be allocated as development bounties to incentivize the achievement of key milestones.

🏆 First Bounty: Porting Medusa to Llama.cpp #35  🏆
Bounty Amount: $100

### feifeibear · 2023-09-20

Hello @ctlllll , Thanks for providing such a wonderful project. I am interested in the part of Fine-grained KV cache management. Could you offer me more guidance on this?

I have been working on a demo for SpeculativeSampling for a while.

https://github.com/feifeibear/LLMSpeculativeSampling

### ctlllll · 2023-09-20

> Hello @ctlllll , Thanks for providing such a wonderful project. I am interested in the part of Fine-grained KV cache management. Could you offer me more guidance on this?
> 
> I have been working on a demo for SpeculativeSampling for a while.
> 
> https://github.com/feifeibear/LLMSpeculativeSampling

Hi @feifeibear , thanks for your interest! In the current version, we implemented a [pre-allocated KV cache](https://github.com/FasterDecoding/Medusa/blob/main/medusa/model/kv_cache.py) with the philosophy of keeping the original HF APIs and only for reducing the memory movement cost when updating KV cache. I think to be more dynamic, the PagedAttention mechanism in [vllm](https://github.com/vllm-project/vllm) might be a better reference :)

### nikshepsvn · 2023-11-21

Hey all, any updates on this?

### ctlllll · 2023-11-21

> Hey all, any updates on this?

We have some exciting stuff baking now. Let's wait and see :p

### nivibilla · 2024-01-22

Hi, could sglang be placed on the roadmap too? It's a recent release also from lmsys who made vllm. But it's faster.

https://github.com/sgl-project/sglang
