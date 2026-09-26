source: https://docs.mthreads.com/onnxruntime-musa-m1000/ONNXRuntime-MUSA-M1000/provider_options

# 性能特性�开关

`MUSAExecutionProvider`

提供若干可选开关，通过 providers 的 option 字典设置，对模型直接生效，无需修改模型文件。

`providers = [`

("MUSAExecutionProvider", {

"device_id": "0",

"prefer_nhwc": "1",

"allow_tf32": "1",

}),

"CPUExecutionProvider",

]



**注意**：option 的取值统一使用字符串。Python 接口会将整数 `0`

/ `1`

规范化为 `"0"`

/ `"1"`

，与字符串写法等价；但布尔值会被转换为 `"True"`

/ `"False"`

，不保证被按 `0`

/ `1`

解析，请勿使用。

## 开关说明[](https://docs.mthreads.com#开关说明)

| 开关 | 取值 | 作用 |
|---|---|---|
`device_id` | GPU 编号字符串，默认 `"0"` | 指定推理使用的 GPU。M1000 为单卡设备，保持 `"0"` |
`prefer_nhwc` | `"0"` / `"1"` | 卷积类算子改用 NHWC 布局。适用于以卷积为主的 CNN 模型 |
`allow_tf32` | `"0"` / `"1"` ，默认 `"1"` | 对 fp32 模型的卷积与矩阵乘启用 TF32（尾数截断）。对 fp16 模型不产生作用 |
`enable_musa_graph` | `"0"` / `"1"` ，默认 `"0"` | 捕获推理的调度序列并在后续调用中重放。须配合 IOBinding 使用，前提条件见
|

## 适用性说明[](https://docs.mthreads.com#适用性说明)

上述开关中，`device_id`

用于选择设备，`prefer_nhwc`

与 `allow_tf32`

影响计算过程，`enable_musa_graph`

影响调度方式并对调用方式有额外要求。本节说明前两者，`enable_musa_graph`

见本页末节。

`prefer_nhwc`

的收益取决于模型结构。以卷积为主的模型通常受益；而当模型中存在不支持 NHWC 布局的算子、且这些算子夹在卷积之间时，会引入额外的布局转换，反而可能变慢。

需要说明的是，**NHWC 布局支持仍在持续完善中**：支持该布局的算子范围会随版本扩展，因此同一模型开启该开关的收益也会随版本变化。本版不给出推荐启用的模型范围，也不发布该开关下的性能数据，请按下面的方式逐模型实测��后决定。

`allow_tf32`

只作用于 fp32 模型的卷积与矩阵乘。该开关默认启用，对 fp16 模型不产生作用。

**上述两个开关的实际效果与模型结构强相关，上线前须在自研工程内实测确认。**

方式为：对同一模型分别测量该开关取 `"0"`

与 `"1"`

时的推理延迟，并按[模型集成](https://docs.mthreads.com/onnxruntime-musa-m1000/ONNXRuntime-MUSA-M1000/model_integration)的精度验证方法对比输出，据实选用。不建议未经实测即全部启用。

## 进一步的优化方式[](https://docs.mthreads.com#进一步的优化方式)

`session.run()`

直接传入 numpy 数组时，每次调用都包含一次 host 与 device 之间的数据拷贝。若模型的输入输出可常驻设备内存，可使用 ONNX Runtime 的 IOBinding 接口省去该拷贝。

### 图捕获（MUSA Graph）[](https://docs.mthreads.com#musa-graph)

引擎提供 `enable_musa_graph`

开关（默认 `"0"`

），��启用后把一次推理的调度序列捕获为一张图并在后续调用中重放，用于降低逐次的调度开销。C++ 接口对应 `OrtMUSAProviderOptions`

的 `enable_musa_graph`

字段。

**该开关必须配合 IOBinding 使用，不能与直接调用 session.run() 传入 numpy 数组的写法混用。**

启用后须同时满足以下条件，否则推理调用会返回错误而不会静默降级：

| 条件 | 说明 |
|---|---|
| 输入与输出均预先分配 | 输入和输出都必须是调用方预先分配好的 tensor，不能由引擎在调用时分配输出 |
| 均位于 MUSA 设备内存 | 上述 tensor 须位于 MUSA 设备上，且设备编号与 `device_id` 一致；不接受 host 侧数据 |
| 跨次调用保持不变 | 同一 session 的后续调用中，输入输出的名称、个数、形状、数据类型以及设备内存地址都须与捕获时一致。任一项变化都须新建 session 重新捕获 |

未满足第一、二项时的错误信息为：

`MUSA Graph capture requires static device IOBinding with preallocated, long-lived MUSA device inputs and outputs; ordinary session.run() with CPU feeds or dynamically allocated outputs is not supported.`



第三项不满足时的错误信息为 `MUSA Graph replay signature mismatch`

，并指明发生变化的是名称、地址、形状还是数据类型。

需要说明的是，**图捕获支持仍在持续完善中**：适用的模型范围与上述使用约束都可能随版本调整，因此本版不给出推荐启用的模型范围，也不发布该开关下的性能数据。本版建议先按默认值 `"0"`

使用。

由于上述约束要求调用方自行管理设备内存的生命周期，接入方式与业务的内存管理强相关。本版文档不提供独立示例，需要接入请联系摩尔线程技术支持获取对应说明。

IOBinding 的使用方式同样可联系技术支持获取。