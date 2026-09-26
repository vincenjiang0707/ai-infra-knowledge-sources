source: https://docs.mthreads.com/mtstream/version-1.0/mtstream-doc-online/introduction

# MTStream SDK 开发者手册

## 什么是 MTStream SDK ?[](https://docs.mthreads.com#什么是-mtstream-sdk-)

**MTStream SDK** 是专为 **摩尔线程长江 SoC（M1000）** 平台设计的高性能多媒体处理软件开发包。它通过插件的形式，封装了底层硬件编解码器、图像处理单元的复杂操作，提供简单易用的插件。
目前支持的硬件形态是 MTT E300 AI 计算模组 (AIModule) 。

## 工作原理[](https://docs.mthreads.com#工作原理)

MTStream SDK 基于 **GStreamer Pipeline** 架构，采用**数据流驱动**模型，允许开发者以模块化方式连接输入源（SRC）、处理单元（DECODE/INFER/OSD/ENCODE）和输出目标（SINK）。

所有中间帧数据通过 Linux 共享内存 DMABUF（Direct Memory Access Buffer） 在硬件间共享，避免内存开销，实现数据高速流转。

同时，MTStream SDK 深度集成以下 M1000 的硬件引擎，确保每一步都由专用硬件完成，最大化吞吐量并降低 CPU 负载：

- VPU: H.264/H.265 硬件编解码
- NPU/GPU：AI 推理加速

### 数据流路径 (Data Flow)[](https://docs.mthreads.com#数据流路径-data-flow)

下图展示了从码流（Bitstream）到像素（Pixels）再到输出流的完整处理过程：

### 组件说明[](https://docs.mthreads.com#组件说明)

组件 | 说明 |
|---|---|
| SRC（Source） | 视频输入源： • `FILE` ：本地 H.264 文件• `RTSP` ：网络拉流• `Camera` ：V4L2 摄像头 • `Others` ：UDP、自定义源 |
| DECODE | 使用 `mtvdec` 插件调用 VDE，硬解 H.264/H.265，输出 YUV 帧（NV12 格式） |
| INFER | 使用 `mtnpuinfer` （NPU）或 `mtgpuinfer` （GPU）加载 `.mtnn` 模型，执行目标检测等任务，结果写入帧元数据 |
| OSD | 使用 `mtosd` 插件在帧上叠加检测框、类别标签、FPS 等信息 |
| ENCODE | 使用 `mtvenc` 调用 VEE，将处理后帧重新编码为 H.264/H.265 |
| SINK（Sink） | 输出目标： • `FILE` ：保存视频• `RTSP` ：推流（如 `rtspclientsink` ）• `Display` ：HDMI/VGA 显示• `Others` ：自定义输出 |
| DMABUF | Linux 内核提供的跨设备共享内存机制。MTStream SDK 所有插件间通过 DMABUF 传递帧，无内存拷贝，极大提升吞吐效率 |
| Pipeline 控制器 | GStreamer 自动管理状态机、时钟同步、缓冲区生命周期，无需用户�干预 |

### 软件分层[](https://docs.mthreads.com#软件分层)

- 应用层：用户构建 GStreamer Pipeline（C/C++ 或命令行）
- GStreamer 层：标准框架，负责调度、同步、错误处理
- MTStream SDK 插件层：提供
`mtvdec`

、`mtnpuinfer`

等自定义元素 - HAL 层：驱动 M1000 硬件寄存器、中断、DMA
- 硬件层：M1000 SoC 专用加速单元

### 核心组件与插件[](https://docs.mthreads.com#核心组件与插件)

下表列出了M1000 MTStream SDK的核心插件，对应的功能和应用场景。

M1000插件名称 | 主要功能 | 典型应用场景 | 插件参数 |
|---|---|---|---|
gst-mtvenc | 提供基于VPU硬件视频编码 | 视频存储、RTSP推流 | |
gst-mtvdec | 提供基于VPU硬件视频解码 | RTSP/h264文件解码 | |
gst-mtgpuinfer | GPU推理 | 使用GPU进行推理 | `model-file` 网络权重`model-name` 网络名称（后处理） |
gst-mtnpuinfer | NPU推理 | 使用NPU进行推理 | `model-file` 网络权重`model-name` 网络名称（后处理）`npu-id NPU core` (0~2, 2表示`core0` /`core1` 交替使用) |
gst-mtosd | osd绘制结果 | 绘制推理结果 | `show-fps` 是否显示视频帧率信息 |
gst-mtvideoconvert | color space转换 | YUV转RGB | |
gst-mtpreprocess | 预处理加速(归一化，ColorSpace转换，Resize，Crop等) | 图像归一化、颜色空间转换 |

## 快速上手[](https://docs.mthreads.com#快速上手)

### 步骤一：检查系统环境[](https://docs.mthreads.com#步骤一检查系统环境)

-
系统镜像：AIModule 1.4.0

-
依赖组件：

- GStreamer 1.20+
- MUSA SDK（5.1.0）
- Linux Driver (5.1.0)
- MTNN SDK（1.5.0）
- PyTorch + torch_musa（2.9.0）


### 步骤二：安装第三方库[](https://docs.mthreads.com#步骤二安装第三方库)

`sudo apt install libyuv-dev`

sudo apt install libopencv-dev

sudo apt install gstreamer1.0-plugins-bad

sudo apt install libva-dev

sudo apt install gstreamer1.0-rtsp

sudo apt-get install libpython3.10-dev

sudo apt install python3-pip



### 步骤三：安装依赖组件[](https://docs.mthreads.com#步骤三安装依赖组件)

`# 1. 设置环境变量`

echo 'export PATH=/usr/local/musa/bin:$PATH' >> ~/.bashrc

echo 'export LD_LIBRARY_PATH=/usr/local/musa/lib:$LD_LIBRARY_PATH' >> ~/.bashrc

source ~/.bashrc


# 2. 安装 torch_musa（若需 GPU 推理）

TORCH_OSS="https://moorethreads-ai-soc.tos-cn-beijing.volces.com/mtstream_sdk_release"

pip uninstall torch torch_musa torchvision

pip install $TORCH_OSS/torch-2.5.0-cp310-cp310-linux_aarch64.whl

pip install $TORCH_OSS/torch_musa-2.1.0-cp310-cp310-linux_aarch64.whl

pip install $TORCH_OSS/torchvision-0.20.0a0+afc54f7-cp310-cp310-linux_aarch64.whl

pip install numpy==1.26.4


# 3. 安装 MTNN SDK, 具体安装可参考 https://gitee.com/MooreThreads-AI-SOC/m1000_mtnn

wget https://moorethreads-ai-soc.tos-cn-beijing.volces.com/npu_sdk_release/npu_sdk_v1.5.0.tar.gz

tar -zxf npu_sdk_v1.5.0.tar.gz

cd ~/npu_sdk_v1.5.0/debs/

sudo dpkg -i kernel-module-m1000-npu_1.5-r20251223061609-8cc96d8_all.deb

sudo dpkg -i m1000-mtc-toolkit_1.5-r20251211102012-5aaa237ba_arm64.deb

sudo dpkg -i m1000-mtnnrt_1.5-r20251211101900-f5a4ba5_all.deb

sudo dpkg -i m1000-mtnn-unify-lib_1.5-r20251211101745-cca46b8_all.deb


# 4. 安装 MTStream SDK

wget https://moorethreads-ai-soc.tos-cn-beijing.volces.com/mtstream_sdk_release/mtstream_sdk_v1.0.tar.gz


tar -xzvf mtstream_sdk_v1.0.tar.gz

sudo dpkg -i mtstream_sdk_v1.0/debs/mt-stream-sdk_1.0-r20251215202747+f360357_all.deb



若有错误提示 `libgstmtosd.so`

和 `mtnnrt`

冲突, 使用 `sudo dpkg -i --force-overwrite mt-stream-sdk_*.deb`

.

### 步骤四：验证安装[](https://docs.mthreads.com#步骤四验证安装)

`# 激活环境（含模型路径等）`

source /usr/share/mt-stream-sdk/data/torch_musa_env.sh


# 检查插件是否加载

gst-inspect-1.0 mtgpuinfer

gst-inspect-1.0 mtnpuinfer

gst-inspect-1.0 mtosd

gst-inspect-1.0 mtvdec

gst-inspect-1.0 mtvenc

gst-inspect-1.0 mtvideoconvert



### 步骤五：运行 Demo[](https://docs.mthreads.com#步骤五运行demo)

#### 接收端：启动 RTSP 服务器[](https://docs.mthreads.com#接收端启动rtsp服务器)

`wget https://github.com/bluenviron/mediamtx/releases/download/v1.15.5/mediamtx_v1.15.5_linux_arm64.tar.gz`

tar -xzf mediamtx_v1.15.5_linux_arm64.tar.gz

./mediamtx



#### 发送端：启动 MTStream Pipeline[](https://docs.mthreads.com#发送端启动mtstreampipeline)

`# 启动 4 路不同配置的 pipeline`

mtstream_demo_npu_0.sh # → rtsp://<ip>:8554/test

mtstream_demo_npu_1.sh # → rtsp://<ip>:8554/test2

mtstream_demo_npu_2.sh # → rtsp://<ip>:8554/test3

mtstream_demo_gpu.sh # → rtsp://<ip>:8554/test4



脚本已自动设置 GPU 频率为 750MHz，并启用 YOLOv8m 最佳性能配置。

每 5 帧刷新一次 OSD 上的实时 FPS 与平均 FPS。

#### 拉流播放（客户端）[](https://docs.mthreads.com#拉流播放客户端)

`# 方法1：使用 ffplay（推荐）`

ffplay -rtsp_transport tcp -buffer_size 2048000 rtsp://<ip>:8554/test

ffplay -rtsp_transport tcp -buffer_size 2048000 rtsp://<ip>:8554/test2

...


# 方法2：使用 mpv

mpv --rtsp-transport=tcp --no-cache --profile=low-latency rtsp://<ip>:8554/test



网络抖动可能导致卡顿，请在稳定局域网环境下测试。

## 示例代码[](https://docs.mthreads.com#示例代码)

以下示例代码介绍了 MTStream SDK 主要的操作流程。命令行和C应用两种方式任选其一即可。

### 命令行[](https://docs.mthreads.com#命令行)

可以使用以下命令行的方式快速验证:

`# 解码+推理+编码+推流 命令行`

gst-launch-1.0 \

multifilesrc location="/usr/share/mt-stream-sdk/data/road_pedestrian_30fps.h264" loop=TRUE ! \

h264parse ! \

video/x-h264,stream-format=byte-stream ! \

mtvdec ! \

videorate ! \

video/x-raw,framerate=30/1 ! \

mtnpuinfer model-file=/usr/share/mt-stream-sdk/data/yolov8m.mtnn model-name=yolov8 npu-id=0 ! \

mtosd show-fps=TRUE ! \

mtvenc ! \

rtspclientsink location=rtsp://127.0.0.1:8554/test


# 拉流+解码+推理+显示 命令行

gst-launch-1.0 rtspsrc location="rtsp://127.0.0.1:8554/test" ! \

rtph264depay ! h264parse ! video/x-h264,stream-format=byte-stream ! \

mtvdec ! videorate ! mtnpuinfer model-file=/usr/share/mt-stream-sdk/data/yolov8m.mtnn model-name=yolov8 npu-id=0 ! \

mtosd show-fps=TRUE ! videoconvert ! autovideosink



### C 应用[](https://docs.mthreads.com#c应用)

也可以使用 C 应用来快速验证：

#### 解码+推理+编码+推流[](https://docs.mthreads.com#解码推理编码推流)

以下是一个简单的 C 应用，用于解码、��推理、编码和推流：

`#include <gst/gst.h>`

/* 总线消息回调函数 */

static gboolean bus_call(GstBus *bus, GstMessage *msg, gpointer data) {

GMainLoop *loop = (GMainLoop *)data;


switch (GST_MESSAGE_TYPE(msg)) {

case GST_MESSAGE_ERROR: {

GError *err = NULL;

gchar *debug_info = NULL;


gst_message_parse_error(msg, &err, &debug_info);

g_printerr("错误从元素 %s: %s\n", GST_OBJECT_NAME(msg->src), err->message);

g_printerr("调试信息: %s\n", debug_info ? debug_info : "无");

g_clear_error(&err);

g_free(debug_info);


g_main_loop_quit(loop);

break;

}

case GST_MESSAGE_EOS:

g_print("流结束\n");

g_main_loop_quit(loop);

break;

case GST_MESSAGE_STATE_CHANGED: {

GstState old_state, new_state, pending_state;

gst_message_parse_state_changed(msg, &old_state, &new_state, &pending_state);

if (GST_MESSAGE_SRC(msg) == GST_OBJECT(data)) {

g_print("管道状态从 %s 变为 %s\n",

gst_element_state_get_name(old_state),

gst_element_state_get_name(new_state));

}

break;

}

default:

break;

}


return TRUE;

}


int main(int argc, char *argv[]) {

GstElement *pipeline, *source, *h264parse, *capsfilter, *decoder, *videorate;

GstElement *infer, *osd, *encoder, *sink;

GstCaps *caps;

GstBus *bus;

GMainLoop *loop;


/* 初始化 GStreamer */

gst_init(&argc, &argv);


/* 创建元素 */

pipeline = gst_pipeline_new("mt-npu-pipeline");

source = gst_element_factory_make("multifilesrc", "source");

h264parse = gst_element_factory_make("h264parse", "parser");

capsfilter = gst_element_factory_make("capsfilter", "capsfilter");

decoder = gst_element_factory_make("mtvdec", "decoder");

videorate = gst_element_factory_make("videorate", "videorate");

infer = gst_element_factory_make("mtnpuinfer", "infer");

osd = gst_element_factory_make("mtosd", "osd");

encoder = gst_element_factory_make("mtvenc", "encoder");

sink = gst_element_factory_make("rtspclientsink", "sink");


if (!pipeline || !source || !h264parse || !capsfilter || !decoder ||

!videorate || !infer || !osd || !encoder || !sink) {

g_printerr("无法创建所有必需的 GStreamer 元素\n");

if (!source) g_printerr(" 无法创建 multifilesrc\n");

if (!h264parse) g_printerr(" 无法创建 h264parse\n");

if (!capsfilter) g_printerr(" 无法创建 capsfilter\n");

if (!decoder) g_printerr(" 无法创建 mtvdec\n");

if (!videorate) g_printerr(" 无法创建 videorate\n");

if (!infer) g_printerr(" 无法创建 mtnpuinfer\n");

if (!osd) g_printerr(" 无法创建 mtosd\n");

if (!encoder) g_printerr(" 无法创建 mtvenc\n");

if (!sink) g_printerr(" 无法创建 rtspclientsink\n");

return -1;

}


/* 设置元素属性 */

g_object_set(G_OBJECT(source),

"location", "/usr/share/mt-stream-sdk/data/road_pedestrian_30fps.h264",

"loop", TRUE,

NULL);


/* 设置 caps filter 属性 */

caps = gst_caps_from_string("video/x-h264,stream-format=byte-stream");

g_object_set(G_OBJECT(capsfilter), "caps", caps, NULL);

gst_caps_unref(caps);


/* 设置 videorate caps */

caps = gst_caps_from_string("video/x-raw,framerate=30/1");

g_object_set(G_OBJECT(videorate), "caps", caps, NULL);

gst_caps_unref(caps);


/* 设置 mtnpuinfer 属性 */

g_object_set(G_OBJECT(infer),

"model-file", "/usr/share/mt-stream-sdk/data/yolov8m.mtnn",

"model-name", "yolov8",

"npu-id", 0,

NULL);


/* 设置 mtosd 属性 */

g_object_set(G_OBJECT(osd), "show-fps", TRUE, NULL);


/* 设置 rtspclientsink 属性 */

g_object_set(G_OBJECT(sink), "location", "rtsp://127.0.0.1:8554/test", NULL);


/* 构建管道 */

gst_bin_add_many(GST_BIN(pipeline),

source, h264parse, capsfilter, decoder, videorate,

infer, osd, encoder, sink, NULL);


/* 链接元素 */

if (!gst_element_link_many(source, h264parse, capsfilter, decoder,

videorate, infer, osd, encoder, sink, NULL)) {

g_printerr("无法链接元素\n");

gst_object_unref(pipeline);

return -1;

}


/* 创建主循环 */

loop = g_main_loop_new(NULL, FALSE);


/* 设置总线消息处理器 */

bus = gst_element_get_bus(pipeline);

gst_bus_add_watch(bus, bus_call, loop);

gst_object_unref(bus);


/* 开始播放 */

g_print("开始播放...\n");

gst_element_set_state(pipeline, GST_STATE_PLAYING);


/* 运行主循环 */

g_main_loop_run(loop);


/* 清理 */

g_print("停止播放...\n");

gst_element_set_state(pipeline, GST_STATE_NULL);

gst_object_unref(pipeline);

g_main_loop_unref(loop);


return 0;

}



#### 拉流+解码+推理+显示[](https://docs.mthreads.com#拉流解码推理显示)

以下是一个完整的 GStreamer 管道，用于拉流、解码、推理和显示：

`#include <gst/gst.h>`

#include <glib.h>


// 定义管道结构

typedef struct _PipelineData {

GstElement *pipeline;

GstElement *src;

GstElement *rtpdepay;

GstElement *h264parse;

GstElement *capsfilter;

GstElement *decoder;

GstElement *videorate;

GstElement *infer;

GstElement *osd;

GstElement *convert;

GstElement *sink;

GMainLoop *loop;

} PipelineData;


// 错误处理回调

static void error_cb(GstBus *bus, GstMessage *msg, PipelineData *data) {

GError *err = NULL;

gchar *debug_info = NULL;


gst_message_parse_error(msg, &err, &debug_info);

g_printerr("错误: %s\n", err->message);

if (debug_info) {

g_printerr("调试信息: %s\n", debug_info);

}


g_error_free(err);

g_free(debug_info);

g_main_loop_quit(data->loop);

}


// EOS（结束流）处理回调

static void eos_cb(GstBus *bus, GstMessage *msg, PipelineData *data) {

g_print("流结束\n");

g_main_loop_quit(data->loop);

}


// rtspsrc的pad-added回调函数

static void on_pad_added(GstElement *src, GstPad *new_pad, GstElement *depay) {

GstPad *sink_pad = gst_element_get_static_pad(depay, "sink");

GstPadLinkReturn ret;

GstCaps *new_pad_caps = NULL;

GstStructure *new_pad_struct = NULL;

const gchar *new_pad_type = NULL;


// 检查新pad是否已链接

if (gst_pad_is_linked(sink_pad)) {

g_print("Pad已经链接，跳过\n");

goto exit;

}


// 检查新pad的媒体类型

new_pad_caps = gst_pad_get_current_caps(new_pad);

if (!new_pad_caps) {

new_pad_caps = gst_pad_query_caps(new_pad, NULL);

}


new_pad_struct = gst_caps_get_structure(new_pad_caps, 0);

new_pad_type = gst_structure_get_name(new_pad_struct);


// 只链接视频流（H.264）

if (g_str_has_prefix(new_pad_type, "application/x-rtp")) {

const gchar *encoding_name = gst_structure_get_string(new_pad_struct, "encoding-name");


if (encoding_name && g_str_equal(encoding_name, "H264")) {

// 尝试链接pad

ret = gst_pad_link(new_pad, sink_pad);

if (GST_PAD_LINK_FAILED(ret)) {

g_print("链接失败\n");

} else {

g_print("成功链接到H.264视频流\n");

}

}

}


if (new_pad_caps) {

gst_caps_unref(new_pad_caps);

}


exit:

if (sink_pad) {

gst_object_unref(sink_pad);

}

}


int main(int argc, char *argv[]) {

GstBus *bus;

PipelineData data;


// 初始化GStreamer

gst_init(&argc, &argv);


// 创建主循环

data.loop = g_main_loop_new(NULL, FALSE);


// 创建管道和元素

data.pipeline = gst_pipeline_new("rtsp-pipeline");

data.src = gst_element_factory_make("rtspsrc", "source");

data.rtpdepay = gst_element_factory_make("rtph264depay", "depayloader");

data.h264parse = gst_element_factory_make("h264parse", "parser");

data.capsfilter = gst_element_factory_make("capsfilter", "capsfilter");

data.decoder = gst_element_factory_make("mtvdec", "decoder");

data.videorate = gst_element_factory_make("videorate", "videorate");

data.infer = gst_element_factory_make("mtnpuinfer", "npu-infer");

data.osd = gst_element_factory_make("mtosd", "osd");

data.convert = gst_element_factory_make("videoconvert", "converter");

data.sink = gst_element_factory_make("autovideosink", "sink");


// 检查所有元素是否创建成功

if (!data.pipeline || !data.src || !data.rtpdepay || !data.h264parse ||

!data.capsfilter || !data.decoder || !data.videorate || !data.infer ||

!data.osd || !data.convert || !data.sink) {

g_printerr("一个或多个元素创建失败。请检查插件安装。\n");

return -1;

}


// 设置元素属性

// RTSP源

g_object_set(G_OBJECT(data.src), "location", "rtsp://127.0.0.1:8554/test", NULL);


// Caps过滤器：设置H.264格式为字节流

GstCaps *caps = gst_caps_from_string("video/x-h264,stream-format=byte-stream");

g_object_set(G_OBJECT(data.capsfilter), "caps", caps, NULL);

gst_caps_unref(caps);


// NPU推理器：设置模型文件等参数

g_object_set(G_OBJECT(data.infer),

"model-file", "/usr/share/mt-stream-sdk/data/yolov8m.mtnn",

"model-name", "yolov8",

"npu-id", 0,

NULL);


// OSD（屏幕显示）：显示FPS

g_object_set(G_OBJECT(data.osd), "show-fps", TRUE, NULL);


// 将所有元素添加到管道

gst_bin_add_many(GST_BIN(data.pipeline),

data.src, data.rtpdepay, data.h264parse,

data.capsfilter, data.decoder, data.videorate,

data.infer, data.osd, data.convert, data.sink,

NULL);


// 链接元素（除了rtspsrc，它需要动态链接）

// 注意：rtspsrc的输出是动态的，我们需要在pad-added回调中链接

gst_element_link_many(data.rtpdepay, data.h264parse, data.capsfilter,

data.decoder, data.videorate, data.infer,

data.osd, data.convert, data.sink, NULL);


// 设置rtspsrc的pad-added信号回调

g_signal_connect(data.src, "pad-added", G_CALLBACK(on_pad_added), data.rtpdepay);


// 获取管道总线并添加消息监视器

bus = gst_element_get_bus(data.pipeline);

gst_bus_add_signal_watch(bus);

g_signal_connect(bus, "message::error", G_CALLBACK(error_cb), &data);

g_signal_connect(bus, "message::eos", G_CALLBACK(eos_cb), &data);

gst_object_unref(bus);


// 设置管道状态为播放

gst_element_set_state(data.pipeline, GST_STATE_PLAYING);


g_print("管道开始运行...\n");


// 运行主循环

g_main_loop_run(data.loop);


// 清理资源

gst_element_set_state(data.pipeline, GST_STATE_NULL);

gst_object_unref(data.pipeline);

g_main_loop_unref(data.loop);


return 0;

}



## 性能测试结果[](https://docs.mthreads.com#性能测试结果)

基于 M1000 平台的性能测试结果如下，可满足实时视频分析需求：

场景 | 并发路数 | 分辨率 | 单路FPS |
|---|---|---|---|
| 解码 + 推理 + 编码 | 4 | 1080P | 25 |

## 相关文档[](https://docs.mthreads.com#相关文档)

## 结语[](https://docs.mthreads.com#结语)

MTStream SDK 以 **GStreamer 插件**的形式，将 M1000 SoC 的硬件能力开放给开发者。它不仅简化了视频处理流水线的构建，更充分发挥了摩尔线程 M1000 SoC 的硬件优势，通过**DMABUF 架构** 和 **全链路硬件加速**，实现了高并发、低延迟、低功耗的智能视频处理能力，适用于 **智慧城市、边缘AI、云游戏、远程办公** 等多种场景。

我们诚邀开发者社区参与反馈、贡献与共建！