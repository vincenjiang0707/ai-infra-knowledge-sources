# [Issue #212] model tracker: improve model/kernel coverage - 20260311

source: https://github.com/flashinfer-ai/flashinfer-bench/issues/212
state: open | updated: 2026-03-11T17:51:48Z
labels: 

## 正文

- discover new open-source model/kernel, update to model coverage doc
- for unsupported kernels, add kernel definitions and reference tests

## 评论 (2)

### yyihuang · 2026-03-11

@claude 

### claude[bot] · 2026-03-11

**Claude finished @yyihuang's task in 11m 59s** —— [View job](https://github.com/flashinfer-ai/flashinfer-bench/actions/runs/22966181399) • [`claude/issue-212-20260311-1739`](https://github.com/flashinfer-ai/flashinfer-bench/tree/claude/issue-212-20260311-1739) • [Create PR ➔](https://github.com/flashinfer-ai/flashinfer-bench/compare/main...claude/issue-212-20260311-1739?quick_pull=1&title=feat%3A%20add%20DeepSeek%20R1-0528%20and%20Qwen3%204B%20to%20model%20coverage%20tracker&body=Closes%20%23212%0A%0A%23%23%20Summary%0A%0A-%20Add%20DeepSeek%20R1-0528%20and%20Qwen3%204B%20to%20%60docs%2Fmodel_coverage.mdx%60%0A-%20Add%206%20new%20kernel%20definition%20JSON%20files%20for%20Qwen3%204B%20(rmsnorm%2C%20gemm)%0A-%20Add%20reference%20tests%20for%20new%20definitions%20(rmsnorm%2C%20fused_add_rmsnorm%2C%20gemm)%0A%0A%23%23%20Models%20Added%0A%0A%7C%20Model%20%7C%20Architecture%20%7C%20Coverage%20%7C%0A%7C-----%7C-------------%7C%3A--------%3A%7C%0A%7C%20DeepSeek%20R1-0528%20%7C%20MLA%20%2B%20Dense%2FMoE%20%7C%20%F0%9F%9F%A1%20Partial%20%7C%0A%7C%20Qwen3%204B%20%7C%20GQA%20%2B%20Dense%20%7C%20%F0%9F%9F%A1%20Partial%20%7C%0A%0AGenerated%20with%20%5BClaude%20Code%5D(https%3A%2F%2Fclaude.ai%2Fcode))

---
### Model/Kernel Coverage Update

- [x] Gather context and understand the request
- [x] Review current model coverage documentation (27 models tracked)
- [x] Phase 1: Discover new open-source models/kernels
  - **DeepSeek R1-0528** (May 28, 2025) — updated reasoning checkpoint, identical MLA+MoE architecture to DeepSeek V3/R1 at TP=8
  - **Qwen3 4B** (April 2025) — GQA dense, hidden=2560, 32q/8kv heads, head_dim=128
- [x] Phase 2: Map kernels to definitions and check coverage
  - DeepSeek R1-0528: 13/14 definitions present (shares all with V3/R1, missing MLA ragged prefill)
  - Qwen3 4B: all 14 definitions now added (🟡 — workloads not yet collected)
- [x] Phase 3: Add 6 new kernel definitions for Qwen3 4B
  - `rmsnorm_h2560`, `fused_add_rmsnorm_h2560`
  - `gemm_n6144_k2560` (qkv_proj), `gemm_n2560_k4096` (o_proj)
  - `gemm_n19456_k2560` (gate_up), `gemm_n2560_k9728` (down)
- [x] Phase 4: Update `docs/model_coverage.mdx` with 2 new model entries
- [x] Add reference tests for new kernel definitions
  - `test_rmsnorm_h2560.py`, `test_fused_add_rmsnorm_h2560.py`
  - `test_gemm_qwen3_4b.py` (covers all 4 Qwen3-4B GEMM shapes)
- [x] Commit and push changes

### Summary

Added **2 new models** to the coverage tracker (29 models total):

| Model | Architecture | Coverage | Notes |
|-------|-------------|:--------:|-------|
| DeepSeek R1-0528 | MLA + Dense/MoE | 🟡 Partial | Shares all defs with V3/R1; only MLA ragged prefill still missing |
| Qwen3 4B | GQA + Dense | 🟡 Partial | All 14 definitions added; GQA/sampling shared, new GEMM+RMSNorm for h=2560 |

**6 new kernel definitions** added for Qwen3 4B (all in `flashinfer_trace/definitions/`):
- `rmsnorm/rmsnorm_h2560.json`, `rmsnorm/fused_add_rmsnorm_h2560.json`
- `gemm/gemm_n6144_k2560.json`, `gemm/gemm_n2560_k4096.json`, `gemm/gemm_n19456_k2560.json`, `gemm/gemm_n2560_k9728.json`

**3 new reference test files** added (`flashinfer_trace/tests/references/`):
- `test_rmsnorm_h2560.py`, `test_fused_add_rmsnorm_h2560.py`, `test_gemm_qwen3_4b.py`

> **Note**: Qwen3 4B GEMM shapes use `intermediate_size=9728` from the Qwen3 technical report. Run `/extract-kernel-definitions --model-name qwen3_4b --hf-repo-id Qwen/Qwen3-4B` to verify from config.json if needed.


 |
