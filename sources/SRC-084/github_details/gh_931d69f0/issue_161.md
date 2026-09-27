# [Issue #161] error occurs when run a quantizated detr-resnet-50

source: https://github.com/dropbox/hqq/issues/161
state: closed | updated: 2025-06-13T12:02:21Z
labels: 

## 正文

i  made a quantization with detr-resnet-50,  and an error occurs during runtime

```
File "/mnt/f/workplace/pycharm/git/quant/hqq/hqq/backends/torchao.py", line 265, in matmul
    c = torch.ops.aten._weight_int4pack_mm(
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/miniconda3/envs/mg/lib/python3.11/site-packages/torch/_ops.py", line 1158, in __call__
    return self._op(*args, **(kwargs or {}))
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
RuntimeError: Expected A.is_contiguous() to be true, but got false.  (Could this error message be improved?  If so, please report an enhancement request to PyTorch.)
ERROR conda.cli.main_run:execute(125): `conda run python /mnt/f/workplace/pycharm/git/quant/hqq/custom/hqq_detr_resnet50.py` failed. (See above for error)
```
Code
```python
import torch
import torch.nn as nn
from transformers import DetrImageProcessor, DetrForObjectDetection
from hqq.core.quantize import BaseQuantizeConfig, HQQLinear
from PIL import Image
from hqq.utils.patching import prepare_for_inference

device, dtype = 'cuda', torch.bfloat16

model: DetrForObjectDetection = DetrForObjectDetection.from_pretrained("facebook/detr-resnet-50", revision="main")
processor: DetrImageProcessor = DetrImageProcessor.from_pretrained("facebook/detr-resnet-50", revision="main")

model.model.to(dtype).to(device)
model.class_labels_classifier.to(dtype).to(device)
model.bbox_predictor.to(dtype).to(device)

quant_config = BaseQuantizeConfig(nbits=4, group_size=256, axis=1)
def replace_linear(module):
    for name, child in module.named_children():
        if isinstance(child, nn.Linear):
            hqq_linear = HQQLinear(child, quant_config=quant_config, compute_dtype=dtype, device=device, initialize=True, del_orig=True)
            setattr(module, name, hqq_linear)
        else:
            replace_linear(child)

replace_linear(model.model)
prepare_for_inference(model.model, backend='torchao_int4')
model.class_labels_classifier = HQQLinear(model.class_labels_classifier, quant_config=quant_config, compute_dtype=dtype, device=device, initialize=True, del_orig=True)

image = Image.open("cat_01.png").convert("RGB")
inputs = processor(images=image, return_tensors="pt")
for k in inputs:
    inputs[k] = inputs[k].to(device).to(dtype).contiguous()

outputs = model(**inputs)

target_sizes = torch.tensor([image.size[::-1]]).to(device=device).to(dtype)
results = processor.post_process_object_detection(outputs, target_sizes=target_sizes, threshold=0.9)[0]

for score, label, box in zip(results["scores"], results["labels"], results["boxes"]):
    box = [round(i, 2) for i in box.tolist()]
    print(f"Detected {model.config.id2label[label.item()]} with confidence {round(score.item(), 3)} at location {box}")
```

On line 265 of the file torchao.py, I modified this line of code to make it run normally:
```python
c = torch.ops.aten._weight_int4pack_mm(
    x.to(self.device).contiguous(), self.weight_int4pack.contiguous(), self.groupsize, self.scales_and_zeros
)
```


## 评论 (2)

### mobicham · 2025-06-13

Hey, thanks for reporting!
The weights from HQQLinear are always contiguous():
```Python
In [11]: model.model.decoder.layers[-1].self_attn.k_proj.W_q.is_contiguous()
Out[11]: True
```
So I think the issue is that for some reason, the activations are not contiguous, I can `x.contiguous()` to the int4pack_mm call. Will test it later to make sure it works.

### mobicham · 2025-06-13

This should  fix it: https://github.com/mobiusml/hqq/commit/b3d56fcaf0f92ec890838f8d2396d55d88212a9f

On a different note, quantization is not gonna be very helpful in your case, the model is very small, just something to keep in mind!
