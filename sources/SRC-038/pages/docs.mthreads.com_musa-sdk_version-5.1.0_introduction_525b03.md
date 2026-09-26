source: https://docs.mthreads.com/musa-sdk/version-5.1.0/introduction

# 摩尔线程 MUSA 软件开发集成套件

## MUSA[](https://docs.mthreads.com#musa)

MUSA 软件是摩尔线程 GPU 并行计算编程语言，面向使用对象是并行计算程序的开发人员，建立摩尔线程 GPU 与并行计算程序之间的桥梁。

### MUSA Toolkits：摩尔线程 MUSA 开发工具包[](https://docs.mthreads.com#musa-toolkits摩尔线程-musa-开发工具包)

为了给开发人员提供了完备的编译器、运行时库、计算加速库、调试和分析工具等内容，MUSA Toolkits 将上述内容打包到一起，并提供二进制的一键安装方式。在安装 MUSA Toolkits 后，开发者可直接进行 MUSA 语言的并行计算编程和调试等工作。

### MUSA-X Library：摩尔线程 MUSA 计算加速库[](https://docs.mthreads.com#musa-x-library摩尔线程-musa-计算加速库)

为了能够让一些并行计算达到更好的加速效果，摩尔线程提供了一系列的计算加速库。

摩�尔线程 MUSA 计算加速库 MUSA-X Library 包括：

- MUSA 深度神经网络加速库，MUSA DNN Library，简称 muDNN
- MUSA 基础线性代数加速库，MUSA BLAS Library，简称 muBLAS
- MUSA 伪随机数生成加速库，MUSA RAND Library，简称 muRAND
- MUSA 傅立叶变换加速库，MUSA FFT Library，简称 muFFT
- MUSA 稀疏矩阵加速库，MUSA SPARSE Library，简称 muSPARSE
- MUSA 线性代数求解加速库，MUSA SOLVER Library，简称 muSOLVER
- MUSA 图像及信号处理加速库，MUSA Performance Primitives Library，简称 muPP
- MUSA Thrust 并行计算加速库，MUSA Thrust Library，简称 muThrust

### MUSA SDK：摩尔线程 MUSA 软件开发集成套件[](https://docs.mthreads.com#musa-sdk摩尔线程-musa-软件开发集成套件)

摩尔线程 MUSA 软件开发集成套件，提供完整的基于摩尔线程 GPU 的 MUSA 并行计算和人工智能开发、运行环境。集成了 MUSA Toolkits，MCCL，muDNN，MUSA-X Library 等内容于一体。

### Moore Perf Tools：摩尔线程 MUSA 应用程序性能分析工具[](https://docs.mthreads.com#moore-perf-tools摩尔线程-musa-应用程序性能分析工具)

[Moore Perf Tools](https://developer.mthreads.com/musa/moore-perf-tools) 是摩尔线程推出的低开销 GPU 性能分析工具套件，帮助开发人员深入分析 MUSA 应用程序和 Graphics 应用程序的性能瓶颈，并提供调试与性能优化能力。该工具套件包括面向 Compute 应用程序深度分析的 Moore Perf Compute，以及面向通用应用程序分析的 Moore Perf System。

## 当前版本[](https://docs.mthreads.com#当前版本)

MUSA 计算通过 MUSA SDK 统一提供软件产品能力，当前最新版本为 MUSA SDK 5.1.0。