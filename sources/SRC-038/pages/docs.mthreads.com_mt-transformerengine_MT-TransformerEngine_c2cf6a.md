source: https://docs.mthreads.com/mt-transformerengine/MT-TransformerEngine

# MT-TransformerEngine MUSA示例

MT-TransformerEngine 是由摩尔线程 AI-Infra 团队开发的高性能深度学习框架。该框架基于 [TransformerEngine](https://github.com/NVIDIA/TransformerEngine) 和 [torch_musa](https://github.com/MooreThreads/torch_musa) 构建，为摩尔线程 GPU 提供了优化的 FP8 训练支持。

与 [MT-Megatron](https://github.com/MooreThreads/MT-MegatronLM/tree/main) 集成后，MT-TransformerEngine 可以实现：

- 在摩尔线程 GPU 上使用 FP8 训练方案。我们通过
`transformer_engine/musa/pytorch/fp8.py`

中的**MTFP8BlockScalingRecipeState**，提供了与 DeepSeek-V3 相同的 FP8 训练策略。 - 支持跨由数千张 GPU 组成的集群进行大模型训练。有关大模型训练的详细介绍，请参考
[MT-Megatron](https://github.com/MooreThreads/MT-MegatronLM/tree/main)。

## 安装[](https://docs.mthreads.com#安装)

通过提供的安装脚本安装 MT-TransformerEngine：

`bash install.sh`



该脚本会编译以下目录中的 MUSA 内核和 C++ 源文件：

`transformer_engine/musa/common`

transformer_engine/musa/pytorch/csrc



## MUSA 示例[](https://docs.mthreads.com#musa-示例)

要在摩尔线程 GPU 上执行兼容 CUDA 的训练，请按以下步骤操作：

- 导入
`torch`

和[torch_musa](https://github.com/MooreThreads/torch_musa)。 - 将 CUDA 设备字符串替换为
`musa`

。

`import torch`

import torch_musa

import transformer_engine.pytorch as te

from transformer_engine.common import recipe


# 设置维度。

in_features = 768

out_features = 3072

hidden_size = 2048


# 初始化模型和输入。

model = te.Linear(in_features, out_features, bias=True)

inp = torch.randn(hidden_size, in_features, device="musa")


# 创建 FP8 训练方案。注意：所有输入参数都是可选的。

fp8_recipe = recipe.DelayedScaling(margin=0, fp8_format=recipe.Format.E4M3)


# 为前向传播启用自动混合精度。

with te.fp8_autocast(enabled=True, fp8_recipe=fp8_recipe):

out = model(inp)


loss = out.sum()

loss.backward()



## 功能特性[](https://docs.mthreads.com#功能特性)

| 功能特性 | 可用性 |
|---|---|
| 逐张量 FP8 | ✔ |
| 分块 FP8 | ✔ |
| TP 重叠（结合 FP8） | ✔ |
| MoE 重计算 | ✔ |
| 零气泡 | ✔ |
| FP8 All-to-All | 即将推出 |

## 社区[](https://docs.mthreads.com#社区)

### 问题反馈[](https://docs.mthreads.com#问题反馈)

如果在使用 MT-TE 进行大模型训练时遇到任何问题，请提交 Issue。

### 贡献[](https://docs.mthreads.com#贡献)

**欢迎以任何形式贡献代码和文档！**