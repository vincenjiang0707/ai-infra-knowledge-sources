# [Issue #2444] [Feature Request]: 集成绿算技术 GP 系列 NVMe-oF 存储后端，打造极致性能的 Mooncake 大模型推理集群

source: https://github.com/kvcache-ai/Mooncake/issues/2444
state: closed | updated: 2026-09-23T03:15:47Z
labels: stale, auto-closed

## 正文

### Describe your feature request

尊敬的 Mooncake 团队：
您好！我们是绿算技术有限公司，国内唯一原生对标 NVIDIA G3/3.5 存储 (CMX) 的解决方案厂商。我们高度关注并赞赏 Mooncake 项目在大模型推理 KV Cache 存储优化领域的开创性工作，注意到项目正在积极推进原生 NVMe-oF 后端 (Storage Backend) 的 RFC 规范与代码集成（如 SsdKvStorageBackend 分支），旨在通过远程存储突破单节点内存墙限制。
我们的 GP 系列通用直连数据栈 (GDDS) 产品（GP-5000/6000/7000/8000）基于全栈自研的 ASIC 加速芯片打造，是专为 AI 大模型推理设计的硬件级高性能 NVMe-oF 存储设备，能够完美适配 Mooncake 的存算分离架构。将 GP 系列设备接入 Mooncake Store，将为大模型推理集群带来三个决定性的改变：
**1. 打通跨机架的 "缓存一致性"，实现真正的 "KV Cache 自由路由"**
在纯本地 SSD 方案中，A 节点的缓存冷了落盘到本地，B 节点是读不到的（除非跨网拷贝）。引入 GP-5000 后，它变成了全集群的全局共享存储池。任何 Prefill 节点写进去的 KV Cache，任何 Decode 节点都能以 **≤20 微秒 ** 的端到端延迟直接读取，这一性能指标已在 NVIDIA 官方测试环境中得到验证。
**2. 动态全局负载均衡，彻底消除 "长尾延迟"**
本地 SSD 方案如果遇到某台机器被高频请求（比如某个爆火的 Agent 提示词恰好在它的 SSD 里），该节点的本地 IO 就会过载，导致请求卡顿。GP-5000 提供1620 万 IOPS、GP-6000 提供3240 万 IOPS的超高并发能力，可以轻松把高频热点切片打散到数十块盘上并发读取，彻底消除单点 IO 瓶颈。
**3. 计算节点彻底 "Diskless（无盘化）"，大幅降低 TCO**
GPU 服务器不再需要配置昂贵、高功耗且易损坏的大容量本地 NVMe U.2/U.3 硬盘。所有的长文本缓存、模型 Checkpoint 全部卸载到 GP 系列存储阵列中，降低了计算节点的硬件复杂度和故障率，同时减少了散热和电力消耗，整体 TCO 下降 30% 以上。

**我们的核心技术壁垒：自研 ASIC 加速芯片**
上述性能优势的核心支撑是绿算技术自主研发的两款专用存储加速芯片，我们采用 "FPGA 验证先行→ASIC 量产迭代" 的技术路线，目前两款芯片均已完成 FPGA 验证并批量应用于 GP 全系列产品，正在推进 PCIe Gen5 ASIC 芯片的流片工作。
**1. NVMe-oF ASIC 芯片（数据传输核心）**
核心功能：实现网络协议全硬件卸载，让数据从存储设备直接传输到 GPU 显存，完全绕开主机 CPU 和传统软件栈，从物理层面消除 "CPU 瓶颈" 和 "协议开销"。
关键性能：端到端读写延迟≤20 微秒，4 盘 NVMe SSD 聚合读取带宽达 144GB/s，原生支持 RoCEv2/RoCE RDMA 协议和 NVIDIA GPU Direct Storage (GDS) 技术。
技术价值：是实现 "KV Cache 自由路由" 和计算节点 Diskless 架构的核心，让远程存储的访问性能媲美服务器主板直插 SSD。
**2. "ASIC+DPU+FPGA" 多架构并行设计**
区别于 Supermicro 等厂商的单一 DPU 路线，绿算技术采用 "ASIC+DPU+FPGA"三元异构架构，将 ASIC 芯片作为性能底座，结合 FPGA 的灵活性和 DPU 的智能调度能力，实现" 多车道并行 " 的极致效率：
GP-5000：集成专用 ASIC 芯片，内置 100Gb 网卡，实现硬件级协议卸载，是构建大规模存算分离架构的基础单元。
GP-6000：采用 "ASIC+FPGA" 异构架构，性能较 GP-5000 翻倍，支持 GPU 与存储之间的直接数据通路。
GP-7000：采用 "DPU+ASIC+FPGA" 三元架构，将 KV Cache 的索引管理、数据压缩和网络协议栈完全硬件卸载，AI 推理效率提升 20 倍，每 GB/s 带宽功耗仅 3.1W。
**我们的产品生态与兼容性**
原生适配 NVIDIA 生态：全系列产品完全兼容 NVIDIA G3/3.5 存储架构 (CMX)，已完成与 BlueField-3/4 DPU、Spectrum-X 交换机的兼容性验证。
全栈自研可控：从底层芯片 IP、RTL 代码到固件、驱动程序全部自主开发，不存在技术卡脖子风险，可根据项目需求快速定制功能。
多形态产品覆盖：提供从机架式、工作站到桌面化的全系产品，满足不同规模推理集群的部署需求。
**合作提议**
我们非常看好 Mooncake 项目在大模型推理优化领域的领先地位，愿意全力支持项目的 NVMe-oF 后端开发工作：
免费提供GP-5000/6000 测试设备供 Mooncake 团队进行性能验证和集成测试
派遣资深芯片与系统工程师全程配合后端对接和调优工作，提供芯片级技术支持
共同开发针对 Mooncake 架构优化的专用存储驱动和 KV Cache 调度策略
分享我们在 NVIDIA CMX 架构和硬件级 KV Cache 存储优化方面的技术积累和工程经验
联系方式
公司官网：[www.luisuantech.com]
邮箱：market@Luisuantech.com
地址：北京海淀区西直门北大街甲 43 号金运大厦 A 座 803 室
我们期待能与 Mooncake 团队深入合作，共同打造业界领先的大模型推理基础设施，推动 AI 技术的普及与发展。
感谢您的考虑！
绿算技术有限公司
2026 年 6 月 12 日

### Before submitting a new issue...

- [x] Make sure you already searched for relevant issues and read the [documentation](https://kvcache-ai.github.io/Mooncake/)

## 评论 (11)

### github-actions[bot] · 2026-06-12

Thanks for opening this issue, @Luisuantech!

| Field | Value |
|-------|-------|
| **Issue** | #2444 |
| **GitHub user ID** | `293029622` |
| **Reporter** | @Luisuantech |

A maintainer will triage this when possible. To help us respond faster, please include:

- Mooncake version or commit SHA
- Environment (OS, CUDA/driver, RDMA stack if relevant)
- Steps to reproduce and expected vs. actual behavior

Useful links: [Documentation](https://kvcache-ai.github.io/Mooncake/) · [Contributing guide](https://github.com/kvcache-ai/Mooncake/blob/main/CONTRIBUTING.md)

> This message was posted automatically by the issue bot.

### Luisuantech · 2026-06-12

[绿算技术通用直连数据栈产品介绍.pdf](https://github.com/user-attachments/files/28871614/default.pdf)
这是我们的产品介绍资料

### ykwd · 2026-06-15

感谢您详细的介绍，请问 GP 系列产品是一个分布式NVMe存储集群吗？对上提供的接口是什么样的呢（例如类似于分布式文件系统）那样吗？

### Luisuantech · 2026-06-15

> 感谢您详细的介绍，请问 GP 系列产品是一个分布式NVMe存储集群吗？对上提供的接口是什么样的呢（例如类似于分布式文件系统）那样吗？

感谢您的提问，我简单给您说明两点：
1、不是传统意义上的分布式 NVMe 存储集群。单台 GP 就是一个完整的 NVMe-oF Target 节点，多台可以通过 RoCEv2网络横向扩容，拼成全局共享的块存储资源池，没有额外的自研分布式管控面，架构上就是存算分离的远程高速块存储。
2、对外提供标准 NVMe-oF 块接口（RoCEv2 RDMA），用通用 NVMe-oF 客户端就能直接挂载成标准块设备，不需要任何私有驱动或定制组件。原生支持 GDS 直连 GPU，没有文件系统额外开销，可以直接对接你们在做的 SsdKvStorageBackend。

### LujhCoconut · 2026-06-15

> > 感谢您详细的介绍，请问 GP 系列产品是一个分布式NVMe存储集群吗？对上提供的接口是什么样的呢（例如类似于分布式文件系统）那样吗？
> 
> 感谢您的提问，我简单给您说明两点： 1、不是传统意义上的分布式 NVMe 存储集群。单台 GP 就是一个完整的 NVMe-oF Target 节点，多台可以通过 RoCEv2网络横向扩容，拼成全局共享的块存储资源池，没有额外的自研分布式管控面，架构上就是存算分离的远程高速块存储。 2、对外提供标准 NVMe-oF 块接口（RoCEv2 RDMA），用通用 NVMe-oF 客户端就能直接挂载成标准块设备，不需要任何私有驱动或定制组件。原生支持 GDS 直连 GPU，没有文件系统额外开销，可以直接对接你们在做的 SsdKvStorageBackend。

所以最后是走GDS+NVMe-oF路线吗？ 类似于也是把这个GP组成一个ssd pool ? 然后可以GDS访问吗？

### Luisuantech · 2026-06-15

> > > 感谢您详细的介绍，请问 GP 系列产品是一个分布式NVMe存储集群吗？对上提供的接口是什么样的呢（例如类似于分布式文件系统）那样吗？
> > 
> > 
> > 感谢您的提问，我简单给您说明两点： 1、不是传统意义上的分布式 NVMe 存储集群。单台 GP 就是一个完整的 NVMe-oF Target 节点，多台可以通过 RoCEv2网络横向扩容，拼成全局共享的块存储资源池，没有额外的自研分布式管控面，架构上就是存算分离的远程高速块存储。2、对外提供标准 NVMe-oF 块接口（RoCEv2 RDMA），用通用 NVMe-oF 客户端就能直接挂载成标准块设备，不需要任何私有驱动或定制组件。原生支持 GDS 直连 GPU，没有文件系统额外开销，可以直接对接你们在做的 SsdKvStorageBackend。
> 
> 所以最后是走GDS+NVMe-oF路线吗？类似于也是把这个GP组成一个SSD池？然后可以GDS访问吗？

感谢您的提问，我简单给您说明内容：
1、GDS和NVMe-oF两者都支持，GDS 是运行在 NVMe-oF 之上的 GPU 直存能力；
2、单台 GP 内部已将多块 SSD 聚合为块存储资源池，多台可通过 RDMA 网络横向扩容，相当于组成一个共享池；
3、GDS 访问完全支持，数据路径与本地 NVMe 盘走 GDS 一致。

### Luisuantech · 2026-06-17

> > > 感谢您详细的介绍，请问 GP 系列产品是一个分布式NVMe存储集群吗？对上提供的接口是什么样的呢（例如类似于分布式文件系统）那样吗？
> > 
> > 
> > 感谢您的提问，我简单给您说明两点： 1、不是传统意义上的分布式 NVMe 存储集群。单台 GP 就是一个完整的 NVMe-oF Target 节点，多台可以通过 RoCEv2网络横向扩容，拼成全局共享的块存储资源池，没有额外的自研分布式管控面，架构上就是存算分离的远程高速块存储。2、对外提供标准 NVMe-oF 块接口（RoCEv2 RDMA），用通用 NVMe-oF 客户端就能直接挂载成标准块设备，不需要任何私有驱动或定制组件。原生支持 GDS 直连 GPU，没有文件系统额外开销，可以直接对接你们在做的 SsdKvStorageBackend。
> 
> 所以最后是走GDS+NVMe-oF路线吗？类似于也是把这个GP组成一个SSD池？然后可以GDS访问吗？

[Mooncake 与绿算ForinnBase GroundPool如何联手打破推理僵局？.pdf](https://github.com/user-attachments/files/29032293/Mooncake.ForinnBase.GroundPool.pdf)
这是我们公众号上构想的与mooncake的合作，如果可以添加您的联系方式进行更深入的交流

### LujhCoconut · 2026-06-17

@Luisuantech 我的微信 Zephyr_Coconut

### Luisuantech · 2026-06-17

> [@Luisuantech](https://github.com/Luisuantech) 我的微信 Zephyr_Coconut

收到，已向您发送添加申请

### github-actions[bot] · 2026-09-16

This issue has had no activity for 90 days and will be closed in 7 days if there is no further activity. Please comment or react if it should stay open.

### github-actions[bot] · 2026-09-23

Closing due to 3 months of inactivity. If this is still relevant, please comment and we can reopen.
