source: https://docs.vllm.ai/projects/recipes/en/stable/DeepSeek/DeepSeek-V3_1.html
lastmod: 2026-04-27

# DeepSeek-V3.1 Usage Guide[¶](https://docs.vllm.ai#deepseek-v31-usage-guide)

## Introduction[¶](https://docs.vllm.ai#introduction)

[DeepSeek-V3.1](https://huggingface.co/deepseek-ai/DeepSeek-V3.1) is a hybrid model that supports both thinking mode and non-thinking mode. This guide describes how to dynamically switch between `think`

and `non-think`

mode in vllm.

## Installing vLLM[¶](https://docs.vllm.ai#installing-vllm)

## Launching DeepSeek-V3.1[¶](https://docs.vllm.ai#launching-deepseek-v31)

### Serving on 8xH200 (or H20) GPUs (141GB × 8)[¶](https://docs.vllm.ai#serving-on-8xh200-or-h20-gpus-141gb-8)

```bash
vllm serve deepseek-ai/DeepSeek-V3.1 \
--enable-expert-parallel \
--tensor-parallel-size 8 \
--served-model-name ds31
```


### Function calling[¶](https://docs.vllm.ai#function-calling)

vLLM also supports calling user-defined functions. Make sure to run your DeepSeek-V3.1 models with the following arguments. The example file is included in the official container and can be downloaded [here](https://github.com/vllm-project/vllm/blob/main/examples/tool_chat_template_deepseekv31.jinja)

vllm serve ...
--enable-auto-tool-choice
--tool-call-parser deepseek_v31
--chat-template examples/tool_chat_template_deepseekv31.jinja


## Using the Model[¶](https://docs.vllm.ai#using-the-model)

### OpenAI Client Example[¶](https://docs.vllm.ai#openai-client-example)

You can use the OpenAI client as follows. You can control whether to enable think mode by using `extra_body={"chat_template_kwargs": {"thinking": False}}`

, where `True`

enables think mode and `False`

disables think mode (non-thinking mode).

from openai import OpenAI
openai_api_key = "EMPTY"
openai_api_base = "http://localhost:8000/v1"
client = OpenAI(
api_key=openai_api_key,
base_url=openai_api_base,
)
models = client.models.list()
model = models.data[0].id
messages = [
{"role": "system", "content": "You are a helpful assistant"},
{"role": "user", "content": "Who are you?"},
{"role": "assistant", "content": "<think>Hmm</think>I am DeepSeek"},
{"role": "user", "content": "9.11 and 9.8, which is greater?"},
]
extra_body = {"chat_template_kwargs": {"thinking": False}}
response = client.chat.completions.create(
model=model, messages=messages, extra_body=extra_body
)
content = response.choices[0].message.content
print("content:\n", content)


### Example Outputs[¶](https://docs.vllm.ai#example-outputs)

#### thinking=True[¶](https://docs.vllm.ai#thinkingtrue)

- As shown below, the output results contain
`</think>`

[Hmm, the user is asking which number is greater between 9.11 and 9.8. This seems straightforward, but I should be careful because decimals can sometimes confuse people.](https://docs.vllm.ai#__codelineno-4-1)[I recall that comparing decimals involves looking at each digit from left to right. Both numbers have the same whole number part (9), so I need to compare the decimal parts. 0.11 is greater than 0.8 because 0.11 is equivalent to 0.110 and 0.8 is 0.800, so 110 thousandths is greater than 800 thousandths? Wait no, that’s wrong.](https://docs.vllm.ai#__codelineno-4-3)[Actually, 0.8 is the same as 0.80, and 0.11 is less than 0.80. So 9.11 is actually less than 9.8. I should double-check that. Yes, 9.8 is larger because 0.8 > 0.11.](https://docs.vllm.ai#__codelineno-4-5)[I’ll explain it clearly by comparing the tenths place: 9.8 has 8 tenths, while 9.11 has 1 tenth and 1 hundredth, so 8 tenths is indeed larger.](https://docs.vllm.ai#__codelineno-4-7)[The answer is 9.8 is greater. I’ll state it confidently and offer further help if needed.</think>9.8 is greater than 9.11.](https://docs.vllm.ai#__codelineno-4-9)[To compare them:](https://docs.vllm.ai#__codelineno-4-11)[- 9.8 is equivalent to 9.80](https://docs.vllm.ai#__codelineno-4-12)[- 9.80 has 8 tenths, while 9.11 has only 1 tenth](https://docs.vllm.ai#__codelineno-4-13)[- Since 8 tenths (0.8) is greater than 1 tenth (0.1), 9.8 > 9.11](https://docs.vllm.ai#__codelineno-4-14)[Let me know if you need further clarification! 😊](https://docs.vllm.ai#__codelineno-4-16)

#### thinking=False[¶](https://docs.vllm.ai#thinkingfalse)

The number **9.11** is greater than **9.8**.
To compare them:
- 9.11 = 9 + 11/100
- 9.8 = 9 + 80/100
Since 11/100 (0.11) is less than 80/100 (0.80), 9.11 is actually smaller than 9.8. Wait, let me correct that:
Actually, **9.8 is greater than 9.11**.
- 9.8 can be thought of as 9.80
- Comparing 9.80 and 9.11: 80 hundredths is greater than 11 hundredths.
So, **9.8 > 9.11**.
Apologies for the initial confusion! 😅


### curl Example[¶](https://docs.vllm.ai#curl-example)

You can run the following `curl`

command: