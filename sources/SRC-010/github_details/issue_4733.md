# [Issue #4733] [Feature] support --default-chat-template-kwargs '{"enable_thinking": false}'

source: https://github.com/InternLM/lmdeploy/issues/4733
state: closed | updated: 2026-07-08T05:57:32Z
labels: 

## 正文

### Motivation

添加此参数，原生支持不输出思维链

### Related resources

_No response_

### Additional context

_No response_

## 评论 (5)

### CUHKSZzxy · 2026-07-06

这个参数需要在 client 端传入，示例如下

```python
from openai import OpenAI

client = OpenAI(api_key='YOUR_API_KEY', base_url='http://0.0.0.0:23333/v1')
model_name = client.models.list().data[0].id

response = client.chat.completions.create(
    model=model_name,
    messages=[{
        'role': 'user',
        'content': [{
            'type': 'text',
            'text': '9.11 and 9.8, which is greater?',
        }],
    }],
    temperature=0.8,
    top_p=0.8,
    # extra_body for reasoning
    extra_body={'chat_template_kwargs': {
        'enable_thinking': False
    }})
print(response)
```

### bltcn · 2026-07-07

实测对qwen3.6-35b-a3b无效

### CUHKSZzxy · 2026-07-08

<img width="1454" height="565" alt="Image" src="https://github.com/user-attachments/assets/473b7ae8-1992-45ca-a45d-f3b4fbdd10db" />

我用 qwen3.6-35b-a3b 测试了，enable_thinking 功能正常。
可能和用户输入或者模型本身有关系。enable_thinking 只是在用户输入中添加 thinking 的特殊字符，然后直接送给模型进行预测。特定输入+模型本身可能没有训好，不排除此时思考模式开关失效的可能性

你的启动命令和输入是怎么样的，方便分享一下吗？

### bltcn · 2026-07-08

我再试试，谢谢

### bltcn · 2026-07-08

测试了没问题，@CUHKSZzxy 谢谢
