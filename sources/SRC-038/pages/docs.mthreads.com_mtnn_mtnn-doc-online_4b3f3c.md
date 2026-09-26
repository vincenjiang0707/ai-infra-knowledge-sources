source: https://docs.mthreads.com/mtnn/mtnn-doc-online/

# AIModule - MTNN

## AIModule[](https://docs.mthreads.com#aimodule)

摩尔线程 **AIModule** 是专为 **摩尔线程长江 SoC（M1000）** 平台设计的一体化 AI 推理与视频智能分析软件模块，深度融合 M1000 的异构计算架构，提供从视频输入到 AI 决策输出的端到端加速能力。

基于 M1000 内置的 **高性能 NPU（神经网络处理单元）** 与 **通用 GPU 算力** ，AIModule 支持多种主流深度学习模型（如 YOLO、ResNet、MobileNet 等）的高效部署，并通过 **MTNN 模型格式** 实现模型轻量化与硬件亲和优化。配合 MTStream 多媒体流水线，AIModule 可在解码后的原始视频帧上直接执行目标检测、人脸识别、行为分析等任务，推理结果以元数据形式回传，供 OSD 渲染或业务系统调用。

AIModule 具备以下核心优势：

**硬件原生加速**：充分利用 M1000 NPU 的 INT8/FP16 计算能力，单芯片支持多路并发 AI 推理；**低延迟高吞吐**：结合 DMABUF 零拷贝机制，避免 CPU 内存搬运，端到端推理延迟可低至 20ms；**灵活部署模式**：支持 NPU 优先、GPU 辅助或纯 GPU 推理，适配不同精度与性能需求；**无缝集成**：通过`mtnpuinfer`

/`mtgpuinfer`

GStreamer 插件，一行命令即可嵌入视频分析 pipeline；**边��缘就绪**：专为智慧城市、工业视觉、智能安防等边缘 AI 场景优化，功耗可控，稳定性高。

作为 M1000 软件栈的关键组件，AIModule 与 MSTtream、MTNN、MUSA 共同构建了“编解码 + 推理 + 渲染”全链路国产化 AI 视频处理生态，助力开发者快速打造高性能、低功耗的智能边缘应用。

## MTNN[](https://docs.mthreads.com#mtnn)

**MTNN (Moore Threads Neural Network)** 是一组专为 M1000 设计的端侧 AI 推理工具链与运行时库。它帮助开发者将训练好的深度学习模型高效部署到 M1000 设备上，充分发挥其 NPU（神经网络处理单元）的硬件加速能力，实现低延迟、高能效的设备端机器学习。

更多信息，请参阅 [MTNN SDK 开发者手册](https://docs.mthreads.com/mtnn/mtnn-doc-online/introduction) 。