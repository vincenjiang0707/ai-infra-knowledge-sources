# zai-org/CogVideoX1.5-5B-SAT

source: https://huggingface.co/zai-org/CogVideoX1.5-5B-SAT

---
license: other
language:
- en
base_model:
- THUDM/CogVideoX-5b
- THUDM/CogVideoX-5b-I2V
pipeline_tag: image-to-video
---

# CogVideoX1.5-5B-SAT

<p style="text-align: center;">
  <div align="center">
  <img src=https://modelscope.oss-cn-beijing.aliyuncs.com/resource/cogvideologo.svg width="50%"/>
  </div>
  <p align="center">
  <a href="https://huggingface.co/THUDM/CogVideoX1.5-5B-SAT/blob/main/README_zh.md">📄 中文阅读</a> |
  <a href="https://github.com/THUDM/CogVideo">🌐 Github </a> | 
  <a href="https://arxiv.org/pdf/2408.06072">📜 arxiv </a>
</p>
<p align="center">
📍 Visit <a href="https://chatglm.cn/video?lang=en?fr=osm_cogvideo">QingYing</a> and <a href="https://open.bigmodel.cn/?utm_campaign=open&_channel_track_key=OWTVNma9">API Platform</a> to experience commercial video generation models.
</p>

CogVideoX is an open-source video generation model originating from [Qingying](https://chatglm.cn/video?fr=osm_cogvideo). CogVideoX1.5 is the upgraded version of the open-source CogVideoX model.

The CogVideoX1.5-5B series model supports **10-second** videos and higher resolutions. The `CogVideoX1.5-5B-I2V` variant supports **any resolution** for video generation.

This repository contains the SAT-weight version of the CogVideoX1.5-5B model, specifically including the following modules:

## Transformer

Includes weights for both I2V and T2V models. Specifically, it includes the following modules:

```
├── transformer_i2v  
│   ├── 1000  
│   │   └── mp_rank_00_model_states.pt  
│   └── latest  
└── transformer_t2v  
    ├── 1000  
    │   └── mp_rank_00_model_states.pt  
    └── latest  
```

Please select the corresponding weights when performing inference.

## VAE

The VAE part is consistent with the CogVideoX-5B series and does not require updating. You can also download it directly from here. Specifically, it includes the following modules:

```
└── vae  
    └── 3d-vae.pt  
```

## Text Encoder

Consistent with the diffusers version of CogVideoX-5B, no updates are necessary. You can also download it directly from here. Specifically, it includes the following modules:

```
├── t5-v1_1-xxl  
   ├── added_tokens.json  
   ├── config.json  
   ├── model-00001-of-00002.safetensors  
   ├── model-00002-of-00002.safetensors  
   ├── model.safetensors.index.json  
   ├── special_tokens_map.json  
   ├── spiece.model  
   └── tokenizer_config.json  


0 directories, 8 files  
```

## Model License

This model is released under the [CogVideoX LICENSE](LICENSE).

## Citation

```
@article{yang2024cogvideox,
  title={CogVideoX: Text-to-Video Diffusion Models with An Expert Transformer},
  author={Yang, Zhuoyi and Teng, Jiayan and Zheng, Wendi and Ding, Ming and Huang, Shiyu and Xu, Jiazheng and Yang, Yuanming and Hong, Wenyi and Zhang, Xiaohan and Feng, Guanyu and others},
  journal={arXiv preprint arXiv:2408.06072},
  year={2024}
}
```



