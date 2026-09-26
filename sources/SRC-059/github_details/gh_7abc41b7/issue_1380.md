# [Issue #1380] WebUI一直在加载中

source: https://github.com/PaddlePaddle/ERNIE/issues/1380
state: closed | updated: 2025-11-26T07:44:59Z
labels: 

## 正文

<img width="1361" height="733" alt="Image" src="https://github.com/user-attachments/assets/9b252017-2fbf-48a3-bc16-e75a34079ed3" />

运行命令：
```
erniekit webui
```

gradio版本：`5.50.0`

请问，怎么解决呢？

## 评论 (3)

### Jonathans575 · 2025-11-25

感谢反馈，我们排查一下

### JoelEmbiiddddd · 2025-11-26

hi，经排查，该问题在`gradio==5.50.0`时是本地能够复现，后续发现是由于gradio版本升级导致tab()组件初始化异常，webui未能及时的兼容新版本，导致前端渲染异常。

建议您将gradio的版本降至`gradio==5.42.0`进行使用，后续我们也将会对`gradio==5.50+`版本进行兼容。感谢您的反馈。

### chenyihang1993 · 2025-11-26

> hi，经排查，该问题在`gradio==5.50.0`时是本地能够复现，后续发现是由于gradio版本升级导致tab()组件初始化异常，webui未能及时的兼容新版本，导致前端渲染异常。
> 
> 建议您将gradio的版本降至`gradio==5.42.0`进行使用，后续我们也将会对`gradio==5.50+`版本进行兼容。感谢您的反馈。

收到，已降级，感谢～
