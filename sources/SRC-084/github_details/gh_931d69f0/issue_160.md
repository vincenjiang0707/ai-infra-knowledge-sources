# [Issue #160] Initializing HQQLinear with None no longer possible

source: https://github.com/dropbox/hqq/issues/160
state: closed | updated: 2025-06-12T17:22:14Z
labels: 

## 正文

We recently encountered an issue with [HQQ in the PEFT CI](https://github.com/huggingface/peft/actions/runs/15600206502/job/43938576455#step:6:155) which is probably caused by the release of the latest HQQ version. I could boil down the issue to the fact that `HQQLinear` cannot be initialized with `linear_layer=None` anymore. Here a small reproducer:

```python
from hqq.core.quantize import HQQLinear

quant_config = {
    'offload_meta': False,
    'scale_quant_params': None,
    'weight_quant_params': {
        'axis': 1,
        'channel_wise': True,
        'group_size': 64,
        'nbits': 4,
        'optimize': True,
        'round_zero': True,
        'view_as_float': False,
    },
    'zero_quant_params': None,
}
new_hqq_layer = HQQLinear(None, quant_config)
```

The error, `AttributeError: 'NoneType' object has no attribute 'named_parameters'`, is in this line:

https://github.com/mobiusml/hqq/blob/bc8f4c7d778a0cdbfe115299ea7253ed28948d31/hqq/core/quantize.py#L457-L458

Maybe the fix is as easy as to indent the whole block so that it's within the `if self.linear_layer is not None:` condition?

## 评论 (5)

### mobicham · 2025-06-12

Thanks for reporting! This should fix it https://github.com/mobiusml/hqq/commit/3b86ac950f699a4ca3584cb18bea023b2f5e1da9

### BenjaminBossan · 2025-06-12

Thanks a lot for the very quick fix. The test should be back to green with the next HQQ release.

### mobicham · 2025-06-12

Will do a new release later this day then!

### BenjaminBossan · 2025-06-12

Fantastic, thanks.

### mobicham · 2025-06-12

https://github.com/mobiusml/hqq/releases/tag/0.2.7.post1 should do it!
