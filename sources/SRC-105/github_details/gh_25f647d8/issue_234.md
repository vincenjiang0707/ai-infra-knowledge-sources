# [Issue #234] Do GeForce RTX 4090/4090D & 5090 Support DCGM Profiling Metrics Such as DCGM_FI_PROF_NVLINK_RX_BYTES, DCGM_FI_PROF_NVLINK_TX_BYTES, DCGM_FI_PROF_PIPE_TENSOR_ACTIVE, DCGM_FI_PROF_PCIE_RX_BYTES, and DCGM_FI_PROF_PCIE_TX_BYTES?

source: https://github.com/NVIDIA/DCGM/issues/234
state: open | updated: 2025-11-12T06:27:35Z
labels: 

## 正文

In the compute nodes where DCGM has been given privileged access, there is no information available for the five metrics: 
DCGM_FI_PROF_NVLINK_RX_BYTES
DCGM_FI_PROF_NVLINK_TX_BYTES
DCGM_FI_PROF_PIPE_TENSOR_ACTIVE
DCGM_FI_PROF_PCIE_RX_BYTES
 DCGM_FI_PROF_PCIE_TX_BYTES. 
Can someone confirm if these five metrics are supported?

## 评论 (4)

### bstollenvidia · 2025-06-09

Profiling metrics on GeForce GPUs are supported starting with Blackwell GPUs, as in GeForce 50xx. 

### marquis-wang · 2025-09-15

> In the compute nodes where DCGM has been given privileged access, there is no information available for the five metrics: DCGM_FI_PROF_NVLINK_RX_BYTES DCGM_FI_PROF_NVLINK_TX_BYTES DCGM_FI_PROF_PIPE_TENSOR_ACTIVE DCGM_FI_PROF_PCIE_RX_BYTES DCGM_FI_PROF_PCIE_TX_BYTES. Can someone confirm if these five metrics are supported?

Metrics supported by GeForce 50xx on driver version 580 and above, GeForce 40xx still unsupported.

DCGM_FI_PROF_PIPE_TENSOR_ACTIVE
DCGM_FI_PROF_PCIE_RX_BYTES
DCGM_FI_PROF_PCIE_TX_BYTES

### adababys · 2025-11-06

> > In the compute nodes where DCGM has been given privileged access, there is no information available for the five metrics: DCGM_FI_PROF_NVLINK_RX_BYTES DCGM_FI_PROF_NVLINK_TX_BYTES DCGM_FI_PROF_PIPE_TENSOR_ACTIVE DCGM_FI_PROF_PCIE_RX_BYTES DCGM_FI_PROF_PCIE_TX_BYTES. Can someone confirm if these five metrics are supported?
> 
> Metrics supported by GeForce 50xx on driver version 580 and above, GeForce 40xx still unsupported.
> 
> DCGM_FI_PROF_PIPE_TENSOR_ACTIVE DCGM_FI_PROF_PCIE_RX_BYTES DCGM_FI_PROF_PCIE_TX_BYTES

 Our cluster is equipped with NVIDIA GeForce RTX 5090 GPUs and uses driver version 580.95.05, yet the following DCGM profiling metrics are still unavailable:

DCGM_FI_PROF_PIPE_TENSOR_ACTIVE
DCGM_FI_PROF_PCIE_RX_BYTES
DCGM_FI_PROF_PCIE_TX_BYTES
Why is that?

### adababys · 2025-11-06

> Profiling metrics on GeForce GPUs are supported starting with Blackwell GPUs, as in GeForce 50xx.

  GeForce RTX 5090 GPUs and uses driver version 580.95.05,  dcgm  4.2.3 support DCGM_FI_PROF_PIPE_TENSOR_ACTIVE, DCGM_FI_PROF_PCIE_RX_BYTES, and DCGM_FI_PROF_PCIE_TX_BYTES .  4090 none 

both 4090 5090 has no DCGM_FI_PROF_NVLINK_RX_BYTES, DCGM_FI_PROF_NVLINK_TX_BYTES,
