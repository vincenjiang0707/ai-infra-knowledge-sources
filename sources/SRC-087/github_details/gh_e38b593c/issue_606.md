# [Issue #606] [RFC]: Does the Eagle3 draft model for Multimodal(VL) require visual data during training?

source: https://github.com/vllm-project/speculators/issues/606
state: open | updated: 2026-08-19T10:15:24Z
labels: RFC

## 正文

### Motivation.

This RFC aims to clarify the training data requirements for the Eagle3 draft model dedicated to Multimodal(VL) models. Several months ago, I generated datasets following the existing guidelines, and found that only image placeholders existed in input_ids, while no mm_features (image visual features) were included throughout the datasets. We intend to confirm whether visual information needs to be incorporated into its training set, and analyze the compatibility and potential risks if the model is trained purely on text data. The goal is to provide clear guidance for model training and deployment in Multimodal(VL) speculative decoding scenarios.

### Proposed Change.

This RFC standardizes the training data format and composition for the Eagle3 draft model serving Multimodal(VL) models. It defines mandatory visual feature fields including mm_features for dataset construction, and supplements relevant specifications to eliminate issues caused by missing visual information.

### Any Other Things.

_No response_

## 评论 (2)

### shanjiaz · 2026-06-15

Thanks for submitting this issue and raising the concerns! @wangyichao1999 

- Regarding training data preparation. You're correct, our recommended pathway for training did not include image data. Our existing multimodal draft models are trained on text-only data and perform well on text inputs. We have since added multi-modal data preprocessing as of PR [495](https://github.com/vllm-project/speculators/pull/495) and will continue to harden the pathway. Please give it a try and let us know! 

- We haven't done extensive testing to set up guideline on whether or not to train multi-modal models on image data. We're planning to investigate this ourselves, but if you have any preliminary results(acceptance rates or speedup comparisons when training with vs. without image data), we'd love to see them! Feel free to reach out on vllm slack and we could talk more there : )

### shyshuai90 · 2026-08-19

**Subject: Re: [RFC]: Does the Eagle3 draft model for Multimodal(VL) require visual data during training?**

Hi @wangyichao1999 and @shanjiaz,

Thanks for raising this RFC. I've been looking into the Eagle3 implementation and have a question about the multimodal training setup.

### Observations

In the Eagle3 forward pass ([`core.py#L281`](https://github.com/vllm-project/speculators/blob/main/src/speculators/models/eagle3/core.py#L281)):
```python
input_embeds = self.embed_tokens(input_ids)
hidden_states = torch.cat([input_embeds, hidden_states], dim=-1)
```
The draft model takes `input_ids` → `embed_tokens` → `input_embeds`, concatenates with historical `hidden_states`, and predicts the next token.

Similarly, in vLLM inference ([`llama_eagle3.py#L235`](https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/models/llama_eagle3.py#L235)):
```python
if input_embeds is None:
    input_embeds = self.embed_input_ids(input_ids)
```

### The Question

If the draft model is trained on text-only data, the `embed_tokens` table learns embeddings for text tokens. But during multimodal inference, `input_ids` will contain **special image tokens** (e.g., `<|image_pad|>`). These tokens:

- May not exist in the vocabulary at all (they're placeholders)
- Or exist but were never trained in the draft model's embedding table

So the draft model would receive a meaningless/untrained embedding for these positions.

### Is this actually correct?

Am I misunderstanding something here? How does the draft model handle these unseen image tokens at inference time? Even if `hidden_states` already contains the visual information, the `input_embeds` part still needs to be meaningful for the current position.

Is the expectation that these image tokens are treated as "don't care" positions, or is there some mechanism I'm missing that maps them to valid embeddings?

### Future Plans

If this is indeed a concern, what's the roadmap for addressing it? I saw PR #495 added multimodal data preprocessing – is the plan to eventually include visual data in training? Or is the text-only approach considered sufficient?

Would appreciate any clarification!

---
