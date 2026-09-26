source: https://docs.opencloudos.org/en/OC9/ai-deployment/GPU-optimization-practice/ascend-deployment/

# 基于 OpenCloudOS 的昇腾部署实践

目前， OpenCloudOS 已实现对昇腾 HDK 驱动与 CANN 的深度适配和原生支持，为使用昇腾硬件的用户提供了完整的 RPM 二进制软件包，包括内核级驱动、系统管理工具、计算库及AI框架适配组件。

本文档将指导如何在 OpenCloudOS 上快速完成昇腾 HDK 驱动与 CANN 的安装部署，并无缝运行上层AI模型与应用。

## 一、基础环境要求及说明

1、 **支持 OpenCloudOS 版本** ：OpenCloudOS 9 版本、6.6内核（含其间各小版本）。同时，在使用昇腾HDK驱动时，gcc版本建议和系统发行版保持一致，cmake版本不低于3.10。

2、 **支持的 GPU 设备** ：Atlas 800T/I A2，Atlas 200 T/I box16。

3、 **驱动软件版本** ：Ascend910B-driver-25.2.0、Ascend910B-firmware-7.7.0.6.236

4、 **环境检查** ：该部署流程中，驱动包主要以二进制形式安装，因此需严格按照第二节「前置检查」流程，匹配软硬件系统，确认CPU架构，操作系统版本是否在列表中。

## 二、前置检查

请执行以下命令确认系统环境是否符合要求：

```
# 检查CPU架构
uname -m
# 检查操作系统版本
lsb_release -a
# 检查内核版本
uname -r
# 检查是否已安装旧版驱动
yum list installed | grep Ascend
```


`yum remove Ascend*`

## 三、安装昇腾 HDK 驱动及SDK

### 3.1 安装 OpenCloudOS EPOL源

```
# 如使用 OpenCloudOS 9系统，请先安装 EPOL extras 软件源
dnf install epol-extras-release
```


### 3.2 安装昇腾 HDK 驱动包

安装驱动前，需要检查内核是否开启ko模块签名，若开启则需要关闭并重启系统：

```
# 查看当前内核是否开启签名
cat /sys/module/module/parameters/sig_enforce
# 若输出结果为Y，则需提前关闭内核ko签名（即下面操作）；
# 若输出结果为N或其他，则无需操作
vim /etc/default/grub
# 修改 `GRUB_CMDLINE_LINUX` ，使 `module.sig_enforce=0`
# 重新生成grub2配置文件
grub2-mkconfig
# 重启
reboot
```


关闭内核ko签名后，安装昇腾 HDK 驱动：

```
# 安装驱动及依赖
dnf install Ascend910B-driver-25.2.0-1 \
Ascend910B-firmware-7.7.0.6.236-1
# 安装后需重启
reboot
```


### 3.3 驱动安装验证

可通过`npu-smi info`

命令查看固件安装结果：

### 3.4 安装CANN包

```
# （最小化安装）安装CANN toolkit/kernels组件
dnf install Ascend-cann-toolkit-8.2.RC1
dnf install Ascend-cann-kernels-910b-8.2.RC1
# 使用vLLM需要nnal
dnf install Ascend-cann-nnal-8.2.RC1
# 配置常用的python库
RUN pip3 install attrs cython 'numpy>=1.19.2,<=1.24.0' decorator pillow sympy cffi pyyaml pathlib2 psutil protobuf==3.20.0 scipy requests absl-py
# 配置环境变量
echo -e '\n. /usr/local/Ascend/ascend-toolkit/set_env.sh' >> /root/.bashrc && source /root/.bashrc
# 若需安装nnal，需要增加下面配置
echo -e '\n. /usr/local/Ascend/nnal/atb/set_env.sh' >> /root/.bashrc && source /root/.bashrc
```


### 3.5 CANN 安装验证

可[参考 CANN 例程](https://gitee.com/ascend/samples/tree/master/cplusplus/level2_simple_inference/1_classification/resnet50_firstapp)实现简单的推理程序易验证 CANN 安装结果。

## 四、AI 框架安装与验证

### 4.1 运行 AI 框架及安装PyTorch框架 （以vLLM示例）

```
# 在线安装（推荐）
pip3 install vllm==0.9.1 vllm-ascend==0.9.1
wget https://gitcode.com/Ascend/pytorch/releases/download/v7.2.0-pytorch2.7.1/torch_npu-2.7.1-cp311-cp311-manylinux_2_28_`arch`.whl && \
pip3 install ./torch_npu-2.7.1-cp311-cp311*.whl
# 验证pytorch安装
python -c "import torch; print(torch.ones(2).cuda())"
# 验证vLLM安装
python -c "from vllm import LLM, SamplingParams"
```


### 4.2 运行模型（以Qwen示例）

#### 4.2.1 下载Qwen3大模型

```
# 安装 modelscope 以下载大模型
pip3 install modelscope
# 下载完整模型库
modelscope download --model Qwen/Qwen3-0.6B
```


#### 4.2.2 基于 vLLM 框架运行大模型，编辑 example.py 脚本：

```
from vllm import LLM, SamplingParams
prompts = [
"Hello, my name is",
"The president of the United States is",
"The capital of France is",
"The future of AI is",
]
# Create a sampling params object.
sampling_params = SamplingParams(temperature=0.8, top_p=0.95)
# Create an LLM.
llm = LLM(model="Qwen/Qwen3-0.6B")
# Generate texts from the prompts.
outputs = llm.generate(prompts, sampling_params)
for output in outputs:
prompt = output.prompt
generated_text = output.outputs[0].text
print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}")
```


### 4.3 运行结果展示

运行脚本，基于 vLLM 和昇腾加速卡实现QWen大模型的端侧推理部署。

## 五、手动安装指南（备用方案）

若驱动程序和 CANN 安装失败，可以从[昇腾社区开发者模块](https://www.hiascend.com/developer)下载需要的驱动程序或开发包进行安装。

### 附录一：

| 文件名 | 包名 | |
|---|---|---|
驱动HDK |
Ascend-hdk-910b-npu-driver-25.2.0-1.x86-64.rpm | Ascend910B-driver |
| Ascend-hdk-910b-npu-firmware-7.7.0.6.236-1.noarch.rpm | Ascend910B-firmware | |
CANN |
Ascend-cann-kernels-910b-8.2.RC1-linux.x86_64.rpm | Ascend-cann-kernels |
| Ascend-cann-toolkit-8.2.RC1-linux.x86_64.rpm | Ascend-cann-toolkit |