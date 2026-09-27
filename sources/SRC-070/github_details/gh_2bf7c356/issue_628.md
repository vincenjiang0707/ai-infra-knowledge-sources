# [Issue #628] ElasticBuffer asserts NCCL_GIN_TYPE_NONE on host with MLNX_OFED 24.10 (libmlx5 < MLX5_1.25)

source: https://github.com/deepseek-ai/DeepEP/issues/628
state: open | updated: 2026-07-09T18:06:51Z
labels: 

## 正文

 DeepEP version: 2.0.0 (commit <你那 commit>)
  NCCL: 2.30.4+cuda13.2
  GPU: B300 SXM6, driver 590.48.01
  NIC: ConnectX-7, fw_ver 40.46.5500
  Host OFED: MLNX_OFED_LINUX-24.10-3.2.5.0 (libmlx5 max symbol MLX5_1.17)

  NCCL_DEBUG=INFO shows:
    dlvsym failed on mlx5dv_reg_dmabuf_mr ... version MLX5_1.25
    dlvsym failed on mlx5dv_get_data_direct_sysfs_path ... version MLX5_1.25
    Assigned GIN plugin GIN_IB_GDAKI to comm
    GPU Direct RDMA Enabled for HCA 0..7
  但 ncclCommQueryProperties() 返回 props.ginType = NCCL_GIN_TYPE_NONE,
  ElasticBuffer ctor 在 csrc/kernels/backend/nccl.cu:87 断言失败。

  Tried (all fail same):
  - allow_hybrid_mode={True, False}
  - NCCL_GIN_ENABLE=1
  - intra-node 8-rank NVLink-only test (no inter-node fabric involved)

  Question:
  1. Is upgrading host MLNX_OFED to 25.x the only path? Or is there an env / NCCL flag to skip the MLX5_1.25 dmabuf
  path?
  2. Could README mention minimum OFED version explicitly?

## 评论 (2)

### jiangzhuti · 2026-05-25

试试 export NCCL_IB_MERGE_NICS=0

### Functionhx · 2026-07-09

I ran into this too. Instead of asserting, I made the GIN check conditional: if GIN isn't available, it prints a debug message and falls back to non-GIN path. Also added ncclAllReduce consensus so heterogeneous ranks don't mismatch. Want a PR?
