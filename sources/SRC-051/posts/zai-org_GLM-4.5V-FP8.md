# zai-org/GLM-4.5V-FP8

source: https://huggingface.co/zai-org/GLM-4.5V-FP8

---
base_model:
- zai-org/GLM-4.5-Air-Base
language:
- zh
- en
library_name: transformers
license: mit
pipeline_tag: image-text-to-text
---

# GLM-4.5V-FP8

<div align="center">
<img src=https://raw.githubusercontent.com/zai-org/GLM-V/refs/heads/main/resources/logo.svg width="40%"/>
</div>
<p align="center">
    👋 Join our <a href="https://discord.com/invite/8cnQKdAprg" target="_blank">Discord</a> communities.
    <br>
    📖 Check out the <a href="https://huggingface.co/papers/2507.01006" target="_blank">paper</a>.
    <br>
    📍 Access the GLM-V series models via API on the <a href="https://docs.z.ai/guides/vlm/glm-4.5v">ZhipuAI Open Platform</a>.
</p>

## Introduction

Vision-language models (VLMs) have become a key cornerstone of intelligent systems. As real-world AI tasks grow increasingly complex, VLMs urgently need to enhance reasoning capabilities beyond basic multimodal perception — improving accuracy, comprehensiveness, and intelligence — to enable complex problem solving, long-context understanding, and multimodal agents.

Through our open-source work, we aim to explore the technological frontier together with the community while empowering more developers to create exciting and innovative applications.

GLM-4.5V is based on ZhipuAI’s next-generation flagship text foundation model GLM-4.5-Air (106B parameters, 12B active). It continues the technical approach of GLM-4.1V-Thinking, achieving SOTA performance among models of the same scale on 42 public vision-language benchmarks. It covers common tasks such as image, video, and document understanding, as well as GUI agent operations.

![bench_45](https://raw.githubusercontent.com/zai-org/GLM-V/refs/heads/main/resources/bench_45v.jpeg)

Beyond benchmark performance, GLM-4.5V focuses on real-world usability. Through efficient hybrid training, it can handle diverse types of visual content, enabling full-spectrum vision reasoning, including:
- **Image reasoning** (scene understanding, complex multi-image analysis, spatial recognition)
- **Video understanding** (long video segmentation and event recognition)
- **GUI tasks** (screen reading, icon recognition, desktop operation assistance)
- **Complex chart & long document parsing** (research report analysis, information extraction)
- **Grounding** (precise visual element localization)

The model also introduces a **Thinking Mode** switch, allowing users to balance between quick responses and deep reasoning. This switch works the same as in the `GLM-4.5` language model.

The special tokens `<|begin_of_box|>` and `<|end_of_box|>` in the response mark the answer’s bounding box in the image. The bounding box is given as four numbers — for example `[x1, y1, x2, y2]`, where `(x1, y1)` is the top-left corner and `(x2, y2`)` is the bottom-right corner. The bracket style may vary ([], [[]], (), <>, etc.), but the meaning is the same: it encloses the coordinates of the box. These coordinates are relative values between 0 and 1000, normalized to the image size.

For more code information, please visit our [GitHub](https://github.com/zai-org/GLM-V/).

## Sample Usage

You can use the model with the `transformers` library as follows:

```python
from transformers import AutoProcessor, AutoModelForConditionalGeneration
from PIL import Image
import requests
import torch

# Load model and processor
model_id = "zai-org/GLM-4.5V-FP8"
model = AutoModelForConditionalGeneration.from_pretrained(
    model_id,
    torch_dtype="auto",
    device_map="auto",
    trust_remote_code=True
)
processor = AutoProcessor.from_pretrained(model_id, trust_remote_code=True)

# Example image loading (replace with your image path or URL)
image_url = "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/tasks/car.jpg"
image = Image.open(requests.get(image_url, stream=True).raw).convert("RGB")

# Prepare the prompt
prompt = "Describe this car in detail."
messages = [
    {"role": "user", "content": [{"type": "image", "image": image}, {"type": "text", "text": prompt}]}
]

# Apply chat template and preprocess image
input_ids = processor.apply_chat_template(messages, add_generation_prompt=True, return_tensors="pt")
pixel_values = processor.preprocess_images(image, return_tensors="pt")

# Generate response
with torch.no_grad():
    output_ids = model.generate(
        input_ids.to(model.device),
        pixel_values=pixel_values.to(model.device),
        max_new_tokens=512
    )

response = processor.decode(output_ids[0], skip_special_tokens=True)
print(response)
```

## Citation

If you use this model, please cite the following paper:

```bibtex
@misc{vteam2025glm45vglm41vthinkingversatilemultimodal,
      title={GLM-4.5V and GLM-4.1V-Thinking: Towards Versatile Multimodal Reasoning with Scalable Reinforcement Learning}, 
      author={V Team and Wenyi Hong and Wenmeng Yu and Xiaotao Gu and Guo Wang and Guobing Gan and Haomiao Tang and Jiale Cheng and Ji Qi and Junhui Ji and Lihang Pan and Shuaiqi Duan and Weihan Wang and Yan Wang and Yean Cheng and Zehai He and Zhe Su and Zhen Yang and Ziyang Pan and Aohan Zeng and Baoxu Wang and Bin Chen and Boyan Shi and Changyu Pang and Chenhui Zhang and Da Yin and Fan Yang and Guoqing Chen and Jiazheng Xu and Jiale Zhu and Jiali Chen and Jing Chen and Jinhao Chen and Jinghao Lin and Jinjiang Wang and Junjie Chen and Leqi Lei and Letian Gong and Leyi Pan and Mingdao Liu and Mingde Xu and Mingzhi Zhang and Qinkai Zheng and Sheng Yang and Shi Zhong and Shiyu Huang and Shuyuan Zhao and Siyan Xue and Shangqin Tu and Shengbiao Meng and Tianshu Zhang and Tianwei Luo and Tianxiang Hao and Tianyu Tong and Wenkai Li and Wei Jia and Xiao Liu and Xiaohan Zhang and Xin Lyu and Xinyue Fan and Xuancheng Huang and Yanling Wang and Yadong Xue and Yanfeng Wang and Yanzi Wang and Yifan An and Yifan Du and Yiming Shi and Yiheng Huang and Yilin Niu and Yuan Wang and Yuanchang Yue and Yuchen Li and Yutao Zhang and Yuting Wang and Yu Wang and Yuxuan Zhang and Zhao Xue and Zhenyu Hou and Zhengxiao Du and Zihan Wang and Peng Zhang and Debing Liu and Bin Xu and Juanzi Li and Minlie Huang and Yuxiao Dong and Jie Tang},
      year={2025},
      eprint={2507.01006},
      archivePrefix={arXiv},
      primaryClass={cs.CV},
      url={https://arxiv.org/abs/2507.01006}, 
}
```
