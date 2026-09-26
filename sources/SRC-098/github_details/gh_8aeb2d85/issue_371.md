# [Issue #371] h100 only has 70GB on bus

source: https://github.com/NVIDIA/nccl-tests/issues/371
state: open | updated: 2026-02-07T18:30:51Z
labels: 

## 正文

log is attached, any adviced?

I am testing on 2*8 h100 machines, DOCA-HOST installed, with 400GB * 8 IB.

[log.txt](https://github.com/user-attachments/files/25144012/log.txt)

## 评论 (1)

### AddyLaddy · 2026-02-07

This is probably more a question for the main NCCL library project.

Anyway, I can't see anything wrong in your logs. 
`NCCL_COLLNET_ENABLE=1` is only required if you have an IB SHARP enabled network, but I can't see it would affect this test.

I'd measure what you achieve with each NIC/HCA individually and then test that the BW increases as you combine them.

But my suspicion would be that you have ACS still enabled on these nodes.


