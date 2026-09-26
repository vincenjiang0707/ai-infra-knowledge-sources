# [Issue #12] How difficult will adding Llama 3 support be?

source: https://github.com/LLMServe/DistServe/issues/12
state: open | updated: 2024-06-15T04:37:57Z
labels: enhancement

## 正文

Hey, love the work you guys have done on DistServe and SwiftTransformer. As far as I can tell it supports Llama-2. How hard will adding Llama-3 models be? I specifically want support for https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct.

Any guidance will be really helpful. Thanks!

## 评论 (8)

### interestingLSY · 2024-06-13

Technically there shouldn't be any issues I think, since that LLaMA-3 has no architectural difference from LLaMA-2. Will try to add that tomorrow.

### kalradivyanshu · 2024-06-13

Thank you for your prompt response! I am broadly interested in having support for more models in DistServe like Phi-3, in general can you tell me what all steps will I have to take to add a new model into DistServe?
Further-more can I have a DistServe server running that has multiple models loaded? And then I add which model I want to infer in the infer request? (like how triton, vllm support multiple models)

### interestingLSY · 2024-06-14

Thank you a lot for your attention and enthusiasm for this project.

The architecture of DistServe can be divided into two parts: the control plane, and the data plane. The former one is responsible for deciding "which request to serve" and is where we implement our "disaggregation" idea, and the latter one performs calculations. This repo contains code for the control plane. For the data plane, in order to achieve the state-of-the-art (SOTA) performance, DistServe utilizes a pure C++/CUDA implementation, [SwiftTransformer](https://github.com/LLMServe/SwiftTransformer).

Generally speaking, the following steps are necessary for adding support for a new model:

- For the control plane, there might be misc stuffs to modify in `ModelConfig` in `distserve/config.py`, and `distserve/tokenizer.py`.
- For the data plane, you may need to add new kernels/layers/model classes into SwiftTransformer, if the architecture of the model is different from OPT/LLaMA/GPT2. Besides, since DistServe need to convert the model weights to a special format before loading, you may also need to modify `distserve/downloader/converter.py`.

If you wish to support a model that has exactly the same architecture as LLaMA2, congratulations, you can just replace `model_type` in the model's `config.json` (you should have that after downloading from HuggingFace) to `llama` and it will work.

Frankly speaking, I am not really satisfied with DistServe's current implementation of the data plane. Despite delivering high performance (up to ~5% speedup compared to PyTorch version on small models (7b), and ~1% speedup on large models), the pure C++/CUDA implementation is hard to develop and maintain. Besides, this creates a barrier between DistServe and the whole ecosystem, e.g., we cannot use operator and kernels from PyTorch or OpenAI Triton, or it takes much effort to add support for a new model. A better solution could be leveraging PyTorch with OpenAI Triton, which achieves nearly equivalent performance while reducing the LoC (line-of-code) of the data plane by 10x compared to SwiftTransformer. [SwiftLLM](https://github.com/interestingLSY/swiftLLM) uses this approach.

Currently DistServe does not support serving multiple models simultaneously. A workaround could be to start multiple DistServe instances.


### kalradivyanshu · 2024-06-14

Oh wow, thank you for such a detailed reply. How mature is SwiftLLM? I briefly went through its code, and I can see you have added things like KV cache swap and separate prefill and decode stages, so I am guessing the plan is to eventually swap SwiftTransformer with SwiftLLM in DistServe? How much more work is needed for this to happen?

Thank you for all your hard work!

### interestingLSY · 2024-06-14

> Oh wow, thank you for such a detailed reply. How mature is SwiftLLM? I briefly went through its code, and I can see you have added things like KV cache swap and separate prefill and decode stages, so I am guessing the plan is to eventually swap SwiftTransformer with SwiftLLM in DistServe? How much more work is needed for this to happen?
> 
> Thank you for all your hard work!

I just throw SwiftLLM as an example of using PyTorch + Triton... SwiftLLM is currently able to launch an API server and perform online serving, but currently we have no plan of migrating DistServe to SwiftLLM

### kalradivyanshu · 2024-06-14

Oh ok. How hard will it be to separate prefill stage and decode stage to separate GPUs in SwiftLLM? My main thing is I think it will be easier to add new models,  make changes in SwiftLLM. And I do want a DistServe style segregation of prefill and decode. Any tips on how I should proceed will be appreciated, thanks!

### interestingLSY · 2024-06-14

I have just checked that DistServe should be able to serve LLaMA3 without any modifications on code. Due to restrictions proposed by Meta, I cannot access to `meta-llama/Meta-Llama-3-8B` so I ran DistServe on `SchizoDev/Llama3-8b-CunnyGPT-16bit` and everything works fine. It should support `meta-llama/Meta-Llama-3-8B` as long as Meta provides `pytorch_model.bin` or a series of `pytorch_model-XXXXX-of-XXXXX.bin.`s (safetensors format is not supported yet).

### KylinC · 2024-06-15

Is this system now support LLaMA-1 architecture? 
