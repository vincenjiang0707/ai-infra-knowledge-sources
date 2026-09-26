# [Issue #694] [Roadmap] On Policy Training

source: https://github.com/vllm-project/speculators/issues/694
state: open | updated: 2026-09-14T08:17:47Z
labels: 

## 正文

## Motivation

The driver is exposure bias: off-policy multi-turn data conditions each turn on the dataset's responses rather than the target's, so every turn past the first is misaligned. Regenerating turn-by-turn against the on-policy prefix fixes this — and yields longer, more realistic context as a bonus.


## Topic

Ensure no cross-instance attention leakage

- [x] #627

You Only Tokenize Once 

- [ ] #652 #665
- [x] vllm renderer endpoint https://github.com/vllm-project/vllm/pull/46846
- [ ] concurrent preprocessing


Response Regeneration as default

- [ ] [Data] Response regeneration should support multi-turn #693. 
- [ ] [Doc] Make on-policy the documented default for training. Keep off-policy as a cheaper fallback (it skips a full target-model pass over the data) with its acceptance penalty called out, so the tradeoff is explicit.
- [ ] Compatible with multi-modal 
- [ ] Compatible with tool use
- [ ] Support customized sampling config
- [ ] Concurrent preprocessing

## 评论 (1)

### Leslie360 · 2026-09-14

A controlled data point for this roadmap, from a Markov-conditioned (DSpark) drafter on a multimodal OCR target. We trained two drafters for 300 steps with identical data, warm-start, and budget — the only variable being the prev-token source:

- **Arm A (teacher forcing, current default):** train loss 0.697 / token acc 0.643 → served aggregate acceptance **46.3%** (6.94 tokens per round)
- **Arm B (in-loop draft-sampled prev, unrolled Markov argmax as next position's context):** train loss 0.604 / token acc 0.722 → served **40.3%** (6.04 per round)

Served on stock vLLM 0.27.1, temp=0, 100 held-out business samples, same engine and protocol for both arms (a draft-layout footgun — `sample_from_anchor` default mismatch — was corrected on both arms before measuring, so the comparison is layout-clean).

In-loop on-policy sampling did align the training objective — lower loss, higher accuracy — but it served *worse* by ~6pp aggregate acceptance. For this head family at this scale, the exposure-bias intuition did not transfer through to acceptance. This matches the roadmap's emphasis on data regeneration over in-loop sampling, and we wanted to share the counterexample so others don't have to run it.

Happy to share the eval harness details if useful.
