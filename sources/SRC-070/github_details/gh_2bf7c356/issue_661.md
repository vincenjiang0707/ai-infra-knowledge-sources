# [Issue #661] [Issue] Would VA signal with RO enabled cause unexpected data correctness problems in DeepEP V2?

source: https://github.com/deepseek-ai/DeepEP/issues/661
state: closed | updated: 2026-07-07T07:59:11Z
labels: 

## 正文

The DeepEP v2 uses GIN VA signal with RO enabled to notify the peers to read tokens from the receive buffer. And the DeepEP document recommends configuring `PCI_ATOMIC_MODE=4` to improve atomic performance, which would use the PCI Atomic, see [pci-atomic-mode](https://github.com/deepseek-ai/DeepEP#pci-atomic-mode). According to the discussion in this issue https://github.com/NVIDIA/nccl/issues/2210, the RO PCI Atomic operation could bypass prior write operations. Maybe there would be a data correctness problem in DeepEP v2 if we configure `PCI_ATOMIC_MODE=4` ?

## 评论 (0)
