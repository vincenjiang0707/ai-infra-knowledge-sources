# zai-org/glm-edge-v-5b

source: https://huggingface.co/zai-org/glm-edge-v-5b

---
frameworks:
- Pytorch
license: other
license_name: glm-4
license_link: LICENSE
pipeline_tag: image-text-to-text
tags:
  - glm
  - edge
inference: false
---

# GLM-Edge-V-5B

中文阅读, 点击[这里](README_zh.md)

## Inference with Transformers

### Installation

Install the transformers library from the source code:

```shell
pip install git+https://github.com/huggingface/transformers.git
```

### Inference

```python
import torch
from PIL import Image
from transformers import (
    AutoTokenizer,
    AutoImageProcessor,
    AutoModelForCausalLM,
)

url = "img.png"
messages = [{"role": "user", "content": [{"type": "image"}, {"type": "text", "text": "describe this image"}]}]
image = Image.open(url)

model_dir = "THUDM/glm-edge-v-5b"

processor = AutoImageProcessor.from_pretrained(model_dir, trust_remote_code=True)
tokenizer = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(
    model_dir,
    torch_dtype=torch.bfloat16,
    device_map="auto",
    trust_remote_code=True,
)

inputs = tokenizer.apply_chat_template(
    messages, add_generation_prompt=True, return_dict=True, tokenize=True, return_tensors="pt"
).to(next(model.parameters()).device)

generate_kwargs = {
    **inputs,
    "pixel_values": torch.tensor(processor(image).pixel_values).to(next(model.parameters()).device),
}
output = model.generate(**generate_kwargs, max_new_tokens=100)
print(tokenizer.decode(output[0][len(inputs["input_ids"][0]):], skip_special_tokens=True))

```

## License

The usage of this model’s weights is subject to the terms outlined in the [LICENSE](LICENSE).
