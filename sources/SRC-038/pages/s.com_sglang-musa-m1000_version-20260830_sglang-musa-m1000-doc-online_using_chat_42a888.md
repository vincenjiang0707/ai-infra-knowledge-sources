source: https://docs.mthreads.com/sglang-musa-m1000/version-20260830/sglang-musa-m1000-doc-online/using_chat

# 服务调用

## 接口测试[](https://docs.mthreads.com#接口测试)

服务启动后，可以通过 OpenAI 兼容接口查看模型信息：

`curl http://127.0.0.1:30000/v1/models`



## Chat Completions 调用[](https://docs.mthreads.com#chat-completions-调用)

`curl http://127.0.0.1:30000/v1/chat/completions \`

-H "Content-Type: application/json" \

-d '{

"temperature": 0.7,

"top_p": 0.8,

"max_tokens": 100,

"chat_template_kwargs":{"enable_thinking":false},

"messages": [

{

"role": "user",

"content": "北京有哪些名胜古迹？"

}

]

}'



## Python 调用[](https://docs.mthreads.com#python-调用)

### 流式输出[](https://docs.mthreads.com#流式输出)

`from openai import OpenAI`


openai_api_key = "EMPTY"

openai_api_base = "http://127.0.0.1:30000/v1"


client = OpenAI(

api_key=openai_api_key,

base_url=openai_api_base,

)


models = client.models.list()

model = models.data[0].id


chat_completion = client.chat.completions.create(

messages=[

{

"role": "system",

"content": "You are a helpful assistant.",

},

{

"role": "user",

"content": "北京有哪些名胜古迹？",

},

],

model=model,

temperature=0.7,

top_p=0.8,

max_tokens=100,

stream=True,

)


print("Chat response (streaming):")

for chunk in chat_completion:

if chunk.choices:

delta = chunk.choices[0].delta

content = delta.content

if content:

print(content, end="", flush=True)

print("\n - Chat response (end) -\n")



### 非流式输出[](https://docs.mthreads.com#非流式输出)

`from openai import OpenAI`


openai_api_key = "EMPTY"

openai_api_base = "http://127.0.0.1:30000/v1"


client = OpenAI(

api_key=openai_api_key,

base_url=openai_api_base,

)


models = client.models.list()

model = models.data[0].id


chat_completion = client.chat.completions.create(

messages=[

{

"role": "system",

"content": "You are a helpful assistant.",

},

{

"role": "user",

"content": "北京有哪些名胜古迹？",

},

],

model=model,

temperature=0.7,

top_p=0.8,

max_tokens=100,

stream=False,

)


print("Chat completion results:")

print(chat_completion)



## 多模态图片调用[](https://docs.mthreads.com#多模态图片调用)

### 使用在线图片 URL[](https://docs.mthreads.com#使用在线图片-url)

`curl http://localhost:30000/v1/chat/completions \`

-H "Content-Type: application/json" \

-d '{

"model": "/home/dev/models/gptq-Qwen3-VL-8B-Instruct-4bit-group",

"max_tokens": 256,

"messages": [

{

"role": "user",

"content": [

{"type": "text", "text": "请描述这张图片。"},

{

"type": "image_url",

"image_url": {

"url": "https://modelscope.oss-cn-beijing.aliyuncs.com/resource/qwen.png"

}

}

]

}

]

}'



### 使用本地图片进行测试[](https://docs.mthreads.com#使用本地图片进行测试)

下面示例会在内存中生成一张 32×32 的四色块 PNG 图片，并调用多模态模型识别图片颜色。该测试适合快速确认图片输入链路是否可用。

`import base64`

import io


from openai import OpenAI

from PIL import Image, ImageDraw


client = OpenAI(api_key="EMPTY", base_url="http://localhost:30000/v1")

model = client.models.list().data[0].id


image = Image.new("RGB", (32, 32), "white")

draw = ImageDraw.Draw(image)

draw.rectangle([0, 0, 15, 15], fill="red")

draw.rectangle([16, 0, 31, 15], fill="green")

draw.rectangle([0, 16, 15, 31], fill="blue")

draw.rectangle([16, 16, 31, 31], fill="yellow")


buffer = io.BytesIO()

image.save(buffer, format="PNG")

image_base64 = base64.b64encode(buffer.getvalue()).decode("utf-8")

image_url = f"data:image/png;base64,{image_base64}"


response = client.chat.completions.create(

model=model,

messages=[{

"role": "user",

"content": [

{"type": "text", "text": "This image is divided into four colored blocks. List the visible colors only."},

{"type": "image_url", "image_url": {"url": image_url}},

],

}],

max_tokens=128,

)


print(response.choices[0].message.content)



提示

图�片测试用于快速验证多模态服务链路。若模型能完成文本对话且能识别出部分图片信息，通常说明图片输入链路已连通；如果需要评估多模态质量，建议结合真实图片和更明确的问题进一步测试。