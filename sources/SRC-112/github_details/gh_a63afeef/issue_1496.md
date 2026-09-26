# [Issue #1496] [infra] h200-nb_0 / h200-nb_1: enroot /mnt/image-storage full — can't unpack TRT-LLM v1.3.0rc14 image / [infra] h200-nb_0 / h200-nb_1：enroot /mnt/image-storage 已满，无法解压 TRT-LLM v1.3.0rc14 镜像

source: https://github.com/SemiAnalysisAI/InferenceX/issues/1496
state: open | updated: 2026-07-04T05:17:45Z
labels: 

## 正文

## Summary

Two H200 self-hosted runners — **`h200-nb_0`** and **`h200-nb_1`** — are unable to unpack newer TensorRT-LLM container images because their `/mnt/image-storage/enroot/data/` partition is full. Every sweep job that lands on either runner fails identically:

```
enroot-mount: failed to create directory:
  /mnt/image-storage/enroot/data/pyxis_nvcr.io_nvidia_tensorrt-llm_release_1.3.0rc14-gharunner/var/run:
  No space left on device
```

…and `pyxis: failed to create container filesystem` during the squashfs extraction step. The benchmark script never runs.

It's been temporarily worked around by removing the `h200` SLURM partition tag from these two nodes — they currently can't pick up jobs at all — but they should be put back into service once the disk is freed.

## How we got here

The recently-tagged `nvcr.io/nvidia/tensorrt-llm/release:v1.3.0rc14` image is significantly larger than `v1.1.0rc2.post2` (it bundles Python 3.12 + new CUDA libs). Old enroot caches haven't been pruned, so `/mnt/image-storage` filled up trying to extract the new image.

Confirmed on these PRs (where every failure landed on `h200-nb_*` and every success landed on `h200-dgxc-slurm_*` or `h200-cw_01`):

- [#1491](https://github.com/SemiAnalysisAI/InferenceX/pull/1491) — `gptoss-fp4-h200-trt` v1.3.0rc11 → v1.3.0rc14 (11/12 failures = disk; 1 = stale port-8888 leak on `h200-cw_01`)
- [#1487](https://github.com/SemiAnalysisAI/InferenceX/pull/1487) — `dsr1-fp8-h200-trt` (+mtp) v1.1.0rc2.post2 → v1.3.0rc14 (12/12 failures = disk)

Failed CI runs:

- https://github.com/SemiAnalysisAI/InferenceX/actions/runs/26016892349
- https://github.com/SemiAnalysisAI/InferenceX/actions/runs/26016868638

## Suggested SRE fix

Any of:

1. **Prune the enroot image cache** on both nodes:
   ```bash
   ssh root@h200-nb_0  # and h200-nb_1
   enroot list  # see what's still there
   enroot remove --force '*'  # nuclear option, drops everything
   # OR: rm -rf /mnt/image-storage/enroot/data/<stale-pyxis-dirs>
   df -h /mnt/image-storage
   ```
2. **Expand `/mnt/image-storage`** on these nodes — they're chronically near-full since the v1.1 → v1.3 image sizes diverged.
3. Add a periodic cron / systemd-timer that prunes pyxis directories older than ~7d (eg. `find /mnt/image-storage/enroot/data -maxdepth 1 -type d -mtime +7 -exec rm -rf {} +`).

Once any of those is done, re-add the `h200` SLURM partition tag and the affected PRs can be re-swept.

## Bonus issue on `h200-cw_01`

A separate one-off failure on `h200-cw_01` during the same #1491 sweep was an `Address already in use` on port 8888 — left over from a previous `trtllm-serve` that didn't shut down cleanly. Worth a `kill` pass on that node too.

cc @sre / @platform

## 中文说明
两个 H200 自托管运行器（`h200-nb_0` 和 `h200-nb_1`）的 `/mnt/image-storage/enroot/data/` 分区已满，无法解压较新的 TensorRT-LLM v1.3.0rc14 容器镜像（该镜像比 v1.1 显著增大）。所有落在这两个节点上的扫描作业都因磁盘空间不足而失败。临时变通方案是移除这两个节点的 `h200` SLURM 分区标签。建议清理 enroot 镜像缓存、扩展存储分区或添加定期清理旧缓存的定时任务，修复后恢复节点服务。


## 评论 (1)

### functionstackx · 2026-05-18

### Fixed

SSH'd in via the new `nebius-h200` alias (`204.12.170.105`) — both worker-0 and worker-1 had `/mnt/image-storage` (915G partition) nearly full (worker-0: 100%, worker-1: 95%) from stale pyxis caches dating back to March/April. Cleaned pyxis dirs older than 7d:

| Worker | Before | After |
|---|---|---|
| `worker-0` | `915G/915G  100%` | `373G/915G  41%` (~542G freed) |
| `worker-1` | `865G/915G  95%` | `469G/915G  52%` (~446G freed) |

shiyi's active job on `worker-0` was untouched (its image cache is <7d).

Re-added the `h200` label to both runners via the GHA API:
- `h200-nb_0`: `self-hosted,Linux,X64,h200,slurm,h200-nb_0,h200-p1`
- `h200-nb_1`: `self-hosted,Linux,X64,h200,slurm,h200-nb_1,h200-p1`

They're back in rotation. Will let this run for a sweep cycle to confirm, then close.

### Suggested durable fix for SRE

To prevent this recurring as image sizes grow (v1.3.0rc14 → v1.4+ will be even larger), add a periodic cleanup. Either:
```bash
# weekly cron / systemd-timer on each h200-nb worker
0 4 * * 0  find /mnt/image-storage/enroot/data -maxdepth 1 -type d -mtime +7 -name 'pyxis_*' -exec rm -rf {} +
```
…or expand the `/mnt/image-storage` partition. The current 915G fills with ~25–30 pyxis caches at 20–55G each (image-version-dependent).
