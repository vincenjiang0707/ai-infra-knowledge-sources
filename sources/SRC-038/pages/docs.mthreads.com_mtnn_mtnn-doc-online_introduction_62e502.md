source: https://docs.mthreads.com/mtnn/mtnn-doc-online/introduction/

# MTNN 开发者指南

## 什么是 MTNN ?[](https://docs.mthreads.com#什么是-mtnn-)

**MTNN (Moore Threads Neural Network)** 是一组专为 **摩尔线程长江 SoC（M1000）** 平台设计的端侧 AI 推理工具链与运行时库。它帮助开发者将训练好的深度学习模型高效部署到 M1000 设备上，充分发挥其 NPU（神经网络处理单元）的硬件加速能力，实现低延迟、高能效的设备端机器学习。

## 工作流程[](https://docs.mthreads.com#工作流程)

MTNN 的开发工作流清晰简洁，主要分为 **模型转换** 和 **运行推理** 两个阶段：

### 阶段一：模型转换[](https://docs.mthreads.com#阶段一模型转换)

ONNX（Open Neural Network Exchange，开放神经网络交换）是一个开放的模型格式标准，被 PyTorch、TensorFlow 等几乎所有主流 AI 框架支持。

将模型先导出为 **ONNX** 格式，然后使用 MTNN 提供的 `mtc_tool`

工具将其转换为 M1000 专有的 `.mtnn`

模型格式。在此过程中，可以应用量化等优化措施。

无论您最初使用哪种框架训练模型，MTNN 的模型转换极大地简化了部署流程，避免了为每个训练框架单独开发转换器。

关于如何将 PyTorch、TensorFlow 框架的模型转为ONNX模型, 请参考各模型的官网。此外，您还可以使用[PyTorch转ONNX](https://docs.pytorch.org/docs/stable/onnx.html)的通用方法。

### 阶段二：运行推理[](https://docs.mthreads.com#阶段二运行推理)

在 M1000 设备上，应用程序通过 **MTNN Runtime C API** 加载 `.mtnn`

模型，并执行推理任务, 从而实现部署。

## 支持的算子[](https://docs.mthreads.com#支持的算子)

MTNN 通过 ONNX 标准实现广泛的算子兼容性，支持以下常用算子：

类别 | 支持的算子 |
|---|---|
| 基础数学 | `Add` , `Sub` , `Mul` , `Div` , `Abs` , `Exp` , `Log` , `Pow` , `Sqrt` , `Sin` , `Neg` , `Reciprocal` , `Sign` , `Mod` , `Sum` , `Mean` |
| 激活函数 | `Relu` , `LeakyRelu` , `PRelu` , `Sigmoid` , `HardSigmoid` , `HardSwish` , `Tanh` , `Softplus` , `Elu` , `Softsign` |
| 归一化 | `BatchNormalization` , `InstanceNormalization` , `LRN` , `MeanVarianceNormalization` |
| 池化与采样 | `MaxPool` , `AveragePool` , `GlobalMaxPool` , `GlobalAveragePool` , `Resize` , `Upsample` |
| 卷积与矩阵运算 | `Conv2D` , `Conv2DTranspose` , `Gemm` , `MatMul` |
| 张量操作 | `Reshape` , `Flatten` , `Squeeze` , `Unsqueeze` , `Expand` , `Tile` , `Transpose` , `Concat` , `Split` , `Slice` , `Gather` , `GatherND` , `ScatterND` , `Where` , `NonZero` , `ReverseSequence` , `Size` , `Shape` |
| 逻辑比较 | `Equal` , `Greater` , `Less` , `GreaterOrEqual` , `LessOrEqual` , `logical_and` , `Xor` |
| RNN | `LSTM` , `GRU` |
| 规约操作 | `ReduceSum` , `ReduceMean` , `ReduceMax` , `ReduceMin` , `ReduceL1` , `ReduceL2` , `ReduceLogSum` , `ReduceLogSumExp` , `ReduceProd` , `ReduceSumSquare` |
| 其他 | `Clip` , `Cast` , `Celu` , `Erf` , `Pad` , `Dropout` , `DepthToSpace` , `SpaceToDepth` , `MaxRoiPool` , `ArgMin` , `ArgMax` , `Ceil` , `Floor` |

## 快速上手[](https://docs.mthreads.com#快速上手)

### 模型转换 (`mtc_tool`

)[](https://docs.mthreads.com#模型转换mtc_tool)

`mtc_tool`

是 MTNN 的核心转换工具，用于将 ONNX 模型转换为 `.mtnn`

格式。

### 步骤一：安装与准备[](https://docs.mthreads.com#步骤一安装与准备)

确保已安装 `m1000-mtc-toolkit`

deb 包。

更多安装包, 请参见[NPU SDK](https://moorethreads-ai-soc.tos-cn-beijing.volces.com/npu_sdk_release/npu_sdk_v1.5.0.tar.gz).

### 步骤二：编写配置文件 (`model.yaml`

)[](https://docs.mthreads.com#步骤二编写配置文件modelyaml)

创建一个 YAML 配置文件来指定转换参数：

`# model.yaml 示例`

Name: "mobilenet_v2"

ModelPath: "./mobilenet_v2.onnx"

algorithm: 'normal'

quant_type: 'uint8'

quantizer: 'asymmetric_affine'

hybrid: false

static_quantization: false

force_fp32input_list: "false"

force_fp32output_list: "true"

perf_collect_enable: true

UseSingleCore: 1




### 步骤三：执行转换[](https://docs.mthreads.com#步骤三执行转换)

`mtc --config ./model.yaml`



成功后，将在指定目录生成 `mobilenet_v2.mtnn`

文件。

### 步骤四：高级工具 (`mtc_wrap`

)[](https://docs.mthreads.com#步骤四高级工具mtc_wrap)

`mtc_wrap`

是一个 Python 脚本，可自动化生成多种量化策略（如 int8, int16）的配置文件，批量调用 `mtc`

进行转换，并汇总结果到 CSV 报告中，极大简化模型选型过程：

`# 示例：为 mobilenet_v2 生成多种量化模型`

mtc_wrap --model_path=./mobilenet_v2.onnx --output_path=./output



更多关于 int6/int16 的 yaml 文件, 请参考 [M1000 NPU Model Zoo](https://gitee.com/MooreThreads-AI-SOC/m1000_npu_model_zoo)。

## Runtime API[](https://docs.mthreads.com#runtimeapi)

### C 应用[](https://docs.mthreads.com#c应用)

以下是使用 MTNN C API 进行推理的完整示例。

#### 1. 引用头文件[](https://docs.mthreads.com#1引用头文件)

`#include "mtnn_api.h"`



#### 2. 完整示例代码[](https://docs.mthreads.com#2完整示例代码)

`#include <stdio.h>`

#include <stdlib.h>

#include <string.h>

#include <errno.h>

#include "mtnn_api.h"


// 错误处理宏

#define ONERROR(status, msg) \

do { \

if ((status) != MTNN_SUCC) { \

printf("Error: %s (code: %d)\n", msg, status); \

goto error_exit; \

} \

} while(0)


// 从文件加载模型

static unsigned char* load_model(const char* filename, size_t* model_size) {

FILE* fp = fopen(filename, "rb");

if (!fp) {

printf("Open file %s failed: %s.\n", filename, strerror(errno));

return NULL;

}

fseek(fp, 0, SEEK_END);

*model_size = ftell(fp);

rewind(fp);

unsigned char* data = (unsigned char*)malloc(*model_size);

if (fread(data, 1, *model_size, fp) != *model_size) {

free(data);

data = NULL;

}

fclose(fp);

return data;

}


int main(int argc, char* argv[]) {

if (argc != 2) {

printf("Usage: %s <mtnn_model_path>\n", argv[0]);

return -1;

}


const char* mtnn_path = argv[1];

unsigned char* model_data = NULL;

size_t model_data_size = 0;

mtnn_mgr network_mgr = NULL;

mtnn_input_output_num io_num = {0};

mtnn_tensor_mem* inputs_mem = NULL;

mtnn_tensor_mem* outputs_mem = NULL;

int status = MTNN_ERR_FAIL;


// 1. 读入模型

model_data = load_model(mtnn_path, &model_data_size);

if (!model_data) {

printf("Failed to load model.\n");

return -1;

}


// 2. 初始化模型上下文

mtnn_work_mode_t work_mode = {0};

work_mode.init_flag = 0; // 可设置 MTNN_FLAG_COLLECT_PERF_MASK 等

work_mode.e_npu_mode = NPU_MODE_SEPARATE;

work_mode.n_npu_device = 0;


status = mtnn_init(&network_mgr, (void*)model_data, model_data_size, &work_mode);

ONERROR(status, "mtnn_init failed.");


// 3. 获取输入/输出数量

status = mtnn_get(network_mgr, MTNN_GET_IN_OUT_NUM, &io_num, sizeof(io_num));

ONERROR(status, "mtnn_get MTNN_GET_IN_OUT_NUM failed.");


inputs_mem = (mtnn_tensor_mem*)calloc(io_num.n_input, sizeof(mtnn_tensor_mem));

outputs_mem = (mtnn_tensor_mem*)calloc(io_num.n_output, sizeof(mtnn_tensor_mem));


// 4. 获取输入 buffer 地址

status = mtnn_inputs_get(network_mgr, io_num.n_input, inputs_mem);

ONERROR(status, "mtnn_inputs_get failed.");


// 5. 填充输入数据 (此处省略具体数据加载逻辑)

// for (int i = 0; i < io_num.n_input; i++) {

// // load_file(input_name[i], inputs_mem[i].logical_addr);

// }


// 6. 设置输入 (使填充的数据生效)

status = mtnn_inputs_set(network_mgr, io_num.n_input, NULL);

ONERROR(status, "mtnn_inputs_set failed.");


// 7. 执行推理

status = mtnn_inference(network_mgr, NULL);

ONERROR(status, "mtnn_inference failed.");


// 8. 获取输出结果

status = mtnn_outputs_get(network_mgr, io_num.n_output, outputs_mem);

ONERROR(status, "mtnn_outputs_get failed.");


printf("Inference completed successfully!\n");


// ... 在此处处理 outputs_mem 中的结果 ...


error_exit:

if (inputs_mem) free(inputs_mem);

if (outputs_mem) free(outputs_mem);

if (network_mgr) mtnn_destroy(network_mgr);

if (model_data) free(model_data);

return (status == MTNN_SUCC) ? 0 : -1;

}



#### 3. 编译与链接[](https://docs.mthreads.com#3编译与链接)

确保链接 `libmtnnrt.so`

库：

`gcc -o mtnn_demo demo.c -lmtnnrt`




## 主要 API [](https://docs.mthreads.com#主要api)

| API | 功能 |
|---|---|
`mtnn_init` | 初始化上下文并加载 `.mtnn` 模型。 |
`mtnn_get` | 查询模型信息（如输入/输出数量、属性、性能详情、SDK版本等）。 |
`mtnn_inputs_get` | 获取模型输入张量的内存地址 (`logical_addr` )。 |
`mtnn_inputs_set` | 提交输入数据，通知运行时准备就绪。 |
`mtnn_inference` | 执行模型推理。 |
`mtnn_outputs_get` | 获取模型输出张量的内存地址。 |
`mtnn_destroy` | 卸载模型并销毁上下文。 |

### 关键结构体[](https://docs.mthreads.com#关键结构体)

-
`mtnn_work_mode_t`

: 初始化时用于配置 NPU 模式（分离/合并）、设备 ID 等。 -
`mtnn_tensor_mem`

: 描述张量的内存信息，包含虚拟地址 (`logical_addr`

)、物理地址、大小等。 -
`mtnn_tensor_attr`

: 描述张量的属性，如维度、数据类型 (`float32`

,`int8`

等)、量化类型等。

### 初始化标��志 (`init_flag`

)[](https://docs.mthreads.com#初始化标志init_flag)

-
`MTNN_FLAG_COLLECT_PERF_MASK`

: 启用性能收集，可通过`mtnn_get`

查询详细性能报告。 -
`MTNN_FLAG_DUMP_LAYER_DATA_MASK`

: 启用逐层数据 dump，用于调试。 -
`MTNN_FLAG_ASYNC_MASK`

: 启用异步模式，提高单线程帧率。

## 高级功能[](https://docs.mthreads.com#高级功能)

### 混合量化[](https://docs.mthreads.com#混合量化)

当全量化导致精度损失过大时，可使用混合量化，对网络中敏感的层保留更高精度。

-
**自动混合量化**: 在 YAML 配置中设置`rebuild: true`

,`compute_entropy: true`

,`hybrid: true`

。工具会自动分析各层熵值，并生成`entropy.txt`

报告。 -
**手动混合量化**: 根据`entropy.txt`

报告，在`.quantize`

配置文件中指定特定层的量化策略（如`dynamic_fixed_point-i16`

），并在 YAML 中通过`quantize_file`

引用该文件。

### 模型可视化[](https://docs.mthreads.com#模型可视化)

`mtc_tool`

生成的中间 IR 文件（`.mtnnir`

）可以使用定制版 **Netron** 打开，方便开发者可视化模型结构。

### 模型性能分析[](https://docs.mthreads.com#模型性能分析)

`mtc_tool`

在转换后会进行软件仿真推理，并生成详细的性能分析报告（Excel 格式），包含每层的带宽、MAC 利用率、理论 FPS 等，用于指导模型和应用优化。

**报告路径**:`${MTC_TOOL_INSTALL_DIR}/result/nets_mtc/excel/onnx/perf_result/`


## 性能基准 (MLPerf Inference v4.0)[](https://docs.mthreads.com#性能基准mlperfinferencev40)

MTNN 在 M1000 NPU 上的 MLPerf 测试结果如下（精度均 >99% 基准值）：

| Model | M1000 NPU (Single Core) - Single Stream Latency (ms) | M1000 NPU (Single Core) - Offline (Samples/s) |
|---|---|---|
ResNet-50 (Image Classification) | 2.09 | 486.051 |
Retinanet (Object Detection) | 728.896 | 1.37 |
3D-Unet (Medical Imaging) | 77480.6 | 0.025 |
RNN-T (Speech-to-text) | 531.715 | 3.34989 |
BERT (Natural Language Processing) | 569.707 | 1.75485 |

## 相关文档[](https://docs.mthreads.com#相关文档)

## 版本信息[](https://docs.mthreads.com#版本信息)

版本号 | 修改日期 | 修改说明 |
|---|---|---|
| V1.3 | 2025/04/16 | 1. 支持 ONNX Static Quantization 模型。 2. 支持 `Float32` 类型的输入输出。 |
| V1.2 | 2025/03/27 | 1. 完善混合量化操作的描述。 |
| V1.1 | 2025/02/28 | 1. 增加 `mtc` 扩展工具 `mtc_wrap` 的使用介绍。 |
| V1.0 | 2025/01/15 | 1. 优化 `mtnnrt` API 描述格式。2. 完善 `mtc_tool` 工具使用描述。3. 增加 NPU MLPerf 相关描述。 |
| V0.9 | 2024/10/11 | 1. 增加支持算子列表。 2. 调整 `mtnnrt` API 描述，并增加示例。 |
| V0.5 | 2024/06/09 | InitVersion |

## 结语[](https://docs.mthreads.com#结语)

MTNN 作为 M1000 SoC 软件栈的核心 AI 组件，为开发者提供了从云端训练模型到端侧高效部署的完整解决方案。通过其强大的模型转换能力和高度优化的运行时库，MTNN 能够充分释放 M1000 NPU 的潜能，赋能千行百业的智能边缘应用。

我们诚邀开发者社区积极参与反馈与贡献！