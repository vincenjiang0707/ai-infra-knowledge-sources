# [Issue #2730] [Bug]: Mix-precision vLLM loading failure (MXFP4+MXFP8)

source: https://github.com/vllm-project/llm-compressor/issues/2730
state: closed | updated: 2026-07-28T17:03:10Z
labels: bug

## 正文

### ⚙️ Your current environment

<summary>hf is working while vllm is not. <code>python test_huggingface.py</code> <code>python test_vllm.py</code></summary>

```python
# test_huggingface.py
import transformers
import sys

text = "The united state of"
max_new_tokens = 10
model_name_or_path = "INCModel/Qwen3-0.6B-MXFP4-MXFP8"
model = transformers.AutoModelForCausalLM.from_pretrained(model_name_or_path, trust_remote_code=True, device_map="cpu", torch_dtype="auto")
tokenizer = transformers.AutoTokenizer.from_pretrained(model_name_or_path, trust_remote_code=True)
inputs = tokenizer(text, return_tensors="pt").to('cpu')
generated_ids = model.generate(**inputs, max_new_tokens=max_new_tokens)[0]
output = tokenizer.decode(generated_ids)
print(output)
```

```python
# test_vllm.py
from vllm import LLM, SamplingParams
import sys

text = "The united state of"
max_new_tokens = 100
model_name_or_path = "INCModel/Qwen3-0.6B-MXFP4-MXFP8"

llm = LLM(model=model_name_or_path, trust_remote_code=True)

sampling_params = SamplingParams(max_tokens=max_new_tokens)
outputs = llm.generate([text], sampling_params)

for output in outputs:
    print(output.outputs[0].text)
```


### 🐛 Describe the bug


Issue1: Loading failure, KeyError: 'layers.0.mlp.gate_up_proj.weight'

Fixed in `find_matched_target` with changed order.
```
    matched_target = (
        _find_first_match(layer_name, targets)
        or _match_fused_layer(layer_name, targets, fused_mapping)
        or _find_first_match(module.__class__.__name__, targets, True)
    )
```

Issue2: Load success but prompt generation is incorrect.


### 🛠️ Steps to reproduce

Using main branch of CT, and latest vllm.
`python test_vllm.py`

## 评论 (18)

### brian-dellabetta · 2026-05-20

Hi @xin3he , can you provide a link to the checkpoint or creation script? I will often have to explicitly add both fused and unfused names to the list of targets for non-uniform quant, because vllm does a name mapping. See example [here](https://github.com/vllm-project/llm-compressor/blob/main/examples/model_free_ptq/deepseek_r1_nvfp4_fp8_block.py#L50-L51), where i add gate_up_proj to the regex. It doesn't do anything during oneshot, just ensures that gate_up_proj is in the list of targets when loading in vllm


### xin3he · 2026-05-22

I'm using AutoRound to generate the llmc format model, considered using same dtype for fused layers (qkv, gate_up).
Here is the model link: https://huggingface.co/INCModel/Qwen3-0.6B-MXFP4-MXFP8
Script: https://github.com/intel/neural-compressor/tree/master/examples/pytorch/nlp/huggingface_models/language-modeling/quantization/auto_round/llama3
```
CUDA_VISIBLE_DEVICES=5 python quantize.py  \
    --model_name_or_path /models/Qwen3-0.6B \
    --quantize \
    --dtype MXFP4 \
    --target_bits 7 \
    --options "MXFP4" "MXFP8" \
    --shared_layer "k_proj" "v_proj" "q_proj" \
    --shared_layer "gate_proj" "up_proj" \
    --enable_torch_compile  \
    --low_gpu_mem_usage \
    --export_format llm_compressor  \
    --export_path qwen-0.6b
```

### brian-dellabetta · 2026-05-26

Hi @xin3he , yeah the problem is a deficiency in the vllm weight loading logic:
- vllm fuses q_proj, k_proj, v_proj into a single qkv_proj 
- vllm fuses gate_proj, up_proj into a single gate_up_proj
- during weight loading, it tries to find a match in targets/ignore for `model.layers.x.mlp.gate_up_proj`
- the checkpoint only has the unfused names in targets, so no match is found
- this results in a downstream error `KeyError: 'layers.0.mlp.gate_up_proj.weight'`

Ultimately, this needs to be resolved in vllm's weight loading logic, but it is nontrivial to back-track out what the unfused names are. I spoke with @kylesayrs , we are considering this after the transformers v5 work lands. In the meantime, you need to ensure the fused layer names appear in targets/ignore, accordingly. I have opened a PR on your model config.json to show what that looks like -- https://huggingface.co/INCModel/Qwen3-0.6B-MXFP4-MXFP8/discussions/1. With this config.json, I get through the weight loading but hit a downstream error that seems unrelated. I've not seen an error like this before, can I pass this back to you to try to debug further?

> RuntimeError: Invalid thread config: thread_m_blocks = 1, thread_k = -1, thread_n = -1, num_threads = -1 for MKN = [16384, 1024, 4096] and num_bits = 8, prob_m_split = 2048, group_size = 32, has_act_order = 0, is_k_full = 1, has_zp = 0, is_zp_float = 0, stages = 4, max_shared_mem_new = 232448

### xin3he · 2026-05-28

Thank you, @brian-dellabetta 
It can run now with below changes.
```python
os.environ.setdefault("VLLM_DISABLED_KERNELS", "MarlinMxfp8LinearKernel")

llm = LLM(
    model=model_name_or_path,
    trust_remote_code=True,
    enforce_eager=True,
    dtype="bfloat16",
)
```

### xin3he · 2026-05-28

From my knowledge, The error is because that the hidden size of this model is too small for `MarlinMxfp8LinearKernel`.

### brian-dellabetta · 2026-05-28

Hi @xin3he , great glad it worked! We have talked a little bit about resolving the deeper issue. I will raise it with the team after our next release (should be soon)

### xin3he · 2026-07-01

Hi @brian-dellabetta 
Do you have any update about this issue?

### brian-dellabetta · 2026-07-06

Hi @xin3he , i've discussed this with the team but haven't looked deeply into a solution. Some models provide `hf_to_vllm_mapper` class vars for the mapping, like Qwen3's [here](https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/models/qwen3_moe.py#L434-L446), but I am not sure this is standardized across all model defs in a way we can rely on it. I will raise it in the SIG meeting today

### xin3he · 2026-07-07

Thanks, really appreciate it.

### brian-dellabetta · 2026-07-07

discussed in SIG meeting, `hf_to_vllm_mapper` is the appropriate source of truth. I will try to set up a resolution this week

### brian-dellabetta · 2026-07-07

Hi @xin3he , I took some time to look into this today. Your initial solution of reordering 
```
    matched_target = (
        _find_first_match(layer_name, targets)
        or _match_fused_layer(layer_name, targets, fused_mapping)
        or _find_first_match(module.__class__.__name__, targets, True)
    )
```
looks like the correct path forward to me. i missed that you were using specific targets for the first config_group and `targets=["Linear"]` for the second config_group. I'll confirm with team and get back to you. If so, we can have you open the vllm PR to get the credit 😄 

Strangely, I am no longer able to reproduce the KeyError you reported. On current vllm, I hit `Error: `AttributeError: 'MergedColumnParallelLinear' object has no attribute 'data'` when loading your original checkpoint. After your reordering, it succeeds. 

If you manage to hit the `KeyError` again, please let me know your environment so I can try to reproduce. I was hitting `KeyError`s when loading my mixed-precision models in vllm, but it no longer seems to be occurring. Perhaps it has been resolved? My attempts to check previous versions of vllm are failing for unrelated installation issues. 

<details><summary>Script to run your original checkpoint:</summary>

```python
import sys
import os

os.environ.setdefault("VLLM_DISABLED_KERNELS", "MarlinMxfp8LinearKernel")

model_name = "INCModel/Qwen3-0.6B-MXFP4-MXFP8"

from vllm import LLM

llm = LLM(
    model=model_name,
    revision="1a0c02ca35d68d86aaa08afc7dc1c177793a3825",
    gpu_memory_utilization=0.9,
    enforce_eager=True,
    # dtype="bfloat16",
)

print("✓ Model loaded successfully!")

# Test generation
prompts = ["Hello, how are you?"]
outputs = llm.generate(prompts)

for output in outputs:
    print(f"Prompt: {output.prompt}")
    print(f"Generated text: {output.outputs[0].text}")

print("✓ Generation test passed!")
```

</details>


### xin3he · 2026-07-10

Hi @brian-dellabetta 
I can reproduce this issue with the script you shared. 
The latest vLLM is installed
`uv pip install -U vllm --pre --extra-index-url https://wheels.vllm.ai/nightly/cu130 --extra-index-url https://download.pytorch.org/whl/cu130 --index-strategy unsafe-best-match`

```
(EngineCore pid=4020088) INFO 07-10 12:16:24 [core.py:114] Initializing a V1 LLM engine (v0.24.0) with confi
g: model='INCModel/Qwen3-0.6B-MXFP4-MXFP8', speculative_config=None, tokenizer='INCModel/Qwen3-0.6B-MXFP4-MX
FP8', skip_tokenizer_init=False, tokenizer_mode=auto, revision=1a0c02ca35d68d86aaa08afc7dc1c177793a3825, tok
enizer_revision=1a0c02ca35d68d86aaa08afc7dc1c177793a3825, trust_remote_code=False, dtype=torch.bfloat16, max
_seq_len=40960, download_dir=None, load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=1, data_
parallel_size=1, decode_context_parallel_size=1, dcp_comm_backend=ag_rs, disable_custom_all_reduce=False, qu
antization=compressed-tensors, quantization_config=None, enforce_eager=True, enable_return_routed_experts=Fa
lse, kv_cache_dtype=auto, device_config=cuda, structured_outputs_config=StructuredOutputsConfig(backend='aut
o', disable_any_whitespace=False, disable_additional_properties=False, reasoning_parser='', reasoning_parser
_plugin='', enable_in_reasoning=False), observability_config=ObservabilityConfig(show_hidden_metrics_for_ver
sion=None, otlp_traces_endpoint=None, collect_detailed_traces=None, kv_cache_metrics=False, kv_cache_metrics
_sample=0.01, cudagraph_metrics=False, enable_layerwise_nvtx_tracing=False, enable_mfu_metrics=False, enable
_mm_processor_stats=False, enable_logging_iteration_details=False, jit_monitor_verbose=False), seed=0, serve
d_model_name=INCModel/Qwen3-0.6B-MXFP4-MXFP8, enable_prefix_caching=True, enable_chunked_prefill=True, poole
r_config=None, compilation_config={'mode': <CompilationMode.NONE: 0>, 'debug_dump_path': None, 'cache_dir': 
'', 'compile_cache_save_format': 'binary', 'backend': 'inductor', 'custom_ops': ['all'], 'ir_enable_torch_wr
ap': False, 'splitting_ops': [], 'compile_mm_encoder': False, 'cudagraph_mm_encoder': False, 'encoder_cudagr
aph_token_budgets': [], 'encoder_cudagraph_max_vision_items_per_batch': 0, 'encoder_cudagraph_max_frames_per
_batch': None, 'compile_sizes': [], 'compile_ranges_endpoints': [8192], 'inductor_compile_config': {'enable_
auto_functionalized_v2': False, 'size_asserts': False, 'alignment_asserts': False, 'scalar_asserts': False, 
'combo_kernels': True, 'benchmark_combo_kernel': True}, 'inductor_passes': {}, 'cudagraph_mode': <CUDAGraphM
ode.NONE: 0>, 'cudagraph_num_of_warmups': 0, 'cudagraph_capture_sizes': [], 'cudagraph_copy_inputs': False, 
'cudagraph_specialize_lora': True, 'use_inductor_graph_partition': False, 'pass_config': {'fuse_norm_quant':
 True, 'fuse_act_quant': True, 'fuse_attn_quant': False, 'enable_sp': False, 'fuse_gemm_comms': False, 'fuse
_allreduce_rms': False, 'fuse_rope_kvcache_cat_mla': False, 'fuse_act_padding': False}, 'max_cudagraph_captu
re_size': 0, 'dynamic_shapes_config': {'type': <DynamicShapesType.BACKED: 'backed'>, 'evaluate_guards': Fals
e, 'assume_32_bit_indexing': False}, 'local_cache_dir': None, 'fast_moe_cold_start': False, 'static_all_moe_
layers': []}, kernel_config=KernelConfig(ir_op_priority=IrOpPriorityConfig(rms_norm=['vllm_c', 'native'], fu
sed_add_rms_norm=['vllm_c', 'native']), enable_flashinfer_autotune=True, moe_backend='auto', linear_backend=
'auto') 
...
(EngineCore pid=4020088)   File "/home/xinhe/.venv/lib/python3.12/site-packages/vllm/model_executor/models/u
tils.py", line 282, in _load_module
(EngineCore pid=4020088)     loaded_params = module_load_weights(weights)
(EngineCore pid=4020088)                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore pid=4020088)   File "/home/xinhe/.venv/lib/python3.12/site-packages/vllm/model_executor/models/q
wen2.py", line 456, in load_weights
(EngineCore pid=4020088)     param = params_dict[name] 
(EngineCore pid=4020088)             ~~~~~~~~~~~^^^^^^ 
(EngineCore pid=4020088) KeyError: 'layers.0.mlp.gate_up_proj.weight'
Loading safetensors checkpoint shards:   0% Completed | 0/1 [00:00<?, ?it/s]

```

### brian-dellabetta · 2026-07-10

Hi @xin3he , thanks for the info. I will try again on a fresh venv with vllm nightly early next week

### brian-dellabetta · 2026-07-13

Hi @xin3he , I tried on multiple GPUs and multiple vllm versions, and I am unable to reproduce your KeyError, I just hit
```
(EngineCore pid=899218) AttributeError: 'MergedColumnParallelLinear' object has no attribute 'data'
```
Can you retry on a fresh venv with vllm 0.25.0? It just came out a couple days ago. Perhaps some older dependency like transformers is causing the different error. 

Switching the order in `find_matched_target` as you suggested resolves the error nonetheless. Would you like to open a PR to vllm? Otherwise I can do so

### xin3he · 2026-07-22

Hi @brian-dellabetta  you're right, the error changed since version 0.25.0. I can only reproduce with v0.24.0.
the latest commit of this model still work on the latest version.
so I think now we have more issues other than the `find_matched_target`. I will dig into it and update in this issue.

### brian-dellabetta · 2026-07-22

@xin3he sounds good, the ordering in `find_matched_target` should resolve. I think that's all we need, the issue might have been resolved somewhere in v0.24+

### xin3he · 2026-07-24

@brian-dellabetta  I can run big model with your PR, and I think we can ignore the error happened in the demo model.

### brian-dellabetta · 2026-07-24

Thanks @xin3he , i will try to get that in soon (failing on unrelated CI/CD) but yeah we can keep an eye and re-open if we find issues in future
