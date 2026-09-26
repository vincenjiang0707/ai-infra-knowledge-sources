source: https://docs.mthreads.com/onnxruntime-musa-m1000/ONNXRuntime-MUSA-M1000/environment_setup

# 环境准�备与部署

本指南适用于摩尔线程 MTT M1000（aarch64）设备，且设备上已安装 **MUSA SDK 5.1.0**。

ONNXRuntime-MUSA-M1000 提供 Python wheel 与 C++ 预编译运行库两种形式，在 M1000 上采用 host 直接部署，无需 Docker。安装前需确认设备满足下表要求，并按后续步骤完成环境自检。

## 环境要求[](https://docs.mthreads.com#环境要求)

| 项目 | 要求 |
|---|---|
| GPU | 摩尔线程 MTT M1000 |
| 架构 | aarch64 |
| 操作系统 | Ubuntu 22.04 |
| MUSA SDK | 5.1.0（运行时 `libmusart.so.5` ） |
| Python | 3.10（安装包为 cp310，须精确匹配）。仅 Python 路线需要 |
| 权限 | 需要 root 或 sudo 权限，用于安装设备上可能缺失的 `pip` 与 `venv` 组件（见 Step6）。仅 Python 路线需要 |

**注意**：Step1 至 Step4、以及后文的[版本判定说明](https://docs.mthreads.com#%E7%89%88%E6%9C%AC%E5%88%A4%E5%AE%9A%E8%AF%B4%E6%98%8E)与[运行库路径](https://docs.mthreads.com#%E8%BF%90%E8%A1%8C%E5%BA%93%E8%B7%AF%E5%BE%84)对 Python 与 C++ 两条路线都适用。Step5、Step6 与[Python 环境](https://docs.mthreads.com#python-%E7%8E%AF%E5%A2%83)仅 Python 路线需要，C++ 路线可跳过，其编译工具链要求见 [C++ 集成](https://docs.mthreads.com/onnxruntime-musa-m1000/ONNXRuntime-MUSA-M1000/cpp_integration)。

## Step1 确认 GPU 与驱动[](https://docs.mthreads.com#step1-确认-gpu-与驱动)

`mthreads-smi`



**注意**：能够列出 M1000 设备信息即表示驱动就绪。该命令报错或找不到设备时，请先完成 MUSA 驱动的安装，不要继续后续步骤。

## Step2 确认 MUSA SDK 版本[](https://docs.mthreads.com#step2-确认-musa-sdk-版本)

`readlink /usr/local/musa`



预期输出：

`musa-5.1.0`



**注意**：输出为 `musa-5.1.0`

才适用本安装包。为其他版本（例如 `musa-4.1.2`

）时请改用对应 MUSA SDK 版本的安装包。

## Step3 确认 toolkit 版本号[](https://docs.mthreads.com#step3-确认-toolkit-版本号)

`grep -m1 -A1 musa_toolkits /usr/local/musa/version.json`



预期输出：

` "musa_toolkits": {`

"version": "5.1.0",



**注意**：`version`

字段为 `5.1.0`

。该字段是 MUSA toolkit 版本号的权威来源。

## Step4 确认 MUSA 运行时库[](https://docs.mthreads.com#step4-确认-musa-运行时库)

`ls -l /usr/local/musa/lib/libmusart.so*`



预期输出中应包含以下三项（`ls -l`

的权限、大小与日期列随环境不同，无需核对）：

`/usr/local/musa/lib/libmusart.so -> libmusart.so.5`

/usr/local/musa/lib/libmusart.so.5 -> libmusart.so.5.1.0

/usr/local/musa/lib/libmusart.so.5.1.0



**注意**：输出中含 `libmusart.so.5`

才可继续。设备上只有 `libmusart.so.4`

时，本安装包无法加载，须改用 MUSA SDK 4.1.2 环境的对应安装包。

## Step5 确认 Python 版本[](https://docs.mthreads.com#step5-确认-python-版本)

`python3 --version`



预期输出：

`Python 3.10.x`



**注意**：版本号须为 `3.10.x`

。本安装包为 cp310，在其他 Python 版本上无法安装。

## Step6 确认 pip 与 venv 可用[](https://docs.mthreads.com#step6-确认-pip-与-venv-可用)

`python3 -m pip --version`

python3 -m venv /tmp/_venv_probe && rm -rf /tmp/_venv_probe && echo "venv OK"



预期输出：

`pip <版本> from <路径> (python 3.10)`

venv OK



部分设备的系统镜像不包含 `pip`

与 `venv`

组件。此时第一条报 `No module named pip`

，第二条报 `ensurepip is not available`

并提示安装 `python3.10-venv`

。安装后重试（需 root 权限）：

`sudo apt-get update`

sudo apt-get install -y python3-pip python3.10-venv



**注意**：两条命令都要有正常输出才继续，后续章节的安装步骤依赖 `pip`

。第二条**实际创建并删除了一个临时虚拟环境**——`python3 -m venv --help`

能正常打印帮助信息，并不代表可以真正创建虚拟环境，不能用它替代本步。

## 版本判定说明[](https://docs.mthreads.com#版本判定说明)

**MUSA SDK 版本判定，以 Step2 的符号链接与 Step3 的 version.json 为准。**

以下两个命令常被用于判断 MUSA 版本，但结论均不可靠：

：显示的是 BSP 元包的版本号，与 toolkit、runtime 的版本号不是同一个编号体系，两者出现差异属于正常现象，不能据此判断 toolkit 版本。`dpkg -s musa`

/`dpkg -l | grep musa`

：结果取决于设备是否将`ldconfig -p | grep libmusart`

`/usr/local/musa/lib`

写入了 ldconfig 配置。有输出与无输出都可能是正常的，不能据此判断库缺失或版本。

## 运行库路径[](https://docs.mthreads.com#运行库路径)

MUSA 运行库通过 `LD_LIBRARY_PATH`

定位。交互式登录 shell 通常已在 profile 中完成设置，可通过以下命令确认：

`printf 'LD_LIBRARY_PATH=%s\n' "$LD_LIBRARY_PATH"`



输出中应包含 `/usr/local/musa/lib`

。

通过**脚本、cron 或非交互式 SSH**（形如 `ssh host "命令"`

）运行推理程序时，`LD_LIBRARY_PATH`

可能为空，会导致 Execution Provider 加载失败，或推理改由 CPU 执行而不产生任何报错。这类场景请在程序启动前显式导出：

`export LD_LIBRARY_PATH=/usr/local/musa/lib:$LD_LIBRARY_PATH`



## Python 环境[](https://docs.mthreads.com#python-环境)

建议在独立的 Python 3.10 环境中安装本安装包，避免与系统环境或其他项目的依赖冲突，也避免出现多个 ONNX Runtime 版本共存。

`python3 -m venv ~/ort-musa-venv`

source ~/ort-musa-venv/bin/activate



若该命令因缺少 `python3.10-venv`

而失败，安装后重试：

`sudo apt-get install -y python3.10-venv`



环境确认完成后，继续[安装与验证](https://docs.mthreads.com/onnxruntime-musa-m1000/ONNXRuntime-MUSA-M1000/installation)。