source: https://docs.opencloudos.org/release/v9.2/

# 简介

开源操作系统社区 OpenCloudOS 由腾讯与合作伙伴共同倡议发起，是完全中立、全面开放、安全稳定、高性能的操作系统及生态。OpenCloudOS 沉淀了多家厂商在软件和开源生态的优势，继承了腾讯在操作系统和内核层面超过 10 年的技术积累，在云原生、稳定性、性能、硬件支持等方面均有坚实支撑，可以平等全面地支持所有硬件平台。

OpenCloudOS 9是 OpenCloudOS 社区联合伙伴共同研发的全链路服务器操作系统社区版本，其上游OpenCloudOS Stream 版本的内核及用户态软件均基于 upstream 社区独立选型、独立演进和维护，不再依赖其他发行版。OpenCloudOS 9 通过内核，用户态软件的全面优化和打磨，为用户和业务提供更先进、更高性能的基础环境和服务能力，解决 CentOS 断供的问题。

# 下载

下载 OpenCloudOS 9.2，请访问以下链接：

-
网站链接： https://www.opencloudos.org

-
ISO 安装镜像： https://mirrors.opencloudos.tech/opencloudos/9.2/isos/

- Docker容器&虚拟机镜像：https://mirrors.opencloudos.tech/opencloudos/9.2/images/

# OpenCloudOS 9.2 新特性汇总

## 1.内核

作为迄今为止最新的长期支持（LTS）版本，Linux Kernel 6.6 包含新功能、硬件支持、安全增强和性能改进等重大更新。升级到 Linux Kernel 6.6 是本次版本开发的一个重要挑战，并成功为新版 OpenCloudOS 9.2 引入了一系列特性：

-
全新内核/内存管理机制，启动加速，性能提升 Folios，Maple Tree，Per VMA Lock 等全新的内核内存管理机制，彻底改变了内存管理核心数据结构，大幅度降低了内存管理开销，适配了更多的大页面透传，提高了并发处理能力，极大的加速了应用启动性能和内存分配性能。

-
MGLRU - 多世代 LRU，全新的内存管理核心 LRU 机制避免 Rmap 开销，并引入 PID 等机制进行 Refault 控制，大幅度降低热度识别开销并提高精度。降低了大压力场景中 OOM 的概率，并大幅度提升内存紧张时系统性能。

-
DAMON，高效低负载的内存数据存取监控方案，支持虚拟地址、物理地址监控以及轻内存压力下主动内存回收。新增 sysfs 接口，精简使用配置，给性能优化带来极大助力。

-
Tiered memory - 分层内存系统与 CXL 支持：原生支持不同性能特性的多层内存系统。根据内存冷热探测自动在多层级内存设备间进行数据升降级搬迁，支持多层级内存容量扩展，降低内存使用成本。内存 CXL 多级卸载支持，满足缓存一致性内存高速互联协议，原生支持多级内存卸载平衡，支持使用 CXL 作为远端内存进行基于水位线的平衡。构建大容量、低延迟内存池，内存使用按需提供，极大降低内存使用成本。

-
Cgroup 控制增强。内存 Cgroup 大幅度优化锁性能，并新增 Object Cgroup 内部机制，彻底解决 Kmem 导致页面碎片化以及 Zombie Cgroup 问题。在 Cgroup 间干扰严重的场景可以提升约 50% 的性能。IO Cgroup 支持设置 IO request 优先级，提升iocost 算法准确度，IO权重分配在不同质磁盘间更平滑，提高吞吐量。

-
调度系统大幅度增强，提供更加强大的算力支持 EEVDF 替代 CFS，改善延迟敏感类任务的延迟，减少业务毛刺抖动以及尾延迟，运行更加平滑。内核动态抢占切换，采用 static key 实现运行时抢占/非抢占调度，告别重新构建。CPU 负载均衡优化，降低调度开销，更好的局部性控制逻辑，提高整体使用率和吞吐。

-
Multi-LLC per-node 架构机器调度功能优化，极大提升如 AMD Zen 系列处理器在众多负载场景下性能表现，提供更加强大的算力支持。

-
提升效率与稳定性，优化缓存

-
文件系统优化，新增系统调用 close_range，提升大批量文件操作性能。Fanotify 支持文件错误报告；EXT4，XFS 等文件系统优化性能，提升 IO 效率与性能，优化并发场景，降低延迟，提升可拓展性。

-
io_uring，新一代异步IO框架全功能支持。新增IORING_OP_MSG_RING支持、优化多线程场景ring fd注册机制、net napi_busy_poll支持、statx API稳定性增强等，降低io_uring内部开销、提升IO异步处理性能。

-
block层优化提升，支持批处理事件，优化缓存，在高性能设备上提升IOPS约8%，降低passthru IO CPU使用率。


### 自研特性

-
最新硬件与国产化支持：支持 Intel GNR，AMD turin 等新世代架构，支持海光，龙芯，鲲鹏，兆芯等国产化平台，支持北中网芯、网讯、云芯智联等国产网卡。

-
基于 Livepatch 的多架构热补丁支持：适配了 Livepatch 的 Thread Switch 结合 Stackbacktrace 结构设计，大幅度提高了 ARM64 上热补丁成功概率，降低 Downtime，并实现了多架构统一。

-
大量企业级特性适配：Cgroupfs 支持，PSI Cgroup V1 支持，网络子系统参数细化，Diststat 扩充，Page Cache 限制，Cgroup V1 IO throtting 等针对大规模生产环境中的痛点而生的自研特性。提升内核成熟度与可用度，增强容器隔离。

-
提供针对 EL 生态的发行版支持：无缝支持第三方内核 Kmod 包，对云场景精简环境，新硬件适配，调试等各种场景提供全面适配支持。


## 2.系统管理和服务：

- systemd 升级至v255，支持soft-reboot用户态重启特性，大幅提升重启速度，支持软重启不中断服务能力；服务启动方式变更为systemd-executor启动，速度更快，内存占用更小
- rsyslog 升级至8.2312.0，修复多个安全问题，新增TLS支持，优化imptcp、等模块的处理速度和效率，优化工作线程和队列处理上的抢占问题
- icu 升级至73.2，Unicode 15支持GB18030-2022
- grub2 升级至 2.12，支持 GCC 13、 clang 14 编译，支持 binutils 2.38，支持 PCI 和 MMIO UART，支持 SDL2，支持 LoongArch架构启动

## 3.网络管理

- nftables 升级至1.0.8，增加对netlink流表支持，支持在nft list hooks中解码BPF ID，支持在标记语句中使用更大的位移操作、位运算表达式
- iptables 升级至1.8.9，支持元数据pkktype模式的解析以及TTL/Hoplimit的解析，改进lib/alg-yescrypt-platform.c中对大页处理的方式

## 4.存储和文件系统管理：

- LVM2 升级至2.03.21，raid+integrity 卷新增对 writecache 的支持，提升VDO 卷的性能和可靠性，逻辑卷调整命令新增 --fs 和 --fsmode 选项以支持文件系统自动调整
- nfs-utils 管理工具升级至2.6.3，新增多个选项以支持对传输层安全等更灵活的设置，新增 fsidd 服务以支持对 reexport 数据库的查询
- e2fsprogs 升级到1.47.0，提升 e2fsck 处理大文件系统的性能，新增对 orphan_file 特性的支持，tune2fs 和 e2label 新增对已挂载文件系统 label 和 UUID 的设置
- xfsprogs 升级至6.5.0，新增对 kernel 6.6文件系统新特性的支持
- ceph 升级至18.2.0,，RADOS的RocksDB 迭代开销和性能都有显著的改进，新功能“读取均衡器”允许用户在其集群上平衡每个池的主 PG；RGW支持多站点配置的存储桶重新分片，多站点复制的稳定性和一致性有显著改进，支持加密上传的对象进行压缩；RBD添加对分层客户端加密的支持

## 5.开发和调测

- glibc 升级至2.38，支持 pidfd 系列接口，aarch64 支持向量数学库 libmvec，支持 configure _FORTIFY_SOURCE 提升安全性
- binutils 升级至2.41，汇编器新增支持Loongarch架构的LSX LASX LVZ LBT指令集
- gcc 升级至12.3.1.1，默认启用c++17，完善C++20支持，部分支持C++23标准；隐式初始化所有堆栈变量；默认调试格式DWARF5；支持Loongarch架构；ARM架构支持新-march参数：armv8.7-a, armv8.8-a, armv9-a，支持SIMD SVE指令集；RISCV架构添加对 zba、zbb、zbc、zbs的新 ISA扩展支持；支持 BOLT 优化，强化PGO/LTO 等反馈优化技术，提升稳定性和兼容性;
- python 升级至3.11，性能改进明显，较 Python 3.10 提升10-60%
- rust 升级至1.75.0，编译器启用BOLT优化，平均运行性能提升2%
- golang 升级至1.21.7，gc收集器优化，整体CPU性能提高2%；新增crypto/ecdh包
- clang/llvm 升级至17.0.6，对AArch64、AMDGPU、ARM、AVR等后端进行改进，包括新增指令支持、优化等；clang增加C++20协程的全面支持，对c++23标准的部分支持
- bcc 升级至0.29.1，支持kernel 6.6；新增rdmaucma、f2fs、futexctn调测工具；
- boost 升级至1.82.0，支持C++20标准

## 6.安全：

- 支持 SM2/SM3 国密安全启动
- scap-security-guide 新增 TencentOS Server 4 安全基线配置文件
- openssl 升级至3.0.12，支持国密
- openssh 升级至9.3p2，支持国密
- gnupg2 升级至2.4.3，签名验证速度提高四倍以上，分离式签名速度提高一倍
- gnutls 升级至3.8.2，增加对AES-GCM-SIV密码的支持（RFC 8452），扩展对透明KTLS（Kernel TLS）的支持，添加对RFC 9258外部PSK导入器的支持

## 7.容器和虚拟化：

- moby 升级至25.0.3版本，profile/seccomp适配kernel 6.6系统调用，新增OpenTelemetry tracing，支持Linux下CDI设备，支持递归只读挂载
- kubernetes 升级到 1.27.4 版本
- qemu 升级到8.2.2，配套kernel 6.6，支持新的CPU类型neoverse-v1，带来新的架构特性支持FEAT_PAN3、FEAT_LSE2、FEAT_RME，支持AES加速指令、SHA指令，RISC-V支持新的ISA和拓展能力，新增hv-balloon、UFS等多种设备支持，linux-user提供大多数流行架构的 vdso
- OpenStack 升级至Wallaby 版本，Nova，Neutron 等组件功能进一步优化

## 8.典型应用：

- sqlite 升级至3.42，支持JSON5拓展，添加FTS5安全删除命令；启用“视图计数”优化，避免计算子查询中未使用的列；提高查询规划器的性能；增加--sate命令行选项，禁止使用有可能危害系统的SQL函数
- 支持企业级分布式HTAP开源数据库 OpenTenBase
- 新增基于 Nginx 与 Lua 的高性能 Web 平台 OpenResty

## 9.桌面&图形库&输入法：

- 新增实验性支持NDE桌面环境
- 新增支持 Kwin 5.27.9
- 新增支持 sddm 0.20
- 新增支持 fcitx4 4.2.9.9，引入配套工具fcitx-configtool im-chooser等
- Qt升级至 5.15.11
- 新增支持 GTK2，目前 OpenCloudOS 9 已支持GTK2 GTK3 GTK4
- 新增支持 ibus 智能拼音输入法