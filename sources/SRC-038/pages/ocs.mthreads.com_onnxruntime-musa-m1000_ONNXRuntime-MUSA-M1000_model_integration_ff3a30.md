source: https://docs.mthreads.com/onnxruntime-musa-m1000/ONNXRuntime-MUSA-M1000/model_integration

# 模型集成

本章介绍将自研 ONNX 模型接入 ONNXRuntime-MUSA-M1000 的方式，以及上线前的两项验证。

## 推理代码[](https://docs.mthreads.com#推理代码)

接入方式与上游 ONNX Runtime 一致，差异仅在于构造 `InferenceSession`

时将 `MUSAExecutionProvider`

置于 providers 列表首位。模型本身无需修改。

`import onnxruntime as ort`

import numpy as np


session = ort.InferenceSession(

"your_model.onnx",

providers=[

("MUSAExecutionProvider", {"device_id": "0"}),

"CPUExecutionProvider",

],

)


inp = session.get_inputs()[0]

x = np.random.default_rng(0).standard_normal(

[d if isinstance(d, int) else 1 for d in inp.shape]

).astype(np.float16 if "float16" in inp.type else np.float32)


outputs = session.run(None, {inp.name: x})

print("output:", outputs[0].shape)



将 `"your_model.onnx"`

替换为实际模型路径后即可运行。

列表中的 `CPUExecutionProvider`

用于个别算子未被支持时由引擎自动改用 CPU 执行。

上例只设置了 `device_id`

，这是基础接入配置。`prefer_nhwc`

、`allow_tf32`

等性能开关的收益与模型�强相关，请按[性能特性开关](https://docs.mthreads.com/onnxruntime-musa-m1000/ONNXRuntime-MUSA-M1000/provider_options)完成实测对比后再决定是否启用。

首次运行包含初始化开销，测量延迟前先执行 2 至 3 次预热再统计。

## 输入输出适配[](https://docs.mthreads.com#输入输出适配)

上述代码为单输入模板。其他情形按下表在业务侧适配：

| 情形 | 适配方式 |
|---|---|
| 多输入 | 遍历 `session.get_inputs()` ，按各输入的 name、shape、type 分别构造数组，以 `session.run(None, {name1: x1, name2: x2, ...})` 执行 |
| fp16 输入输出 | 输入数组的 dtype 使用 `np.float16` 。注意 `mobilenet_v2_fp16.onnx` 为 fp16 权重、fp32 输入输出 |
| 动态维度 | 模板中将动态维度置 1 仅为占位。实际须按业务显式固定 batch、分辨率等维度，而非置 1 |
| 多输出 | `session.run(None, feeds)` 按 `session.get_outputs()` 的顺序返回列表，逐个按各自的 dtype 与 shape 读取 |

图像缩放、归一化、检测框解码等前后处理在业务侧完成，与推理过程解耦。

## 精度验证[](https://docs.mthreads.com#精度验证)

**上线前须对自研模型执行精度验证。**

同一模型、同一输入，分别以纯 `CPUExecutionProvider`

与 `MUSAExecutionProvider`

各建一个 session 执行一次，对比两者输出。判定标准为余弦相似度不低于 0.999（该指标与数值尺度无关），且 MUSA 侧输出非全零。

将下列脚本中的 `MODEL`

替换为实际模型路径后运行，多输入模型按注释补齐 feed：

`import numpy as np, onnxruntime as ort`


MODEL = "your_model.onnx"


def run(providers):

s = ort.InferenceSession(MODEL, providers=providers)

inp = s.get_inputs()[0]

shape = [d if isinstance(d, int) else 1 for d in inp.shape] # 动态维度置 1 为占位，按业务修改

x = np.random.default_rng(42).standard_normal(shape).astype(

np.float16 if "float16" in inp.type else np.float32)

return s.run(None, {inp.name: x}) # 多输入时改为 {n1: x1, n2: x2, ...}


musa = run([("MUSAExecutionProvider", {"device_id": "0"}), "CPUExecutionProvider"])

cpu = run(["CPUExecutionProvider"])

for i, (m, c) in enumerate(zip(musa, cpu)):

m, c = m.ravel().astype(np.float64), c.ravel().astype(np.float64)

cos = float(m @ c / (np.linalg.norm(m) * np.linalg.norm(c) + 1e-12))

print(f"output[{i}] cosine={cos:.8f} musa_all_zero={not np.any(m)}")

assert cos >= 0.999 and np.any(m), f"output[{i}] 精度不达标（cosine={cos:.8f}）"

print("PASS: MUSA vs CPU 精度验证通过")



预期输出末行：

`PASS: MUSA vs CPU 精度验证通过`



**注意**：脚本在不达标时会以 `AssertionError`

中止并打印该输出的 cosine 值。出现 `musa_all_zero=True`

或 cosine 明显偏低时，请按[常见问题](https://docs.mthreads.com/onnxruntime-musa-m1000/ONNXRuntime-MUSA-M1000/faq)提供的信息联系摩尔线程技术支持。

## 确认节点在 GPU 上执行[](https://docs.mthreads.com#确认节点在-gpu-上执行)

`providers`

中含 `MUSAExecutionProvider`

只表示 Execution Provider 已加载。模型中个别算子未被支持时，相关节点会由引擎自动改用 CPU 执行，此时 providers 列表不变。

如需确认模型的全部节点都在 GPU 上执行，构造 session 时禁用 CPU 回退，并且 **providers 只传 MUSAExecutionProvider**：

`import numpy as np, onnxruntime as ort`


so = ort.SessionOptions()

so.add_session_config_entry("session.disable_cpu_ep_fallback", "1")

session = ort.InferenceSession(

"your_model.onnx",

sess_options=so,

providers=[("MUSAExecutionProvider", {"device_id": "0"})],

)

print("session created")


inp = session.get_inputs()[0]

x = np.random.default_rng(0).standard_normal(

[d if isinstance(d, int) else 1 for d in inp.shape]

).astype(np.float16 if "float16" in inp.type else np.float32)


outputs = session.run(None, {inp.name: x})

print("output:", outputs[0].shape)

print("PASS: all nodes executed with CPU fallback disabled")



预期输出：

`session created`

output: (1, 1000)

PASS: all nodes executed with CPU fallback disabled



**注意**：`output`

的形状随模型不同，上例取自[快速开始](https://docs.mthreads.com/onnxruntime-musa-m1000/ONNXRuntime-MUSA-M1000/quick_start)的��示例模型。存在无法在 GPU 上执行的节点时，session 创建阶段即报错，看不到 `session created`

；能够创建成功**并完整跑完一次推理、打印出末行**，才表示全部节点都在 GPU 上执行。

**注意**：禁用回退的同时在 providers 中显式列出 `CPUExecutionProvider`

会导致配置冲突，报错如下，因此此处只传 `MUSAExecutionProvider`

：

`INVALID_ARGUMENT : Conflicting session configuration: explicitly added the CPU EP`

to the session, but also disabled fallback to the CPU EP via session configuration options.



`session.get_providers()`

仍可能列出引擎自动注册的 CPU EP，属正常现象。

该配置用于确认节点分布，不作为常规运行配置。若某模型启用后报错，关闭该配置即可正常运行，相关节点将由引擎自动改用 CPU 执行。