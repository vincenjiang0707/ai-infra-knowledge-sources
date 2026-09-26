source: https://docs.mthreads.com/mooreperf/mooreperf-doc-online/moore_perf_system/introduction

# 产品介绍

Moore Perf System 是摩尔线程自主研发的 GPU 性能分析工具，帮助开发者在开发和调试过程中识别系统级性能瓶颈，进行有针对性的分析和优化。该工具无需修改应用程序即可启用性能分析，支持命令行界面（CLI）和图形用户界面（GUI）两种操作模式。

## 核心功能[](https://docs.mthreads.com#核心功能)

### 多平台支持[](https://docs.mthreads.com#多平台支持)

**跨平台兼容**：支持 Linux (Ubuntu 22.04) 和 Windows 10/11 操作系统**多GPU架构支持**：支持 S70/S80/S4000/S5000/M1000 等 GPU**容器支持**：可在 Docker 容器环境中进行性能分析

### 全面的API追踪[](https://docs.mthreads.com#全面的api追踪)

**MUSA API Trace**：完整追踪 MUSA Runtime 和 Driver API 调用，支持 MUSA Graph 的 graph 和 node 粒度分析**图形API支持**：支持 OpenGL、OpenGL ES、Vulkan、Direct3D 11/12 等主流图形API**系统调用追踪**：可追踪操作系统运行时库（OS Runtime Libraries）的关键系统调用

### 高级分析能力[](https://docs.mthreads.com#高级分析能力)

**硬件级监控**：实时监控 GPU 计算单元、内存子系统和指令流水线效率**多报告对比**：支持同时加载多个报告进行性能对比分析**专家系统视图**：提供智能分析建议，自动识别优化机会**统计视图**：生成详细的性能统计信息，支持导出为 CSV/JSON/TXT 格式

### 灵活的数据收集[](https://docs.mthreads.com#灵活的数据收集)

**交互式控制**：支持手动开始/停止收集、延迟收集、限时收集等多种模式**热键控制**：通过 F12 等热键控制数据收集，适用于全屏应用**远程分析**：通过 SSH 连接远程 Linux 设备进行性能分析

## 使用场景[](https://docs.mthreads.com#使用场景)

### 应用性能优化[](https://docs.mthreads.com#应用性能优化)

- 识别 CPU-GPU 通信瓶颈
- 分析内核执行效率和资源利用率
- 优化内存访问模式和数据传输

### 游戏和图形应用开发[](https://docs.mthreads.com#游戏和图形应用开发)

- Direct3D 11/12 和 Vulkan API 性能分析
- 帧率和渲染管线性能监控
- WDDM 队列调度分析

### AI和计算工作负载[](https://docs.mthreads.com#ai和计算工作负载)

- MUSA 计算内核性能分析
- 多流并发执行监控
- GPU 利用率和吞吐量评估

### 系统级调试[](https://docs.mthreads.com#系统级调试)

- 容器化应用性能分析
- 远程设备性能监控
- 多进程/多线程应用调试