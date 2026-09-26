# [Issue #1390] [Feature]: Generating a new topology file

source: https://github.com/ROCm/rccl/issues/1390
state: closed | updated: 2024-10-29T16:06:34Z
labels: 

## 正文

### Suggestion Description

I was looking at the `topo_expl` tool and I see a reference to [topo_8p_942.xml](https://github.com/ROCm/rccl/blob/develop/tools/topo_expl/topo_expl.cpp#L162C8-L162C23). But strangely enough, I can't seem to find this file (or any other related 942 variants) in the [models directory](https://github.com/ROCm/rccl/tree/develop/tools/topo_expl/models).

Where can I get this file/topology from? Or better yet, is there a way to auto-generate a topology file for my system?

### Operating System

_No response_

### GPU

_No response_

### ROCm Component

_No response_

## 评论 (1)

### gilbertlee-amd · 2024-10-29

Hi - you can dump the topology file for your own system by setting the path to a file using the environment variable NCCL_TOPO_DUMP_FILE

