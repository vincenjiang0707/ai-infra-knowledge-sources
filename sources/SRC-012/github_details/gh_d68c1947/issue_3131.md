# [Issue #3131] [Question] While waiting for the model's response on an Android phone, performing other operations may cause the phone to become unresponsive or reboot.

source: https://github.com/mlc-ai/mlc-llm/issues/3131
state: closed | updated: 2026-03-01T20:44:12Z
labels: question

## 正文

## ❓ General Questions

While waiting for the model's response on an Android phone, performing other operations may cause the phone to become unresponsive or reboot.
For example, if I want to return to the home screen.

![Image](https://github.com/user-attachments/assets/e5f915aa-b337-433c-8809-d7d474a895a7)



I suspect that it's due to insufficient GPU resources on the device. Trying to use only the CPU results in the app crashing.

2025-03-04 15:03:37.647 19380-19447/ai.mlc.mlcchat E/AndroidRuntime: FATAL EXCEPTION: Thread-5
    Process: ai.mlc.mlcchat, PID: 19380
    org.apache.tvm.Base$TVMError: TVMError: Assert fail: T.tvm_struct_get(p_model_embed_tokens_q_weight, 0, 10, "int32") == 4, Argument qwen2_q4f16_1_e396fd42f6a997ca798eafc3bf56647f_fused_dequantize_take1.p_model_embed_tokens_q_weight.device_type has an unsatisfied constraint: 4 == T.tvm_struct_get(p_model_embed_tokens_q_weight, 0, 10, "int32")
    
        at org.apache.tvm.Base.checkCall(Base.java:173)
        at org.apache.tvm.Function.invoke(Function.java:130)
        at ai.mlc.mlcllm.JSONFFIEngine.runBackgroundLoop(JSONFFIEngine.java:65)
        at ai.mlc.mlcllm.MLCEngine$backgroundWorker$1.invoke(MLCEngine.kt:42)
        at ai.mlc.mlcllm.MLCEngine$backgroundWorker$1.invoke(MLCEngine.kt:40)
        at ai.mlc.mlcllm.BackgroundWorker$start$1.invoke(MLCEngine.kt:19)
        at ai.mlc.mlcllm.BackgroundWorker$start$1.invoke(MLCEngine.kt:18)
        at kotlin.concurrent.ThreadsKt$thread$thread$1.run(Thread.kt:30)




## 评论 (3)

### ghost · 2025-02-17

Some devices' systems may have mechanisms to prevent the device from completely freezing. 

Due to MLC occupying the GPU for an extended period, the device's UI rendering becomes completely unresponsive.

On some devices(a Qualcomm Automotive board I tested), this behavior may cause the SystemUI to restart or forcefully interrupt the execution of the OpenCL kernel. 

In some cases(a new gen Qualcomm phone I tested), the device may only attempt to kill the application.

So it might be a device issue, maybe you can try with another phone instead.

### Mawriyo · 2025-02-21

I've experienced this as well! 

https://github.com/mlc-ai/mlc-llm/issues/2894

I would love for this to be clarified but my solution was to compile/use models that have _0. 

### lixiaolong0424 · 2025-05-25

遇到一点小问题，楼主方便有偿问下吗？
