# zai-org/WebGLM-2B

source: https://huggingface.co/zai-org/WebGLM-2B

---
language:
- en
tags:
- glm
- webglm
- thudm
inference: false
---

<h1>WebGLM: Towards An Efficient Web-enhanced Question Answering System with Human Preference</h1>

<p align="center">
  📃 <a href="https://arxiv.org/pdf/2306.07906.pdf" target="_blank">Paper (KDD 2023)</a> 
  | 
  💻 <a href="https://github.com/THUDM/WebGLM" target="_blank">Github Repo</a>
</p>

# Introduction

WebGLM-2B aspires to provide an efficient and cost-effective web-enhanced question-answering system using the 2-billion-parameter General Language Model (GLM). It aims to improve real-world application deployment by integrating web search and retrieval capabilities into the pre-trained language model.

WebGLM is built by the following parts:

-   **LLM-augmented Retriever**: Enhances the retrieval of relevant web content to better aid in answering questions accurately.
-   **Bootstrapped Generator**: Generates human-like responses to questions, leveraging the power of the GLM to provide refined answers.
-   **Human Preference-aware Scorer**: Estimates the quality of generated responses by prioritizing human preferences, ensuring the system produces useful and engaging content.

This repo is the implementation of **Bootstrap Generator**.

See our [Github Repo](https://github.com/THUDM/WebGLM) for more detailed usage.

