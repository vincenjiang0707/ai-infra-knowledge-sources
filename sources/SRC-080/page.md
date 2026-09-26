source: https://github.com/NVIDIA/Model-Optimizer/releases

# Releases: NVIDIA/Model-Optimizer

## Release list

## ModelOpt 0.47.0 Release

### New Features

#### Quantization

-
ONNX quantization with Autotune now benchmarks placements in the requested runtime precision and retains calibrated INT8/FP8 Q/DQ only when it meets the configured TensorRT speedup threshold (1.02x by default); otherwise it saves the high-precision no-Q/DQ model.

-
Add a Muse Glimmer AutoQuantize recipe that searches language-model MLP projections, self-attention projections, and

`lm_head`

over W4A16 NVFP4 Four-Over-Six, FP8, and BF16 fallback at 5.5 effective bits while leaving the vision tower unquantized. -
Add

`examples/alpamayo/qad.py`

, which runs quantization-aware distillation on the quantized Alpamayo checkpoint produced by`examples/alpamayo/quantize.py`

. It distills the quantized VLM against the original FP16 VLM with`QADTrainer`

, supports FSDP2 for multi-GPU runs, and`--export`

reassembles the trained VLM into a full AlpamayoR1 checkpoint that`AlpamayoR1.from_pretrained`

can reload. -
Add a calibration-free streaming Kimi-K3 converter and checkpoint-mirror recipe for NVFP4 routed experts with

`input_scale=1.0`

and 128x128 block-FP8 KDA/MLA attention weights. The converter operates shard-by-shard on the source checkpoint's packed MXFP4 experts instead of loading the 2.8T model through the in-memory`hf_ptq.py`

path. -
Add end-to-end PETRv1 and PETRv2 ONNX PTQ examples covering calibration, INT8 and FP8 VoVNet backbone quantization, TensorRT deployment, and accuracy evaluation.

-
Add opt-in FP8 Vision Encoder recipes under the

`qwen3_vl`

and`qwen3_5`

model types. The vision-only recipe keeps the language model and KV cache in high precision; the joint recipe quantizes Vision Encoder and language-model Linears and uses FP8 KV-cache cast. Both quantize primary and deepstack merger Linears where present, while leaving patch embedding and vision-attention BMMs in high precision. Exported checkpoints require an inference runtime that supports quantized Vision Encoder Linears. -
Add

`mtq.temporarily_fold_weights`

for repeated frozen-weight inference and`mtq.preserve_quantizer_attributes_context`

for restoring temporary quantizer property and type changes. Temporary folding snapshots affected fake-quant weights on a configurable device and restores them with their quantizer state; retained pre-quant scales are inactive, while shared weights, shared quantizers, and`SequentialQuantizer`

weights are unsupported. -
Add the

`nvfp4_act_headroom`

calibration algorithm for NVFP4**activation**global scales. Instead of setting the global scale from the largest per-block amax seen during calibration (plain`max`

, which leaves no room above it so any larger activation saturates), it anchors the scale to a low percentile of the per-block amax distribution, leaving the rest of the FP8 block-scale range as headroom:`amax = max(rho * anchor, upper)`

, where`anchor`

and`upper`

are the per-block amaxes at`anchor_percentile`

(default 1) and`upper_percentile`

(default 99.99; set to 100 to never clip calibration data), and`rho`

(default 16384) is the headroom factor. Applies only to NVFP4 dynamic-block input quantizers;`SequentialQuantizer`

activation quantizers raise. Weight scales are an orthogonal axis selected by a nested`weight_scale_algorithm`

(`max`

by default, or`mse`

/`local_hessian`

), so one recipe can combine a weight calibration with this activation policy in a single pass. Ships`modelopt_recipes/general/ptq/nvfp4_act_headroom-kv_fp8_cast.yaml`

, which mirrors`nvfp4_default-kv_fp8_cast`

with only the calibration algorithm swapped and exports a standard NVFP4 checkpoint. -
Add PTQ support for Step-3.7 (

`stepfun-ai/Step-3.7-Flash`

), whose routed experts were previously left unquantized. Quantize with the new`huggingface/step3p7/ptq/nvfp4_experts_only-kv_fp8_cast`

or`huggingface/step3p7/ptq/nvfp4_mlp_only-kv_fp8`

recipes rather than the general ones, which select experts by module names Step does not use.

#### Megatron Framework (M-LM / M-Bridge)

- Add
`clamp_kv_cache_scales`

to`export_mcore_gpt_to_hf`

. Set it to`False`

when exporting a QAT Megatron-Core model to preserve its learned FP8 KV-cache scales; the default retains the existing minimum scale of 1.0. - Add SFT-masked data support to
`examples/megatron_bridge/distill.py`

:`--sft --sft_dataset_root <dir>`

distills on raw prompt-completion JSONL (`{"input", "output"}`

records) with the loss masked to the response tokens, using Megatron-Bridge's`FinetuningDatasetConfig`

and the model's own HuggingFace tokenizer instead of the pretraining`GPTDataset`

and`NullTokenizer`

. - Add per-expert weight quantization for Transformer Engine
`TEGroupedLinear`

(fused MoE experts): each expert now has its own`weight_quantizer`

(a`GroupedQuantizer`

holding one`TensorQuantizer`

per expert) with an independent`amax`

, instead of a single shared`amax`

across all experts. Applies to`mtq.quantize`

calibration, HF / Megatron export, and QAD. - Add opt-in
`torch.compile`

execution for Transformer Engine grouped-linear per-expert weight quantizers while preserving their native checkpoint amax shapes. Set`MODELOPT_TEGROUPED_COMPILE_WEIGHT_LOOP=1`

before quantized-module conversion; the default path remains eager. - Add HuggingFace unified export of quantized Qwen3-VL and Qwen3.5-VL checkpoints (PTQ or QAD) via
`examples/megatron_bridge/export_quantized_megatron_to_hf.py`

, Qwen3.5-VL additionally covering GatedDeltaNet linear-attention layers and MoE shared experts. Only the language model is quantized; the vision tower is copied from the source HuggingFace checkpoint. - Megatron-Bridge scripts now choose the MoE expert layout automatically from the model config: the faster fused
`TEGroupedMLP`

(grouped GEMM) unless the architecture cannot export it to HuggingFace, in which case`SequentialMLP`

keeps the checkpoint exportable and`--no_moe_grouped_gemm`

forces it explicitly. For the affected architectures this changes MoE activation scales from one shared scale to per-expert.

#### Misc

- Add
`modelopt.torch.utils.mlflow.MlflowRunLogger`

for recording a script run on an MLflow tracking server: the invocation, the ModelOpt version, the run log (captured by teeing`stdout`

/`stderr`

) and any caller-supplied artifacts, with configuration as searchable params.`mlflow`

is an optional dependency, imported only when tracking is enabled. - Add
`--mlflow <tracking-uri>`

to`examples/hf_ptq/hf_ptq.py`

(MLflow's own`MLFLOW_TRACKING_URI`

is honoured too). A tracked run records the invocation, the resolved recipe (`$import`

s expanded), the run log and the quantization summaries, with every command-line argument as a searchable param; failed runs are recorded with their traceback. The experiment defaults to`$USER/hf_ptq/<checkpoint basename>-<recipe name or --qformat>`

and can be overridden with`--mlflow_experiment`

/`--mlflow_run_name`

. - Add
`--mlflow <tracking-uri>`

to`examples/vllm_serve/vllm_serve_fakequant.py`

(MLflow's own`MLFLOW_TRACKING_URI`

is honoured too), so a fake-quant serve records what it quantized and an evaluation of that endpoint can be traced back to a recipe. A tracked run uploads the launcher command, the resolved`RECIPE_PATH`

(or the merged`QUANT_CFG`

/`KV_QUANT_CFG`

when presets are used), the worker log and the quantizer summary; the experiment defaults to`$USER/vllm_serve_fakequant/<model basename>-<recipe name or quantization config>`

and can be overridden with`--mlflow-experiment`

/`--mlflow-run-name`

.

### Backward Breaking Changes

- Migrate the FAR3D ONNX PTQ example to the shared evaluator and ModelOpt containers and
`quantize_vovnet.py`

. Only the encoder supports INT8 and FP8; decoder calibration, quantization, and related CLI flags are removed, and the decoder remains in its exported mixed FP16/FP32 precision. - Image-text calibration with
`--calib_with_images`

now forwards multimodal batches through the complete VLM for all VLM families, so existing non-Nemotron commands may produce different language-model activation ranges and output scales. Recipe-based VLM PTQ also targets the complete VLM: vision modules stay in high precision by default and are quantized only when a model-specific recipe enables them, so custom recipes must explicitly exclude vision modules when required. - Move the checkpoint-mirror recipe tier from
`huggingface/models/<org>/<checkpoint>/`

to the top-level`models/<org>/<model_id>/`

, keyed by each recipe's canonical Hugging Face Hub id — so the Step 3.5 Flash recipe moves to`models/stepfun-ai/Step-3.5-Flash/ptq/`

and the NVIDIA Nemotron recipes gain the`NVIDIA-`

prefix (e.g.`models/nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-BF16/ptq/nvfp4-mse`

). Update any saved`--recipe`

paths for these checkpoint recipes accordingly; the per-`model_type`

recipes under`huggingface/`

are unchanged. - Move the Mistral Medium 3.5 checkpoint-mirror recipe from
`huggingface/models/nvidia/Mistral-Medium-3.5-128B-NVFP4/ptq/nvfp4-max-calib`

to`models/mistralai/Mistral-Medium-3.5-128B/ptq/nvfp4-max-calib`

, keying it by the canonical Hugging Face base model. Update any saved`--recipe`

paths to the new location. - Remove the
`--auto_quantize_bits`

,`--auto_quantize_method`

,`--auto_quantize_score_size`

,`--auto_quantize_cost_model`

and`--auto_quantize_active_moe_expert_ratio`

flags from`examples/hf_ptq`

(deprecated in 0.46). Use an AutoQuantize`--recipe`

from`modelopt_recipes/general/auto_quantize/`

instead. Those recipes now also splice in the shared base`cost_excluded_layers`

unit, which the removed CLI applied unconditionally, so a VL model keeps its vision tower and MTP layers out of the effective-bits denominator. On a VL model this changes the per-layer cost weights, so an existing`--auto_quantize_checkpoint`

from an earlier release is rejected with "Use a different checkpoint path"; delete or repoint it to re-run the search. - Remove the
`examples/llm_ptq`

symlink and the`examples/vlm_ptq`

forwarder (both deprecated in 0.46). Use `e...

[Read more](https://github.com/NVIDIA/Model-Optimizer/releases/tag/0.47.0)

## 0.47.0rc2

Install this pre-release version using:

`pip install "nvidia-modelopt[all] @ https://github.com/NVIDIA/Model-Optimizer/releases/download/0.47.0rc2/nvidia_modelopt-0.47.0rc2-py3-none-any.whl"`

## 0.47.0rc1

Install this pre-release version using:

pip install "nvidia-modelopt[all] @ [https://github.com/NVIDIA/Model-Optimizer/releases/download/0.47.0rc1/nvidia_modelopt-0.47.0rc1-py3-none-any.whl](https://github.com/NVIDIA/Model-Optimizer/releases/download/0.47.0rc1/nvidia_modelopt-0.47.0rc1-py3-none-any.whl)"

## ModelOpt 0.46.1 Release

## WoA (Windows) Support

Add opt-in TensorRT-RTX ABI Execution Provider support for ONNX calibration on Windows arm64. Select it with `--calibration_eps=NvTensorRtRtx --trt_rtx_backend=abi`

; the legacy backend remains the default.

## 0.47.0rc0

Install this pre-release version using

```
pip install "nvidia-modelopt[all] @ https://github.com/NVIDIA/Model-Optimizer/releases/download/0.47.0rc0/nvidia_modelopt-0.47.0rc0-py3-none-any.whl"
```


*Published by Chad's Agent.*

## ModelOpt 0.46.0 Release

## New Features

### Quantization

- Add NVFP4 and FP8 PTQ recipes with projection-output quantizers for Llama-Nemotron embedding and reranking models (
`modelopt_recipes/huggingface/nemotron_llama/`

) and an end-to-end HF embedding/reranking quantize-to-ONNX example (`examples/torch_onnx/hf_embedding_quant_to_onnx.py`

). Quantizing the projection-Linear outputs keeps TensorRT inter-layer activations in FP4, roughly halving engine activation memory versus the plain`nvfp4`

preset. NVFP4/MXFP8 output quantizers now export through the dynamic quantize path.`examples/torch_onnx/torch_quant_to_onnx.py`

also gains a`--recipe`

flag to load quantization configs from YAML recipes instead of the removed`mtq.*_CFG`

module-constant table. - Add an end-to-end FAR3D ONNX PTQ example with calibration data generation, INT8 and FP8 quantization, TensorRT engine building, and Argoverse 2 accuracy evaluation. See
[examples/onnx_ptq/far3d/README.md](https://github.com/NVIDIA/Model-Optimizer/tree/main/examples/onnx_ptq/far3d)for details. - Add Learned Scale Quantization (LSQ) and Dual-LSQ support for quantization-aware distillation, including learnable
`amax`

parameters, tied-scale and pre-scale options, focused NVFP4 recipes, and scale-only training. - Add a fused Triton fast path for the
`local_hessian`

NVFP4 weight-scale search, roughly**34x**faster than the Python reference sweep on a single 8192x4096 weight and bit-exact with it for fp32/fp16 weights. Used automatically during`local_hessian`

calibration for both dense and fused-MoE expert weights; falls back to the reference sweep on CPU, when Triton is unavailable, or via`MODELOPT_NVFP4_TRITON_SWEEP=0`

. - Add NVFP4 Four-Over-Six (4/6) weight quantization (
`mtq.NVFP4_FOUR_OVER_SIX_CFG`

): MSE weight calibration picks, per block, between an M=6 and an M=4 dynamic range (the choice is folded into the FP8 per-block scales), with the`four_over_six: true`

flag normalizing those scales by 256 (vs 448) for M=4 headroom. Supported via`mtq.quantize`

and HF / Megatron export only --**not**`mtq.compress`

, which does not preserve the per-block M=4/M=6 choice. - Add dLLM (tied-weight PTQ and HF-checkpoint export) support for diffusion-based encoder-decoder LLMs (e.g. DiffusionGemma) whose encoder/decoder stacks share parameters via HF
`_tied_weights_keys`

. Modules sharing a source weight are deduplicated at export (~42% storage reduction on`nvfp4_experts_only`

for tied 26B MoE checkpoints), a new`sync_tied_input_amax`

helper max-merges per-side`input_quantizer.amax`

across tied modules so single-backbone consumers don't clip either side, and the exported state dict is reordered so the canonical-side keys win the dedup. Ships a DiffusionGemma recipe under`modelopt_recipes/huggingface/diffusion_gemma/ptq/`

. Non-tied models see no behavioral change. - Add Torch-TensorRT FP8 deployment example for HuggingFace ViT (
`examples/torch_trt/`

):`torch_tensorrt_ptq.py`

covers`mtq.quantize`

→`torch_tensorrt.compile(ir="dynamo")`

, and`torch_tensorrt_accuracy.py`

reports the compiled model's ImageNet-1k top-1/top-5 accuracy (the unquantized baseline is Torch-TensorRT-compiled too, for an apples-to-apples comparison). Ships a ViT-tuned FP8 PTQ recipe under`modelopt_recipes/huggingface/vit/ptq/fp8.yaml`

that quantizes the encoder Linears, patch-embed`nn.Conv2d`

,`classifier`

, per-block LayerNorm inputs, and the attention Q/K/V BMMs and softmax. Verified on`google/vit-base-patch16-224`

: FP8 stays within 0.13 pp Top-1 of the FP16 baseline. - Add
**AutoQuantize recipe**support:`mtq.auto_quantize`

can be driven declaratively from a YAML recipe (`RecipeType.AUTO_QUANTIZE`

/`AutoQuantizeConfig`

) specifying candidate formats, the`effective_bits`

target, cost model (incl.`active_moe`

and`excluded_module_name_patterns`

), scoring method, and disabled layers. Adds an`effective_bits`

cost-model override on`QuantizeConfig`

/`QuantizerAttributeConfig`

(block-scale-accurate NVFP4 = 4.5 via`configs/numerics/nvfp4`

). Shipped recipes live under`modelopt_recipes/general/auto_quantize/`

and model-specific ones under`modelopt_recipes/huggingface/<model>/auto_quantize/`

. - Add module-specific AutoQuantize search spaces through
`mtq.auto_quantize(..., module_search_spaces=...)`

and recipe-level`auto_quantize.module_search_spaces`

. Glob-matched decision groups can override the global candidate formats and control whether BF16/no-quant is solver-selectable with`allow_no_quant`

. A recipe can instead reuse a normal PTQ`quantize`

config as the fixed baseline and list only the genuinely searched modules; fixed and searched groups stay in one calibration, scoring, effective-bits, checkpoint, and export flow. - Add
`rotate.mode`

to torch quantizer configs. The default`"rotate"`

keeps the existing rotate-before-quantize behavior;`"rotate_back"`

enables fake-quant rotate → quantize → rotate-back for TensorQuantizer. - Add a
`constant_amax`

`QuantizerAttributeConfig`

field that pins a quantizer's`amax`

to a fixed value and skips activation calibration. Unlike`use_constant_amax`

(which hardcodes 448.0 for KV-cache cast math and registers no buffer),`constant_amax`

stores the constant on the`_amax`

buffer so it is used by both the fake-quant forward and the exported scaling factor — for NVFP4 activations,`constant_amax: 2688.0`

yields`input_scale == 1.0`

. Ships`modelopt_recipes/general/ptq/nvfp4_experts_only_input_scale1-kv_fp8_cast.yaml`

, which applies this to the MoE expert activation quantizers. - Add
`MaxCalibConfig.skip_forward_without_activation_calib`

(opt-in, default`False`

): max calibration skips the`forward_loop`

when no enabled quantizer needs data-driven activation statistics — e.g. an experts-only recipe using`constant_amax`

/`use_constant_amax`

, or dynamic / MX quantization. Weight calibration still runs on the weight tensors directly, so quantized weights are unchanged. It is opt-in because the`forward_loop`

can carry caller-side effects (notably materializing sharded parameters under DeepSpeed ZeRO-3). Enabled by the`nvfp4_experts_only_input_scale1-kv_fp8_cast`

recipe. - Add
`examples/minimax_m3/hf_ptq_mixed_mxfp8_nvfp4.py`

for streaming MiniMax-M3 export and a model-specific`hf_ptq.py`

recipe that produces an MXFP8 language-model base with MSE-calibrated NVFP4 routed experts directly from BF16. The NVFP4 expert`input_scale`

is fixed to 1.0.

### Speculative Decoding

- Add the
**D-PACE**loss objective for DFlash speculative-decoding training ([arXiv:2605.18810](https://arxiv.org/abs/2605.18810)) and make it the default (`dflash_loss_objective: dpace`

). It replaces the static exponential position decay with dynamic, confidence-derived per-position weights that adapt to whichever block positions currently limit acceptance. Smoothing is controlled by`dflash_dpace_alpha`

(default 0.5); set`dflash_loss_objective: decay`

to restore the previous static schedule. Training-only and detached from the gradient (no architecture or inference change). - Add
**streaming**speculative-decoding training (EAGLE3 / DFlash): the draft trains on base-model hidden states produced on the fly by a co-located`vllm serve`

(no disk dump), moved trainer-side over NIXL RDMA, scaling to multi-node (dedicated serve replicas + DDP trainers). New launcher examples for NVFP4 Kimi-K2.5 / K2.6 on GB200/aarch64 under`tools/launcher/examples/moonshotai/`

. - Add
**Domino**speculative-decoding training: the parallel DFlash draft backbone plus a lightweight GRU causal correction head, selected via`dflash_architecture_config.projector_type=domino`

. Trained with a base/final dual loss whose`dflash_lambda_base_start`

/`dflash_lambda_base_decay_ratio`

curriculum decays the base-loss weight 1→0. Exports in the z-lab drafter format; recipe at`modelopt_recipes/general/speculative_decoding/domino.yaml`

. Training only — the inference path is not wired up yet.

### Megatron Framework (M-LM / M-Bridge)

-
Add Minitron pruning support for Megatron-Core models with the following new attention and MoE variants. For these, only

`hidden_size`

is pruned (alongside the usual`ffn_hidden_size`

/`num_layers`

/ MoE dimensions); the variant-internal dimensions noted below are not pruned:**GatedDeltaNet**(linear attention) and**gated attention**(`attention_output_gate`

), such as Qwen3.5 (hybrid GatedDeltaNet + gated-attention) language models, including MoE variants — attention / linear-attention heads are not pruned.**Multi-Latent Attention (MLA)**, such as DeepSeek — MLA latent ranks are not pruned.**Latent MoE**, such as Nemotron-3-Super —`hidden_size`

pruning resizes the latent projections while the MoE latent dim itself is not pruned.

-
Optimize Minitron pruning support for MoE models using the fused

**grouped GEMM**experts (`TEGroupedMLP`

) in addition to the existing`SequentialMLP`

path.`examples/megatron_bridge/prune_minitron.py`

now uses grouped GEMM by default (pass`--no_moe_grouped_gemm`

to fall back to`TESequentialMLP`

). -
Add Minitron pruning support for the language model part of vision-language models (e.g. Qwen3.5-VL, Gemma3-VL) via

`examples/megatron_bridge/prune_minitron.py`

. The language model is pruned while the vision tower is left intact and the full VLM is saved back;`hidden_size`

is not pruned if it is shared with the vision projector. Pruning importance is estimated from image-text calibration (the full VLM forward over vision-conditioned activations) by default, or from a text dataset for text-only ablations. -
Add PTQ support for the language model part of vision-language models (e.g. Qwen3.5-VL, Gemma3-VL) via

`examples/megatron_bridge/quantize.py`

. Only the language model is quantized (vision tower + projector left in full precision) and the full VLM is saved as a Megatron checkpoint. The calibration modality is inferred from`--calib_dataset_name`

: an image-text dataset drives the full VLM forward (vision-conditioned activations), while ...

[Read more](https://github.com/NVIDIA/Model-Optimizer/releases/tag/0.46.0)

## 0.46.0rc2

Install this pre-release version using:

```
pip install "nvidia-modelopt[all] @ https://github.com/NVIDIA/Model-Optimizer/releases/download/0.46.0rc2/nvidia_modelopt-0.46.0rc2-py3-none-any.whl"
```


## 0.46.0rc1

Install this pre-release version using:

```
pip install "nvidia-modelopt[all] @ https://github.com/NVIDIA/Model-Optimizer/releases/download/0.46.0rc1/nvidia_modelopt-0.46.0rc1-py3-none-any.whl"
```


## 0.46.0rc0

Install this pre-release version using

```
pip install "nvidia-modelopt[all] @ https://github.com/NVIDIA/Model-Optimizer/releases/download/0.46.0rc0/nvidia_modelopt-0.46.0rc0-py3-none-any.whl"
```


## ModelOpt 0.45.0 Release

## New Features

### Quantization

- Add NVFP4 W4A16 weight-only quantization (
`w4a16_nvfp4`

): FP4 weights with group_size=16, BF16 activations, no calibration forward pass required. Use`mtq.W4A16_NVFP4_CFG`

or`--qformat w4a16_nvfp4`

in`hf_ptq.py`

. vLLM deployment support is in progress. - Add
`--cast_mxfp4_to_nvfp4`

flag to`examples/llm_ptq/hf_ptq.py`

for closed-form, bit-exact MXFP4 → NVFP4 weight conversion. Supports the GPT-OSS family (`openai/gpt-oss-20b`

,`openai/gpt-oss-120b`

). See[examples/llm_ptq/README.md](https://github.com/NVIDIA/Model-Optimizer/tree/main/examples/llm_ptq#mxfp4--nvfp4-cast-for-gpt-oss)for usage. - Add
`--cast_mxfp4_to_nvfp4`

flag to`examples/deepseek/deepseek_v4/quantize_to_nvfp4.py`

for closed-form, bit-exact MXFP4 → NVFP4 conversion of DeepSeek V4 routed-expert weights (mirrors the GPT-OSS cast; w1/w3 share one per-tensor`scale_2`

for the fused GEMM1). Activation`input_scale`

still comes from`--amax_path`

calibration. - DeepSeek PTQ (
`examples/deepseek/ptq.py`

) now defaults to native top-k calibration with post-hoc per-layer peer-max sync of expert`input_quantizer.amax`

; the all-experts path is preserved behind`--calib_all_experts`

. - Add active-MoE cost accounting for
`mtq.auto_quantize`

effective-bits search. Set`constraints={"effective_bits": ..., "cost_model": "active_moe", "cost": {"active_moe_expert_ratio": ...}}`

to weight routed MoE expert costs by active experts per token while keeping shared experts fully counted. The`hf_ptq.py`

AutoQuant path exposes this via`--auto_quantize_cost_model active_moe`

and`--auto_quantize_active_moe_expert_ratio`

. - Add quantized
`nn.Embedding`

support.`nn.Embedding`

is now registered in`QuantModuleRegistry`

and exposes`weight_quantizer`

(embedding table),`output_quantizer`

(lookup activations), and a permanently disabled`input_quantizer`

placeholder — embedding inputs are integer indices and cannot be fake-quantized, so direct`enable*()`

calls raise.`export_hf_checkpoint`

packs quantized embedding weights alongside Linear layers. Embedding quantizers are opt-in (`parent_class: nn.Embedding`

disabled by default). - Add composable
`$import`

system for recipe YAML configs, enabling reusable config snippets referenced via`{$import: name}`

markers. All built-in PTQ recipes converted to use imports with shared snippets under`modelopt_recipes/configs/`

(numeric formats, quant_cfg building blocks, presets). See composable-imports docs. - The PTQ example scripts
`examples/llm_ptq/hf_ptq.py`

,`examples/llm_ptq/multinode_ptq.py`

and`examples/megatron_bridge/quantize.py`

now derive their`--qformat`

/`--kv_cache_qformat`

(`--quant_cfg`

/`--kv_cache_quant`

for Megatron-Bridge) CLI vocabularies by discovering the YAML presets under`modelopt_recipes/configs/ptq/presets/{model,kv}/`

rather than carrying hardcoded`QUANT_CFG_CHOICES`

/`KV_QUANT_CFG_CHOICES`

tables. The discovery helper, alias table and ready-built`QUANT_CFG_CHOICES`

/`KV_QUANT_CFG_CHOICES`

mappings now live in`modelopt.recipe.presets`

and are shared by all three scripts. Presets are loaded eagerly into a plain dict at import. Adding a new preset YAML makes it available on the CLI of all three with no script change — note this means each script now accepts every preset under those directories, not just a previously curated subset. All previously-supported short names (`int8_sq`

,`nvfp4_awq`

,`fp8_pb_wo`

,`nvfp4_mse`

,`w4a8_awq`

,`nvfp4_local_hessian`

,`fp8_pc_pt`

,`int8_wo`

) keep working via a small deprecation alias table; new formats should be exposed as preset YAMLs (or, longer term, as full`--recipe`

recipes). - Add
`configs/ptq/presets/kv/fp8_cast.yaml`

and`configs/ptq/presets/kv/nvfp4_cast.yaml`

, promoting`fp8_cast`

/`nvfp4_cast`

to first-class KV presets composed from the existing`kv_fp8_cast`

/`kv_nvfp4_cast`

unit fragments. The previous runtime`use_constant_amax`

post-edit in`hf_ptq.py`

is removed;`use_constant_amax: true`

now lives in the YAML and is therefore authoritative.**Custom (out-of-tree) recipes that target a cast KV format must set**— in-tree recipes already do via the`use_constant_amax: true`

themselves on the`[kv]_bmm_quantizer`

config`kv_*_cast`

units. - Add FP8 KV-cache cast variants for the partial-NVFP4 and weight-only general PTQ recipes:
`general/ptq/nvfp4_mlp_only-kv_fp8_cast`

,`general/ptq/nvfp4_experts_only-kv_fp8_cast`

,`general/ptq/nvfp4_omlp_only-kv_fp8_cast`

, and`general/ptq/nvfp4_weight_only-kv_fp8_cast`

. These compose the same model-quant configs as their`-kv_fp8`

siblings with the`kv_fp8_cast`

unit (constant-amax FP8 KV cache, no KV calibration forward pass). - Add Nemotron-3-Super-120B-A12B PTQ recipes
`modelopt_recipes/models/Nemotron-3-Super-120B-A12B/super-nvfp4.yaml`

(MSE-mixed) and`super-nvfp4-max-calib.yaml`

(max-calib mixed): NVFP4 W4A4 routed experts + FP8 per-tensor shared experts / Mamba in/out_proj + FP8 KV cache. - Group layerwise calibration options under a nested
`LayerwiseConfig`

and add two knobs:`get_qdq_activations_from_prev_layer`

(correct GPTQ-Hessian vs max-calib activation semantics — defaults to True for GPTQ, False for max/mse/local_hessian) and`save_every`

(gate per-window`next_inputs.pt`

activation-cache writes). Legacy bool`layerwise`

and flat`layerwise_checkpoint_dir`

keys still work; the bool form emits a`DeprecationWarning`

. - Add
`examples/alpamayo`

showing FP8, NVFP4, and AutoQuantize (mixed-precision) quantization of the Alpamayo (formerly Alpamayo-R1) ~10B vision-language-action model, with a joint VLM + diffusion calibration loop and both fake-quant and`--real-quant`

packed-checkpoint export. See[examples/alpamayo/README.md](https://github.com/NVIDIA/Model-Optimizer/tree/main/examples/alpamayo)for details. - Refactor
`llm_qat`

example with unified YAML-based configuration and flexible dataset blending.`ModelOptArgParser`

adds`--config`

YAML support with CLI overrides and auto-generates`ARGUMENTS.md`

from dataclass definitions. Dataset blending (`configs/dataset/blend.yaml`

) supports HuggingFace datasets, local JSON/JSONL/Parquet files, and weighted multi-source blends. The legacy FSDP1 accelerate config is removed;`llm_qat`

now documents FSDP2, DeepSpeed, and DDP backends.

### Megatron Framework (M-LM / M-Bridge)

- Add quantization examples for the Megatron-Bridge framework (
`examples/megatron_bridge/`

): post-training quantization ([quantize.py](https://github.com/NVIDIA/Model-Optimizer/blob/main/examples/megatron_bridge/quantize.py)calibrates an HF model via`--quant_cfg`

alias / full config name or a`--recipe`

YAML, with optional KV-cache quant, weight-only, compression, and MoE expert-ratio calibration, and saves a Megatron checkpoint with tensor / pipeline / expert parallelism), export to a deployable HuggingFace (unified) checkpoint for TensorRT-LLM / vLLM / SGLang ([export.py](https://github.com/NVIDIA/Model-Optimizer/blob/main/examples/megatron_bridge/export.py)), and Quantization Aware Distillation (extend existing[distill.py](https://github.com/NVIDIA/Model-Optimizer/blob/main/examples/megatron_bridge/distill.py)). See[examples/megatron_bridge/README.md](https://github.com/NVIDIA/Model-Optimizer/tree/main/examples/megatron_bridge)for details. - Add Megatron Core export/import mapping for Qwen3-VL (
`Qwen3VLForConditionalGeneration`

) vision-language models. The mapping handles the`model.language_model.`

weight prefix used by Qwen3-VL. - Add shared Megatron-Core calibration forward loop:
`modelopt.torch.utils.plugins.megatron_calibration.get_megatron_calibration_forward_loop`

produces the`forward_loop`

callable expected by`mtq.quantize`

/`mtp.prune`

. Replaces the bespoke calibration loops in Megatron-LM and Megatron-Bridge for quantization and pruning with a single canonical implementation. - Support Megatron-Core checkpoint restore and export for MSE
`NVFP4StaticQuantizer`

. - Add mixed-precision FP8 + NVFP4 export for Megatron-Core: per-layer
`quant_algo`

recorded under`quantized_layers`

in`hf_quant_config.json`

, PP-aware`kv_cache_dtype`

gather, fused-QKV exclude split into per-HF-name`q/k/v_proj`

entries. - Add support for
`active_params`

(for MoE models) and`memory_mb`

constraints in Minitron pruning on top of existing`params`

constraint. You can also provide multiple constraints. See[examples/pruning/README.md](https://github.com/NVIDIA/Model-Optimizer/tree/main/examples/pruning)for more details. The underlying utility functions`mcore_param_count`

,`mcore_memory_footprint_mb`

, and`print_mcore_model_stats`

in`modelopt.torch.nas.plugins.megatron_model_stats`

are also available for standalone use to compute parameter counts and memory footprints (weights + KV-cache + Mamba state) for any Megatron-Core model. - Add Minitron pruning support for Megatron-Bridge Gemma3 models.
- Add end-to-end optimization tutorial for Minitron pruning + two-phase distillation (80B @ 8K + 20B @ 32K long-context = 100B tokens) + FP8 PTQ + vLLM deployment for Nemotron-3-Nano-30B-A3B-BF16 (MoE + Mamba-Transformer hybrid) → Pruned 22B/A3.0B active params, along with data blend preparation steps (with tool-calling data) and detailed pruning / data-blend / long-context ablations. See
[examples/megatron_bridge/tutorials/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16/README.md](https://github.com/NVIDIA/Model-Optimizer/tree/main/examples/megatron_bridge/tutorials/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16/)for details.

### Datasets & Calibration

- Add
`DATASET_COMBOS`

to`modelopt.torch.utils.dataset_utils`

— single`--dataset`

tokens that fan out to multiple registered datasets; per-entry`num_samples`

is split evenly across the members. Initial combos:`cnn_nemotron_v2_mix`

(`cnn_dailymail`

+`nemotron-post-training-dataset-v2`

, used by`hf_ptq.py`

when no`--dataset`

is provided) and`nemotron-post-training-v3`

(the seven`nvidia/Nemotron-*`

SFT datasets added in[#1498](https://github.com/NVIDIA/Model-Optimizer/pull/1498), mirroring the [nemotron-post-training-v3 collection]([https://h](https://h)...

[Read more](https://github.com/NVIDIA/Model-Optimizer/releases/tag/0.45.0)