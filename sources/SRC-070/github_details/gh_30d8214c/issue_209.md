# [Issue #209] [QUESTION] dsv32 mqa_logits kernel not considering causal masking?

source: https://github.com/deepseek-ai/DeepGEMM/issues/209
state: open | updated: 2026-01-21T03:35:56Z
labels: 

## 正文

Thanks for dsv32 great work!

By analysis the `fp8_mqa_logits` and `fp8_paged_mqa_logits` function, looks like after the q@k, we don't consider causal masking before topk?

I know the q/k feed to mqa_logits kernel is different from the q/k feed to MLA attention kernel, but we use the output of the mqa_logits kernel (and topk 2048) as indexer into the real MLA's kvcache, hence during the real attention computation we need consider causal, in prefill or decode(MTP) case.

vLLM [prefill dispatch](https://github.com/vllm-project/vllm/blob/08d26a1b7edc200d8d117491eac3e28c0428e571/vllm/model_executor/models/deepseek_v2.py#L654C26-L654C39) using `torch.ops._C.top_k_per_row` seems not considering causal, [decode dispatch](https://github.com/vllm-project/vllm/blob/08d26a1b7edc200d8d117491eac3e28c0428e571/vllm/model_executor/models/deepseek_v2.py#L708) looks like considered causal in MTP case after the logits kernel, before topk.

not sure if it is suppose to let the framework side to do causal before topk, or actually causal is not important during the indexer kernel?

## 评论 (1)

### zheanxu · 2025-10-22

To apply causal masking, you can set `clean_logits=True`. In this case, the subsequent `clean_logits` kernel will perform the masking. See:
https://github.com/deepseek-ai/DeepGEMM/blob/c9f8b34dcdacc20aa746b786f983492c51072870/csrc/apis/attention.hpp#L120

A more efficient approach is to set `clean_logits=False` and incorporate causal masking directly into the topk operation — i.e., ignore masked positions during topk selection. However, this requires implementing your own topk kernel.
