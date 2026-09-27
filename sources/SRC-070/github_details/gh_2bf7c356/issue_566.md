# [Issue #566] Feature request: Enable multi-NIC RDMA support for GPU = 1:2 (CX8) systems in Hybrid-EP / GIN

source: https://github.com/deepseek-ai/DeepEP/issues/566
state: open | updated: 2026-04-09T09:19:43Z
labels: 

## 正文

On the hybrid-ep branch, on B300 systems equipped with CX8 NICs, where each GPU is connected to two RDMA NICs, inter-node communication during training appears to utilize only one NIC per GPU. As a result, the effective RDMA bandwidth per GPU does not scale with the available NIC resources, even though the hardware topology supports concurrent usage of multiple NICs. This behavior is consistently observed on B300 + CX8 platforms across training runs.

## 评论 (3)

### Autumn1998 · 2026-01-30

Yes, this is a known issue for now. We are working on switching to a more mature backend instead of relying on the low-level API, and we will then try to support this case.

### Brook017 · 2026-04-02


@Autumn1998 Does it mean underlying doca api will no longer be used?


### Autumn1998 · 2026-04-09

We will still fix bugs, but there will be no new features.
