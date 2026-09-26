# [Issue #2310] [RFE]: Add active-standby paths for fused IB NICs

source: https://github.com/NVIDIA/nccl/issues/2310
state: open | updated: 2026-08-09T23:29:02Z
labels: 

## 正文

### Goal

Add an opt-in active-standby data path for fused Net IB devices. Normal payload and CTS traffic should use the topology-nearest primary NIC, while a second connected NIC remains ready for failover.

### Problem statement and test evidence

The current fused-device data path treats participating QPs as equivalent and splits each request approximately evenly across them. That assumption does not hold when one GPU reaches one NIC through PIX and another through PHB.

H100 measurements show the following per-NIC bandwidth and congestion behavior:

| Configuration | Per-NIC bandwidth | PFC/CNP |
| --- | ---: | --- |
| One PIX NIC | 400 Gbps | None |
| One PHB NIC | 234 Gbps | None |
| Two PHB NICs | 117 Gbps | A small amount of PFC |
| One PIX and one PHB NIC | 70 Gbps | Heavy PFC/CNP on the PIX NIC |

Two PHB NICs at approximately 117 Gbps each provide roughly the same aggregate bandwidth as one PHB NIC at 234 Gbps, indicating that the PHB paths likely share upstream bandwidth. More importantly, combining PIX and PHB reduces each NIC to approximately 70 Gbps and produces heavy PFC/CNP on the otherwise faster PIX NIC.

The result indicates that equal striping across heterogeneous DMA and PCIe paths creates resource contention and backpressure rather than aggregating their nominal bandwidth. The slower path delays request completion, while concurrent access to the same GPU can contend for PCIe, host-bridge, GPU DMA, and network buffering resources.

### Who benefits

Users running NCCL over fused IB devices on heterogeneous GPU-to-NIC PCIe topologies, especially systems where one NIC is connected through PIX and another through PHB.

### Target infrastructure

This request targets NCCL Net IB P2P transport with NIC Fusion, IB resiliency port failover, and port recovery. It does not introduce a public NCCL API.

### Requested behavior

- Configure unordered redundant HCA pairs.
- Expose two topology-directed virtual NIC directions so NCCL selects the nearest primary for each GPU.
- Keep primary and standby data QPs connected, but send normal payload and CTS traffic only on the primary.
- Probe standby data QPs in both directions without affecting user request completion accounting.
- Map failed primary QPs to the same lane on the standby and reuse completion probing for selective retransmission.
- Automatically return to the topology-selected primary after successful port recovery.
- Preserve existing Active-Active behavior when the feature is not configured.

The initial scope handles one failed device at a time. Standby health probing is driven by primary payload or CTS progress.

### Workflow impact

This avoids concurrent traffic over heterogeneous PIX and PHB paths in the healthy state while preserving transparent failover. It also prevents standby resources from inflating the topology bandwidth reported to NCCL graph search.

### Priority

Medium. The feature targets deployments where fused NIC resiliency is required but Active-Active traffic across asymmetric PCIe paths causes a measured performance regression and congestion backpressure.

### Validation

The implementation has been validated with clean builds on two NCCL nodes, non-destructive active-standby functional cases, dual-GPU PIX/PHB topology direction selection, pair-order equivalence, and real IB port down/up failover and recovery.

Implementation: #2309


## 评论 (1)

### xiaofanl-nvidia · 2026-08-09

++ @sjeaugey @thomasgillis to take a look and see if this is interesting use case. 
