# [Issue #2226] [Question]: [GIN] GPI vs GDAKI: who selects the QP, and what NIC support does GPI need?

source: https://github.com/NVIDIA/nccl/issues/2226
state: closed | updated: 2026-09-16T20:04:18Z
labels: question

## 正文

### Question

Hi,  dear NCCL developers，

We're reading the GIN code in NCCL 2.30.7 and want to confirm our understanding of
the GPI vs GDAKI backends.

What we see:
- GDAKI: device context holds a verbs QP (doca_gpu_dev_verbs_qp* gdqp). The GPU
  picks the per-peer QP and posts an mlx5 WQE itself.
- GPI: device context (gpi_gpu_channel_t) has no QP — just an on-NIC queue
  (gpu_memic_ptr). The GPU posts a 64B "GFD" via st.b128 MMIO, and the destination
  is just a field in the GFD (dst.pe), not a chosen QP. There's also no host-side
  gpi/*.cc, which makes it look like the NIC firmware consumes the GFD.

Our guess: in GPI the GPU only writes an abstract op (with dst.pe) into an on-NIC
queue, and the NIC firmware selects the QP and generates the actual RDMA — i.e. GPI
offloads QP selection + WQE generation to the NIC, while GDAKI keeps it on the GPU.

Questions:
1. Is that understanding correct? Does the NIC (not the GPU/host) pick the QP in GPI?
2. Which NICs support GPI (specific ConnectX/BlueField generations)?
3. Does GPI require new hardware, or is it firmware-only on existing NICs?

Thanks!


## 评论 (3)

### xiaofanl-nvidia · 2026-06-22

++ @pakmarkthub @khamidouche for this question. 

### pakmarkthub · 2026-06-26

@QizhouZhang97 

> 1. Is that understanding correct? Does the NIC (not the GPU/host) pick the QP in GPI?

GPI uses the NIC engine to manage the control path. You can think of it similar to CPU Proxy but it runs on the NIC engine instead. Note that the implementation is not the same.


> 2. Which NICs support GPI (specific ConnectX/BlueField generations)?
> 3. Does GPI require new hardware, or is it firmware-only on existing NICs?

You need Spectrum-X.

### QizhouZhang97 · 2026-06-29

thanks for your comments
