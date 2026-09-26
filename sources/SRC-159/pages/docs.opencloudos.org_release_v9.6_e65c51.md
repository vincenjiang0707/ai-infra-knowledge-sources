source: https://docs.opencloudos.org/release/v9.6/

# OpenCloudOS 9 Update 6 发行说明

OpenCloudOS 9 Update 6（OC9.6）是 OpenCloudOS 9 系列的重要更新版本。此次更新为 OpenCloudOS 9 系列引入了内核增强功能和关键安全修复，升级了编程语言运行时，对软件包进行了精细优化，全面升级容器和云原生生态，为用户带来更加稳定、高效的使用体验。

## 1. 下载体验

### 安装镜像与 YUM 源

OpenCloudOS 9.6 的安装镜像及 YUM 源软件包可从 OpenCloudOS 镜像站获取：

https://mirrors.opencloudos.tech/opencloudos/9.6/

该目录下提供适用于不同场景的 ISO 安装镜像及在线安装所需的仓库内容，用户可根据自身环境选择合适的镜像进行下载和部署。

#### ISO 镜像

OpenCloudOS 9 提供以下几种 ISO 类型：
- **boot.iso**：用于启动安装，需要联网加载软件包，适合网络安装。
- **everything.iso**：包含完整软件包集合的安装镜像，适合离线安装或本地源部署。
- **minimal.iso**：精简安装镜像，仅包含基础系统组件，适合构建最小化系统。

下载地址：https://mirrors.opencloudos.tech/opencloudos/9.6/isos/

#### QCOW2 镜像

OpenCloudOS 9 提供标准 QCOW2 格式的通用虚拟机镜像，适用于 KVM 等虚拟化环境。

下载地址：https://mirrors.opencloudos.tech/opencloudos/9.6/images/qcow2/

#### Docker 镜像

容器镜像 tar 包下载地址：https://mirrors.opencloudos.tech/opencloudos/9.6/images/docker/

通过镜像站 docker pull 获取（以下镜像标签均为 latest，会随最新版本更新）：

-
**Minimal 镜像**

使用命令：`docker pull opencloudos/opencloudos9-minimal:latest`


Minimal 镜像使用 dnf（yum）作为包管理器，并提供 coreutils 作为基础 Linux 工具集，是具备完整包管理功能的最小镜像。常规情况下推荐优先使用该镜像。 -
**Init 镜像**

使用命令：`docker pull opencloudos/opencloudos9-init:latest`


Init 镜像在 Minimal 基础上集成 systemd，支持容器内运行系统服务，适合需要完整 init 系统的场景。 -
**MicroDNF 镜像**

使用命令：`docker pull opencloudos/opencloudos9-microdnf:latest`


MicroDNF 镜像使用轻量级 microdnf 包管理器，镜像体积更小，适合对镜像大小敏感的场景。 -
**Busybox 镜像**

使用命令：`docker pull opencloudos/opencloudos9-busybox:latest`


Busybox 镜像是最精简的容器镜像，仅包含 busybox 工具集，适合静态编译应用或极简运行环境。

更多小型化容器镜像和 AI 容器镜像，请访问：https://hub.docker.com/u/opencloudos 查看（所有容器镜像的 latest 标签会随最新版本更新）。

### 在已有 OpenCloudOS 9 系统上升级至 OC9.6

在 OpenCloudOS 9 系统配置中，版本 "9" 是一个软链接，当前指向最新的 9.6 版本。这种方式确保系统始终使用最新版本的软件包和安全更新。如果你当前已在运行 OpenCloudOS 9，系统会自动切换至指向 9.6 的最新版本，同时保持对核心应用和服务的兼容支持。

执行以下命令更新系统软件包：

```
sudo dnf update
```


## 2. 内核

### kernel 6.6.119

OpenCloudOS 9 Update 6 搭载 **Linux Kernel 6.6.119**，在上游 6.6 LTS 稳定分支的基础上，从 6.6.80 升级至 6.6.119，累计合入 39 个补丁版本的更新，并深度集成了 OpenCloudOS Kernel SIG 的自研增强特性。

#### 2.1 性能优化

**调度器增强：**
- EEVDF 公平调度算法进一步完善。
- 引入 FAIR_SLEEPERS 调度特性，改善延迟敏感型负载的响应表现。
- SCX 可扩展调度器框架优化，为用户态调度提供更灵活的接入能力。
- CPU idle 调优与 SMT 抗干扰优化。
- 支持 NUMA aware spinlock，降低跨 NUMA 节点的锁竞争开销。

**内存管理优化：**
- 引入 Swap Table 特性，大幅提升 swap 性能。
- 支持多种 size 的透明大页（mTHP），覆盖匿名页与 swap 场景。
- per-vma lock 改进（MADV_FREE/DONTNEED 场景），减少内存操作延迟。
- 引入虚拟 NUMA（numa=fake）功能，缓解单 NUMA 众核环境下的 zone lock 竞争，支持 numa=fake=4C 语法，使不同 CPU 的内存申请均衡分布于各 fake NUMA node。
- per-CPU pagelist（PCP）改进。
- objcg 内存统计性能提升。
- zsmalloc 锁竞争优化。

**I/O 优化：**
- NVMe 中断汇聚支持，提升 NVMe 设备吞吐量，改善 8KB 以下随机写性能。
- 支持 uncached buffer I/O。
- AF_XDP 性能优化。
- XFS pread 性能提升。
- batch TLB flush 优化页面回收路径。

**CPU 与系统优化：**
- PSI（Pressure Stall Information）底噪降低，支持动态开关。
- pipe 锁竞争优化。

#### 2.2 安全特性

**Landlock 安全沙箱**：默认开启 Landlock 安全模块，为进程提供细粒度的文件系统和网络访问控制能力，无需 root 权限即可构建安全隔离环境，适用于 AI 编程等场景。**AMD SEV-SNP**：支持 AMD SEV-SNP（Secure Encrypted Virtualization-Secure Nested Paging）Host 侧及 Guest 侧完整功能，增强虚拟机内存加密隔离性。**ARM CCA**：ARM64 平台支持机密计算架构（Confidential Compute Architecture），增强 ARM 平台的可信执行能力。

#### 2.3 可观测性与维测增强

**early OOM 机制**：支持全局与 per-memcgroup 的 early OOM，允许用户配置内存使用比例阈值，在达到阈值时内核主动触发 OOM，避免系统陷入严重内存压力。**RCU stall 增强**：开启 CONFIG_RCU_CPU_STALL_CPUTIME，RCU stall 时可输出硬中断、软中断、内核态线程上下文的实际占用耗时，便于定位 CPU 占用异常。**hungtask 维测**：支持 hungtask 发生时打印 rwsem owner、sem owner 等锁持有者信息，便于快速定位死锁成因。**softlockup 增强**：softlockup 检测时增加中断风暴识别能力，快速区分 CPU 占用来源。**CSD lock 维测**：支持 CSD lock 长时间等待时的诊断信息输出。**printk 调用者信息**：内核 printk 支持附加调用者信息（caller_id），提升日志的可追溯性。**kfence 增强**：支持基于采样的内存越界检测，显著降低运行时开销。**内核 panic 增强**：支持配置 panic 时打印更多内核上下文信息。

#### 2.4 新硬件与驱动支持

**海光（Hygon）：**
- 支持 Hygon family 18h model 8h、18h 等新款处理器。
- CSV3 虚拟化增强：Hostdata 支持、共享内存管理、热迁移（vtkm live migration）、1G 大页 Guest 私有内存。
- 海光大内存快速拷贝功能；HCT 加密驱动升级至 0.6；perf mem/c2c load/store 事件映射支持。

**ARM 平台（鲲鹏/飞腾）：**
- 支持鲲鹏 950（Kunpeng 950）新芯片，覆盖 cpufreq、PCIe、ext-GPU、soc_cache、power_meter、perf、SDEI watchdog、FEAT_NMI、DDRC 等核心子系统。
- 鲲鹏 920 支持快速页拷贝加速。
- 飞腾平台支持 PCI 热插拔 workaround 及 PSWIOTLB 机制，提升 DMA 性能。
- AArch64 支持 2023 DPISA 扩展、FEAT_HDBSS（Armv9.5）及 AArch64 Rust 语言支持。

**龙芯（LoongArch）：**
- 支持龙芯 3C6000 多节点 AVEC 中断控制器功能增强。
- 新增龙芯 TPM 驱动支持。
- 支持 cbc(sm4) 加密算法、EDAC 错误检测、SM3/SM4 国密算法、EFI RTC 及 mem 内核参数。

**Intel：**
- 支持 CWF（Clearwater Forest）、DMR 等新平台。
- 新增 PLR（Power Limit Reasons）TPMI 驱动；支持 uncore-freq 效率延迟控制。
- 回移 Intel pstate/TPMI 驱动，增强 Intel 处理器电源管理能力。

**AMD：**
- 支持 AMD Zen6（Venice）CPU。
- 增强了对 Zen6 CPU Perf、MCE、EDAC、AMD_NB、HSMP 等模块的支持。

**其他 CPU：**
- 新增申威（sw64）架构支持。
- 支持兆芯 KH-50000 芯片。

**网卡驱动：**
- 网讯（wangxun）1G/10G/25G/40G 全系网卡驱动支持。
- 新增 mucse 网卡驱动、linkdata sxe/sxevf 网卡驱动。
- 博通 bnxt_en 商用网卡驱动升级。
- 支持 3SNIC 3S5XX/910/920/930 系列 RAID/HBA 及网卡控制器。

**其他驱动：**
- 新增 linkdata ps3stor SCSI 驱动。

#### 2.5 重要 Bug 修复

- 修复 block 层判断驱动返回值不当，导致可能数据丢失的问题。
- 修复 ext4 磁盘空闲块查找耗时过长导致 IO 卡顿的问题。
- 修复 NVMe 热拔插后传输速度从 32G 降至 2.5G 且需重启才能恢复的问题。
- 修复 MGLRU 在高内存压力下并行内存回收造成 memcg OOM 的问题。
- 修复 mem cgroup 中 dirty pagecache 尚未回收导致 OOM 的问题。
- 修复 br_netfilter 与 net.bridge.bridge-nf-call-iptables=1 同时启用导致容器网络不通的问题。
- 修复 /proc/stat 中 processes 计数出现负数的问题。
- 修复光盘刻录引起内核死锁的问题。
- 修复 mem_cgroup_bind_blkio_write 中等待 cgroup_mutex 导致死锁的问题。
- 修复内核 MAX_ARG_STRLEN 宏重定义导致外部模块编译链接失败的问题。
**Crypto 子系统大量修复**：修复 algif_aead 解密 RX 大小检查、页面重新分配溢出问题，authencesn 偏移量、AAD 长度验证、AEAD 解密问题。**架构配置更新**：x86 启用 CONFIG_MICROCODE_LATE_LOADING（微码后期加载），RISC-V 调整 CONFIG_RXKAD 配置，修改 CONFIG_CHR_DEV_SG 磁盘子系统配置。**安全修复**：xfrm esp 避免共享 skb frags 的原地解密。- 修复大量社区 CVE 漏洞，如 CVE-2026-31431、CVE-2026-43284 等。

## 3. AI 大模型生态

### 3.1 AI 软件栈

#### AI 软件栈支持概览

OpenCloudOS 9 通过 EPOL 仓库提供主流 AI 计算硬件的驱动与软件栈支持，覆盖 NVIDIA、AMD、昇腾、海光、沐曦、昆仑芯、紫霄、天数智芯、寒武纪等厂商。

| 硬件厂商 | 支持型号/系列 | 软件栈组件 | 驱动版本 | 关键软件包名 | 状态管理工具 |
|---|---|---|---|---|---|
| NVIDIA | HCCPNV6/PNV6、PNV5b、L40、T4等 | GPU 驱动 + CUDA cuDNN / NCCL / cuSPARSELt（详见下方附表） | 驱动：525 ~ 595 CUDA：11.8 ~ 13.2 | nvidia-driver-{版本}（专有） nvidia-driver-{版本}-open（开源） cuda-toolkit-11-8 ~ cuda-toolkit-13-2 |
nvidia-smi |
| AMD | MI300系列、MI308x | ROCm 软件栈 | 7.0.2.70002 | rocm amdgpu-dkms | amd-smi |
| 昇腾 | Ascend910B 系列 | HDK 驱动 + CANN | 25.2.0 | Ascend910B-driver Ascend910B-firmware Ascend-cann-toolkit Ascend-cann-kernels | npu-smi |
| 海光 | BW1000 DCU Z100 / K100 / K100_AI | DTK 软件栈 | 6.3.16 | hygon-driver | hy-smi |
| 沐曦 MetaX | 曦云 C500 / C500-E / C550 / C550-E 曦云 C588 / C600 曦思 N260 | MXMACA SDK 软件栈 | 3.1.0.26 | metax-driver maca_sdk | mx-smi |
| 昆仑芯 | P600 / P800 / P900 | XRE + XDR 软件栈 | 随仓库版本更新 | 昆仑芯 XRE / XDR 软件包暂未上线软件源 | - |
| 紫霄 | 紫霄 V1 / V2 | TopsRider 计算框架 LightRuntime 推理软件栈 | 随仓库版本更新 | 紫霄驱动及运行时软件包暂未上线软件源 | - |
| 天数智芯 | 智铠 100 | 全栈软硬件适配软件包 | 随仓库版本更新 | 天数智芯驱动及开发运行环境软件包暂未上线软件源 | - |
| 寒武纪 | MLU590 | 寒武纪计算卡软件栈 | 随仓库版本更新 | 寒武纪驱动及软件栈软件包暂未上线软件源 | - |

#### NVIDIA 扩展组件详情（cuDNN / NCCL / cuSPARSELt）

以下组件按 CUDA 版本分包，安装时需与对应 CUDA 版本配套使用：

| 组件 | 版本/组合 | CUDA 适配范围 | 软件包名 | 说明 |
|---|---|---|---|---|
| cuDNN（GPU 深度神经网络库） | cudnn9-cuda-13 | CUDA 13.x | cudnn9-cuda-13 | cuDNN 9.x for CUDA 13.x（推荐，最新） |
| cuDNN（GPU 深度神经网络库） | cudnn9-cuda-12 | CUDA 12.x | cudnn9-cuda-12 | cuDNN 9.x for CUDA 12.x |
| cuDNN（GPU 深度神经网络库） | cudnn8-cuda-12 | CUDA 12.x | cudnn8-cuda-12 | cuDNN 8.x for CUDA 12.x（停止更新） |
| cuDNN（GPU 深度神经网络库） | cudnn9-cuda-11 | CUDA 11.x | cudnn9-cuda-11 | cuDNN 9.x for CUDA 11.x（停止更新） |
| cuDNN（GPU 深度神经网络库） | cudnn8-cuda-11 | CUDA 11.x | cudnn8-cuda-11 | cuDNN 8.x for CUDA 11.x（停止更新） |
| NCCL（多 GPU 通信库） | nccl-cuda-12.0 | CUDA 12.0~ 12.7 | nccl-cuda-12.0 | 适用旧版 GPU |
| NCCL（多 GPU 通信库） | nccl-cuda-12.8 | CUDA 12.8~ 13.x | nccl-cuda-12.8 | 适用新版 GPU |
| cuSPARSELt（稀疏计算库） | 0.6.x | CUDA 12.x | libcusparselt0-12 | 稀疏矩阵计算加速库 |

上述 AI 软件栈 RPM 包均通过 EPOL 软件源发布。安装前请先执行以下命令配置好 EPOL 软件源，之后即可直接使用 dnf 安装所需组件：

```
sudo dnf install epol-release epol-extras-release
```


### 3.2 AI 容器概览

#### 3.2.1 基础 SDK 容器

OpenCloudOS 9 已实现对 NVIDIA 等主流 GPU 的深度适配和原生支持，为用户提供一键部署、开箱即用的基础 SDK 容器。

| 厂商 | 容器镜像 | 版本 | 组件范围 | 适用场景 |
|---|---|---|---|---|
| NVIDIA | cuda-runtime | 12.0 ~ 12.9（分支默认支持最新小版本，后续支持 13.x） | 可执行文件 + .so 动态库 | 轻量级生产部署 |
| NVIDIA | cuda-devel | 12.0 ~ 12.9（分支默认支持最新小版本，后续支持 13.x） | runtime + 头文件 + .a 静态库 | 代码编译/模型训练 |
| NVIDIA | cuda-toolkit | 12.0 ~ 12.9（分支默认支持最新小版本，后续支持 13.x） | devel + Nsight 性能分析工具 | 性能调优/算法研究 |

#### 3.2.2 AI 框架容器

在基础 SDK 容器镜像之上，OpenCloudOS 9 结合硬件实现了对 AI 热门框架的开箱即用镜像，方便用户快速部署，一键拉起运行环境。

| AI 框架 | 硬件支持 | 获取方式 |
|---|---|---|
| TensorFlow | nvidia / hygon | docker pull opencloudos/opencloudos9-tensorflow:latest |
| PyTorch | nvidia | docker pull opencloudos/opencloudos9-pytorch:latest |
| PaddlePaddle | nvidia / hygon / muxi | docker pull opencloudos/opencloudos9-paddlepaddle:latest |
| TensorRT-LLM（TensorRT） | nvidia | docker pull opencloudos/opencloudos9-tensorrt_llm:latest |
| vLLM | nvidia / hygon / muxi | docker pull opencloudos/opencloudos9-vllm:latest |
| SGLang | nvidia / hygon / muxi | docker pull opencloudos/opencloudos9-sglang:latest |
| Transformers | nvidia / hygon | docker pull opencloudos/opencloudos9-tf-ds:latest |
| DeepSpeed | nvidia / hygon / muxi | docker pull opencloudos/opencloudos9-tf-ds:latest |
| 优图Agent（Youtu-Agent） | nvidia | docker pull opencloudos/opencloudos9-youtu:latest |
| LangChain | nvidia | docker pull opencloudos/opencloudos9-langchain:latest |

#### 3.2.3 Agent 容器

针对近期热门的 Agent 应用场景，OpenCloudOS 9 已推出 Agent 基础环境镜像及各大热门 Agent 开箱即用容器镜像，并重点支持 OpenClaw，用户无需繁琐配置，即可快速搭建环境、一键体验热门 Agent 产品。

| 镜像 | 组件范围 | 获取方式 |
|---|---|---|
| Agent use | 集成 XFCE、Xvfb 和 Chromium 的通用 AI Agent 基础运行环境 | docker pull opencloudos/opencloudos9-agent-use:latest |
| Browser use | 内置 Chromium 与核心工具链的 Browser-use 镜像 | docker pull opencloudos/opencloudos9-browser-use:latest |
| Android world | 内置 Android 手机模拟器与相关工具链的 Mobile-use 镜像 | docker pull opencloudos/opencloudos9-android-world:latest |
| OpenClaw | 基于 agent-use 封装、预置 QQ 等多个主流 IM 平台插件的 OpenClaw 镜像 | docker pull opencloudos/opencloudos9-openclaw:latest |

## 4. 编程语言与运行时

### golang 1.25.8

- Golang 从 1.22.10 升级到
**1.25.8**，跨越 1.23、1.24、1.25 三个次版本。 **安全修复**：修复 16+ 个安全漏洞，包括 CVE-2025-58183、CVE-2025-58186、CVE-2025-58187、CVE-2025-58189、CVE-2025-61723 至 CVE-2025-61731、CVE-2025-68119、CVE-2026-27140、CVE-2026-34040 等**核心包安全增强**：修复 archive/tar、crypto/tls、crypto/x509、encoding/asn1、net/http、net/mail、html/template、os 等多个核心包的安全问题**编译器增强**：使用 GOEXPERIMENT=nodwarf5 提升 debugedit 兼容性**重要修复**：CGO 信任边界绕过漏洞（CVE-2026-27140）

### nodejs 20.20.0

- 从 Node.js 18.20.4 升级至
**Node.js 20**LTS 版本，这是一次主版本升级。 **权限模型（Permission Model）**：可限制程序对文件系统、子进程、Worker 线程等资源的访问，增强运行时安全性**V8 JavaScript 引擎升级**：升级至 V8 11.3，性能进一步提升**loader hooks API 稳定化**：改善模块加载的扩展能力**实验性 WebAssembly tail call 支持**- 同时提供
**nodejs20**独立软件包，当前 nodejs 是虚包，其依赖 nodejs20 填充

### php 8.3.20

- 从 8.3.10 升级至 8.3.20，跨越 10 个补丁版本的累积更新。
**适配 php-sodium 加密扩展**，增强加密功能支持**安全修复**：修复 9+ 个安全漏洞，包括：- CVE-2022-31628、CVE-2022-31629、CVE-2022-31630、CVE-2022-31631
- CVE-2024-3096
- CVE-2024-11235（引用计数导致 UAF）
- CVE-2025-1220（null byte 终止）
- CVE-2025-6491（SOAP 扩展空指针）
- CVE-2025-14180（堆缓冲区溢出）
**性能优化**：改进 Opcache JIT 编译器性能**稳定性增强**：修复 PDO/PGSQL/SQLite3 数据库扩展的内存泄漏和类型混淆问题，增强 HTTP 流包装器安全性

### Java（KonaJDK）

KonaJDK 是基于 OpenJDK 构建的优化版本，内置国密算法（SM2/SM3/SM4）支持，并针对 LoongArch、AArch64 等国产架构进行了专项优化。本次更新覆盖多个主流 LTS 版本。

#### java-8-konajdk 8.0.25

- 从 8.0.20 升级至 8.0.25，在 JDK 8 LTS 分支内跨越 5 个补丁版本。
- 修复多个 CVE 安全漏洞，增强 JVM 稳定性。
- 改进向后兼容性，确保老旧应用的平滑运行。
- 内置国密算法（SM2/SM3/SM4）支持。
- 包含针对龙芯等国产架构的性能优化。

#### java-11-konajdk 11.0.30

- 从 11.0.25 升级至 11.0.30，在 JDK 11 LTS 分支内跨越 5 个补丁版本。
- 修复多个 CVE 安全漏洞，改进 JVM 性能。
- 增强 TLS 加密支持，提升通信安全性。
- 内置国密算法（SM2/SM3/SM4）支持。
- 包含针对 LoongArch、AArch64 等国产架构的专项优化。

#### java-17-konajdk 17.0.17

- 从 17.0.14 升级至 17.0.17，在 JDK 17 LTS 分支内跨越 3 个补丁版本。
- 修复多个 CVE 安全漏洞，改进垃圾回收器性能。
- 增强密码学功能，提升加密操作效率。
- 内置国密算法（SM2/SM3/SM4）支持。
- 针对 LoongArch、AArch64 等国产架构进行了专项优化。

#### java-21-konajdk（EPOL 仓库）

通过 EPOL 仓库，OpenCloudOS 9.6 额外提供 **java-21-konajdk** 支持，这是 OpenJDK 21 LTS 版本的优化实现：

**获取方式**:`sudo dnf install epol-release epol-extras-release sudo dnf install java-21-konajdk`

**版本**: 基于 OpenJDK 21 LTS**特性**:- 针对 LoongArch、AArch64 等国产架构的专项优化
- Virtual Threads（虚拟线程）支持，大幅提升并发性能
- Record Patterns 和 Pattern Matching for switch 等现代 Java 特性
**适用场景**: 需要较新 Java 特性的现代应用开发

## 5. 数据库

### mariadb 10.11.15

- 从 10.11.4 升级至 10.11.15，在 LTS 分支内包含 11 个补丁版本的累积更新。
- 修复大量安全漏洞，提升数据库安全性。
- 改进 InnoDB 存储引擎性能，提升事务处理效率。
- 增强 Galera Cluster 多主集群的稳定性与兼容性。

### mysql 8.0.45

- 从 8.0.41 升级至 8.0.45，在 8.0 LTS 分支内包含 4 个补丁版本的累积更新。
- 修复多个安全漏洞，增强数据库安全性。
- 改进 InnoDB 性能，优化大事务处理能力。
- 优化复制功能，提升主从同步稳定性。

### postgresql 15.16

- 从 15.12 升级至 15.16，在 15 LTS 分支内跨越 4 个补丁版本。
- 修复查询优化器 bug，改进复杂查询的执行计划。
- 改进复制稳定性，增强高可用场景的可靠性。
- 修复多个安全问题。

## 6. Web 服务与框架

### httpd 2.4.67

- 从 2.4.57 升级至 2.4.67，跨越 10 个次版本的累积更新。
**安全修复**：修复 13 个 CVE 安全漏洞，包括 CVE-2025-55753、CVE-2025-58098 等**HTTP/2 性能优化**：改进 HTTP/2 处理性能，提升高并发下的响应能力**mod_ssl 增强**：增强 mod_ssl 功能与稳定性，增加对 sscg 的依赖，支持自签名证书的自动生成

### nginx 1.26.3

- 从 1.26.2 升级至 1.26.3，在稳定分支内的补丁版本更新。
- 修复 HTTP/3 QUIC 连接处理问题。
- 改进 SSL/TLS 性能。
- 修复若干稳定性 bug。

### tomcat 9.0.117

- 从 9.0.86 升级至 9.0.117，跨越 31 个补丁版本。
**新特性**：引入 CSRF 防护过滤器路径白名单、Manager 应用 JSON 输出、自定义 SSLContext 配置、Cookie partitioned 属性**关键修复**：修复 TLS 热重载稳定性问题、WebSocket 连接释放异常、FORM 登录超时恢复等关键问题

### python-django 5.2.11

- 从 5.0.8 升级至 5.2.11，跨越 5.1 和 5.2 两个大版本。
**安全修复**：修复 CVE-2025-14550、CVE-2026-1207、CVE-2026-1285、CVE-2026-1287、CVE-2026-1312 等多个安全漏洞

### mod_security 2.9.9

- 从 2.9.6 升级至 2.9.9，跨越 3 个补丁版本。
- 改进规则引擎的正则表达式处理逻辑，提升检测准确率。
- 增强 Web 应用防火墙的安全日志功能，改善审计能力。
- 提升规则检测准确性，降低误报率。

## 7. 密码学与安全库

### nss 3.112

- 从 3.105 升级至 3.112，跨越 7 个小版本。
**后量子密码学支持**：引入 ML-KEM-768 混合密钥交换算法，增强 TLS 通信对量子计算威胁的抵御能力**PKCS#8 改进**：改进 PKCS#8 私钥导入流程，提升安全性**国密算法增强**：增强 SM2/SM3 国密算法支持**SSL/TLS 配置灵活性提升****安全修复**：修复证书处理和 ASN.1 解码中的安全问题

### nspr 4.36

- Netscape Portable Runtime（NSPR）是 NSS 密码学库的底层运行时基础，提供跨平台的线程、I/O、网络等抽象接口。
- 从 4.35 升级至 4.36。
- 改进多线程支持，修复内存管理问题。
- 增强跨平台兼容性，为 NSS 和 Mozilla 相关组件提供更稳定的底层运行时基础。

### opensc 0.26.0

- 从 0.25.0 升级至 0.26.0，次版本升级。
**安全修复**：修复 7 个 CVE 安全漏洞（CVE-2024-45615、CVE-2024-45616、CVE-2024-45617、CVE-2024-45618、CVE-2024-45619、CVE-2024-45620、CVE-2024-8443）**功能增强**：- PKCS#11 客户端能力升级：AES CMAC、AES GCM、RSA OAEP、HKDF、EdDSA 支持
- PKCS#11 工具改进：列出令牌时显示 URI，移除 5000 字节对象大小限制
- 驱动程序改进：PIV 卡、IDPrime、D-Trust 等多种智能卡驱动增强

### keylime 7.12.2

- 从 7.11.0 升级至 7.12.2，跨越 1 个次版本。
**安全修复**：修复 CVE-2025-13609、CVE-2026-1709 等安全漏洞**TPM 2.0 增强**：改进 TPM 2.0 支持，增强 Agent 性能**稳定性提升**：改进集群部署下的稳定性

### lasso 2.9.0

- Lasso 是 SAML 2.0 / Liberty Alliance 协议的实现库，用于企业级单点登录（SSO）和联邦身份认证。
- 从 2.8.2 升级至 2.9.0，跨越 1 个次版本。
- 改进 XML 签名验证逻辑，增强安全性。
- 增强 SAML 断言处理能力，提升单点登录（SSO）场景的兼容性。
- 修复身份认证流程中的安全问题，提升企业 SSO/SAML 场景下的可靠性。

### freeipa 4.12.5

- FreeIPA 是企业级身份管理系统，集成了 LDAP、Kerberos、DNS 和 CA 等身份认证与访问控制组件。
- 从 4.12.2 升级至 4.12.5，在 4.12 分支内跨越 3 个补丁版本。
- 修复 Kerberos 认证问题，提升认证成功率。
- 改进 LDAP 复制稳定性，增强多节点身份管理可靠性。
- 增强 Web UI 功能，改善管理员操作体验。

## 8. 容器与云原生

### moby 29.3.1

- Docker Engine 进行了主版本升级，从 27.3.1 升级至
**29.3.1**，跨越 28 和 29 两个主版本。 **网络功能增强**：增强 IPv6 支持，默认为 Linux 桥接网络启用 ip6tables 并支持直接路由**lazy pulling 优化**：引入容器镜像 lazy pulling 优化，显著加快大镜像的启动速度**BuildKit 性能提升**：改进了 BuildKit 构建性能，提升容器镜像构建效率**网络插件增强**：增强了网络插件接口，提升容器网络的可扩展性**新增特性**：新增卷子路径挂载支持和容器健康检查改进- 包含功能增强和安全修复

### containerd 1.7.29

- 在 1.7 LTS 分支内从 1.7.3 升级到 1.7.29，跨越 26 个补丁版本的累积更新。
**安全修复**：修复 CVE-2024-40635、CVE-2025-23329 等安全漏洞**兼容性改进**：新增 containerd.io 的 provides 支持，改进兼容性**CRI 性能优化**：改进 CRI 插件性能，增强镜像拉取的稳定性

### buildah 1.41.4

- 从 1.37.5 升级至 1.41.4，跨越近 4 个版本的功能迭代。
**安全修复**：修复 CVE-2025-47913（x/crypto 漏洞）、CVE-2025-52881 等安全漏洞**runc 升级**：同步升级底层 runc 依赖至 1.3.3+**BuildKit 优化**：改进 BuildKit 构建后端性能**稳定性增强**：增强容器镜像构建的稳定性与兼容性

### etcd 3.5.28

- 从 3.5.7 升级至 3.5.28，在 3.5 分支内跨越 21 个补丁版本的长跨度累积更新。
- 修复多个安全漏洞。
- 改进 Raft 共识协议性能，提升集群选举效率。
- 增强集群稳定性，改善高负载下的表现。

### netavark 1.16.0

- 从 1.12.2 升级至 1.16.0，跨越 4 个次版本。
- 增强 IPv6 支持，修复 IPv6 网络配置相关 bug。
- 改进网络插件接口，提升扩展性。
- 优化容器网络性能，降低网络延迟。
- 修复多个网络配置相关的稳定性问题。

### aardvark-dns 1.16.0

- 从 1.12.2 升级至 1.16.0，跨越 4 个次版本。
- 1.13 版本为容器名称设置 DNS TTL 为 0，确保 DNS 记录及时刷新。
- 1.13 版本限制解析器数量，优化高并发下的 DNS 查询性能。
- 1.14–1.16 修复 IPv6 链路本地地址解析问题。
- 改进错误处理逻辑，增强异常场景下的稳定性。
- 增强日志记录能力，便于问题排查。

### bubblewrap 0.11.0

- 从 0.10.0 升级至 0.11.0。
- 改进 namespace 隔离机制，增强容器沙箱的安全隔离性。
- 修复若干 namespace 相关的 bug。

### conmon 2.1.13

- 从 2.1.10 升级至 2.1.13，跨越 3 个补丁版本。
- v2.1.11 添加 s390x 架构支持。
- v2.1.11 移除 libsystemd-journal 依赖，改用更轻量的 libsystemd。
- v2.1.12 同步 CentOS Stream 10 配置。
- v2.1.13 确保时间戳生成永不失败，提升记录可靠性。
- v2.1.13 将日志文件权限从 0600 调整为 0640，符合最小权限原则。
- v2.1.13 移除多余的 fsync 调用，提升 I/O 性能。

## 9. 图形与多媒体

### firefox 140.10.0

- 从 128.7.0 升级至
**140.10.0**，升级至 ESR 140 系列，这是扩展支持版本（Extended Support Release）的一次重要大版本升级。 **安全修复**：修复 200+ 个 CVE 安全漏洞，涵盖内存安全、沙箱逃逸等高危问题**渲染引擎优化**：性能和稳定性全面提升

### babl 0.1.118

- 从 0.1.102 升级至 0.1.118，跨越 16 个次版本。
- 新增多种色彩空间支持，增强图像处理覆盖范围。
- 改进像素格式转换性能，提升图像处理效率。
- 适配 GIMP 3.0，保持 GIMP 生态版本同步。
- 修复 CVE-2025-2760 安全漏洞（配合 gimp-3.0）。

### gegl04 0.4.66

- 从 0.4.48 升级至 0.4.66，跨越 18 个次版本。
- 新增多种图像滤镜，丰富图形处理能力。
- 改进 GPU 加速处理能力，提升大图处理效率。
- 适配 GIMP 3.0 生态，保持版本同步。

### gjs 1.84.1

- 从 1.74.1 升级至 1.84.1，跨越 10 个次版本。
- 升级内置 SpiderMonkey JavaScript 引擎，提升 JS 运行性能。
- 改进 ES 模块支持，增强模块化开发能力。
- 改善与 GObject 的集成能力，适配 GNOME 45/46。

### mozjs 128.14.0（新增）

- SpiderMonkey JavaScript 引擎，作为 GNOME Shell、GJS（GNOME JavaScript bindings）、Polkit 等桌面组件的底层脚本引擎依赖。
- 由原 mozjs102（SpiderMonkey 102 ESR）升级改名而来，版本升级至
**128 ESR**。 - 为 GNOME 相关组件提供更新的 JavaScript 引擎支持。
- 提升 JS 引擎安全性和性能。

## 10. 本地化与国际化

### icu 74.2（oc9 补丁更新）

- 版本号维持 74.2 不变，此次为 oc9 补丁更新（74.2-1 → 74.2-3）。
**GB 18030-2022 支持**：更新 GB 18030-2022 字符集映射表（ICU-23135），使系统更好地支持最新中文国家标准**安全修复**：修复 CVE-2025-5222 安全漏洞

## 11. 存储与虚拟化

### libmicrohttpd 1.0.2

- 从 0.9.77 升级至 1.0.2，这是首个正式稳定版本（主版本升级）。
**请求解析重写**：完全重写请求解析实现，全面对齐 RFC 9110/9112 规范**认证 API 重设计**：重新设计 Digest/Basic 认证 API，增强安全性**多线程改进**：改进多线程环境下的功能支持，提升并发处理能力**HTTPS 增强**：重新实现 GnuTLS 初始化逻辑，增强 HTTPS 支持**注意**：此版本包含重要 API 变更，升级前请参阅官方迁移指南

### ostree 2025.5

- 从 2023.3 升级至 2025.5，跨越约 2 年的版本更新。
**OCI 镜像支持增强**：提升容器化操作系统部署能力**SELinux 标签处理改进**：增强安全合规性**稳定性提升**：包含大量 bug 修复和性能改进，提升原子化部署的稳定性与可靠性

### luksmeta 10

- 从 9 升级至 10（主版本升级）。
**安全修复**：修复 CVE-2025-11568（大型元数据处理漏洞）**新功能**：PPC64LE 架构支持**LUKS2 增强**：改进 LUKS2 元数据处理逻辑，增强对复杂加密卷的支持**兼容性提升**：提升与最新 cryptsetup 版本的兼容性

### libiscsi 1.20.0

- 从 1.19.0 升级至 1.20.0，次版本更新。
**错误处理改进**：改进 iSCSI 协议错误处理逻辑，提升存储网络的容错能力**稳定性增强**：修复内存泄漏问题，提升长时间运行的稳定性**整体优化**：增强存储网络连接的整体稳定性

### libtpms 0.9.7

- 从 0.9.6 升级至 0.9.7，补丁版本更新。
**安全修复**：修复 CVE-2025-49133 安全漏洞**稳定性增强**：改进 TPM 2.0 命令处理流程的健壮性，提升 TPM 模拟器稳定性

### libvirt 9.10.0

- 从 9.7.0 升级至 9.10.0，跨越 3 个次版本。
- 包含功能增强和 bug 修复，改进虚拟机管理接口的稳定性。

## 12. 监控与高可用

### grafana-pcp 5.3.0

- 从 5.1.1 升级至 5.3.0，跨越 2 个次版本。
**查询性能改进**：改进性能指标的查询效率，提升大规模监控场景的响应速度**可视化增强**：增强可视化面板的展示能力，丰富监控图表类型**PCP 集成优化**：提升与 PCP（Performance Co-Pilot）的集成稳定性

### pacemaker 2.1.8

- 从 2.1.6 升级至 2.1.8，跨越 2 个补丁版本。
**安全修复**：包含安全修复，增强集群管理的安全性**资源调度增强**：增强集群资源调度的可靠性，改善故障切换表现**稳定性提升**：提升稳定性，减少误触发 failover 的概率

### frr 10.0.3

- FRR 路由软件进行主版本升级（9.0 升至 10.0），从 9.0.3 升级至 10.0.3。
**BGP 性能优化**：FRR 10 引入 BGP 协议性能优化，大幅提升路由处理吞吐量**OSPF 改进**：改进 OSPF 路由收敛速度，提升动态路由稳定性**IS-IS 协议增强****安全修复**：修复 RTR 协议处理逻辑中的高危漏洞 CVE-2024-55553

## 13. 开发工具链

### git 2.43.7

- 从 2.41.1 升级至 2.43.7，跨越 2 个次版本和多个补丁版本。
**reftable 支持**：引入 reftable 后端支持，显著改善大型仓库的性能，减少引用读写开销**子模块改进**：改进子模块（submodule）处理逻辑，提升多模块项目的管理体验**bisect 增强**：增强 git-bisect 功能，优化 bug 定位效率**安全修复**：修复多个 CVE 安全漏洞

### meson 1.4.2

- 从 1.2.0 升级至 1.4.2，跨越 2 个次版本。
**Wayland 支持**：1.3 版本新增对 Wayland 协议的改进支持**CMake 集成**：1.4 版本增强 CMake 集成能力，提升与 CMake 项目的互操作性**依赖查找优化**：改进依赖查找机制，提升构建系统的依赖解析准确性**跨平台兼容**：提升跨平台构建的兼容性

### gcc 12.3.1.8

- 从 12.3.1.4 升级至 12.3.1.8，包含 4 个编译器补丁版本的累积更新。
**代码生成修复**：修复代码生成中的 bug，提升代码质量**C++20 支持改进**：改进 C++20 标准的支持**LoongArch 修复**：修复 LoongArch 架构相关的编译问题**AArch64 修复**：修复 AArch64 架构相关的编译问题

### llvm 17.0.6

- 版本号维持 17.0.6 不变，此次为 oc9 补丁更新（17.0.6-9.oc9 → 17.0.6-17.oc9）。
**clang**、**compiler-rt**、**libomp**、**lld**、**lldb**、**python-lit**六个原本独立的软件包已合并至 llvm 主包中统一管理（见第 15 章），简化了 LLVM 工具链的安装与维护，避免多包版本不一致导致的兼容性问题。

## 14. 硬件支持与内核模块管理

### linux-firmware 20250917

- 从 20240909 升级至 20250917，跨越约 1 年的固件累积更新。
**新硬件支持**：新增多个硬件设备的固件支持**GPU 固件更新**：更新 Intel/AMD/Nvidia GPU 固件，改善图形显示稳定性**Wi-Fi 固件更新**：更新无线网卡固件，提升 Wi-Fi 连接稳定性**问题修复**：修复已知的固件加载问题

### microcode_ctl 20250812

- 从 20250211 升级至 20250812，覆盖 6 个月的 Intel CPU 微码累积更新。
**安全加固**：修复多个 CPU 级安全漏洞和硬件缺陷

### dkms 3.2.2（新增）

- 本次新增软件包，提供动态内核模块支持（Dynamic Kernel Module Support）。
- 用于管理第三方内核模块在内核升级时的自动重新编译与安装。
- 简化外部内核模块的维护流程，无需手动重新编译。

## 15. 新增软件包

本次更新新增以下软件包：

| 软件包 | 版本 | 说明 |
|---|---|---|
| dkms | 3.2.2 | 动态内核模块支持，用于第三方内核模块的安装与管理 |
| mozjs | 128.14.0 | Mozilla SpiderMonkey JavaScript 引擎（由 mozjs102 升级改名，升至 128 ESR） |
| nodejs20 | 20.20.0 | Node.js 20 独立软件包，nodejs 虚包依赖此包填充 |
| ocai-agent | 2.0.0 | OpenCloudOS AI Agent 工具 |
| perl-Crypt-URandom | 0.39 | Perl 加密随机数生成模块 |
| perl-YAML | 1.30 | Perl YAML 格式解析模块 |
| python-influxdb | 5.2.0 | Python InfluxDB 客户端库（从 EPOL 仓库迁入） |

## 16. 移除与整合的软件包

### LLVM 相关包整合

**clang、compiler-rt、libomp、lld、lldb、python-lit** 六个独立软件包已整合至 llvm 主包，不再单独分发。

### KonaJDK LoongArch 包整合

**java-8-konajdk-loongarch、java-11-konajdk-loongarch、java-17-konajdk-loongarch** 三个独立软件包已分别合并至对应主包（java-8/11/17-konajdk），LoongArch 平台支持现在统一由主包提供。

### 其他

**mozjs102**已由**mozjs**（128.14.0 ESR）替代，包名及版本均已升级。**webkit2gtk4.0**已移除，由**webkit2gtk4.1**和**webkitgtk6.0**替代，统一由 webkitgtk 2.52.1 源码包提供。**umoci**OCI（Open Container Initiative）镜像操作工具已移除。umoci 核心功能围绕容器镜像解包/打包（类似 docker save/load 的底层实现），其主要应用场景已被更上层工具（如 Buildah、Skopeo）覆盖。umoci 社区的最新 release 版本在 2021 年发布，至今已无新的软件包发布，因此予以移除。

## 17. 其他资源

OpenCloudOS 官网：https://www.opencloudos.org/

有关 OpenCloudOS 的详细文档，请访问官方文档站点：https://docs.opencloudos.org/

包括但不限于： - 系统安装与部署指南 - YUM 软件源配置 - 各类镜像使用说明 - 系统管理员指南 - 兼容性与迁移指南

如需技术支持或参与社区讨论，请加小助手微信：qingmin0623

有关 OpenCloudOS 内核的详细信息，请参考内核 Wiki：https://gitee.com/OpenCloudOS/OpenCloudOS-Kernel/wikis

内核相关问题请提交 Issue：https://gitee.com/OpenCloudOS/OpenCloudOS-Kernel/issues

如需反馈用户态软件包的问题或提交 Bug，建议在 OpenCloudOS Stream 组织下对应软件包的 Gitee 仓库提交 Issue：[https://gitee.com/opencloudos-stream/](https://gitee.com/opencloudos-stream/)（OpenCloudOS Stream 是 OpenCloudOS 9 的上游 L1 社区，所有软件包问题建议优先在此提交）。