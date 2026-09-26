# [Issue #2230] Add nightly performance benchmark for guides/multimodal-serving

source: https://github.com/llm-d/llm-d/issues/2230
state: closed | updated: 2026-09-03T22:55:31Z
labels: 

## 正文

As llmd continues to evolve, it is critical that we monitor the performance of our core use cases to catch any potential regressions early.

Currently we don't have a nightly benchmark running against the multimodal-serving guide (guides/multimodal-serving). We need to implement a dedicated nightly benchmark for this specific guide to ensure our multimodal capabilities remain performant.

Goal:
Set up an automated nightly benchmark for the multimodal-serving guide to track performance metrics over time and alert the team to any performance degradation.

Acceptance Criteria:

[ ] Verify the current status of nightly benchmarks for existing multimodal serving guides.

[ ] Create a benchmark test suite specifically for the guides/multimodal-serving implementation.

[ ] Integrate the benchmark into the nightly CI/CD pipeline.

[ ] Ensure benchmark results are logged and any significant performance degradation triggers an alert.

## 评论 (3)

### capri-xiyue · 2026-08-10

cc @rlakhtakia 

### rlakhtakia · 2026-08-10

/assign

### capri-xiyue · 2026-09-03

Hi @rlakhtakia, do you know why
GPU Aggregation: nightly-e2e-multimodal-serving-aggregation-gke-acc-gpu-vllm-x.yaml
GPU E-Disaggregation: nightly-e2e-multimodal-serving-e-disaggregation-gke-acc-gpu-vllm-x.yaml
doesn't show in https://github.com/llm-d/llm-d/blob/main/release/README.md?
