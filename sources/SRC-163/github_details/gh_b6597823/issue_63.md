# [Issue #63] the inference result sentence is null

source: https://github.com/LLMServe/DistServe/issues/63
state: open | updated: 2025-04-17T10:45:06Z
labels: 

## 正文

Thanks for your great work. When I run DistServe/examples/offline.py for inference, the generated inference result is empty when the input prompt "Give me three tips for healthy life." is given. I guess it may be caused by stop=["\n"], so I changed it to stop=["</s>"], and the generated inference result is a sentence that keeps repeating. The various temperature and top_p values ​​I tried did not solve this problem. Do you know how to solve it?

The model I use is llama2-7B.

## 评论 (4)

### LordEdison · 2025-04-08

similar with https://github.com/LLMServe/DistServe/issues/40 & https://github.com/LLMServe/DistServe/issues/16, maybe you can try end your prompts with word or comma ?

### LordEdison · 2025-04-08

I've met the same problem and it seems that the request didn't get into decode phase after context phase😭

### Dreamer-HIT · 2025-04-08

> similar with [#40](https://github.com/LLMServe/DistServe/issues/40) & [#16](https://github.com/LLMServe/DistServe/issues/16), maybe you can try end your prompts with word or comma ?

Adding a comma or inputing an incomplete prompt does solve the problem. But I don't think it solves the problem fundamentally. Have you tried the OPT model to see if this problem exists?

### LordEdison · 2025-04-17

> Adding a comma or inputing an incomplete prompt does solve the problem. But I don't think it solves the problem fundamentally. Have you tried the OPT model to see if this problem exists?

sorry I haven't found any way to use OPT model. I tried to modify the initial maxidx in findmax (https://github.com/LLMServe/SwiftTransformer/blob/main/src/csrc/kernel/findmax.cu#L24) as https://github.com/LLMServe/DistServe/issues/16 said,  only to find it in vain😭
