# [Issue #3234] [Question] TVMError: Binary was created using {relax.Executable} but a loader of that name is not registered.

source: https://github.com/mlc-ai/mlc-llm/issues/3234
state: closed | updated: 2026-03-02T14:51:57Z
labels: question

## 正文

## ❓ General Questions
org.apache.tvm.Base$TVMError: TVMError: Binary was created using {relax.Executable} but a loader of that name is not registered. Available loaders are opencl, relax.VMExecutable. Perhaps you need to recompile with this runtime enabled.
Stack trace:
  File "/home/lixiaolong/桌面/mlc-llm/android/mlc4j/../../3rdparty/tvm/src/runtime/library_module.cc", line 122

```bash
	at org.apache.tvm.Base.checkCall(Base.java:173)
	at org.apache.tvm.Function.invoke(Function.java:130)
	at ai.mlc.mlcllm.JSONFFIEngine.runBackgroundLoop(JSONFFIEngine.java:64)
	at ai.mlc.mlcllm.MLCEngine$backgroundWorker$1.invoke(MLCEngine.kt:42)
	at ai.mlc.mlcllm.MLCEngine$backgroundWorker$1.invoke(MLCEngine.kt:40)
	at ai.mlc.mlcllm.BackgroundWorker$start$1.invoke(MLCEngine.kt:19)
	at ai.mlc.mlcllm.BackgroundWorker$start$1.invoke(MLCEngine.kt:18)
	at kotlin.concurrent.ThreadsKt$thread$thread$1.run(Thread.kt:30)
<!-- Describe your questions -->
之前有人提到这个问题，但是按照他们的方法，都没有解决。https://github.com/mlc-ai/mlc-llm/issues/3055，https://github.com/mlc-ai/mlc-llm/issues/638
在此之前，顺利完成了模型转换权重，和编译，都没有问题。不知道为什么，可以有偿解决，谢谢~
```

## 评论 (1)

### lixiaolong0424 · 2025-06-08

已经解决了，tvm配置的问题，如果不明白可以联系我，有偿，872660436@qq.com
