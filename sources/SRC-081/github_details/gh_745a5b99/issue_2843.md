# [Issue #2843] [Bug]: GPTQ modifier error in llm-compressor

source: https://github.com/vllm-project/llm-compressor/issues/2843
state: closed | updated: 2026-09-09T16:04:45Z
labels: bug

## 正文

### ⚙️ Your current environment

When I tried to quantize a Qwen-2.5-14B model using llm-compressor from FP16 to INT8-W8A8(SmoothQuant), it went all good but when I tried to serve it using VLLM, I received an error:

ValueError: {'actorder': static}

 (Note: I know the fix is updated in the ct latest version but just sharing the fixes that helped me)

### 🐛 Describe the bug

VLLM is not able to load the quantized model because the config consists of {actorder=True} because of GPTQ modifier and I have two simple solutions:

1) Just change in the config manually or through script ,{Actorder= False/None}  and try to serve it using VLLM and no issues.

2)It is because of ct , so try to upgrade the ct version and you don't face any issues and It will resolve the issue because the bug is resolved in the ct newer version and not updated in the latest version of vllm.

So, try to use these 2 fixes until we receive the newer version of vllm.


### 🛠️ Steps to reproduce

Quantize Qwen2.5-14B using llm-compressor with SmoothQuant W8A8.
Save the quantized model.
Try to serve the model using VLLM script or openai compatible endpoint
Observe the failure during model loading.

## 评论 (0)
