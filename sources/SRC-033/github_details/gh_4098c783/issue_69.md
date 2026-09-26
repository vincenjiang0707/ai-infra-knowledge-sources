# [Issue #69] F.interpolate on NPU is REALLY slow, even slower than CPU

source: https://github.com/Ascend/pytorch/issues/69
state: open | updated: 2025-12-23T04:41:58Z
labels: 

## 正文

一、问题现象（附报错日志上下文）：
```python
import time
import torch
import torch.nn.functional as F

mode = 'npu' # or npu, cuda

tensor = torch.rand([1, 518, 9]).float().to(mode)
upsample_scale = 300

t_start = time.time()
phase = F.interpolate((tensor.transpose(1, 2) * upsample_scale), scale_factor=upsample_scale, mode="linear").transpose(1, 2)
torch.npu.synchronize()
t_end = time.time()
print(f"Time taken: {t_end - t_start}", tensor.shape, phase.shape)
```

CPU or GPU：
```python
import time
import torch
import torch.nn.functional as F

mode = 'cpu'

tensor = torch.rand([1, 518, 9]).float().to(mode)
upsample_scale = 300

t_start = time.time()
phase = F.interpolate((tensor.transpose(1, 2) * upsample_scale).cpu(), scale_factor=upsample_scale, mode="linear").transpose(1, 2)
torch.cpu.synchronize()
t_end = time.time()
print(f"Time taken: {t_end - t_start}", tensor.shape, phase.shape)
print(phase)
```

二、软件版本:
-- CANN 版本 (e.g., CANN 3.0.x，5.x.x):  CANN 8.0.0
--Tensorflow/Pytorch/MindSpore 版本: Torch 2.5.1 + Torch NPU 2.5.1.post1.dev20250406
--Python 版本 (e.g., Python 3.7.5): 3.10.16
-- MindStudio版本 (e.g., MindStudio 2.0.0 (beta3)): /
--操作系统版本 (e.g., Ubuntu 18.04): Ubuntu 20.04.3 LTS

三、测试步骤：
run the script above and modify `mode` from 'cpu' to 'npu' or 'cuda'


四、日志信息:
- cpu: Time taken: 0.007272243499755859 torch.Size([1, 518, 9]) torch.Size([1, 155400, 9])
- npu: Time taken: 3.5338704586029053 torch.Size([1, 518, 9]) torch.Size([1, 155400, 9])
- gpu: Time taken: 0.015298843383789062 torch.Size([1, 518, 9]) torch.Size([1, 155400, 9])

## 评论 (4)

### yunyiyun · 2025-07-04

1、统计时间时加上同步，确保统计时间准确，这里只在结束的时候添加了同步，开始的时候也需要添加同步
2、NPU首次运行存在编译等过程，耗时较多，可以多跑些step观察后续step耗时
3、可以尝试配置torch.npu.set_compile_mode(jit_compile=False)走二进制，减少编译耗时

### parap1uie-s · 2025-07-04

> 1、统计时间时加上同步，确保统计时间准确，这里只在结束的时候添加了同步，开始的时候也需要添加同步 2、NPU首次运行存在编译等过程，耗时较多，可以多跑些step观察后续step耗时 3、可以尝试配置torch.npu.set_compile_mode(jit_compile=False)走二进制，减少编译耗时

这个是从kokoro-82M的代码里定位到的，同一段输入文本，生成语音，GPU上生成耗时大概1s，NPU 第一次请求42 - 60s，后续请求稳定在27s，调用interploate前手动把tensor卸载到cpu上，计算完转移回来，只要1.7s。所以可以确定和首次运行等因素无关，就是这个算子的NPU实现问题

### yunyiyun · 2025-07-12

> > 1、统计时间时加上同步，确保统计时间准确，这里只在结束的时候添加了同步，开始的时候也需要添加同步 2、NPU首次运行存在编译等过程，耗时较多，可以多跑些step观察后续step耗时 3、可以尝试配置torch.npu.set_compile_mode(jit_compile=False)走二进制，减少编译耗时
> 
> 这个是从kokoro-82M的代码里定位到的，同一段输入文本，生成语音，GPU上生成耗时大概1s，NPU 第一次请求42 - 60s，后续请求稳定在27s，调用interploate前手动把tensor卸载到cpu上，计算完转移回来，只要1.7s。所以可以确定和首次运行等因素无关，就是这个算子的NPU实现问题

针对提供的这段代码，
1、统计时间时加上同步，剔除tensor = torch.rand([1, 518, 9]).float().to(mode)耗时，仅统计phase = F.interpolate((tensor.transpose(1, 2) * upsample_scale), scale_factor=upsample_scale, mode="linear").transpose(1, 2)耗时，
2、配置torch.npu.set_compile_mode(jit_compile=False)走二进制
3、本地测试多次运行时，剔除首次耗时，后续step耗时未观察到比cpu慢

如果您这边发现性能较差，可以多跑些step，通过采集profiling数据做针对性的分析优化
https://www.hiascend.com/document/detail/zh/Pytorch/700/ptmoddevg/trainingmigrguide/performance_tuning_0014.html

### goingHan · 2025-12-23

> > 1、统计时间时加上同步，确保统计时间准确，这里只在结束的时候添加了同步，开始的时候也需要添加同步 2、NPU首次运行存在编译等过程，耗时较多，可以多跑些step观察后续step耗时 3、可以尝试配置torch.npu.set_compile_mode(jit_compile=False)走二进制，减少编译耗时
> 
> 这个是从kokoro-82M的代码里定位到的，同一段输入文本，生成语音，GPU上生成耗时大概1s，NPU 第一次请求42 - 60s，后续请求稳定在27s，调用interploate前手动把tensor卸载到cpu上，计算完转移回来，只要1.7s。所以可以确定和首次运行等因素无关，就是这个算子的NPU实现问题

你好，你在npu上运行kokoro tts ,生成的音频正常吗， 我可以正常推理，但是生成的声音有杂音。 
我得环境是：
torch==2.5.1
torch-npu==2.5.1.post1
cann: 8.0.0 
910B2

生成音频链接：https://nbchat-test.oss-cn-beijing.aliyuncs.com/test_tts_cvo/202512231000-I5q5AxNmI8tZO/final_audio_cWHr54K0.wav
