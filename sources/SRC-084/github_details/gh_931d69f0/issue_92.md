# [Issue #92] module 'torch.library' has no attribute 'custom_op'

source: https://github.com/dropbox/hqq/issues/92
state: closed | updated: 2024-07-16T07:49:20Z
labels: 

## 正文

When I'm trying to

```python
from hqq.utils.patching import prepare_for_inference
```

I got this error

```python
AttributeError                            Traceback (most recent call last)
Cell In[3], line 1
----> 1 from hqq.utils.patching import prepare_for_inference

File ~/hqq/hqq/utils/patching.py:11
      9 from ..backends.torchao import patch_hqq_to_aoint4
     10 from ..backends.marlin import patch_hqq_to_marlin
---> 11 from ..backends.bitblas import patch_hqq_to_bitblas
     14 def patch_linearlayers(model, fct, patch_param=None, verbose=False):
     15     base_class = model.base_class if (hasattr(model, "base_class")) else AutoHQQHFModel

File ~/hqq/hqq/backends/bitblas.py:20
     17 from ..core.peft import HQQLinearLoRA
     18 from ..core.utils import cleanup
---> 20 @torch.library.custom_op("hqq::matmul_bitblas", mutates_args=())
     21 def matmul_bitblas(x: Tensor, W_q: Tensor, scale: Tensor, zero: Tensor, out_features:int, eng_tag:str) -> Tensor:
     22 	origin_x_size = x.size()
     23 	x = x.reshape(-1, origin_x_size[-1])

AttributeError: module 'torch.library' has no attribute 'custom_op'
```

## 评论 (4)

### mobicham · 2024-07-15

Yeah this is something that just happened over the weekend, it was working fine on Friday, they changed something in the torch nightly, Will check with the torch team

### fahadh4ilyas · 2024-07-15

> Yeah this is something that just happened over the weekend, it was working fine on Friday, they changed something in the torch nightly, Will check with the torch team

Yeah, after I check pytorch, that function didn't even in version `2.3`. So, I have to comment bitblas import to make this works.

### mobicham · 2024-07-15

It's an advanced feature: https://pytorch.org/tutorials/advanced/python_custom_ops.html
Unfortunately, it's really necessary to use with BitBlas to be able to compile the model. I will see what the torch team says. Thanks for pointing this out!

### mobicham · 2024-07-16

I didn't get an answer from the torch team. For the moment, I removed the bitblas dependency, so it now the import should simply print a message and will not crash:
https://github.com/mobiusml/hqq/commit/e57104fdcac92bab2a3eed01e75bd30a837c1cfe
