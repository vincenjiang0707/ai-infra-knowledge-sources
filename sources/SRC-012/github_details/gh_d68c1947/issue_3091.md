# [Issue #3091] [Question] Android App Crash

source: https://github.com/mlc-ai/mlc-llm/issues/3091
state: closed | updated: 2026-03-01T20:43:40Z
labels: question

## 正文

## ❓ General Questions

<!-- Describe your questions -->
The Android app is crashing with an exception - 
```
 channel '1cce162 ai.mlc.mlcchat/ai.mlc.mlcchat.MainActivity (server)' ~ Channel is unrecoverably broken and will be disposed!
2025-01-15 20:28:24.710  1424-1541  WindowManager           system_server                        E  RemoteException occurs on reporting focusChanged, w=Window{1cce162 u0 ai.mlc.mlcchat/ai.mlc.mlcchat.MainActivity}
                                                                                                    android.os.DeadObjectException
                                                                                                    	at android.os.BinderProxy.transactNative(Native Method)
                                                                                                    	at android.os.BinderProxy.transact(BinderProxy.java:575)
                                                                                                    	at android.view.IWindow$Stub$Proxy.windowFocusChanged(IWindow.java:829)
                                                                                                    	at com.android.server.wm.WindowState.reportFocusChangedSerialized(WindowState.java:3793)
                                                                                                    	at com.android.server.wm.WindowManagerService$H.handleMessage(WindowManagerService.java:5433)
                                                                                                    	at android.os.Handler.dispatchMessage(Handler.java:107)
                                                                                                    	at android.os.Looper.loop(Looper.java:237)
                                                                                                    	at android.os.HandlerThread.run(HandlerThread.java:67)
                                                                                                    	at com.android.server.ServiceThread.run(ServiceThread.java:44)
```

I'm using a Galaxy S9 with 64GB of memory. 
package-config.json
``{
    "device": "android",
    "model_list": [
        {
            "model": "HF://mlc-ai/Phi-3.5-mini-instruct-q4f16_0-MLC",
            "estimated_vram_bytes": 4250586449,
            "model_id": "Phi-3.5-mini-instruct-q4f16_0-MLC",
            "overrides": {
                "prefill_chunk_size": 128
            }
        }
   `
``
I also noticed there was a crash at runtime because the linker couldn't find the .so output. I renamed the .so to the file name it was looking for and it worked. 

Any thoughts?


## 评论 (1)

### MasterJH5574 · 2025-02-10

Hi @mhollis1980, thanks for reporting. we are not able to reproduce this failure so have no immediate ideas. It's also interesting to me why the linker couldn't find the .so output, and it might be helpful for us to dig into it if you would like to share the logs when running `mlc_llm package`.
