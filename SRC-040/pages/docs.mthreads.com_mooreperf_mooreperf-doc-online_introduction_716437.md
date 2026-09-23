source: https://docs.mthreads.com/mooreperf/mooreperf-doc-online/introduction

# 摩尔线程 GPU 性能分析套件

**Moore Perf Tools** 是摩尔线程推出的低开销 GPU 性能分析工具套件，帮助开发人员深入分析 MUSA 应用程序和 Graphics 应用程序的性能瓶颈，并提供强大��的调试能力。

## 套件组成[](https://docs.mthreads.com#套件组成)

| 工具 | 用途 | 核心能力 |
|---|---|---|
| 通用应用程序性能分析 | 系统级性能监控、资源利用率分析 |
| Compute 应用程序深度分析 | Kernel 级性能指标、Roofline 模型分析 |
Moore Perf Graphics | Graphics 应用程序分析 | 图形管线性能分析、帧调试 |
| GPU 内存错误调试 | 越界检测、内存泄漏检查、API 错误报告 |

## 使用场景[](https://docs.mthreads.com#使用场景)

### 性能分析场景[](https://docs.mthreads.com#性能分析场景)

**Kernel 优化**：识别计算/内存瓶颈，定位性能热点**资源调优**：分析占用率、寄存器使用、共享内存配置**瓶颈诊断**：通过 Roofline 模型快速定位性能限制因素

### 调试场景[](https://docs.mthreads.com#调试场景)

**内存错误检测**：自动捕捉全局内存越界访问**泄漏排查**：发现未释放的 GPU 内存分配**API 验证**：检查 MUSA Runtime/Driver API 调用正确性