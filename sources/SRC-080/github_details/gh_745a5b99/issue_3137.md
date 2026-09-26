# [Issue #3137] [Tests] Add example tests to cover `compress_xxx.py` scripts in compressed-tensors

source: https://github.com/vllm-project/llm-compressor/issues/3137
state: open | updated: 2026-09-10T16:17:19Z
labels: enhancement, good first issue, compressed-tensors, good follow-up issue

## 正文

**Is your feature request related to a problem? Please describe.**

Add tests to run and validate the examples under compressed-tensors, starting with all the scripts `compress_xxx.py` (should include 4 scripts) https://github.com/vllm-project/compressed-tensors/tree/main/examples

**Describe the solution you'd like**

The tests should run the examples, validate that it runs end-to-end and do basic sanity checks on the output product (i.e should include `safetensors` file, should include a config.json with the quantization_config correctly filed out). The tests should live in the compressed-tensors repo.


## 评论 (5)

### giovannicozzolongo · 2026-09-03

Hi, I'd like to take this. Could you assign it to me?

### therealruthvik · 2026-09-04

Hi @dsikka — I'm interested in this issue too.

My plan: add pytest cases under compressed-tensors/tests that run each compress_xxx.py example end-to-end and check for the safetensors file and a correctly populated config.json.

### dsikka · 2026-09-04

@giovannicozzolongo 

### dsikka · 2026-09-10

@giovannicozzolongo are you still interested in picking up this issue?

### giovannicozzolongo · 2026-09-10

Yes
