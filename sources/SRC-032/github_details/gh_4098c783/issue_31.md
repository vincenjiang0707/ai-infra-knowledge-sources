# [Issue #31] Huawei NPU device_map=auto doesn't split model evenly over all devices

source: https://github.com/Ascend/pytorch/issues/31
state: open | updated: 2025-02-27T09:50:46Z
labels: 

## 正文

https://github.com/huggingface/accelerate/issues/2368

这个地址说4月底能够解决，目前好像还是不行，不知道是不是解决了？

## 评论 (4)

### yunyiyun · 2024-05-23

请使用最新版本的cann和torch_npu，如果不行，请提供具体报错信息。

### xiuxiuxius · 2024-06-05

环境：910B4，32G*2
cann：8.0.rc1
torch_npu：2.2.0
python：3.10

代码如下，我使用官方示例加载qwen1.5-32B-chat，发现模型权重没有平均加载到两张卡上，而是每张卡都加载了一遍，导致显存不足，帮忙看下
```
import os
os.environ['NPU_VISIBLE_DEVICES']='0,1'
os.environ['ASCEND_RT_VISIBLE_DEVICES']='0,1'
import time
import torch
import torch_npu
from modelscope import AutoModelForCausalLM, AutoTokenizer


# model_name = "qwen/Qwen1.5-0.5B-Chat"
model_name = "qwen/Qwen1.5-32B-Chat"


tt1 = time.time()
model = AutoModelForCausalLM.from_pretrained(model_name,device_map="auto")
device = next(model.parameters()).device
print("模型所在的device:", device)
# model = AutoModelForCausalLM.from_pretrained(model_name, device_map="auto").npu().eval()

tt2 = time.time()


print("load model successfully")

tokenizer = AutoTokenizer.from_pretrained(model_name)

prompts = [
    "背诵出师表",
    "描述一下夏天的天气",
    "介绍一下自然语言处理的基本概念",
    "讲一个你喜欢的故事",
    "谈谈你对人工智能的看法"
]

total_time = 0

for prompt in prompts:
    print("输入文本:", prompt)
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt}
    ]
    text = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True
    )
    model_inputs = tokenizer([text], return_tensors="pt").to(device)
    # model_inputs = tokenizer([text], return_tensors="pt").npu()
    t1 = time.time()
    generated_ids = model.generate(
        model_inputs.input_ids,
        max_new_tokens=512
    )
    t2 = time.time()
    print("回答:", tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0])
    elapsed_time = t2 - t1
    print("生成耗时:", elapsed_time)
    total_time += elapsed_time

average_time = total_time / len(prompts)


print("模型：", model_name)
print("加载模型耗时：", tt2 - tt1)
print("生成平均耗时: ", average_time)
```
![image](https://github.com/Ascend/pytorch/assets/89114157/252dbe48-ab49-4b9b-bee0-35028ce3d4e6)


### xiuxiuxius · 2024-06-06

> 环境：910B4，32G*2 cann：8.0.rc1 torch_npu：2.2.0 python：3.10
> 
> 代码如下，我使用官方示例加载qwen1.5-32B-chat，发现模型权重没有平均加载到两张卡上，而是每张卡都加载了一遍，导致显存不足，帮忙看下
> 
> ```
> import os
> os.environ['NPU_VISIBLE_DEVICES']='0,1'
> os.environ['ASCEND_RT_VISIBLE_DEVICES']='0,1'
> import time
> import torch
> import torch_npu
> from modelscope import AutoModelForCausalLM, AutoTokenizer
> 
> 
> # model_name = "qwen/Qwen1.5-0.5B-Chat"
> model_name = "qwen/Qwen1.5-32B-Chat"
> 
> 
> tt1 = time.time()
> model = AutoModelForCausalLM.from_pretrained(model_name,device_map="auto")
> device = next(model.parameters()).device
> print("模型所在的device:", device)
> # model = AutoModelForCausalLM.from_pretrained(model_name, device_map="auto").npu().eval()
> 
> tt2 = time.time()
> 
> 
> print("load model successfully")
> 
> tokenizer = AutoTokenizer.from_pretrained(model_name)
> 
> prompts = [
>     "背诵出师表",
>     "描述一下夏天的天气",
>     "介绍一下自然语言处理的基本概念",
>     "讲一个你喜欢的故事",
>     "谈谈你对人工智能的看法"
> ]
> 
> total_time = 0
> 
> for prompt in prompts:
>     print("输入文本:", prompt)
>     messages = [
>         {"role": "system", "content": "You are a helpful assistant."},
>         {"role": "user", "content": prompt}
>     ]
>     text = tokenizer.apply_chat_template(
>         messages,
>         tokenize=False,
>         add_generation_prompt=True
>     )
>     model_inputs = tokenizer([text], return_tensors="pt").to(device)
>     # model_inputs = tokenizer([text], return_tensors="pt").npu()
>     t1 = time.time()
>     generated_ids = model.generate(
>         model_inputs.input_ids,
>         max_new_tokens=512
>     )
>     t2 = time.time()
>     print("回答:", tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0])
>     elapsed_time = t2 - t1
>     print("生成耗时:", elapsed_time)
>     total_time += elapsed_time
> 
> average_time = total_time / len(prompts)
> 
> 
> print("模型：", model_name)
> print("加载模型耗时：", tt2 - tt1)
> print("生成平均耗时: ", average_time)
> ```
> 
> ![image](https://private-user-images.githubusercontent.com/89114157/336907414-252dbe48-ab49-4b9b-bee0-35028ce3d4e6.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MTc2NjY1MDcsIm5iZiI6MTcxNzY2NjIwNywicGF0aCI6Ii84OTExNDE1Ny8zMzY5MDc0MTQtMjUyZGJlNDgtYWI0OS00YjliLWJlZTAtMzUwMjhjZTNkNGU2LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDA2MDYlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwNjA2VDA5MzAwN1omWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTc5ZWRlMmViZDdlNjg1YzEyNGRmMjJmMGZmNWI1MjlhOTUzMmUzNTY1NDgzNzc5NWRjNzUxNjVmMzFiNDI2ZGImWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.mutQYlgxr0BbXLLhC-bY5qrlrg4ZGmxvAAcPwk86XLI)

我是这么解决的
```bash
export ASCEND_LAUNCH_BLOCKING=1
```
PyTorch训练或在线推理场景，可通过此环境变量控制算子执行时是否启动同步模式。当设置为“1”时，强制算子采用同步模式运行，从而更容易地调试和跟踪代码中的问题。设置为“0”时则会采用异步方式执行。

Qwen1.5-32B-Chat消耗的显存如下：
![image](https://github.com/Ascend/pytorch/assets/89114157/2aba4008-0332-4906-9942-ab78e2f1fd37)



### geekchen007 · 2025-02-27

版本问题，torchnpu更新到2.1.0.post10解决，devicemap设置为auto
