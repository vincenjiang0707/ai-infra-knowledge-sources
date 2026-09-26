# [Issue #2979] [Kimi-K3] Integrate KimiSparseMoeBlock with LinearExperts2D for REAP Support

source: https://github.com/vllm-project/llm-compressor/issues/2979
state: closed | updated: 2026-09-02T21:50:44Z
labels: enhancement, good first issue, moe

## 正文

## Background ##
The Kimi-K3 model definition currently uses `KimiSparseMoeBlock`, which does not integrate with LLM Compressor's `LinearExperts2D` class. This means the REAP algorithm cannot be applied to Kimi-K3 models, which is a significant missed opportunity for memory savings through expert pruning.

If `KimiSparseMoeBlock` is replaced with `LinearExperts2D`, the full REAP expert-removal flow becomes available for Kimi-K3 models.

## Proposed Changes ##
1. Follow the `inference-optimization/Kimi-K3-0.40B` model card to demonstrate loading the tiny version of the model using the `KimiK3ForConditionalGeneration` definition provided by LLM Compressor
2. Replace `KimiSparseMoeBlock` with `LinearExperts2D` in the model definition
3. Add a load mapping that maps weight names from the original `KimiSparseMoeBlock` class to the new `LinearExperts2D` class
4. Verify that the model can load with the new `LinearExperts2D` class and add a test to verify that outputs are the same before and after the replacement
5. Run the REAP algorithm on the tiny model to verify the end-to-end flow

## 评论 (3)

### kylesayrs · 2026-07-29

Assigned to @KKothuri

### Siraj637909 · 2026-08-14

@kylesayrs  is this issue still open .if  yes i will start working after get assigned


### kylesayrs · 2026-09-02

Closing this for now as blocked by 2994
