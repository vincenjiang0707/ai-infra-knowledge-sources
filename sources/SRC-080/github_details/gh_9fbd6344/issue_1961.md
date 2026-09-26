# [Issue #1961] Is dtype of calibration_data the same as dtype of onnx?

source: https://github.com/NVIDIA/Model-Optimizer/issues/1961
state: closed | updated: 2026-07-20T17:34:50Z
labels: question

## 正文

Make sure you already checked the [examples](https://github.com/NVIDIA/Model-Optimizer/tree/main/examples) and [documentation](https://nvidia.github.io/Model-Optimizer/) before submitting an issue.

## How would you like to use ModelOpt

<!-- Description of what you would like to do with ModelOpt. -->

- My question is, I want to quantize my ONNX model (float32) to int8. Should the dtype (data type) of the calibration data be FLOAT32 or INT8?
```
import modelopt.onnx.quantization as moq

calibration_data = np.load(calibration_data_path)

moq.quantize(
    onnx_path=onnx_path,
    calibration_data=calibration_data,
    output_path="quant.onnx",
    quantize_mode="int8",
)
```

## 评论 (1)

### ajrasane · 2026-07-20

Hi @canyueduxuan , the calibration data should be float32. It must match the dtypes of your ONNX model's graph inputs, not the target quantization precision.

Calibration runs your original fp32 model with ONNX Runtime to collect activation statistics, which are then used to compute the int8 scaling factors. quantize_mode="int8" only controls the precision of the output model.

A couple of practical notes:

- ModelOpt does not cast the calibration data for you, the arrays are fed directly to the ONNX Runtime session, so each array's dtype must exactly match the corresponding graph input (e.g., float inputs -> np.float32; any integer inputs such as token IDs or masks keep their declared int32/int64 type).
- If your model has multiple inputs, pass a dict of arrays {input_name: np.ndarray} (e.g., an .npz file). The first dimension of each array is the total sample count, which gets split into batches according to the model/calibration_shapes batch size.
