# [Issue #30] Error when quantizing onnx model

source: https://github.com/NVIDIA/Model-Optimizer/issues/30
state: closed | updated: 2026-05-24T10:30:15Z
labels: 

## 正文

Hi,
This error occurred when I tried to quantize my onnx model.
```
Traceback (most recent call last):
  File "quant.py", line 4, in <module>
    quantize(
  File "/usr/local/lib/python3.8/dist-packages/modelopt/onnx/quantization/quantize.py", line 207, in quantize
    onnx_model = quantize_func(
  File "/usr/local/lib/python3.8/dist-packages/modelopt/onnx/quantization/int8.py", line 186, in quantize
    quantize_static(
  File "/usr/local/lib/python3.8/dist-packages/onnxruntime/quantization/quantize.py", line 513, in quantize_static
    calibrator.collect_data(calibration_data_reader)
  File "/usr/local/lib/python3.8/dist-packages/modelopt/onnx/quantization/ort_patching.py", line 271, in _collect_data_histogram_calibrator
    calibrator.intermediate_outputs.append(calibrator.infer_session.run(None, inputs))
  File "/usr/local/lib/python3.8/dist-packages/onnxruntime/capi/onnxruntime_inference_collection.py", line 220, in run
    return self._sess.run(output_names, input_feed, run_options)
onnxruntime.capi.onnxruntime_pybind11_state.Fail: [ONNXRuntimeError] : 1 : FAIL : CopyTensorAsync is not implemented
```
I have installed onnxruntime-gpu for cuda 12.x by https://onnxruntime.ai/docs/install/.
Could you help with that?

## 评论 (10)

### i-riyad · 2024-06-25

Please share the input ONNX model and the command to reproduce the error.

### DefTruth · 2024-08-09

same error, any one can help me? https://github.com/microsoft/onnxruntime/issues/21690

### DefTruth · 2024-08-09

@riyadshairi979 some warning
```bash
2024-08-09 18:31:40.646326213 [W:onnxruntime:, transformer_memcpy.cc:74 ApplyImpl] 680 Memcpy nodes are added to the graph main_graph for CUDAExecutionProvider. It might have negative impact on performance (including unable to run CUDA graph). Set session_options.log_severity_level=1 to see the detail logs before this message
```


### DefTruth · 2024-08-09

```bash
2024-08-09 10:50:50.360780: W external/xla/xla/service/gpu/nvptx_compiler.cc:718] The NVIDIA driver's CUDA version is 12.4 which is older than the ptxas CUDA version (12.5.40). Because the driver is older than the ptxas version, XLA is disabling parallel compilation, which may slow down compilation. You should update your NVIDIA driver or use the NVIDIA-provided CUDA forward compatibility packages.
INFO:root:Model vit_mlp_encoder/vit_mlp.onnx with opset_version 17 is loaded.
INFO:root:Quantization Mode: fp8
INFO:root:Quantizable op types in the model: ['MatMul', 'Conv']
INFO:root:Found unpaddable conv for FP8: /vision_model/embeddings/patch_embedding/Conv
INFO:root:Total number of nodes: 7544
INFO:root:Skipped node count: 1
WARNING:root:Please consider to run pre-processing before quantization. Refer to example: https://github.com/microsoft/onnxruntime-inference-examples/blob/main/quantization/image_classification/cpu/ReadMe.md
```

### DefTruth · 2024-08-09

using modelopt_examples:latest

### i-riyad · 2024-08-12

What is your onnxruntime version? Try using [this](https://github.com/NVIDIA/TensorRT-Model-Optimizer/tree/main/onnx_ptq#linux) docker.

### Roxbili · 2024-09-12

In my case, running the pre-processing step as described in the following document resolved the error.

```
WARNING:root:Please consider to run pre-processing before quantization. Refer to example: https://github.com/microsoft/onnxruntime-inference-examples/blob/main/quantization/image_classification/cpu/ReadMe.md
```

### i-riyad · 2025-09-09

We’ve re-encountered the issue and identified that mixed precision ONNX models (e.g., FP32 + FP16 ONNX exported with `torch.autocast` enabled) fail when multiple execution providers are passed to the ONNX Runtime inference session. ModelOpt uses autocast by default during INT8/FP8 ONNX export from PyTorch models.

To avoid the `CopyTensorAsync` issue, users should specify a single execution provider when calling the quantization API—for example: `calibration_eps = ["cpu"]` or `calibration_eps = ["cuda:0"]`.

### i-riyad · 2025-09-10

[This](https://github.com/NVIDIA/TensorRT-Model-Optimizer/pull/304) MR fixes the issue by skipping `torch.autocast` when a pure FP32 ONNX export is expected.

### lix19937 · 2026-05-24


(thoru_py) nv@lix:~/workspaces/thoru/quant_demo/examples/onnx_ptq$ python -m modelopt.onnx.quantization     --onnx_path=vit_base_patch16_224.onnx     --quantize_mode=fp8     --calibration_data=calib.npy     --calibration_method=max     --output_path=vit_base_patch16_224.quant.onnx  --calibration_eps cuda:0

```
2026-05-24 18:25:07,047 - [modelopt][onnx] - INFO - Starting quantization process for model: vit_base_patch16_224.onnx
2026-05-24 18:25:07,047 - [modelopt][onnx] - INFO - Quantization mode: fp8
2026-05-24 18:25:07,047 - [modelopt][onnx] - INFO - Preprocessing the model vit_base_patch16_224.onnx
2026-05-24 18:25:09,915 - [modelopt][onnx] - INFO - Found 0 custom layers and 1246 tensors
2026-05-24 18:25:10,949 - [modelopt][onnx] - INFO - No custom ops found. If that's not correct, please make sure that the 'tensorrt' python package is correctly installed and that the paths to 'libcudnn*.so' and TensorRT 'lib/' are in 'LD_LIBRARY_PATH'. If the custom op is not directly available as a plugin in TensorRT, please also make sure that the path to the compiled '.so' TensorRT plugin is also being given via the  '--trt_plugins' flag (requires TRT 10+).
2026-05-24 18:25:10,961 - [modelopt][onnx] - INFO - Duplicating shared constants
2026-05-24 18:25:11,125 - [modelopt][onnx] - INFO - Setting up CalibrationDataProvider for calibration
2026-05-24 18:25:11,300 - [modelopt][onnx] - INFO - Analyzing MHA nodes for fp8 quantization
2026-05-24 18:25:11,660 - [modelopt][onnx] - INFO - Creating ORT InferenceSession
2026-05-24 18:25:11,660 - [modelopt][onnx] - INFO - Checking for cuDNN library
2026-05-24 18:25:11,661 - [modelopt][onnx] - WARNING - cuDNN not found in LD_LIBRARY_PATH. Attempting onnxruntime.preload_dlls() to load from site-packages...
2026-05-24 18:25:11,661 - [modelopt][onnx] - INFO - onnxruntime.preload_dlls() succeeded — CUDA/cuDNN DLLs loaded from site-packages. Verify version compatibility at https://onnxruntime.ai/docs/execution-providers/CUDA-ExecutionProvider.html#requirements.
2026-05-24 18:25:11,661 - [modelopt][onnx] - INFO - Successfully enabled 1 EPs for ORT: [('CUDAExecutionProvider', {'device_id': 0})]
2026-05-24 18:25:11.817346317 [W:onnxruntime:, transformer_memcpy.cc:83 ApplyImpl] 16 Memcpy nodes are added to the graph main_graph for CUDAExecutionProvider. It might have negative impact on performance (including unable to run CUDA graph). Set session_options.log_severity_level=1 to see the detail logs before this message.
2026-05-24 18:25:11.819343273 [W:onnxruntime:, session_state.cc:1280 VerifyEachNodeIsAssignedToAnEp] Some nodes were not assigned to the preferred execution providers which may or may not have an negative impact on performance. e.g. ORT explicitly assigns shape related ops to CPU to improve perf.
2026-05-24 18:25:11.819352644 [W:onnxruntime:, session_state.cc:1282 VerifyEachNodeIsAssignedToAnEp] Rerunning with verbose output on a non-minimal build will show node assignments.
```

has 3 warnings.  
