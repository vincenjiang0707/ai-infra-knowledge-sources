source: https://docs.mthreads.com/aibook/m1000-doc-online/ai_development

# AI 开发工具

MTT AIBOOK 是一款面向 AI 开发者的算力本，AI 开发能力核心体现在硬件算力、系统调度、工具链集成与生态适配�的全栈整合，整体基于自研“长江”智能 SoC 芯片、MUSA 统一架构和 AIOS 操作系统实现。

这些功能使得 MTT AIBOOK 成为一个完整的 AI 开发和应用平台。

MTT AIBOOK 为您提供开箱即用的 AI 开发工具，包含 Python、Jupyter 和 VS Code。


▶Python

[Python](https://docs.python.org/3/) 因其简洁易学的语法、丰富的库和框架成为当前 AI 开发的首选语言。MTT AIBOOK 预装 Python 3.10.12，以及一系列主流 Python 框架和库，如 NumPy、pandas、Matplotlib、PyTorch、OpenCV 等，为 AI 开发者提供开箱即用的开发环境。


▶Jupyter

[Jupyter](https://jupyter.org/) 是一款开源的交互式计算环境与文档工具。Jupyter Notebook 文件使用 `.ipynb`

扩展名，以单元格（Cell）为基本单位，可混合编写代码、说明文字、公式、图片和可视化图表，实现「**代码 + 文档 + 结果**」的一体化呈现。


▶VS Code

[Visual Studio Code](https://code.visualstudio.com/docs)（简称 VS Code）是一款轻量且强大的跨平台代码编辑器，支持 Python、Java、C/C++ 等多种编程语言，具备代码编辑、语法高亮、智能提示、调试和插件扩展等功能。

### 创建 Jupyter Notebook 文件[](https://docs.mthreads.com#创建-jupyter-notebook-文件)

-
�点击

**Dock**中的 ，打开应用列表。找到**Jupyter Notebook**，然后单击。 -
依次选择

**File**>**New**>**Notebook**，创建 Notebook 文件。 -
在内核选择页面选择

**Python3（ipykernel）**。新文件默认命名为`Untitled`

，如需修改请直接重命名。

### 使用 Notebook 进行 AI 模型推理[](https://docs.mthreads.com#使用-notebook-进行-ai-模型推理)

-
在新建的 Notebook 中选择一个单元格，然后输入以下代码：

import torchimport torch_musaimport torchvision.models as models# 1. 加载模型并打印模型状态model = models.resnet50().eval()print("===== 步骤1：加载ResNet50模型 =====")print(f"模型初始设备（默认CPU）: {next(model.parameters()).device}") # 查看模型初始设备print("-" * 50)# 2. 生成随机输入张量并打印信息x = torch.rand((1, 3, 224, 224), device="musa")print("===== 步骤2：生成随机输入张量 =====")print(f"输入张量设备: {x.device}") # 验证是否在MUSA上print("-" * 50)# 3. 将模型迁移到MUSA并验证model = model.to("musa")print("===== 步骤3：模型迁移到MUSA设备 =====")print(f"模型迁移后设备: {next(model.parameters()).device}") # 验证模型是否成功到MUSAprint("-" * 50)# 4. 执行推理并打印结果信息print("===== 步骤4：执行模型推理 =====")y = model(x)print(f"输出张量设备: {y.device}") # 验证输出是否也在MUSA上print(f"输出张量前10个值（分类得分）: {y[0][:10]}") # 查看前10个分类的预测得分print(f"预测得分最高的类别索引: {torch.argmax(y).item()}") # 看随机输入的“预测类别" -
选中代码单元格，点击 ，或按

`Shift`

+`Enter`

运行代码。执行完成后，输出显示在单元格下方。

### 使用 VS Code 编写��并运行 MUSA 程序[](https://docs.mthreads.com#使用-vs-code-编写并运行-musa-程序)

-
点击 打开应用列表，找到 并单击。

-
在 VS Code 中，选择

**File**>**Open Folder**，然后选择用于保存 MUSA 源码的文件夹。 -
点击 创建文件，并将文件命名为

`musa.mu`

。 -
在

`musa.mu`

中输入以下 MUSA 示例，实现向量加法：#include <stdio.h>#include <stdlib.h>#include <math.h>#include <musa_runtime.h>#define CHECK_MUSA_ERR(err, msg) \do { \if (err != musaSuccess) { \fprintf(stderr, "%s (error code: %s)\n", msg, musaGetErrorString(err)); \exit(EXIT_FAILURE); \} \} while(0)// MUSA内核：向量加法 C = A + B__global__ void vectorAdd(const float *A, const float *B, float *C, int numElements) {int i = blockDim.x * blockIdx.x + threadIdx.x;if (i < numElements) C[i] = A[i] + B[i];}int main(void) {const int numElements = 50000;const size_t size = numElements * sizeof(float);musaError_t err;// 1. 分配主机内存并初始化float *h_A = (float *)malloc(size);float *h_B = (float *)malloc(size);float *h_C = (float *)malloc(size);if (!h_A || !h_B || !h_C) { // 合并NULL校验fprintf(stderr, "Failed to allocate host vectors!\n");exit(EXIT_FAILURE);}for (int i = 0; i < numElements; ++i) {h_A[i] = rand()/(float)RAND_MAX;h_B[i] = rand()/(float)RAND_MAX;}// 2. 分配设备内存float *d_A = NULL, *d_B = NULL, *d_C = NULL;CHECK_MUSA_ERR(musaMalloc((void**)&d_A, size), "Failed to allocate device vector A");CHECK_MUSA_ERR(musaMalloc((void**)&d_B, size), "Failed to allocate device vector B");CHECK_MUSA_ERR(musaMalloc((void**)&d_C, size), "Failed to allocate device vector C");// 3. 主机→设备拷贝数据CHECK_MUSA_ERR(musaMemcpy(d_A, h_A, size, musaMemcpyHostToDevice), "Copy A: host→device failed");CHECK_MUSA_ERR(musaMemcpy(d_B, h_B, size, musaMemcpyHostToDevice), "Copy B: host→device failed");// 4. 启动MUSA内核const int threadsPerBlock = 256;const int blocksPerGrid = (numElements + threadsPerBlock - 1) / threadsPerBlock;printf("Launch kernel: %d blocks × %d threads\n", blocksPerGrid, threadsPerBlock);vectorAdd<<<blocksPerGrid, threadsPerBlock>>>(d_A, d_B, d_C, numElements);CHECK_MUSA_ERR(musaGetLastError(), "Kernel launch failed");// 5. 设备→主机拷贝结果CHECK_MUSA_ERR(musaMemcpy(h_C, d_C, size, musaMemcpyDeviceToHost), "Copy C: device→host failed");// 6. 验证计算结果for (int i = 0; i < numElements; ++i) {if (fabs(h_A[i] + h_B[i] - h_C[i]) > 1e-5) {fprintf(stderr, "Verification failed at element %d!\n", i);exit(EXIT_FAILURE);}}printf("Test PASSED\n");// 7. 释放内存（设备 + 主机）musaFree(d_A); musaFree(d_B); musaFree(d_C);free(h_A); free(h_B); free(h_C);printf("Done\n");return 0;} -
保存

`musa.mu`

，然后打开**Terminal**。如果菜单栏未显示**Terminal**，点击 展开菜单后再选择**Terminal**。 -
在下方的 Terminal 窗口中，输入命令：

`mcc musa.mu -o musa -lmusart`

，对刚刚编写的`musa`

源码进行编译。 -
编译完成后，在终端中执行

`./musa`

运行程序。确认输出包含`Test PASSED`

和`Done`

。