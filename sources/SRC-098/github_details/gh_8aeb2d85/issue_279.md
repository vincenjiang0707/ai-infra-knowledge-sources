# [Issue #279] Is it suitable to calculate busBw in AllReduceGetBw for all of the algos?

source: https://github.com/NVIDIA/nccl-tests/issues/279
state: open | updated: 2025-06-16T02:08:51Z
labels: 

## 正文

Hi Dear developer,
In AllReduceGetBw, the busBw = baseBw * ((double)(2*(nranks - 1)))/((double)nranks)

I think it is good for ring algorithm, but for the other algorithm, such as Tree/NVLS, does is suitable to use (2*(nranks - 1)))/((double)nranks?
As from the source code of NCCL, the ratio of converting bus BW to algorithm BW is different.

```
        // Convert bus BW to algorithm BW
        float ratio;
        if (a == NCCL_ALGO_RING) ratio = (1.0 * nRanks) / nsteps;
        else if (a == NCCL_ALGO_NVLS) ratio = 5.0/6.0;
        else if (a == NCCL_ALGO_NVLS_TREE) ratio = .70 * nNodes / (2*(nNodes-1));
        else ratio = .5;
        comm->bandwidths[coll][a][p] = busBw * ratio;
```

Thank you.

## 评论 (1)

### cychenbuaa · 2025-06-16

https://github.com/NVIDIA/nccl-tests/issues/312

We have the same question.😄
