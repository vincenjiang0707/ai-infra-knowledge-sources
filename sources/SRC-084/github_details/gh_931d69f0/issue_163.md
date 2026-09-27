# [Issue #163] set_vllm_onthefly_hqq_quant doesn't work vllm LLM v1 engine

source: https://github.com/dropbox/hqq/issues/163
state: closed | updated: 2025-09-29T00:43:27Z
labels: 

## 正文

I believe your gemlite and HQQ are excellent solutions in LLM. 

I would like to run the gemlite Triton code (specifically the MXFP8 code) in the vLLM engine v1, but I've found that it doesn't work properly. ([examples/vllm.py](https://github.com/mobiusml/hqq/blob/595e5cf665d8632f2f8f59493a3a8f17f6de897d/examples/vllm.py)'s set_vllm_onthefly_hqq_quant can convert vllm's linear layer but doesn't work vllm v1 engine.)

Do you have any additional methods or ideas to solve this? 



## 评论 (3)

### mobicham · 2025-09-28

Hi, thank ou! 

It does work, you just need to patch it the right way because V1 is using spawn mode. So you either need to patch it in the engine launch code or you launch it before the main function if you are using python code to interact with a vLLM LLM instance, see https://github.com/mobiusml/hqq/issues/152 
This logic applies to any patching applied to vLLM, it's not related to how hqq/gemlite work.

### mobicham · 2025-09-28

Also note that for MXFP8, you'll need custom Triton build for sm_120, because it's still work in progress. The gemlite implementation fpr MXFP is for sm_120 mainly, it's not optimized for sm_100 (B200).

### pdh930105 · 2025-09-29

Thank you for your quick response.

It was successful!
