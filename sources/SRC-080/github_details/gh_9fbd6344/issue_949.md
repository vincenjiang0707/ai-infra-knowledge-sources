# [Issue #949] Is there a max input size limitation in QAT INT8 CNN TRT model?

source: https://github.com/NVIDIA/Model-Optimizer/issues/949
state: closed | updated: 2026-06-24T04:30:54Z
labels: bug, stale, waiting for feedback, onnx.quantization, feature

## 正文

Hi, @ajrasane 

When input size is `h*w*c>=1024x1024x6`, QAT IN8 CNN model fail to convert TRT model. Is it a bug or do have this limitation?

Thank you for any answers.

<img width="431" height="318" alt="Image" src="https://github.com/user-attachments/assets/33f5a2f9-6a98-4fad-8542-0615e990baf3" />

## 评论 (5)

### ajrasane · 2026-04-02

@PonyPinkPie, which model are you trying this for? Could you share the model and steps you used to reproduce this issue? ModelOpt does not have any limits as such for the input dimensions of a model. We do check for certain conditions while deciding wether or not we quantize certain layers. For example:
- INT8: MHA BMMs excluded when seq_len > 512
- FP8: MHA BMMs excluded when head_size > 256 or head_size <= 8 
- INT8/FP8: MatMul excluded when M or N dimension == 1 (GEMV pattern)
- INT8/FP8: MatMul excluded when rank < 3 and any dim == 1 
- INT8: Conv excluded when input or output channels < 16 (with exceptions for first layer, square kernels, channels divisible by 8)
- INT8: Grouped conv excluded when channels < 16 unless out_channels % 8 == 0 and all kernel dims >= 3
- FP8: Conv excluded when filter_size > 32 (product of spatial dims)


### PonyPinkPie · 2026-04-03

> [@PonyPinkPie](https://github.com/PonyPinkPie), which model are you trying this for? Could you share the model and steps you used to reproduce this issue? ModelOpt does not have any limits as such for the input dimensions of a model. We do check for certain conditions while deciding wether or not we quantize certain layers. For example:
> 
> * INT8: MHA BMMs excluded when seq_len > 512
> * FP8: MHA BMMs excluded when head_size > 256 or head_size <= 8
> * INT8/FP8: MatMul excluded when M or N dimension == 1 (GEMV pattern)
> * INT8/FP8: MatMul excluded when rank < 3 and any dim == 1
> * INT8: Conv excluded when input or output channels < 16 (with exceptions for first layer, square kernels, channels divisible by 8)
> * INT8: Grouped conv excluded when channels < 16 unless out_channels % 8 == 0 and all kernel dims >= 3
> * FP8: Conv excluded when filter_size > 32 (product of spatial dims)

sorry, my bad, i just re-test my code and want to reproduce this result, however it can be converted successfully. 

anyway, thank you for your reply.

### PonyPinkPie · 2026-05-26

Hi @ajrasane 

# Here's what happened

1、I tested on an RTX4090D and encountered no issues. 
2、I tested on an RTX5090 and  discovered this issue and reported it. 
3、A month later, I attempted to reproduce the issue, but it did not occur during testing on the RTX4090D, so i closed it.
4、It was only recently, when I started testing on the RTX5090 again, that I realized the issue was related to GPU type.



# How to get qat int8 onnx model?
- normal training step to get best pth model
- using `mtq.quantize` to get quantized pth model
- normal training step to get best quantized pth model
- using `torch.save` to save best quantized pth model
- using `torch.load` to load best quantized pth model
- using `torch.onnx.export` to get quantized onnx model

Here is the onnx model https://github.com/PonyPinkPie/export/tree/main/ckpt

Convert command is 
```shell
trtexec --onnx=QAT-INT8-BCHW=Bx6x1024x1024.onnx \
--fp16 --int8 --saveEngine=QAT-INT8-BCHW=Bx6x1024x1024.engine \
--exportProfile=QAT-INT8-BCHW=Bx6x1024x1024.profile.json\
--exportLayerInfo=QAT-INT8-BCHW=Bx6x1024x1024.layerinfo.json \
--maxAuxStreams=0 --profilingVerbosity=detailed --noDataTransfers --useCudaGraph --useSpinWait --separateProfileRun \
--builderOptimizationLevel=5 --shapes=input_image:32x6x1024x1024 \
> QAT-INT8-BCHW=Bx6x1024x1024.log 

```

Hoping for any reply, thank you


### github-actions[bot] · 2026-06-09

Issue has not received an update in over 14 days. Adding stale label.

### github-actions[bot] · 2026-06-24

This issue was closed because it has been 14 days without activity since it has been marked as stale.
