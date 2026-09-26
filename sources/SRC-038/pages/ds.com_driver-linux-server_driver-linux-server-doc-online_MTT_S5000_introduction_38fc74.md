source: https://docs.mthreads.com/driver-linux-server/driver-linux-server-doc-online/MTT_S5000/introduction

# 产品介绍

本章节介绍 Linux 服务器驱动文档覆盖的 `MTT S5000`

与 `MTT S4000`

两款产品，包括产品定位、关键能力和典型应用场景。环境兼容性与安装方法，参见[发布版本信息](https://docs.mthreads.com/driver-linux-server/driver-linux-server-doc-online/MTT_S5000/releasenotes/)和[安装指南](https://docs.mthreads.com/driver-linux-server/driver-linux-server-doc-online/MTT_S5000/install_guide)。

## MTT S5000[](https://docs.mthreads.com#mtt-s5000)

### 产品定位[](https://docs.mthreads.com#产品定位)

`MTT S5000`

是面向生成式 AI 训练、推理和高性能计算的训推一体全功能 GPU 智算卡，基于第四代 MUSA 全栈平��台，核心搭载 `PH100`

芯片。

### 主要特性[](https://docs.mthreads.com#主要特性)

- 支持多种精度计算，适用于大模型训练、微调和推理。
- 支持
`MTLink`

多卡互联，便于构建大规模训练和推理集群。 - 提供风冷和液冷形态，可覆盖数据中心不同部署方案。
- 原生适配
`PyTorch`

、`Megatron-LM`

、`vLLM`

、`SGLang`

等主流框架，便于将现有代码迁移到 MUSA 平台。

### 典型应用场景[](https://docs.mthreads.com#典型应用场景)

- 大语言模型训练与微调
- 高并发、低时延在线推理
- 高性能计算
- 多媒体处理与安全计算

## MTT S4000[](https://docs.mthreads.com#mtt-s4000)

### 产品定位[](https://docs.mthreads.com#产品定位-1)

`MTT S4000`

是面向大模型训练、微调和推理的智算加速卡，采用第三代 MUSA 架构，兼顾 AI 计算、图形渲染、多媒体处理和超高清显示能力。

### 主要特性[](https://docs.mthreads.com#主要特性-1)

- 配备 Tensor 核心，支持多种主流精度。
- 支持基于
`MTLink`

的多卡互联，便于扩展多卡和集群部署。 - 提供图形渲染、视频编解码和
`8K HDR`

显示能力，可支撑 AI 与图形、多媒体融合场景。 - 支持
`PCIe 5.0 x16`

、硬件虚拟化、`SR-IOV`

隔离和`MUSA`

安全引擎`2.0`

。 - 基于 MUSA 软件栈与
`MUSIFY`

工具，可平滑迁移现有 CUDA 程序。

### 典型应用场景[](https://docs.mthreads.com#典型应用场景-1)

- 大语言模型训练、微调和推理
- 图形渲染与数字内容创作
- 视频处理与多媒体服务
- 虚拟化和多租户 GPU 资源隔离