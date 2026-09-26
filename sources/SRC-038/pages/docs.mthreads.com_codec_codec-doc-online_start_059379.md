source: https://docs.mthreads.com/codec/codec-doc-online/start

# 入门指南

为了满足用户在不同方案架构下的使用需求，摩尔线程提供了多种途径的编解码解决方案以供用户选择。 用户能够选取当下的开源多媒体框架，诸如 FFmpeg、Gstreamer 来展开开发。亦能够直接运用操作系统的 API 接口，像 Windows 系统的 DXVA2、D3D11VA，以及 Linux 系统的 VAAPI。不过，系统层的 API 在使用时相对更为繁杂，需要用户实现较多的应用层逻辑。鉴于此，我们还提供了摩尔线程专属的Codec SDK，对底层接口进行封装，并对外提供简单易用的API接��口，极大地降低了用户使用难度。 使用前请先保证已经正确安装了摩尔线程gpu驱动程序。

## 1.开源多媒体框架[](https://docs.mthreads.com#1开源多媒体框架)

### 1.1 FFmpeg[](https://docs.mthreads.com#11-ffmpeg)

摩尔线程有基于公版FFmpeg定制开发的私有版本，为了充分使用到摩尔线程GPU的相关特性，建议使用摩尔线程私有版本的FFmpeg进行相关开发测试。 我们可以为用户提供FFmpeg可执行程序，或者相关FFmpeg库文件。满足用户的使用需求。

摩尔线程定制版FFmpeg可执行程序以及相关库文件获取，下载地址：[mt-ffmpeg](https://developer.mthreads.com/sdk/download/mt_video_codec_sdk) 。

其中还包含了已经编译好的libva依赖库。 具体版本间依赖关系和功能支持情况如下：

| ffmpeg版本 | libva版本 | h264 enc | h265 enc | av1 enc | h264/h265 dec | av1 dec | vp8 dec | vp9 dec | avs/avs+/avs2 dec |
|---|---|---|---|---|---|---|---|---|---|
| mt-ffmpeg（基于公版ffmpeg-4.4.2） | libva_2.12以下版本 | Y | Y | N | Y | N | Y | Y | N |
| libva_2.12及以上版本 | Y | Y | Y | Y | Y | Y | Y | N | |
| mt-libva_2.20 | Y | Y | Y | Y | Y | Y | Y | Y | |
| 公版ffmpeg-4.4 | libva_2.12以下版本 | Y | N | N | Y | N | Y | Y | N |
| libva_2.12及以上版本 | Y | N | N | Y | Y | Y | Y | N |

- FFmpeg+vaapi 可配置的参数如下：

| 可配置项 | 描述 |
|---|---|
| -vcodec [s] | 编码器： h264_vaapi hevc_vaapi |
| -s:v [s] | 指定输入视频的分辨率，例如1920x1080 |
| -r [n] | 指定输出视频的帧率 |
| -pix_fmt [s] | 输入视频的图像采样格式： yuv420p/nv12/p010le |
| -profile:v [s] | 编码Profile： h.264：main, high hevc：main, main10 |
| -rc_mode [s] | 码控方式： CBR/CQP/VBR |
| -g [n] | GOP大小 |
| -qp [n] | QP值，取值范围为[1:63] |
| -bf:v [n] | 连续B帧数量，取值范围[0:7] |
| -b:v [n] | 设定码率 |
| -b_depth [n] | B帧作为参考帧的最大深度，取值范围是[1:3]。 默认值为1。 当b_depth值大于1时，连续的B帧个数应该是[3:7]。 |
| -refs [n] | P帧可以参考前面多帧，包括I/P帧，取值范围是[1:2]。 默认值为1 |
| -vf [s] | 滤镜支持能力，例如格式转换、帧上传和下载、缩放、ROI编码等： format hwupload download scale_vaapi=w=$width:h=$height addroi=iw/2:ih/2:iw/3:ih/3:-$qpOffset，其中$qpOffset表示ROI区域的QP与整帧QP值的偏移量 |

- 编码测试

- 对8bit YUV视频源进行编码：

`LIBVA_DRIVER_NAME=mtgpu LIBVA_DRIVERS_PATH=/usr/lib/x86_64-linux-gnu/dri/ \`

./ffmpeg -hwaccel vaapi -vaapi_device /dev/dri/renderD128 -v verbose -f rawvideo \

-pix_fmt yuv420p -s:v 1920x1080 -r 50 -i input.yuv -vf 'format=nv12,hwupload' -c:v h264_vaapi -profile:v main -rc_mode VBR -g 250 -b_depth 3 -refs 2 -bf:v 3 -b:v 3M encode_out_8bit.mp4



- 对10bit YUV视频源进行编码：

`LIBVA_DRIVER_NAME=mtgpu LIBVA_DRIVERS_PATH=/usr/lib/x86_64-linux-gnu/dri/ ./ffmpeg -hwaccel vaapi -vaapi_device /dev/dri/renderD129 -v verbose -f rawvideo -pix_fmt p010le -s:v 1920x1080 -r 50 -stream_loop 10 -i 1080p_P010LE.yuv -vf 'format=p010le ,hwupload' -c:v hevc_vaapi -profile:v main10 -rc_mode VBR -g 250 -bf:v 0 -b:v 4000k -y encode_out_h264_10.mp4 `



- 对YUV视频源进行ROI编码：

`LIBVA_DRIVER_NAME=mtgpu LIBVA_DRIVERS_PATH=/usr/lib/x86_64-linux-gnu/dri/ \`

./ffmpeg -hwaccel vaapi -vaapi_device /dev/dri/renderD128 -hwaccel_output_format vaapi -v verbose -f rawvideo \

-pix_fmt yuv420p -s:v 1920x1080 -r 30 -i input.yuv -vf 'addroi=iw/5:ih/4:iw/5:ih/2:-1/3,format=nv12,hwupload' -c:v h264_vaapi -profile:v main -rc_mode CQP -qp 40 -b:v 5M -bf:v 3 encode_out_roi.mp4



- 解码测试

- 将码流解码成YUV格式命令：

`LIBVA_DRIVER_NAME=mtgpu LIBVA_DRIVERS_PATH=/usr/lib/x86_64-linux-gnu/dri \`

./ffmpeg -hwaccel vaapi -hwaccel_device /dev/dri/renderD128 -i input.mp4 -pix_fmt yuv420p -vframes 1000 -y out_1.yuv



- 仅测试解码能力，但不保存解码数据：

`LIBVA_DRIVER_NAME=mtgpu LIBVA_DRIVERS_PATH=/usr/lib/x86_64-linux-gnu/dri \`

./ffmpeg -hwaccel vaapi -hwaccel_device /dev/dri/renderD128 -hwaccel_output_format vaapi \

-i input.mp4 -f null -



- 转码测试

- 将原H.264压缩格式的MP4视频转码成H.265压缩格式的MP4码流：

`LIBVA_DRIVER_NAME=mtgpu LIBVA_DRIVERS_PATH=/usr/lib/x86_64-linux-gnu/dri/ \`

./ffmpeg -hwaccel vaapi -vaapi_device /dev/dri/renderD128 -hwaccel_output_format vaapi \

-i input_h264.mp4 -c:v hevc_vaapi transcode.mp4



- 将原H.264压缩格式的MP4视频转码成H.265压缩格式的MP4码流，并指定编码Profile、码控模式、连续B帧数量、码率等：

`LIBVA_DRIVER_NAME=mtgpu LIBVA_DRIVERS_PATH=/usr/lib/x86_64-linux-gnu/dri/ \`

./ffmpeg -hwaccel vaapi -vaapi_device /dev/dri/renderD128 -hwaccel_output_format vaapi \

-i input_h264.mp4 -c:v hevc_vaapi -profile:v main -rc_mode CBR -bf:v 3 -b:v 4M transcode.mp4



- 将原H.265 10bit压缩格式的MP4视频转码成H.264 8bit压缩格式的MP4码流，并指定编码Profile、码率等：

`LIBVA_DRIVER_NAME=mtgpu LIBVA_DRIVERS_PATH=/usr/lib/x86_64-linux-gnu/dri/ \`

./ffmpeg -hwaccel vaapi -vaapi_device /dev/dri/renderD128 -hwaccel_output_format vaapi \

-i input_h265_10bit.mp4 -vf 'scale_vaapi=format=nv12' -c:v h264_vaapi -profile:v high -b:v 4M transcode_10bit_to_8bit.mp4



- 将原H.264 8bit压缩格式的MP4视频转码成H.265 10bit压缩格式的MP4码流，并指定编码Profile、码控模式、连续B帧数量、码率等：

`LIBVA_DRIVER_NAME=mtgpu LIBVA_DRIVERS_PATH=/usr/lib/x86_64-linux-gnu/dri/ \`

./ffmpeg -hwaccel vaapi -vaapi_device /dev/dri/renderD128 -hwaccel_output_format vaapi \

-i input_h264_8bit.mp4 -vf 'scale_vaapi=format=p010le' -c:v hevc_vaapi -profile:v main10 -b:v 8M transcode_8bit_to_10bit.mp4



- 将原H.265压缩格式的MP4视频转码成H.264压缩格式的MP4码流，对视频分辨率进行Scaling缩放，改变帧率，并指定编码Profile、码控模式、码率等：

`LIBVA_DRIVER_NAME=mtgpu LIBVA_DRIVERS_PATH=/usr/lib/x86_64-linux-gnu/dri/ \`

./ffmpeg -hwaccel vaapi -vaapi_device /dev/dri/renderD128 -hwaccel_output_format vaapi \

-i input_h265.mp4 -r 20 -vf 'scale_vaapi=w=1280:h=720:format=nv12' -c:v h264_vaapi -profile:v main -rc_mode VBR -b:v 4M transcode_scaling.mp4



### 1.2 Gstreamer[](https://docs.mthreads.com#12-gstreamer)

使用公版Gstreamer+VAAPI的形式，可以实现GPU�加速需求。 Gstreamer官方自带调试命令，主要包括：gst-inspect-1.0、gst-launch-1.0和gst-play-1.0。

使用前需要先设置好环境变量

`export GST_VAAPI_ALL_DRIVERS=1`

export LIBVA_DRIVER_NAME=mtgpu

export LIBVA_DRIVERS_PATH=/usr/lib/x86_64-linux-gnu/dri

export GST_VAAPI_DRM_DEVICE=/dev/dri/renderD128



以上四个环境变量是在摩尔线程显卡环境下运行gstreamer+vaapi所必须的。

- gst-inspect-1.0

主要用来查看当前配置支持的plugin和element。例如：gst-inspect-1.0 vaapi 下面展示的列表为，当前vaapi支持的element（格式）。

` gst-inspect-1.0 vaapi`

trace path : /sys/kernel/debug/tracing/trace_marker_raw

Connecting to pvr device ID: 0 (128)

Disconnect from services:

OK

trace path : /sys/kernel/debug/tracing/trace_marker_raw

Connecting to pvr device ID: 0 (128)

Disconnect from services:

OK

Plugin Details:

Name vaapi

Description VA-API based elements

Filename /usr/lib/x86_64-linux-gnu/gstreamer-1.0/libgstvaapi.so

Version 1.16.2

License LGPL

Source module gstreamer-vaapi

Source release date 2019-12-03

Binary package gstreamer-vaapi

Origin URL http://bugzilla.gnome.org/enter_bug.cgi?product=GStreamer


vaapih264enc: VA-API H264 encoder

vaapih265enc: VA-API H265 encoder

vaapisink: VA-API sink

vaapidecodebin: VA-API Decode Bin

vaapipostproc: VA-API video postprocessing

vaapih265dec: VA-API H265 decoder

vaapivp9dec: VA-API VP9 decoder

vaapivp8dec: VA-API VP8 decoder

vaapih264dec: VA-API H264 decoder

vaapih263dec: VA-API H263 decoder

vaapimpeg4dec: VA-API MPEG4 decoder

vaapimpeg2dec: VA-API MPEG2 decoder


12 features:

+-- 12 elements



当前配置的gstreamer可能不包含某些element，此时可以在[Gstreamer 官网](https://gstreamer.freedesktop.org/documentation/?gi-language=c)进行查询。

- gst-inspect-1.0 可以用来查看element支持的参数。例如:gst-inspect-1.0 vaapih264enc

gst-launch-1.0是最为常用的命令，用来进行码流及图像的处理，最常用的为视频编解码： 视频编码：

`gst-launch-1.0 -vf filesrc location=/home/user/work/mt/vaapi-fits/assets/yuv/720p_NV12.yuv num-buffers=150 ! rawvideoparse format=nv12 width=1280 height=720 framerate=30 ! videoconvert chroma-mode=none dither=0 ! video/x-raw,format=NV12 ! vaapih264enc rate-control=cbr keyframe-period=30 num-slices=4 max-bframes=2 bitrate=4000 tune=none ! video/x-h264,profile=main ! h264parse ! filesink location=720p-cbr-main-30-30-4-2-4000k-4000k.h264`



视频解码：

`gst-launch-1.0 -vf filesrc location=/home/user/Videos/1280_704.h264 num-buffers=1 ! h264parse ! vaapih264dec ! video/x-raw,format=NV12 ! filesink location=gst_1280x704_NV12.yuv`

gst-launch-1.0 -vf filesrc location=/home/user/work/vaapi-fits/assets/avc/720p.h264 num-buffers=10 ! h264parse ! vaapih264dec ! 'video/x-raw(memory:DMABuf), format=I420' ! filesink location=gst_720p_1280x720_NV12.yuv



- gst-play-1.0 主要用于视频播放

## 2.系统标准API[](https://docs.mthreads.com#2系统标准api)

摩尔线程驱动根据不同系统规范，实现对应操作系统的API接口。应用层可以根据系统规范，调用对应接口，实现硬件编解码的加速。

| 系统 | API |
|---|---|
| Windows | DXVA2/D3D11VA |
| Linux | VAAPI |

## 3.摩尔线程自研SDK[](https://docs.mthreads.com#3摩尔线程自研sdk)

为了用户能更加方便的使用摩尔线程显卡进行视频编解码工作。摩尔线程提供了MT Encode SDK 、 MT Decode SDK、 MT DirectStream SDK等开发工具套件，用户只需要按照api接口说明即可快速完成编解码功能的开发。