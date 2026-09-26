source: https://docs.mthreads.com/vllm-musa-m1000/vllm-musa-m1000-doc-online/AIModule/AIModule1.3.0.003+vllm1.3.2/

# AIModule AIOS 1.3.0.003 用户指南

本文档适用于：

| 项目 | 版本 |
|---|---|
| 设备 | AIModule |
| 系统版本 | AIOS 1.3.0.003 |
| vLLM-MUSA 版本 | 1.3.2 |
| 状态 | 历史版本 |

vLLM MUSA 是一个硬件插件，使得 vLLM 框架可以方便快速的在摩尔线程的 GPU 上运行，而无需侵入式的去修改 vLLM 原始的代码。vLLM MUSA 采用标准化的硬件抽象接口和动态注册架构，实现了摩尔线程GPU与vLLM框架的解耦集成。

借助 vLLM MUSA，Transformer系列模型、混合专家（Mixture-of-Expert）模型、嵌入模型以及多模态大语言模型在内的各类主流开源模型，均可在摩尔线程GPU上运行。