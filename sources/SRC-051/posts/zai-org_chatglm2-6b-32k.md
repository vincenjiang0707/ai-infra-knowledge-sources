# zai-org/chatglm2-6b-32k

source: https://huggingface.co/zai-org/chatglm2-6b-32k

---
language:
- zh
- en
tags:
- glm
- chatglm
- thudm
---
# ChatGLM2-6B-32K
<p align="center">
  💻 <a href="https://github.com/THUDM/ChatGLM2-6B" target="_blank">Github Repo</a> • 🐦 <a href="https://twitter.com/thukeg" target="_blank">Twitter</a> • 📃 <a href="https://arxiv.org/abs/2103.10360" target="_blank">[GLM@ACL 22]</a> <a href="https://github.com/THUDM/GLM" target="_blank">[GitHub]</a> • 📃 <a href="https://arxiv.org/abs/2210.02414" target="_blank">[GLM-130B@ICLR 23]</a> <a href="https://github.com/THUDM/GLM-130B" target="_blank">[GitHub]</a> <br>
</p>

<p align="center">
    👋 Join our <a href="https://join.slack.com/t/chatglm/shared_invite/zt-1y7pqoloy-9b1g6T6JjA8J0KxvUjbwJw" target="_blank">Slack</a> and <a href="https://github.com/THUDM/ChatGLM-6B/blob/main/resources/WECHAT.md" target="_blank">WeChat</a>
</p>

## 更新/Update

- 我们优化了KV Cache的存储方式，减少了显存碎片的产生。基于优化后的代码，模型可以在约**20G显存**的情况下处理32K长度的上下文（FP/BF16格式）。
- We have optimized the storage method of the KV Cache, reducing the generation of memory fragmentation. Based on the optimized code, the model can process a context length of 32K under approximately **20G** of memory (FP/BF16 format).

## 介绍

ChatGLM**2**-6B-32K在[ChatGLM2-6B](https://huggingface.co/THUDM/chatglm2-6b)的基础上进一步强化了对于长文本的理解能力，能够更好的处理最多32K长度的上下文。具体地，我们基于[位置插值](https://arxiv.org/abs/2306.15595)（Positional Interpolation）的方法对位置编码进行了更新，并在对话阶段使用 32K 的上下文长度训练。在实际的使用中，如果您面临的上下文长度基本在 **8K 以内**，我们推荐使用[ChatGLM2-6B](https://huggingface.co/THUDM/chatglm2-6b)；如果您需要处理**超过 8K** 的上下文长度，我们推荐使用ChatGLM2-6B-32K。

ChatGLM**2**-6B-32K是开源中英双语对话模型 [ChatGLM2-6B](https://github.com/THUDM/ChatGLM2-6B) 的加长版本，在保留了初代模型对话流畅、部署门槛较低等众多优秀特性的基础之上，ChatGLM**2**-6B-32k 引入了如下新特性：

1. **更强大的性能**：基于 ChatGLM 初代模型的开发经验，我们全面升级了 ChatGLM2-6B-32K 的基座模型。ChatGLM2-6B-32K 使用了 [GLM](https://github.com/THUDM/GLM) 的混合目标函数，经过了 1.4T 中英标识符的预训练与人类偏好对齐训练。
2. **更长的上下文**：基于 [FlashAttention](https://github.com/HazyResearch/flash-attention) 技术，我们将基座模型的上下文长度（Context Length）由 ChatGLM-6B 的 2K 扩展到了 32K，并在对话阶段使用 32K 的上下文长度训练，允许更多轮次的对话。
3. **更高效的推理**：基于 [Multi-Query Attention](http://arxiv.org/abs/1911.02150) 技术，ChatGLM2-6B-32K 有更高效的推理速度和更低的显存占用：在官方的模型实现下，推理速度相比初代提升了 42%，INT4 量化下，6G 显存支持的对话长度由 1K 提升到了 8K。
4. **更开放的协议**：ChatGLM2-6B-32K 权重对学术研究**完全开放**，在填写[问卷](https://open.bigmodel.cn/mla/form)进行登记后**亦允许免费商业使用**。

The ChatGLM**2**-6B-32K further strengthens the ability to understand long texts based on the [ChatGLM2-6B](https://huggingface.co/THUDM/chatglm2-6b), and can better handle up to 32K context length. Specifically, we have updated the position encoding based on the method of [Positional Interpolation](https://arxiv.org/abs/2306.15595), and trained with a 32K context length during the dialogue alignment. In practical use, if the context length you are dealing with is generally within 8K, we recommend using [ChatGLM2-6B](https://huggingface.co/THUDM/chatglm2-6b); if you need to handle a context length exceeding 8K, we recommend using ChatGLM2-6B-32K.

ChatGLM2-6B-32K is the second-generation version of the open-source bilingual (Chinese-English) chat model [ChatGLM-6B](https://github.com/THUDM/ChatGLM-6B). It retains the smooth conversation flow and low deployment threshold of the first-generation model, while introducing the following new features:

1. **Stronger Performance**: Based on the development experience of the first-generation ChatGLM model, we have fully upgraded the base model of ChatGLM2-6B-32K. ChatGLM2-6B-32K uses the hybrid objective function of [GLM](https://github.com/THUDM/GLM), and has undergone pre-training with 1.4T bilingual tokens and human preference alignment training. 
2. **Longer Context**: Based on [FlashAttention](https://github.com/HazyResearch/flash-attention) technique, we have extended the context length of the base model from 2K in ChatGLM-6B to 32K, and trained with a context length of 32K during the dialogue alignment, allowing for more rounds of dialogue. 
3. **More Efficient Inference**: Based on [Multi-Query Attention](http://arxiv.org/abs/1911.02150) technique, ChatGLM2-6B-32K has more efficient inference speed and lower GPU memory usage: under the official  implementation, the inference speed has increased by 42% compared to the first generation; under INT4 quantization, the dialogue length supported by 6G GPU memory has increased from 1K to 8K.
4. **More Open License**: ChatGLM2-6B-32K weights are **completely open** for academic research, and **free commercial use** is also allowed after completing the [questionnaire](https://open.bigmodel.cn/mla/form).

## 软件依赖

```shell
pip install protobuf transformers==4.30.2 cpm_kernels torch>=2.0 gradio mdtex2html sentencepiece accelerate
```

## 代码调用 

可以通过如下代码调用 ChatGLM-6B-32K 模型来生成对话：

```ipython
>>> from transformers import AutoTokenizer, AutoModel
>>> tokenizer = AutoTokenizer.from_pretrained("THUDM/chatglm2-6b-32k", trust_remote_code=True)
>>> model = AutoModel.from_pretrained("THUDM/chatglm2-6b-32k", trust_remote_code=True).half().cuda()
>>> model = model.eval()
>>> response, history = model.chat(tokenizer, "你好", history=[])
>>> print(response)
你好👋!我是人工智能助手 ChatGLM-6B,很高兴见到你,欢迎问我任何问题。
>>> response, history = model.chat(tokenizer, "晚上睡不着应该怎么办", history=history)
>>> print(response)
晚上睡不着可能会让你感到焦虑或不舒服,但以下是一些可以帮助你入睡的方法:

1. 制定规律的睡眠时间表:保持规律的睡眠时间表可以帮助你建立健康的睡眠习惯,使你更容易入睡。尽量在每天的相同时间上床,并在同一时间起床。
2. 创造一个舒适的睡眠环境:确保睡眠环境舒适,安静,黑暗且温度适宜。可以使用舒适的床上用品,并保持房间通风。
3. 放松身心:在睡前做些放松的活动,例如泡个热水澡,听些轻柔的音乐,阅读一些有趣的书籍等,有助于缓解紧张和焦虑,使你更容易入睡。
4. 避免饮用含有咖啡因的饮料:咖啡因是一种刺激性物质,会影响你的睡眠质量。尽量避免在睡前饮用含有咖啡因的饮料,例如咖啡,茶和可乐。
5. 避免在床上做与睡眠无关的事情:在床上做些与睡眠无关的事情,例如看电影,玩游戏或工作等,可能会干扰你的睡眠。
6. 尝试呼吸技巧:深呼吸是一种放松技巧,可以帮助你缓解紧张和焦虑,使你更容易入睡。试着慢慢吸气,保持几秒钟,然后缓慢呼气。

如果这些方法无法帮助你入睡,你可以考虑咨询医生或睡眠专家,寻求进一步的建议。
```

关于更多的使用说明，包括如何运行命令行和网页版本的 DEMO，以及使用模型量化以节省显存，请参考我们的 [Github Repo](https://github.com/THUDM/ChatGLM2-6B)。

For more instructions, including how to run CLI and web demos, and model quantization, please refer to our [Github Repo](https://github.com/THUDM/ChatGLM2-6B).

## Change Log
* v1.0

## 协议

本仓库的代码依照 [Apache-2.0](LICENSE) 协议开源，ChatGLM2-6B-32K 模型的权重的使用则需要遵循 [Model License](MODEL_LICENSE)。

## 引用

如果你觉得我们的工作有帮助的话，请考虑引用下列论文。

If you find our work helpful, please consider citing the following paper.

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
