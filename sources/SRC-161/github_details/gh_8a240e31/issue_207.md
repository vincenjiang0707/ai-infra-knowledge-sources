# [Issue #207] model tracker: discover new open-source model, update to model coverage doc, add new kernel definition 20260304

source: https://github.com/flashinfer-ai/flashinfer-bench/issues/207
state: closed | updated: 2026-03-11T17:37:57Z
labels: 

## 正文

- discover new open-source model
- update model to model-coverage summary
- add new kernel definitions, if needed

## 评论 (4)

### yyihuang · 2026-03-05

@claude 

### claude[bot] · 2026-03-05

**Claude finished @yyihuang's task in 5m 45s** —— [View job](https://github.com/flashinfer-ai/flashinfer-bench/actions/runs/22695544728) • [`claude/issue-207-20260305-0005`](https://github.com/flashinfer-ai/flashinfer-bench/tree/claude/issue-207-20260305-0005) • [Create PR ➔](https://github.com/flashinfer-ai/flashinfer-bench/compare/main...claude/issue-207-20260305-0005?quick_pull=1&title=docs%3A%20add%20Gemma%203%2027B%2C%20NemotronH%2047B%2C%20Qwen3%2014B%20to%20model%20coverage%20tracker&body=Adds%203%20newly%20discovered%20open-source%20models%20to%20docs%2Fmodel_coverage.mdx%3A%0A%0A-%20Gemma%203%2027B%20(Google%2C%202025)%3A%20GQA%2BDense%2C%20all%2015%20definitions%20missing%0A-%20NemotronH%2047B%20(NVIDIA%2C%202025)%3A%20GQA%2BMamba2%20hybrid%2C%20Mamba2%20SSU%20op%20type%20not%20yet%20supported%0A-%20Qwen3%2014B%20(Alibaba%2C%202025)%3A%20GQA%2BDense%2C%203%2F14%20defs%20present%0A%0ACloses%20%23207%0A%0AGenerated%20with%20%5BClaude%20Code%5D(https%3A%2F%2Fclaude.ai%2Fcode))

---
### Model Tracker: Discover New Models & Update Coverage

- [x] Gather context and understand the request
- [x] Read current model_coverage.mdx (24 models previously tracked)
- [x] Audit existing definitions (rmsnorm, gemm, gqa_paged, gqa_ragged, mla_paged, moe, sampling, dsa_paged, gdn)
- [x] Discover new popular models not yet tracked
- [x] Add 3 new model entries to model_coverage.mdx (now 27 models total)
- [x] Commit and push changes

### Summary

Added 3 new open-source models to `docs/model_coverage.mdx`:

| Model | Architecture | Coverage | Key Gap |
|-------|-------------|:--------:|---------|
| **Gemma 3 27B** | GQA + Dense | ❌ Not covered | New dims: `rmsnorm_h5376`, `gqa_*_h32_kv16_d128`, `sampling_v262144` (15 defs missing) |
| **NemotronH 47B** | GQA + Mamba2 | ❌ Not covered | **Mamba2 SSU op type not yet supported** in FlashInfer-Bench |
| **Qwen3 14B** | GQA + Dense | ❌ Not covered | New dims: `rmsnorm_h5120`, `gqa_*_h20_kv4_d128` at TP=2 (11 defs missing, 3 sampling ✅ shared) |

**Key findings from this discovery run:**
- **Gemma 3 27B** is the most popular untracked model (Google's flagship open model, served by Groq/Together/Fireworks/Vertex AI). Its unique `head_dim=128` explicit config (decoupled from hidden_size=5376) means all GQA and GEMM dimensions are new.
- **NemotronH 47B** (NVIDIA) represents a new architecture class (Mamba2 hybrid) that requires a new `mamba_ssu` op type before it can be supported. This is analogous to how MiniMax M2 requires `lightning_attn`.
- **Qwen3 14B** fills a gap in the Qwen3 model family coverage. Its `rmsnorm_h5120` is also needed by Mistral Nemo 12B and Mistral Small 3.1 24B.

**Next steps to improve coverage:**
- Run `/extract-kernel-definitions --model-name gemma3_27b` to create the 15 missing definitions
- Define the `mamba_ssu` op type to enable NemotronH support
- Verify Qwen3 14B exact dims with HuggingFace config; run `/extract-kernel-definitions --model-name qwen3_14b`


 |

### yyihuang · 2026-03-05

@claude perform next steps to improve coverage

### claude[bot] · 2026-03-05

**Claude finished @yyihuang's task in 16m 24s** —— [View job](https://github.com/flashinfer-ai/flashinfer-bench/actions/runs/22695899481) • [`claude/issue-207-20260305-0017`](https://github.com/flashinfer-ai/flashinfer-bench/tree/claude/issue-207-20260305-0017) • [Create PR ➔](https://github.com/flashinfer-ai/flashinfer-bench/compare/main...claude/issue-207-20260305-0017?quick_pull=1&title=feat%3A%20add%20Gemma%203%2027B%20and%20Qwen3%2014B%20kernel%20definitions%2C%20update%20model%20coverage&body=Closes%20%23207%0A%0AAdds%2026%20new%20kernel%20definition%20JSON%20files%20for%20Gemma%203%2027B%20(15%20defs%2C%20fully%20covered)%20and%20Qwen3%2014B%20(14%20defs%2C%20fully%20covered%20with%203%20sampling%20shared)%2C%20plus%20NemotronH%2047B%20coverage%20entry%20noting%20Mamba2%20blocker.%0A%0AThe%20new%20rmsnorm_h5120%20definition%20also%20improves%20coverage%20for%205%20existing%20models%20(Mistral%20Nemo%2C%20Mistral%20Small%2C%20Phi-4%2C%20Llama%204%20Scout%2FMaverick).%0A%0AGenerated%20with%20%5BClaude%20Code%5D(https%3A%2F%2Fclaude.ai%2Fcode))

---
### Model Coverage Improvement: Next Steps

- [x] Gather context and understand the request
- [x] Read current model_coverage.mdx and existing definitions
- [x] Verify Gemma 3 27B exact architecture dimensions (hidden=5376, intermediate=21504, 32q/16kv heads, vocab=262208)
- [x] Verify Qwen3 14B exact architecture dimensions (hidden=5120, intermediate=17408, 40q/8kv heads, vocab=151936, TP=2)
- [x] Create 15 kernel definition JSONs for Gemma 3 27B (all new dims)
- [x] Create 11 kernel definition JSONs for Qwen3 14B (3 sampling shared with other Qwen3 models)
- [x] Update model_coverage.mdx (new models + improved coverage for 5 existing h5120 models)
- [x] Commit and push changes (27 files, 2064 insertions)

### Summary

**26 new definition JSON files** added across rmsnorm, gqa_paged, gqa_ragged, gemm, and sampling op types:

#### Gemma 3 27B — now ✅ Fully Covered (15/15)
Verified from HuggingFace config: `hidden=5376, intermediate=21504, 32q/16kv heads, head_dim=128, vocab=262208`

| Category | Definitions |
|----------|-------------|
| RMSNorm | `rmsnorm_h5376`, `fused_add_rmsnorm_h5376` |
| GQA Paged | `h32_kv16_d128` decode (ps1, ps64) + prefill (ps1, ps64) |
| GQA Ragged | `gqa_ragged_prefill_causal_h32_kv16_d128` |
| GEMM | `n4096_k5376` (q), `n2048_k5376` (k/v), `n5376_k4096` (o), `n21504_k5376` (gate/up), `n5376_k21504` (down) |
| Sampling | top_k / top_k_top_p / top_p v262208 |

#### Qwen3 14B — now ✅ Fully Covered (14/14)
Verified from HuggingFace config: `hidden=5120, intermediate=17408, 40q/8kv heads, head_dim=128, vocab=151936`; **TP=2** serving config → 20q/4kv per device

| Category | Definitions |
|----------|-------------|
| RMSNorm | `rmsnorm_h5120`, `fused_add_rmsnorm_h5120` |
| GQA Paged | `h20_kv4_d128` decode (ps1, ps64) + prefill (ps1, ps64) at TP=2 |
| GQA Ragged | `gqa_ragged_prefill_causal_h20_kv4_d128` |
| GEMM | `n7168_k5120` (qkv), `n5120_k5120` (o), `n34816_k5120` (gate_up), `n5120_k17408` (down) |
| Sampling | shared v151936 (already existed) |

#### NemotronH 47B — ❌ Blocked
Added to model_coverage.mdx. Requires new `mamba_ssu` op type for Mamba2 layers before any definitions can be created.

#### Cascade improvements from rmsnorm_h5120 (now shared):
| Model | Before | After |
|-------|:------:|:-----:|
| Mistral Nemo 12B | 5/14 | 7/14 |
| Mistral Small 3.1 24B | 5/14 | 7/14 |
| Phi-4 14B | 0/14 | 3/14 |
| Llama 4 Scout 17B-16E | 0/10 | 2/10 |
| Llama 4 Maverick 17B-128E | 0/10 | 2/10 |


 • [`claude/issue-207-20260305-0017`](https://github.com/flashinfer-ai/flashinfer-bench/tree/claude/issue-207-20260305-0017)
