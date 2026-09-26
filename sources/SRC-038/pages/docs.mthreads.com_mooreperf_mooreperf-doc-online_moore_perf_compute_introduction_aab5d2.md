source: https://docs.mthreads.com/mooreperf/mooreperf-doc-online/moore_perf_compute/introduction

# 产品介绍

Moore Perf Compute（简称 MCU）是摩尔线程自主研发的 GPU 性能分析工具，专为 MUSA GPU 应用程序设计。该工具可帮助开发者精确识别和分析 MUSA GPU 上的性能瓶颈，通过直观的指标数据和 Roofline 可视化，帮助优化应用程序性能。Moore Perf Compute 提供命令行界面（CLI）和图形界面（GUI）两种使用方式，满足不同开发场景的需求。

## 核心功能[](https://docs.mthreads.com#核心功能)

### 性能指标收集[](https://docs.mthreads.com#性能指标收集)

Moore Perf Compute 支持收集多种性能指标，按功能划分为三个模块：

| 模块 | 功能描述 |
|---|---|
LaunchStats | 获取内核启动配置，包括 Grid/Block 大小、占用率、寄存器使用情况 |
MemoryWorkloadAnalysis | 分析内存访问模式，包括带宽利用率、内存管道利用率 |
SpeedOfLight | 评估计算和内存吞吐量，显示相较于硬件峰值的利用率 |

### Roofline 可视化[](https://docs.mthreads.com#roofline-可视化)

内置 Roofline 模型图表，直观展示内核性能与硬件极限的关系，帮助快速定位性能瓶颈类型（计算受限或内存受限）。

### 多方式分析[](https://docs.mthreads.com#多方式分析)

**CLI 方式**：适合自动化流程和脚本集成**GUI 方式**：支持本地和远程目标程序分析，提供可视化报告

### 重放机制[](https://docs.mthreads.com#重放机制)

通过多次重放应用程序收集完整指标集。由于 GPU 硬件性能计数器数量有限，需要多次执行才能收集所有指标。

### Green Contexts 支持[](https://docs.mthreads.com#green-contexts-支持)

支持分析使用 MUSA Green Contexts 的应用程序，自动识别并收集相关指标。

## 使用场景[](https://docs.mthreads.com#使用场景)

### 内核性能优化[](https://docs.mthreads.com#内核性能优化)

当开发者需要优化现有 MUSA GPU 内核性能时，可使用 Moore Perf Compute 分析内核的：

- 计算资源利用效率
- 内存访问模式
- 与硬件峰值的差距

### 新应用开发[](https://docs.mthreads.com#新应用开发)

在开发新的 MUSA GPU 应用时，通过性能分析确保应用充分利用硬件资源，避免常见的性能陷阱。

### 性能回归检测[](https://docs.mthreads.com#性能回归检测)

在持续集成流程中集成性能测试，通过对比基线数据及时发现性能退化。

### 多进程应用分析[](https://docs.mthreads.com#多进程应用分析)

支持 MPI 等多进程应用的性能分析，可对多节点、多 rank 应用进行统一分析。