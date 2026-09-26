# [Issue #88] Weight initialization in custom Conv3d seems different from nn.Conv3d

source: https://github.com/ScalingIntelligence/KernelBench/issues/88
state: open | updated: 2025-12-17T22:25:44Z
labels: 

## 正文

Hi, I noticed that the outputs from my custom Conv3d and PyTorch’s `nn.Conv3d` were very different,
so I added some simple `print()` statements in both constructors (added at level1 question 60)  
to check their weights.

Here’s what I got:

[RefModel] in=3, out=64, kernel=(3, 5, 7), stride=1, padding=0, bias=False
[RefModel Conv3d] weight shape: (64, 3, 3, 5, 7)
mean=-0.000240, std=0.032601, min=-0.056343, max=0.056341

[ModelNew] in=3, out=64, kernel=(3, 5, 7), stride=1, padding=(0, 0, 0), bias=False
[ModelNew Conv3d] weight shape: (64, 3, 3, 5, 7)
mean=0.009656, std=1.001391, min=-4.590487, max=4.220885

The shapes match, but the distributions are very different — `nn.Conv3d` has much smaller weights (std≈0.03),
while the custom one uses `torch.randn()` (std≈1.0).  
This likely causes large output differences even if the kernels are correct.

## 评论 (3)

### yuxuan-z19 · 2025-11-12

@qy-777 maybe try resetting the random seed **before** creating both `RefModel` and `ModelNew` to ensure they start from the same initialization state.

### qy-777 · 2025-11-21

> [@qy-777](https://github.com/qy-777) maybe try resetting the random seed **before** creating both `RefModel` and `ModelNew` to ensure they start from the same initialization state.

This isn’t a situation that can be fixed just by changing the seed. You’ll understand once you try to reproduce the issue yourself.

### jason-yoo-108 · 2025-12-17

I also find this to be a problem with `run_and_check`. Specifically, for problems that use torch modules with parameter initializations such as `nn.Linear` and `nn.Conv3D`, there is no mechanism that ensures Model and ModelNew's corresponding parameters are set identically. Ideally, both models should receive parameters as their inputs. This seems like a serious problem.

Example Problem with Issue (only one of the matmul matrix to nn.Linear is explicitly specified): https://github.com/ScalingIntelligence/KernelBench/blob/main/KernelBench/level2/9_Matmul_Subtract_Multiply_ReLU.py

Example Problem without Issue (both matmul matrices are explicitly specified): https://github.com/ScalingIntelligence/KernelBench/blob/main/KernelBench/level1/1_Square_matrix_multiplication_.py


