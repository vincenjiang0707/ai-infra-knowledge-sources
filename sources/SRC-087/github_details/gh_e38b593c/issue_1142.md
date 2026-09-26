# [Issue #1142] [Question]: DFlash2 multimodal acceptance gap with mixed text+MM training — text deploy ≥ train val, but ALLaVA deploy −10%

source: https://github.com/vllm-project/speculators/issues/1142
state: open | updated: 2026-09-18T11:42:24Z
labels: 

## 正文

### Summary

DFlash2 draft trained on MIXED text + multimodal data. Text deployment matches/exceeds training val, but
multimodal deployment is systematically lower — and ORACLE decomposition shows
the draft and selector are NOT degraded. Root cause appears to be path
divergence amplified by multimodal next-token uncertainty, not draft quality.

### Setup

- Verifier: Qwen3.5-122B-A10B-w8a8 (MoE, W8A8, Ascend NPU, TP8+DP2)
- Draft: DFlash2 5-layer (conv_kernel_size=2, selector_top_k=16, block_size=8),
  trained on MIXED text + multimodal data (pure text + image prompts),
  `--loss-fn kl_div` + selector CE, teacher-forced
- Deployment: vLLM (speculators-based fork) 0.27.2rc1, greedy (temp=0), c=1
- Test sets: GSM8K (1319), MATH-500 (500), ALLaVA (100, 1 image each)

### Results (same checkpoint, c=1 greedy, accept_len includes +1 bonus token)

| Eval set | N | type | accept_rate | accept_len |
|---|---|---|---|---|
| Train val (self_cond path) | - | - | - | **4.310** |
| GSM8K | 1319 | text deploy | **0.6298** | **5.408** |
| MATH-500 | 500 | text deploy | **0.6022** | **5.215** |
| ALLaVA | 100 | 1-img deploy | 0.4074 | **3.852** |

- Text deploy accept_len (5.41 / 5.22) > train val (4.31) — text path is healthy
- Multimodal ALLaVA deploy (3.85) < train val (4.31) — **−10%**
- accept_rate is token-level (accepted / draft_tokens), bonus-free in all rows

### ORACLE decomposition (ALLaVA, 67 requests)

Both draft and selector are NOT degraded:
- trunk_topK_hit (candidate contains target): pos0=1.0 → pos6=0.729
  (better than train val recall 0.847)
- selector_hit (picks correct): pos0=0.847 → pos6=0.494
  (≈ train teacher_forced_selector_acc 0.666)

So the acceptance gap is NOT caused by a broken draft/selector — it is
autoregressive path divergence: once the draft guesses wrong at an early
position, the block-internal context deviates from the training distribution,
and multimodal (image→text) mapping is much more ambiguous than text, so
errors compound faster.

### Questions

1. Training is MIXED text+MM, yet multimodal deployment still drops vs text.
   Is the remaining gap purely path divergence, or does mixed training itself
   under-fit the multimodal distribution?
2. Train val uses the `1-TV` upper bound (distribution overlap) while
   deployment requires argmax agreement. For multimodal flat distributions,
   is the val metric systematically optimistic?
3. Would switching unary loss from `kl_div` to `nla`/`tv` (argmax-aligned)
   or adding more multimodal data to the mix narrow this gap?

### Environment

- Ascend NPU, CANN 9.0.1, vLLM 0.27.2rc1.dev92, speculators 0.8.0.dev208
- Can provide config.json / train_command.txt / reproduction data

## 评论 (1)

### ScutYangLin · 2026-09-18

please provide config.json / train_command.txt / reproduction data
