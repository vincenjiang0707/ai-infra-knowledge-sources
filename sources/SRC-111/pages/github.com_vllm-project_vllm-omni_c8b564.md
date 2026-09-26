source: https://github.com/vllm-project/vllm-omni

| [ Documentation](https://vllm-omni.readthedocs.io/en/latest/) |

[|](https://deepwiki.com/vllm-project/vllm-omni)

**DeepWiki**[|](https://discuss.vllm.ai)

**User Forum**[|](https://slack.vllm.ai)

**Developer Slack**[|](https://github.com/vllm-project/vllm-omni/blob/main/docs/assets/WeChat.jpg)**WeChat**

[|](https://arxiv.org/abs/2602.02204)

**Paper**[|](https://docs.google.com/presentation/d/1aPj0OGl_-ZVoib-Qne5dGDAlrRFB-PdHl6E-EE99g8E/edit?usp=sharing)

**Slides***Latest News* 🔥

- [2026/08] We released
[0.28.0](https://github.com/vllm-project/vllm-omni/releases/tag/v0.28.0), featuring production-ready[MiniMax H3](https://github.com/vllm-project/vllm-omni/blob/main/recipes/MiniMaxAI/MiniMax-H3.md)serving on GPU and NPU, a unified AR/DiT paged KV cache runtime, and enhanced realtime full-duplex serving for the[MiniCPM-o series](https://github.com/vllm-project/vllm-omni/blob/main/recipes/OpenBMB/MiniCPM-o-4_5.md). - [2026/08]
[VeRL-Omni](https://github.com/verl-project/verl-omni)`v0.2.0`

is released: faster diffusion RL powered by vLLM-Omni (request-level/step-wise batching with FA3), rebuilt Qwen3-Omni multimodal training (DPO & GSPO), plus LTX-2.3, Qwen-Image-Edit support and more. See the[release notes](https://github.com/verl-project/verl-omni/releases/tag/v0.2.0). - [2026/08] We released
[0.26.0](https://github.com/vllm-project/vllm-omni/releases/tag/v0.26.0)- aligned with the vLLM 0.26 release line, featuring[MiniMax H3](https://github.com/vllm-project/vllm-omni/blob/main/recipes/MiniMaxAI/MiniMax-H3.md)joint video/audio generation, an experimental full-duplex realtime runtime for[MiniCPM-o 4.5](https://github.com/vllm-project/vllm-omni/blob/main/recipes/OpenBMB/MiniCPM-o-4_5.md), distributed layerwise diffusion offload, and broader model, hardware, streaming, TTS, and quantization support. - [2026/07] We released
[0.24.0](https://github.com/vllm-project/vllm-omni/releases/tag/v0.24.0)- aligned with the vLLM 0.24 release line, expanding production-ready coverage across TTS, speech, diffusion, image/video generation, and robot-policy serving, with major Omni stage runtime refactoring, diffusion request-level batching, async output materialization, quantization/cache/memory improvements, and broad CUDA/ROCm/XPU/NPU support. - [2026/06] Starting with
[0.14.0](https://github.com/vllm-project/vllm-omni/releases/tag/v0.14.0), vLLM-Omni publishes a stable release aligned with every even-numbered upstream vLLM minor version.[0.16.0](https://github.com/vllm-project/vllm-omni/releases/tag/v0.16.0),[0.18.0](https://github.com/vllm-project/vllm-omni/releases/tag/v0.18.0),[0.20.0](https://github.com/vllm-project/vllm-omni/releases/tag/v0.20.0), and[0.22.0](https://github.com/vllm-project/vllm-omni/releases/tag/v0.22.0)continued this cadence, expanding omni and world-model support with[NVIDIA Cosmos3](https://github.com/vllm-project/vllm-omni/blob/main/recipes/cosmos3/Cosmos3-Nano.md)and DreamZero, adding models such as MiniCPM-o 4.5, MOSS-TTS, and Lance, and advancing TTS, diffusion, distributed execution, quantization, RL integration through[VeRL-Omni](https://github.com/verl-project/verl-omni), and CUDA/ROCm/MUSA/NPU/XPU coverage. - [2026/03] Check out our first public
[project deepdive](https://youtu.be/sgwNfsNnR9I)at the vLLM Hong Kong Meetup! - [2025/11] vLLM community officially released
[vllm-project/vllm-omni](https://github.com/vllm-project/vllm-omni)in order to support omni-modality models serving.

[vLLM](https://github.com/vllm-project/vllm) was originally designed to support large language models for text-based autoregressive generation tasks. vLLM-Omni is a framework that extends its support for omni-modality model inference and serving:

**Omni-modality**: Text, image, audio, video, and action data processing**Non-autoregressive Architectures**: extend the AR support of vLLM to Diffusion Transformers (DiT) and other parallel generation models**Heterogeneous outputs**: from traditional text generation to multimodal and action outputs


vLLM-Omni is fast with:

- State-of-the-art AR support by leveraging efficient KV cache management from vLLM
- Pipelined stage execution overlapping for high throughput performance
- Fully disaggregation based on OmniConnector and dynamic resource allocation across stages

vLLM-Omni is flexible and easy to use with:

- Heterogeneous pipeline abstraction to manage complex model workflows
- Seamless integration with popular Hugging Face models
- Tensor, pipeline, data and expert parallelism support for distributed inference
- Streaming outputs
- OpenAI-compatible API server
[Full-duplex realtime serving](https://github.com/vllm-project/vllm-omni/blob/main/docs/serving/realtime_duplex_api.md)with streaming audio input and output

vLLM-Omni seamlessly supports most popular open-source models on HuggingFace, including:

**Omni-modality models**(e.g. Qwen3-Omni, MiniCPM-o 4.5, Cosmos3, HunyuanImage, BAGEL)**TTS models**(e.g. Qwen3-TTS, IndexTTS 2.5, CosyVoice3)**Diffusion models**— image, video, and audio generation (e.g. MiniMax H3, LTX-2.5, SANA-Video, Wan2.2)**Robot-policy and action models**(e.g. π0, GR00T-N1.7, DreamZero-DROID, InternVLA-A1)

Visit our [documentation](https://vllm-omni.readthedocs.io/en/latest/) to learn more.

[Installation](https://vllm-omni.readthedocs.io/en/latest/getting_started/installation/)[Quickstart](https://vllm-omni.readthedocs.io/en/latest/getting_started/quickstart/)[Nightly CUDA Docker images](https://hub.docker.com/r/vllm/vllm-omni/tags?name=nightly)built from the latest`main`

[List of Supported Models](https://vllm-omni.readthedocs.io/en/latest/models/supported_models/)[Deployment Recipes](https://recipes.vllm.ai)for vLLM-Omni model serving

We welcome and value any contributions and collaborations.
Please check out [Contributing to vLLM-Omni](https://vllm-omni.readthedocs.io/en/latest/contributing/) for how to get involved.

If you use vLLM-Omni for your research, please cite our [paper](https://arxiv.org/abs/2602.02204):

```
@article{yin2026vllmomni,
title={vLLM-Omni: Fully Disaggregated Serving for Any-to-Any Multimodal Models},
author={Peiqi Yin, Jiangyun Zhu, Han Gao, Chenguang Zheng, Yongxiang Huang, Taichang Zhou, Ruirui Yang, Weizhi Liu, Weiqing Chen, Canlin Guo, Didan Deng, Zifeng Mo, Cong Wang, James Cheng, Roger Wang, Hongsheng Liu},
journal={arXiv preprint arXiv:2602.02204},
year={2026}
}
```

Feel free to ask questions, provide feedbacks and discuss with fellow users of vLLM-Omni in `#sig-omni`

slack channel at [slack.vllm.ai](https://slack.vllm.ai) or vLLM user forum at [discuss.vllm.ai](https://discuss.vllm.ai).


Apache License 2.0, as found in the [LICENSE](https://github.com/vllm-project/vllm-omni/blob/main/LICENSE) file.