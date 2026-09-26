# [Issue #1063] [RFC]: Add Qwen3-ASR audio-conditioned speculator training support

source: https://github.com/vllm-project/speculators/issues/1063
state: open | updated: 2026-09-14T19:04:24Z
labels: RFC

## 正文

### Motivation.

Speculators supports multimodal dataset preprocessing and Qwen3-VL workflows, but it does not currently provide a documented and tested end-to-end training path for audio-language models such as Qwen3-ASR.

Qwen3-ASR contains a Qwen3 language model behind an audio encoder. Training a post-hoc draft model requires preserving the original audio request while the frozen verifier performs audio preprocessing, audio-tower inference, and language-model inference. The resulting expanded token IDs, loss mask, and audio-conditioned decoder hidden states can then use the standard Speculators training contract.

I have a working out-of-tree prototype validated with:

- Qwen/Qwen3-ASR-0.6B-hf
- Qwen/Qwen3-ASR-1.7B-hf
- EAGLE-3, DFlash, and P-EAGLE
- offline cached hidden states and online hidden-state generation
- multi-GPU DDP training
- vLLM speculative serving and ASR evaluation

 After training on LibriSpeech 960h, Qwen3-ASR-1.7B speculators increased single-H100 throughput at concurrency 8 by 51.9% for EAGLE-3, 93.2% for DFlash, and 59.0% for P-EAGLE over dense decoding.

### Proposed Change.

I propose adding Qwen3-ASR as the audio counterpart to the existing Qwen3-VL training integration. It should reuse the shared multimodal pipeline rather than introduce a separate ASR trainer.

The implementation would:

1. Support audio paths and URLs in the existing multimodal conversation format, with the transcription stored in the assistant turn.

2. Preserve the original audio messages throughout data preparation and hidden-state generation. vLLM remains responsible for chat-template rendering, audio decoding, feature extraction, placeholder expansion, audio-tower execution, and verifier inference.

3. Use vLLM as the authoritative source of expanded token IDs and strictly validate alignment between token IDs, loss masks, auxiliary hidden states, and final hidden states before training.

4. Reuse the existing generic `text_config` and nested-weight resolution for the Qwen3 decoder. Core Speculators code should remain capability-based and modality-generic, without scattered `model_type == "qwen3_asr"` branches.

5. Keep the Qwen3-ASR verifier and audio tower frozen. EAGLE-3, DFlash, P-EAGLE, and DSpark continue consuming the standard Speculators tensor contract through the existing online, offline, hybrid, and distributed training workflows.

6. Add generic audio preprocessing and alignment tests, a Qwen3-ASR online/offline end-to-end smoke test, and a small documented training example analogous to the current Qwen3-VL coverage.

### Any Other Things.

I have a working prototype and would be happy to implement this contribution. If this scope and architecture look appropriate, please assign the issue to me.

## 评论 (2)

### MatthewCYM · 2026-09-13

Hi @shanjiaz @fynnsu, following up on this RFC. Would Qwen3-ASR training support fit the project’s direction? I’m happy to open a draft PR for review. Thanks!

### shanjiaz · 2026-09-14

@MatthewCYM Thanks for reaching out! Yes we're generally welcoming of new features. Please feel free to open up PR and we can work out a way to land this if it's not too invasive. Thank you!
