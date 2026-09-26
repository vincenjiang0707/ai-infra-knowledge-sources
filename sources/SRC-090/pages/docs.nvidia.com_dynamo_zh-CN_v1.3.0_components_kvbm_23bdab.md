source: https://docs.nvidia.com/dynamo/zh-CN/v1.3.0/components/kvbm
lastmod: 2026-09-23T23:30:39.914Z

# KVBM

Dynamo KV Block Manager (KVBM) 是一个可扩展的运行时组件，旨在为异构和分布式环境中的推理任务处理 Key-Value (KV) 块的内存分配、管理和远程共享。它可作为 vLLM 和 TensorRT-LLM 等框架的统一内存层和直写缓存。

KVBM 提供：

- 跨 GPU 内存、固定主机内存、远程 RDMA 可访问内存、本地/分布式 SSD，以及远程文件/对象/云存储系统的
**统一内存 API** - 支持带有基于事件状态转换的
**块生命周期**（allocate → register → match） - 与
集成；NIXL 是一个动态内存交换层，用于内存块的远程注册、共享和访问[NIXL](https://github.com/ai-dynamo/nixl/blob/main/docs/nixl.md)


开始使用：请参阅[KVBM 指南]，了解安装和部署说明。

## 何时使用 KV Cache 卸载

KV Cache 卸载可以避免代价高昂的 KV Cache 重新计算，从而缩短响应时间并改善用户体验。服务提供方可获得更高吞吐量和更低的单 token 成本，使推理服务更具可扩展性且更高效。

当 KV Cache 超出 GPU 内存，并且缓存复用收益超过数据传输开销时，将 KV cache 卸载到 CPU 或存储最为有效。它在以下场景中尤其有价值：

## 功能支持矩阵

## 架构

*Dynamo KV Block Manager 的高层分层架构视图，以及它如何与 LLM 推理生态系统中的不同组件交互*

KVBM 有三个主要逻辑层：

**LLM Inference Runtime Layer** — 顶层包含推理运行时（TensorRT-LLM、vLLM），它们通过专用连接器模块集成到 Dynamo KVBM。这些连接器充当转换层，将运行时特定的操作和事件映射到 KVBM 面向块的内存接口。这样可以将内存管理与推理运行时解耦，从而支持后端可移植性和内存分层。

**KVBM Logic Layer** — 中间层封装核心 KV block manager 逻辑，并作为管理块内存的运行时基础。KVBM adapter 会对来自不同运行时的请求表示和数据布局进行规范化，并将其转发给核心内存管理器。该层实现表查找、内存分配、块布局管理、生命周期状态转换，以及块复用/淘汰策略。

**NIXL Layer** — 底层为所有数据和存储事务提供统一支持。NIXL 支持 P2P GPU 传输、RDMA 和 NVLink 远程内存共享、动态块注册和元数据交换，并为存储后端提供插件接口，包括块内存（GPU HBM、Host DRAM、Remote DRAM、Local SSD）、本地/远程文件系统、对象存储和云存储。


了解更多：请参阅[KVBM 设计文档]，了解详细架构、组件和数据流。

## 后续步骤

— 安装、配置和部署说明[KVBM 指南](https://docs.nvidia.com/dynamo/dev/user-guides/kv-cache-offloading)— 架构深入解析、组件和数据流[KVBM 设计](https://docs.nvidia.com/dynamo/dev/design-docs/component-design/kvbm-design)— 将 LMCache 与 Dynamo vLLM 后端配合使用[LMCache 集成](https://docs.nvidia.com/dynamo/dev/integrations/kv-cache-integrations/lm-cache)— 使用 FlexKV 进行 KV cache 管理[FlexKV 集成](https://docs.nvidia.com/dynamo/dev/integrations/kv-cache-integrations/flex-kv)— 通过 NIXL 启用 SGLang 的分层缓存[SGLang HiCache](https://docs.nvidia.com/dynamo/dev/integrations/kv-cache-integrations/hi-cache)— NIXL 通信库详细信息[NIXL Documentation](https://github.com/ai-dynamo/nixl/blob/main/docs/nixl.md)