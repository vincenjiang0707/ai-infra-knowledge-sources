# [Issue #1157] [Question] Which vLLM Ascend version is compatible with Speculators 0.8.0

source: https://github.com/vllm-project/speculators/issues/1157
state: open | updated: 2026-09-24T03:14:40Z
labels: 

## 正文

I would like to use **Speculators 0.8.0** for speculative decoding, specifically during the **training process** where I want to leverage **vLLM Ascend** for preprocessing and hidden states generation. The base model I plan to use is **GLM5.3-w8a8**, and I intend to train **dflash2** and **dspark** draft models on Ascend 910C.

However, I cannot find a clear compatibility statement that specifies which vLLM Ascend version(s) work with Speculators 0.8.0, especially in this training-time usage scenario.

The vLLM Ascend release compatibility matrix lists mappings for vLLM Ascend, upstream vLLM, Python, CANN, PyTorch/torch_npu, etc., but it does not appear to include Speculators. The Speculators documentation mentions integration with vLLM through `vllm serve`, but I could not find any vLLM Ascend-specific version constraints, known issues, or guidance for using it during training for preprocessing/hidden states generation.

Could you please clarify:

1. Which vLLM Ascend version(s) are compatible with Speculators 0.8.0 for training-time preprocessing and hidden states generation?
2. Are there any known limitations, required patches, or workarounds when using Speculators 0.8.0 with GLM5.3-w8a8 and training dflash2 / dspark on vLLM Ascend?
3. Are there plans to add Speculators compatibility information to the vLLM Ascend release compatibility matrix or documentation?

Any guidance on the supported version combination would be greatly appreciated. I can provide more environment details, logs, or reproduction steps if needed.

## 评论 (1)

### fynnsu · 2026-09-23

@sunny-infra would you be able to provide some guidance here?
