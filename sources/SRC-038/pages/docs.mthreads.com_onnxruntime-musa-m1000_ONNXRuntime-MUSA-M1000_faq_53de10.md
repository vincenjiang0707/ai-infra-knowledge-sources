source: https://docs.mthreads.com/onnxruntime-musa-m1000/ONNXRuntime-MUSA-M1000/faq

# 常见问�题（FAQ）

## 安装与导入[](https://docs.mthreads.com#安装与导入)

`pip install`

报安装包与平台不兼容[](https://docs.mthreads.com#pip-install-报安装包与平台不兼容)

`ERROR: onnxruntime_musa-...-cp310-cp310-linux_aarch64.whl is not a supported wheel on this platform.`



安装包为 cp310 + aarch64，Python 版本或架构不匹配时报此错。核对两项：

`python3 --version # 应为 Python 3.10.x`

uname -m # 应为 aarch64



`import onnxruntime`

报 `GLIBCXX`

或 `GLIBC`

符号缺失[](https://docs.mthreads.com#import-onnxruntime-报-glibcxx-或-glibc-符号缺失)

`ImportError: /usr/lib/aarch64-linux-gnu/libstdc++.so.6: version `GLIBCXX_3.4.30' not found`



`ImportError: /usr/lib/aarch64-linux-gnu/libc.so.6: version `GLIBC_2.34' not found`



设备的 C++ / C 运行时版本低于安装包的构建环境，与 MUSA 无关。安装包面向 Ubuntu 22.04，在更低版本的��发行版上会出现此类报错。

处理方式：在 Ubuntu 22.04 环境中运行，或升级系统的 `libstdc++6`

。可先确认当前系统提供的版本：

`strings /usr/lib/aarch64-linux-gnu/libstdc++.so.6 | grep -c GLIBCXX_3.4.30`



输出为 `1`

表示该符号存在，为 `0`

表示不存在。

`ModuleNotFoundError: No module named 'onnxruntime.capi'`

[](https://docs.mthreads.com#modulenotfounderror-no-module-named-onnxruntimecapi)

在包含 `onnxruntime`

同名目录的路径下执行 Python 导致导入路径冲突。切换到其他目录后重试：

`cd /tmp`

python3 -c "import onnxruntime as ort; print(ort.__version__)"



### 版本号不是 `1.23.0+musa.04f2c3f1`

[](https://docs.mthreads.com#版本号不是-1230musa04f2c3f1)

环境中存在其他 ONNX Runtime 版本并被优先加载，常见于用户目录（user-site）中安装过其他版本。该情况不产生任何报错，但实际运行的是另一个引擎。

`cd /tmp`

python3 -c "import onnxruntime as ort; print(ort.__version__); print(ort.__file__)"



`__file__`

若落在 `~/.local/lib/python3.10/site-packages/`

下即可确认。处理方式见[安装与验证](https://docs.mthreads.com/onnxruntime-musa-m1000/ONNXRuntime-MUSA-M1000/installation)。

## 设备与运行环境[](https://docs.mthreads.com#设备与运行环境)

`MUSAExecutionProvider`

不在 providers 列表中[](https://docs.mthreads.com#musaexecutionprovider-不在-providers-列表中)

按顺序确认三项：

`mthreads-smi # GPU 与驱动是否就绪`

ls -l /usr/local/musa/lib/libmusart.so* # 应含 libmusart.so.5

printf 'LD_LIBRARY_PATH=%s\n' "$LD_LIBRARY_PATH"



若 `LD_LIBRARY_PATH`

为空或不含 `/usr/local/musa/lib`

，显式导出后重试：

`export LD_LIBRARY_PATH=/usr/local/musa/lib:$LD_LIBRARY_PATH`



判断 MUSA SDK 版本请勿使用 `dpkg`

或 `ldconfig -p`

，原因见[环境准备与部署](https://docs.mthreads.com/onnxruntime-musa-m1000/ONNXRuntime-MUSA-M1000/environment_setup)。

`libmusart.so.4: cannot open shared object file`

[](https://docs.mthreads.com#libmusartso4-cannot-open-shared-object-file)

设备的 MUSA SDK 为 4.1.2（`libmusart.so.4`

），而本安装包链接 `libmusart.so.5`

（SDK 5.1.0）。

两者的 wheel 文件名完全相同，只能通过下载路径区分。请改用 MUSA SDK 4.1.2 环境对应的安装包，或将设备的 MUSA SDK 升�级至 5.1.0。

`initialization error`

或 `CreatePlatform failed!`

[](https://docs.mthreads.com#initialization-error-或-createplatform-failed)

当前用户没有 GPU 设备节点的访问权限。通过 SSH 登录且桌面未解锁时，该问题会概率性出现。

`sudo usermod -aG render,video $USER`



执行后重新登录或重启设备，再次验证。

## 推理过程[](https://docs.mthreads.com#推理过程)

### 模型输出全零或数值异常，但没有任何报错[](https://docs.mthreads.com#模型输出全零或数值异常但没有任何报错)

按[模型集成](https://docs.mthreads.com/onnxruntime-musa-m1000/ONNXRuntime-MUSA-M1000/model_integration)的精度验证方法，对同一模型、同一输入分别使用 `CPUExecutionProvider`

与 `MUSAExecutionProvider`

执行并对比输出。

若验证不通过，请按本页末尾的方式采集信息并联系摩尔线程技术支持，同时提供模型输入输出的 name、shape、dtype。

`providers`

中有 MUSA，但推理速度接近 CPU[](https://docs.mthreads.com#providers-中有-musa但推理速度接近-cpu)

Execution Provider 已加载，但模型中部分节点由引擎改用 CPU 执行。按[模型集成](https://docs.mthreads.com/onnxruntime-musa-m1000/ONNXRuntime-MUSA-M1000/model_integration)中禁用 CPU 回退的方法定位无法在 GPU 上执行的节点。

### 刷屏出现 `muDNN ... ERROR# NOT_SUPPORTED in Convolution::RunBwdData`

[](https://docs.mthreads.com#刷屏出现-mudnn--error-not_supported-in-convolutionrunbwddata)

`muDNN(...) ERROR# NOT_SUPPORTED in Convolution::RunBwdData, Reason:`

Unsupported Convolution configs for algorithm GEMM



含 ConvTranspose（反卷积、上采样）的模型会出现该日志。这是底层库对该配置的某一算法不支持、随即改用其他算法的提示，推理照常完成且输出正确。`ERROR#`

是日志级别标签，不表示推理失败。

可通过环境变量降低日志级别以消除刷屏：

`export MUDNN_LOG_LEVEL=FATAL`



若推理确实中断并报 `Non-zero status code returned while running ConvTranspose node ... status: 4`

，则属另一类问题，请联系摩尔线程技术支持。

### 销毁 session 后新建的 session 报 `invalid resource handle`

[](https://docs.mthreads.com#销毁-session-后新建的-session-报-invalid-resource-handle)

`musa runtime failed ... err 400 = invalid resource handle`



在同一进程内销毁一个 `InferenceSession`

后再新建，新建的 session 执行时可能报此错。第一个 session 本身工作正常，数值结果也正确。

规避方式：同一进程内的多个 session 同时持有、不销毁；或将不同模型的推理放在不同进程中。

## 技术支持[](https://docs.mthreads.com#技术支持)

反馈问题时请提供以下信息：

`mthreads-smi`

cat /etc/os-release

ls -l /usr/local/musa

head -20 /usr/local/musa/version.json

ls -l /usr/local/musa/lib/libmusart.so*

python3 --version; uname -m

printf 'LD_LIBRARY_PATH=%s\n' "$LD_LIBRARY_PATH"


cd /tmp && python3 -c "import onnxruntime as o; print(o.__version__); print(o.__file__); print(o.get_available_providers())"



以及 Execution Provider 的依赖解析情况：

`cd /tmp`

ORT_MUSA_PROVIDER="$(python3 -c 'import onnxruntime, os; print(os.path.dirname(onnxruntime.__file__))')/capi/libonnxruntime_providers_musa.so"

ldd "$ORT_MUSA_PROVIDER" | grep -E "musart|mudnn|mublas|not found"



输出会列出十余行 MUSA 相关的依赖库，开头几行形如：

` libmusart.so.5 => /usr/local/musa/lib/libmusart.so.5 (0x...)`

libmudnn.so.3 => /usr/local/musa/lib/libmudnn.so.3 (0x...)

libmublas.so.1 => /usr/local/musa/lib/libmublas.so.1 (0x...)

libmudnn_xmma.so => /usr/local/musa/lib/libmudnn_xmma.so (0x...)

libmudnn_ops.so => /usr/local/musa/lib/libmudnn_ops.so (0x...)



**注意**：行数与具体条目�随 MUSA SDK 版本不同，无需逐行核对。判断依据是**输出中不出现 not found**，且各库均解析到

`/usr/local/musa/lib`

下。另请一并提供：设备型号、完整的安装与运行输出、ONNX 模型输入输出的 name、shape 与 dtype。