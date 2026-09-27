# zai-org/glm-roberta-large

source: https://huggingface.co/zai-org/glm-roberta-large

---
language:
- en
tags:
- glm
- thudm
---
GLM is a General Language Model pretrained with an autoregressive blank-filling objective and can be finetuned on various natural language understanding and generation tasks.

Please refer to our paper for a detailed description of GLM:

[GLM: General Language Model Pretraining with Autoregressive Blank Infilling](https://arxiv.org/abs/2103.10360) (ACL 2022)

Zhengxiao Du*, Yujie Qian*, Xiao Liu, Ming Ding, Jiezhong Qiu, Zhilin Yang, Jie Tang (*: equal contribution)

Find more examples in our [Github repo](https://github.com/THUDM/GLM).

## Model description
`glm-roberta-large` is pretrained on the RoBERTa dataset. It has 24 transformer layers, with hidden size 1024 and 16 attention heads in each layer. The model is pretrained with autoregressive blank filling objectives designed for natural language understanding, seq2seq, and language modeling. Find more details from our [repo](https://github.com/THUDM/GLM).

## How to use 
Please refer the [instruction](https://github.com/THUDM/GLM#hugging-face-hub) in our Github repo.

`glm-roberta-large` only supports `[MASK]` for short blank filling. The prediction always begin with a special `<|startofpiece|>` token and ends with a `<|endofpiece|>` token.

## Citation
Please cite our paper if you find this code useful for your research:
```
@article{DBLP:conf/acl/DuQLDQY022,
  author    = {Zhengxiao Du and
               Yujie Qian and
               Xiao Liu and
               Ming Ding and
               Jiezhong Qiu and
               Zhilin Yang and
               Jie Tang},
  title     = {{GLM:} General Language Model Pretraining with Autoregressive Blank Infilling},
  booktitle = {Proceedings of the 60th Annual Meeting of the Association for Computational
               Linguistics (Volume 1: Long Papers), {ACL} 2022, Dublin, Ireland,
               May 22-27, 2022},
  pages     = {320--335},
  publisher = {Association for Computational Linguistics},
  year      = {2022},
}
```

