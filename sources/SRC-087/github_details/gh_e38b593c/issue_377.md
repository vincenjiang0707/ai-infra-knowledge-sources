# [Issue #377] Q2 Roadmap

source: https://github.com/vllm-project/speculators/issues/377
state: closed | updated: 2026-07-13T15:52:56Z
labels: keep-open, RFC, ROADMAP

## 正文

# Q2 Roadmap

## MTP Finetune Support
### Status:  Completed

RFC: https://github.com/vllm-project/speculators/issues/267

For models natively released with MTP layers, enable finetune support through Speculators with a desired dataset for potentially improved domain capabilities.

Issues: 
- [x] https://github.com/vllm-project/speculators/issues/273
- [x] https://github.com/vllm-project/speculators/issues/274
- [x] https://github.com/vllm-project/speculators/issues/275
- [x] https://github.com/vllm-project/speculators/issues/276

Related PRs:
1. https://github.com/vllm-project/speculators/pull/452
2. https://github.com/vllm-project/speculators/pull/474

## P-Eagle Training Support
### Status:  Completed

Enable e2e P-Eagle speculator training with Speculators.

RFC: https://github.com/vllm-project/speculators/issues/292

Related PRs:
1. https://github.com/vllm-project/speculators/pull/480
2. https://github.com/vllm-project/speculators/pull/554
3. https://github.com/vllm-project/speculators/pull/530


## Hardening new algorithmic training and finetune support
### Status: Completed

This includes ensuring that all training and finetune pathways are well integrated with the vLLM hidden state extraction system for online and offline data generation.

 - DFlash
 - P-Eagle Training Support 
 - MTP 

## Multi-Node Training Support
### Status: In Progress
Extending beyond FSDP support for end-to-end training support

RFC: https://github.com/vllm-project/speculators/issues/599
1. Offline Multi-Node Data Generation: https://github.com/vllm-project/speculators/pull/526

## Long context support
### Status: In Progress

Using sequence parallel Ulysses or other approaches to reduce memory usage on long context sequences/
- [x] Sliding Window Attention for DFlash: https://github.com/vllm-project/speculators/pull/523

## Training UX Updates
- Potentially unifying on a standardized CLI or Python API

## Next generation exploration and experimentation 

1. https://github.com/togethercomputer/aurora
2. https://arxiv.org/pdf/2512.15834#:~:text=Speculative%20decoding%20is%20an%20inference,proposed%20by%20Leviathan%20et%20al

## Buildkite CI / CD migration 
### Status: Completed

- [x] Migrate CI/CD to Buildkite 

## Legacy code pathway removal and refactoring 
### Status: Not Yet Started

- [ ] Removal of old model definition
- [ ] Potential clean-up / update to the model conversion pathway 

## New Trained Speculators
### DFlash

- Qwen3-8B: https://huggingface.co/RedHatAI/Qwen3-8B-speculator.dflash
- Laguna-XS2.2: https://huggingface.co/RedHatAI/Laguna-XS.2-speculator.dflash
- Gemma 4:  https://huggingface.co/RedHatAI/gemma-4-31B-it-speculator.dflash

### P-Eagle 
- Qwen3-8B: https://huggingface.co/RedHatAI/Qwen3-8B-speculator.peagle

## 评论 (1)

### dsikka · 2026-07-13

Closing this off. Please refer to: https://github.com/vllm-project/speculators/issues/781
