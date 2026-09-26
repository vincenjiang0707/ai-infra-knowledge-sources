# [Issue #1372] baidu/ERNIE-4.5-VL-28B-A3B-Thinking本地图片示例代码

source: https://github.com/PaddlePaddle/ERNIE/issues/1372
state: closed | updated: 2026-02-21T12:02:18Z
labels: 

## 正文

您好，我正在借助baidu/ERNIE-4.5-VL-28B-A3B-Thinking开源模型完成图片评估任务，但我发现huggingface上仅提供了网络图片的传入方法，我想知道应该如何传入本地图片，希望官方可以提供给我一个示例代码，谢谢。

## 评论 (5)

### BossPi · 2025-11-19

您好，您可以参考如下方式传入本地图片：
```
messages = [
    {
        "role": "user",
        "content": [
            {"type": "text", "text": "What color clothes is the girl in the picture wearing?"},
            {"type": "image_url", "image_url": {"url": "local_image.jpg"}},
        ]
    },
]
```
您只需要简单地将示例中的url链接替换为本地图片路径即可传入本地图片。如果您还有其他问题，欢迎随时提问。

### Blinkion · 2025-11-22

为什么我传入本地图片后会报Incorrect padding？

### BossPi · 2025-11-22

请问方便提供您的运行代码和具体的报错信息吗？

### nepeplwu · 2026-02-21

The issue has no response for a long time and will be closed. You can reopen or new another issue if are still confused.

---
_From Bot_

### Blinkion · 2026-02-21

这是来自QQ邮箱的假期自动回复邮件。您好，我已经收到您的邮件。我将在阅读后，尽快给您回复。
