source: https://docs.nvidia.com/dynamo/zh-CN/dev/knowledge-base/modular-components/router/overview
lastmod: 2026-09-23T23:30:39.914Z

# Router

Dynamo KV Router 通过评估不同 worker 上的计算成本来智能地路由请求。它同时考虑解码成本（来自活动 block）和预填充成本（来自新计算的 block），并利用 KV cache 重叠来尽量减少重复计算。优化 KV Router 对于在分布式推理部署中实现最大吞吐量和最低延迟至关重要。

## 快速开始

我们可以通过 Dynamo frontend 使用 KV Router：

对于 Kubernetes，请在 Frontend service 上设置 `DYN_ROUTER_MODE=kv`

。对于事件驱动的 KV 状态，请使用 [Router Operations](https://docs.nvidia.com/dynamo/dev/knowledge-base/modular-components/router/router-operations#additional-notes) 中描述的后端专用 flag，配置 backend worker 发布 KV cache 事件。仅当你希望使用近似的 cache 状态预测时，才使用 `--no-router-kv-events`

。

### 独立 Router

你也可以将 KV router 作为独立服务运行（不使用 Dynamo frontend）。更多详细信息请参阅 [Standalone Router component](https://github.com/ai-dynamo/dynamo/tree/main/components/src/dynamo/router/)。

有关部署模式和快速开始步骤，请参阅 [Router Guide](https://docs.nvidia.com/dynamo/dev/knowledge-base/modular-components/router/router-guide)。有关 CLI 参数和调优指南，请参阅 [Configuration and Tuning](https://docs.nvidia.com/dynamo/dev/knowledge-base/modular-components/router/configuration-and-tuning)。有关 A/B 基准测试，请参阅 [KV Router A/B Benchmarking Guide](https://docs.nvidia.com/dynamo/dev/recipes/benchmarks/kv-router-ab-testing)。

## 前提条件和限制

**要求：**

**仅支持动态 endpoint**：KV router 要求使用`model_input=ModelInput.Tokens`

调用`register_model()`

。你的 backend handler 会接收带有`token_ids`

的预分词请求，而不是原始文本。- Backend worker 必须使用
`model_input=ModelInput.Tokens`

调用`register_model()`

（请参阅[Backend Guide](https://docs.nvidia.com/dynamo/dev/advanced-customizations/writing-custom-backends/writing-python-workers)） - 使用 KV routing 时请使用动态发现，以便 router 跟踪 worker 实例及其 KV cache 状态

**多模态支持：**

**通过多模态 hash 进行图像路由**：在已文档化的 TRT-LLM 和 vLLM router 路径中受支持。**其他 backend 或模态组合**：在依赖多模态 hash routing 之前，请检查相应 backend 的多模态文档。

**限制：**

- KV routing 不支持静态 endpoint；请使用动态发现，以便 router 跟踪 worker 实例及其 KV cache 状态

对于不使用 KV routing 的基础模型注册，请在静态和动态 endpoint 中使用 `--router-mode round-robin`

、`--router-mode random`

、`--router-mode least-loaded`

或 `--router-mode device-aware-weighted`

。

## 后续步骤

：部署模式、快速开始和页面地图[Router Guide](https://docs.nvidia.com/dynamo/dev/knowledge-base/modular-components/router/router-guide)：成本模型和 worker 选择行为[Routing Concepts](https://docs.nvidia.com/dynamo/dev/knowledge-base/modular-components/router/routing-concepts)：Router flag、传输模式和指标[Configuration and Tuning](https://docs.nvidia.com/dynamo/dev/knowledge-base/modular-components/router/configuration-and-tuning)：Prefill 和 decode 路由设置[分离式服务](https://docs.nvidia.com/dynamo/dev/knowledge-base/modular-components/router/disaggregated-serving)：副本、持久化和恢复[Router Operations](https://docs.nvidia.com/dynamo/dev/knowledge-base/modular-components/router/router-operations)：Python API 用法、K8s 示例和自定义路由模式[Router Examples](https://docs.nvidia.com/dynamo/dev/knowledge-base/modular-components/router/router-examples)：从 Rust 单元测试到基于 fixture 的 replay 和完整进程 E2E 的测试层级[Router Testing](https://docs.nvidia.com/dynamo/dev/knowledge-base/modular-components/router/router-testing)：将 KV indexer 作为单独服务运行，以便独立扩缩容[Standalone Indexer](https://docs.nvidia.com/dynamo/dev/knowledge-base/modular-components/router/standalone-indexer)：架构细节、算法和事件传输模式[Router Design](https://docs.nvidia.com/dynamo/dev/knowledge-base/modular-components/router/router-design)