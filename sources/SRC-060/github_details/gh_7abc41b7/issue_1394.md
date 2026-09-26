# [Issue #1394] ERNIE-4.5-VL-28B-A3B-Thinking 如何测试think with image的能力

source: https://github.com/PaddlePaddle/ERNIE/issues/1394
state: open | updated: 2026-01-13T04:16:35Z
labels: 

## 正文

请问如何测试ERNIE-4.5-VL-28B-A3B-Thinking的 think with image的能力 或者 工具调用的测试代码？

## 评论 (1)

### dongZheX · 2026-01-13

感谢使用ERNIE-4.5-VL-28B-A3B-Thinking，下面是工具调用使用的示例：

### 启动 vLLM 服务

```bashhttps://github.com/PaddlePaddle/ERNIE/issues/1394#top
vllm serve baidu/ERNIE-4.5-VL-28B-A3B-Thinking --trust-remote-code \
    --reasoning-parser ernie45 \
    --tool-call-parser ernie45 \
    --enable-auto-tool-choice
```

### Python 测试代码

```python
from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:8000/v1",
    api_key="EMPTY"
)

tools = [
    {
        "type": "function",
        "function": {
            "name": "image_search",
            "description": "Image search engine, input the image and search for similar images.",
            "parameters": {
                "type": "object",
                "properties": {
                    "img_idx": {
                        "type": "number",
                        "description": "The index of the image (starting from 0)"
                    }
                },
                "required": ["img_idx"]
            }
        }
    }
]

response = client.chat.completions.create(
    model="baidu/ERNIE-4.5-VL-28B-A3B-Thinking",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "image_url",
                    "image_url": {
                        "url": "https://img3.chinadaily.com.cn/images/202411/10/67304d18a310b5910b7e518c.png",
                        "detail": "high"
                    }
                },
                {
                    "type": "text",
                    "text": "这是什么"
                }
            ]
        }
    ],
    tools=tools,
    tool_choice="auto",
    temperature=0.2,
    max_tokens=16384
)

message = response.choices[0].message

# 思考内容
if hasattr(message, 'reasoning_content') and message.reasoning_content:
    print(f"Thinking: {message.reasoning_content}")

# 工具调用
if message.tool_calls:
    for tool_call in message.tool_calls:
        print(f"Tool: {tool_call.function.name}, Args: {tool_call.function.arguments}")
else:
    print(f"Response: {message.content}")
```
