# [Issue #219] v4.1.1 failed to load profiling module

source: https://github.com/NVIDIA/DCGM/issues/219
state: open | updated: 2025-06-19T06:32:36Z
labels: 

## 正文

dcgm cannot get profile metrics because failed to load profiling module, plz help

![Image](https://github.com/user-attachments/assets/c43ff7de-782f-4c5c-8742-3c7c46036788)

**System specs**:
Ubuntu: 20.04
CUDA Version: 12.2
Driver Version: 535.161.08
GPU:  L20 * 8

**dcgm**
Version : 4.1.1
Build ID : 11087
Build Date : 2025-02-14
Build Type : RelWithDebInfo
Commit ID : 3965d2e947bcea4c496759177222de6115bd58d0
Branch Name : v4.1.1
CPU Arch : x86_64
Build Platform : Linux 5.15.0-122-generic https://github.com/NVIDIA/DCGM/issues/132-Ubuntu SMP Thu Aug 29 13:45:52 UTC 2024 x86_64
CRC : 84de5921dcda2d8986924b6bcea05213

![Image](https://github.com/user-attachments/assets/3747732a-1781-4362-bcf2-4f33710b7253)

![Image](https://github.com/user-attachments/assets/ea5d02cc-a931-4fec-bdb3-192a59814020)

some debug log

![Image](https://github.com/user-attachments/assets/645078e2-017a-451d-86e7-6a26ba0c9f70)

## 评论 (6)

### HH-66 · 2025-03-24

1. docker images nvidia/dcgm-exporter:4.1.1-4.0.4-ubuntu22.04
2. apt install dcgm-4

Both methods encountered the same error

### bstollenvidia · 2025-05-21

Can you please retry with DCGM 4.2.3? There were several fixes to how we load the profiling module. 

### HH-66 · 2025-06-19

> Can you please retry with DCGM 4.2.3? There were several fixes to how we load the profiling module.

Already tried it, but still have problems

### HH-66 · 2025-06-19

![Image](https://github.com/user-attachments/assets/2827b0dc-56b0-4af5-b926-d3426b6ad7c4)

### HH-66 · 2025-06-19

![Image](https://github.com/user-attachments/assets/fffa5ab4-a311-4662-9858-64eba035492f)

### HH-66 · 2025-06-19

![Image](https://github.com/user-attachments/assets/7a6ed406-d7cd-4c81-bc8c-b852f160def5)
Maybe it's a debug log related to the error
