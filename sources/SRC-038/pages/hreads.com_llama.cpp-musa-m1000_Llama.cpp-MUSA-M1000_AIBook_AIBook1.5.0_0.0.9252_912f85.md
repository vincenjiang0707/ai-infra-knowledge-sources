source: https://docs.mthreads.com/llama.cpp-musa-m1000/Llama.cpp-MUSA-M1000/AIBook/AIBook1.5.0+0.0.9252/

# AIBook AIOS 1.5.0 用户指南

欢迎使用 AIBook AIOS 1.5.0 文档。本章节介绍在 M1000 设备上验证和使用系统预装的 Llama.cpp-MUSA-M1000 0.0.9252。

## 版本信息[](https://docs.mthreads.com#版本信息)

| 项目 | 版本 |
|---|---|
| 系统版本 | AIOS 1.5.0 |
| Llama.cpp-MUSA-M1000 版本 | 0.0.9252 |
| 发布时间 | 2026.08.20 |
| 状态 | 最新推荐 |

## 版本更新说明[](https://docs.mthreads.com#版本更新说明)

AIBook AIOS 1.5.0 系统环境预装 Llama.cpp-MUSA-M1000 0.0.9252，支持 Qwen3.6-35B-A3B-Q4_K、Qwen3.5-9B-Q4_K、Qwen3.5-4B-Q4_K 和 Qwen3-Embedding-0.6B-f16 模型的单并发推理。

llama.cpp-musa 当前主要针对 Q4_K 量化类型进行性能优化，推荐优先使用 Q4_K 格式的 GGUF 模型。除 MUSA 相关运行参数外，使用方法尽量与原生 llama.cpp 保持兼容。