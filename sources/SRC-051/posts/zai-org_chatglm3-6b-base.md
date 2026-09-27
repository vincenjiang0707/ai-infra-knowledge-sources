# zai-org/chatglm3-6b-base

source: https://huggingface.co/zai-org/chatglm3-6b-base

---
language:
- zh
- en
tags:
- glm
- chatglm
- thudm
---
# ChatGLM3-6B-Base
<p align="center">
  💻 <a href="https://github.com/THUDM/ChatGLM" target="_blank">Github Repo</a> • 🐦 <a href="https://twitter.com/thukeg" target="_blank">Twitter</a> • 📃 <a href="https://arxiv.org/abs/2103.10360" target="_blank">[GLM@ACL 22]</a> <a href="https://github.com/THUDM/GLM" target="_blank">[GitHub]</a> • 📃 <a href="https://arxiv.org/abs/2210.02414" target="_blank">[GLM-130B@ICLR 23]</a> <a href="https://github.com/THUDM/GLM-130B" target="_blank">[GitHub]</a> <br>
</p>

<p align="center">
    👋 Join our <a href="https://join.slack.com/t/chatglm/shared_invite/zt-25ti5uohv-A_hs~am_D3Q8XPZMpj7wwQ" target="_blank">Slack</a> and <a href="https://github.com/THUDM/ChatGLM/blob/main/resources/WECHAT.md" target="_blank">WeChat</a>
</p>
<p align="center">
📍Experience the larger-scale ChatGLM model at <a href="https://www.chatglm.cn">chatglm.cn</a>
</p>

## 介绍 (Introduction)
ChatGLM3-6B 是 ChatGLM 系列最新一代的开源模型，在保留了前两代模型对话流畅、部署门槛低等众多优秀特性的基础上，ChatGLM3-6B 引入了如下特性：

1. **更强大的基础模型：** ChatGLM3-6B 的基础模型 ChatGLM3-6B-Base 采用了更多样的训练数据、更充分的训练步数和更合理的训练策略。在语义、数学、推理、代码、知识等不同角度的数据集上测评显示，ChatGLM3-6B-Base 具有在 10B 以下的预训练模型中最强的性能。
2. **更完整的功能支持：** ChatGLM3-6B 采用了全新设计的 [Prompt 格式](https://github.com/THUDM/ChatGLM3/blob/main/PROMPT.md)，除正常的多轮对话外。同时原生支持[工具调用](https://github.com/THUDM/ChatGLM3/blob/main/tool_using/README.md)（Function Call）、代码执行（Code Interpreter）和 Agent 任务等复杂场景。
3. **更全面的开源序列：** 除了对话模型 ChatGLM3-6B 外，还开源了基础模型 ChatGLM-6B-Base、长文本对话模型 ChatGLM3-6B-32K。以上所有权重对学术研究**完全开放**，在填写[问卷](https://open.bigmodel.cn/mla/form)进行登记后**亦允许免费商业使用**。

本仓库为 ChatGLM3-6B 的基础模型 ChatGLM3-6B-Base。

ChatGLM3-6B is the latest open-source model in the ChatGLM series. While retaining many excellent features such as smooth dialogue and low deployment threshold from the previous two generations, ChatGLM3-6B introduces the following features:

1. **More Powerful Base Model:** The base model of ChatGLM3-6B, ChatGLM3-6B-Base, employs a more diverse training dataset, more sufficient training steps, and a more reasonable training strategy. Evaluations on datasets such as semantics, mathematics, reasoning, code, knowledge, etc., show that ChatGLM3-6B-Base has the strongest performance among pre-trained models under 10B.
2. **More Comprehensive Function Support:** ChatGLM3-6B adopts a newly designed [Prompt format](https://github.com/THUDM/ChatGLM3/blob/main/PROMPT_en.md), in addition to the normal multi-turn dialogue. It also natively supports [function call](https://github.com/THUDM/ChatGLM3/blob/main/tool_using/README_en.md), code interpreter, and complex scenarios such as agent tasks.
3. **More Comprehensive Open-source Series:** In addition to the dialogue model ChatGLM3-6B, the base model ChatGLM-6B-Base and the long-text dialogue model ChatGLM3-6B-32K are also open-sourced. All the weights are **fully open** for academic research, and after completing the [questionnaire](https://open.bigmodel.cn/mla/form) registration, they are also **allowed for free commercial use**.

This repo is ChatGLM3-6B-Base, the base model of ChatGLM3-6B.

## 软件依赖 (Dependencies)

```shell
pip install protobuf transformers==4.30.2 cpm_kernels torch>=2.0 gradio mdtex2html sentencepiece accelerate
```

## 代码调用 (Code Usage)

作为没有经过人类意图对齐的模型，ChatGLM3-6B-Base 不能用于多轮对话。但是可以进行文本续写。

As a model that has not been aligned with human intent, ChatGLM3-6B-Base cannot be used for multi-turn conversations. However, text completion is possible.

```python
from transformers import AutoTokenizer, AutoModel
tokenizer = AutoTokenizer.from_pretrained("THUDM/chatglm3-6b-base", trust_remote_code=True)
model = AutoModel.from_pretrained("THUDM/chatglm3-6b-base", trust_remote_code=True).half().cuda()

inputs = tokenizer(["今天天气真不错"], return_tensors="pt").to('cuda')
outputs = model.generate(**inputs)
print(tokenizer.decode(outputs[0].tolist()))
```

关于更多的使用说明，包括如何运行命令行和网页版本的 DEMO，以及使用模型量化以节省显存，请参考我们的 [Github Repo](https://github.com/THUDM/ChatGLM)。

For more instructions, including how to run CLI and web demos, and model quantization, please refer to our [Github Repo](https://github.com/THUDM/ChatGLM).


## 协议 (License)

本仓库的代码依照 [Apache-2.0](LICENSE) 协议开源，ChatGLM3-6B 模型的权重的使用则需要遵循 [Model License](MODEL_LICENSE)。

The code in this repository is open-sourced under the [Apache-2.0 license](LICENSE), while the use of the ChatGLM3-6B model weights needs to comply with the [Model License](MODEL_LICENSE).

## 引用 (Citation)

如果你觉得我们的工作有帮助的话，请考虑引用下列论文。

If you find our work helpful, please consider citing the following papers.

```
@misc{glm2024chatglm,
      title={ChatGLM: A Family of Large Language Models from GLM-130B to GLM-4 All Tools}, 
      author={Team GLM and Aohan Zeng and Bin Xu and Bowen Wang and Chenhui Zhang and Da Yin and Diego Rojas and Guanyu Feng and Hanlin Zhao and Hanyu Lai and Hao Yu and Hongning Wang and Jiadai Sun and Jiajie Zhang and Jiale Cheng and Jiayi Gui and Jie Tang and Jing Zhang and Juanzi Li and Lei Zhao and Lindong Wu and Lucen Zhong and Mingdao Liu and Minlie Huang and Peng Zhang and Qinkai Zheng and Rui Lu and Shuaiqi Duan and Shudan Zhang and Shulin Cao and Shuxun Yang and Weng Lam Tam and Wenyi Zhao and Xiao Liu and Xiao Xia and Xiaohan Zhang and Xiaotao Gu and Xin Lv and Xinghan Liu and Xinyi Liu and Xinyue Yang and Xixuan Song and Xunkai Zhang and Yifan An and Yifan Xu and Yilin Niu and Yuantao Yang and Yueyan Li and Yushi Bai and Yuxiao Dong and Zehan Qi and Zhaoyu Wang and Zhen Yang and Zhengxiao Du and Zhenyu Hou and Zihan Wang},
      year={2024},
      eprint={2406.12793},
      archivePrefix={arXiv},
      primaryClass={id='cs.CL' full_name='Computation and Language' is_active=True alt_name='cmp-lg' in_archive='cs' is_general=False description='Covers natural language processing. Roughly includes material in ACM Subject Class I.2.7. Note that work on artificial languages (programming languages, logics, formal systems) that does not explicitly address natural-language issues broadly construed (natural-language processing, computational linguistics, speech, text retrieval, etc.) is not appropriate for this area.'}
}
```

