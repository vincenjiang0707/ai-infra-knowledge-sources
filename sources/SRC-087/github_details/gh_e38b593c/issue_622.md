# [Issue #622] [RFC]: Add Medusa speculator (parallel decoding heads)

source: https://github.com/vllm-project/speculators/issues/622
state: closed | updated: 2026-08-29T09:18:03Z
labels: RFC

## 正文

### Motivation.

Speculators trains EAGLE-family, MTP, and DFlash drafters for vLLM but lacks Medusa, one of the most widely adopted speculative-decoding methods. Medusa (ICML 2024, [arXiv 2401.10774](https://arxiv.org/abs/2401.10774), `FasterDecoding/Medusa`) attaches K lightweight heads on the target's last hidden state to predict positions t+1..t+K in parallel. It runs natively in vLLM (`v1/spec_decode/medusa.py`, `{"method": "medusa"}`), TensorRT-LLM, and HF TGI.

Adding it lets users train Medusa heads here and deploy them straight to vLLM, and convert existing `FasterDecoding/Medusa` checkpoints.

### Proposed Change.

Add Medusa as a new speculator type. It has no draft transformer or recursive feedback, so it gets its own model/config rather than a flag:

1. **Model + config.** `MedusaDraftModel` / `MedusaSpeculatorConfig` (registered via `SpeculatorModel.register("medusa")` and `SpeculatorModelConfig.register("medusa")`): K residual MLP heads over the verifier's last hidden state, reusing `DraftVocabMixin` for the head vocab.
2. **Training.** Reuse the existing verifier-last-hidden-state pipeline (already extracted for eagle3/dflash); train heads with per-head loss against shifted targets (Medusa-1, frozen backbone).
3. **Converter.** Add a `MedusaConverter` for external `FasterDecoding/Medusa` checkpoints (remap head weights, build config from the verifier).
4. **vLLM parity.** Emit config compatible with vLLM's `{"method": "medusa"}` runtime so checkpoints deploy directly.

### Any Other Things.

Reference: Medusa, ICML 2024 — https://arxiv.org/abs/2401.10774

## 评论 (3)

### guan404ming · 2026-06-21

cc @fynnsu please help take a look, would be appreciate if you have any idea or suggestion about this. Thanks in advance!

### fynnsu · 2026-06-22

Hi @guan404ming, my understanding is that Medusa was largely superseded by approaches like Eagle-3. And now with even more modern methods like P-Eagle and DFlash, Medusa doesn't seem to be a super competitive algorithm. For that reason, I don't think it makes much sense to add this to speculators.

The challenge is that every algorithm we add must be maintained, tested regularly (we regularly run training regression tests), and updated whenever shared logic changes. More algorithms can also confuse users who aren't familiar with the space and aren't sure what the tradeoffs are.

We will continue to add new algorithms as the research community produces them, but it doesn't seem like there is a strong reason to add Medusa support at this stage. 

### guan404ming · 2026-06-23

Thanks @fynnsu, those are fair points. Agreed Medusa trails EAGLE-3/DFlash on standard benchmarks. A few reasons I'd still keep it on the table:

1. It fits some deployment constraints like edge deployment. with a frozen backbone and no separate draft model in memory, the head-only footprint can be worth it in latency- or memory-bound serving even if peak speedup is lower, and Hydra-style dependent heads recover much of the acceptance gap.
2. Implementation is relatively light. I think that it could reuses the `verifier-last-hidden-state` pipeline we already have for eagle3/dflash, so it's mostly K MLP heads + a config + a converter, no draft transformer or recursive feedback.
3. Main value is ecosystem reach. Native `{"method": "medusa"}` in vLLM/TRT-LLM/TGI, plus a converter for existing FasterDecoding/Medusa checkpoints.

No strong push, fine to skip if you'd rather keep the surface small. Appreciate for any suggestion!
