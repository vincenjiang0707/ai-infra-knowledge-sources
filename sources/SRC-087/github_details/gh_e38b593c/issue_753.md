# [Issue #753] Would an SGLang export helper for DSpark checkpoints be welcome?

source: https://github.com/vllm-project/speculators/issues/753
state: open | updated: 2026-07-14T18:30:11Z
labels: 

## 正文

We ran [RedHatAI/GLM-5.2-speculator.dspark](https://huggingface.co/RedHatAI/GLM-5.2-speculator.dspark) on SGLang's DSPARK stack (sgl-project/sglang#30261) with a config-only transformation — weights untouched:

- `architectures: ["DSparkDraftModel"]` → `["Qwen3DSparkModel"]`, flatten `transformer_layer_config` to top level
- `aux_hidden_state_layer_ids` → `target_layer_ids` shifted by −1 (SGLang captures layer inputs and re-adds +1 internally)
- copy `block_size` / `mask_token_id` / `markov_rank` / `markov_head_type` / confidence-head flags into `dflash_config` + `dspark_config` blocks

Accept length matches this checkpoint's published vLLM reference (details: [sgl-project/sglang#30261 (comment)](https://github.com/sgl-project/sglang/pull/30261#issuecomment-4923019073)).

Happy to send a PR if useful.


## 评论 (2)

### shanjiaz · 2026-07-14

@jessiewei7 Thanks for reaching out! yes sglang support would be great, feel free to put up a PR! Reach out to us on vllm slack if you have any questions/concerns.

### fynnsu · 2026-07-14

@jessiewei7 just want to point out that we just landed #760 which allows users to choose between the dflash style anchor sampling "slot `k` predicts `anchor + k` and the dspark version "slot `k` predicts `anchor + k + 1`.

We also store the selection in the speculators config. Note vLLM supports both variants and the dflash style is useful for finetuning dflash models into dspark ones.
