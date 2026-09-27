# [Issue #3442] [Bug] MLC Chat crashes on Pixel 8 when loading prebuilt Llama 3.2 models

source: https://github.com/mlc-ai/mlc-llm/issues/3442
state: open | updated: 2026-03-06T14:27:23Z
labels: bug

## 正文

## 🐛 Bug

<!-- A clear and concise description of what the bug is. -->
When trying to run Llama-3.2 models on MLC-CHAT on my Google pixel 8, the app instantly crashes when initializing. I can use models like qwen and gemma but not Llama. Previously I was only trying to run Llama-3.2-1B-Instruct-q4f16_1-MLC but once it failed, I tried other versions to be sure. 

Models used.
Llama-3.2-1B-Instruct-q4f16_1-MLC
Llama-3.2-1B-Instruct-q0f16-MLC
Llama-3.2-3B-Instruct-q4f16_1-MLC

## To Reproduce

Steps to reproduce the behavior:

1. download the prebuilt package for MLC-LLM
2. Load any of the 3 models above in the config file
3. Open MLC on device and try to initialize the model.

Here is a snippet of the error message I get from logcat.

```
---------------------------- PROCESS STARTED (4591) for package ai.mlc.mlcchat ----------------------------
2026-03-02 21:49:10.472  4591-4591  re-initialized>         ai.mlc.mlcchat                       W  type=1400 audit(0.0:207234): avc:  granted  { execute } for  path="/data/data/ai.mlc.mlcchat/code_cache/startup_agents/4d42d08a-agent.so" dev="dm-64" ino=1755930 scontext=u:r:untrusted_app:s0:c243,c257,c512,c768 tcontext=u:object_r:app_data_file:s0:c243,c257,c512,c768 tclass=file app=ai.mlc.mlcchat
2026-03-02 21:49:10.479  4591-4591  nativeloader            ai.mlc.mlcchat                       D  Load /data/user/0/ai.mlc.mlcchat/code_cache/startup_agents/4d42d08a-agent.so using system ns (caller=<unknown>): ok
2026-03-02 21:49:10.484  4591-4591  ai.mlc.mlcchat          ai.mlc.mlcchat                       W  hiddenapi: DexFile /data/data/ai.mlc.mlcchat/code_cache/.studio/instruments-855ca6dc.jar is in boot class path but is not in a known location
2026-03-02 21:49:10.551  4591-4591  ai.mlc.mlcchat          ai.mlc.mlcchat                       W  Redefining intrinsic method java.lang.Thread java.lang.Thread.currentThread(). This may cause the unexpected use of the original definition of java.lang.Thread java.lang.Thread.currentThread()in methods that have already been compiled.
2026-03-02 21:49:10.551  4591-4591  ai.mlc.mlcchat          ai.mlc.mlcchat                       W  Redefining intrinsic method boolean java.lang.Thread.interrupted(). This may cause the unexpected use of the original definition of boolean java.lang.Thread.interrupted()in methods that have already been compiled.
2026-03-02 21:49:10.835  4591-4591  nativeloader            ai.mlc.mlcchat                       D  Configuring clns-9 for other apk /data/app/~~XqFmk8LXzFauzOggSmCmOA==/ai.mlc.mlcchat-RvV-uocj8Wo-hk3-MQynBw==/base.apk. target_sdk_version=35, uses_libraries=libOpenCL.so:libOpenCL-pixel.so, library_path=/data/app/~~XqFmk8LXzFauzOggSmCmOA==/ai.mlc.mlcchat-RvV-uocj8Wo-hk3-MQynBw==/lib/arm64:/data/app/~~XqFmk8LXzFauzOggSmCmOA==/ai.mlc.mlcchat-RvV-uocj8Wo-hk3-MQynBw==/base.apk!/lib/arm64-v8a, permitted_path=/data:/mnt/expand:/data/user/0/ai.mlc.mlcchat
2026-03-02 21:49:10.836  4591-4591  CompatChangeReporter    ai.mlc.mlcchat                       D  Compat change id reported: 202956589; UID 10499; state: ENABLED
2026-03-02 21:49:10.844  4591-4591  GraphicsEnvironment     ai.mlc.mlcchat                       V  Currently set values for:
2026-03-02 21:49:10.844  4591-4591  GraphicsEnvironment     ai.mlc.mlcchat                       V    angle_gl_driver_selection_pkgs=[com.android.angle, com.google.android.apps.tachyon]
2026-03-02 21:49:10.844  4591-4591  GraphicsEnvironment     ai.mlc.mlcchat                       V    angle_gl_driver_selection_values=[angle, native]
2026-03-02 21:49:10.844  4591-4591  GraphicsEnvironment     ai.mlc.mlcchat                       V  ai.mlc.mlcchat is not listed in per-application setting
2026-03-02 21:49:10.844  4591-4591  GraphicsEnvironment     ai.mlc.mlcchat                       V  ANGLE allowlist from config: 
2026-03-02 21:49:10.844  4591-4591  GraphicsEnvironment     ai.mlc.mlcchat                       V  No special selections for ANGLE, returning default driver choice
2026-03-02 21:49:10.844  4591-4591  GraphicsEnvironment     ai.mlc.mlcchat                       V  Neither updatable production driver nor prerelease driver is supported.
2026-03-02 21:49:10.865  4591-4761  DisplayManager          ai.mlc.mlcchat                       I  Choreographer implicitly registered for the refresh rate.
2026-03-02 21:49:10.866  4591-4761  vulkan                  ai.mlc.mlcchat                       D  searching for layers in '/data/app/~~XqFmk8LXzFauzOggSmCmOA==/ai.mlc.mlcchat-RvV-uocj8Wo-hk3-MQynBw==/lib/arm64'
2026-03-02 21:49:10.866  4591-4761  vulkan                  ai.mlc.mlcchat                       D  searching for layers in '/data/app/~~XqFmk8LXzFauzOggSmCmOA==/ai.mlc.mlcchat-RvV-uocj8Wo-hk3-MQynBw==/base.apk!/lib/arm64-v8a'
2026-03-02 21:49:10.877  4591-4591  DesktopExperienceFlags  ai.mlc.mlcchat                       D  Toggle override initialized to: false
2026-03-02 21:49:10.881  4591-4591  ashmem                  ai.mlc.mlcchat                       E  Pinning is deprecated since Android Q. Please use trim or other methods.
2026-03-02 21:49:10.891  4591-4591  System.err              ai.mlc.mlcchat                       W  Try loading tvm4j from native path.
2026-03-02 21:49:10.920  4591-4591  nativeloader            ai.mlc.mlcchat                       D  Load libtvm4j.so using class loader ns clns-9 (caller=/data/app/~~XqFmk8LXzFauzOggSmCmOA==/ai.mlc.mlcchat-RvV-uocj8Wo-hk3-MQynBw==/base.apk!classes7.dex): dlopen failed: library "libtvm4j.so" not found
2026-03-02 21:49:10.920  4591-4591  System.err              ai.mlc.mlcchat                       W  Try loading tvm4j-linux-x86_64 from native path.
2026-03-02 21:49:10.920  4591-4591  nativeloader            ai.mlc.mlcchat                       D  Load libtvm4j-linux-x86_64.so using class loader ns clns-9 (caller=/data/app/~~XqFmk8LXzFauzOggSmCmOA==/ai.mlc.mlcchat-RvV-uocj8Wo-hk3-MQynBw==/base.apk!classes7.dex): dlopen failed: library "libtvm4j-linux-x86_64.so" not found
2026-03-02 21:49:10.920  4591-4591  System.err              ai.mlc.mlcchat                       W  [WARN] TVM native library not found in path. Copying native library from the archive. Consider installing the library somewhere in the path (for Windows: PATH, for Linux: LD_LIBRARY_PATH), or specifying by Java cmd option -Djava.library.path=[lib path].
2026-03-02 21:49:10.921  4591-4591  System.err              ai.mlc.mlcchat                       W  Attempting to load libtvm4j.so
2026-03-02 21:49:10.922  4591-4591  System.err              ai.mlc.mlcchat                       W  [WARN] Couldn't find native library tvm4j.
2026-03-02 21:49:10.922  4591-4591  System.err              ai.mlc.mlcchat                       W  java.lang.UnsatisfiedLinkError: Couldn't find the resource libtvm4j.so
2026-03-02 21:49:10.922  4591-4591  System.err              ai.mlc.mlcchat                       W  	at org.apache.tvm.NativeLibraryLoader.extractResourceFileToTempDir(NativeLibraryLoader.java:129)
2026-03-02 21:49:10.922  4591-4591  System.err              ai.mlc.mlcchat                       W  	at org.apache.tvm.NativeLibraryLoader.loadLibrary(NativeLibraryLoader.java:88)
2026-03-02 21:49:10.922  4591-4591  System.err              ai.mlc.mlcchat                       W  	at org.apache.tvm.Base.<clinit>(Base.java:71)
2026-03-02 21:49:10.922  4591-4591  System.err              ai.mlc.mlcchat                       W  	at org.apache.tvm.Function.getGlobalFunc(Function.java:55)
2026-03-02 21:49:10.922  4591-4591  System.err              ai.mlc.mlcchat                       W  	at org.apache.tvm.Function.getFunction(Function.java:34)
2026-03-02 21:49:10.923  4591-4591  System.err              ai.mlc.mlcchat                       W  	at ai.mlc.mlcllm.JSONFFIEngine.<init>(JSONFFIEngine.java:24)
2026-03-02 21:49:10.923  4591-4591  System.err              ai.mlc.mlcchat                       W  	at ai.mlc.mlcllm.MLCEngine.<init>(MLCEngine.kt:33)
2026-03-02 21:49:10.923  4591-4591  System.err              ai.mlc.mlcchat                       W  	at ai.mlc.mlcchat.AppViewModel$ChatState.<init>(AppViewModel.kt:516)
2026-03-02 21:49:10.923  4591-4591  System.err              ai.mlc.mlcchat                       W  	at ai.mlc.mlcchat.AppViewModel.<init>(AppViewModel.kt:38)
2026-03-02 21:49:10.923  4591-4591  System.err              ai.mlc.mlcchat                       W  	at ai.mlc.mlcchat.MainActivity.onCreate(MainActivity.kt:76)
2026-03-02 21:49:10.923  4591-4591  System.err              ai.mlc.mlcchat                       W  	at android.app.Activity.performCreate(Activity.java:9306)
2026-03-02 21:49:10.923  4591-4591  System.err              ai.mlc.mlcchat                       W  	at android.app.Activity.performCreate(Activity.java:9284)
2026-03-02 21:49:10.923  4591-4591  System.err              ai.mlc.mlcchat                       W  	at android.app.Instrumentation.callActivityOnCreate(Instrumentation.java:1541)
2026-03-02 21:49:10.923  4591-4591  System.err              ai.mlc.mlcchat                       W  	at android.app.ActivityThread.performLaunchActivity(ActivityThread.java:4480)
2026-03-02 21:49:10.923  4591-4591  System.err              ai.mlc.mlcchat                       W  	at android.app.ActivityThread.handleLaunchActivity(ActivityThread.java:4699)
2026-03-02 21:49:10.923  4591-4591  System.err              ai.mlc.mlcchat                       W  	at android.app.servertransaction.LaunchActivityItem.execute(LaunchActivityItem.java:224)
2026-03-02 21:49:10.923  4591-4591  System.err              ai.mlc.mlcchat                       W  	at android.app.servertransaction.TransactionExecutor.executeNonLifecycleItem(TransactionExecutor.java:133)
2026-03-02 21:49:10.923  4591-4591  System.err              ai.mlc.mlcchat                       W  	at android.app.servertransaction.TransactionExecutor.executeTransactionItems(TransactionExecutor.java:103)
2026-03-02 21:49:10.923  4591-4591  System.err              ai.mlc.mlcchat                       W  	at android.app.servertransaction.TransactionExecutor.execute(TransactionExecutor.java:80)
2026-03-02 21:49:10.923  4591-4591  System.err              ai.mlc.mlcchat                       W  	at android.app.ActivityThread$H.handleMessage(ActivityThread.java:2961)
2026-03-02 21:49:10.923  4591-4591  System.err              ai.mlc.mlcchat                       W  	at android.os.Handler.dispatchMessage(Handler.java:132)
2026-03-02 21:49:10.923  4591-4591  System.err              ai.mlc.mlcchat                       W  	at android.os.Looper.dispatchMessage(Looper.java:333)
2026-03-02 21:49:10.923  4591-4591  System.err              ai.mlc.mlcchat                       W  	at android.os.Looper.loopOnce(Looper.java:263)
2026-03-02 21:49:10.923  4591-4591  System.err              ai.mlc.mlcchat                       W  	at android.os.Looper.loop(Looper.java:367)
2026-03-02 21:49:10.923  4591-4591  System.err              ai.mlc.mlcchat                       W  	at android.app.ActivityThread.main(ActivityThread.java:9287)
2026-03-02 21:49:10.923  4591-4591  System.err              ai.mlc.mlcchat                       W  	at java.lang.reflect.Method.invoke(Native Method)
2026-03-02 21:49:10.923  4591-4591  System.err              ai.mlc.mlcchat                       W  	at com.android.internal.os.RuntimeInit$MethodAndArgsCaller.run(RuntimeInit.java:566)
2026-03-02 21:49:10.923  4591-4591  System.err              ai.mlc.mlcchat                       W  	at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:929)
2026-03-02 21:49:10.923  4591-4591  System.err              ai.mlc.mlcchat                       W  Try to load tvm4j (runtime packed version) ...
2026-03-02 21:49:10.972  4591-4591  nativeloader            ai.mlc.mlcchat                       D  Load /data/app/~~XqFmk8LXzFauzOggSmCmOA==/ai.mlc.mlcchat-RvV-uocj8Wo-hk3-MQynBw==/base.apk!/lib/arm64-v8a/libtvm4j_runtime_packed.so using class loader ns clns-9 (caller=/data/app/~~XqFmk8LXzFauzOggSmCmOA==/ai.mlc.mlcchat-RvV-uocj8Wo-hk3-MQynBw==/base.apk!classes7.dex): ok
2026-03-02 21:49:10.972  4591-4591  System.err              ai.mlc.mlcchat                       W  libtvm4j loads successfully.
2026-03-02 21:49:11.267  4591-4591  Activity                ai.mlc.mlcchat                       V  No requestable permission in the request.
2026-03-02 21:49:11.271  4591-4591  CompatChangeReporter    ai.mlc.mlcchat                       D  Compat change id reported: 309578419; UID 10499; state: ENABLED
2026-03-02 21:49:11.271  4591-4591  DesktopModeFlags        ai.mlc.mlcchat                       D  Toggle override initialized to: OVERRIDE_UNSET
2026-03-02 21:49:11.278  4591-4591  ContentCaptureHelper    ai.mlc.mlcchat                       I  Setting logging level to OFF
2026-03-02 21:49:11.289  4591-4591  CompatChangeReporter    ai.mlc.mlcchat                       D  Compat change id reported: 349153669; UID 10499; state: ENABLED
2026-03-02 21:49:11.463  4591-4591  VRI[MainActivity]       ai.mlc.mlcchat                       D  WindowInsets changed: 1080x2400 statusBars:[0,132,0,0] navigationBars:[0,0,0,63] mandatorySystemGestures:[0,164,0,84] 
2026-03-02 21:49:11.463  4591-4591  WindowOnBackDispatcher  ai.mlc.mlcchat                       D  setTopOnBackInvokedCallback (unwrapped): android.view.ViewRootImpl$$ExternalSyntheticLambda12@88eca82
2026-03-02 21:49:11.481  4591-4591  Permissions             ai.mlc.mlcchat                       D  android.permission.CAMERA = false
2026-03-02 21:49:11.512  4591-4595  ai.mlc.mlcchat          ai.mlc.mlcchat                       I  Compiler allocated 5145KB to compile void android.view.ViewRootImpl.performTraversals()
2026-03-02 21:49:11.526  4591-4591  HWUI                    ai.mlc.mlcchat                       I  Using FreeType backend (prop=Auto)
2026-03-02 21:49:11.762  4591-4591  InsetsController        ai.mlc.mlcchat                       D  hide(ime())
2026-03-02 21:49:11.763  4591-4591  ImeTracker              ai.mlc.mlcchat                       I  ai.mlc.mlcchat:19788897: onCancelled at PHASE_CLIENT_ALREADY_HIDDEN
2026-03-02 21:49:12.674  4591-4591  WindowOnBackDispatcher  ai.mlc.mlcchat                       W  OnBackInvokedCallback is not enabled for the application.
                                                                                                    Set 'android:enableOnBackInvokedCallback="true"' in the application manifest.
2026-03-02 21:49:12.845  4591-4596  ai.mlc.mlcchat          ai.mlc.mlcchat                       W  userfaultfd: MOVE ioctl seems unsupported: Try again
2026-03-02 21:49:17.150  4591-5551  ProfileInstaller        ai.mlc.mlcchat                       D  Installing profile for ai.mlc.mlcchat
2026-03-02 21:49:21.079  4591-4591  VRI[MainActivity]       ai.mlc.mlcchat                       D  WindowInsets changed: navigationBars:null mandatorySystemGestures:[0,164,0,0] 
2026-03-02 21:49:25.119  1599-2214  InputDispatcher         system_server                        E  channel 'cfbc49c ai.mlc.mlcchat/ai.mlc.mlcchat.MainActivity' ~ Channel is unrecoverably broken and will be disposed!
---------------------------- PROCESS ENDED (4591) for package ai.mlc.mlcchat ----------------------------

```

## Environment

 - Platform (e.g. WebGPU/Vulkan/IOS/Android/CUDA): Android 16
 - Operating system (e.g. Ubuntu/Windows/MacOS/...): Ubuntu
 - Device (e.g. iPhone 12 Pro, PC+RTX 3090, ...) Pixel 8
 - How you installed MLC-LLM (`conda`, source):  conda, https://mlc.ai/wheels mlc-llm-nightly-cpu mlc-ai-nightly-cpu

 - How you installed TVM (`pip`, source):
 - Python version (e.g. 3.10): 3.13
 - GPU driver version (if applicable): none
 - CUDA/cuDNN version (if applicable):
 - TVM Hash Tag (`python -c "import tvm; print('\n'.join(f'{k}: {v}' for k, v in tvm.support.libinfo().items()))"`, applicable if you compile models):
 - Any other relevant information:

## Additional context
https://huggingface.co/mlc-ai/Llama-3.2-1B-Instruct-q4f16_0-MLC
https://huggingface.co/mlc-ai/Llama-3.2-3B-Instruct-q4f16_0-MLC
https://huggingface.co/mlc-ai/Llama-3.2-1B-Instruct-q4f16_1-MLC
<!-- Add any other context about the problem here. -->


## 评论 (3)

### MasterJH5574 · 2026-03-03

Hi @Grodoe thank you for reporting this.  We couldn't reproduce the issue on Pixel 7.   Could you please confirm that `python -m mlc_llm package` finishes successfully?

### Grodoe · 2026-03-03

Yes, here is the code snippet of running the command

```text
[2026-03-03 12:53:03] INFO prepare_libs.py:58: Running cmake build [ 0%] Built target tokenizers_c [ 0%] Built target tvm4j_core [ 0%] Built target tvm_libinfo_objs [ 12%] Built target tvm_ffi_objs [ 12%] Built target tvm_ffi_static [ 36%] Built target tvm_runtime_objs [ 60%] Built target sentencepiece-static [ 64%] Built target tvm_runtime [ 68%] Built target tokenizers_cpp [ 96%] Built target mlc_llm_objs [100%] Built target mlc_llm_static [100%] Building CXX object CMakeFiles/tvm4j_runtime_packed.dir/home/gordon-linux/mlc-llm/3rdparty/tvm/jvm/native/src/main/native/org_apache_tvm_native_c_api.cc.o [100%] Linking CXX shared library libtvm4j_runtime_packed.so [100%] Built target tvm4j_runtime_packed [2026-03-03 12:54:43] INFO prepare_libs.py:73: Running cmake install Install the project... -- Install configuration: "Release" -- Up-to-date: /home/gordon-linux/mlc-llm/android/MLCChat/build/output/tvm4j_core.jar -- Installing: /home/gordon-linux/mlc-llm/android/MLCChat/build/output/arm64-v8a/libtvm4j_runtime_packed.so [2026-03-03 12:54:44] INFO package.py:281: Clean up all directories under "dist/lib/mlc4j" [2026-03-03 12:54:44] INFO package.py:288: Copying "/home/gordon-linux/mlc-llm/android/mlc4j/src" to "dist/lib/mlc4j/src" [2026-03-03 12:54:44] INFO package.py:293: Copying "/home/gordon-linux/mlc-llm/android/mlc4j/build.gradle" to "dist/lib/mlc4j/build.gradle" [2026-03-03 12:54:44] INFO package.py:298: Copying "build/output" to "dist/lib/mlc4j/output" [2026-03-03 12:54:44] INFO package.py:304: Moving "dist/bundle/mlc-app-config.json" to "dist/lib/mlc4j/src/main/assets/mlc-app-config.json" [2026-03-03 12:54:44] INFO package.py:401: All finished.
```

the ends with "All finished" and exits cleanly with no error. All the other models in the config run except for the Llama models

### MasterJH5574 · 2026-03-06

Thanks for confirming. We will look into the llama model.
