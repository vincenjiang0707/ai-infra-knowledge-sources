source: https://docs.nvidia.com/dynamo/zh-CN/v1.3.0/components/planner/planner-guide
lastmod: 2026-09-23T23:30:39.914Z

Planner 指南


Planner 指南

Dynamo Planner 是一个自动扩缩容控制器，会在运行时调整 prefill 和 decode 引擎的副本数，以满足延迟 SLA。它读取流量信号（Prometheus 指标或负载预测器输出）和引擎性能模型，用于决定何时扩容或缩容。

如需快速概览，请参阅 [Planner overview](https://docs.nvidia.com/dynamo/dev/components/planner)。如需了解架构内部机制，请参阅 [Planner 设计](https://docs.nvidia.com/dynamo/zh-CN/dev/design-docs/component-design/planner-design)。

## 扩缩容模式

planner 支持四个优化目标，这些目标决定扩缩容决策的方式：

（默认）：基于队列深度和 KV cache 利用率使用静态阈值。不需要 SLA 目标或 profiling。开箱即用。`throughput`

：与`latency`

`throughput`

采用相同方法，但使用更激进的阈值，即更早扩容并容忍更少排队。适合对延迟敏感的工作负载。：使用用户定义的 prefill 队列 token 阈值和 decode KV 利用率阈值，进行反应式的基于负载扩缩容。`load`

：使用 Rust 引擎性能模型 shim；原生 AIC 可用时直接使用 AIC 估算，并结合在线 FPM 调优，否则回退到 FPM 回归模型。支持基于吞吐量（预测式）和基于负载（反应式）的扩缩容模式。适合需要精确 SLA 控制的高级用户。`sla`


**何时使用哪种模式：**

- 从
（默认）开始，它无需配置即可立即工作。`throughput`

- 如果工作负载有严格的延迟要求，并且你更倾向于过度预配置而不是排队，请切换到
。`latency`

- 当你希望通过 prefill 队列和 decode KV 利用率阈值直接控制扩缩容时，请使用
。`load`

- 当你有部署前 profiling 数据，并希望以特定 TTFT/ITL 值为目标时，请使用
。`sla`


## PlannerConfig 参考

planner 通过 `PlannerConfig`

JSON/YAML 对象进行配置。使用 profiler 时，该对象位于 DGDR 规范的 `features.planner`

部分下：

对于基于 SLA 的扩缩容：

若要在不改变副本数的情况下评估 Planner 行为，请启用 advisory 模式：

advisory 模式仅提供建议。Planner 会计算建议副本数、记录日志、将其导出为诊断信息，并显示在 HTML 报告中。这些建议不会作为扩缩容决策应用：Planner 不会执行扩缩容操作，也不会更改部署。

### 优化目标

当 `optimization_target`

为 `throughput`

、`latency`

或 `load`

时，会自动启用基于负载的扩缩容，并禁用基于吞吐量的扩缩容。`ttft_ms`

/`itl_ms`

字段会被忽略。

### 扩缩容模式字段（SLA 模式）

使用 `optimization_target: sla`

时，必须至少启用一种扩缩容模式。

### 部署前扫描

SLA 模式使用 Rust 引擎性能模型 shim。如果配置了 `aic_perf_model`

，planner 会用原生 AIC 模型身份和引擎上限初始化 shim；如果该模型不被原生 AIC 支持，shim 会自动回退到基于观测 FPM 的回归模型。如果没有配置 `aic_perf_model`

，shim 会从 FPM 回归模型启动，并在自基准测试或在线 FPM 观测足够后变为可用。

启动时，planner 总会先尝试从 `get_perf_metrics`

Dynamo 端点获取自基准测试结果。如果不可用，则在配置存在时回退到 rapid 模式 AIC interpolation 数据或 `profile_results_dir`

中 profiler 生成的数据（npz 或 JSON）。这些数据都会转换为 ForwardPassMetrics，并用于调优或启动性能模型。当 `pre_deployment_sweeping_mode: none`

时，planner 仍然可以启动；吞吐量决策会在原生 AIC 可用或在线 FPM 足够之前报告 `model_not_ready`

。

手动配置原生 AIC 性能模型：

### 基于吞吐量的扩缩容设置

### 基于负载的扩缩容设置

### 通用设置

### 流量预测设置

KV hit rate 和 speculative decode accept length 是引擎/Router 运行时信号，不是流量形状。Planner 会保存每个信号最新的有效观测值，并在新的有效值到达前复用它。冷启动时，缺失的 KV hit rate 表示不做 prefix-cache discount，缺失的 accept length 表示 `1.0`

。

### Kalman Filter 设置

### 诊断报告

这些报告中展示的同一组诊断信号也会以 `dynamo_planner_*`

前缀导出为 Prometheus 指标，例如估算的 TTFT/ITL（`dynamo_planner_estimated_ttft_ms`

、`dynamo_planner_estimated_itl_ms`

）、建议副本数（`dynamo_planner_predicted_num_prefill_replicas`

、`dynamo_planner_predicted_num_decode_replicas`

）、每个引擎的容量和 FPM 队列深度，以及负载/吞吐量扩缩容决策枚举。

Replica Counts 图会将实际 prefill/decode 副本与 Planner 建议的 prefill/decode 副本的离散建议标记叠加显示。当 `advisory: true`

时，这些建议数量仅作为建议；Planner 会记录它本会执行的操作，但不会应用该变更。

### 调度 / plugin pipeline

Planner 默认通过内置 plugin pipeline 运行。基础 pipeline cadence 位于 `PlannerConfig`

的 `scheduling`

子树；plugin 注册、transport 和认证设置位于 `plugin_registration`

。

现有 planner 字段仍然驱动内置 plugin：

`load_adjustment_interval_seconds`

调度`builtin_load_propose`

。它读取 FPM 和 worker count 观测，并执行当前 load-based 算法。`throughput_adjustment_interval_seconds`

调度`builtin_load_predict`

和`builtin_throughput_propose`

。Throughput propose 依赖同一个 tick 里的 prediction，因此只会在 predict plugin 触发的 tick 中执行。- 当两个 proposer 在同一个 tick 都产生目标时，load-based scaling 在 throughput-based scaling 之后运行，保留现有行为：throughput 先更新副本数下限，load-based scaling 再在该 floor 之上调整并应用全局 GPU budget clamp。
- Plugin pipeline 结束后，planner 会对 builtin 和外部 plugin 的目标统一应用最终的
`min_endpoint`

和 GPU-budget safety check，然后才执行扩缩容。

#### DGDR 示例

## 与 Profiler 集成

当 profiler 在启用 planner 的情况下运行时，它会：

- 选择最佳 prefill 和 decode 引擎配置
- 生成可选的引擎性能启动数据（prefill TTFT vs ISL、decode ITL vs KV-cache 利用率）
- 将
`PlannerConfig`

和可选性能数据保存到独立的 Kubernetes ConfigMaps 中 - 将 planner 服务添加到生成的 DGD，并配置为从这些 ConfigMaps 读取

planner 通过 `--config /path/to/planner_config.json`

接收其配置，该文件从 `planner-config-XXXX`

ConfigMap 挂载。当生成 thorough 启动数据时，profiling 数据会从 `planner-profile-data-XXXX`

ConfigMap 挂载。

请参阅 [Profiler Guide](https://docs.nvidia.com/dynamo/dev/components/profiler/profiler-guide)，了解完整 profiling 工作流以及如何配置部署前扫描。

## 分层部署

如果你希望一个模型拥有一个公共端点，但同时有多个针对不同请求类别优化的私有 DGD，请使用分层部署：

- 一个包含
`Frontend`

、`GlobalRouter`

和`GlobalPlanner`

的 control DGD - 一个或多个 prefill pool DGD
- 一个或多个 decode pool DGD

在当前工作流中，请为每个目标 pool 独立运行 profiling，然后手动组合最终的 control DGD 和 pool DGD。请参阅 [Global Planner Guide](https://docs.nvidia.com/dynamo/dev/components/planner/global-planner-guide)。

## 另请参阅

[Planner overview](https://docs.nvidia.com/dynamo/dev/components/planner)— 为什么 LLM 推理需要不同的 autoscaler[Planner 设计](https://docs.nvidia.com/dynamo/zh-CN/dev/design-docs/component-design/planner-design)— 架构和算法内部机制[DGDR Examples](https://docs.nvidia.com/dynamo/dev/kubernetes-deployment/deploy-models/dgdr-examples)— DGDR YAML 示例、样例配置、高级模式[Global Planner Guide](https://docs.nvidia.com/dynamo/dev/components/planner/global-planner-guide)— 多 DGD 协调、共享 GPU 预算、单端点多 pool 部署[Profiler Guide](https://docs.nvidia.com/dynamo/dev/components/profiler/profiler-guide)— profiling 数据的生成方式