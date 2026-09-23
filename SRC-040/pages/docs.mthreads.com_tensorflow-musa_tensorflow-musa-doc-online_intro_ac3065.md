source: https://docs.mthreads.com/tensorflow-musa/tensorflow-musa-doc-online/intro

# TensorFlow-MUSA 简介

TensorFlow-MUSA 是摩尔线程（Moore Threads）为 MUSA 架构 GPU 推出的专属插件。它通过将 MUSA 注册为原生 TensorFlow 设备，让开发者能够在摩尔线程硬件上基于 TensorFlow 进行 AI 模型的训练与推理任务。

## 工作原理[](https://docs.mthreads.com#工作原理)

`用户TensorFlow程序`

(训练/推理/模型脚本)

│

▼

标准 TensorFlow API

│

▼

tensorflow_musa Python wrapper

(import tensorflow_musa)

设备查询 / 配置接口 / 加载插件

│

▼

libmusa_plugin.so

(MUSA 后端插件)

│

▼

MUSA SDK（5.1.0+）

Runtime / mublas / mudnn / mcc 等

提交 kernel / 管理显存与 stream

│

▼

MUSA GPU