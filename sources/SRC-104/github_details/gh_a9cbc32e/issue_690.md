# [Issue #690] how can the L2 arithmetic intensity be less than the HBM AI.

source: https://github.com/ROCm/rocprofiler-compute/issues/690
state: closed | updated: 2025-08-06T18:20:04Z
labels: question, Under Investigation

## 正文

### Describe your question

I have the following roofline:

![Image](https://github.com/user-attachments/assets/c8a09a8b-c7a9-4098-96db-88bc0aa9981e)

This gives me a lower L2 ai than HBM ai. As all loads/stores that go through L2 should go through HBM we should have AI L1 >= AI L2 >= AI HBM right ?

### Additional context

_No response_

## 评论 (4)

### etiennemlb · 2025-04-30

Additionally, how would one interpret the AI L1/L2 dots. Would that mean the farther left we are, the better the caches are used (we do more loads in caches/LDS). If the L1 dot is farther than L2 this means we use the L1, if the L2 is farther than the HBM that means we use it ?

### ppanchad-amd · 2025-04-30

Hi @etiennemlb. Internal ticket has been created to assist with your issue. Thanks!

### systems-assistant[bot] · 2025-08-06

This issue has been migrated to: https://github.com/ROCm/rocm-systems/issues/37

### amd-hsivasun · 2025-08-06

Imported to ROCm/rocm-systems
