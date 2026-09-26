source: https://docs.opencloudos.org/release/ocs/

# OpenCloudOS Stream 版本说明

OpenCloudOS Stream 是 OpenCloudOS 社区联合伙伴共同研发的自主可控的上游版本，其内核及用户态软件均基于社区 Upstream 独立演进、自编译，自主选型和维护，不再依赖任何发行版，完全自主可控。通过内核，用户态软件的全面优化和打磨，为用户和业务提供更先进、更高性能的基础环境和服务能力，彻底解决 CentOS 断供的问题。

2023 年，操作系统开源社区 OpenCloudOS 联合伙伴共同研发的自主可控的上游版本 OpenCloudOS Stream，其内核及用户态软件均基于 upstream 社区自主选型、独立演进和维护，开启了国产 OS 全新独立路线。

2024 年 3 月，全新版本的 OpenCloudOS Stream 发布，新版 Stream 国内首发了 Linux Kernel 6.6，并对 kernel、glibc、systemd 等基础组件进行更新，引入超多新特性，提供更佳的安全、性能和稳定性体验。

## 下载

新版 OpenCloudOS Stream 提供 Netinst（网络安装镜像）、DVD（标准安装镜像）、Live（LiveCD镜像）、Minimal（小型化基础安装镜像）、QCOW2（虚拟机镜像）、Containers（容器镜像）六种安装方式，方便用户快速部署。

可在下方链接中选择【Stream 23】，找到如下图位置，选择合适的镜像下载安装：[https://www.opencloudos.org/ospages/downloadISO](https://www.opencloudos.org/ospages/downloadISO)

## OpenCloudOS Stream 23 新特性汇总

### 内核全新升级，自研特性加持

作为迄今为止最新的长期支持（LTS）版本，Linux Kernel 6.6 包含新功能、硬件支持、安全增强和性能改进等重大更新。升级到 Linux Kernel 6.6 是本次版本开发的一个重要挑战，并成功为新版 OpenCloudOS Stream 引入了一系列特性：

#### 全新内核/内存管理机制，启动加速，性能提升

Folios，Mapple Tree，Per VMA Lock 等全新的内核内存管理机制，彻底改变了内存管理核心数据结构，大幅度降低了内存管理开销，适配了更多的大页面透传，提高了并发处理能力，极大的加速了应用启动性能和内存分配性能。

MGLRU - 多世代 LRU，全新的内存管理核心 LRU 机制避免 Rmap 开销，并引入 PID 等机制进行 Refault 控制，大幅度降低热度识别开销并提高精度。降低了大压力场景中 OOM 的概率，并大幅度提升内存紧张时系统性能。

DAMON，高效低负载的内存数据存取监控方案，支持虚拟地址、物理地址监控以及轻内存压力下主动内存回收。新增 syfs 接口，精简使用配置，给性能优化带来极大助力。

Tiered memory - 分层内存系统与 CXL 支持：原生支持不同性能特性的多层内存系统。根据内存冷热探测自动在多层级内存设备间进行数据升降级搬迁，支持多层级内存容量扩展，降低内存使用成本。内存 CXL 多级卸载支持，满足缓存一致性内存高速互联协议，原生支持多级内存卸载平衡，支持使用 CXL 作为远端内存进行基于水位线的平衡。构建大容量、低延迟内存池，内存使用按需提供，极大降低内存使用成本。

Cgroup 控制增强。内存 Cgroup 大幅度优化锁性能，并新增 Object Cgroup 内部机制，彻底解决 Kmem 导致页面碎片化以及 Zombie Cgroup 问题。在 Cgroup 间干扰严重的场景可以提升约 50% 的性能。IO Cgroup 支持设置 IO request 优先级，提升iocost 算法准确度，IO权重分配在不同质磁盘间更平滑，提高吞吐量。

#### 调度系统大幅度增强，提供更加强大的算力支持

EEVDF 替代 CFS，改善延迟敏感类任务的延迟，减少业务毛刺抖动以及尾延迟，运行更加平滑。内核动态抢占切换，采用 static key 实现运行时抢占/非抢占调度，告别重新构建。CPU 负载均衡优化，降低调度开销，更好的局部性控制逻辑，提高整体使用率和吞吐。

Multi-LLC per-node 架构机器调度功能优化，极大提升如 AMD Zen 系列处理器在众多负载场景下性能表现，提供更加强大的算力支持。

#### 提升效率与稳定性，优化缓存

文件系统优化，新增系统调用 close_range，提升大批量文件操作性能。Fanotify 支持文件错误报告；EXT4，XFS 等文件系统优化性能，提升 IO 效率与性能，优化并发场景，降低延迟，提升可拓展性。

io_uring，新一代异步IO框架全功能支持。新增IORING_OP_MSG_RING支持、优化多线程场景ring fd注册机制、net napi_busy_poll支持、statx API稳定性增强等，降低io_uring内部开销、提升IO异步处理性能。

block层优化提升，支持批处理事件，优化缓存，在高性能设备上提升IOPS约8%，降低passthru IO CPU使用率。

#### 自研特性

同时，在 Linux Kernel 6.6 的基础上，OpenCloudOS 也加入了一系列自研特性：

-
最新硬件与国产化支持：支持 Intel EMR，SPR 等新世代架构，支持海光，龙芯等国产化平台。

-
基于 Livepatch 的多架构热补丁支持：适配了 Livepatch 的 Thread Switch 结合 Stackbacktrace 结构设计，大幅度提高了 ARM64 上热补丁成功概率，降低 Downtime，并实现了多架构统一。

-
大量企业级特性适配：Cgroupfs 支持，PSI Cgroup V1 支持，网络子系统参数细化，Diststat 扩充，Page Cache 限制，Cgroup V1 IO throtting 等针对大规模生产环境中的痛点而生的自研特性。提升内核成熟度与可用度，增强容器隔离。

-
提供针对 EL 生态的发行版支持：无缝支持第三方内核 Kmod 包，对云场景精简环境，新硬件适配，调试等各种场景提供全面适配支持。


### 系统管理更全面，算法更安全，开发更便捷

新版 OpenCloudOS Stream 在内核态提升性能和效率的同时，也在用户态为企业和开发者提供了更全面的支持，带来更多的创新：

#### 更全面的系统管理和服务

systemd 升级至 v255，支持 soft-reboot 用户态重启特性，大幅提升重启速度，支持软重启不中断服务能力；

服务启动方式变更为 systemd-executor 启动，速度更快，内存占用更小；

rsyslog 升级至 8.2312.0，修复多个安全问题，新增 TLS 支持，优化 imptcp、等模块的处理速度和效率，优化工作线程和队列处理上的抢占问题；

ICU 升级至 73.2，Unicode 15 支持 GB18030-2022

#### 网络管理

nftables 升级至 1.0.8，增加对 netlink 流表支持，支持在 nft list hooks 中解码BPF ID，支持在标记语句中使用更大的位移操作、位运算表达式；

iptables 升级至 1.8.9，支持元数据 pkktype 模式的解析以及 TTL/Hoplimit 的解析，改进对大页处理的方式。

#### 存储和文件系统管理

LVM2 升级至 2.03.21，raid+integrity 卷新增对 writecache 的支持，提升 VDO 卷的性能和可靠性，逻辑卷调整命令新增 --fs 和 --fsmode 选项以支持文件系统自动调整；

nfs 管理工具升级至 2.6.3，新增多个选项以支持对传输层安全等更灵活的设置，新增 fsidd 服务以支持对 reexport 数据库的查询；

e2fsprogs 升级到 1.47.0，提升 e2fsck 处理大文件系统的性能，新增对 orphan_file 特性的支持，tune2fs 和 e2label 新增对已挂载文件系统 label 和 UUID 的设置；

xfsprogs 升级至 6.5.0，新增对 Linux Kernel 6.6 文件系统新特性的支持；

ceph 升级至 18.2.0,，RADOS 的 RocksDB 迭代开销和性能都有显著的改进，新功能「读取均衡器」允许用户在其集群上平衡每个池的主 PG；RGW 支持多站点配置的存储桶重新分片，多站点复制的稳定性和一致性有显著改进，支持加密上传的对象进行压缩；RBD 添加对分层客户端加密的支持。

#### 开发和调测

glibc 升级至 2.38，支持 pidfd 系列接口，aarch64 支持向量数学库 libmvec，支持 configure _FORTIFY_SOURCE 提升安全性；

binutils 升级至 2.41，汇编器新增支持 Loongarch 架构的 LSX LASX LVZ LBT 指令集；

gcc 升级至 12.3，默认启用 C++ 17，完善 C++ 20 支持，部分支持 C++ 23 标准；隐式初始化所有堆栈变量；默认调试格式 DWARF5；开始支持 Loongarch 架构；ARM 架构支持新-march 参数：armv8.7-a, armv8.8-a, armv9-a，支持 SIMD SVE 指令集；RISCV 架构添加对 zba、zbb、zbc、zbs 的新 ISA 扩展支持；

python升级至3.11，性能改进明显，较 Python 3.10 提升10-60%；

rust升级至1.75.0，编译器启用BOLT优化，平均运行性能提升2%；

golang升级至1.20.6，gc收集器优化，整体CPU性能提高2%；新增crypto/ecdh包；

clang/llvm升级至17.0.6，对AArch64、AMDGPU、ARM、AVR等后端进行改进，包括新增指令支持、优化等；clang增加C++20协程的全面支持，对c++23标准的部分支持；

bcc升级至0.29，支持kernel 6.6；新增rdmaucma、f2fs、futexctn调测工具；

boost升级至1.82.0，支持C++20标准。

#### 安全

支持SM2/SM3国密安全启动；

scap-security-guide 新增OpenCloudOS Stream安全基线配置文件；

openssl升级至3.0.12，支持国密；

openssh升级至9.3p1，支持国密；

iptables升级至1.8.9，改进lib/alg-yescrypt-platform.c中对大页处理的方式；

gnupg2升级至2.4.3，签名验证速度提高四倍以上，分离式签名速度提高一倍；

gnutls升级至3.8.2，增加对AES-GCM-SIV密码的支持（RFC 8452），扩展对透明KTLS（Kernel TLS）的支持，添加对RFC 9258外部PSK导入器的支持。

#### 容器和虚拟化

moby 升级至 25.0.3 版本，profile/seccomp 适配 Kernel 6.6 系统调用，新增 OpenTelemetry tracing，支持 Linux 下 CDI 设备，支持递归只读挂载；

kubernetes 升级到 1.27.4 版本；

qemu 升级到 8.2.0，配套 Kernel 6.6，支持新的 CPU 类型 neoverse-v1，带来新的架构特性支持 FEAT_PAN3、FEAT_LSE2、FEAT_RME，支持 AES 加速指令、SHA 指令，RISC-V 支持新的 ISA 和拓展能力，新增 hv-balloon、UFS 等多种设备支持，Linux-user 提供大多数流行架构的 vdso；

OpenStack 升级至 Wallaby 版本，Nova，Neutron 等组件功能进一步优化。

#### 典型应用

sqlite 升级至 3.42，支持 JSON5 拓展，添加 FTS5 安全删除命令；启用「视图计数」优化，避免计算子查询中未使用的列；提高查询规划器的性能；增加 --sate 命令行选项，禁止使用有可能危害系统的 SQL 函数；

支持企业级分布式 HTAP 开源数据库 OpenTenBase；

新增基于 Nginx 与 Lua 的高性能 Web 平台 OpenResty。

#### 桌面 & 图形库 & 输入法

新增实验性支持 NDE 桌面环境；

新增支持 Kwin 5.27.9；

新增支持 sddm 0.20；

新增支持 fcitx4 4.2.9.9，引入配套工具 fcitx-configtool im-chooser 等；

Qt 升级至 5.15.11；

新增支持 GTK2，目前已支持 GTK2、GTK3、GTK4；

新增支持 ibus 智能拼音输入法。

## 注意事项

- 对于 x86平台，物理机和虚拟机需要支持 x86-64-v2 微架构及以上
- 容器部署，Docker 需要 v24 以上版本
- 旧版本升级时，请注意 ctdb-ceph-mutex、samba-vfs-cephfs、wxGTK3、wxGTK3-devel、wxGTK3-gl、wxGTK3-i18n、wxGTK3-media、wxGTK3-webview、openstack-placement-doc、python3-django-doc 已从版本中衰退，如果安装了上述衰退包，请先执行
`dnf remove --noautoremove <package name>`

后再升级系统。

## 问题反馈

技术反馈可进入下方链接进行提交（在 Product 选项中选择 OpenCloudOS Stream）：[https://bugs.opencloudos.tech/](https://bugs.opencloudos.tech/)

如果能够确认发生问题的软件包，也可以在 Gitee 源码仓库对应的软件包提交 issue：[https://gitee.com/opencloudos-stream](https://gitee.com/opencloudos-stream)

使用 OpenCloudOS Stream 版本遇到和任何问题，诚挚欢迎社区的用户、开发者朋友多提宝贵建议。我们还有很多需要改进和完善的地方。