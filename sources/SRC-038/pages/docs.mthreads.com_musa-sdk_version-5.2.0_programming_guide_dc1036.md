source: https://docs.mthreads.com/musa-sdk/version-5.2.0/programming_guide/

# MUSA 编程指南

MUSA 编程指南包含完整的 GPU 并行计算编程指导。

## 推荐学习路径[](https://docs.mthreads.com#推荐学习路径)

`入门 → 编程模型 → 语法 → API → 硬件架构 → 性能优化`




## 什么是 MUSA

MUSA 概述、GPU 并行计算基础、SIMT 模型、线程层次结构、内存层次、MUSA SDK 软件栈


## 快速开始

15 分钟快速上手 MTGPU 编程——从环境验证到完整 Kernel 程序


## MUSA 编程模型

Host/Device 模型、线程层次结构 (Grid/Block/Thread)、内存层次结构 (寄存器/共享内存/全局内存)、L2 缓存管理、执行模型、流与事件


## MUSA C++ 语法

MUSA C++ Device Code 语法、并行原语、Tensor 编程、TME 与访存操作


## API 编程指南

Runtime API 与 Driver API 使用指南——设备管理、内存管理、内核启动、流与事件、错误处理


## 高级功能

MUSA Graphs 图模式编程、Green Context 轻量级执行上下文与 MP 资源隔离


## 性能优化

性能瓶颈分析 (计算/内存/延迟/同步绑定)、性能分析工具、内存/计算/归约/GEMM/Flash Attention 优化