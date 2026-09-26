source: https://docs.mthreads.com/musa-sdk/version-5.2.0/releasenote

# MUSA SDK v5.2.0 发布版本信息

## 下载链接[](https://docs.mthreads.com#下载链接)

## 发布说明[](https://docs.mthreads.com#发布说明)

MUSA SDK v5.2.0 围绕 MUSA Driver/Runtime、编译工具链、核心数学库、深度学习库、通信库和调试分析工具进行了能力扩展与稳定性提升，重点增强通用计算兼容能力、Graph 能力和编译器能力，升级 Triton 版本支持，扩展 Math-X API 覆盖，并完善 MCCL 通信能力与多平台部署验证。

本版本已完成多平台发布测试。测试结论显示，S5000 在 Intel、Hygon4、AMD 等 CPU 平台及 Alinux、VesselOS、Ubuntu、Kylin、Bclinux 等系统环境下功能可用，模型性能达标。部分 CTS 或专项测试存在已知问题，评估为不影响模型性能或不影响本次版本发布，作为 Open Issue 后续跟踪。

具体支持平台详见下方列表。

## 重��点更新内容[](https://docs.mthreads.com#重点更新内容)

- MUSA Graph 功能增强，新增 33 个 Graph API。
- 编译器功能增强，新增 46 个 FP128 相关 API 支持。
- Triton 生态支持增强，升级 Triton 兼容版本至 3.6.0。
- muDNN 新增 5 个 C 接口 API。
- 数学库功能增强，新增 17 个 muBLAS / muBLASLt API 支持，新增 8 个 muSOLVER API 支持。
- MCCL 支持 GPU 对等内存直接访问（DevComm / Window / LSA Pointer / Team-LSA），GPU 可直接读写其他 GPU 数据，通信可在 kernel 内部发起，降低 MoE 专家并行、投机解码等场景的通信延迟。

## 支持平台[](https://docs.mthreads.com#支持平台)

### S5000 支持平台[](https://docs.mthreads.com#s5000-支持平台)

MUSA SDK 支持 x86 架构 CPU，并通过 DEB 和 RPM 包覆盖多种 OS 组合。下述环境为推荐使用环境。


| CPU | OS | 内核版本 | MUSA SDK 包 |
|---|---|---|---|
| Intel | Alibaba Cloud Linux 3 (Soaring Falcon) | 5.10.134-13.al8.x86_64 | RPM |
| Intel | VesselOS 2.0 (LTS-SP2) | 6.6.0-100.jd_b007.x86_64 | RPM |
| Intel | Ubuntu 24.04.1 LTS | 6.8.0-124-generic | DEB |
| Intel | Ubuntu 22.04.4 LTS | 5.15.0-105-generic | DEB |
| Hygon4 | Ubuntu 22.04.4 LTS | 5.15.0-105-generic | DEB |
| AMD | Ubuntu 22.04.4 LTS | 5.15.0-105-generic | DEB |
| Hygon4 | Kylin Linux Advanced Server V10 (Halberd) | 4.19.90-89.11.v2401.ky10.x86_64 | RPM |
| Hygon4 | Kylin Linux Advanced Server V11 (Swan25) | 6.6.0-32.7.v2505.ky11.x86_64 | RPM |
| Hygon4 | BigCloud Enterprise Linux For Euler 21.10 LTS | 4.19.90-2107.6.0.0208.16.oe1.bclinux.x86_64 | RPM |

## 产品说明[](https://docs.mthreads.com#产品说明)

摩尔线程 MUSA SDK 是一套完整的 GPU 并行计算开发环境，专为利用摩尔线程 GPU 加速程序而设计。通过 MUSA SDK，用户可以基于摩尔线程 GPU 构建和部署高性能计算、人工智能训练与推理、科学计算、通信与多媒体等应用。

MUSA SDK 包含 GPU 加速库、调试和优化工具、C/C++ 编译器以及用于应用程序部署的运行时库等功能。作为一套完整的开发工具，MUSA SDK 包含以下主要组件：

- MUSA Toolkits：包含底层编译器、MUSA 运行时库、Musify 工具以及 MUSA-X 基础数学计算加速库。
- muDNN：MT GPU 深度学习加速库。
- MCCL：MT GPU 通信加速库。
- Triton-MUSA：支持在摩尔线程 GPU 上运行 Triton DSL。
- TileLang-MUSA：支持在摩尔线程 GPU 上运行 TileLang 相关工作负载。
- MATE：算子加速库。
- MUSA 工具链：包含 MUPTI、msys、mcu、MUSA Snapshot、MUSA sanitizer、MUSA gdb 等调试、分析与诊断工具。
- MUSA SDK 依赖摩尔线程 GPU 和摩尔线程 GPU 通用驱动程序，需要运行在带有摩尔线程 GPU 的服务器、工作站或 PC 中，并安装对应版本�的通用 Linux 驱动程序。

## 功能描述[](https://docs.mthreads.com#功能描述)

- 支持 SIMT (Single Instruction Multiple Thread) 架构并行编程模型。
- 提供 MUSA 编程语言配套编译器工具链
`mcc`

，用于将 MUSA 应用程序源码编译为可在 GPU 上执行的程序。 - 提供 MUSA Driver/Runtime，支撑基于 MT GPU 的完整运行环境。
- 提供 MUSA 数学库，包括 muBLAS、muRAND、muFFT、muSPARSE、muSOLVER、muPP、muThrust、muAlg 等。
- 提供 muDNN 深度学习加速库，支撑神经网络算子和模型训练、推理场景。
- 提供 MCCL 通信库，支持多 GPU、多节点通信原语和性能优化。
- 提供 Triton-MUSA 和 TileLang-MUSA，支撑大模型训练、推理和算子开发生态。
- 提供 MUPTI、msys、mcu、MUSA Snapshot、MUSA sanitizer 等调试、性能分析和诊断能力。

## 主要更新[](https://docs.mthreads.com#主要更新)

### 功能更新（Feature Updates）[](https://docs.mthreads.com#功能更新feature-updates)

#### MUSA Driver/Runtime[](https://docs.mthreads.com#musa-driverruntime)

- 支持 pfm dump 在 UserQ �模式下工作。
- MUPTI 支持 graph 粒度的 user queue graph trace。
- MUSA sanitizer 增强 spill、printf、VMM API 相关定位能力。
- 本版本验证 33 个 Graph API。
- 增强 MUSA Snapshot 功能，提升问题定位和可调试性。
- 下列能力以实验特性提供，后续版本将逐步转为正式发布能力：
- Error Log Management Functions
- Graph Management API support
- MTSHMEM DeepEP normal / ll_compatibility 相关能力


#### mtcc 编译工具链[](https://docs.mthreads.com#mtcc-编译工具链)

`use_fast_math`

编译选项对齐 NVCC 语义。- 支持 MTRTC。
- 新增 46 个 FP128 相关 API 支持。
- 支持
`-dc`

场景下的 MUSA automatic RDC。

#### Triton-MUSA[](https://docs.mthreads.com#triton-musa)

- 支持 Triton 3.2.0。
- 支持 Triton 3.6.0。

#### Math-X[](https://docs.mthreads.com#math-x)

- muBLAS / muBLASLt 新增 17 个 API 支持，增强 emulation 相关 API 能力，持续优化 VASP、HPC 等场景表现。
- muSOLVER 新增 8 个 API 支持。

#### muDNN[](https://docs.mthreads.com#mudnn)

- 新增
`mudnnGather`

、`mudnnUnfold`

、`mudnnScan`

、`mudnnWeightNorm`

和`mudnnL2Loss`

等 5 个 backend C API 支持。

#### MCCL[](https://docs.mthreads.com#mccl)

- 支持 MCCL Base Comm / CommProperties。
- 支持 MCCL DevComm / Window / LSA Pointer / Team-LSA。

#### Linux Driver[](https://docs.mthreads.com#linux-driver)

- 支持 EDC counter 相关变更。

## 已知问题与限制[](https://docs.mthreads.com#已知问题与限制)

当 `mtbios`

> `4.3.43`

时，EDC counter 相关变更需要 Linux Driver 5.2.0、dcgm 1.1.6 和 mtml 2.4.2 配合使用。

## 产品组件版本说明[](https://docs.mthreads.com#产品组件版本说明)

| 组件 | 版本 |
|---|---|
| MT Linux Driver | 5.2.0 |
| MUSA Toolkit | 5.2.0 |
| muDNN | 3.4.0 |
| MCCL | 2.4.0 |
| Triton-MUSA | 3.6.0 |
| TileLang-MUSA | 0.1.8 |
| MATE | 0.2.3 |