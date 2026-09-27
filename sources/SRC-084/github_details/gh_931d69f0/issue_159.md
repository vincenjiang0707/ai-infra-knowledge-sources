# [Issue #159] `Quantizer.quantize` on CUDA returns NaN for every quantization bit

source: https://github.com/dropbox/hqq/issues/159
state: closed | updated: 2025-06-01T17:34:42Z
labels: 

## 正文

## Summary

When quantizing a constant matrix (where all values in a group are identical) on CUDA, `Quantizer.quantize` returns `scale` and `zero` as `NaN` and a `q_tensor` full of `NaN`.

## Code to Reproduce

```python
import torch
from hqq.core.quantize import Quantizer

matrix = torch.tensor([[ 9.0,  9.0],
                       [-9.0, -9.0]], 
                      dtype=torch.float32,
                      device="cuda")

q_tensor, meta = Quantizer.quantize(
    matrix,
    nbits=8,
    axis=1,
    group_size=2,
    optimize=True,
    round_zero=True,
    bitpack=False,
    view_as_float=False,
    device="cuda",
)

print("meta:", meta)
print("q_tensor:", q_tensor)
```

### Observed Output (on CUDA)

```
meta: {
    'nbits': 8,
    'group_size': 2,
    'shape': torch.Size([2, 2]),
    'scale': tensor([[5.0008e-05],
                     [5.0008e-05]], device='cuda:0', dtype=torch.float16),
    'zero': tensor([[nan],
                    [nan]], device='cuda:0', dtype=torch.float16),
    'axis': 1,
    'packing': None,
    'unpack_view_dtype': torch.uint8,
    'view_as_float': False
}
q_tensor: tensor([[nan, nan],
                  [nan, nan]], device='cuda:0')
```


Is this NaN result on CUDA an intended behavior? I guess it's because of the way that **optimizer** works. 


## 评论 (2)

### mobicham · 2025-06-01

Hey, thanks for reporting! It's an edge case when max == min along a dimension, which would be extremely rare in real-world models. It's fixed here: https://github.com/mobiusml/hqq/commit/373cbea93892cb491a3c072e0036a37848926404

```Python
import torch
from hqq.core.quantize import Quantizer

matrix = torch.tensor(
    [[9.0, 9.0], [-9.0, -9.0]], 
    dtype=torch.float32, 
    device="cuda"
)

q_tensor, meta = Quantizer.quantize(
    matrix,
    nbits=8,
    axis=1,
    group_size=2,
    device="cuda",
    optimize=True,
    bitpack=False,
)

matrix_deq = (
    (q_tensor.view([-1, meta['group_size']]) - meta['zero']) * meta['scale']
).view(meta['shape'])

print(matrix_deq)
tensor([[ 9.,  9.],
        [-9., -9.]], device='cuda:0')
```

### mohsenhariri · 2025-06-01

Great! Thanks!
