source: https://docs.mthreads.com/mtstream/mtstream-doc-online/

# AIModule - MTStream

## AIModule[](https://docs.mthreads.com#aimodule)

摩尔线程 **AIModule** 是专为 **摩尔线程长江 SoC（M1000）** 平台设计的一体化 AI 推理与视频智能分析软件模块，深度融合 M1000 的异构计算架构，提供从视频输入到 AI 决策输出的端到端加速能力。

基于 M1000 内置的 **高性能 NPU（神经网络处理单元）** 与 **通用 GPU 算力** ，AIModule 支持多种主流深度学习模型（如 YOLO、ResNet、MobileNet 等）的高效部署，并通过 **MTNN 模型格式** 实现模型轻量化与硬件亲和优化。配合 MTStream 多媒体流水线，AIModule 可在解码后的原始视频帧上直接执行目标检测、人脸识别、行为分析等任务，推理结果以元数据形式回传，供 OSD 渲染或业务系统调用。

AIModule 具备以下核心优势：

**硬件原生加速**：充分利用 M1000 NPU 的 INT8/FP16 计算能力，单芯片支持多路并发 AI 推理；**低延迟高吞吐**：结合 DMABUF 零拷贝机制，避免 CPU 内存搬运，端到端推理延迟可低至 20ms；**灵活部署模式**：支持 NPU 优先、GPU 辅助或纯 GPU 推理，适配不同精度与性能需求；**无缝��集成**：通过`mtnpuinfer`

/`mtgpuinfer`

GStreamer 插件，一行命令即可嵌入视频分析 pipeline；**边缘就绪**：专为智慧城市、工业视觉、智能安防等边缘 AI 场景优化，功耗可控，稳定性高。

作为 M1000 软件栈的关键组件，AIModule 与 MSTtream、MTNN、MUSA 共同构建了“编解码 + 推理 + 渲染”全链路国产化 AI 视频处理生态，助力开发者快速打造高性能、低功耗的智能边缘应用。

## MTStream[](https://docs.mthreads.com#mtstream)

**MTStream SDK** 是专为 M1000 设计的高性能多媒体处理软件开发包。它通过插件的形式，封装了底层硬件编解码器、图像处理单元的复杂操作，提供简单易用的插件。目前支持的硬件形态是 MTT E300 AI计算模组 (AIMODULE) 。

### 核心能力[](https://docs.mthreads.com#核心能力)

**高并发：**支持多达 4 路以上 1080P 实时视频同步编解码和AI推理。**低延迟：**针对实时视频流优化，端到端延迟极低。**硬件加速：**深度集成 M1000 的 解码、编码、图像处理、NPU/GPU （AI推理）。**插件化架构**：基于 GStreamer，可灵活组合解码、推理、OSD、编码等模块。**支持 AI 推理：**可无缝接入 MTNN 框架进行推理。

### 适用场景[](https://docs.mthreads.com#适用场景)

- 智能视频分析（IVA）、智慧城市监控。
- 云游戏、云桌面视频流处理。
- 边缘 AI 推理前的多媒体数据预处理（对接 MTNN 推理）。

更多信息，请参阅 [MTStream SDK 开发者手册](https://docs.mthreads.com/mtstream/mtstream-doc-online/introduction)。