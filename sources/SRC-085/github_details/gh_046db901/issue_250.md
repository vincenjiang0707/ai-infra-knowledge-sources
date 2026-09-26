# [Issue #250] Batch size >1 execution fails

source: https://github.com/SafeAILab/EAGLE/issues/250
state: open | updated: 2025-09-13T15:57:58Z
labels: 

## 正文

Dear EAGLE Dev-Team,

I am trying to use EAGLE-2 with more than one prompt at a time, aka batch_size > 1.
Unfortunately, this fails using the following minimal example:

```python
from eagle.model.ea_model import EaModel
import torch

base_model_path = "models--meta-llama--Llama-3.1-8B-Instruct"
EAGLE_model_path = "yuhuili/EAGLE-LLaMA3-Instruct-8B"

model = EaModel.from_pretrained(
    base_model_path=base_model_path,
    ea_model_path=EAGLE_model_path,
    torch_dtype=torch.bfloat16,
    use_eagle3=False,
    low_cpu_mem_usage=True,
    device_map="auto",
    total_token=-1,
)
model.eval()
prompts = ["Hello","Goodbye"]
model.tokenizer.pad_token = model.tokenizer.eos_token

input_ids=model.tokenizer(prompts,padding="longest").input_ids
input_ids = torch.as_tensor(input_ids).cuda()
output_ids=model.eagenerate(input_ids,temperature=0.5,max_new_tokens=32)
```

The key states do not match the batch size in terms of tensor dimension, so this code reveals the following error:
```
  File "EAGLE/eagle/model/kv_cache.py", line 64, in cat
    dst.copy_(tensor)
RuntimeError: output with shape [1, 8, 3, 128] doesn't match the broadcast shape [2, 8, 3, 128]
```
This happens already when the draft tree is initialized in 
```
EAGLE/eagle/model/ea_model.py", line 241, in eagenerate
    draft_tokens, retrieve_indices, tree_mask, tree_position_ids, logits, hidden_state, sample_token = initialize_tree[...]
```

Looking into the EAGLE Code,the check for `batch size ==1`  is commented out, so I thought, batching is implemented.
https://github.com/SafeAILab/EAGLE/blob/c9d050a641f29b9b882cf9e1c1eedafd5e6e51df/eagle/model/ea_model.py#L398

Is there something wrong with my EaModel configuration?

## 评论 (1)

### w32zhong · 2025-09-13

If I recall correctly, only Eagle1 has batched inference support in this repo.
