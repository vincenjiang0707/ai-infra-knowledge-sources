# zai-org/cogvlm2-llama3-chinese-chat-19B-tgi

source: https://huggingface.co/zai-org/cogvlm2-llama3-chinese-chat-19B-tgi

---
license: other
license_name: cogvlm2
license_link: https://huggingface.co/THUDM/cogvlm2-llama3-chat-19B-tgi/blob/main/LICENSE
 
language:
- en
pipeline_tag: text-generation
tags:
- chat
- cogvlm2

inference: false
---

# CogVLM2 

<div align="center">
<img src=https://raw.githubusercontent.com/THUDM/CogVLM2/60907317370f38b73c5ef89c36dfea4d6d4c6b88/resources/logo.svg width="40%"/>
</div>
<p align="center">
   👋 Join us on <a href="https://github.com/THUDM/CogVLM2/blob/main/resources/WECHAT.md" target="_blank">WeChat</a>
</p>
<p align="center">
📍Experience the larger-scale CogVLM model on the <a href="https://open.bigmodel.cn/dev/api#super-humanoid">ZhipuAI Open Platform</a>.
</p>


## Model introduction

We launch a new generation of **CogVLM2** series of models and open source two models built with [Meta-Llama-3-8B-Instruct](https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct). Compared with the previous generation of CogVLM open source models.

**This is a [TGI](https://huggingface.co/docs/text-generation-inference/en/index) format model.**
## Quick Start

here is a simple example of how to use the model to chat with the CogVLM2 TGI model.
```python
import requests
import json
import base64
import os


requests.packages.urllib3.disable_warnings()
BAD_RESPONSE = "<error></error>"
def image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
        return encoded_string.decode('utf-8')

def history_to_prompt(query):
    answer_format = 'Answer:'
    prompt = ''
    prompt += 'Question: {} {}'.format(query, answer_format)
    return prompt

def get_response(image_path, question):
    image_extension = os.path.splitext(image_path)[1][1:]
    
    base64_img = image_to_base64(image_path)
    
    url = 'http://127.0.0.1:8080'
    headers = {
        'Content-Type': 'application/json',
    }

    prompt = history_to_prompt(question)
    payload = {
        "inputs": f"![](data:image/{image_extension};base64,{base64_img}){prompt}",
        "stream": False,
        "parameters": {
            "best_of": 1,
            "decoder_input_details": False,
            "details": False,
            "repetition_penalty": 1.1,
            "do_sample": True,
            "max_new_tokens": 1000,
            "return_full_text": False,
            "temperature": 0.8,
            "top_p": 0.4,
            "top_k": 1
        }
    }
    try_times = 0
    while try_times < 3:
        try_times += 1
        try:
            response = requests.post(url, headers=headers, stream=False, data=json.dumps(payload), verify=False)
            if response.status_code == 200:
                try:
                    output = response.json()[0]["generated_text"].strip()
                    return output
                except Exception as e:
                    pass
            else:
                print(f"Received bad status code: {response.status_code}")
        except requests.exceptions.ConnectionError as errc:
            print("Error Connecting:", errc)
        except requests.exceptions.Timeout as errt:
            print("Timeout Error:", errt)
        except requests.exceptions.RequestException as err:
            print("Something Else:", err)
    return BAD_RESPONSE
if __name__ == "__main__":
    from glob import glob
    files = glob("demo.jpeg")
    for file in files:
        print(file)
        print(get_response(
            image_path=file,
            question="who is this",
        ))
```


## License

This model is released under the CogVLM2 [LICENSE](./LICENSE). For models built with Meta Llama 3, please also adhere to the [LLAMA3_LICENSE](./LLAMA3_LICENSE).

## Citation

If you find our work helpful, please consider citing the following papers

```
@misc{wang2023cogvlm,
      title={CogVLM: Visual Expert for Pretrained Language Models}, 
      author={Weihan Wang and Qingsong Lv and Wenmeng Yu and Wenyi Hong and Ji Qi and Yan Wang and Junhui Ji and Zhuoyi Yang and Lei Zhao and Xixuan Song and Jiazheng Xu and Bin Xu and Juanzi Li and Yuxiao Dong and Ming Ding and Jie Tang},
      year={2023},
      eprint={2311.03079},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}
```


