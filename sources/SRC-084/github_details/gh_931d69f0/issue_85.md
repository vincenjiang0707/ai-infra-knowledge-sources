# [Issue #85] hqq+ lora ValueError || ValueError: Unable to create tensor, you should probably activate truncation and/or padding with 'padding=True' 'truncation=True'

source: https://github.com/dropbox/hqq/issues/85
state: closed | updated: 2024-08-13T13:58:31Z
labels: 

## 正文

ValueError: Unable to create tensor, you should probably activate truncation and/or padding with 'padding=True' 'truncation=True' to have batched tensors with the same length. Perhaps your features (`text` in this case) have excessive nesting (inputs type `list` where type `int` is expected).

## 评论 (3)

### mobicham · 2024-06-20

Can you please explain a bit and provide a code snippet to reproduce the error?

### SAIVENKATARAJU · 2024-08-13

This issue happening from here: https://github.com/mobiusml/hqq/blob/master/examples/lora/train_hqq_lora_example.py

### mobicham · 2024-08-13

Hi, that's an old issue. HQQ works directly in Peft for a while now: https://huggingface.co/docs/peft/developer_guides/quantization#hqq-quantization 
