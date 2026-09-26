# [Issue #1895] warnings.warn(f"RealQuantLinear: No real-quant GEMM found: {self}.")

source: https://github.com/NVIDIA/Model-Optimizer/issues/1895
state: closed | updated: 2026-09-03T20:06:27Z
labels: bug, waiting for feedback, torch.quantization, model support

## 正文

## Describe the bug
I followed this [quant recipe](https://github.com/NVlabs/alpamayo-recipes/tree/main/recipes/alpamayo1_5_quant#readme) to quantize Alpamayo 1.5 to FP8 on B300. First, I ran the quantize.py to quantize Alpamayo 1.5 to FP8 and save the FP8 model (mtq.compress() is called before saving). It was successfully saved. Then, when I ran the eval.py to test the FP8 model, I got the error:
```
.../lib/python3.12/site-packages/modelopt/torch/quantization/nn/modules/quant_linear.py:214: UserWarning: RealQuantLinear: No real-quant GEMM found: RealQuantQuantLinear(
  in_features=2048, out_features=2, bias=True
  (input_quantizer): TensorQuantizer((4, 3) bit fake per-tensor amax=2.7363 calibrator=MaxCalibrator quant)
  (output_quantizer): TensorQuantizer(disabled)
  (weight_quantizer): TensorQuantizer((4, 3) bit per-tensor amax=0.1025 calibrator=MaxCalibrator quant)
).
  warnings.warn(f"RealQuantLinear: No real-quant GEMM found: {self}.")
```

I only tested on B300, so I'm not sure if that's because Blackwell is not well supported or it's a general issue.

### Steps/Code to reproduce bug
Please follow https://github.com/NVlabs/alpamayo-recipes/tree/main/recipes/alpamayo1_5_quant#readme to install ENV. and then run:
```
# quant + save model
python quantize.py --quant_format=fp8 --num_of_calib_clips=10 --save_model_dir=./outputs

# eval
python eval.py --ckpt ./outputs/alpamayo1.5_fp8_calib10
# then the error pops up
```

### Expected behavior
The eval script should run in FP8 without error.

### Who can help?

<!-- To expedite the response to your issue, it would be helpful if you could identify the appropriate person(s) to tag using the @ symbol.
If you are unsure about whom to tag, you can leave it blank, and we will make sure to involve the appropriate person. -->

- ?

## System information

<!-- Run this script to automatically collect system information: https://github.com/NVIDIA/Model-Optimizer/blob/main/.github/ISSUE_TEMPLATE/get_system_info.py -->

- Container used (if applicable): nvcr.io/nvidia/pytorch:26.04-py3
- OS (e.g., Ubuntu 22.04, CentOS 7, Windows 10): ? <!-- If Windows, please add the `windows` label to the issue. --> Ubuntu 22.04
- CPU architecture (x86_64, aarch64): x86_64
- GPU name (e.g. H100, A100, L40S): B300
- GPU memory size: ?
- Number of GPUs: ?
- Library versions (if applicable):
  - Python: 3.12
  - ModelOpt version or commit hash: 0.43
  - CUDA: 13.2
  - PyTorch: 2.12.1
  - Transformers: ?
  - TensorRT-LLM: ?
  - ONNXRuntime: ?
  - TensorRT: ?
- Any other details that may help: ?


## 评论 (16)

### h-guo18 · 2026-07-05

Hi @cjluo-nv , could you take a look at this bug. Thanks


### rohansjoshi · 2026-07-07

You shared a warning, not an error? Could you share the full log?

We have a working example [here](https://github.com/NVIDIA/Model-Optimizer/tree/main/examples/alpamayo) for Alpamayo-1 quantization, and the exported checkpoint can be evaluated with eval.py.

### zewenli98 · 2026-07-21

@rohansjoshi yes that's just warning. It's just the same repetitive warnings. That example you shared is AM1 but we are working on AM1.5 now.
```
action_out_proj.input_quantizer                                                  TensorQuantizer((4, 3) bit fake per-tensor amax=2.7363 calibrator=MaxCalibrator quant)
action_out_proj.output_quantizer                                                 TensorQuantizer(disabled)
action_out_proj.weight_quantizer                                                 TensorQuantizer((4, 3) bit per-tensor amax=0.1025 calibrator=MaxCalibrator quant)
2274 TensorQuantizers found in model

Evaluating clips:   0%|          | 0/644 [00:00<?, ?it/s]/home/scratch.zewenl_sw/docker_workspace/alpamayo-recipes/recipes/alpamayo1_5_quant/am15_quant/lib/python3.12/site-packages/modelopt/torch/quantization/nn/modules/quant_linear.py:214: UserWarning: RealQuantLinear: No real-quant GEMM found: RealQuantQuantLinear(
  in_features=1152, out_features=3456, bias=True
  (input_quantizer): TensorQuantizer((4, 3) bit fake per-tensor amax=14.6172 calibrator=MaxCalibrator quant)
  (output_quantizer): TensorQuantizer(disabled)
  (weight_quantizer): TensorQuantizer((4, 3) bit per-tensor amax=0.5820 calibrator=MaxCalibrator quant)
).
  warnings.warn(f"RealQuantLinear: No real-quant GEMM found: {self}.")
Loading extension modelopt_cuda_ext_fp8...
/home/scratch.zewenl_sw/docker_workspace/alpamayo-recipes/recipes/alpamayo1_5_quant/am15_quant/lib/python3.12/site-packages/modelopt/torch/quantization/nn/modules/quant_linear.py:214: UserWarning: RealQuantLinear: No real-quant GEMM found: RealQuantQuantLinear(
  in_features=1152, out_features=1152, bias=True
  (input_quantizer): TensorQuantizer((4, 3) bit fake per-tensor amax=3.0254 calibrator=MaxCalibrator quant)
  (output_quantizer): TensorQuantizer(disabled)
  (weight_quantizer): TensorQuantizer((4, 3) bit per-tensor amax=0.3027 calibrator=MaxCalibrator quant)
).
  warnings.warn(f"RealQuantLinear: No real-quant GEMM found: {self}.")
/home/scratch.zewenl_sw/docker_workspace/alpamayo-recipes/recipes/alpamayo1_5_quant/am15_quant/lib/python3.12/site-packages/modelopt/torch/quantization/nn/modules/quant_linear.py:214: UserWarning: RealQuantLinear: No real-quant GEMM found: RealQuantQuantLinear(
  in_features=1152, out_features=4304, bias=True
  (input_quantizer): TensorQuantizer((4, 3) bit fake per-tensor amax=31.6250 calibrator=MaxCalibrator quant)
  (output_quantizer): TensorQuantizer(disabled)
  (weight_quantizer): TensorQuantizer((4, 3) bit per-tensor amax=0.3945 calibrator=MaxCalibrator quant)
).
  warnings.warn(f"RealQuantLinear: No real-quant GEMM found: {self}.")
/home/scratch.zewenl_sw/docker_workspace/alpamayo-recipes/recipes/alpamayo1_5_quant/am15_quant/lib/python3.12/site-packages/modelopt/torch/quantization/nn/modules/quant_linear.py:214: UserWarning: RealQuantLinear: No real-quant GEMM found: RealQuantQuantLinear(
  in_features=4304, out_features=1152, bias=True
  (input_quantizer): TensorQuantizer((4, 3) bit fake per-tensor amax=20.5469 calibrator=MaxCalibrator quant)
  (output_quantizer): TensorQuantizer(disabled)
  (weight_quantizer): TensorQuantizer((4, 3) bit per-tensor amax=0.2236 calibrator=MaxCalibrator quant)
).
  warnings.warn(f"RealQuantLinear: No real-quant GEMM found: {self}.")
/home/scratch.zewenl_sw/docker_workspace/alpamayo-recipes/recipes/alpamayo1_5_quant/am15_quant/lib/python3.12/site-packages/modelopt/torch/quantization/nn/modules/quant_linear.py:214: UserWarning: RealQuantLinear: No real-quant GEMM found: RealQuantQuantLinear(
  in_features=1152, out_features=3456, bias=True
  (input_quantizer): TensorQuantizer((4, 3) bit fake per-tensor amax=20.9375 calibrator=MaxCalibrator quant)
  (output_quantizer): TensorQuantizer(disabled)
  (weight_quantizer): TensorQuantizer((4, 3) bit per-tensor amax=0.4570 calibrator=MaxCalibrator quant)
).
  warnings.warn(f"RealQuantLinear: No real-quant GEMM found: {self}.")
...
...
...
/home/scratch.zewenl_sw/docker_workspace/alpamayo-recipes/recipes/alpamayo1_5_quant/am15_quant/lib/python3.12/site-packages/modelopt/torch/quantization/nn/modules/quant_linear.py:214: UserWarning: RealQuantLinear: No real-quant GEMM found: RealQuantQuantLinear(
  in_features=2048, out_features=2, bias=True
  (input_quantizer): TensorQuantizer((4, 3) bit fake per-tensor amax=2.7363 calibrator=MaxCalibrator quant)
  (output_quantizer): TensorQuantizer(disabled)
  (weight_quantizer): TensorQuantizer((4, 3) bit per-tensor amax=0.1025 calibrator=MaxCalibrator quant)
).
  warnings.warn(f"RealQuantLinear: No real-quant GEMM found: {self}.")

Evaluating clips:   0%|          | 1/644 [02:56<31:36:22, 176.96s/it]
```

### ChenhanYu · 2026-08-02

Software Release Triage
release: ModelOpt v0.46.0
fingerprint: ffb014e3d2d9368b5dd140f801346aff041e29b1ba5fa3ec508827e0887890e0

This open issue is in the ModelOpt release sweep. Owner: confirm release impact, linked fix/validation, or that it is non-blocking for this release.

### ChenhanYu · 2026-08-02

Software Release Triage
release: ModelOpt v0.46.0
fingerprint: 8fdc0b27b7c5152f6706bc59f544442bde203a29e1dfa41a5c4c0ae5f8a552ce

This open issue is in the ModelOpt release sweep. Owner: confirm release impact, linked fix/validation, or that it is non-blocking for this release.

### ChenhanYu · 2026-08-02

Software Release Triage
release: ModelOpt v0.46.0
fingerprint: 185b355406e4c755d5cbbe472f73e91e38aa1082a0271e36e7dcb723ef37741a

Release follow-up: this open ModelOpt issue needs release relevance confirmed. Link its planned fix/validation, or confirm it is not a v0.46.0 blocker.

### abd-gang · 2026-08-17

Hi
I got the same wwrnings and my fp8 underperfoms the basline fp16. Have we got any solution for this? 

I tried to run on Nvidia Thor and rtx pro 6000 blackwell. Got same issue on both

Thanks

### rohansjoshi · 2026-08-17

Works for me on RTX Pro 6000 Blackwell (torch 2.10.0+cu128), can you try with these imports?
```
from modelopt.torch.quantization.backends.fp8_per_tensor_gemm import Fp8PerTensorLinear
from modelopt.torch.quantization.backends.gemm_registry import gemm_registry
from modelopt.torch.quantization.backends.utils import fp8_compatible
```

### abd-gang · 2026-08-18

Hi @rohansjoshi 

I tried with exact torch cuda what you mentioned on rtx pro 6000. Still I got those warnings and inference is slower than fp16 for fp8.  Also, those imports are already there in place I checked. 

Did you make any other changes? Also, did you see difference in inference time with fp8 and auto quant? 

My lib-

torch : 2.10.0+cu128
Nvidia model opt : 0.43.0

Thanks

### abd-gang · 2026-08-18

Tried with latest Nvidia model opt 0.45 and got this 


Name: torch
Version: 2.10.0+cu128

Name: nvidia-modelopt
Version: 0.45.0

`python3 quantize.py --quant_format=fp8 --num_of_calib_clips=10 --save_model_dir=./outputs/`


Quantization done-- 

2398 TensorQuantizers found in model
[2026-08-18 08:06:17,852][__main__][INFO] - [rank: 0] Compressing quantized weights to real low-bit format (mtq.compress) ...
/usr/local/lib/python3.12/dist-packages/modelopt/torch/quantization/compress.py:117: UserWarning: Real quantization has been applied to the model. This feature is still experimental, and some functionalities may not be supported. For example, converting the model back to its original state or saving and restoring the quantized model may not be available.
  warnings.warn(
[2026-08-18 08:06:18,349][__main__][INFO] - [rank: 0] Compression complete.
[2026-08-18 08:06:18,349][__main__][INFO] - [rank: 0] Saving quantized model to: ./outputs/alpamayo1.5_fp8_calib10
Saved ModelOpt state to ./outputs/alpamayo1.5_fp8_calib10/modelopt_state.pth
[2026-08-18 08:06:43,877][__main__][INFO] - [rank: 0] Quantized model saved to: ./outputs/alpamayo1.5_fp8_calib10


Now running the quantised model.

`python eval.py --ckpt ./outputs/alpamayo1.5_fp8_calib10`

Skipping import of cpp extensions due to incompatible torch version 2.10.0+cu128 for torchao version 0.15.0             Please see https://github.com/pytorch/ao/issues/2919 for more info
/usr/local/lib/python3.12/dist-packages/modelopt/torch/utils/import_utils.py:35: UserWarning: Failed to import modelopt transformer_engine plugin due to: ImportError('/usr/local/lib/python3.12/dist-packages/transformer_engine/transformer_engine_torch.cpython-312-x86_64-linux-gnu.so: undefined symbol: _ZNK3c104cuda10CUDAStream5queryEv'). You may ignore this warning if you do not need this plugin.
  warn_rank_0(
[2026-08-18 06:40:00,675][__main__][INFO] - [rank: 0] Loaded 306152 clip_ids from local dataset: /workspace/hf/PhysicalAI-Autonomous-Vehicles-Subset/
[2026-08-18 06:40:00,678][__main__][INFO] - [rank: 0] Evaluating 10 clips (limit=10)
[2026-08-18 06:40:00,679][__main__][INFO] - [rank: 0] Clip IDs: ['25cd4769-5dcf-4b53-a351-bf2c5deb6124', '2edf278f-d5e3-4b83-b5df-923a04335725', 'eed514a0-a366-4550-b9bd-4c296c531511', 'ecafce84-447d-43a6-aff1-b385fbc71f15', '1f47bf7f-d233-480c-b166-7512d8e9ac97', 'c6915a10-9f22-464d-a422-15b8960a57d7', 'ea5c5be6-5e18-4489-9784-8f73860f887b', '1fcf2fef-279b-4490-adc6-9b7d1ff0118d', 'ef4264ed-0fd2-4a64-9831-87e1aae28407', '30f3d243-f26e-43f9-a63a-ac5d1b115d15']
Initialized OfflinePhysicalAIAVDatasetInterface from /workspace/hf/PhysicalAI-Autonomous-Vehicles-Subset/ 306152 clips available
[2026-08-18 06:40:00,770][__main__][INFO] - [rank: 0] Using OFFLINE local dataset from: /workspace/hf/PhysicalAI-Autonomous-Vehicles-Subset/
ModelOpt save/restore enabled for `transformers` library.
ModelOpt save/restore enabled for `diffusers` library.
ModelOpt save/restore enabled for `peft` library.
`torch_dtype` is deprecated! Use `dtype` instead!
Registered <class 'transformers.models.qwen3_vl.modeling_qwen3_vl.Qwen3VLVisionAttention'> to _QuantAttention for KV Cache quantization
Registered <class 'transformers.models.qwen3_vl.modeling_qwen3_vl.Qwen3VLTextAttention'> to _QuantAttention for KV Cache quantization
Inserted 2398 quantizers
Restored ModelOpt state from ./outputs/alpamayo1.5_fp8_calib10/modelopt_state.pth
Loading checkpoint shards: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 3/3 [00:00<00:00, 10.19it/s]
Some weights of the model checkpoint at ./outputs/alpamayo1.5_fp8_calib10 were not used when initializing Alpamayo1_5: ['vlm.model.language_model.embed_tokens.weight_quantizer._scale', 'vlm.model.visual.pos_embed.weight_quantizer._scale']
This IS expected if you are initializing Alpamayo1_5 from the checkpoint of a model trained on another task or with another architecture (e.g. initializing a BertForSequenceClassification model from a BertForPreTraining model).
This IS NOT expected if you are initializing Alpamayo1_5 from the checkpoint of a model that you expect to be exactly identical (initializing a BertForSequenceClassification model from a BertForSequenceClassification model).
Evaluating clips:   0%|                                                                                                                                         | 0/10 [00:00<?, ?it/s]it is..... :  Evaluating clips:   0%|                                                                                                                                         | 0/10 [00:00<?, ?it/s]
[2026-08-18 06:40:09,754][__main__][INFO] - [rank: 0] [1/10] FAILED clip_id=25cd4769-5dcf-4b53-a351-bf2c5deb6124: self._dequantize is True and self.fake_quant is False. This case should have been handled.
.....
.....
[2026-08-18 06:40:29,798][__main__][INFO] - [rank: 0] No successful clips; average minADE not computed.
[2026-08-18 06:40:29,799][__main__][INFO] - [rank: 0]

[2026-08-18 06:40:29,799][__main__][INFO] - [rank: 0] Failed clips: 10
[2026-08-18 06:40:29,799][__main__][INFO] - [rank: 0]   25cd4769-5dcf-4b53-a351-bf2c5deb6124: ValueError('self._dequantize is True and self.fake_quant is False. This case should have been handled.')
[2026-08-18 06:40:29,799][__main__][INFO] - [rank: 0]   2edf278f-d5e3-4b83-b5df-923a04335725: ValueError('self._dequantize is True and self.fake_quant is False. This case should have been handled.')
[2026-08-18 06:40:29,799][__main__][INFO] - [rank: 0]   eed514a0-a366-4550-b9bd-4c296c531511: ValueError('self._dequantize is True and self.fake_quant is False. This case should have been handled.')
[2026-08-18 06:40:29,799][__main__][INFO] - [rank: 0]   ecafce84-447d-43a6-aff1-b385fbc71f15: ValueError('self._dequantize is True and self.fake_quant is False. This case should have been handled.')
[2026-08-18 06:40:29,799][__main__][INFO] - [rank: 0]   1f47bf7f-d233-480c-b166-7512d8e9ac97: ValueError('self._dequantize is True and self.fake_quant is False. This case should have been handled.')
[2026-08-18 06:40:29,799][__main__][INFO] - [rank: 0]   c6915a10-9f22-464d-a422-15b8960a57d7: ValueError('self._dequantize is True and self.fake_quant is False. This case should have been handled.')
[2026-08-18 06:40:29,799][__main__][INFO] - [rank: 0]   ea5c5be6-5e18-4489-9784-8f73860f887b: ValueError('self._dequantize is True and self.fake_quant is False. This case should have been handled.')
[2026-08-18 06:40:29,799][__main__][INFO] - [rank: 0]   1fcf2fef-279b-4490-adc6-9b7d1ff0118d: ValueError('self._dequantize is True and self.fake_quant is False. This case should have been handled.')
[2026-08-18 06:40:29,799][__main__][INFO] - [rank: 0]   ef4264ed-0fd2-4a64-9831-87e1aae28407: ValueError('self._dequantize is True and self.fake_quant is False. This case should have been handled.')
[2026-08-18 06:40:29,799][__main__][INFO] - [rank: 0]   30f3d243-f26e-43f9-a63a-ac5d1b115d15: ValueError('self._dequantize is True and self.fake_quant is False. This case should have been handled.')
`

Thanks


### abd-gang · 2026-08-20

@rohansjoshi @ChenhanYu 

Any update on this? I am blocked because of this issue. 

### abd-gang · 2026-08-22

Any update? 

Thanks.

### rohansjoshi · 2026-08-24

Here's a one-line fix: in `alpamayo-recipes/recipes/alpamayo1_5_quant/utils.py`, `FP8_CONFIG`:
 ```
 -        "*patch_embed*": {"enable": False},
 +        "*embed*": {"enable": False},
```
`*embed*` subsumes `*patch_embed*` and also adds `embed_tokens` and `visual.pos_embed`. The problem can be traced down to the fact that real-quant is not currently implemented for embedding layers, so we should skip them. 

### abd-gang · 2026-08-26

Not sure. But it didn't work out for me. 
On rtx pro 6000 -
Best case scenario  for alpamayo r1.5 inference -

Inference time fp16 : 1200ms approx 
Inference time fp8   : 2500ms approx

So as per document, I am not seeing any speed up. Also, even after making those changes, I am still seeing those warnings. 

Library -
Model opt - 0.43
Torch - 2.8 cuda 12.9



### abd-gang · 2026-08-31

Any update? 

### zewenli98 · 2026-09-03

Hi @abd-gang, I figured out the warning is from two issues:
1. The real FP8 GEMM kernel requires dimensions are divisible by 16.
[Our recipe](https://github.com/NVlabs/alpamayo-recipes/blob/main/recipes/alpamayo1_5_quant/utils.py#L64) currently has only `"*patch_embed*": {"enable": False}`, but all of the following layers should be disabled because their dims are not divisible by 16:
```
"*patch_embed*": {"enable": False},
"*lm_head*": {"enable": False},
"*action_in_proj.encoder.trunk.0*": {"enable": False},
"*action_out_proj*": {"enable": False},
```
In Alpamayo 1.5, the shape of `*lm_head*` is (4096x155697). The second dim is not divisible by 16. The shape of `action_in_proj.encoder.trunk.0` is 60 → 512. Since 60 is not divisible by 16, real FP8 GEMM cannot run it. `action_out_proj` (2048 → 2) will fail next.

2. With the patch above, a new issue will occur: ModelOpt’s `@torch.compile(dynamic=True)` FP8 kernel gives symbolic weight dimensions to `torch._scaled_mm`, which cannot prove they are divisible by 16 even though the actual dimensions are divisible by 16. So this is a PyTorch/ModelOpt dynamic-compilation compatibility issue. Running that FP8 kernel eagerly (register ModelOpt's real FP8 GEMM while bypassing its dynamic torch.compile) is a workaround. You can add the following two lines in the [eval.py](https://github.com/NVlabs/alpamayo-recipes/blob/main/recipes/alpamayo1_5_quant/eval.py#L17):
```
import modelopt.torch.quantization.backends.fp8_per_tensor_gemm as fp8_backend
fp8_backend._fp8_gemm_impl = fp8_backend._fp8_gemm_impl.__wrapped__
```

I verified the fix works on H100. I didn't get a chance to benchmark the accuracy and latency but please feel free to report your results here! 

cc: @rohansjoshi 
