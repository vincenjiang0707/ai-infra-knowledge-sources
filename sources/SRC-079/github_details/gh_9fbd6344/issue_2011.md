# [Issue #2011] NVFP4 support for Qwen3_5MoeExperts (fused MoE): quantizer registration + export serializer

source: https://github.com/NVIDIA/Model-Optimizer/issues/2011
state: open | updated: 2026-09-09T19:13:54Z
labels: 

## 正文

## Summary
`mtq.quantize` **silently skips** the fused experts of `transformers` `Qwen3_5MoeExperts` (Qwen3.5/3.6-VL-MoE) — they're 3-D `nn.Parameter`s (`gate_up_proj [E,2I,H]`, `down_proj [E,H,I]`) with a per-expert `F.linear` loop, and there's no `QuantModuleRegistry` entry. Result: the ~50GB expert bulk stays bf16, and `export_hf_checkpoint` has no serializer for it (`layer_utils.get_experts_list` only handles per-expert `nn.Linear`, Mixtral/DBRX-style).

## Proposed
1. Register a `_QuantQwen3_5MoeExperts(QuantModule)` (analogous to `_QuantLlama4TextExperts` but with `F.linear`/`(out,in)` layout — no transpose). Reference impl that works today as an external registration is included in the HF repo below.
2. Add a fused-3-D export path so `export_hf_checkpoint` emits `w13/w2` NVFP4 (packed uint8 + fp8 block scale + fp32 per-shard global + input scale).

## Workaround shipped
Custom registration + **manual NVFP4 packing** via `NVFP4QTensor` (global `amax/(6·448)`, block `amax/(6·global)`), writing the vLLM-ready checkpoint directly (also avoids `export_hf_checkpoint` OOM on unified-memory boxes).

## Artifacts
Full `quantize.py` + resulting model (67GB→22GB, vision intact): https://huggingface.co/frischeDaten/Qwen3.6-VL-35B-A3B-NVFP4-DGX-Spark-VisionSafe


## 评论 (8)

### meenchen · 2026-07-23

@frischeDaten can you try the main branch and see if that works for you?

### frischeDaten · 2026-07-23

Thanks @meenchen — confirmed, `main` resolves the quantizer side. 🎉

`register_fused_experts_on_the_fly` / `_QuantFusedExperts` now auto-detects and wraps the fused `Qwen3_5MoeExperts` with no custom registration. Verified against the real `transformers` module (`modelopt 0.46.0.dev193+gd984de379`, `transformers 5.14.1`):

```
experts type BEFORE: Qwen3_5MoeExperts       | is QuantModule: False
experts type AFTER : QuantQwen3_5MoeExperts   | is QuantModule: True   # auto-detected & wrapped
gate_up per-expert weight quantizers: 8 (expect 8)
calibrated amax present on experts   : True (8/8)
quantized forward finite: True | mean rel delta vs fp: 0.0444          # weights actually quantized
```

The per-expert-index-from-storage-offset approach is also nicer than the whole-tensor workaround I'd been using locally — thanks for the thorough fix (and the Mixtral/DeepSeek/MiniMax/Jamba coverage).

One note on scope: I validated the **detection + quantization** path on CPU with `INT8_DEFAULT_CFG`, since NVFP4 fake-quant asserts `amax must be a CUDA tensor` and my GB10 was busy. The interception path is format-independent, so this confirms the experts are no longer skipped — but I haven't yet run a full **NVFP4 export end-to-end** (`mtq.quantize` → `export_hf_checkpoint` → load in vLLM) on the real 67B checkpoint.

Quick question before this can be closed: is the **export** side (the second half of this issue — serializing the fused experts into the standard NVFP4 checkpoint layout) also expected to work on `main` now, or is that still pending? I'm happy to run the full NVFP4 export on GB10 and report back.


### ChenhanYu · 2026-08-02

Software Release Triage
release: ModelOpt v0.46.0
fingerprint: ff20d41e994ec14583ff69c2a60798ab53e4836aa627a98341547086f03fce5b

This open issue is in the ModelOpt release sweep. Owner: confirm release impact, linked fix/validation, or that it is non-blocking for this release.

### ChenhanYu · 2026-08-02

Software Release Triage
release: ModelOpt v0.46.0
fingerprint: 92e587d7022ea978ef5ac9337a719d683acf00558c5e7c0e630ec70b7f3dd5b6

This open issue is in the ModelOpt release sweep. Owner: confirm release impact, linked fix/validation, or that it is non-blocking for this release.

### frischeDaten · 2026-08-02

Release-impact input from the reporter's side: **non-blocking for 0.46.0**, with one part still unvalidated end-to-end.

**Half 1 — quantizer registration: fixed and verified.** `register_fused_experts_on_the_fly` / `_QuantFusedExperts` auto-detects and wraps the fused `Qwen3_5MoeExperts` with no custom registration (details in my comment above).

**Half 2 — export serializer: looks addressed on `main`, but I haven't confirmed it on real weights.** Reading the current code, `hf_export_handlers.py` registers `_prepare_fused_experts` and `_export_fused_experts_module` by the `_has_fused_experts_quantizers` **predicate** rather than by model name, so `Qwen3_5MoeExperts` should route into `_export_fused_experts` without needing a per-architecture entry — and the 0.46 changelog describes the same machinery unblocking export for MiniMax-M2/M3. That matches the second half of what I asked for here, so I'd consider the issue substantively resolved unless a maintainer knows otherwise.

Two things I couldn't resolve by reading, which may or may not matter for the release:

1. `get_experts_list` (`modelopt/torch/export/layer_utils.py`) still raises `NotImplementedError` for unrecognized `model_type` and reaches experts via `experts[i].<linear_name>`, which doesn't hold for a fused 3-D experts module. It's only called from `requantize_resmooth_fused_llm_layers` under `"awq" in quantization_format or == NVFP4_SVDQUANT`, so plain `nvfp4` never hits it — but `nvfp4_awq` on a fused-expert model presumably still would. Intentional scope, or a follow-up?

2. The 0.46 changelog notes that mapping ops which can't be reversed quant-aware yet — "e.g. still-stacked fused experts" — fall back to in-memory names instead of hub names. For a fused-expert VL-MoE that's precisely the key naming a downstream loader keys off, and it's the same surface as my companion vLLM issue (vllm-project/vllm#49638, fused-expert NVFP4 scales dropped in the `qwen3_5_vl_moe` weight_loader). Worth knowing whether the exported checkpoint for this architecture lands on hub names or the fallback.

I do plan to run the full `mtq.quantize` → `export_hf_checkpoint` → vLLM load on the real 67B checkpoint against `0.46.0rc0` and report the result here, but my GB10 is tied up with an unrelated A/B at the moment, so I can't promise that lands before the release cut. Please don't hold 0.46.0 on it — feel free to close, and I'll reopen or file fresh if the E2E export turns up anything.


### ChenhanYu · 2026-08-02

Software Release Triage
release: ModelOpt v0.46.0
fingerprint: 5c98dd4d163a0594a38d8e6fca88e8619da8370de53108d702eb5aa92b177a7f

Release follow-up: this open ModelOpt issue needs release relevance confirmed. Link its planned fix/validation, or confirm it is not a v0.46.0 blocker.

### t-timms · 2026-09-06

Independent repro on the **text / coder** side of this arch (not just VL), in case it widens the scope usefully.

**Setup:** `mtq.quantize` on a REAP-50-pruned `Kwaipilot/KAT-Coder-V2.5-Dev` (`Qwen3_5MoeForConditionalGeneration`, `model_type: qwen3_5_moe`), transformers 5.15.1, `NVFP4_W4A4_WEIGHT_LOCAL_HESSIAN_CFG`.

**Observed:** after load, `model.named_modules()` reports 868 modules and **0** expert projection submodules. The 128 experts per layer are collapsed into one `Qwen3_5MoeExperts` holding two 3-D `nn.Parameter`s:

- `gate_up_proj` — `(128, 1024, 2048)` = `(E, 2*moe_intermediate, hidden)`
- `down_proj`   — `(128, 2048, 512)`  = `(E, hidden, moe_intermediate)`

`Qwen3_5MoeExperts.forward` runs a per-expert `nn.functional.linear(x, gate_up_proj[e])` / `linear(., down_proj[e])` loop, i.e. `(out, in)` weight layout, no transpose — matching the note in the issue body. So a `_QuantQwen3_5MoeExperts` modeled on `_QuantLlama4TextExperts` + `_TransposedExpertsCalibMixin` needs the **non-transposed** calibration/forward variant (weights are already `(out, in)`; `_transposed_quantize` / `iter_weights_for_calibration`'s `.transpose(-1, -2)` would be wrong here).

**Second call site:** `modelopt/torch/export/layer_utils.py::get_experts_list()` on `main` also has no branch for this class — it would raise `NotImplementedError(f" {model_type} not supported")`, and its `range(len(module.experts))` assumes an indexable expert list. It's reached from `unified_export_hf.py::requantize_resmooth_fused_llm_layers()` for AWQ / SVDQuant. For fused experts that resmoothing is a no-op (one shared tensor, one shared input quantizer), so an early `return []` there is the right behavior, but the arch still needs recognizing.

Happy to contribute the `_QuantQwen3_5MoeExperts` plugin (quantizer registration + the non-transposed calib mixin) and validate the NVFP4 W4A4 path end-to-end on an RTX 5070 Ti (sm_120) if that's useful — will follow the `_QuantLlama4TextExperts` / `Gemma4` precedent and coordinate here first rather than opening a parallel PR. cc @jenchen13 @meenchen


### t-timms · 2026-09-06

Correcting my own comment above: I'd been testing against `nvidia-modelopt` **0.46.0** (latest on PyPI). On `main` (`a7f339ed0`) the picture is different —

- `_fused_experts_wrapper_class` in `modelopt/torch/quantization/plugins/huggingface.py` already lists **`Qwen3_5MoeExperts`** as a recognised gated fused layout, and `register_fused_experts_on_the_fly` / `force_eager_experts_impl_on_the_fly` are wired into `CUSTOM_MODEL_PLUGINS`.

So the **quantizer-registration** half of this issue looks already handled generically on `main` (landed after 0.46.0, e.g. #1421 / #1381 / #2046). Please disregard my offer to add a bespoke `_QuantQwen3_5MoeExperts` — the generic `_QuantFusedExperts` path supersedes it.

Two things I couldn't confirm and would value a pointer on:

1. **Export.** On 0.46.0, `export_hf_checkpoint` for this arch fails in `unified_export_hf.py::_prepare_moe_inputs` (`experts type '...' is not supported`), with the hard-coded list at `~:717` (`["Llama4TextExperts", "GptOssExperts"]`). Is the fused-3D export path covered for `Qwen3_5MoeExperts` on `main`, or is that the remaining part of this issue?
2. Is this slated for the **0.47** release? For anyone on 0.46.0 the whole `qwen3_5_moe` family (KAT-Coder, Ornith, Apodex, Qwen3.5-27B) currently NVFP4-quantizes to a bf16 MoE silently.

Happy to test a fix against a real REAP-50 `Qwen3_5MoeForConditionalGeneration` checkpoint on sm_120 if useful.

