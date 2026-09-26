# [Issue #356] Does Mega MoE support RTX 50-series GPUs, and can it work in a PCIe-only setup without NVLink?

source: https://github.com/deepseek-ai/DeepGEMM/issues/356
state: open | updated: 2026-09-11T08:03:16Z
labels: 

## 正文

Does Mega MoE support RTX 50-series GPUs, and can it work in a PCIe-only setup without NVLink?

## 评论 (1)

### aganhui · 2026-09-11

Short answer as of nv_dev today: **no, Mega MoE does not run on RTX 50-series (SM120) yet — it is SM100-only (B200).**

The dispatch in `csrc/apis/mega.hpp` hard-requires `arch_major == 10` (see the `fp8_fp4_mega_moe` / `fp4_fp4_mega_moe` / `bf16_mega_moe` entry points), and the underlying kernels are `sm100_fp8_fp4_mega_moe.cuh` / `sm100_bf16_mega_moe.cuh` — they use SM100's UMMA/tcgen05 machinery and tensor-memory features that consumer Blackwell does not expose. Mega MoE landed for SM100 first (April, #304); the SM90 port is still in flight (#323, with #383 merged earlier this month); an SM120 port has not been started.

On the NVLink/PCIe question: NVLink should not matter for DeepGEMM itself. DeepGEMM provides the per-GPU MoE compute kernels; the inter-GPU communication lives in the serving stack around it (e.g., DeepEP, which is where NVLink vs PCIe matters). So whenever SM120 Mega MoE arrives, a PCIe-only setup should be fine at the DeepGEMM level — the effective constraint is memory capacity and bandwidth of the card, not the interconnect.

What SM120 users do get today (nv_dev): the fp8/fp4 GEMM family (normal + m-grouped contiguous/masked + k-grouped), bf16 GEMM, and the fp8/fp4 MQA-logits kernels (dense + paged). Note if you are running on a 5090: the fp8 MQA-logits path has a swizzle bug for head_dim 32/64 that is being fixed in #379/#434, so builds from older nv_dev revisions may return wrong logits for those head dims.
