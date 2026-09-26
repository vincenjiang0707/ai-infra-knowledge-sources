# [Issue #352] Performance drop from v2.22 to v2.25 on 2 nodes due to algo RING

source: https://github.com/NVIDIA/nccl-tests/issues/352
state: closed | updated: 2025-10-23T16:33:02Z
labels: 

## 正文

Hello, we are running on a HPC cluster nccl-tests of allreduce, and we observe a performance drop for 2-node runs from circa 50 GB/s to 7 GB/s comparing nccl v2.22 to nccl 2.25, 2.26 and 2.27 (algorithmic bandwidth at saturation). By analyzing the NCCL_DEBUG=INFO, we understood that the two runs differ from the algorithm used: ring with v2.25+ and tree with v2.22. Ring uses only one port to communicate among nodes while tree uses all fours (confirmed by nsys profile --nic-metrics=true).

To recover performance of v2.22 in the latest installations, we tried forcing the tree algorithm with NCCL_ALGO, but the run crashes. This warning appears

`[2025-10-23 10:26:31] lrdn2146:1399931:1399978 [3] graph/search.cc:1127 NCCL WARN Could not find a path for pattern 1, falling back to simple order
`
and then
`[2025-10-23 10:26:31] lrdn2151:2678763:2678858 [0] graph/topo.h:234 NCCL WARN Could not find NET with id 0
`
Could you please suggest how to debug this issue? 


## 评论 (2)

### bellenlau · 2025-10-23

Another bit of information: nccl/2.18 generates 8 channels:
```
lrdn0020:2080194:2080296 [0] NCCL INFO Channel 00/08 :    0   1   2   3   4   5   6   7
lrdn0020:2080194:2080296 [0] NCCL INFO Channel 01/08 :    0   3   2   5   4   7   6   1
lrdn0020:2080194:2080296 [0] NCCL INFO Channel 02/08 :    0   3   6   5   4   7   2   1
lrdn0020:2080194:2080296 [0] NCCL INFO Channel 03/08 :    0   7   6   5   4   3   2   1
lrdn0020:2080194:2080296 [0] NCCL INFO Channel 04/08 :    0   1   2   3   4   5   6   7
lrdn0020:2080194:2080296 [0] NCCL INFO Channel 05/08 :    0   3   2   5   4   7   6   1
lrdn0020:2080194:2080296 [0] NCCL INFO Channel 06/08 :    0   3   6   5   4   7   2   1
lrdn0020:2080194:2080296 [0] NCCL INFO Channel 07/08 :    0   7   6   5   4   3   2   1
```
while nccl/2.26 only two
```
lrdn2785:785563:785668 [0] NCCL INFO Channel 00/02 : 0 1 2 3 4 5 6 7
lrdn2785:785563:785668 [0] NCCL INFO Channel 01/02 : 0 1 2 3 4 5 6 7
```

### AddyLaddy · 2025-10-23

These are NCCL library issues and so should be logged against the NCCL github project: [NCCL](https://github.com/NVIDIA/nccl)
