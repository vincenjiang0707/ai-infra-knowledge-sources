# [Issue #543] GPUs cluster with a distributed memory

source: https://github.com/ROCm/rccl/issues/543
state: closed | updated: 2022-04-28T16:08:35Z
labels: 

## 正文

Hello, dear colleagues!

I have 2 nodes with a distributed memory. GPUs 0,1,2,3 are installed on _Node 0_ and are connected by Infiniti Fabric. _Node 1_ has 4 more GPUs installed, which are also interconnected by Infiniti Fabric. Thus, nodes 0 and 1 have a distributed memory system, but within a separate _Node_ GPUs can interact via Infinity Fabric.   
- If I use a collective P2P for N0:GPU X -> N1:GPU Y, the exchange be done via sockets?
- If I use a collective AllGather, will Infinity Fabric be used within GPU:0,1,2,3 on Node 0 (and similarly within GPUs on Node 1), or will all transfers (_N0_:GPUx1-_N0_:GPUx2 and _N0_:GPUy1-_N1_:GPUy2 be done via sockets)

Thanks any way)!

## 评论 (2)

### gilbertlee-amd · 2022-04-28

1) Yes.  Unless you have Infiniband and appropriate software stack installed
2) Yes - Ranks will communicate with each other on the fastest detected transport - Likely Infinity Fabric within the node.

### vasslavich · 2022-04-28

@gilbertlee-amd , thank you again!)
