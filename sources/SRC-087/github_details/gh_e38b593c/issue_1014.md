# [Issue #1014] [Feature request]: Support DFlash 2 drafters (path selector + local convolution)

source: https://github.com/vllm-project/speculators/issues/1014
state: closed | updated: 2026-08-30T01:06:31Z
labels: 

## 正文

## Feature request: Support DFlash 2 drafters (path selector + local convolution)

### Summary
Speculators already supports the original DFlash training algorithm
(anchored-block drafting), but Inco AI's follow-up, **DFlash 2**
(https://inco.ai/blog/dflash2/, Aug 18 2026), adds two small modules on
top of the existing DFlash backbone that aren't currently supported:

1. **Lightweight pairwise path selector** — scores every adjacent pair of
   top-16 candidates per position and greedily/samples a coherent path
   through them, instead of taking each position's independent top-1 pick.
2. **Two-tap dynamic depthwise convolution** — inserted before/after each
   attention and MLP sublayer, mixing each draft position's hidden state
   with its predecessor's to reduce "suffix decay" toward the end of the
   block.

Both are cheap (~2M and ~16.5M added params respectively, <1.5% added
draft–verify cycle latency combined) and reportedly raise acceptance
length ~20%+ over plain DFlash.

Notably, Inco AI's own benchmarks show DFlash 2 outperforming DSpark drafters. 
On Qwen3.5-4B (per-request mean acceptance length):

| Dataset   | MTP  | DFlash | DSpark | DFlash 2 |
| --------- | ---- | ------ | ------ | -------- |
| GSM8K     | 4.78 | 4.99   | 5.69   | **6.20** |
| MATH-500  | 5.04 | 5.42   | 6.20   | **6.76** |
| HumanEval | 4.84 | 5.43   | 5.80   | **6.28** |
| MBPP      | 4.16 | 4.49   | 4.96   | **5.41** |
| MT-Bench  | 3.90 | 4.26   | 4.77   | **5.20** |
| Mean      | 4.54 | 4.92   | 5.49   | **5.97** |

### Motivation
Two DFlash 2 checkpoints are already public on Hugging Face:
- `incoai/Qwen3.8-27B-DFlash2`
- `incoai/Muse-Glimmer-30B-DFlash2`

and are runnable today via a fork/PR of SGLang, vLLM, and llama.cpp (see
the blog's "Run It Now" section). It'd be great to have first-class
support in Speculators so these (and future DFlash 2 drafters) can be
trained/converted/served through the standard Speculators → vLLM path,
consistent with existing DFlash support.

### Reference material
- DFlash 2 blog post: https://inco.ai/blog/dflash2/
- Original DFlash repo (architecture DFlash 2 builds on): https://github.com/z-lab/dflash/
- DFlash 2 checkpoints: https://huggingface.co/collections/incoai/dflash-2-6a8432273c9998ce1685d4c5

cc @jianc99 @xiziqiao @zhijian-liu

## 评论 (3)

### coderabbitai[bot] · 2026-08-19

<!-- This is an auto-generated issue plan by CodeRabbit -->
<details>
<summary>🔗 Related PRs</summary>

vllm-project/speculators#589 - feat(dflash): selectable attention backend (sdpa/eager) with dense mask [merged]
vllm-project/speculators#736 - Add D-PACE loss implementation for D-Flash training [merged]
vllm-project/speculators#760 - Add support sample_from_anchor logic to DFlash/DSpark  [merged]
vllm-project/speculators#986 - Add Muse Glimmer training support [open]
vllm-project/speculators#992 - feat(train): add --gradient-checkpointing for DFlash/DSpark [open]
</details>

---
<details>
<summary>📝 Issue Planner</summary>

<sub>Check the box below or use the `@coderabbitai plan` command to generate an implementation plan and prompts that you can use with your favorite coding assistant.</sub>

- [ ] <!-- {"checkboxId":"8d4f2b9c-3e1a-4f7c-a9b2-d5e8f1c4a7b9"} --> Create Plan
</details>


---
<details>
<summary> 🧪 Issue enrichment is currently in open beta.</summary>


You can configure auto-planning by selecting labels in the issue_enrichment configuration.

To disable automatic issue enrichment, add the following to your `.coderabbit.yaml`:
```yaml
issue_enrichment:
  auto_enrich:
    enabled: false
```
</details>

💬 Have feedback or questions? Drop into our [discord](https://discord.gg/coderabbit)!

### fynnsu · 2026-08-25

#1006 

### rasyosef · 2026-08-30

#1006 (`Add experimental DFlash2 training and checkpoint support`) has been merged 🙌. Closing this issue.
