# [Issue #66] Clarifications on Models + Batch Size

source: https://github.com/FasterDecoding/Medusa/issues/66
state: closed | updated: 2023-12-23T02:52:17Z
labels: 

## 正文

Which models are supported?

Currently, is it only Vicuna models?
- Although any Llama 2 model could be trained as well, it's just that without the original dataset the heads will be a little weaker?
- Mistral cannot be trained as that architecture isn't supported? correct?

What batch size is supported?
- Just a batch size of 1 for now?
- Same for the TGI support - it will only work for a batch size of 1?

Would be great if this could be added to the model card. Also, linking some 

## 评论 (5)

### leeyeehoo · 2023-12-22

Support for the Mistral-based models is added ([branch](https://github.com/FasterDecoding/Medusa/tree/v1.0-prerelease)). Batch size 1 yes. We will soon release the new models :) Feel free to report any issue you encounter and we will address those ASAP.

### RonanKMcGovern · 2023-12-23

Does speculative inference work for batch size greater than one? Thanks

And, thanks, that's great on Mistral being available, will open up training openchat 3.5 too and get away from the non-commercial vicuna.

### leeyeehoo · 2023-12-23

It should work with batch size > 1. We are trying to find a good inference lib for implementation since extending bs>1 on vanilla hugging face is kinda like rebuilding the wheel... If you have any suggestions feel free to discuss :)

### RonanKMcGovern · 2023-12-23

Ok, cool. I need to get better at the intimate details, but here are some high level thoughts:
- TGI is faster than vLLM so to the extent supporting that is possible, that's probably good.
- vLLM would also be a good option as it has an openai style api which makes adoption easy.

Thanks for all the answers above btw, I'm keen to check out the Mistral model.

### leeyeehoo · 2023-12-23

Thank you for providing good insights! 
