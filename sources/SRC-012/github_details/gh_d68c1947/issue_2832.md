# [Issue #2832] [Bug] Android app crashing/error with all models

source: https://github.com/mlc-ai/mlc-llm/issues/2832
state: closed | updated: 2026-03-01T20:45:03Z
labels: bug

## 正文

## 🐛 Bug

Every model downloaded either complains download not complete, try to redownload, or when it is downloaded again or doesn't make that complaint, throws this error:

MLCChat failed

Stack trace:
org.apache.tvm.Base$TVMError: TVMError: Function vm.builtin.paged_attention_kv_cache_create_reduced(0: runtime.ShapeTuple, 1: int64_t, 2: int64_t, 3: int64_t, 4: int64_t, 5: int, 6: double, 7: double, 8: runtime.NDArray, 9: runtime.PackedFunc, 10: runtime.PackedFunc, 11: runtime.PackedFunc, 12: runtime.PackedFunc, 13: runtime.PackedFunc, 14: runtime.PackedFunc, 15: runtime.PackedFunc, 16: runtime.PackedFunc, 17: runtime.PackedFunc, 18: runtime.PackedFunc) -> relax.vm.AttentionKVCache expects 19 arguments, but 18 were provided.
Stack trace:
  File "/Users/kartik/mlc/tvm/include/tvm/runtime/packed_func.h", line 1908

	at org.apache.tvm.Base.checkCall(Base.java:173)
	at org.apache.tvm.Function.invoke(Function.java:130)
	at ai.mlc.mlcllm.ChatModule.reload(ChatModule.java:46)
	at ai.mlc.mlcchat.AppViewModel$ChatState$mainReloadChat$1$2.invoke(AppViewModel.kt:648)
	at ai.mlc.mlcchat.AppViewModel$ChatState$mainReloadChat$1$2.invoke(AppViewModel.kt:646)
	at ai.mlc.mlcchat.AppViewModel$ChatState.callBackend(AppViewModel.kt:548)
	at ai.mlc.mlcchat.AppViewModel$ChatState.mainReloadChat$lambda$3(AppViewModel.kt:646)
	at ai.mlc.mlcchat.AppViewModel$ChatState.$r8$lambda$CXL6v4mjTu_Sr5Pk2zFDcus0R-8(Unknown Source:0)
	at ai.mlc.mlcchat.AppViewModel$ChatState$$ExternalSyntheticLambda2.run(Unknown Source:8)
	at java.util.concurrent.Executors$RunnableAdapter.call(Executors.java:487)
	at java.util.concurrent.FutureTask.run(FutureTask.java:264)
	at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1145)
	at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:644)
	at java.lang.Thread.run(Thread.java:1012)

## To Reproduce

Steps to reproduce the behavior:

1. install app
1. download any model (error log provided from attempt to run gemma-2b-q416_1
1. tap the chat icon to the right of model name

<!-- If you have a code sample, error messages, stack traces, please provide it here as well -->

## Expected behavior

Text chat with a language model

## Environment

 - Platform (e.g. 
 - Android 13
 - Samsung z flip 3 5g
 - Installed from Android apk package release at 
https://github.com/mlc-ai/binary-mlc-llm-libs/releases/download/Android-08052024/mlc-chat.apk 

## Additional context

App attempts to initialize chat but throws the error either immediately after initialize or when interacting with the input box. 

## 评论 (7)

### DesolateIntention · 2024-08-22

I have the exact same issue on a Galaxy A54 running Android 14.

### mengshyu · 2024-08-22

Hi @DesolateIntention, I can chat with Gemma-2-2b-it-q4f16_1-MLC on the Samsung S23. Could you please try uninstall first and then reinstalling the app? If the issue persists, could you provide a log for debugging? Thanks.

### seabodylibra · 2024-08-25

I have the same problem on my vivox100

### BlindDeveloper · 2024-08-26

@DesolateIntention @seabodylibra 
First of all try clear Mlc Chat app data and cache, uninstall app and reboot phone.

### BlindDeveloper · 2024-08-26

@richcb @DesolateIntention @seabodylibra 
First of all try clear Mlc Chat app data and cache, uninstall app and reboot phone.

### richcb · 2024-08-26

> @richcb @DesolateIntention @seabodylibra First of all try clear Mlc Chat app data and cache, uninstall app and reboot phone.

I have done this. App now crashes at Initialize toast. Does not go far enough to get an error log
![Screenshot_20240826_145104_MLCChat](https://github.com/user-attachments/assets/5b97bb79-d76a-49de-84a1-4e465b5c2f85)
![Screenshot_20240826_145126_Nova Launcher](https://github.com/user-attachments/assets/7586ed4a-6792-44f3-995f-d676d9d4185a)

I have additionally cleared ram/closed all background apps, restarted phone again.

I will try again with another model and/or newest apk release if there is one newer

**UPDATE**

Llama 2 and Llama 3 work, but all other models give these errors:

**Gemma**
MLCChat failed

Stack trace:
org.apache.tvm.Base$TVMError: ValueError: Error when loading parameters from params_shard_8.bin: [14:57:01] /Users/kartik/mlc/tvm/src/runtime/relax_vm/ndarray_cache_support.cc:193: Check failed: this->nbytes == raw_data_buffer->length() (29542400 vs. 5234233) : ValueError: Encountered an corrupted parameter shard. It means it is not downloaded completely or downloading is interrupted. Please try to download again.
Stack trace:
  File "/Users/kartik/mlc/tvm/src/runtime/relax_vm/ndarray_cache_support.cc", line 255

	at org.apache.tvm.Base.checkCall(Base.java:173)
	at org.apache.tvm.Function.invoke(Function.java:130)
	at ai.mlc.mlcllm.ChatModule.reload(ChatModule.java:46)
	at ai.mlc.mlcchat.AppViewModel$ChatState$mainReloadChat$1$2.invoke(AppViewModel.kt:648)
	at ai.mlc.mlcchat.AppViewModel$ChatState$mainReloadChat$1$2.invoke(AppViewModel.kt:646)
	at ai.mlc.mlcchat.AppViewModel$ChatState.callBackend(AppViewModel.kt:548)
	at ai.mlc.mlcchat.AppViewModel$ChatState.mainReloadChat$lambda$3(AppViewModel.kt:646)
	at ai.mlc.mlcchat.AppViewModel$ChatState.$r8$lambda$CXL6v4mjTu_Sr5Pk2zFDcus0R-8(Unknown Source:0)
	at ai.mlc.mlcchat.AppViewModel$ChatState$$ExternalSyntheticLambda2.run(Unknown Source:8)
	at java.util.concurrent.Executors$RunnableAdapter.call(Executors.java:487)
	at java.util.concurrent.FutureTask.run(FutureTask.java:264)
	at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1145)
	at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:644)
	at java.lang.Thread.run(Thread.java:1012)


Error message:
ValueError: Error when loading parameters from params_shard_8.bin: [14:57:01] /Users/kartik/mlc/tvm/src/runtime/relax_vm/ndarray_cache_support.cc:193: Check failed: this->nbytes == raw_data_buffer->length() (29542400 vs. 5234233) : ValueError: Encountered an corrupted parameter shard. It means it is not downloaded completely or downloading is interrupted. Please try to download again.
Stack trace:
  File "/Users/kartik/mlc/tvm/src/runtime/relax_vm/ndarray_cache_support.cc", line 255


**Phi**

MLCChat failed

Stack trace:
org.apache.tvm.Base$TVMError: TVMError: Function vm.builtin.paged_attention_kv_cache_create_reduced(0: runtime.ShapeTuple, 1: int64_t, 2: int64_t, 3: int64_t, 4: int64_t, 5: int, 6: double, 7: double, 8: runtime.NDArray, 9: runtime.PackedFunc, 10: runtime.PackedFunc, 11: runtime.PackedFunc, 12: runtime.PackedFunc, 13: runtime.PackedFunc, 14: runtime.PackedFunc, 15: runtime.PackedFunc, 16: runtime.PackedFunc, 17: runtime.PackedFunc, 18: runtime.PackedFunc) -> relax.vm.AttentionKVCache expects 19 arguments, but 18 were provided.
Stack trace:
  File "/Users/kartik/mlc/tvm/include/tvm/runtime/packed_func.h", line 1908

	at org.apache.tvm.Base.checkCall(Base.java:173)
	at org.apache.tvm.Function.invoke(Function.java:130)
	at ai.mlc.mlcllm.ChatModule.reload(ChatModule.java:46)
	at ai.mlc.mlcchat.AppViewModel$ChatState$mainReloadChat$1$2.invoke(AppViewModel.kt:648)
	at ai.mlc.mlcchat.AppViewModel$ChatState$mainReloadChat$1$2.invoke(AppViewModel.kt:646)
	at ai.mlc.mlcchat.AppViewModel$ChatState.callBackend(AppViewModel.kt:548)
	at ai.mlc.mlcchat.AppViewModel$ChatState.mainReloadChat$lambda$3(AppViewModel.kt:646)
	at ai.mlc.mlcchat.AppViewModel$ChatState.$r8$lambda$CXL6v4mjTu_Sr5Pk2zFDcus0R-8(Unknown Source:0)
	at ai.mlc.mlcchat.AppViewModel$ChatState$$ExternalSyntheticLambda2.run(Unknown Source:8)
	at java.util.concurrent.Executors$RunnableAdapter.call(Executors.java:487)
	at java.util.concurrent.FutureTask.run(FutureTask.java:264)
	at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1145)
	at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:644)
	at java.lang.Thread.run(Thread.java:1012)


Error message:
TVMError: Function vm.builtin.paged_attention_kv_cache_create_reduced(0: runtime.ShapeTuple, 1: int64_t, 2: int64_t, 3: int64_t, 4: int64_t, 5: int, 6: double, 7: double, 8: runtime.NDArray, 9: runtime.PackedFunc, 10: runtime.PackedFunc, 11: runtime.PackedFunc, 12: runtime.PackedFunc, 13: runtime.PackedFunc, 14: runtime.PackedFunc, 15: runtime.PackedFunc, 16: runtime.PackedFunc, 17: runtime.PackedFunc, 18: runtime.PackedFunc) -> relax.vm.AttentionKVCache expects 19 arguments, but 18 were provided.
Stack trace:
  File "/Users/kartik/mlc/tvm/include/tvm/runtime/packed_func.h", line 1908

**Red Pajama**

MLCChat failed

Stack trace:
org.apache.tvm.Base$TVMError: TVMError: Function vm.builtin.paged_attention_kv_cache_create_reduced(0: runtime.ShapeTuple, 1: int64_t, 2: int64_t, 3: int64_t, 4: int64_t, 5: int, 6: double, 7: double, 8: runtime.NDArray, 9: runtime.PackedFunc, 10: runtime.PackedFunc, 11: runtime.PackedFunc, 12: runtime.PackedFunc, 13: runtime.PackedFunc, 14: runtime.PackedFunc, 15: runtime.PackedFunc, 16: runtime.PackedFunc, 17: runtime.PackedFunc, 18: runtime.PackedFunc) -> relax.vm.AttentionKVCache expects 19 arguments, but 18 were provided.
Stack trace:
  File "/Users/kartik/mlc/tvm/include/tvm/runtime/packed_func.h", line 1908

	at org.apache.tvm.Base.checkCall(Base.java:173)
	at org.apache.tvm.Function.invoke(Function.java:130)
	at ai.mlc.mlcllm.ChatModule.reload(ChatModule.java:46)
	at ai.mlc.mlcchat.AppViewModel$ChatState$mainReloadChat$1$2.invoke(AppViewModel.kt:648)
	at ai.mlc.mlcchat.AppViewModel$ChatState$mainReloadChat$1$2.invoke(AppViewModel.kt:646)
	at ai.mlc.mlcchat.AppViewModel$ChatState.callBackend(AppViewModel.kt:548)
	at ai.mlc.mlcchat.AppViewModel$ChatState.mainReloadChat$lambda$3(AppViewModel.kt:646)
	at ai.mlc.mlcchat.AppViewModel$ChatState.$r8$lambda$CXL6v4mjTu_Sr5Pk2zFDcus0R-8(Unknown Source:0)
	at ai.mlc.mlcchat.AppViewModel$ChatState$$ExternalSyntheticLambda2.run(Unknown Source:8)
	at java.util.concurrent.Executors$RunnableAdapter.call(Executors.java:487)
	at java.util.concurrent.FutureTask.run(FutureTask.java:264)
	at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1145)
	at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:644)
	at java.lang.Thread.run(Thread.java:1012)


Error message:
TVMError: Function vm.builtin.paged_attention_kv_cache_create_reduced(0: runtime.ShapeTuple, 1: int64_t, 2: int64_t, 3: int64_t, 4: int64_t, 5: int, 6: double, 7: double, 8: runtime.NDArray, 9: runtime.PackedFunc, 10: runtime.PackedFunc, 11: runtime.PackedFunc, 12: runtime.PackedFunc, 13: runtime.PackedFunc, 14: runtime.PackedFunc, 15: runtime.PackedFunc, 16: runtime.PackedFunc, 17: runtime.PackedFunc, 18: runtime.PackedFunc) -> relax.vm.AttentionKVCache expects 19 arguments, but 18 were provided.
Stack trace:
  File "/Users/kartik/mlc/tvm/include/tvm/runtime/packed_func.h", line 1908

App quits responding or crashes very, very often, upwards of 6-10 times per minute. This is before initializing a model. After, Llama 2 or 3 work slowly but stably. Other models still do not work. 

### seabodylibra · 2024-08-27

> @DesolateIntention @seabodylibra 
> First of all try clear Mlc Chat app data and cache, uninstall app and reboot phone.

Thank you for your explanation.I am encountering the exact same issues which the author posted earlier. Only Llama 2 and Llama 3 work, while all other models fail to initialize, leading to frequent crashes. I've also tried clearing the app data, cache, 
uninstalling, rebooting, and closing background apps, but the problem persists. Are there any updates or fixes available for this issue?
