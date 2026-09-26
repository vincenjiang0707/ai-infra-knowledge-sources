# [Issue #2735] DSv4 canonical example drops MTP layer; load_quantizable_moe regex anchored at ^layers excludes mtp.* block

source: https://github.com/vllm-project/llm-compressor/issues/2735
state: closed | updated: 2026-09-24T20:20:26Z
labels: stale

## 正文

## Summary

The canonical `examples/quantizing_moe/deepseek_v4_example.py` (`kylesayrs/transformers-v5` branch, commit `8c533c21f`, 2026-05-20) calibrates the main 43 routed-expert layers of DeepSeek-V4-Flash but **silently drops the MTP (multi-token-prediction) draft block** (`mtp.0.ffn.experts.0..255`). This makes the resulting artifact unusable with vLLM's `--speculative-config '{"method":"mtp","num_speculative_tokens":N}'`.

Two independent root causes compound:

### Root cause 1 — `transformers` 5.8.1 silently drops `mtp.*` on load

`transformers.models.deepseek_v4.modeling_deepseek_v4.DeepseekV4PreTrainedModel` carries:

```python
_keys_to_ignore_on_load_unexpected = [r"(^|\.)mtp\..*"]
```

`from_pretrained` filters these keys before they reach the state dict. Even after this filter is neutralized, `transformers/models/deepseek_v4/` has **no MTP module class** — only `num_nextn_predict_layers: int = 1` in the config. So the MTP block has no submodule for the keys to attach to.

### Root cause 2 — `load_quantizable_moe` / `linearize_moe` is MTP-unaware

In `src/llmcompressor/modeling/moe/conversion_mappings.py`:

```python
ARCH_TO_2D_MAPPINGS = {
    "deepseek_v4": (
        ["mlp.experts.gate_up_proj", "mlp.experts.down_proj"],
        [
            WeightRenaming(
                source_patterns=r"^layers\.(\d+)\.mlp\.experts\.(\d+)\.w1\.",
                target_patterns=r"layers.\1.mlp.experts.\2.gate_proj.",
            ),
            # ... w2, w3 ...
        ],
    )
}
```

The `^layers\.` anchor excludes `mtp.0.mlp.experts.*` paths. Even if root cause 1 were fixed (MTP module class added), `linearize_moe` would skip MTP's MoE block.

Grep across `src/llmcompressor/modeling/` confirms: **zero references to `mtp`/`MTP`/`nextn`.**

## Repro

```python
from llmcompressor.modeling.moe.linearize import load_quantizable_moe
from transformers import AutoModelForCausalLM
with load_quantizable_moe():
    model = AutoModelForCausalLM.from_pretrained("RedHatAI/DeepSeek-V4-Flash-BF16", device_map="cpu")
# Count modules matching mtp.*ffn.experts:
mtp_experts = [n for n,_ in model.named_modules() if "mtp." in n and "experts." in n]
print(f"MTP expert modules found: {len(mtp_experts)}")  # → 0
# Where they should be: 256 routed experts on mtp.0.ffn
```

## Why this matters

- **vLLM speculative decoding with MTP requires the draft head to be quantized in the same compressed-tensors metadata** (otherwise vLLM's `--speculative-config method=mtp` rejects the model)
- Existing public DSv4 W4A16/NVFP4 quants ship without MTP for this exact reason
- DSv4-Flash's MTP block claims ~1.5-2× decode throughput on agentic workloads (per upstream paper); a quant artifact that drops it forfeits that gain

## Proposed direction

Three artifact changes:

1. **Add a `DeepseekV4NextNPredictor` module class** to `transformers.models.deepseek_v4.modeling_deepseek_v4` — wraps the existing `DeepseekV4DecoderLayer` with the `e_proj`, `h_proj`, `enorm`, `hnorm`, `shared_head`, `hc_*` parameters. Then drop the `_keys_to_ignore_on_load_unexpected` regex (or at least emit a warning).

2. **Extend `ARCH_TO_2D_MAPPINGS["deepseek_v4"]`** to cover `mtp.\d+.mlp.experts.*` paths in addition to `layers.\d+.mlp.experts.*`. Either generalize the regex anchor to `(?:^|^layers\.\d+|^mtp\.\d+)` or add explicit mtp-prefixed WeightRenaming entries.

3. **Update `examples/quantizing_moe/deepseek_v4_example.py`** to verify MTP keys are present in the quantized artifact (post-`save_pretrained` assertion).

Item 1 needs to land in `huggingface/transformers`; items 2-3 land here.

## PRs filed

- huggingface/transformers#46127 — `DeepseekV4NextNPredictor` class shim (item 1)
- vllm-project/llm-compressor#2739 — `ARCH_TO_2D_MAPPINGS` MTP regex extension (item 2)

cc @kylesayrs — companion to your active DSv4 iteration. The PRs are paired (#2739 depends on #46127).

## 评论 (4)

### pasta-paul · 2026-05-22

## Production validation — extended DSv4 example shipped

Update: extended the DSv4 canonical example to include the MTP block in quantization recipe + validated end-to-end in a shipping artifact.

### Setup
- Repo: https://github.com/canada-quant/dsv4-flash-w4a16-fp8-mtp
- Artifact: https://huggingface.co/canada-quant/DeepSeek-V4-Flash-W4A16-FP8-MTP (public)
- Recipe: [`scripts/quantize_v4_w4a16_mtp.py`](https://github.com/canada-quant/dsv4-flash-w4a16-fp8-mtp/blob/main/scripts/quantize_v4_w4a16_mtp.py)

### Deltas vs the upstream DSv4 example
1. Recipe passes `sequential_targets=["DeepseekV4DecoderLayer", "DeepseekV4NextNPredictor"]` so `linearize_moe` walks MTP's MoE block as well as the main MoE.
2. Recipe `ignore=` includes `[r"re:.*mtp\..*"]` to defense-in-depth exclude MTP from quant.
3. Recipe `targets=` anchored at `^model.layers.\d+\.` (workaround for vllm-project/compressed-tensors#712 — `ignore=` not honored at save).
4. Runtime install of `DeepseekV4NextNPredictor` class (per huggingface/transformers#46127) + extended conversion mapping (per huggingface/transformers#46129) BEFORE `from_pretrained`.

### Evidence the example works
- Phase 2 GPTQ run: 8× H200, 15h wall, 44 subgraphs (43 main layers + 1 MTP, MTP gets 0 quant tensors per Option Y).
- Output: 4 shards, 159 GB, 799 `mtp.*` keys all BF16 (no quant suffixes).
- Serve validation: 69.94% MTP draft-token acceptance on 200 prompts via vLLM with PRs #43248+#43288+#43290+#43319 cherry-picked.

Quality (vs predecessor non-MTP W4A16):
- GSM8K 8-shot strict: 93.71% (predecessor 94.99%, within SE)
- MMLU 5-shot: 86.88% (predecessor 87.27%, within SE)
- HumanEval pass@1: 84.76% (predecessor reported 54.27% as strict-regex artifact)

Raw data: https://github.com/canada-quant/dsv4-flash-w4a16-fp8-mtp/tree/main/benchmarks/phase2

Happy to send a PR to land the MTP extensions in the upstream DSv4 example if there's appetite — the recipe diff is well-scoped now that the patterns are validated.

### pasta-paul · 2026-05-27

> **Disclosure:** this comment was generated with AI assistance.

**Tracking note — MTP-class cluster.** This filing is one of four artifacts for what is fundamentally a single bug — "DSv4 MTP weights have no home in the canonical loader path":

| Filing | Layer | Role |
|---|---|---|
| huggingface/transformers#46127 (PR) | transformers | Add `DeepseekV4NextNPredictor` class so the MTP block has a module to load into |
| huggingface/transformers#46129 (issue) | transformers | `conversion_mapping` doesn't cover `mtp.*` paths — companion to #46127 |
| vllm-project/llm-compressor#2735 (issue) | llm-compressor | Canonical DSv4 calibration example drops MTP; regex `^layers\.` anchored excludes `mtp.*` |
| vllm-project/llm-compressor#2739 (PR) | llm-compressor | Extend `ARCH_TO_2D_MAPPINGS` for the MTP block — fixes #2735 |

Posting this header on all four so maintainers see one effort rather than four independent threads. Happy to consolidate further if reviewers prefer a single tracking issue.

### github-actions[bot] · 2026-08-25

This issue has been automatically marked as stale because it has not had any activity within 90 days. It will be automatically closed if no further activity occurs within 30 days. Leave a comment if you feel this issue should remain open. Thank you!

### github-actions[bot] · 2026-09-24

This issue has been automatically closed due to inactivity. Please feel free to reopen if you feel it is still relevant. Thank you!
