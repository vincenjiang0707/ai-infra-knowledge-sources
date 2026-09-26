# [Issue #149] High Latency in _generate_code_from_prompt Function: Tens of Minutes vs Expected 3 Minutes per Kernel (DeepSeek-v3.2-reasoner)

source: https://github.com/flashinfer-ai/flashinfer-bench/issues/149
state: open | updated: 2026-01-26T01:07:18Z
labels: 

## 正文

### Description
I'm testing kernel generation with the `deepseek-v3.2-reasoner` model, and I've observed a significant latency discrepancy:
- **Expected/Reference Time**: Generating a response for a single kernel takes approximately 3 minutes (tested in standalone `deepseek-v3.2-reasoner` mode).
- **Actual Time in Code**: The `_generate_code_from_prompt` function in the codebase takes **tens of minutes** to complete, which is far longer than expected.

### Environment
- Hardware: 8-GPU server (used for workload testing)
- Model: deepseek-v3.2-reasoner
- Codebase: FlashInfer-bench (kernel generator module)

### Questions
1. Why is the `_generate_code_from_prompt` function taking so much longer than the standalone model inference?
2. Does this function perform additional operations beyond just calling the LLM API to generate code (e.g., post-processing, retries, additional validation, or resource contention)?
3. Could the 8-GPU setup be causing resource contention or misconfiguration that leads to this latency?

### Additional Context
I'm running the standard kernel generation script (the example script provided in the repo) with no custom modifications other than setting the correct API key and trace path. 

Any insights into the function's internal logic or potential optimization points would be greatly appreciated!

## 评论 (2)

### Ubospica · 2026-01-20

@OwenVigil Thanks for your issue. We also used 8-gpu setup in testing, so that should be fine. It just parses the output from LLMs, without any retry/resource allocation logic. 

Could you provide further time breakdown? We are happy to help investigate it.

### OwenVigil · 2026-01-26


@Ubospica Thanks for yout reply. After tracking, we found though we took 38h to generate and track for kernels without sampling, it was the high latency due to deepseek-v3.2 producing tockens.  Such as for gqa_ragged_prefill_causal_h32_kv8_d128, we spent 834S
