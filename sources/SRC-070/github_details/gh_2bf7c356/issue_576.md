# [Issue #576] [Performance] B200 underperforms H100 in DeepEP Low-Latency Mode

source: https://github.com/deepseek-ai/DeepEP/issues/576
state: open | updated: 2026-04-07T13:46:33Z
labels: 

## 正文

Hi DeepEP Team 
We've been evaluating the low-latency mode recently and noticed some unexpected performance behavior on newer GPUs. We'd like to share our findings in case this helps with tuning or further investigation.

Environment
* DeepEP commit: b57e5e212ab75350f53c72064333e4fe1076b1da
* Test command:


python3 /opt/DeepEP/tests/test_low_latency.py --num-experts 256

* Nodes: 2
* GPUs compared: H100 vs B200
* Mode: Low-Latency Mode


Problem Description
When running DeepEP in low-latency mode, we observed that B200 consistently underperforms H100, which is unexpected given the newer architecture.
The gap appears in both dispatch and combine phases, and is visible in:
* Non-hook path (end-to-end bandwidth & latency)
* Hook mode (pure send latency)

We also evaluated an optimization that merges multiple WRs (WR=16) in low-latency mode. While this reduces send latency for both GPUs, B200 still remains slower than H100, and shows much higher sensitivity to WR batching.

<meta charset="UTF-8"><h2 class="mp-heading" data-morpho-type="heading" data-uuid="480ea7b2-fdc5-11f0-a2b9-67e82a3f8d27" data-indent="0" data-slate-node="element" style="padding-left:0px"><span data-morpho-text="1%EF%B8%8F%E2%83%A3%20Low-Latency%20Mode%20(Default)">1️⃣ Low-Latency Mode (Default)</span></h2><h3 class="mp-heading" data-morpho-type="heading" data-uuid="480ea7b4-fdc5-11f0-a2b9-67e82a3f8d27" data-indent="0" data-slate-node="element" style="padding-left:0px"><span data-morpho-text="Non-hook%20path%20performance">Non-hook path performance</span></h3><div class="mp-table-align"><div class="mp-table-wrapper"><div data-slate-node="element" style="padding-left:0px" class="mp-table-container">
GPU | Dispatch Bandwidth (GB/s) | Dispatch Latency (us) | Combine Bandwidth (GB/s) | Combine Latency (us)
-- | -- | -- | -- | --
H100 | 59.86 | 125.69 | 70.40 | 206.65
B200 | 52.92 | 142.59 | 65.55 | 222.32

</div><div class="mp-table-serialize-flag"><br/></div></div></div><span data-morpho-doc-data='{"token":"eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIiwiYXBwSWQiOjEsInVpZCI6IkxfcWM3dVFiT3oiLCJkb2NJZCI6ImJScWtIOGMwUmhLY2tGIn0..zD5E7cZrGROxzLvS.n0ZFDm_-jJMh28u0eLJPHVwoAfRCOFsaXzUiliWulZkRHYa0Ij2aKiN_lxCxu61HJs1u8xw8WEzQdOjISDCFpYUwr674McI6fmGZFYQjQIu2l_G785UjNDnFtWgAPuLhRY3UXwQaO-glL9HgOzDZV7JB04Y8Av0oDi66FGCX9PzMI8FmydfsWNKcvkzfcrd_CZ7R9O1TzGpm-2tmF1VmSi38CQ.yv0pmd58EdHQCy9j-p589g","appId":"1"}' class='mp-morpho-clipboard-doc-data' ></span>

<meta charset="UTF-8"><h3 class="mp-heading" data-morpho-type="heading" data-uuid="48100742-fdc5-11f0-a2b9-67e82a3f8d27" data-indent="0" data-slate-node="element" style="padding-left:0px"><span data-morpho-text="Hook%20mode%20(Send%20latency%20only)">Hook mode (Send latency only)</span></h3><div class="mp-table-align"><div class="mp-table-wrapper"><div data-slate-node="element" style="padding-left:0px" class="mp-table-container">
GPU | Dispatch Send Latency (us) | Combine Send Latency (us)
-- | -- | --
H100 | 24.44 | 31.40
B200 | 34.20 | 38.82

</div><div class="mp-table-serialize-flag"><br/></div></div></div><span data-morpho-doc-data='{"token":"eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIiwiYXBwSWQiOjEsInVpZCI6IkxfcWM3dVFiT3oiLCJkb2NJZCI6ImJScWtIOGMwUmhLY2tGIn0..zD5E7cZrGROxzLvS.n0ZFDm_-jJMh28u0eLJPHVwoAfRCOFsaXzUiliWulZkRHYa0Ij2aKiN_lxCxu61HJs1u8xw8WEzQdOjISDCFpYUwr674McI6fmGZFYQjQIu2l_G785UjNDnFtWgAPuLhRY3UXwQaO-glL9HgOzDZV7JB04Y8Av0oDi66FGCX9PzMI8FmydfsWNKcvkzfcrd_CZ7R9O1TzGpm-2tmF1VmSi38CQ.yv0pmd58EdHQCy9j-p589g","appId":"1"}' class='mp-morpho-clipboard-doc-data' ></span>

<meta charset="UTF-8"><h2 class="mp-heading" data-morpho-type="heading" data-uuid="48102e54-fdc5-11f0-a2b9-67e82a3f8d27" data-indent="0" data-slate-node="element" style="padding-left:0px"><span data-morpho-text="2%EF%B8%8F%E2%83%A3%20Low-Latency%20Mode%20%2B%20Merged%20WR%20(WR%20%3D%2016)">2️⃣ Low-Latency Mode + Merged WR (WR = 16)</span></h2><h3 class="mp-heading" data-morpho-type="heading" data-uuid="48102e56-fdc5-11f0-a2b9-67e82a3f8d27" data-indent="0" data-slate-node="element" style="padding-left:0px"><span data-morpho-text="Hook%20mode%20(Send%20latency%20only)">Hook mode (Send latency only)</span></h3><div class="mp-table-align"><div class="mp-table-wrapper"><div data-slate-node="element" style="padding-left:0px" class="mp-table-container">
GPU | Dispatch Send Latency (us) | Combine Send Latency (us)
-- | -- | --
H100 | 22.75 | 31.43
B200 | 29.50 | 36.51

</div><div class="mp-table-serialize-flag"><br/></div></div></div><span data-morpho-doc-data='{"token":"eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIiwiYXBwSWQiOjEsInVpZCI6IkxfcWM3dVFiT3oiLCJkb2NJZCI6ImJScWtIOGMwUmhLY2tGIn0..zD5E7cZrGROxzLvS.n0ZFDm_-jJMh28u0eLJPHVwoAfRCOFsaXzUiliWulZkRHYa0Ij2aKiN_lxCxu61HJs1u8xw8WEzQdOjISDCFpYUwr674McI6fmGZFYQjQIu2l_G785UjNDnFtWgAPuLhRY3UXwQaO-glL9HgOzDZV7JB04Y8Av0oDi66FGCX9PzMI8FmydfsWNKcvkzfcrd_CZ7R9O1TzGpm-2tmF1VmSi38CQ.yv0pmd58EdHQCy9j-p589g","appId":"1"}' class='mp-morpho-clipboard-doc-data' ></span>

Key Observations
1. B200 has higher dispatch and combine latency than H100 in low-latency mode.
2. Send latency (hook path) is significantly worse on B200

    * Dispatch send latency is ~40% higher than H100 in default LL mode.

3. WR merging reduces latency for both GPUs, but does not eliminate the gap.
4. Since this is a 2-node test under identical workload and scale, the issue is unlikely to be caused by topology differences.

5. B200 is significantly more sensitive to WR merging than H100
After increasing WR merge depth (WR=16):
* B200 dispatch send latency drops from 34.20 us → 29.50 us (~14% improvement)
* H100 dispatch send latency drops from 24.44 us → 22.75 us (~7% improvement)

This suggests:
* B200 benefits much more from reducing doorbell/MMIO write frequency
* The bottleneck on B200 may be more strongly related to:
    * GPU→NIC doorbell write latency
    * PCIe/NVLink MMIO path efficiency
    * WQE posting overhead in low-latency mode


In contrast, H100 appears less sensitive to WR batching, indicating its doorbell or WQE submission path may already be more efficient.
This architectural sensitivity difference may explain why B200 underperforms in the default low-latency configuration.

Questions
1. Has DeepEP low-latency mode been specifically tuned or validated on B200 / Blackwell?
2. Are there recommended parameter adjustments for B200, such as:

    * Different WQE batching strategy
    * Different doorbell ringing policy
    * Different QP or CQ moderation settings

3. Could this be related to GPU→NIC doorbell MMIO latency differences on B200?

We can provide Nsight Systems traces or IB hardware counters if needed.



## 评论 (0)
