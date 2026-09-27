# [Issue #3381] [Bug] Failed to load Llama

source: https://github.com/mlc-ai/mlc-llm/issues/3381
state: closed | updated: 2026-02-27T22:05:39Z
labels: bug

## 正文

## 🐛 Bug

<!-- A clear and concise description of what the bug is. -->

## To Reproduce

Steps to reproduce the behavior:

1.Load LLama model
1.
1.

<!-- If you have a code sample, error messages, stack traces, please provide it here as well -->

## Expected behavior

response

MLCChat failed

Stack trace:
org.apache.tvm.Base$TVMError: InternalError: Check failed: (config["conv_template"].is<std::string>()) is false: 
Stack trace:
  File "/Users/kartik/mlc/mlc-llm/cpp/llm_chat.cc", line 540

	at org.apache.tvm.Base.checkCall(Base.java:173)
	at org.apache.tvm.Function.invoke(Function.java:130)
	at ai.mlc.mlcllm.ChatModule.reload(ChatModule.java:46)
	at ai.mlc.mlcchat.AppViewModel$ChatState$mainReloadChat$1$2.invoke(AppViewModel.kt:648)
	at ai.mlc.mlcchat.AppViewModel$ChatState$mainReloadChat$1$2.invoke(AppViewModel.kt:646)
	at ai.mlc.mlcchat.AppViewModel$ChatState.callBackend(AppViewModel.kt:548)
	at ai.mlc.mlcchat.AppViewModel$ChatState.mainReloadChat$lambda$3(AppViewModel.kt:646)
	at ai.mlc.mlcchat.AppViewModel$ChatState.$r8$lambda$CXL6v4mjTu_Sr5Pk2zFDcus0R-8(Unknown Source:0)
	at ai.mlc.mlcchat.AppViewModel$ChatState$$ExternalSyntheticLambda2.run(Unknown Source:8)
	at java.util.concurrent.Executors$RunnableAdapter.call(Executors.java:524)
	at java.util.concurrent.FutureTask.run(FutureTask.java:317)
	at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1156)
	at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:651)
	at java.lang.Thread.run(Thread.java:1119)


Error message:
InternalError: Check failed: (config["conv_template"].is<std::string>()) is false: 
Stack trace:
  File "/Users/kartik/mlc/mlc-llm/cpp/llm_chat.cc", line 540


## Environment

 - Platform (e.g. WebGPU/Vulkan/IOS/Android/CUDA): Android 15
 - Operating system (e.g. Ubuntu/Windows/MacOS/...):
 - Device (e.g. iPhone 12 Pro, PC+RTX 3090, ...) Xiaoimi Note 13 pro+
 - How you installed MLC-LLM (`conda`, source):
 - How you installed TVM (`pip`, source):
 - Python version (e.g. 3.10):
 - GPU driver version (if applicable):
 - CUDA/cuDNN version (if applicable):
 - TVM Hash Tag (`python -c "import tvm; print('\n'.join(f'{k}: {v}' for k, v in tvm.support.libinfo().items()))"`, applicable if you compile models):
 - Any other relevant information:

## Additional context

<!-- Add any other context about the problem here. -->


## 评论 (1)

### MasterJH5574 · 2025-11-18

Thank you @mariagcomesanaia-spa for reporting.  Do you mind sharing the concrete model HuggingFace repo link? So we can try to reproduce the issue.
