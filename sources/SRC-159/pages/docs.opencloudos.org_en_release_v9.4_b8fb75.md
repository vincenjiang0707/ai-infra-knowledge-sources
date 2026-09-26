source: https://docs.opencloudos.org/en/release/v9.4/

# 简介

OpenCloudOS 9 (OC9) 是 OpenCloudOS 社区联合伙伴共同研发的全链路服务器操作系统社区版本，沉淀了多家厂商在软件和开源生态的优势，继承了腾讯在操作系统和内核层面超过 10 年的技术积累。 其内核及用户态软件均基于 upstream 社区独立演进，自主选型并持续维护。 全新 OpenCloudOS 9.4 现已迭代发布，该版本新增并实现了对 1w+ 用户态软件的独立编译维护，具备高性能、安全、支持多硬件平台的特性，能为云上产品和业务提供可靠的基础环境和服务能力。 同源支持全新龙芯架构，并升级众多软件包（如 kernel-6.6.80、 grub2-2.12、php-8.3.10 和 moby-27.3.1），带来上游最新特性， bug 及安全漏洞修复，加入腾讯自研 tgcc 12.3.1.4 编译器提高系统性能。

# 新版本支持龙芯架构

OpenCloudOS 9.4 新增对 LoongArch64 架构的支持，标志着 OpenCloudOS 在多架构生态建设方面迈出了重要一步。该能力基于上游 OpenCloudOS-Stream 23 的同步成果，由 OpenCloudOS 社区联合龙芯共同开发，采用与 x86 和 ARM 架构同源异构的代码体系，具备良好的兼容性与一致性体验。 OC9.4 loongarch64 版本支持多款龙芯处理器（如 3A5000、3C5000、3D5000、3A6000 等），同时新增对 YT6801 国产网卡驱动的支持 。支持虚拟化、EFI 启动、内核态 SE（安全加密）驱动等各项功能。

# 新特性汇总

## 1.内核

内核版本迭代至 6.6.80，持续回合上游补丁，带来更多新硬件支持和自研特性支持。

### 1.1.新硬件及驱动支持

- 新 CPU 支持，支持 intel GNR CPU、龙芯（3A5000、3C5000、3D5000、3A6000）、海光（Hygon PSP on Hygon 2nd/3rd CPUs）、兆芯（cpu core、pmu、CRC32C、SB HDAC and other extended topology）、kunpeng（920 以及 920 next CPU）、phytium CPU（S2500、5000C）
- 支持北中网芯、3snic、7A2000的网卡驱动
- 支持 linkdata 的 ps3stor 驱动
- 支持 phytium 显卡驱动
- 支持 Hygon4 的加密驱动、Montage Mont-TSSE（澜起科技的信任与安全系统扩展）驱动
- 支持 Hygon 安全虚拟化技术 (CSV)，支持 Hygon Trusted Key Management run on CSV
- 集成博通商用质量的 bxnt_en 驱动
- 集成 broadcom 商用质量的 mpt3sas 驱动

### 1.2.新特性支持

- 开启对 CONFIG_PCIE_EDR 的支持，加强 pcie 硬件故障的恢复能力
- 开启对 EROFS_FS 和 CACHEFILES 的支持，用于容器镜像加速
- 开启对 CONFIG_SMC 的支持，用于 sockets over RDMA
- 支持 zstd 压缩格式的 squashfs
- 支持 dynamic integrity measurement (DIM)
- 支持 kill protect 特性
- 支持通过自研的 min_wait_time，限制最小的 epoll 时间
- 支持盘符保序、支持网卡设备编号保序
- 支持 arp 双发、支持识别内部网段
- 支持磁盘 IO 延时抖动常态化监控
- 支持网络时延超阈值的检测
- 支持 SLI (Service level indicator)
- 支持 csig 的 toa 模块
- 支持调整 execve 参数的大小，以便支持 gcc 传递很多参数
- 支持 cmdline.ia32_emulation 启动参数，允许用户自行选择是否开启 32-bit 兼容性支持

## 2.启动

### 2.1.grub2 2.12

- 支持龙芯架构
- 跨架构统一 EFI Linux 内核加载器。
- 初步支持引导加载程序接口 (Boot Loader Interface)
- 支持使用固件调用动态添加 GRUB 运行时内存
- 支持 PCI 和 MMIO UART 2.2.安全启动支持 OC9.4 版本对系统的安全启动（Secure Boot）功能进行了增强，带来了更高的安全性，支持国产商密算法（SM系列）和国际算法双签名，可满足国内用户对国产密码算法的合规性和安全性要求，为政企用户提供更加稳固、可信的安全基础。安全启动配置指南 https://docs.opencloudos.org/OCS/Install_Guide/ocs-secure-boot/

## 3.开发和调测

### 3.1.tgcc 12.3.1.4

- 引入腾讯自研 tgcc：支持链接后优化（BOLT）和分布式构建系统加速，并积累司内编译器团队百万核运营经验，修复多处 corner case
- 增强龙芯架构的支持：
- 新增对龙芯 3A6000 机型的支持
- 优化分支/乘法/立即数加载指令生成，新增 LSX/LASX 向量扩展指令
- 修复 gnome 桌面启动失败
- 修复 frint 和 ftint 指令使用错误
- 添加 Ada, libffi，libvtv，libitm LoongArch 支持
- 添加 mcmodel=medium，extreme 支持
- 增强鲲鹏平台 (KUNPENG-Aarch64) 支持：
- 支持 Kunpeng 920 高性能处理器 & AI 编译优化
- 结构体优化
- 数组宽比较优化
- 指令生成优化
- 增强RISCV架构支持：
- 新增 RISC-V 矢量加密指令

### 3.2.ocaml 5.2.0

- 引入全新多核运行时，支持共享内存并行性与效果处理器（effect handlers），但作为实验性版本，仅支持 x86-64 和 ARM64 架构，且存在 Ephemeron 性能问题
- 恢复 RISC-V/s390x 原生编译支持，安装体积缩减 50%，新增 57 个标准库函数，并通过尾递归优化提升性能
- 紧急修复打包、类型检查和数值性能三大用户痛点，移除 "Marshal" 模块的 ZSTD 压缩依赖以避免强制绑定，并修复并发安全问题
- 重新引入 GC 压缩以优化内存碎片，恢复 POWER 架构支持，新增 "Dynarray" 模块和线程检测工具，改进 IDE 元数据追踪
- 恢复 Windows MSVC 工具链支持，增强 Unicode 标识符兼容性，优化 "Dynarray" 内存效率，并重新引入统计内存分析 "statmemprof" 模块

### 3.3.nano 8.0

引入现代快捷键绑定模式，默认搜索行为发生变更，支持通过 filename:number 方式打开特定行。增强锚点与灰度色彩支持，优化宏执行和鼠标滚动体验。需注意快捷键行为与旧版本不兼容，建议审查自定义配置。

## 4.网络管理

### 4.1.bind 9.18.21

- 根服务器 IP 更新：B.ROOT-SERVERS.NET 的 IP 地址已更新为 170.247.170.2 和 2801:1b8:10::b
- 内存优化：通过为发送缓冲区实现专用 jemalloc 内存区域，提高了内存使用效率，更好地管理向操作系统返回内存页面
- 衰退 DNS COOKIE 的 AES算法：cookie-algorithm aes 已被弃用，推荐使用当前默认的 SipHash-2-4 算法
- 解析器参数弃用：resolver-nonbackoff-tries 和 resolver-retry-interval 语句已被弃用，使用它们现在会导致警告被记录

### 4.2.libnbd 1.20.2

- 支持 NBD 64 位 "extended headers" 和范围大小
- 支持过滤块状态请求
- 新的 Rust 绑定，有一个用于日常使用的基本 API，以及一个使用 Tokio 实现的异步 API
- OCaml 绑定支持 AIO pread 和 pwrite 中的零拷贝函数

### 4.3.nbdkit 1.38.4

- VRRP 接口组与名称增强：新增对 VMAC 和 ipvlan 接口组 "interface group" 的支持，默认继承父接口组，便于防火墙规则统一管理。允许自定义 VMAC/ipvlan 接口名称（如 "bridge"），并支持显式配置接口组
- SNMP 统计优化：新增 "snmp_rs_stats_update_interval" 和 "snmp_vs_stats_update_interval" 配置项，分别控制实时服务器（RS）和虚拟服务器（VS）的 SNMP 统计更新频率，默认 5 秒。优化 64 位统计数据处理，减少冗余存储
- IPVS 性能与逻辑改进：重构 IPVS 健康检查机制，减少配置重载时间（从 132 秒优化至 0.24 秒）。修复虚拟服务器组在重载时未正确移除或添加服务器的问题，并优化“抱歉服务器”（sorry server）的逻辑处理
- 系统服务与兼容性调整：新增 "use_symlink_paths" 全局配置项，允许脚本路径保留符号链接。修复 systemd 非 root 服务文件中的 SNMP 配置错误，并优化进程启动时的安全检查逻辑
- 关键问题修复：修复 IPv6 VMAC 接口的邻居请求响应问题，避免备份节点误接收主节点流量。解决 "skip_check_adv_addr" 和 "strict_mode" 配置解析错误，优化接口组通知逻辑

### 4.4.iperf3 3.18

- 安全漏洞修复：修复了导致服务器段错误的 JSON 安全漏洞（CVE-2024-53580）和身份验证中的侧信道定时攻击漏洞（CVE-2024-26306）
- 多线程优化：-P/--parallel 选项的多个测试流现在由不同线程处理，充分利用多核 CPU，大幅提高了测试的吞吐量和性能
- 新增支持流式 JSON 输出格式，便于实时数据分析和处理
- 修复了在有限波特率测试中 CPU 利用率异常偏高的问题，移除了 --pacing-timer 选项，优化了整体性能
- 支持超过 32Gbps 的速率控制，满足高速网络测试需求

### 4.5.tomcat 9.0.86

- 引入 CSRF 防护过滤器路径白名单、Manager 应用 JSON 输出、自定义 SSLContext 配置、Cookie partitioned 属性等新特性
- 修复 TLS 热重载稳定性问题、WebSocket 连接释放异常、FORM 登录超时恢复等关键问题
- 最低构建 JDK 要求提升至 Java 17

## 5.存储和文件系统管理

### 5.1.mysql 8.0.41

- 重构 data_locks 和 data_lock_waits 表，提升查询速度
- TABLE_HANDLES 使用的 RAM 量最大调整为 9GB

### 5.2.postgresql 15.12

- 优化 Waiters 列表复杂度，大幅提升吞吐量
- 避免在并行哈希连接中超大共享内存分配
- 修复 DSM 分配问题
- 新服务器 session 的 client socket 无法 non-blocking 时断连

### 5.3.xfsprogs 6.6.0

- 外部日志设备支持：新增支持从独立日志设备（如专用日志盘）读取数据。增强对分离式日志架构的调试能力
- xfs_io 加密策略支持：新增 log2_data_unit_size 选项，支持通过 fscrypt_policy_v2 配置内核级文件加密策略。优化全盘加密（FDE）场景下的数据单元粒度，提升加密效率
- 元数据转储格式升级：引入新版 metadump 工具格式，优化元数据备份与恢复的兼容性。适用于大规模存储环境的数据迁移与灾难恢复，提升对复杂文件系统结构的支持能力

## 6.安全

### 6.1.nss 3.105

- 添加对 EdDSA 签名算法的支持，以及对一些量子密码算法（如 Kyber、Dillthium）的实验性支持
- 新增 SSL_SignatureScheme 相关函数，用于管理 TLS 签名方案，弃用旧版随机数生成器 API

### 6.2.opensc 0.25.0

- 依赖的加密库从 OpenSSL 1.1.1 升级到 3.0，并移除了一些旧的智能卡支持驱动
- 支持使用 valgrind 进行测试

### 6.3.freeradius 3.2.6

- 针对 BlastRADIUS 攻击添加了缓解措施，提升服务器的安全性
- 支持 TEAP 协议，扩展了 EAP 认证方式，增强了灵活性和兼容性
- 添加了 dpsk 模块和 radsecret 工具，提高了密码管理的安全性
- totp 模块现在支持 TOTP-Time-Offset，允许处理时间不同步的令牌

## 7.容器和虚拟化

### 7.1.moby 27.3.1

- 网络功能增强：增强 IPv6 支持，默认为Linux桥接网络启用 ip6tables 并支持直接路由
- 新增特性：新增卷子路径挂载支持和容器健康检查改进
- bug 修复：修复了使用 "--checkpoint" 选项时 docker start 失败的问题、解决了内部桥接网络上主机与容器之间的 IP 连接问题。

### 7.2.container-selinux 2.234.2

- 添加对DRI和GPU设备的访问支持
- 改进容器域权限，如 BPF 文件系统访问、FIFO 文件监控和 UNIX 套接字通信
- 优化Kubernetes组件标记，如kubelet_exec_t标记与pod资源访问
- 扩展权限集成，允许特权容器使用系统工具和添加Buildah标记）

### 7.3.libguestfs 1.53.2

- 对 python、OCaml 等语言绑定改进
- API改进：SELinux 并行重标记、压缩支持扩展、Btrfs 兼容性修复
- 工具改进：guestfish 支持--key 选项支持 LVM 设备名和通配符

### 7.4.libvirt 9.10.0

- 优化 QCOW2 镜像协议驱动处理，避免自动格式探测的安全风险
- 引入 nbdkit 后端处理网络磁盘（HTTP/FTP/SSH），减少 QEMU 攻击面
- 修复磁盘热插拔配置失败、快照恢复导致 QEMU 崩溃、空 CDROM 热插拔问题
- 支持PipeWire音频后端，新增 vDPA 块设备支
- 支持外部快照还原，优化内部快照恢复逻辑
- 新增网络元数据变更事件，支持网络 XML 的标题/描述字段
- 引入 VFIO 变种驱动（如GPU专用驱动），支持设备迁移等高级功能
- 添加 EPYC-Genoa CPU 模型适配，优化 virsh 控制台恢复(--resume)功能
- 启动时自动连接控制台（--console）、控制台连接后自动恢复暂停状态（--resume）

### 7.5.pcp 6.2.2

- PMDA 增强和新增功能：新增对指标标签的支持、新增 mem.vmmemctl 虚拟机内存balloon指标、新增 HugePage、文件系统 UUID、TCP 扩展指标
- 安全增强：服务初始化脚本（pmie/pmlogger/pmcd）以更低权限运行（pcp:pcp 用户）

### 7.6.docker-ce 28.0.1

- 通过 OpenCloudOS 社区 EPOL9 软件源可获取 docker-ce 28.0.1 版本
- docker-proxy 更新：docker-proxy 二进制文件更新，旧版本无法与新 dockerd 兼容；不再使用 rootlesskit-docker-proxy
- DNS 配置调整：从主机 /etc/resolv.conf 读取的 DNS 服务器始终从主机网络命名空间访问；特定情况下不再使用 Google 的 DNS 服务器
- 端口发布与网络隔离：dockerd 在 Linux 内核中需要 ipset 支持；广泛修改 iptables 和 ip6tables 规则实现端口发布和网络隔离，涉及功能变化和规则清理；修复多个端口相关的安全问题和连接问题；新增 gateway_mode_ipv[46] 网络模式选项。
- IPv6 支持提升：docker network create 添加--ipv4选项；--ipv6 守护进程选项使用更灵活；IPAM 可处理更大的子网；禁用桥接网络中地址的重复地址检测；改进 host-gateway 与 IPv6-only 网络的兼容性。

## 8.编解码

### 8.1.libvpx 1.14.1

- Neon (Arm)指令集优化带来 VoD 视频处理速度提升，bitdepth 8 提升 12-35%，对于高 bitdepth 提升可达 68%-151%。
- 对 x86 平台的 AVX2 和 SSE 指令集和龙芯的 LSX 指令集也进行了优化改进。
- 在 speed 0 VoD encoding（质量最高速度最慢）上速度提升 42-49

## 9.web远程桌面

### 9.1.KasmVNC

- Web 化访问：无需安装客户端，通过浏览器（Chrome/Firefox）直接连接远程桌面，支持响应式设计。
- 安全升级：内置 TLS 加密，支持 LDAP/OAuth/SAML 等身份验证，密码策略更灵活。
- 性能优化：采用 VP8/VP9 编码，动态调整压缩率，低带宽场景下延迟显著降低。功能扩展：支持双向剪贴板同步、文件传输，可集成至容器化工作流（如 Docker）。

## 10.AI 大模型生态

### 9.1 AI 算力引擎加速

- AI 高性能文件系统 DeepSeek 3FS 支持 OC9 已支持 DeekSeek 官方分布式高速文件系统 3FS 快速编译构建和部署。使用 OC9 进行部署构建已获得 3FS 官方支持，OC9 还提供相关镜像方便快速编译构建。
- OCAI Agent 支持 DeepSeek-R1 深度思考模型，增强复杂问题的推理能力，提供更精准的解决方案；支持模型切换，用户可根据需求灵活选择混元或者deepseek 模型，适配不同场景；优化客户端体验，改进交互流程，提升响应速度。

# 下载体验

## 1.手动下载

- ISO：https://mirrors.opencloudos.tech/opencloudos/9.4/isos/ 其中，包含以下几种 ISO 类型： boot.iso， 启动安装用 ISO，需联网加载软件包（适合网络安装） everything.iso，包含完整软件包集合的安装镜像（适合离线安装或本地源部署） minimal.iso， 精简安装镜像，仅包含基础系统组件（适合构建最小化系统）
- QCOW2：https://mirrors.opencloudos.tech/opencloudos/9.4/images/qcow2/
- Docker：https://mirrors.opencloudos.tech/opencloudos/9.4/images/docker/ 请根据实际需求选择对应架构和镜像类型进行下载与安装。

## 2.docker pull

- 标准镜像 docker pull opencloudos/opencloudos9:latest 标准镜像包含大量服务器操作系统所需的常用软件，从物理机迁移业务方便，但体积较大。适合不在意镜像体积大小，想直接体验各种常用软件的用户。
- minimal 镜像 docker pull opencloudos/opencloudos9-minimal:latest minimal 镜像使用 dnf（yum）作为包管理器，coreutils 为 Linux 工具集。是包含包管理器完整功能的最小镜像。常规情况推荐使用这款镜像。