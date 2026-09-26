# [Issue #971] Some issue when using the RCCL_NChannels

source: https://github.com/ROCm/rccl/issues/971
state: closed | updated: 2024-02-01T09:11:44Z
labels: 

## 正文

I found there is something wrong when using RCCL_NChannels.
For example, the bw from my setup is 24, if I set the RCCL_NChannels to 6, finally the total bw for the channel displayed by NCCL_GRAPH_DUMP_FILE will bigger than 24, I think there are something wrong with this EV.

```
  int savedChannels = graph->nChannels;
  //ADD
...
    graph->bwIntra /= DIVUP(nc, savedChannels);
    graph->bwInter /= DIVUP(nc, savedChannels);
```

I have modified this code in function ncclTopoCompute() and test the result, it will be OK now.


## 评论 (1)

### shanleo2024 · 2024-02-01

There is no such issue on the RCCL of github, it is just an issue from the private code. so close this issue.
