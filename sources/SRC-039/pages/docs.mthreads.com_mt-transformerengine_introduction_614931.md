source: https://docs.mthreads.com/mt-transformerengine/introduction

# MT-TransformerEngine 入门

## 1. MT-TransformerEngine 是什么[](https://docs.mthreads.com#1-mt-transformerengine-是什么)

[Transformer Engine](https://github.com/NVIDIA/TransformerEngine) 是面向 Transformer 模型的低精度训练与高性能算子库。它提供优化后的 Linear、LayerNorm、Attention 等模块，并通过 FP8 recipe、缩放因子和自动混合精度上下文管理低精度计算。

**MT-TransformerEngine（MT-TE）** 基于 Transformer Engine 和 [torch_musa](https://github.com/MooreThreads/torch_musa) 适配，使摩尔线程 GPU 能够使用 FP8 训练和相关融合优化。它可以单独用于 PyTorch 模块，也可以与 MT-Megatron 集成到大模型训练中。

### 1.1 适用场景[](https://docs.mthreads.com#11-适用场景)

- 在摩尔线程 GPU 上验证 FP8 forward/backward；
- 用 TE 模块替换普通 PyTorch Transformer 层；
- 降低大模型训练的计算和通信成本；
- 在 MT-Megatron 中使用 FP8、TP overlap、MoE 重计算等优化；
- 对比 BF16 与 FP8 的吞吐、显存和数值稳定性。

### 1.2 设计特点[](https://docs.mthreads.com#12-设计特点)

**高性能模块**：提供融合或定制实现的 Transformer 核心层；**FP8 recipe**：统一配置格式、缩放、统计与更新策略；**作用域控制**：通过`fp8_autocast`

控制哪些 forward 使用 FP8；**训练框架集成**：可与 Megatron 的并行和 checkpoint 体系组合；**MUSA 内核**：通过 MUSA C++/kernel 和`torch_musa`

执行实际计算。

## 2. 核心架构[](https://docs.mthreads.com#2-核心架构)

### 2.1 主要组件[](https://docs.mthreads.com#21-主要组件)

| 组件 | 作用 |
|---|---|
| TE PyTorch Modules | Linear、LayerNorm、TransformerLayer 等高性能模块 |
| FP8 Recipe | 定义 FP8 格式、margin、缩放与统计策略 |
`fp8_autocast` | 开启或关闭指定代码段中的 FP8 计算 |
| Scaling Metadata | 维护 amax、scale、scale inverse 等状态 |
| Fused Kernels | 执行 GEMM、归一化、激活等融合计算 |
| Distributed Integration | 与 TP、通信 overlap、MoE 等训练能力协作 |
| torch_musa / MUSA Kernels | 提供设备、运行时和底层算子实现 |

### 2.2 一次 FP8 forward 如何运行[](https://docs.mthreads.com#22-一次-fp8-forward-如何运行)

`BF16/FP32 输入`

↓

读取 FP8 recipe 与历史 amax

↓

计算或更新 scaling factor

↓

输入/权重转换为目标 FP8 格式

↓

执行 MUSA FP8 kernel / GEMM

↓

输出以训练所需精度返回

↓

反向传播并更新 FP8 metadata



FP8 不只是把 tensor 类型改成 8 bit。训练稳定性取决于数值格式、缩放策略、amax 历史、累加精度以及不同算子的精度边界。

## 3. 如何选择精度与集成方式[](https://docs.mthreads.com#3-如何选择精度与集成方式)

### 3.1 BF16 基线与 FP8[](https://docs.mthreads.com#31-bf16-基线与-fp8)

建议先建立可收敛的 BF16 基线，再开启 FP8：

`BF16 基线正确`

↓

单层 TE 模块 FP8 forward/backward

↓

小规模模型数值对比

↓

完整模型 FP8 训练

↓

多卡与性能优化



若直接从完整多机 FP8 任务开始，模型、数据、�并行、通信或低精度任一环节都可能成为错误来源。

### 3.2 独立模块与 MT-Megatron 集成[](https://docs.mthreads.com#32-独立模块与-mt-megatron-集成)

| 方式 | 适合用途 |
|---|---|
独立 `te.Linear` 等模块 | 功能验证、算子开发、最小复现 |
| 自定义 PyTorch 模型使用 TE 模块 | 局部替换和性能优化 |
| MT-Megatron 集成 | 大模型、多机、TP/PP/EP 等完整训练 |

### 3.3 FP8 format 与 recipe[](https://docs.mthreads.com#33-fp8-format-与-recipe)

E4M3 通常具有更多尾数位，适合需要较高精度的 forward；其他格式可能提供更大动态范围。具体选择应以 MT-TE 当前支持的 recipe 和目标模型验证结果为准，不要直接照搬其他硬件或软件版本的配置。

## 4. MUSA 环境准备[](https://docs.mthreads.com#4-musa-环境准备)

### 4.1 版本匹配[](https://docs.mthreads.com#41-版本匹配)

MT-TE 依赖下列组件共同工作：

- 宿主机 MUSA Driver；
- 容器中的 MUSA Runtime；
- PyTorch 与
`torch_musa`

； - MT-TransformerEngine 源码和编译产物；
- 使用 MT-TE 的 MT-Megatron 版本；
- 多卡任务需要 MCCL。

进入容器后先检查：

`mthreads-gmi`

python3 -c "import torch, torch_musa; print(torch.__version__, torch_musa.__version__)"

python3 -c "import transformer_engine; print(transformer_engine.__file__)"



### 4.2 编译安装[](https://docs.mthreads.com#42-编译安装)

本项目使用仓库提供的安装脚本：

`bash install.sh`



它会编译下列目录中的 MUSA 内核和 C++ 源码：

`transformer_engine/musa/common`

transformer_engine/musa/pytorch/csrc



编译失败时应保留完整日志，并核对编译器、Python、PyTorch ABI、MUSA SDK 和环境变量，而不是只重试安装命令。

### 4.3 安装后验证[](https://docs.mthreads.com#43-安装后验证)

`python3 - <<'PY'`

import torch

import torch_musa

import transformer_engine.pytorch as te


print('MUSA available:', torch.musa.is_available())

print('TE Linear:', te.Linear)

PY



只有 import 成功还不够，仍需运行一个实际 MUSA forward/backward，才能确认扩展库和 kernel 正常。

## 5. 从模块到模型训练的完整流程[](https://docs.mthreads.com#5-从模块到模型训练的完整流程)

### 5.1 创建 TE 模块和 MUSA 输入[](https://docs.mthreads.com#51-创建-te-模块和-musa-输入)

`import torch`

import torch_musa

import transformer_engine.pytorch as te

from transformer_engine.common import recipe


model = te.Linear(768, 3072, bias=True).to("musa")

inp = torch.randn(2048, 768, device="musa")



模型参数和输入必须在同一 MUSA 设备。若模块构造时没有自动放置，应显式调用 `.to("musa")`

。

### 5.2 配置 FP8 recipe[](https://docs.mthreads.com#52-配置-fp8-recipe)

`fp8_recipe = recipe.DelayedScaling(`

margin=0,

fp8_format=recipe.Format.E4M3,

)



recipe 参数影响缩放更新和数值范围。修改前应记录 BF16 基线，并用固定输入比较输出、loss 和梯度。

### 5.3 开启 FP8 forward/backward[](https://docs.mthreads.com#53-开启-fp8-forwardbackward)

`with te.fp8_autocast(enabled=True, fp8_recipe=fp8_recipe):`

out = model(inp)


loss = out.sum()

loss.backward()



先运行多次迭代确认没有 NaN/Inf，再扩大 batch、隐藏维度和模型层数。

### 5.4 集成到 MT-Megatron[](https://docs.mthreads.com#54-集成到-mt-megatron)

完整模型训练还需要同步配置：

- 使用 TE 实现的 Transformer 层；
- 模型并行和数据并行；
- FP8 recipe 与模型精度参数；
- checkpoint 中的 FP8 metadata；
- TP overlap、MoE 和重计算等特性；
- MCCL 网络和多机环境。

### 5.5 验证正确性和性能[](https://docs.mthreads.com#55-验证正确性和性能)

建议分别记录 BF16 与 FP8 的：

- 前若干 step 的 loss 和梯度范数；
- 是否出现 NaN/Inf；
- 每 step 时间、tokens/s；
- MUSA 显存和利用率；
- 多卡通信耗时；
- checkpoint 保存与恢复结果。

## 6. API 和概念速查[](https://docs.mthreads.com#6-api-和概念速查)

### 6.1 常用 API[](https://docs.mthreads.com#61-常用-api)

| API | 用途 |
|---|---|
`transformer_engine.pytorch` | PyTorch TE 模块入口 |
`te.Linear` | TE 优化线性层 |
`te.fp8_autocast` | 控制 FP8 作用域 |
`recipe.DelayedScaling` | 配置延迟缩放策略 |
`recipe.Format.E4M3` | 选择 FP8 数据格式 |

实际可用 API 以当前 MT-TE 版本为准，上游新版 Transformer Engine 的参数不一定已同步到 MUSA 分支。

### 6.2 当前文档列出的能力[](https://docs.mthreads.com#62-当前文档列出的能力)

| 功能 | 状态 |
|---|---|
| 逐张量 FP8 | 支持 |
| 分块 FP8 | 支持 |
| TP 重叠（结合 FP8） | 支持 |
| MoE 重计算 | 支持 |
| 零气泡 | 支持 |
| FP8 All-to-All | 以当前版本发布说明为准 |

### 6.3 精度相关概念[](https://docs.mthreads.com#63-精度相关概念)

| 概念 | 含义 |
|---|---|
| amax | 一段时间内用于估计缩放的最大绝对值 |
| scale / scale inverse | FP8 量化与反量化使用的比例 |
| margin | 缩放时预留的数值范围 |
| history | 使用历史 amax 平滑缩放更新 |
| accumulation dtype | GEMM/归约中使用的累加精度 |

## 7. 常见问题定位[](https://docs.mthreads.com#7-常见问题定位)

### 7.1 `import transformer_engine`

失败[](https://docs.mthreads.com#71-import-transformer_engine-失败)

检查安装位置、Python 环境和动态库搜索路径。确认执行测试的 Python 与运行 `install.sh`

时使用的是同一环境。

### 7.2 找不到 MUSA kernel 或动态库[](https://docs.mthreads.com#72-找不到-musa-kernel-或动态库)

检查编译是否真正成功、MUSA SDK 路径、运行时库和 PyTorch ABI。仅存在 Python 包目录不代表 C++/MUSA 扩展已正确生成。

### 7.3 模型和输入设备不一致[](https://docs.mthreads.com#73-模型和输入设备不一致)

错误通常表现为参数在 CPU、输入在 MUSA。显式检查：

`print(next(model.parameters()).device)`

print(inp.device)



### 7.4 FP8 出现 NaN、Inf 或不收敛[](https://docs.mthreads.com#74-fp8-出现-naninf-或不收敛)

先退回 BF16，确认模型、数据和优化器正确；再缩小到单层 FP8，检查 recipe、输入范围、缩放 metadata 和不应使用 FP8 的敏感算子。

### 7.5 单卡正常、多卡失败[](https://docs.mthreads.com#75-单卡正常多卡失败)

检查 MCCL、并行组、TE 与 Megatron 版本，以及 TP overlap/FP8 通信配置。先关闭 overlap 等性能特性验证基础多卡路径。

### 7.6 性能没有提升[](https://docs.mthreads.com#76-性能没有提升)

小矩阵、短序列或频繁同步可能无法发挥 FP8 优势。使用 profiler 区分 GEMM、数据转换、通信和 Python 调度开销，并与同形状 BF16 基线比较。

## 8. 下一步阅读[](https://docs.mthreads.com#8-下一步阅读)

[MT-TransformerEngine MUSA 示例](https://docs.mthreads.com/mt-transformerengine/MT-TransformerEngine)：安装、最小 FP8 示例和功能表；[MT-TransformerEngine 官方仓库](https://github.com/MooreThreads/MT-TransformerEngine)：MUSA 源码和版本信息；[Transformer Engine 官方仓库](https://github.com/NVIDIA/TransformerEngine)：上游设计与示例；[Transformer Engine 用户指南](https://docs.nvidia.com/deeplearning/transformer-engine/user-guide/)：FP8、API 和调试资料；[torch_musa](https://github.com/MooreThreads/torch_musa)：MUSA PyTorch 后端；[MT-Megatron](https://github.com/MooreThreads/MT-MegatronLM)：大模型分布式训练集成。

本文中的 API 和能力以 MT-TransformerEngine 当前版本为准。升级 PyTorch、`torch_musa`

、MUSA SDK、MT-TE 或 MT-Megatron 后，应重新编译并运行最小 forward/backward 与多卡验证。