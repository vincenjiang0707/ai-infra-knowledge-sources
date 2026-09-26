# [Issue #3344] [Bug] Qwen3 model Can not use function calling

source: https://github.com/mlc-ai/mlc-llm/issues/3344
state: open | updated: 2026-08-29T13:24:03Z
labels: bug

## 正文

## 🐛 Bug

According to the sample in the official documentation(https://llm.mlc.ai/docs/deploy/rest.html), when I test function calling, none of the 'Qwen3' series models I deployed locally (' Qwen3-14b-Q4f16_1-MLC ', 'Qwen3-8B-Q4f16_1-MLC') could recognize the tool.

## To Reproduce

The code I used as follows
<!-- If you have a code sample, error messages, stack traces, please provide it here as well -->
```python
import requests
import json

tools = [
   {
      "type": "function",
      "function": {
            "name": "get_current_weather",
            "description": "Get the current weather in a given location",
            "parameters": {
               "type": "object",
               "properties": {
                  "location": {
                        "type": "string",
                        "description": "The city and state, e.g. San Francisco, CA",
                  },
                  "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
               },
               "required": ["location"],
            },
      },
   }
]

payload = {
   "model": "./Qwen3-8B-Q4f16_1-MLC",
   "messages": [
      {
            "role": "user",
            "content": "What is the current weather in Pittsburgh, PA in fahrenheit?",
      }
   ],
   "stream": False,
   "tools": tools,
}

r = requests.post("http://127.0.0.1:8000/v1/chat/completions", json=payload)
print(f"{r.json()['choices'][0]['message']['tool_calls'][0]['function']}\n")
```

Output as follows
```
Traceback (most recent call last):
  File "/home/otcaix/dev-proj/tmp/test2.py", line 38, in <module>
    print(f"{r.json()['choices'][0]['message']['tool_calls'][0]['function']}\n")
TypeError: 'NoneType' object is not subscriptable
```

## Expected behavior

`Output: {'name': 'get_current_weather', 'arguments': {'location': 'Pittsburgh, PA', 'unit': 'fahrenheit'}}`
<!-- A clear and concise description of what you expected to happen. -->

## Environment

 - Platform (e.g. WebGPU/Vulkan/IOS/Android/CUDA): CUDA
 - Operating system (e.g. Ubuntu/Windows/MacOS/...): Ubuntu 22.04
 - Device (e.g. iPhone 12 Pro, PC+RTX 3090, ...): Nvidia Jetson Orin 64GB
 - How you installed MLC-LLM (`conda`, source): MLC-LLM docker images(provided by https://github.com/dusty-nv/jetson-containers/tree/master/packages/llm/mlc)
 - Any other relevant information: mlc docker image version is 0.20.0

## Additional context

<!-- Add any other context about the problem here. -->


## 评论 (2)

### delphiRo · 2025-10-18

<img width="1280" height="823" alt="Image" src="https://github.com/user-attachments/assets/5ca285a6-4440-4a08-8764-bf5b3e50ec19" />

### gokuljp78 · 2026-08-29

does this issue solved ?
