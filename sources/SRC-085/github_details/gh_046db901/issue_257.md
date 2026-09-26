# [Issue #257] Can eagle3 support qwen-vl?

source: https://github.com/SafeAILab/EAGLE/issues/257
state: closed | updated: 2025-11-08T07:56:12Z
labels: 

## 正文

Hi, there. Thanks a lot for your great work on speculative decoding! As the title describes, can EAGLE3 support qwen-vl, such as qwen-2.5-vl-3b-instruct / qwen-2.5-vl-7b-instruct and so forth? or how can we extend EAGLE3 to support multimodal model?

## 评论 (4)

### hongyanz · 2025-07-17

It is technically possible for EAGLE to extend to multi-modal models, but the current version only supports LLMs.

### ChiikawaSama · 2025-07-17

> It is technically possible for EAGLE to extend to multi-modal models, but the current version only supports LLMs.

thanks for reply! i'm gonna try add EAGLE3 to qwen-vl, thought it's only need to feed combined token (vit output + llm input) to the llm part, and thus would be fine?

### hongyanz · 2025-07-17

I think so. Vision tokens and language tokens have no significant difference.

### 330205812 · 2025-11-08

> > It is technically possible for EAGLE to extend to multi-modal models, but the current version only supports LLMs.
> 
> thanks for reply! i'm gonna try add EAGLE3 to qwen-vl, thought it's only need to feed combined token (vit output + llm input) to the llm part, and thus would be fine?
Hi, How's the implementation of your project going? What stage are you at?
