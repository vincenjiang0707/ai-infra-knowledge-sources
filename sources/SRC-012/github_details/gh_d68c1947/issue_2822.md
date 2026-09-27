# [Issue #2822] [Bug] 安装的apk下载模型点击对话时闪退

source: https://github.com/mlc-ai/mlc-llm/issues/2822
state: closed | updated: 2026-03-01T20:45:28Z
labels: bug

## 正文

## 🐛 Bug

<!-- A clear and concise description of what the bug is. -->
在下载后的模型点击对话时闪退，浮窗依然显示Initialize...
闪退的分析报告如下：
应用名称：MLCChat
应用版本：1.0
问题发生时间：2024-08-19 14:22:15
问题Trace：
org.apache.tvm.Base$TVMError: ValueError: Check failed: (f != nullptr) is false: Cannot find function mlc.multi_gpu.SendFromLastGroupToWorker0
Stack trace:
  File "/Users/moyu/myworkspace/mlcllm/mlc-llm/cpp/serve/function_table.cc", line 139

```bash
	at org.apache.tvm.Base.checkCall(Base.java:173)
	at org.apache.tvm.Function.invoke(Function.java:130)
	at ai.mlc.mlcllm.JSONFFIEngine.runBackgroundLoop(JSONFFIEngine.java:64)
	at ai.mlc.mlcllm.MLCEngine$backgroundWorker$1.invoke(MLCEngine.kt:42)
	at ai.mlc.mlcllm.MLCEngine$backgroundWorker$1.invoke(MLCEngine.kt:40)
	at ai.mlc.mlcllm.BackgroundWorker$start$1.invoke(MLCEngine.kt:19)
	at ai.mlc.mlcllm.BackgroundWorker$start$1.invoke(MLCEngine.kt:18)
	at kotlin.concurrent.ThreadsKt$thread$thread$1.run(Thread.kt:30)
```

## To Reproduce

Steps to reproduce the behavior:

1.
1.
1.

<!-- If you have a code sample, error messages, stack traces, please provide it here as well -->

## Expected behavior

<!-- A clear and concise description of what you expected to happen. -->

## Environment

 - Platform (e.g. WebGPU/Vulkan/IOS/Android/CUDA):
 - Operating system (e.g. Ubuntu/Windows/MacOS/...):
 - Device (e.g. iPhone 12 Pro, PC+RTX 3090, ...)
 - How you installed MLC-LLM (`conda`, source):
 - How you installed TVM-Unity (`pip`, source):
 - Python version (e.g. 3.10):
 - GPU driver version (if applicable):
 - CUDA/cuDNN version (if applicable):
 - TVM Unity Hash Tag (`python -c "import tvm; print('\n'.join(f'{k}: {v}' for k, v in tvm.support.libinfo().items()))"`, applicable if you compile models):
 - Any other relevant information:

## Additional context

<!-- Add any other context about the problem here. -->


## 评论 (12)

### lcystudy · 2024-08-19

![image](https://github.com/user-attachments/assets/ff6516fc-3fe4-44e1-a580-afab8d029f36)
无论是通过链接下载模型权重，或者使用bundle_weight.py自动绑定权重，点击对话图标时就会发生闪退

### renwanggtv · 2024-08-19

测试机型是什么，看起来是gpu相关的报错，官方示例是骁龙8gen2的机型，我用骁龙888的机器用量化过的小模型也卡半天

### lcystudy · 2024-08-19

对，补充一下硬件信息：redmi k60，处理器是骁龙8+，不知道是不是因为没做好适配，但是之前跑minicpm官方的demo，他们也是用mlcllm做的demo，那个可以跑通，这个我是从头到尾自己build的，不知道在哪里能修改让这个work起来

### renwanggtv · 2024-08-19

我用的Phi-3-mini-4k-instruct-q4f16_1-MLC本地模型，可以正常跑起来，没走下载，要不你换这个模型先试试

### lcystudy · 2024-08-19

> 我用的Phi-3-mini-4k-instruct-q4f16_1-MLC本地模型，可以正常跑起来，没走下载，要不你换这个模型先试试

好的好的，我等会试试，非常感谢！我等会也测试一下不同的机型不同的模型的情况

### lcystudy · 2024-08-19

> 我用的Phi-3-mini-4k-instruct-q4f16_1-MLC本地模型，可以正常跑起来，没走下载，要不你换这个模型先试试

刚刚我用别人做好的apk测试了一下，https://github.com/mlc-ai/binary-mlc-llm-libs/releases/tag/Android-06072024
qwen2-1.5b的模型好像确实有点问题，phi可以正常回复
![image](https://github.com/user-attachments/assets/9b31b299-767d-4098-984c-4625f42375cc)
![image](https://github.com/user-attachments/assets/f017c007-eaef-44de-a183-1c1f29242688)
闪退的问题，我在另一台1+6的机子上测试了，也是闪退，不过这个处理器是骁龙845，可能兼容性更差了，我后面看看有没有机会在更新的机器上测试，我再检查一下我的整个流程是不是哪里做的不对，方便加您的联系方式吗，有些问题交流一下

### warmsnowing · 2024-08-26

我上周遇到同样的闪退问题，更新到最新的代码以后重新打包编译之后就正常了，应该是 #2807 版本修复了。

### gejian-iscas · 2024-08-29

phi3运行起来倒是没问题，但是速度特别慢。首词出现大概要等40s+，手机配置vivo x100 天玑9300，按理说好像不应该吧。

### lcystudy · 2024-08-29

> phi3运行起来倒是没问题，但是速度特别慢。首词出现大概要等40s+，手机配置vivo x100 天玑9300，按理说好像不应该吧。

我用phi2好像是正常的，qwen2不行，纯llm这个速度确实不应该，我记得llama.cpp好像是对高通的npu做过专门的优化，不知道mlc有没有搞过，如果没针对优化可能联发科的芯片推理就会慢点，这个可能要等官方对不同机型做适配吧（我猜测的原因哈）

### lcystudy · 2024-08-29

> 我上周遇到同样的闪退问题，更新到最新的代码以后重新打包编译之后就正常了，应该是 #2807 版本修复了。

好的好的，非常感谢，我有空再去试试看

### gejian-iscas · 2024-08-29

> > phi3运行起来倒是没问题，但是速度特别慢。首词出现大概要等40s+，手机配置vivo x100 天玑9300，按理说好像不应该吧。
> 
> 我用phi2好像是正常的，qwen2不行，纯llm这个速度确实不应该，我记得llama.cpp好像是对高通的npu做过专门的优化，不知道mlc有没有搞过，如果没针对优化可能联发科的芯片推理就会慢点，这个可能要等官方对不同机型做适配吧（我猜测的原因哈）

换了三星的骁龙8gen3，感觉是快了些prefill 1.2 decode 19.7，在vivo上的数据大概是0.2和15，但是感觉首字还是要等很久。

### lcystudy · 2024-08-29

> > > phi3运行起来倒是没问题，但是速度特别慢。首词出现大概要等40s+，手机配置vivo x100 天玑9300，按理说好像不应该吧。
> > 
> > 
> > 我用phi2好像是正常的，qwen2不行，纯llm这个速度确实不应该，我记得llama.cpp好像是对高通的npu做过专门的优化，不知道mlc有没有搞过，如果没针对优化可能联发科的芯片推理就会慢点，这个可能要等官方对不同机型做适配吧（我猜测的原因哈）
> 
> 换了三星的骁龙8gen3，感觉是快了些prefill 1.2 decode 19.7，在vivo上的数据大概是0.2和15，但是感觉首字还是要等很久。

可以用其他模型试试看，我感觉增速度慢很有可能是美联储的框架对phi3模型的适配没有做好，我用minicpm 2.0在我的骁龙8+的红米k60上跑prefill有11.6，decode 6.7，我觉得应该是模型适配的原因
