source: https://docs.mthreads.com/onnxruntime-musa-m1000/ONNXRuntime-MUSA-M1000/installation

# 安装与验证

本章完成安装包的下载校验、安装与安装后验证。开始前请先完成[环境准备与部署](https://docs.mthreads.com/onnxruntime-musa-m1000/ONNXRuntime-MUSA-M1000/environment_setup)。

## 安装包[](https://docs.mthreads.com#安装包)

| 项目 | 值 |
|---|---|
| 文件名 | `onnxruntime_musa-1.23.0+musa.04f2c3f1-cp310-cp310-linux_aarch64.whl` |
| 下载地址 | `https://mt-vaas-web.tos-cn-beijing.volces.com/release/ort_musa/OrtMusaV0.27.7_M1000/M1000-SDK5.1.0/onnxruntime_musa-1.23.0+musa.04f2c3f1-cp310-cp310-linux_aarch64.whl` |
| SHA256 | `aa03a06fe6a44cbfbc73e096ffa48d615e5129eb0b743cc4200e51d61d74f9c3` |

## Step1 下载并校验[](https://docs.mthreads.com#step1-下载并校验)

`wget https://mt-vaas-web.tos-cn-beijing.volces.com/release/ort_musa/OrtMusaV0.27.7_M1000/M1000-SDK5.1.0/onnxruntime_musa-1.23.0+musa.04f2c3f1-cp310-cp310-linux_aarch64.whl`


echo "aa03a06fe6a44cbfbc73e096ffa48d615e5129eb0b743cc4200e51d61d74f9c3 onnxruntime_musa-1.23.0+musa.04f2c3f1-cp310-cp310-linux_aarch64.whl" | LC_ALL=C sha256sum -c -



预期输出：

`onnxruntime_musa-1.23.0+musa.04f2c3f1-cp310-cp310-linux_aarch64.whl: OK`



**注意**：输出为 `OK`

才继续。不是 `OK`

则文件不完整，重新下载，不要继续安装。

命令中的

`LC_ALL=C`

用于固定输出语言。中文环境下`sha256sum`

会将`OK`

显示为`成功`

，加上该前缀可保证输出与上文逐字一致。

## Step2 安装[](https://docs.mthreads.com#step2-安装)

安装前先清除环境中可能存在的其他 ONNX Runtime 版本，避免同时存在多�个版本导致加载到非预期的引擎：

`pip uninstall -y onnxruntime onnxruntime-gpu onnxruntime-musa`

pip install onnxruntime_musa-1.23.0+musa.04f2c3f1-cp310-cp310-linux_aarch64.whl



预期输出末行以 `Successfully installed`

开头，其中包含：

`onnxruntime-musa-1.23.0+musa.04f2c3f1`



**注意**：末行需包含 `onnxruntime-musa-1.23.0+musa.04f2c3f1`

，且命令退出码为 0。若显示其他版本号，说明安装的不是本安装包。同一行中还会列出本次一并安装的依赖包（`numpy`

、`protobuf`

等），其数量与顺序随环境和 pip 版本变化，无需核对。

设备可访问外网时，也可跳过 Step1 直接从下载地址安装：

`pip install https://mt-vaas-web.tos-cn-beijing.volces.com/release/ort_musa/OrtMusaV0.27.7_M1000/M1000-SDK5.1.0/onnxruntime_musa-1.23.0+musa.04f2c3f1-cp310-cp310-linux_aarch64.whl`



## Step3 验证安装[](https://docs.mthreads.com#step3-验证安装)

从 `/tmp`

目录执行，避免在包含 `onnxruntime`

同名目录的路径下产生导入冲突：

`cd /tmp`

python3 -c "

import onnxruntime as ort

print('version :', ort.__version__)

print('loaded :', ort.__file__)

print('providers:', ort.get_available_providers())

"



预期输出：

`version : 1.23.0+musa.04f2c3f1`

loaded : <当前 Python 环境>/site-packages/onnxruntime/__init__.py

providers: ['MUSAExecutionProvider', 'CPUExecutionProvider']



**注意**：三行需同时满足——`version`

为 `1.23.0+musa.04f2c3f1`

；`loaded`

指向当前 Python 环境的 `site-packages`

；`providers`

中含 `MUSAExecutionProvider`

。

** loaded 这一行必须核对。** 若该路径落在

`~/.local/lib/python3.10/site-packages/`

下，说明用户目录中存在另一个 ONNX Runtime 版本并被优先加载，此时 `version`

也会显示其他版本号。这种情况不产生任何报错，但实际运行的是另一个引擎。处理方式：使用独立的 venv，或以 `pip install --target <目录>`

安装到独立目录后通过 `PYTHONPATH`

指向该目录。临时确认可加 `PYTHONNOUSERSITE=1`

重跑上述命令。

`providers`

中含 `MUSAExecutionProvider`

表示 Execution Provider 已加载，不代表模型的全部节点都会在 GPU 上执行。确认节点分布的方法见[模型集成](https://docs.mthreads.com/onnxruntime-musa-m1000/ONNXRuntime-MUSA-M1000/model_integration)。

## 离线安装[](https://docs.mthreads.com#离线安装)

设备无外网时，安装包自身的依赖（`numpy`

、`protobuf`

、`flatbuffers`

、`sympy`

、`coloredlogs`

、`packaging`

、`humanfriendly`

、`mpmath`

等）也需一并准备，仅拷贝一个 wheel 文件无法完成安装。按设备情况选择以下一种方式。

### 方式一：设备已具备依赖[](https://docs.mthreads.com#方式一设备已具备依赖)

若设备的 Python 3.10 环境中已安装 `numpy`

等依赖（已部署 PyTorch 或 ONNX 相关工程的环境通常满足），拷入 wheel 后�跳过依赖解析安装：

`pip install --no-deps onnxruntime_musa-1.23.0+musa.04f2c3f1-cp310-cp310-linux_aarch64.whl`



### 方式二：设备为纯净环境[](https://docs.mthreads.com#方式二设备为纯净环境)

在架构相同（aarch64）、Python 版本相同（3.10）的联网设备上打包完整依赖：

`pip download https://mt-vaas-web.tos-cn-beijing.volces.com/release/ort_musa/OrtMusaV0.27.7_M1000/M1000-SDK5.1.0/onnxruntime_musa-1.23.0+musa.04f2c3f1-cp310-cp310-linux_aarch64.whl -d wheelhouse/`



将整个 `wheelhouse/`

目录拷贝到目标设备后安装：

`pip install --no-index --find-links wheelhouse/ 'onnxruntime-musa==1.23.0+musa.04f2c3f1'`



**此处按包名安装，不能写成 wheel 文件名。**

`--find-links`

只指定查找依赖的位置。若位置参数写成文件名，pip 会将其视为当前目录下的文件路径；而按上述步骤只拷贝了 `wheelhouse/`

目录，当前目录并无该文件，安装会以 `[Errno 2] No such file or directory`

失败。

如需使用文件路径，须写完整路径 `wheelhouse/onnxruntime_musa-1.23.0+musa.04f2c3f1-cp310-cp310-linux_aarch64.whl`

。

离线安装完成后，同样按 Step3 验证。

安装验证通过后，继续[快速开始](https://docs.mthreads.com/onnxruntime-musa-m1000/ONNXRuntime-MUSA-M1000/quick_start)。