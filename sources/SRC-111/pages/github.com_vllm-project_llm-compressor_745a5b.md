source: https://github.com/vllm-project/llm-compressor

`llmcompressor`

is the fast, efficient, and easy-to-use library for optimizing models for deployment with vLLM, including:

- Comprehensive set of quantization algorithms and transforms for weight, activation, KV cache, and attention quantization
- Seamless integration with Hugging Face models and repositories
- Models saved in the
`compressed-tensors`

format, compatible with vLLM - DDP and disk offloading support for compressing very large models with hardware efficiency

**✨ Read the announcement blog here! ✨**

📊 Help us improve by taking our [1-minute user survey](https://red.ht/llm-compressor-user-survey)

💬 Join us on the [vLLM Community Slack](https://inviter.co/vllm-slack) and share your questions, thoughts, or ideas in:

`#sig-quantization`

`#llm-compressor`


Big updates have landed in LLM Compressor! To get a more in-depth look, check out the [LLM Compressor overview](https://docs.google.com/presentation/d/1WNkYBKv_CsrYs69lb7bJKjh2dWt8U1HXUw7Gr4Wn3gE/edit?usp=sharing).

Since the v0.13.0 release, a number of meaningful improvements have landed:

**Batched GPTQ quantization with a new Triton GPTQ kernel**: GPTQ now ships a Triton-based quantization kernel (~15x faster than the previous eager path) together with the ability to batch layers that share the same shape (up to ~1.67x per batch, roughly ~30x end-to-end on MoE workloads). Activation-order (act-order) calibration is supported, hessian offloading has been removed, and the remaining eager path was also sped up by 1.5-2x on its own.**Expanded MSE and iMatrix observers for FP4**: The MSE observer and the iMatrix observer gained a grid-search expansion factor that makes the search a strict superset of*fouroversix*(which chooses between the full`absmax`

and`absmax * 1.5`

scales for FP4 blocks). These observers outperform GPTQ for NVFP4 on average across our internal perplexity benchmarks.**Triton grid-search kernel for the MSE observer**: A Triton kernel now performs the MSE observer's scale grid search using buffered per-qparam patience and adaptive 512-value tiling. It reaches bitwise parity with the eager path when configured for full evaluation, supports INT, FP4, FP8, and FP16/BF16 (with E8M0 scales), and defaults`triton_error_buffer`

to 100% for FP4 and 30% otherwise.

The Red Hat AI team has been using LLM Compressor to produce a fresh batch of production-ready quantized checkpoints:

**GLM-5.3 MXFP4**: An MXFP4 quantized checkpoint for[GLM-5.3](https://huggingface.co/zai-org/GLM-5.3). The linear operators within the transformer blocks are quantized to MXFP4, while the MoE router, embeddings, DSA indexer, and output head are kept in their original precision to maintain accuracy recovery.**GLM-5.3-Flash NVFP4**: An NVFP4 quantized checkpoint for[GLM-5.3-Flash](https://huggingface.co/zai-org/GLM-5.3-Flash). The expert layers are quantized to NVFP4, while the MTP (multi-token prediction) layers are quantized to per-block FP8.**Qwen3.8-Flash-Next NVFP4**: An NVFP4 quantized checkpoint for[Qwen3.8-Flash-Next](https://huggingface.co/Qwen/Qwen3.8-Flash-Next).**Qwen3.8-27B INT4, NVFP4, and MXFP4**: 4-bit quantized checkpoints for[Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B)across three formats — INT4, NVFP4, and MXFP4 — covering a range of hardware and accuracy trade-offs.**Nemotron 3.5 Lightning FP8**: An FP8 quantized checkpoint for[Nemotron 3.5 Lightning](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-BF16), created using GPTQ-based FP8 quantization.**Qwen3.8-2.4T-A95B NVFP4, NVFP4+FP8, and REAP+NVFP4**: NVFP4 and NVFP4+FP8 quantized checkpoints for[Qwen3.8-2.4T-A95B](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B), along with`REAP-25`

and`REAP-50`

variants that combine[REAP](https://arxiv.org/pdf/2510.13999)expert pruning (25% and 50% of the least-salient experts pruned prior to quantization) with NVFP4, further reducing VRAM requirements while maintaining accuracy recovery.**Muse-Glimmer-30B FP8, NVFP4, and INT4**: FP8, NVFP4, and INT4 checkpoints for[Muse-Glimmer-30B](https://huggingface.co/meta-models/Muse-Glimmer-30B), enabling single-GPU deployment of this multimodal model.**Kimi-K3 NVFP4 and FP8**: NVFP4 and per-block FP8 quantized checkpoints for[Kimi-K3](https://huggingface.co/moonshotai/Kimi-K3). A native`KimiK3ForConditionalGeneration`

model definition is now shipped in the library to support quantizing this architecture.**Hy3 NVFP4+FP8**: A quantized checkpoint for[Hy3](https://huggingface.co/tencent/Hy3)combining NVFP4 quantization of the MoE layers with FP8 quantization of the attention layers, significantly reducing VRAM requirements while maintaining accuracy recovery.**GLM-5.2 NVFP4+FP8**: Mixed-precision quantized checkpoints for[GLM-5.2](https://huggingface.co/zai-org/GLM-5.2), created with DDP + disk offloading in under 2 hours. NVFP4 quantization of the MoE layers and FP8 quantization of the attention layers reduces the model size by >70% while maintaining state-of-the-art accuracy recovery on GPQA.

- Activation Quantization: W8A8 (int8 and fp8), W4AFP8, Microscale (NVFP4, MXFP4, MXFP8)
- Mixed Precision: W4A16, W8A16, MXFP8A16, MXFP4A16, NVFP4A16
- Attention and KV Cache Quantization: FP8, NVFP4
- Low/Arbitrary-bit Quantization: WNA4, WNA8, WNA16

- Simple PTQ
- GPTQ
- AWQ
- SmoothQuant
- AutoRound
- Rotation-based (SpinQuant, QuIP)
- REAP expert pruning

Please refer to our [step-by-step compression guide](https://docs.vllm.ai/projects/llm-compressor/en/latest/steps/choosing-model/) for detailed information about selecting quantization schemes, algorithms, and their use cases.

Additional information about LLM Compressor functionality is also available in our [User Guides](https://docs.vllm.ai/projects/llm-compressor/en/latest/guides/entrypoints/) and [FAQ](https://docs.vllm.ai/projects/llm-compressor/en/latest/faq/faq/).

`pip install llmcompressor`

Applying quantization with `llmcompressor`

:

[Activation quantization to](https://github.com/vllm-project/llm-compressor/blob/main/examples/quantization_w8a8_int8/README.md)`int8`

[Activation quantization to](https://github.com/vllm-project/llm-compressor/blob/main/examples/quantization_w8a8_fp8/README.md)`fp8`

[Activation quantization to MXFP8](https://github.com/vllm-project/llm-compressor/blob/main/examples/quantization_w8a8_mxfp8)[Activation quantization to](https://github.com/vllm-project/llm-compressor/blob/main/examples/quantization_w4a4_fp4)`fp4`

(NVFP4)[Activation quantization to](https://github.com/vllm-project/llm-compressor/blob/main/examples/quantization_w4a4_mxfp4)`fp4`

(MXFP4)[Activation quantization to](https://github.com/vllm-project/llm-compressor/blob/main/examples/autoround/quantization_w4a4_fp4/README.md)`fp4`

using AutoRound[Activation quantization to](https://github.com/vllm-project/llm-compressor/blob/main/examples/quantization_w4a8_fp8)`fp8`

and weight quantization to`int4`


[Weight only quantization to](https://github.com/vllm-project/llm-compressor/blob/main/examples/quantization_w4a16_fp4/nvfp4)`fp4`

(NVFP4 format)[Weight only quantization to](https://github.com/vllm-project/llm-compressor/blob/main/examples/quantization_w4a16_fp4/mxfp4)`fp4`

(MXFP4 format)[Weight only quantization to](https://github.com/vllm-project/llm-compressor/blob/main/examples/quantization_w4a16/README.md)`int4`

using GPTQ[Weight only quantization to](https://github.com/vllm-project/llm-compressor/blob/main/examples/awq/README.md)`int4`

using AWQ[Weight only quantization with AutoRound (](https://github.com/vllm-project/llm-compressor/blob/main/examples/autoround/quantization_wNa16/README.md)`wNa16`

)

[KV Cache quantization to](https://github.com/vllm-project/llm-compressor/blob/main/examples/quantization_kv_cache/README.md)`fp8`

[KV Cache quantization to](https://github.com/vllm-project/llm-compressor/blob/main/examples/quantization_kv_cache/llama3_fp8_head_kv_example.py)`fp8`

using per-head[Attention quantization to](https://github.com/vllm-project/llm-compressor/blob/main/examples/quantization_attention/README.md)`fp8`

[Attention quantization to](https://github.com/vllm-project/llm-compressor/blob/main/experimental/attention/README.md)`NVFP4`

with SpinQuant (experimental)

Let's quantize `Qwen3-30B-A3B`

with FP8 weights and activations using the `Round-to-Nearest`

algorithm.

Note that the model can be swapped for a local or remote HF-compatible checkpoint and the `recipe`

may be changed to target different quantization algorithms or formats.

Quantization is applied by selecting an algorithm and calling the `oneshot`

API.

```
from compressed_tensors.offload import dispatch_model
from transformers import AutoModelForCausalLM, AutoTokenizer
from llmcompressor import oneshot
from llmcompressor.modifiers.quantization import QuantizationModifier
MODEL_ID = "Qwen/Qwen3-30B-A3B"
# Load model.
model = AutoModelForCausalLM.from_pretrained(MODEL_ID)
tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)
# Configure the quantization algorithm and scheme.
# In this case, we:
# * quantize the weights to FP8 using RTN with block_size 128
# * quantize the activations dynamically to FP8 during inference
recipe = QuantizationModifier(
targets="Linear",
scheme="FP8_BLOCK",
ignore=["lm_head", "re:.*mlp.gate$"],
)
# Apply quantization.
oneshot(model=model, recipe=recipe)
# Confirm generations of the quantized model look sane.
print("========== SAMPLE GENERATION ==============")
dispatch_model(model)
input_ids = tokenizer("Hello my name is", return_tensors="pt").input_ids.to(
model.device
)
output = model.generate(input_ids, max_new_tokens=20)
print(tokenizer.decode(output[0]))
print("==========================================")
# Save to disk in compressed-tensors format.
SAVE_DIR = MODEL_ID.split("/")[1] + "-FP8-BLOCK"
model.save_pretrained(SAVE_DIR)
tokenizer.save_pretrained(SAVE_DIR)
```

The checkpoints created by `llmcompressor`

can be loaded and run in `vllm`

:

Install:

`pip install vllm`

Run:

```
from vllm import LLM
model = LLM("Qwen/Qwen3-30B-A3B-FP8-BLOCK")
output = model.generate("My name is")
```

- If you have any questions or requests open an
[issue](https://github.com/vllm-project/llm-compressor/issues)and we will add an example or documentation. - We appreciate contributions to the code, examples, integrations, and documentation as well as bug reports and feature requests!
[Learn how here](https://github.com/vllm-project/llm-compressor/blob/main/CONTRIBUTING.md).

If you find LLM Compressor useful in your research or projects, please consider citing it:

```
@software{llmcompressor2024,
title={{LLM Compressor}},
author={Red Hat AI and vLLM Project},
year={2024},
month={8},
url={https://github.com/vllm-project/llm-compressor},
}
```