# [Issue #2693] [Bug]: `compressed-tensors` W4A8 INT (int4 weights + int8 activations) fails to find any compatible kernel on H100

source: https://github.com/vllm-project/llm-compressor/issues/2693
state: closed | updated: 2026-08-18T17:16:56Z
labels: bug

## 正文

### ⚙️ Your current environment

<details>
<summary>The output of <code>python collect_env.py</code></summary>

```text
### Environment Information ###
Operating System: `Linux-5.15.0-119-generic-x86_64-with-glibc2.39`
Python Version: `3.10.20 (main, Apr 14 2026, 14:28:08) [Clang 22.1.3 ]`
llm-compressor Version: `0.10.0.2`
compressed-tensors Version: `0.14.0.1`
transformers Version: `4.57.6`
torch Version: `2.11.0`
CUDA Devices: `['NVIDIA H100 80GB HBM3', 'NVIDIA H100 80GB HBM3', 'NVIDIA H100 80GB HBM3', 'NVIDIA H100 80GB HBM3', 'NVIDIA H100 80GB HBM3', 'NVIDIA H100 80GB HBM3', 'NVIDIA H100 80GB HBM3', 'NVIDIA H100 80GB HBM3']`
AMD Devices: `None`
NPU Devices: `None`
```

</details>


### 🐛 Describe the bug

When loading a model quantized to W4A8 INT (int4 channel-wise symmetric weights + int8 per-token dynamic activations) via `compressed-tensors`, vLLM fails during model initialization with `ValueError: Failed to find a kernel that can implement the WNA16 linear layer`. All available kernels reject the configuration.

vLLM should successfully load the W4A8 INT quantized model and serve it, or at least provide a clear error message indicating that this quantization format is not supported.

EngineCore crashes during model loading with the following kernel selection failure:
`ValueError: Failed to find a kernel that can implement the WNA16 linear layer. Reasons: 
  CutlassW4A8LinearKernel cannot implement due to: CUTLASS W4A8 only supports FP8 (e4m3) activations
  MacheteLinearKernel cannot implement due to: Quant type (int4) not supported by Machete, supported types are: [ScalarType.uint4b8, ScalarType.uint8b128]
  AllSparkLinearKernel cannot implement due to: AllSpark currently does not support device_capability = 90.
  MarlinLinearKernel cannot implement due to: Quant type (int4) not supported by Marlin, supported types are: [ScalarType.uint4b8, ScalarType.uint8b128, ScalarType.float8_e4m3fn, ScalarType.float4_e2m1f]
  ConchLinearKernel cannot implement due to: Weight type (int4) not supported by ConchLinearKernel, supported types are: [ScalarType.uint4, ScalarType.uint8, ScalarType.uint4b8, ScalarType.uint8b128]
  ExllamaLinearKernel cannot implement due to: Exllama only supports float16 activations`

### 🛠️ Steps to reproduce

**1. Quantization script (form llm-compressor example https://github.com/vllm-project/llm-compressor/blob/main/examples/quantization_w4a8/gpt_oss_20b_example.py):**
```python
import torch
from compressed_tensors.quantization import QuantizationScheme
from compressed_tensors.quantization.quant_args import (
    QuantizationArgs, QuantizationStrategy, QuantizationType,
)
from transformers import AutoModelForCausalLM, AutoTokenizer
from llmcompressor import oneshot
from llmcompressor.modifiers.quantization import QuantizationModifier
from llmcompressor.modeling.gpt_oss import convert_model_for_quantization_gptoss

MODEL_ID = "/vllm-workspace/Projects/models/gpt-oss-20b"

model = AutoModelForCausalLM.from_pretrained(
    MODEL_ID,
    torch_dtype=torch.bfloat16,
    device_map="auto",
    trust_remote_code=True,
)
tokenizer = AutoTokenizer.from_pretrained(MODEL_ID, trust_remote_code=True)
convert_model_for_quantization_gptoss(model)

weights_args = QuantizationArgs(
    num_bits=4,
    type=QuantizationType.INT,
    strategy=QuantizationStrategy.CHANNEL,
    symmetric=True,
    dynamic=False,
)

activations_args = QuantizationArgs(
    num_bits=8,
    type=QuantizationType.INT,
    strategy=QuantizationStrategy.TOKEN,
    symmetric=False,
    dynamic=True,
    observer=None,
)

scheme = QuantizationScheme(
    targets=["Linear"],
    weights=weights_args,
    input_activations=activations_args,
)

recipe = QuantizationModifier(
    config_groups={"group_0": scheme},
    ignore=["lm_head"],
)

oneshot(
    model=model,
    recipe=recipe,
    tokenizer=tokenizer,
    output_dir="gpt-oss-20b-w4a8-channelwise",
    trust_remote_code_model=True,
)
```

**2. vLLM serve command:**

```bash
export CUDA_VISIBLE_DEVICES=0,1,2,3

MODEL_NAME="/vllm-workspace/Projects/models/gpt-oss-20b-w4a8-channelwise"
LOG_NAME="run_server_$(date +%Y%m%d_%H%M%S).log"

vllm serve "$MODEL_NAME" \
    --trust-remote-code \
    --pipeline-parallel-size 1 \
    --tensor-parallel-size 1 \
    --port 30000 \
    |& tee "$LOG_NAME"
```

log please check [run_server_20260510_044436.log](https://github.com/user-attachments/files/27562815/run_server_20260510_044436.log)
quant relate config [recipe.yaml](https://github.com/user-attachments/files/27562861/recipe.yaml) [config.json](https://github.com/user-attachments/files/27562862/config.json)


## 评论 (5)

### brian-dellabetta · 2026-05-13

Hi @RedHeartSecretMan , each kernel is configured for very specific usage. You can see in the error logs why a compatible kernel couldn't be found. Can you try with either of [these two preset schemes](https://github.com/vllm-project/compressed-tensors/blob/main/src/compressed_tensors/quantization/quant_scheme.py#L310-L346) and see if that resolves your issue?

### RedHeartSecretMan · 2026-05-17

This is extremely frustrating. I am following the official llmcompressor example `quantization_w4a8/gpt_oss_20b_example.py` on H100, the industry's flagship GPU for FP8/INT8 inference. Yet the entire official pipeline is fundamentally broken for GPT-OSS 20B.

After the [these two preset schemes](https://github.com/vllm-project/compressed-tensors/blob/main/src/compressed_tensors/quantization/quant_scheme.py#L310-L346) switching to preset GROUP schemes, I hit a dead end:
group_size=128 fails during quantization because GPT-OSS 20B's MoE expert dimensions (2880) are not divisible by 128.
group_size=64 allows quantization to complete, but vLLM hard-rejects it at load time with:

`ValueError: W4A8 kernels require group quantization with group size 128`

The official example, running on mainstream H100 hardware, produces a model that is impossible to serve. This is not a user-side misconfiguration—this is a critical compatibility gap between two officially maintained components (llmcompressor examples and the vLLM W4A8 kernel backend). Users should not be used as integration testers for broken official examples.

Please escalate this immediately. The official example must be urgently removed or annotated as incompatible with GPT-OSS 20B. Shipping a non-functional official example on flagship hardware is unacceptable.

### brian-dellabetta · 2026-05-20

Hi @RedHeartSecretMan , sorry i missed that you were using the scheme provided in the example. It fails for me as well, will raise this internally

### brian-dellabetta · 2026-05-20

Spoke internally, the example was added with the goal of eventual support in vllm, but there is no pathway to run gpt oss models in vllm in any quantization format other than its original mxfp4 format. Will open a PR to remove this example.

Sorry about that. You can stick to the original checkpoint

### Tobi-Adesoye · 2026-06-15

The kernel dispatch failure here is almost certainly a stride misalignment during the shape contract. When packing Int4 weights against Int8 activations, the low-bit quantization matrices force un-aligned shapes into the CUDA shared memory tiles. If the activation tensors are not strictly contiguous or use irregular sequence-length padding, the Triton/CUDA compilation wrapper rejects the shapes because they don't map cleanly to the physical Warp Matrix Multiply and Accumulate (WMMA) layout on the Hopper architecture.

A drop-in way to secure these boundary layouts before they hit the kernel compiler is using a hardware-aware fallback wrapper like renorm-native to flatten and anchor the tensor layout parameters dynamically
