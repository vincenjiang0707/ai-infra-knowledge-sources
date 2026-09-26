# [Issue #1095] [Question] Is it recommended to use the same examples for SFT and QAT?

source: https://github.com/NVIDIA/Model-Optimizer/issues/1095
state: closed | updated: 2026-06-19T04:38:00Z
labels: question, stale, waiting for feedback, torch.quantization, triaged

## 正文

Quantizing a model to NVFP4. The model was SFT'd then RL fine-tuned. Planning to do QAT to recover accuracy after PTQ.                                            
                                                                                                                  
  Looking at `examples/llm_qat/`, the same Daring-Anteater dataset is used across all three steps (SFT → PTQ      
  calibration → QAT), just different splits. A few questions:                                                     
                                                                                                                  
  1. **Calibration vs QAT data** — Is using the exact same samples for both SFT and QAT fine-tuning         
  intentional/recommended, or just a simplification for the example?
                                                                                                                  
  2. **RL-tuned models** — My model's final training stage was RL, not SFT. Should QAT fine-tuning data    
  match the RL distribution (tool calls, reasoning traces, environment feedback), or the original SFT data, or
  does it not matter much?
                                                                                                                  
  ### Who can help?                                                                                             

  @kevalmorabia97 @sugunav14  

## 评论 (3)

### ChenhanYu · 2026-03-30

## Triage Analysis

| Field | Value |
|-------|-------|
| Classification | Question |
| Severity | Medium |
| Complexity | Simple |
| Auto-fixable | No |

### Summary
User is asking whether it's recommended to use the same dataset splits for both SFT and QAT fine-tuning, and whether QAT data should match the distribution of RL-tuned models or original SFT data. The issue seeks clarification on best practices for QAT workflows, particularly for models that have undergone RL fine-tuning rather than just SFT.

### Root Cause / Approach
The documentation and examples use a single dataset (Daring-Anteater) with different splits for calibration and QAT, which raises questions about whether this is optimal or merely a simplification. Additionally, there is no guidance on handling RL-tuned models, which have different data distributions than SFT models.

### Suggested Fix
1) Add explicit documentation in README.md clarifying whether calibration and QAT should use the same or different data distributions. 2) Provide guidance on QAT for RL-fine-tuned models, including whether to use RL-distribution data or original SFT data. 3) Consider adding an additional example or section demonstrating QAT with different dataset distributions. 4) Document empirical findings on accuracy trade-offs when using matching vs. different data splits.

### Relevant Files
- `examples/llm_qat/README.md`
- `examples/llm_qat/main.py`
- `examples/llm_qat/utils.py`
- `examples/llm_qat/simple_qat_train.py`
- `examples/llm_ptq/hf_ptq.py`
- `modelopt/torch/quantization/model_quant.py`
- `modelopt/torch/quantization/model_calib.py`

---
_Auto-triaged by pensieve `/magic-triage`_

### github-actions[bot] · 2026-06-05

Issue has not received an update in over 14 days. Adding stale label.

### github-actions[bot] · 2026-06-19

This issue was closed because it has been 14 days without activity since it has been marked as stale.
