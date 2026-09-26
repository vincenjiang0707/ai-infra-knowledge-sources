# [Issue #1315] Does RCCL have the plan to support whole NCCL MNNVL feature in the next release? and when will RCCL update to NCCL v2.21.5?

source: https://github.com/ROCm/rccl/issues/1315
state: closed | updated: 2024-12-09T01:01:24Z
labels: Under Investigation

## 正文

Hi Dear developer,
I found the latest RCCL 2.20.5 for ROCm 6.2.0 has updated to NCCL 2.20.5, which including MNNVL feature in NCCL, while NCCL improve the MNNVL feature in v2.21.5, for example:
"Exchange XML between peers in the same NVLS clique and fuse XMLs before creating the topology graph."
Which is necessary for MNNVL.

Does RCCL have the plan to support whole NCCL MNNVL feature in the next release? and when will RCCL update to NCCL v2.21.5?
Thank you.



## 评论 (4)

### ppanchad-amd · 2024-10-28

Hi @shanleo2024. Internal ticket has been created to assist with your question. Thanks!

### gilbertlee-amd · 2024-10-29

Although the code path for Multi-Node NVLink is part of RCCL, this is a hardware feature that we do not support on any of our current AMD hardware.

### corey-derochie-amd · 2024-12-06

I can also answer your second question, @shanleo2024 . RCCL has been updated to v2.21.5 in the latest ROCm 6.3.0.

### shanleo2024 · 2024-12-09

> I can also answer your second question, @shanleo2024 . RCCL has been updated to v2.21.5 in the latest ROCm 6.3.0.

Thanks a lot.
