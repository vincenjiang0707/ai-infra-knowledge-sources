source: https://docs.mthreads.com/onnxruntime-musa-m1000/ONNXRuntime-MUSA-M1000/cpp_integration

# C++ 集成

本章面向在自有 C++ 工程内集成 ONNXRuntime-MUSA-M1000 的场景，适用于模型需在本地推理、不便外发的情况。

发布通道同时提供预编译的 C++ 运行库（`include/`

+ `lib/`

），通过 CMake `FetchContent`

链接。接口与 ONNX Runtime 上游 release 兼容，差异仅在于新增 `MUSAExecutionProvider`

。

开始前请先完成[环境准备与部署](https://docs.mthreads.com/onnxruntime-musa-m1000/ONNXRuntime-MUSA-M1000/environment_setup)。该章的驱动、MUSA SDK 与 `LD_LIBRARY_PATH`

要求对 C++ 路线同样适用。Python 路线见[安装与验证](https://docs.mthreads.com/onnxruntime-musa-m1000/ONNXRuntime-MUSA-M1000/installation)。

运行库有两种取用方式：本章 Step1 起为**工程内引入**（下载 tarball，由工程自己管理路径与版本）；设备批量部署可改用 **deb 安装包**安装到系统目录，见[方式二](https://docs.mthreads.com#%E6%96%B9%E5%BC%8F%E4%BA%8C%E4%BD%BF%E7%94%A8-deb-%E5%AE%89%E8%A3%85%E5%8C%85)。

## 运行库[](https://docs.mthreads.com#运行库)

| 项目 | 值 |
|---|---|
| 文件名 | `onnxruntime-linux-aarch64-1.23.0-release.tgz` |
| 下载地址 | `https://mt-vaas-web.tos-cn-beijing.volces.com/release/ort_musa/OrtMusaV0.27.7_M1000/M1000-SDK5.1.0/onnxruntime-linux-aarch64-1.23.0-release.tgz` |
| SHA256 | `7e18c1875127d520fbe2421d39b63ac5d3035b323ae12e4622e748f557cb1e71` |
| 大小 | 12,433,667 字节 |

解压后的目录结构：

`onnxruntime-linux-aarch64/`

├── include/

│ ├── onnxruntime_c_api.h

│ ├── onnxruntime_cxx_api.h

│ ├── onnxruntime_cxx_inline.h

│ ├── onnxruntime_float16.h

│ ├── onnxruntime_lite_custom_op.h

│ ├── onnxruntime_run_options_config_keys.h

│ ├── onnxruntime_session_options_config_keys.h

│ ├── provider_options.h

│ ├── musa_provider_options.h

│ └── core/providers/{resource.h, custom_op_context.h}

└── lib/

├── libonnxruntime.so → libonnxruntime.so.1 → libonnxruntime.so.1.23.0

├── libonnxruntime_providers_musa.so

├── libonnxruntime_providers_shared.so

├── cmake/onnxruntime/*.cmake

└── pkgconfig/libonnxruntime.pc



`libonnxruntime_providers_musa.so`

是 MUSA Execution Provider，在创建 session 时才被动态加载。

**C++ 运行时的 Ort::GetVersionString() 只返回 1.23.0，不含版本标识后缀。**


C++ 路线无法从二进制自证引擎版本。版本以下载地址中的路径段 `OrtMusaV0.27.7_M1000/M1000-SDK5.1.0`

与同目录 `SHA256SUMS`

内的 wheel 文件名为准。

## Step1 编译工具链[](https://docs.mthreads.com#step1-编译工具链)

| 用途 | 最低 cmake 版本 |
|---|---|
| 接入自有工程（本章 Step3 起） | 3.22，Ubuntu 22.04 的 `apt install cmake` 提供 3.22.1，满足要求 |
| 运行 Step2 的示例包 | 3.23，示例包 `CMakeLists.txt` 首行有此声明 |

另需 gcc ≥ 9.4（支持 C++17），Ubuntu 22.04 自带的 11.4.0 满足要求。

用低于 3.23 的 cmake 配置示例包会直接失败：

`CMake Error at CMakeLists.txt:1 (cmake_minimum_required):`

CMake 3.23 or higher is required. You are running version 3.22.6



安装 cmake ≥ 3.23 使用官方 aarch64 预编译包，解压即用，不需要 root 权限：

`curl -fsSLO https://cmake.org/files/v3.31/cmake-3.31.6-linux-aarch64.tar.gz`


echo "b4cc788d63112b2749b40627e719eb5d3b8ed8f00c36d77189f4019cfe64bc9e cmake-3.31.6-linux-aarch64.tar.gz" | LC_ALL=C sha256sum -c -


tar xzf cmake-3.31.6-linux-aarch64.tar.gz

export PATH="$PWD/cmake-3.31.6-linux-aarch64/bin:$PATH"

cmake --version | head -1



预期输出：

`cmake-3.31.6-linux-aarch64.tar.gz: OK`

cmake version 3.31.6



**注意**：`export PATH`

只对当前 shell 生效，新开终端需重新执行，或写入个人 shell 配置。上述 SHA256 取自官方校验清单 `https://cmake.org/files/v3.31/cmake-3.31.6-SHA-256.txt`

。

## Step2 快速验证[](https://docs.mthreads.com#step2-快速验证)

示例包包含 CMakeLists、`main.cc`

与一个通用的 mobilenet_v2 模型，用于在接入自有工程之前先验证链路。**需要 cmake ≥ 3.23**。

`curl -fsSLO https://mt-vaas-web.tos-cn-beijing.volces.com/release/ort_musa/feature-demos/cpp/ort_musa_cpp_demo.tar.gz`


echo "aa823ce86013eb60c3447b56d7e7ee33581df5cea4cedfeb47bb084152fd295f ort_musa_cpp_demo.tar.gz" | LC_ALL=C sha256sum -c -


tar xzf ort_musa_cpp_demo.tar.gz && cd ort_musa_cpp_demo

mkdir -p build && cd build


cmake -DORTMUSA_TARBALL_URL=https://mt-vaas-web.tos-cn-beijing.volces.com/release/ort_musa/OrtMusaV0.27.7_M1000/M1000-SDK5.1.0/onnxruntime-linux-aarch64-1.23.0-release.tgz \

-DORTMUSA_TARBALL_HASH=SHA256=7e18c1875127d520fbe2421d39b63ac5d3035b323ae12e4622e748f557cb1e71 ..


make -j4

export LD_LIBRARY_PATH=/usr/local/musa/lib:$LD_LIBRARY_PATH

./ort_musa_cpp_demo ../models/mobilenet_v2_fp16.onnx 0



预期输出：

`model = ../models/mobilenet_v2_fp16.onnx`

device_id = 0

providers : MUSAExecutionProvider CPUExecutionProvider

output : [1, 1000]

inference : <耗时> ms (mean of 20, after 3 warmup)

PASS: MUSA EP C++ inference completed.



**注意**：以下三项同时满足即表示链路已跑通——`providers`

中含 `MUSAExecutionProvider`

；`output`

为 `[1, 1000]`

；末行为 `PASS: MUSA EP C++ inference completed.`

。`inference`

一行随设备负载波动，仅用于说明输出格式。

**两个 -D 参数必须同时给出，且不能省略。**

示例包 `CMakeLists.txt`

内置的默认下载地址指向另一平台（x86_64）的运行库，在 M1000 上不覆盖会下载到 x86_64 包并在链接阶段失败。URL 与 SHA256 成对，只改其一会导致校验失败。

**注意**：`cmake`

配置阶段会下载并校验 12.4 MB 的运行库，耗时取决于网络，期间无进度显示。`make`

只编译一个源文件，为秒级。配置阶段出现的 `DOWNLOAD_EXTRACT_TIMESTAMP`

/ `CMP0135`

警告为 cmake 的开发者提示，不影响构建结果。

**注意**：示例包 `main.cc`

中设置了 `prefer_nhwc = 1`

。该开关的适用性见下文[性能特性开关](https://docs.mthreads.com#%E6%80%A7%E8%83%BD%E7%89%B9%E6%80%A7%E5%BC%80%E5%85%B3)。

## Step3 接入自有工程[](https://docs.mthreads.com#step3-接入自有工程)

将下列片段加入工程的 `CMakeLists.txt`

，`your_target`

替换为工程中的可执行或库 target。该片段最低要求 cmake 3.22。

`include(FetchContent)`


# 使用 CACHE STRING，以便命令行 -D 覆盖（离线编译需要）。普通 set 会覆盖 -D 传入的值。

set(ORTMUSA_TARBALL_URL "https://mt-vaas-web.tos-cn-beijing.volces.com/release/ort_musa/OrtMusaV0.27.7_M1000/M1000-SDK5.1.0/onnxruntime-linux-aarch64-1.23.0-release.tgz"

CACHE STRING "OrtMusa C++ tarball URL")

set(ORTMUSA_TARBALL_HASH "SHA256=7e18c1875127d520fbe2421d39b63ac5d3035b323ae12e4622e748f557cb1e71"

CACHE STRING "OrtMusa C++ tarball hash")


FetchContent_Declare(onnxruntime URL ${ORTMUSA_TARBALL_URL} URL_HASH ${ORTMUSA_TARBALL_HASH})

FetchContent_MakeAvailable(onnxruntime)


find_library(location_onnxruntime onnxruntime

PATHS "${onnxruntime_SOURCE_DIR}/lib" NO_CMAKE_SYSTEM_PATH REQUIRED)

add_library(onnxruntime SHARED IMPORTED)

set_target_properties(onnxruntime PROPERTIES

IMPORTED_LOCATION ${location_onnxruntime}

INTERFACE_INCLUDE_DIRECTORIES "${onnxruntime_SOURCE_DIR}/include")


target_link_libraries(your_target PRIVATE onnxruntime)


# BUILD_RPATH 使 build 目录内可直接运行；INSTALL_RPATH 使安装后仍能定位运行库

set_target_properties(your_target PROPERTIES

BUILD_RPATH "${onnxruntime_SOURCE_DIR}/lib"

INSTALL_RPATH "$ORIGIN/../lib")



安装规则，使 `INSTALL_RPATH`

的 `$ORIGIN/../lib`

生效，将引擎运行库与可执行文件一并安装：

`install(TARGETS your_target RUNTIME DESTINATION bin)`

install(DIRECTORY "${onnxruntime_SOURCE_DIR}/lib/" DESTINATION lib

FILES_MATCHING PATTERN "*.so*")



## Step4 验证部署[](https://docs.mthreads.com#step4-验证部署)

`readelf`

显示 `RUNPATH`

、`ldd`

检查主程序无缺失，都不足以说明部署成功。

MUSA Execution Provider 在创建 session 时才被动态加载，且其自身还有 MUSA SDK 的传递依赖。三项须逐一确认。

`cmake --install build --prefix "$PWD/install"`


readelf -d install/bin/your_target | grep -E "RPATH|RUNPATH"


export LD_LIBRARY_PATH=/usr/local/musa/lib:$LD_LIBRARY_PATH

ldd install/lib/libonnxruntime_providers_musa.so | grep -E "musart|mudnn|mublas|not found"



预期输出的关键行：

`0x000000000000001d (RUNPATH) Library runpath: [$ORIGIN/../lib]`

libmusart.so.5 => /usr/local/musa/lib/libmusart.so.5

libmudnn.so.3 => /usr/local/musa/lib/libmudnn.so.3

libmudnn_xmma.so => /usr/local/musa/lib/libmudnn_xmma.so

libmublas.so.1 => /usr/local/musa/lib/libmublas.so.1



**注意**：判定标准是输出中**不出现 not found**。除上述四条直接依赖外，

`ldd`

还会列出若干 `libmudnn_*.so`

子库，均应指向 `/usr/local/musa/lib`

，属正常。这些库由 MUSA SDK 提供，标准安装即包含。第三项：**从任意其他目录**（如 `cd /tmp`

）运行一次安装后的程序，确认能够创建 session 并完成推理。

两类库的定位分工：引擎自带库（`libonnxruntime.so*`

、`libonnxruntime_providers_musa.so`

、`libonnxruntime_providers_shared.so`

）由 `INSTALL_RPATH`

解决；MUSA 运行时（`libmusart`

、`libmudnn`

等）由 SDK 安装路径提供，需保证 `LD_LIBRARY_PATH`

包含 `/usr/local/musa/lib`

。

`LD_LIBRARY_PATH`

由登录环境提供。

通过脚本、cron 或非交互 SSH 执行时不会加载登录环境配置，该变量为空，程序会在创建 session 时抛出异常并中止：

`Failed to load library libonnxruntime_providers_musa.so with error:`

libmusart.so.5: cannot open shared object file: No such file or directory



这类场景请显式导出 `export LD_LIBRARY_PATH=/usr/local/musa/lib:$LD_LIBRARY_PATH`

。

## 推理代码[](https://docs.mthreads.com#推理代码)

`#include <onnxruntime_cxx_api.h>`

#include <musa_provider_options.h>


Ort::Env env(ORT_LOGGING_LEVEL_WARNING, "app");

Ort::SessionOptions so;


OrtMUSAProviderOptions musa{}; // 花括号不可省略，见下方说明

musa.device_id = 0; // M1000 为单卡设备，保持 0

so.AppendExecutionProvider_MUSA(musa);


Ort::Session session(env, "your_model.onnx", so);

// 构造输入 CPU tensor → session.Run(...) → 读取输出



完整可运行版本见 Step2 示例包的 `main.cc`

，其中包含从 session 自动查询输入输出名称与形状、构造 tensor、执行与读取输出的全过程。

**注意**：`OrtMUSAProviderOptions musa{};`

的花括号不可省略。省略后各字段为未初始化值，行为不确定；带花括号时按下表的默认值初始化。

输入输出的适配方式（多输入、fp16、动态维度、多输出）与 Python 路线同理，对应的 C++ API 为：

| 情形 | 关键 API |
|---|---|
| 多输入 | 遍历 `session.GetInputCount()` ，逐输入取 `GetInputTypeInfo(i)` 的 name、shape、dtype 各建一个 tensor，`Run` 传入名称数组与 tensor 数组 |
| fp16 输入输出 | 用 `std::vector<Ort::Float16_t>` 缓冲配合 `CreateTensor<Ort::Float16_t>()` 。不要使用 ，它创建的是 `CreateTensor<uint16_t>()` `UINT16` tensor 而非 `FLOAT16` |
| 动态维度 | 须按业务在构造输入 shape 时显式固定 batch、分辨率等维度 |
| 输出读取 | `Run` 返回的 `Ort::Value` 用 `GetTensorTypeAndShapeInfo().GetShape()` 取形状、`GetTensorData<T>()` 取数据指针，`T` 与输出 dtype 一致 |

## 性能特性开关[](https://docs.mthreads.com#性能特性开关)

C++ 接口通过 `OrtMUSAProviderOptions`

的结构体字段设置，字段含义与 Python 接口一致，取值为 `int`

而非字符串：

| 字段 | 默认值 | 对应 Python option |
|---|---|---|
`device_id` | `0` | `"device_id"` |
`prefer_nhwc` | `0` | `"prefer_nhwc"` |
`allow_tf32` | `1` | `"allow_tf32"` |
`enable_musa_graph` | `0` | `"enable_musa_graph"` |

各开关的作用、适用性与实测方式见[性能特性开关](https://docs.mthreads.com/onnxruntime-musa-m1000/ONNXRuntime-MUSA-M1000/provider_options)。该章的结论对 C++ 路线同样适用：开关效果与模型结构强相关，上线前须在自有工程内实测确认，不建议未经实测即全部启用。

** enable_musa_graph 不能在本章的写法下直接置 1。** 该开关须配合 IOBinding 使用，要求输入输出预先分配在 MUSA 设备内存上、且跨次调用地址不变；本章示例使用的是普通

`Run()`

与 host 侧输入，置 1 后推理调用会返回错误。该开关仍在持续完善中，本版建议保持默认值 `0`

；前提条件见[图捕获（MUSA Graph）](https://docs.mthreads.com/onnxruntime-musa-m1000/ONNXRuntime-MUSA-M1000/provider_options#musa-graph)。

**注意**：`allow_tf32`

默认为 `1`

，即带花括号初始化后该开关已处于开启状态。如需关闭须显式设置 `musa.allow_tf32 = 0;`

。

## 精度验证[](https://docs.mthreads.com#精度验证)

**上线前须对自研模型执行精度验证。**

�方式与判定标准同[模型集成](https://docs.mthreads.com/onnxruntime-musa-m1000/ONNXRuntime-MUSA-M1000/model_integration#%E7%B2%BE%E5%BA%A6%E9%AA%8C%E8%AF%81)：同一模型、同一输入分别以纯 CPU 与 MUSA 各建一个 session 执行一次，判定标准为余弦相似度不低于 0.999，且 MUSA 侧输出非全零。

下列 `precision_check.cc`

为 C++ 的完整实现，适用于单输入、fp32 输入输出的模型，按 Step3 的方式链接即可：

`// 用法: ./precision_check <model.onnx> [device_id]`

#include <onnxruntime_cxx_api.h>

#include <musa_provider_options.h>

#include <cmath>

#include <cstdlib>

#include <iostream>

#include <random>

#include <vector>


static std::vector<Ort::Value> Run(const char* model, bool use_musa, int device_id,

const std::vector<float>& input,

const std::vector<int64_t>& shape, Ort::Env& env) {

Ort::SessionOptions so;

if (use_musa) {

OrtMUSAProviderOptions musa{};

musa.device_id = device_id;

so.AppendExecutionProvider_MUSA(musa);

}

Ort::Session session(env, model, so);

Ort::AllocatorWithDefaultOptions alloc;

auto in_name = session.GetInputNameAllocated(0, alloc);

auto out_name = session.GetOutputNameAllocated(0, alloc);

const char* in_names[] = {in_name.get()};

const char* out_names[] = {out_name.get()};

auto mem = Ort::MemoryInfo::CreateCpu(OrtArenaAllocator, OrtMemTypeDefault);

auto tensor = Ort::Value::CreateTensor<float>(mem, const_cast<float*>(input.data()),

input.size(), shape.data(), shape.size());

return session.Run(Ort::RunOptions{nullptr}, in_names, &tensor, 1, out_names, 1);

}


int main(int argc, char** argv) {

if (argc < 2) { std::cerr << "用法: " << argv[0] << " <model.onnx> [device_id]\n"; return 2; }

const char* model = argv[1];

int device_id = argc >= 3 ? std::atoi(argv[2]) : 0;

Ort::Env env(ORT_LOGGING_LEVEL_WARNING, "precision_check");


std::vector<int64_t> shape;

{ Ort::SessionOptions so; Ort::Session s(env, model, so);

shape = s.GetInputTypeInfo(0).GetTensorTypeAndShapeInfo().GetShape();

for (auto& d : shape) if (d < 0) d = 1; } // 动态维度置 1 为占位，按业务修改

size_t n = 1; for (auto d : shape) n *= static_cast<size_t>(d);


std::vector<float> input(n);

std::mt19937 rng(42);

std::normal_distribution<float> dist(0.f, 1.f);

for (auto& v : input) v = dist(rng);


auto musa_out = Run(model, true, device_id, input, shape, env);

auto cpu_out = Run(model, false, device_id, input, shape, env);


bool ok = true;

for (size_t i = 0; i < musa_out.size(); ++i) {

size_t cnt = musa_out[i].GetTensorTypeAndShapeInfo().GetElementCount();

const float* m = musa_out[i].GetTensorData<float>();

const float* c = cpu_out[i].GetTensorData<float>();

double dot = 0, nm = 0, nc = 0; bool any = false;

for (size_t k = 0; k < cnt; ++k) {

dot += double(m[k]) * c[k]; nm += double(m[k]) * m[k]; nc += double(c[k]) * c[k];

if (m[k] != 0.f) any = true;

}

double cos = dot / (std::sqrt(nm) * std::sqrt(nc) + 1e-12);

std::cout << "output[" << i << "] cosine=" << cos

<< " musa_all_zero=" << (any ? "false" : "true") << "\n";

if (cos < 0.999 || !any) ok = false;

}

std::cout << (ok ? "PASS: MUSA vs CPU 精度验证通过\n" : "FAIL: 精��度不达标\n");

return ok ? 0 : 1;

}



预期输出末行：

`PASS: MUSA vs CPU 精度验证通过`



**注意**：不达标时程序打印 `FAIL: 精度不达标`

并以退出码 1 结束，同时逐输出打印 cosine 值。出现 `musa_all_zero=true`

或 cosine 明显偏低时，请按[常见问题](https://docs.mthreads.com/onnxruntime-musa-m1000/ONNXRuntime-MUSA-M1000/faq)提供的信息联系摩尔线程技术支持。

## 确认节点在 GPU 上执行[](https://docs.mthreads.com#确认节点在-gpu-上执行)

`providers`

中含 `MUSAExecutionProvider`

只表示 Execution Provider 已加载，不代表模型的全部节点都在 GPU 上执行。

如需确认，创建 session 前禁用 CPU 回退：

`so.AddConfigEntry("session.disable_cpu_ep_fallback", "1");`



启用后，若存在无法在 GPU 上执行的节点，session 创建阶段即直接报错而非改用 CPU；能够创建成功并完成一次推理，即表示全部节点都在 GPU 上执行。

该配置用于确认节点分布，不作为常规运行配置。若某模型启用后报错，关闭该配置即可正常运行，相关节点将由引擎自动改用 CPU 执行。

## 离线编译[](https://docs.mthreads.com#离线编译)

设备无外网时，先在��联网设备下载运行库并拷贝到 M1000。Step3 的片段使用了 `CACHE STRING`

，因此命令行 `-D`

可覆盖默认地址：

`ORTMUSA_TGZ="$HOME/onnxruntime-linux-aarch64-1.23.0-release.tgz" # ← 改成本机实际路径`

test -f "$ORTMUSA_TGZ" || echo "文件不存在，请先确认路径：$ORTMUSA_TGZ"

ORTMUSA_TGZ="$(readlink -f "$ORTMUSA_TGZ")"


cmake -DORTMUSA_TARBALL_URL="file://$ORTMUSA_TGZ" \

-DORTMUSA_TARBALL_HASH=SHA256=7e18c1875127d520fbe2421d39b63ac5d3035b323ae12e4622e748f557cb1e71 ..

make -j4



`cmake`

与 `make`

的退出码为 0 不能作为"确实使用了本地包"的判据。

设备有外网时，即使 `-D`

未生效也会构建成功，实际仍从网络下载。

验证方式：

`find _deps -name "*urlinfo.txt" -exec grep -H "^url" {} +`

grep ORTMUSA_TARBALL_URL CMakeCache.txt



预期输出（路径为实际值）：

`_deps/onnxruntime-subbuild/onnxruntime-populate-prefix/src/onnxruntime-populate-stamp/onnxruntime-populate-urlinfo.txt:url(s)=/home/<user>/onnxruntime-linux-aarch64-1.23.0-release.tgz`

ORTMUSA_TARBALL_URL:STRING=file:///home/<user>/onnxruntime-linux-aarch64-1.23.0-release.tgz



**注意**：判定标准是 `url(s)`

的值为本地绝对路径、不以 `http(s)://`

开头。CMake 会在 `urlinfo.txt`

中规范化去掉 `file://`

前缀，`CMakeCache.txt`

中仍保留，两处不一致属正常。该文件名带项目前缀，因此用 `-name "*urlinfo.txt"`

匹�配，写成 `-name urlinfo.txt`

找不到。

也可让 `CMakeLists.txt`

自动探测本地包，放置后无需每次传 `-D`

。该段须放在 Step3 的 `FetchContent_Declare`

之前：

`set(possible_file_locations`

$ENV{HOME}/onnxruntime-linux-aarch64-1.23.0-release.tgz

${PROJECT_SOURCE_DIR}/onnxruntime-linux-aarch64-1.23.0-release.tgz

/tmp/onnxruntime-linux-aarch64-1.23.0-release.tgz)

foreach(f IN LISTS possible_file_locations)

if(EXISTS ${f})

file(TO_CMAKE_PATH "${f}" ORTMUSA_TARBALL_URL)

break()

endif()

endforeach()



## 方式二：使用 deb 安装包[](https://docs.mthreads.com#方式二使用-deb-安装包)

前文各步骤将运行库放在工程自己的目录内，工程完全控制其位置与版本，适合把引擎集成进自有程序。

另有一个 deb 安装包，把同一份运行库安装到系统目录。它面向的是设备批量部署：装完之后 `find_package(onnxruntime)`

与 `pkg-config`

直接可用，工程侧不再需要下载与解压。

**deb 安装包只提供 C++ 运行库，不包含 Python 支持。**

在同一台设备上使用 Python 接口，仍需按[安装与验证](https://docs.mthreads.com/onnxruntime-musa-m1000/ONNXRuntime-MUSA-M1000/installation)安装 wheel，两者互不影响。

| 项目 | 值 |
|---|---|
| 文件名 | `onnxruntime-musa_1.23.0+musa.04f2c3f1_arm64.deb` |
| 下载地址 | `https://mt-vaas-web.tos-cn-beijing.volces.com/release/ort_musa/OrtMusaV0.27.7_M1000/M1000-SDK5.1.0/onnxruntime-musa_1.23.0+musa.04f2c3f1_arm64.deb` |
| SHA256 | `202c22299ee449ff27c7a9eba076f240667832d65b69b0fcf86193ec3f1bd174` |

安装包内的运行库与[运行库](https://docs.mthreads.com#%E8%BF%90%E8%A1%8C%E5%BA%93)一节的 tarball 逐字节相同，仅目录布局不同。两者不要在同一台设备上混用。

### Step1 下载并校验[](https://docs.mthreads.com#step1-下载并校验)

`wget https://mt-vaas-web.tos-cn-beijing.volces.com/release/ort_musa/OrtMusaV0.27.7_M1000/M1000-SDK5.1.0/onnxruntime-musa_1.23.0+musa.04f2c3f1_arm64.deb`


echo "202c22299ee449ff27c7a9eba076f240667832d65b69b0fcf86193ec3f1bd174 onnxruntime-musa_1.23.0+musa.04f2c3f1_arm64.deb" | LC_ALL=C sha256sum -c -



预期输出：

`onnxruntime-musa_1.23.0+musa.04f2c3f1_arm64.deb: OK`



### Step2 安装[](https://docs.mthreads.com#step2-安装)

`sudo dpkg -i onnxruntime-musa_1.23.0+musa.04f2c3f1_arm64.deb`



安装后确认：

`dpkg -l onnxruntime-musa`



预期输出的末行：

`ii onnxruntime-musa 1.23.0+musa.04f2c3f1 arm64 ONNX Runtime with MUSA execution provider (C++ runtime)`



**注意**：状态须为 `ii`

，版本须为 `1.23.0+musa.04f2c3f1`

。

安装位置：

| 内容 | 路径 |
|---|---|
| 头文件 | `/usr/include/onnxruntime/` |
| 运行库 | `/usr/lib/aarch64-linux-gnu/libonnxruntime.so*` 、`libonnxruntime_providers_musa.so` 、`libonnxruntime_providers_shared.so` |
| CMake package config | `/usr/lib/aarch64-linux-gnu/cmake/onnxruntime/` |
| pkg-config | `/usr/lib/aarch64-linux-gnu/pkgconfig/libonnxruntime.pc` |

安装包不声明对 MUSA 驱动与 SDK 的依赖，也不修改动态库搜索路径。运行时仍需 `LD_LIBRARY_PATH`

包含 `/usr/local/musa/lib`

，与前文一致。

### Step3 接入工程[](https://docs.mthreads.com#step3-接入工程)

安装后，工程的 `CMakeLists.txt`

只需下列内容，不再需要 `FetchContent`

与两个 `-D`

参数：

`cmake_minimum_required(VERSION 3.22)`

project(your_project LANGUAGES CXX)


set(CMAKE_CXX_STANDARD 17)

set(CMAKE_CXX_STANDARD_REQUIRED ON)


find_package(onnxruntime REQUIRED)


add_executable(your_target main.cc)

target_link_libraries(your_target PRIVATE onnxruntime::onnxruntime)



`onnxruntime::onnxruntime`

已携带头文件搜索路径，源码中的 `#include <onnxruntime_cxx_api.h>`

与 `#include <musa_provider_options.h>`

写法不变。

使用 `pkg-config`

的工程则为：

`pkg-config --cflags --libs libonnxruntime`



`-I/usr/include/onnxruntime -lonnxruntime`



### Step4 验证[](https://docs.mthreads.com#step4-验证)

沿用[快速验证](https://docs.mthreads.com#step2-%E5%BF%AB%E9%80%9F%E9%AA%8C%E8%AF%81)一节的示例包。解压后**将其 CMakeLists.txt 整体替换为上一节的内容**（

`your_project`

与 `your_target`

改为 `ort_musa_cpp_demo`

），其余文件不动：`cd ort_musa_cpp_demo`

mkdir -p build && cd build

cmake ..

make -j4


export LD_LIBRARY_PATH=/usr/local/musa/lib:$LD_LIBRARY_PATH

./ort_musa_cpp_demo ../models/mobilenet_v2_fp16.onnx 0



预期输出的关键行：

`providers : MUSAExecutionProvider CPUExecutionProvider`

output : [1, 1000]

PASS: MUSA EP C++ inference completed.



**注意**：`providers`

一行须含 `MUSAExecutionProvider`

，且末行为 `PASS`

。

此处 cmake 只需 3.22，Ubuntu 22.04 的 `sudo apt install cmake`

提供 3.22.1，已满足，无需[编译工具链](https://docs.mthreads.com#step1-%E7%BC%96%E8%AF%91%E5%B7%A5%E5%85%B7%E9%93%BE)一节的高版本 cmake。

### 卸载[](https://docs.mthreads.com#卸载)

`sudo dpkg -P onnxruntime-musa`



卸载后 `dpkg -l onnxruntime-musa`

报 `没有找到与 onnxruntime-musa 相匹配的软件包`

，上表中的四处安装位置一并移除。

## 常见问题[](https://docs.mthreads.com#常见问题)

C++ 路线特有的问题见下表，环境与驱动类问题见[常见问题](https://docs.mthreads.com/onnxruntime-musa-m1000/ONNXRuntime-MUSA-M1000/faq)。

| 现象 | 原因 | 处�理 |
|---|---|---|
`CMake 3.23 or higher is required` | 示例包要求 cmake ≥ 3.23，本机版本偏低 | 按 Step1 安装官方预编译包。仅接入自有工程时 3.22 已满足，无需升级 |
运行报 `libmusart.so.5: cannot open shared object file` | `LD_LIBRARY_PATH` 未包含 `/usr/local/musa/lib` ，脚本、cron 与非交互 SSH 场景最易发生 | `export LD_LIBRARY_PATH=/usr/local/musa/lib:$LD_LIBRARY_PATH` |
运行报 `libonnxruntime.so: cannot open shared object file` | 可执行文件定位不到引擎自带运行库 | 按 Step3 设置 `BUILD_RPATH` 与 `INSTALL_RPATH` ；或运行前将运行库目录加入 `LD_LIBRARY_PATH` |
`ldd` 报 `libmudnn_xmma.so => not found` | 本机 muDNN 安装不完整 | 该库由 MUSA SDK 提供，标准安装即包含。确认 `/usr/local/musa/lib/libmudnn_xmma.so` 存在 |
链接阶段报架构不匹配或 `file in wrong format` | 下载到了 x86_64 版运行库 | 示例包默认地址指向另一平台，按 Step2 用两个 `-D` 参数覆盖 |
`MUSAExecutionProvider` 不在 providers 列表 | provider 动态库加载失败 | 依次确认 `mthreads-smi` 能看到 GPU、`LD_LIBRARY_PATH` 含 `/usr/local/musa/lib` 、Step4 的 `ldd` 无 `not found` |
| 离线编译"成功"但怀疑仍走了网络 | 退出码不能作为离线判据 | 按上文检查 `urlinfo.txt` 中的 `url(s)` 是否为本地绝对路径 |
cmake 配置阶段出现 `DOWNLOAD_EXTRACT_TIMESTAMP` / `CMP0135` 警告 | cmake 的开发者提示 | 不影响构建结果，可忽略 |