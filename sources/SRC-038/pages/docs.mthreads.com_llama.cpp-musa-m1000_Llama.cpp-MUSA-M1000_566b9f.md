source: https://docs.mthreads.com/llama.cpp-musa-m1000/Llama.cpp-MUSA-M1000/

# 端侧 Llama.cpp-MUSA-M1000

Llama.cpp-MUSA-M1000 是 Llama.cpp 的硬件后端适配，使得 Llama.cpp 可以在摩尔线程 GPU 上运行大语言模型推理任务。Llama.cpp-MUSA-M1000 基于 ggml backend 抽象接口接入 MUSA 计算能力，将摩尔线程 GPU 的算子实现、显存管理和运行时调度与 Llama.cpp 主框架解耦集成。

借助 Llama.cpp-MUSA-M1000，Transformer 系列模型、混合专家（Mixture-of-Experts）模型以及部分多模态大语言模型，可以通过 GGUF 模型格式在摩尔线程 GPU 上运行。

## 版本选择[](https://docs.mthreads.com#版本选择)

Llama.cpp-MUSA-M1000 版本是推理软件版本；AIModule 1.4.1、AIBook 1.5.0 是设备系统版本。请先根据设备类型和系统版本选择对应文档。

| 设备 | 系统版本 | Llama.cpp-MUSA-M1000 版本 | 状态 | 文档入口 |
|---|---|---|---|---|
| AIBook | AIOS 1.5.0 | 0.0.9252 | 最新推荐 |
|

[进入文档](https://docs.mthreads.com/llama.cpp-musa-m1000/Llama.cpp-MUSA-M1000/AIModule/AIModule1.4.1+0.0.9252/)更多 Llama.cpp-MUSA-M1000 版本变更说明，请查看 [Llama.cpp-MUSA-M1000 版本说明](https://docs.mthreads.com/llama.cpp-musa-m1000/Llama.cpp-MUSA-M1000/release-notes)。