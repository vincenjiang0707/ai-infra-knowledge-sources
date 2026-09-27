# zai-org/cogagent-9b-20241220

source: https://huggingface.co/zai-org/cogagent-9b-20241220

---
license: other
language:
  - zh
  - en
base_model:
  - THUDM/glm-4v-9b
pipeline_tag: image-text-to-text
library_name: transformers
---

# CogAgent

<p style="text-align: center;">
  <p align="center">
  <a href="https://github.com/THUDM/CogAgent">🌐 Github </a> | 
  <a href="https://huggingface.co/spaces/THUDM-HF-SPACE/CogAgent-Demo">🤗 Huggingface Space</a> |
  <a href="https://cogagent.aminer.cn/blog#/articles/cogagent-9b-20241220-technical-report-en">📄 Technical Report </a> | 
  <a href="https://arxiv.org/abs/2312.08914">📜 arxiv paper </a>
</p>

[中文阅读](README_zh.md)

## About the Model

The `CogAgent-9B-20241220` model is based on [GLM-4V-9B](https://huggingface.co/THUDM/glm-4v-9b), a bilingual
open-source VLM base model. Through data collection and optimization, multi-stage training, and strategy improvements,
`CogAgent-9B-20241220` achieves significant advancements in GUI perception, inference prediction accuracy, action space
completeness, and task generalizability. The model supports bilingual (Chinese and English) interaction with both
screenshots and language input.

This version of the CogAgent model has already been applied in
ZhipuAI's [GLM-PC product](https://cogagent.aminer.cn/home). We hope this release will assist researchers and developers
in advancing the research and applications of GUI agents based on vision-language models.

## Running the Model

Please refer to our [GitHub](https://github.com/THUDM/CogAgent) for specific examples of running the model.

## Input and Output

`cogagent-9b-20241220` is an agent execution model rather than a conversational model. It does not support continuous
conversations but does support continuous execution history. Below are guidelines on how users should format their input
for the model and interpret the formatted output.

## Run the Model

<p>Please visit our <a href="https://github.com/THUDM/CogAgent">github</a> for specific running examples, as well as the part for prompt concatenation <strong style="color: red;">(this directly affects whether the model runs correctly)</strong>.</p>

In particular, pay attention to the prompt concatenation process.
You can refer to [app/client.py#L115](https://github.com/THUDM/CogAgent/blob/e3ca6f4dc94118d3dfb749f195cbb800ee4543ce/app/client.py#L115) for concatenating user input prompts.
``` python
current_platform = identify_os() # "Mac" or "WIN" or "Mobile"，注意大小写
platform_str = f"(Platform: {current_platform})\n"
format_str = "(Answer in Action-Operation-Sensitive format.)\n" # You can use other format to replace "Action-Operation-Sensitive"

history_str = "\nHistory steps: "
for index, (grounded_op_func, action) in enumerate(zip(history_grounded_op_funcs, history_actions)):
   history_str += f"\n{index}. {grounded_op_func}\t{action}" # start from 0. 

query = f"Task: {task}{history_str}\n{platform_str}{format_str}" # Be careful about the \n

```

A minimal user input concatenation code is as follows:
```
"Task: Search for doors, click doors on sale and filter by brands \"Mastercraft\".\nHistory steps: \n0. CLICK(box=[[352,102,786,139]], element_info='Search')\tLeft click on the search box located in the middle top of the screen next to the Menards logo.\n1. TYPE(box=[[352,102,786,139]], text='doors', element_info='Search')\tIn the search input box at the top, type 'doors'.\n2. CLICK(box=[[787,102,809,139]], element_info='SEARCH')\tLeft click on the magnifying glass icon next to the search bar to perform the search.\n3. SCROLL_DOWN(box=[[0,209,998,952]], step_count=5, element_info='[None]')\tScroll down the page to see the available doors.\n4. CLICK(box=[[280,708,710,809]], element_info='Doors on Sale')\tClick the \"Doors On Sale\" button in the middle of the page to view the doors that are currently on sale.\n(Platform: WIN)\n(Answer in Action-Operation format.)\n"
```
The concatenated Python string will look like:

```
"Task: Search for doors, click doors on sale and filter by brands \"Mastercraft\".\nHistory steps: \n0. CLICK(box=[[352,102,786,139]], element_info='Search')\tLeft click on the search box located in the middle top of the screen next to the Menards logo.\n1. TYPE(box=[[352,102,786,139]], text='doors', element_info='Search')\tIn the search input box at the top, type 'doors'.\n2. CLICK(box=[[787,102,809,139]], element_info='SEARCH')\tLeft click on the magnifying glass icon next to the search bar to perform the search.\n3. SCROLL_DOWN(box=[[0,209,998,952]], step_count=5, element_info='[None]')\tScroll down the page to see the available doors.\n4. CLICK(box=[[280,708,710,809]], element_info='Doors on Sale')\tClick the \"Doors On Sale\" button in the middle of the page to view the doors that are currently on sale.\n(Platform: WIN)\n(Answer in Action-Operation format.)\n"
```

Due to the length, if you would like to understand the meaning and representation of each field in detail, please refer to the [GitHub](https://github.com/THUDM/CogAgent).

## Previous Work

In November 2023, we released the first generation of CogAgent. You can find related code and weights in
the [CogVLM & CogAgent Official Repository](https://github.com/THUDM/CogVLM).

<div align="center">
    <img src=https://raw.githubusercontent.com/THUDM/CogAgent/refs/heads/main/assets/cogagent_function.jpg width=70% />
</div>

<table>
  <tr>
    <td>
      <h2> CogVLM </h2>
      <p> 📖  Paper: <a href="https://arxiv.org/abs/2311.03079">CogVLM: Visual Expert for Pretrained Language Models</a></p>
      <p><b>CogVLM</b> is a powerful open-source vision-language model (VLM). CogVLM-17B has 10 billion vision parameters and 7 billion language parameters, supporting 490x490 resolution image understanding and multi-turn conversations.</p>
      <p><b>CogVLM-17B achieved state-of-the-art performance on 10 classic cross-modal benchmarks</b> including NoCaps, Flicker30k captioning, RefCOCO, RefCOCO+, RefCOCOg, Visual7W, GQA, ScienceQA, VizWiz VQA, and TDIUC benchmarks.</p>
    </td>
    <td>
      <h2> CogAgent </h2>
      <p> 📖  Paper: <a href="https://arxiv.org/abs/2312.08914">CogAgent: A Visual Language Model for GUI Agents </a></p>
      <p><b>CogAgent</b> is an improved open-source vision-language model based on CogVLM. CogAgent-18B has 11 billion vision parameters and 7 billion language parameters, <b>supporting image understanding at 1120x1120 resolution. Beyond CogVLM's capabilities, it also incorporates GUI agent capabilities.</b></p>
      <p><b>CogAgent-18B achieved state-of-the-art performance on 9 classic cross-modal benchmarks,</b> including VQAv2, OK-VQ, TextVQA, ST-VQA, ChartQA, infoVQA, DocVQA, MM-Vet, and POPE benchmarks. It significantly outperformed existing models on GUI operation datasets like AITW and Mind2Web.</p>
    </td>
  </tr>
</table>

## License

Please follow the [Model License](LICENSE) for using the model weights.

