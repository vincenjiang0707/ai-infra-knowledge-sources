# [Issue #290] [QUESTION]Why does fp8_mqa_logits use four MATH WGs for computation?

source: https://github.com/deepseek-ai/DeepGEMM/issues/290
state: closed | updated: 2026-05-22T01:30:07Z
labels: 

## 正文

Why does fp8_mqa_logits use four MATH WGs for computation? In typical Hopper implementations, only two MATH WGs are generally used. This is also the case in the DeepGEMM 1d1d and 1d2d implementations.

Is this design choice related to the KV block dimension being 256? If we change the KV block size to 128, would it impact performance?

## 评论 (2)

### ajwise9 · 2026-03-22

In simple terms just because FP8 WGMMA on H100 delivers ~2× the throughput of BF16.  

<img width="1075" height="287" alt="Image" src="https://github.com/user-attachments/assets/2e59de40-6c12-480d-9fc6-5f809bc4bcc6" />

[source](https://gemslabs.io/reports )

Also, with 2 MATH WGs (the standard ping-pong schedule), the tensor cores in each WG  are underutilized because the per-WG tile doesn't generate enough independent WGMMA instructions to fully hide the ~16-cycle WGMMA latency. Going to 4 WGs doubles the in-flight WGMMA wavefronts, keeping the tensor core pipeline saturated.


**Is it tied to block_N=256? What if you drop to 128?**
Yes, directly. 256 gives 8× k32 WGMMA steps per KV iteration, so enough to keep 4 WGs fed. At 128 you'd halve that, starve the WGs, and want to drop back to 2. Expect ~10–20% give or take regression.

### pengwubj · 2026-05-22

Thanks a  lot !
