# [Issue #20] mobilenet_v2_convert_qat.py 报错 Scale and Zero-point must be a scalar

source: https://github.com/Ascend/samples/issues/20
state: open | updated: 2025-11-10T15:11:28Z
labels: 

## 正文

一、问题现象（附报错日志上下文）：
```
Traceback (most recent call last):
  File "src/mobilenet_v2_convert_qat.py", line 73, in <module>
    main()
  File "src/mobilenet_v2_convert_qat.py", line 43, in main
    ort_session = ort.InferenceSession(model_path, amct.AMCT_SO)
  File "/home/ebaina/miniconda3/lib/python3.7/site-packages/onnxruntime/capi/onnxruntime_inference_collection.py", line 283, in __init__
    self._create_inference_session(providers, provider_options, disabled_optimizers)
  File "/home/ebaina/miniconda3/lib/python3.7/site-packages/onnxruntime/capi/onnxruntime_inference_collection.py", line 321, in _create_inference_session
    sess.initialize_session(providers, provider_options, disabled_optimizers)
onnxruntime.capi.onnxruntime_pybind11_state.Fail: [ONNXRuntimeError] : 1 : FAIL : Node (MobilenetV2/expanded_conv_2/add) Op (QLinearAdd) [TypeInferenceError] Scale and Zero-point must be a scalar
```

二、软件版本:
-- CANN 版本 (e.g., CANN 3.0.x，5.x.x):  Ascend-cann-toolkit_5.20.t6.2.b060_linux-x86_64
--Tensorflow/Pytorch/MindSpore 版本: 无
--Python 版本 (e.g., Python 3.7.5): 3.7.10
-- MindStudio版本 (e.g., MindStudio 2.0.0 (beta3)):
--操作系统版本 (e.g., Ubuntu 18.04):Ubuntu 18.04
--onnx 版本: 1.8.0
--onnxruntime 版本： 1.8.0

三、测试步骤：
按照https://gitee.com/ascend/samples/tree/master/python/level1_single_api/9_amct/amct_onnx/mobilenet_v2说明执行命令 python ./src/mobilenet_v2_convert_qat.py


四、日志信息:
```
Traceback (most recent call last):
  File "src/mobilenet_v2_convert_qat.py", line 73, in <module>
    main()
  File "src/mobilenet_v2_convert_qat.py", line 43, in main
    ort_session = ort.InferenceSession(model_path, amct.AMCT_SO)
  File "/home/ebaina/miniconda3/lib/python3.7/site-packages/onnxruntime/capi/onnxruntime_inference_collection.py", line 283, in __init__
    self._create_inference_session(providers, provider_options, disabled_optimizers)
  File "/home/ebaina/miniconda3/lib/python3.7/site-packages/onnxruntime/capi/onnxruntime_inference_collection.py", line 321, in _create_inference_session
    sess.initialize_session(providers, provider_options, disabled_optimizers)
onnxruntime.capi.onnxruntime_pybind11_state.Fail: [ONNXRuntimeError] : 1 : FAIL : Node (MobilenetV2/expanded_conv_2/add) Op (QLinearAdd) [TypeInferenceError] Scale and Zero-point must be a scalar
```

## 评论 (1)

### Ssecant · 2025-11-10

我也有这个问题，请问解决了吗？

