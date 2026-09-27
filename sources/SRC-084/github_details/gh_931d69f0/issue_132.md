# [Issue #132] No benefit from batch inference.

source: https://github.com/dropbox/hqq/issues/132
state: closed | updated: 2024-11-11T12:01:29Z
labels: 

## 正文

Hello, I’m testing the performance of the hqq quantization library in 4/8-bit quantization. For the original FP16 model, I also compiled the prefill and decoder separately. In my tests, 8-bit quantization showed no speed improvement across different batch sizes. Meanwhile, 4-bit quantization achieved about a 2-3x speedup over FP16 for a batch size of 1, but it became slower than FP16 as the batch size increased to 8/16/32/64. Throughout the process, the 8-bit quantization’s inference speed was almost the same as FP16. Could you help explain the reason for this?

## 评论 (4)

### mobicham · 2024-11-11

Hey, 

Yes that is expected, you need to make sure you use the right inference backend. The `torchao_int4` backend will significantly slow down with batch_sizes larger than 8 because it's a GEMV not GEMM. 
The 8-bit quantization in HQQ is not using any special backend, it's just using torch.compile, so you're not gonna see a large speed-up.

For faster batched inference for both 8-bit (A16W8) and 4-bit (A16W4), you need to use GemLite: https://github.com/mobiusml/gemlite/ as an inference backend. You should see significant speed-up for batched inference. 
I would also recommend you use this through GPTFast not transformers. 
Current master branched is optimized for ADA Gpus (4090 / A6000 Ada), we are currently working on improving perf for the A100 / H100.

For example, this is what you'd expect with the GemLite backend vs. the `torchao_int4` backend with GPTFast
![Llama3-8B Asymmetric (A16W4 - gs=64) - Decoding Speed (tokens _ sec)](https://github.com/user-attachments/assets/6e95f016-09ea-4747-89ba-cd80ca6ff72b)



### mobicham · 2024-11-11

The core hqq lib is just a quantization library, it just takes fp16 weights and produces a quantized version stored in `HQQLinear`.

In order to actually run the quantized model faster, we need to use optimized Triton/CUDA kernels at inference time, which are not directly implemented in the hqq lib. Since there are many different optimized kernels from different projects (BitBlas, TorchAO, GemLite, etc.), we swap the raw `HQQLinear` layer with the corresponding optimized layer based on the inference backend specified in the following call:
 
```Python
prepare_for_inference(model, backend='...')
```

For example, if you want to use GemLite, you'd first need to install it: 
`pip install git+https://github.com/mobiusml/gemlite.git`
Then here, you use `gemlite` as the backend:
```Python
from hqq.utils.patching import prepare_for_inference
prepare_for_inference(model, backend='gemllite', verbose=True)
```
Hope that answers the question!


### Emily-Ward · 2024-11-11

Oh, I see. Separating the backend's CUDA implementation from the quantization strategy is indeed a very flexible approach. Thank you very much for your help!

### mobicham · 2024-11-11

You're welcome! Let me know how it works out with `GemLite`. As I have mentioned earlier, performance right now is great on Ada GPUs, we are working on improving performance on the A100/H100. In any case, the current master version should already work much better than `torchao_int4` at batch_size > 8 (including the prefill phase).

