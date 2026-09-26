# [Issue #62] More changes in v0.1 than mentioned in the changelog?

source: https://github.com/ScalingIntelligence/KernelBench/issues/62
state: closed | updated: 2025-10-30T06:34:06Z
labels: 

## 正文

In the changelog found at https://scalingintelligence.stanford.edu/blogs/kernelbenchv01/ it doesn't mention that the names of problems have changed or the code therein (aside from scaling dimensions).

Meanwhile, I can no longer find the following problems that likely previously existed:
```
❌ Level 1 - Missing Problems (2 total):
    1. 50_Product_reduction_over_a_dimension (Problem #50)
    2. 97_CosineSimilarityLoss (Problem #97)

❌ Level 2 - Missing Problems (5 total):
    1. 27_Conv3d_HardSwish_ReLU_Softmax_Mean (Problem #27)
    2. 41_Gemm_BatchNorm_GELU_GroupNorm_Mean_ReLU (Problem #41)
    3. 45_Gemm_Sigmoid_Sum_LogSumExp (Problem #45)
    4. 58_ConvTranspose3d_LogSumExp_HardSwish_Subtract_Clamp_Max (Problem #58)
    5. 66_Matmul_Dropout_Mean_Softmax (Problem #66)

❌ Level 3 - Missing Problems (5 total):
    1. 35_LTSM (Problem #35)
    2. 36_LTSMHn (Problem #36)
    3. 37_LTSMCn (Problem #37)
    4. 38_LTSMBidirectional (Problem #38)
    5. 41_GRUBirectional (Problem #41)

```

It seems that the two in level 1 have been changed entirely, the five problems in level two changed but more slightly and in level three code was changed in implementation logic but it's still the same function semantically.

## 评论 (2)

### simonguozirui · 2025-10-03

@AffectionateCurry @anneouyang @nataliakokoromyti 

### AffectionateCurry · 2025-10-30

Yes we did change those problems due to issues that were pointed out in the blog. We'll make sure to have a changelog in the problem directory in the future to be clear on which problems have been removed and changed!
