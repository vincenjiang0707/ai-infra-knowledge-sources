# [Issue #1] Number of heads

source: https://github.com/FasterDecoding/Medusa/issues/1
state: closed | updated: 2023-12-15T06:49:05Z
labels: 

## 正文

Hi thanks for releasing this. 

Any findings/intuition around the new hyperparameters?
For example how many heads to use?

Thanks! 

## 评论 (3)

### leeyeehoo · 2023-09-11

Hi Anton,

We trained the additional 5 heads with frozen LLM.

 The intuition of each head's top-k choices can be found in the [appendix](https://sites.google.com/view/medusa-llm#h.2yq1gf32dw1x). We observed that when the number of additional tokens exceeds 64, there's a significant reduction in speed, possibly due to the [warp size](https://docs.nvidia.com/cuda/ampere-tuning-guide/index.html#occupancy) of the A100, based on our findings. Since the search space is relatively small, either brutal or grid search can easily be implemented to find a good-choice combination.

You can refer to the [notebook](https://github.com/FasterDecoding/Medusa/blob/main/notebooks/medusa_configuration_explained.ipynb) for a detailed explanation of how those heads are used in the tree attention. 
 


### kmn1024 · 2023-12-15

How was the plot in https://sites.google.com/view/medusa-llm#h.n6cj4elv4i5f generated? Asking because I would like to test this idea on cheap hardware (Mali GPUs on MLC, with warp size of 16 https://developer.arm.com/documentation/102811/0106/Shader-core-data-path), and am not sure where to start.

Given warp size 16, would it be reasonable to try mc_sim_7b_63, but just take the first 16 rows? So just 3 heads, corresponding to:

```
>>> medusa_position_ids[0:16]
tensor([0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2])

```

?

### leeyeehoo · 2023-12-15

Hi, can you try [this](https://github.com/FasterDecoding/Medusa/tree/v1.0-prerelease/medusa/eval) first? You can generate the sparse tree and customize it. I am not sure if other factors affect the speed/introduce the overhead. The plot is based on the randomly generated trees (the blue dots). So you don't need to implement so many runs. Just see if tree size effect speeds or not should be fine I guess?
