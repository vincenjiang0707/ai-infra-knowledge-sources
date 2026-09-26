source: https://docs.vllm.ai/en/latest/features/quantization/quantized_kvcache/
lastmod: 2026-09-24

# Quantized KV Cache[¶](https://docs.vllm.ai#quantized-kv-cache)

## FP8 KV Cache Overview[¶](https://docs.vllm.ai#fp8-kv-cache-overview)

Efficient memory usage is crucial for working with large language models. Quantizing the KV (Key-Value) cache to FP8 format can significantly reduce its memory footprint. This optimization enables you to store more tokens in memory, leading to improved throughput and support for longer context windows.


Note:When using the Flash Attention 3 backend with FP8 KV cache, attention operations are also performed in the quantized (FP8) domain. In this configuration, queries are quantized to FP8 in addition to keys and values.

### Supported FP8 KV-Cache Quantization Schemes[¶](https://docs.vllm.ai#supported-fp8-kv-cache-quantization-schemes)

vLLM supports two main quantization strategies for the FP8 KV-cache:

**Per-tensor quantization:**

A single scale is applied for each Q, K, and V tensor individually. (`q/k/v_scale = [1]`

)**Per-attention-head quantization:**

Each scale corresponds to an attention head:`q_scale = [num_heads]`

,`k/v_scale = [num_kv_heads]`

.


Note:

Per-attention-head quantization is currently availableonly with the Flash Attention backendand requires the calibration pathway provided byllm-compressor.

### Scale Calibration Approaches[¶](https://docs.vllm.ai#scale-calibration-approaches)

You can configure how the quantization scales are computed in vLLM using three different approaches:

-
**No calibration (default scales):**

All quantization scales are set to`1.0`

.

*Configure with:*

-
**[Recommended] Calibration with a dataset (via llm-compressor):**

Scales are estimated using a curated calibration dataset for maximum accuracy.

This requires the[llm-compressor](https://github.com/vllm-project/llm-compressor)library.

*See example below!*

#### Additional `kv_cache_dtype`

Options[¶](https://docs.vllm.ai#additional-kv_cache_dtype-options)

`kv_cache_dtype="auto"`

: Use the model's default data type`kv_cache_dtype="fp8_e4m3"`

: Supported on CUDA 11.8+ and ROCm (AMD GPUs)`kv_cache_dtype="fp8_e5m2"`

: Supported on CUDA 11.8+

### Skipping Specific Layers from KV-Cache Quantization[¶](https://docs.vllm.ai#skipping-specific-layers-from-kv-cache-quantization)

Some attention layer types (e.g. sliding-window) are more sensitive to KV-cache quantization. The `--kv-cache-dtype-skip-layers`

flag leaves the specified layers at the model's native dtype while keeping the rest of the layers under the chosen quantized dtype. The flag accepts either layer indices or layer-type names:

# Skip every sliding-window attention layer.
vllm serve <model> \
--kv-cache-dtype fp8 \
--kv-cache-dtype-skip-layers sliding_window
# Skip specific layer indices.
vllm serve <model> \
--kv-cache-dtype fp8 \
--kv-cache-dtype-skip-layers 0 1 23


Programmatic usage:

llm = LLM(
model="meta-llama/Llama-3.1-8B-Instruct",
kv_cache_dtype="fp8",
kv_cache_dtype_skip_layers=["sliding_window"],
)


## Examples[¶](https://docs.vllm.ai#examples)

### 1. No Calibration (`kv_cache_dtype="fp8"`

)[¶](https://docs.vllm.ai#1-no-calibration-kv_cache_dtypefp8)

All quantization scales are set to 1.0.

from vllm import LLM, SamplingParams
sampling_params = SamplingParams(temperature=0.7, top_p=0.8)
llm = LLM(
model="meta-llama/Llama-2-7b-chat-hf",
kv_cache_dtype="fp8",
)
prompt = "London is the capital of"
out = llm.generate(prompt, sampling_params)[0].outputs[0].text
print(out)


### 2. **[Recommended] Calibration Using a Dataset (with **`llm-compressor`

)[¶](https://docs.vllm.ai#2-recommended-calibration-using-a-dataset-with-llm-compressor)

`llm-compressor`

)For the highest-quality quantization, we recommend calibrating against a dataset using `llm-compressor`

. This enables advanced strategies such as per-attention-head quantization.

#### Install the required package[¶](https://docs.vllm.ai#install-the-required-package)

#### Example: Quantize Llama Attention & KV Cache to FP8[¶](https://docs.vllm.ai#example-quantize-llama-attention-kv-cache-to-fp8)

"""
Quantize Llama attention + KV cache to FP8 (choose either 'tensor' or 'attn_head' strategy)
using llm-compressor one-shot calibration.
"""
from datasets import load_dataset
from transformers import AutoModelForCausalLM, AutoTokenizer
from llmcompressor import oneshot
from llmcompressor.modifiers.quantization import QuantizationModifier
from compressed_tensors.quantization import QuantizationScheme, QuantizationArgs
# -----------------------------
# Config
# -----------------------------
MODEL_ID = "meta-llama/Llama-3.1-8B-Instruct"
DATASET_ID = "HuggingFaceH4/ultrachat_200k"
DATASET_SPLIT = "train_sft"
STRATEGY = "tensor" # or "attn_head"
NUM_CALIB_SAMPLES = 512 # Good starting value
MAX_SEQ_LEN = 2048
# -----------------------------
# Helpers
# -----------------------------
def process_and_tokenize(example, tokenizer: AutoTokenizer):
"""Convert chat messages to tokens."""
text = tokenizer.apply_chat_template(example["messages"], tokenize=False)
return tokenizer(
text,
padding=False,
max_length=MAX_SEQ_LEN,
truncation=True,
add_special_tokens=False,
)
def build_recipe(strategy: str) -> QuantizationModifier:
fp8_args = QuantizationArgs(num_bits=8, type="float", strategy=strategy)
return QuantizationModifier(
config_groups={
"attention": QuantizationScheme(
targets=["LlamaAttention"], # Quantize queries: q_scale
input_activations=fp8_args,
)
},
kv_cache_scheme=fp8_args, # Quantize KV cache: k/v_scale
)
# -----------------------------
# Main
# -----------------------------
def main():
model = AutoModelForCausalLM.from_pretrained(MODEL_ID, torch_dtype="auto")
tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)
ds = load_dataset(DATASET_ID, split=f"{DATASET_SPLIT}[:{NUM_CALIB_SAMPLES}]")
ds = ds.shuffle(seed=42)
ds = ds.map(
lambda ex: process_and_tokenize(ex, tokenizer),
remove_columns=ds.column_names,
)
recipe = build_recipe(STRATEGY)
oneshot(
model=model,
dataset=ds,
recipe=recipe,
max_seq_length=MAX_SEQ_LEN,
num_calibration_samples=NUM_CALIB_SAMPLES,
)
save_dir = f"{MODEL_ID.rstrip('/').split('/')[-1]}-kvattn-fp8-{STRATEGY}"
model.save_pretrained(save_dir, save_compressed=True)
tokenizer.save_pretrained(save_dir)
if __name__ == "__main__":
main()


For more detailed and up-to-date examples, see the [ llm-compressor official examples](https://github.com/vllm-project/llm-compressor/tree/main/examples/quantization_kv_cache).