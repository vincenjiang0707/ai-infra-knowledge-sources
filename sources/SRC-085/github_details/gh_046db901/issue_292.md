# [Issue #292] Qwen3-MoE-30B-A3B-2507-thinking training issue

source: https://github.com/SafeAILab/EAGLE/issues/292
state: closed | updated: 2025-09-06T12:28:35Z
labels: 

## 正文

I'm trying to train the Qwen3-30b-A3B-thinking-2507 model using Specforge-EAGLE3. However, I noticed that in many example draft model configs, the architecture is always set to "LlamaForCausalLMEagle3", even for Qwen3 examples. After checking the source code, it seems that only LlamaForCausalLMEagle3 is supported.

How can I train a Qwen3-MoE-Thinking model in this setup? There is a Qwen3MoeForCausalLM class, but it doesn't seem to work properly. Is it only possible to use Llama3 as the draft model?

## 评论 (1)

### hongyanz · 2025-09-06

We highly encourage you to submit an issue to Specforge instead.
