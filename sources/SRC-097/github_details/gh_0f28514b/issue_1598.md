# [Issue #1598] Why UCX Performance at lower blocksize is too less

source: https://github.com/ai-dynamo/nixl/issues/1598
state: closed | updated: 2026-05-11T16:00:01Z
labels: Network

## 正文

Based on the conversation in 
https://github.com/ai-dynamo/nixl/issues/1021
https://github.com/ai-dynamo/nixl/issues/610
it seems that 0.324 GB/s B/W over RDMA at 4KB is expected, i dont understand if perftest reaches line rate with 4K block 
why cant NIXLBench , 

## 评论 (1)

### brminich · 2026-05-06

The mentioned issues are quite old and there were multiple fixes since then.
Can you pls provide more details on your issue? Any logs, bench numbers, etc?

