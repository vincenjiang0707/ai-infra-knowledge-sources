# zai-org/UI2Code_N

source: https://huggingface.co/zai-org/UI2Code_N

---
license: mit
language:
- zh
- en
base_model:
- zai-org/GLM-4.1V-9B-Base
pipeline_tag: image-text-to-text
library_name: transformers
---


<h1>UI2Code^N: A Visual Language Model for Test-Time Scalable Interactive UI-to-Code Generation</h1>

- **Repository:** https://github.com/zai-org/UI2Code_N
- **Paper:** https://arxiv.org/abs/2511.08195


<p align="center">
  <img src="https://raw.githubusercontent.com/zheny2751-dotcom/UI2Code-N/main/assets/fig1.png" alt="abs" style="width:90%;" />
</p>

**UI2Code^N** is a visual language foundation model trained through staged **pretraining**, **fine-tuning**, and **reinforcement learning** to achieve foundational improvements in multimodal coding, which unifies three key capabilities: **UI-to-code generation**, **UI editing**, and **UI polishing**.
Instead of relying on single-turn paradigms that make little use of iterative visual feedback, UI2Code^N introduces an interactive UI-to-code framework that more accurately reflects real-world workflows and raises the upper bound of achievable performance.


### Backbone Model

Our model is built on [GLM-4.1V-9B-Base](https://huggingface.co/zai-org/GLM-4.1V-9B-Base).


### Quick Inference

This is a simple example of running single-image inference using the `transformers` library.  
First, install the `transformers` library:

```
pip install transformers>=4.57.1
```

Then, run the following code:

```python
from transformers import AutoProcessor, AutoModelForImageTextToText
import torch

messages = [
    {
        "role": "user",
        "content": [
            {
                "type": "image",
                "url": "https://raw.githubusercontent.com/zheny2751-dotcom/UI2Code-N/main/assets/example.png"
            },
            {
                "type": "text",
                "text": "Please generate the corresponding html code for the given UI screenshot."
            }
        ],
    }
]
processor = AutoProcessor.from_pretrained("zai-org/UI2Code_N")
model = AutoModelForImageTextToText.from_pretrained(
    pretrained_model_name_or_path="zai-org/UI2Code_N",
    torch_dtype=torch.bfloat16,
    device_map="auto",
)
inputs = processor.apply_chat_template(
    messages,
    tokenize=True,
    add_generation_prompt=True,
    return_dict=True,
    return_tensors="pt"
).to(model.device)
generated_ids = model.generate(**inputs, max_new_tokens=16384)
output_text = processor.decode(generated_ids[0][inputs["input_ids"].shape[1]:], skip_special_tokens=False)
print(output_text)
```

See our [Github Repo](https://github.com/zai-org/UI2Code_N) for more detailed usage.




## Citation
If you find our model useful in your work, please cite it with:
```
@article{ui2coden2025,
    title   = {UI2Code$^{N}$: A Visual Language Model for Test-Time Scalable Interactive UI-to-Code Generation},
    author  = {Yang, Zhen and Hong, Wenyi and Xu, Mingde and Fan, Xinyue and Wang, Weihan and Gu, Xiaotao and Tang, Jie},
    journal = {arXiv preprint arXiv:2511.08195},
    year    = {2025}
}
```


