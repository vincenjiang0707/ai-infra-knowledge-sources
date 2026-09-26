# [Issue #1377] ERNIE-4.5-VL-28B-A3B-Thinking: tokenizer_config.json里的chat_template与vllm里的不一致

source: https://github.com/PaddlePaddle/ERNIE/issues/1377
state: closed | updated: 2026-02-25T12:01:53Z
labels: 

## 正文

vllm命令：
vllm serve ERNIE-4.5-VL-28B-A3B-Thinking --trust-remote-code
--reasoning-parser ernie45
--tool-call-parser ernie45
--enable-auto-tool-choice --cpu-offload-gb 48

跟踪模型的输入，结果是：
<|begin_of_sentence|>You are a multimodal AI assistant called ERNIE developed by Baidu based on the PaddlePaddle framework.\nUser: <|IMAGE_START|><|image@placeholder|><|IMAGE_END|>\nFrom which era does the artifact in the image originate?\nAssistant: \n\n

而直接读取tokenizer_config.json里的chat_template，结果是：
<|begin_of_sentence|>You are a multimodal AI assistant called ERNIE developed by Baidu based on the PaddlePaddle framework.
User: Picture 1:<|IMAGE_START|><|image@placeholder|><|IMAGE_END|>From which era does the artifact in the image originate?
Assistant:

直接读取chat_template结果中多了Picture 1。同样，视频多了Video 1。

虽然以上两个输入，模型的输出几乎不受影响。

本着严谨的态度，询问一下哪个才是正确的？

## 评论 (8)

### a31413510 · 2025-11-25

收到，我们复现一下

### CSWYF3634076 · 2025-11-25

在vllm的代码中，调用apply_chat_template之前会有一系列数据处理[代码](https://github.com/vllm-project/vllm/blob/main/vllm/entrypoints/chat_utils.py#L1624)，不是直接用message调用apply_chat_template。28B-VL-Thinking模型运行时，对应的wrap_dicts为false（false的原因[代码](https://github.com/vllm-project/vllm/blob/main/vllm/entrypoints/chat_utils.py#L411)，判定chattemplate为string格式），然后在[代码](https://github.com/vllm-project/vllm/blob/main/vllm/entrypoints/chat_utils.py#L1427)中会调用mm_placeholder_storage进行占位符拼接，这部分无Picture字符串，故最后没有Picture

### jikhunb · 2025-11-25

> 在vllm的代码中，调用apply_chat_template之前会有一系列数据处理[代码](https://github.com/vllm-project/vllm/blob/main/vllm/entrypoints/chat_utils.py#L1624)，不是直接用message调用apply_chat_template。28B-VL-Thinking模型运行时，对应的wrap_dicts为false（false的原因[代码](https://github.com/vllm-project/vllm/blob/main/vllm/entrypoints/chat_utils.py#L411)，判定chattemplate为string格式），然后在[代码](https://github.com/vllm-project/vllm/blob/main/vllm/entrypoints/chat_utils.py#L1427)中会调用mm_placeholder_storage进行占位符拼接，这部分无Picture字符串，故最后没有Picture

非常感谢您的回答。我没有进一步细看您给出的代码链接，也许有空的话，我会细看。

我有个疑问，在模型的监督微调过程是严格按照tokenizer_config.json里的chat_template加上Picture还是直接使用vllm框架不加Picture，因为我觉得模型看到的才是重要的，正因为这样我才去追踪模型的输入。

所以，我关心的是在模型的训练语料，监督微调数据构造中，有Picture，还是没有Picture？

### jikhunb · 2025-11-25

只要我知道模型的准确输入，我可以直接使用更底层vllm的代码来取代vllm server和openai api的组合。

### a31413510 · 2025-11-26

训练是按照tokenizer_config.json里的chat_template

### jikhunb · 2025-11-26

> 训练是按照tokenizer_config.json里的chat_template

非常感谢您的回答。

我在使用vllm和openai api等框架时，受够了他们的层层封装，总感觉迟早会出问题。果然，预言被验证了。

### a31413510 · 2025-11-26

好的，有问题再沟通

### nepeplwu · 2026-02-25

The issue has no response for a long time and will be closed. You can reopen or new another issue if are still confused.

---
_From Bot_
