# zai-org/glm-edge-v-5b-gguf

source: https://huggingface.co/zai-org/glm-edge-v-5b-gguf

---
license: other
license_name: glm-4
license_link: LICENSE
language:
  - zh
  - en
pipeline_tag: image-text-to-text
tags:
  - glm
  - edge
inference: false
---

# Glm-Edge-V-5B-GGUF

中文阅读, 点击[这里](README_zh.md)

## Inference with Ollama

### Installation

The code for adapting this model is actively being integrated into the official `llama.cpp`. You can test it using the
following adapted version:

```bash
git clone https://github.com/piDack/llama.cpp -b support_glm_edge_model
cmake -B build -DGGML_CUDA=ON # Or enable other acceleration hardware
cmake --build build -- -j 
```

### Inference

After installation, you can start the GLM-Edge Chat model using the following command:

```shell
llama-cli -m <path>/model.gguf -p "<|user|>\nhi<|assistant|>\n" -ngl 999
```

In the command-line interface, you can interact with the model by entering your requests, and the model will provide the
corresponding responses.

## License

The usage of this model’s weights is subject to the terms outlined in the [LICENSE](LICENSE).
