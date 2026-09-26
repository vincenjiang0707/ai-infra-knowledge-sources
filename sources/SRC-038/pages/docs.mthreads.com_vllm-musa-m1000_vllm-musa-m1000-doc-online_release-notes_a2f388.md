source: https://docs.mthreads.com/vllm-musa-m1000/vllm-musa-m1000-doc-online/release-notes

# vLLM-MUSA 版本说明

本页只说明 vLLM-MUSA 推理软件版本的变化。设备系统版本和文档入口请以首页的版本选择表为准。

| 版本 | 发布时间 | 说明 | 当前适用范围 |
|---|---|---|---|
| 1.4.2 | 2026.07.03 | 修复长上下文性能衰减问题。 | AIModule（系统版本：AIOS 1.4.1）、AIBook（系统版本：AIOS 1.5.0 / AIOS 1.4.2） |
| 1.4.1 | 2026.06.10 | 升级 vLLM 0.16、PyTorch 2.9.0、torch_musa 2.9.0、triton 3.2.0，支持 Qwen3.5 / Qwen3.6 / Qwen3-VL 系列。 | AIModule（系统版本：AIOS 1.4.1） |
| 1.3.2 | 2026.04.27 | 修复内存占用增加问题。 | AIModule（系统版本：AIOS 1.3.0.003）、AIBook（系统版本：AIOS 1.4.0 / AIOS 1.4.1） |
| 1.3.1 | 2026.03.03 | 修复 prefix-cache 场景 TTFT 变慢问题。 | AIBook（系统版本：AIOS 1.3.3） |
| 1.3 | 2025.12.19 | 升级 vLLM v1 engine，默认打开 prefill-cache，长上下文解码提速 x3。 | 已由后续版本替代，不作为官网推荐入口 |
| 1.2 | 2025.09.30 | 升级 vLLM 0.9.2、PyTorch 2.5、torch_musa 2.1.0，优化 GPTQ 相关算子，支持 Qwen3 系列。 | AIModule（系统版本：AIOS 1.3.0） |

## 选择建议[](https://docs.mthreads.com#选择建议)

- AIModule 用户优先使用系统版本 AIOS 1.4.1 + vLLM-MUSA 1.4.2。
- AIBook 用户优先使用系统版本 AIOS 1.5.0 + vLLM-MUSA 1.4.2。
- AIBook 系统版本 AIOS 1.4.2 使用 vLLM-MUSA 1.4.2。
- AIBook 系统版本 AIOS 1.4.0 / AIOS 1.4.1 使用 vLLM-MUSA 1.3.2。
- AIBook 系统版本 AIOS 1.3.3 作为历史版本保留，对应 vLLM-MUSA 1.3.1。
- AIModule 系统版本 AIOS 1.3.0.003 作为历史版本保留，对应 vLLM-MUSA 1.3.2。
- AIModule 系统版本 AIOS 1.3.0 作为历史版本保留，对应 vLLM-MUSA 1.2。