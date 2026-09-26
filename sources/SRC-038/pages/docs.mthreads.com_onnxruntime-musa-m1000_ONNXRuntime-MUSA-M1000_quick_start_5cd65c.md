source: https://docs.mthreads.com/onnxruntime-musa-m1000/ONNXRuntime-MUSA-M1000/quick_start

# 快速开始

本章使用一个自包含的示例包验证推理链路。示例包只依赖 `onnxruntime`

与 `numpy`

，附带一个通用的 mobilenet_v2 模型，可直接在 M1000 上运行。

开始前请先完成[安装与验证](https://docs.mthreads.com/onnxruntime-musa-m1000/ONNXRuntime-MUSA-M1000/installation)。

## Step1 下载并校验示例包[](https://docs.mthreads.com#step1-下载并校验示例包)

`wget https://mt-vaas-web.tos-cn-beijing.volces.com/release/ort_musa/feature-demos/python/ort_musa_python_demo.tar.gz`


echo "c90b259e1eb517de1ee6c4d606483c28f8faa2893209bcaefc10390ffae0e107 ort_musa_python_demo.tar.gz" | LC_ALL=C sha256sum -c -



预期输出：

`ort_musa_python_demo.tar.gz: OK`



**注意**：输出为 `OK`

才继续。

## Step2 解压[](https://docs.mthreads.com#step2-解压)

`tar xzf ort_musa_python_demo.tar.gz`

cd ort_musa_python_demo



包内结构：

`ort_musa_python_demo/`

├── README.md

├── run_demo.py

├── SHA256SUMS

├── LICENSE-mobilenet_v2.txt

└── models/

└── mobilenet_v2_fp16.onnx



## Step3 运行[](https://docs.mthreads.com#step3-运行)

`python3 run_demo.py --model models/mobilenet_v2_fp16.onnx --device-id 0`



预期输出：

`onnxruntime : 1.23.0+musa.04f2c3f1`

providers : ['MUSAExecutionProvider', 'CPUExecutionProvider']

model : mobilenet_v2_fp16.onnx

output : (1, 1000)

inference : <耗时> ms (mean of 20, after 3 warmup)

PASS: MUSA EP Python inference completed.



**注意**：以下三项同时满足即表示推理链路已跑通——`providers`

中含 `MUSAExecutionProvider`

；`output`

为 `(1, 1000)`

；末行为 `PASS: MUSA EP Python inference completed.`

。`inference`

一行随设备负载波动，仅用于说明输出格式。

## 示例脚本说明[](https://docs.mthreads.com#示例脚本说明)

`run_demo.py`

接受两个可选参数：

| 参数 | 含义 | 默认值 |
|---|---|---|
`--model` | ONNX 模型路径，相对路径按脚本所在目录解析 | `models/mobilenet_v2_fp16.onnx` |
`--device-id` | GPU 编号，M1000 单卡设备保持 `0` | `0` |

脚本从 session 自动查询第一个输入的名称、形状与数据类型并构造随机输入，因此更换为**单输入、静态 shape** 的同类模型时无需修改脚本：

`python3 run_demo.py --model /path/to/your_model.onnx --device-id 0`



多输入、动态维度、多输出等情形的适配方式见[模型集成](https://docs.mthreads.com/onnxruntime-musa-m1000/ONNXRuntime-MUSA-M1000/model_integration)。