# [Issue #2699] [Help Wanted] Transformers Load of 3D Packed MoE Checkpoints

source: https://github.com/vllm-project/llm-compressor/issues/2699
state: closed | updated: 2026-09-23T05:42:18Z
labels: good follow-up issue, qwen, moe

## 正文

Hi, I want to export onnx model from llmcompressor quantized model. Our onnx export tool relies on "huggingface transformers", so it would be very helpful if quantized model can be loaded by hf transformers.  I got a few questions about "moe calibration design" in llmcompressor.

Some model such as glm_moe_dsa set "is_permanent = True". After quantization, can this model be properly loaded by huggingface transfomrers? (my attempts failed because of missing weight and unexpected weight)
If I want to restore the original structure of a quantized model (such as glm_moe_dsa), what should I do? According to my understanding, models such as glm_moe_dsa and qwen3.5_moe have changed the model structure when replacing MoE with CalibrationMoE (It can also be said that a new weight layer or tensor is created). This means that simply returning "origin" in the restore function is not feasible, because "origin" does not include information such as "scales" and "zero point". Is there an example of llmcompressor correctly restoring the original structure after such modifications?

## 评论 (6)

### brian-dellabetta · 2026-05-13

Hi @Sekri0 , no I don't think there's an easy way to do this. We generally only support running llmcompressor quantized models on vllm, which doesn't have onnx support

Can you explain your use case a bit more? What are you hoping to do with the onnx-exported model?

### Sekri0 · 2026-05-14

Deploy LLM on NPU chip needs onnx-exported model. We have a LLM-onnx-export tool, which is dependent on hf transformers ecosystem. This means if a model can be loaded by hf transformers, we can get onnx-model with little efforts. My goal is to load a llmcompressor-quanted model using hf transforms. Therefore, I can easily export an quanted onnx model, which has the same accuracy with llmcompressor quanted model. 
According to my attemptation, models whose structures remain unchanged after quantization can be loaded correctly by hf transformers. But I still encounter issues when loading models such as qwen3.5_moe and glm_moe_dsa due to model structure miss match.

### brian-dellabetta · 2026-05-14

Got it, thanks for the information. I'm surprised llm-compressor compressed models work in onnx. We wrap the huggingface transformers logic to run "fake quantized" forward passes, i.e. convert the bfloat16 values to what they would be in quantized format while retaining the bfloat16 dtype. This is not at all performant, but provides a dev pathway needed during compression. Do you see speedups in onnx? Custom logic is needed to unpack parameters to be used with performant kernels, like in vllm and in llm-compressor's MoE calibration context.

As a way to reduce our maintenance surface area, we try to funnel all users into vllm. Have you looked into the [vllm ascend plugin](https://docs.vllm.ai/projects/ascend/en/v0.13.0/)? This is the recommended approach for vllm on ascend NPU devices.

### kylesayrs · 2026-07-14

Hey @Sekri0!

`glm_moe_dsa` is an architecture where the checkpoint has 2d weights typically, so in this case the model should load without issue. I believe that @KKothuri has validated that this loads in transformers with `inference-optimization/GLM-5.2-0.8B-A0.8B`.

As for architectures which pack expert weights such as `qwen3_vl_moe`, LLM Compressor typically leaves these as linearized experts, so you're right that model loading wouldn't work.

The long term plan is to add [backwards_mappings](https://github.com/vllm-project/llm-compressor/blob/7e2c6bfefd9d844c8a5c9852baa49f550f312ede/src/llmcompressor/modeling/moe/linearize.py#L57-L60) which are used during model saving. For `qwen3_vl_moe`, the backwards mappings would repack the weights (and qparams) into 3d tensors, thus preserving the original checkpoint format.

If you @Sekri0, @GOavi101 or any others are interested in helping to contribute to this I can help collaborate.

### GOavi101 · 2026-07-14

i am interested @kylesayrs... you can assign it to me

### kylesayrs · 2026-09-23

Loading 3d packed weights with quantization is not supported by huggingface. Until that support is added, you can only load models in HF if they are already 2d using a script similar to this:

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
from llmcompressor.utils import load_context

model_id = "inference-optimization/ZAYA1-74B-preview-NVFP4-linear"
with load_context():
    model = AutoModelForCausalLM.from_pretrained(model_id, device_map="auto")
tokenizer = AutoTokenizer.from_pretrained(model_id)

input_ids = tokenizer("According to all known laws", return_tensors="pt").input_ids.to(model.device)
output = model.generate(input_ids, max_new_tokens=20)
print(tokenizer.decode(output[0]))
```

See `inference-optimization/ZAYA1-74B-preview-NVFP4` for more context
