# [Issue #374] Where is the test reading these values from? This is from running `ib_send_lat` and `ib_read_bw`, should I be worried?

source: https://github.com/NVIDIA/nccl-tests/issues/374
state: closed | updated: 2026-03-24T00:58:16Z
labels: 

## 正文

Where is the test reading these values from? This is from running `ib_send_lat` and `ib_read_bw`, should I be worried?
`Conflicting CPU frequency values detected: 3645.037000 != 4299.667000. CPU Frequency is not max`

_Originally posted by @sushma-4 in https://github.com/linux-rdma/perftest/issues/372_

## 评论 (2)

### AddyLaddy · 2026-03-23

I don't see how this is related to nccl-tests?
You should ask on a `perftests` related group/repo. Maybe [perftest](https://github.com/linux-rdma/perftest) ?

I normally just ignore those messages with `--CPU-freq`



### sushma-4 · 2026-03-24

I have it opened in `perftest` - https://github.com/linux-rdma/perftest/issues/372
Why did you open it here...? @evelyn2908 are you an AI agent?
