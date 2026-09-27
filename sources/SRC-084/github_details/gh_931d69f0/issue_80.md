# [Issue #80] [Question] Model Outputting Gibberish After Quantization

source: https://github.com/dropbox/hqq/issues/80
state: closed | updated: 2024-06-04T10:38:47Z
labels: 

## 正文

```python
quantization_config = HqqConfig(nbits=2, group_size=64, quant_zero=False, quant_scale=False, axis=1)
```

Model outputs gibberish after being quantized to two bits. 
Model is `1048k context length Llama 3 8b`. 

```
 we you this perfect L only only you only last you you June R you last you you you only last only you it unit last only we you you last this last last.
 you you June last  last.
 only  this last this last you you it  last it last last.
 you.
 only this only it it last only this on only last love last travel Kr  last you.
 you it June last this last all.
 you on last only you this last unit last you.
 you.
 only p last you last you you last last travel only you.
 love you p last only you last you this this this last you only it this last last last @
```


## 评论 (4)

### mobicham · 2024-06-03

Hello! Well, that's expected with such a small model without calibration.
 
Use 4-bit instead with Llama3-8B, you should get better results than GPTQ/AWQ and you can run inference very fast via the `torchao_int4` backend: https://github.com/mobiusml/hqq/?tab=readme-ov-file#faster-inference

```Python
quantization_config = HqqConfig(nbits=4, group_size=64, quant_zero=False, quant_scale=False, axis=1)
```

### DefinitlyEvil · 2024-06-03

@mobicham Hi thanks for the note. Will it be faster or better than BnB implementation? I am kinda limited by the VRAM so I wanted to compress the model even harder than it might should be. xD Thanks again for the info! 

### mobicham · 2024-06-03

No problem!
Yeah it should run much faster following this example (using an older version of transformers): https://github.com/mobiusml/hqq/blob/master/examples/backends/torchao_int4_demo.py
This requires a relatively new gpu though (3090 or 4090).

Yeah, unfortunately Llama3-8B is pretty difficult to quantize at lower bits without some kind of calibration!

### DefinitlyEvil · 2024-06-04

@mobicham Thanks! I will do some experiments with it! I have a single RTX4090. 
