source: https://docs.mthreads.com/onnxruntime-musa-m1000/ONNXRuntime-MUSA-M1000/

# 端侧 ONNXRuntime-MUSA-M1000

ONNXRuntime-MUSA-M1000 是 ONNX Runtime 的硬件后端适配，使得 ONNX Runtime 可以在摩尔线�程 GPU 上运行 ONNX 模型的推理任务。ONNXRuntime-MUSA-M1000 以 Execution Provider 的形式接入 MUSA 计算能力，将摩尔线程 GPU 的算子实现、显存管理和运行时调度与 ONNX Runtime 主框架解耦集成。

对外接口与 ONNX Runtime 上游 release 保持兼容，差异仅在于新增了 `MUSAExecutionProvider`

。已有的 ONNX Runtime Python 工程接入时，通常只需在构造 `InferenceSession`

时把 `MUSAExecutionProvider`

加入 providers 列表，模型本身无需修改。

本文档面向在摩尔线程 MTT M1000（aarch64）上集成 ONNXRuntime-MUSA-M1000、部署自研 ONNX 模型的场景。M1000 为端侧平台，采用 host 直接部署，无需 Docker。

提供 **Python** 与 **C++** 两条接入路线，两者共用同一套环境要求：Python 路线通过 pip 安装 wheel，见[安装与验证](https://docs.mthreads.com/onnxruntime-musa-m1000/ONNXRuntime-MUSA-M1000/installation)；C++ 路线通过 CMake 链接预编译运行库，见 [C++ 集成](https://docs.mthreads.com/onnxruntime-musa-m1000/ONNXRuntime-MUSA-M1000/cpp_integration)。

## 版本信息[](https://docs.mthreads.com#版本信息)

| 项目 | 版本 |
|---|---|
| ONNXRuntime-MUSA-M1000 版本 | OrtMusaV0.27.7_M1000 |
| ONNX Runtime | 1.23.0（版本串 `1.23.0+musa.04f2c3f1` ） |
| 目标平台 | 摩尔线程 MTT M1000（aarch64） |
| MUSA SDK | 5.1.0（运行时 `libmusart.so.5` ） |
| Python | 3.10（wheel 为 cp310，须精确匹配） |
| C++ | C++17，cmake ≥ 3.22、gcc ≥ 9.4 |
| 部署方式 | host 直接部署，无需 Docker |
| 发布时间 | 2026.09.04 |

Python wheel 文件名为 `onnxruntime_musa-1.23.0+musa.04f2c3f1-cp310-cp310-linux_aarch64.whl`

，文件名内含构建标识 `04f2c3f1`

；安装后 `onnxruntime.__version__`

返回完整版本串 `1.23.0+musa.04f2c3f1`

，可据此核对版本。

C++ 运行库文件名为 `onnxruntime-linux-aarch64-1.23.0-release.tgz`

，包含 `include/`

与 `lib/`

。C++ 运行时的 `Ort::GetVersionString()`

只返回 `1.23.0`

、不含构建标识，版本以下载地址的路径段为准，详见 [C++ 集成](https://docs.mthreads.com/onnxruntime-musa-m1000/ONNXRuntime-MUSA-M1000/cpp_integration)。

设备批量部署可改用 deb 安装包 `onnxruntime-musa_1.23.0+musa.04f2c3f1_arm64.deb`

，将同一份 C++ 运行库安装到系统目录，见 [C++ 集成](https://docs.mthreads.com/onnxruntime-musa-m1000/ONNXRuntime-MUSA-M1000/cpp_integration)。该安装包不含 Python 支持。

## 文档目录[](https://docs.mthreads.com#文档目录)

更多 ONNXRuntime-MUSA-M1000 版本变更说明，请查看 [ONNXRuntime-MUSA-M1000 版本说明](https://docs.mthreads.com/onnxruntime-musa-m1000/ONNXRuntime-MUSA-M1000/release-notes)。