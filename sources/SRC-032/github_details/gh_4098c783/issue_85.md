# [Issue #85] Conv3dv2 only supports groups = 1 or groups = cin

source: https://github.com/Ascend/pytorch/issues/85
state: open | updated: 2025-10-16T08:33:57Z
labels: 

## 正文

I attempted to run [Open-Sora 2.0](https://github.com/hpcaitech/Open-Sora) DC-AE inference on NPU  and got this error:

```
[rank0]:   File "xxx/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 603, in _conv_forward
[rank0]:     return F.conv3d(
[rank0]: RuntimeError: call aclnnConvolution failed, detail:EZ1001: [PID: xxx] 2025-xx-xx-17:44:xxx Conv3dv2 only supports groups = 1 or groups = cin
[rank0]:         TraceBack (most recent call last):
[rank0]:         conv3d raise an unknown error
[rank0]:         check the condition which is "ret == ACLNN_SUCCESS" failed, except the condition is true.
``` 
## Specs

`python3.9.10`,`CANN-8.0.RC3`, `torch-npu==2.4.0`

## Question 
The issue occurs only when using `torch.npu.config.allow_internal_format = False`. There is no issue using  `True` but inference is extremely slow, this is why i planned to try with  `True` as well.
Is there a way to overcome this issue and successfully run the inference using   `torch.npu.config.allow_internal_format = False`? Can the issue relate to https://github.com/Ascend/pytorch/issues/73 ? 

More info: https://github.com/hpcaitech/Open-Sora/issues/884


## 评论 (6)

### yunyiyun · 2025-10-14

Can you provide the minimum reproduction case, which is to save the input of the error operator and see if it can be reproduced separately

### 3manifold · 2025-10-14

# Description 
This is a modified version of [test_npu_conv3d.py](https://github.com/Ascend/pytorch/blob/master/test/custom_ops/test_npu_conv3d.py), adjusted for `groups=2`. It tests  both `conv3d_fp16` and `conv3d_fp32`. Although `test_npu_conv3d_fp16()` passes, `test_npu_conv3d_fp32()` fails with an error. 


# Error message
```
RuntimeError: call aclnnConvolution failed, detail:EZ1001: [PID: 3608462] Conv3dv2 only supports groups = 1 or groups = cin
        TraceBack (most recent call last):
        conv3d raise an unknown error
        check the condition which is "ret == ACLNN_SUCCESS" failed, except the condition is true.

[ERROR] (PID:3608462, Device:0, RankID:0) ERR01100 OPS call acl api failed
```

# Test code  

```bash
#!/bin/bash

PYTHONPATH=$(pwd) \
DEVICE_TYPE=npu \
ASCEND_RT_VISIBLE_DEVICES=0 \
ASCEND_LAUNCH_BLOCKING=0 \
torchrun --standalone --nproc_per_node 1 \
test_npu_conv3d.py 
```

```python
import numpy as np
import torch
import os
import torch_npu 
from numpy.testing import assert_array_equal, assert_array_almost_equal 

torch.npu.config.allow_internal_format = False 

def get_npu_device():
    npu_device = os.environ.get('SET_NPU_DEVICE')
    if npu_device is None:
        npu_device = "npu:0"
    else:
        npu_device = f"npu:{npu_device}"
    return npu_device

def create_common_tensor(item, minValue, maxValue, device=None):
    if device is None:
        device = get_npu_device()

    dtype = item[0]
    npu_format = item[1]
    shape = item[2]
    input1 = np.random.uniform(minValue, maxValue, shape).astype(dtype)
    cpu_input = torch.from_numpy(input1)
    npu_input = torch.from_numpy(input1).to(device)
    if npu_format != -1:
        npu_input = torch_npu.npu_format_cast(npu_input, npu_format)
    return cpu_input, npu_input

 

def custom_op_exec( input1, weight, bias, stride, padding, dilation, groups):
    output = torch.nn.functional.conv3d(input1, weight, bias, stride, padding, dilation, groups)
    output = output.cpu().numpy()
    return output

def npu_op_exec( input1, weight, bias, stride, padding, dilation, groups):
    output = torch_npu.npu_conv3d(input1, weight, bias, stride, padding, dilation, groups)
    output = output.cpu().numpy()
    return output

def test_npu_conv3d_fp16(): 
    shape_format = [
        # Format: [input, weight, bias, stride, padding, dilation, groups]
        # Adjusted for groups=2: input_channels=128, output_channels=2, weight=[2, 64, 3, 3, 3]
        [
            [np.float16, 30, [1, 128, 4, 14, 14]], 
            [np.float16, 30, [2, 64, 3, 3, 3]], 
            None, 
            [1, 1, 1], 
            [1, 1, 1],
            [1, 1, 1], 
            2
        ],
        # Adjusted for groups=2: input_channels=64, output_channels=4, weight=[4, 32, 3, 3, 3]
        [
            [np.float16, 30, [1, 64, 4, 14, 14]], 
            [np.float16, 30, [4, 32, 3, 3, 3]], 
            None, 
            [1, 1, 1], 
            [2, 2, 2],
            [1, 1, 1], 
            2
        ],
        # Adjusted for groups=2: input_channels=16, output_channels=32, weight=[32, 8, 3, 3, 3], bias=[32]
        [
            [np.float16, 30, [20, 16, 50, 10, 20]], 
            [np.float16, 30, [32, 8, 3, 3, 3]], 
            [np.float16, 2, [32]],
            [1, 1, 1], 
            [2, 2, 2], 
            [1, 1, 1], 
            2
        ],
    ]

    for item in shape_format:
        _, input_npu = create_common_tensor(item[0], -1, 1)
        _, weight_npu = create_common_tensor(item[1], -1, 1)
        _, bias_npu = create_common_tensor(item[2], -1, 1) if item[2] else None, None
        custom_output = custom_op_exec(input_npu,
                                            weight_npu,
                                            bias_npu,
                                            stride=item[3],
                                            padding=item[4],
                                            dilation=item[5],
                                            groups=item[6])
        npu_output = npu_op_exec(input_npu,
                                        weight_npu,
                                        bias_npu,
                                        stride=item[3],
                                        padding=item[4],
                                        dilation=item[5],
                                        groups=item[6])
        # print(npu_output)
        assert_array_equal(custom_output, npu_output)


def test_npu_conv3d_fp32(): 
    shape_format = [
        # Format: [input, weight, bias, stride, padding, dilation, groups]
        # Adjusted for groups=2: input_channels=128, output_channels=2, weight=[2, 64, 3, 3, 3]
        [
            [np.float32, 30, [1, 128, 4, 14, 14]], 
            [np.float32, 30, [2, 64, 3, 3, 3]], 
            None, 
            [1, 1, 1], 
            [1, 1, 1],
            [1, 1, 1], 
            2
        ],
        # Adjusted for groups=2: input_channels=64, output_channels=4, weight=[4, 32, 3, 3, 3]
        [
            [np.float32, 30, [1, 64, 4, 14, 14]], 
            [np.float32, 30, [4, 32, 3, 3, 3]], 
            None, 
            [1, 1, 1], 
            [2, 2, 2],
            [1, 1, 1], 
            2
        ],
        # Adjusted for groups=2: input_channels=16, output_channels=32, weight=[32, 8, 3, 3, 3], bias=[32]
        [
            [np.float32, 30, [20, 16, 50, 10, 20]], 
            [np.float32, 30, [32, 8, 3, 3, 3]], 
            [np.float32, 2, [32]],
            [1, 1, 1], 
            [2, 2, 2], 
            [1, 1, 1], 
            2
        ],
    ]

    for item in shape_format:
        _, input_npu = create_common_tensor(item[0], -1, 1)
        _, weight_npu = create_common_tensor(item[1], -1, 1)
        _, bias_npu = create_common_tensor(item[2], -1, 1) if item[2] else None, None
        custom_output = custom_op_exec(input_npu,
                                            weight_npu,
                                            bias_npu,
                                            stride=item[3],
                                            padding=item[4],
                                            dilation=item[5],
                                            groups=item[6])
        npu_output = npu_op_exec(input_npu,
                                        weight_npu,
                                        bias_npu,
                                        stride=item[3],
                                        padding=item[4],
                                        dilation=item[5],
                                        groups=item[6])
        assert_array_equal(custom_output, npu_output)

 

if __name__ == "__main__": 
    test_npu_conv3d_fp16()
    test_npu_conv3d_fp32()
```

### yunyiyun · 2025-10-15

Thank you for your feedback. We will analyze it

### yunyiyun · 2025-10-16

The cann version is too old. We recommend using the new cann 8.1.rc1 and later versions，as well as the torch.nn.functionalist.conv3d interface


### 3manifold · 2025-10-16

> The cann version is too old. We recommend using the new cann 8.1.rc1 and later versions，as well as the torch.nn.functionalist.conv3d interface

Does this mean that  `cann 8.1.rc1` support any `groups` value?

### yunyiyun · 2025-10-16

As long as it meets Torch's requirements for the groups, it's fine
