source: https://docs.mthreads.com/sglang-musa-m1000/version-20260718/sglang-musa-m1000-doc-online/intro

# SGLang-MUSA M1000 简介

SGLang 是面向大语言模型和视觉语言模型的高性能推理框架。SGLang-MUSA M1000 提供了在摩尔线程 M1000 ��端侧 GPU 上运行 SGLang 的适配能力，便于用户在 MUSA 软件栈中部署模型服务并进行推理验证。

当前文档覆盖 SGLang-MUSA M1000 的环境准备、源码安装、wheel 出包、服务启动、接口调用和性能测试流程。

## 版本说明[](https://docs.mthreads.com#版本说明)

| 组件 | 版本 |
|---|---|
| MUSA | 5.1.1 |
| MUSA SDK | 5.1.1 |
| Triton MUSA | 3.2.0 |
| Torch | 2.9.0 |
| Torch MUSA | 2.9.0 |
| TorchAudio | 2.9.0+eaa9e4e |
| TorchVision | 0.22.1+e98278b |
| TileLang MUSA | 0.1.6.post2+musa.3 |
| MATE | 0.2.0+mu510torch2.9 |
| Apache TVM FFI | 0.1.9.post3.dev0+musa.1.gf6b52d7f4.d20260703 |
| SGLang | 0.5.10+20260630 |
| SGLang Kernel | 0.4.1.dev20260630 |