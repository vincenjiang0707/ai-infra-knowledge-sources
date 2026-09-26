# [Issue #37] [Feature]: Initialize Both The HIP Compiler Table and The HIP Dispatch Tables On the First Call To Any HIP C-API Function

source: https://github.com/ROCm/rocprofiler-sdk/issues/37
state: closed | updated: 2025-01-31T20:04:47Z
labels: Feature Request

## 正文

### Suggestion Description

In our use-case, we have a rocprofiler-sdk tool which links to the HIP runtime to load device code on the GPU for dynamic binary instrumentation, while the target application relies on a non-HIP runtime (e.g. HSA/OpenCL/OpenMP). The tool uses rocprofiler-sdk to obtain all currently possible API tables: ROCr, HIP Compiler, and HIP Dispatch. Here, by explicit calls I mean calling APIs without using the API table obtained via rocprofiler-sdk, e.g. `hipMalloc(...)` instead of `myHIPDispatchApiTable.hipMalloc(...)`.

In this scenario, HIP is only present for the sake of the tool, and the target application does not use HIP in any shape or form. 
Since the tool is linked with the HIP runtime, the tool makes the first explicit HIP call to the compiler table (i.e. `__hipRegisterFatBinary`), causing 
the compiler table to be registered with rocprofiler-sdk. However, since there are no direct calls to HIP runtime API functions on the application side, and the tool is written to not make any explicit calls to the HIP runtime API, the Runtime table will never get registered with the tool.

I have a potential use-case around this issue, which is to make an explicit call on the tool side to the most harmless HIP runtime API function `hipApiName` to trigger the initialization of the table, but I think this is slightly ugly. At the same time I was wondering if HIP's API table registration can be changed so that both the HIP Compiler table and the HIP Dispatch tables get registered on any call to a HIP C-API (regardless of the API being listed under the compiler table or the dispatch table). 


CC: @bwelton @vlaindic @jrmadsen 

### Operating System

_No response_

### GPU

_No response_

### ROCm Component

CLR

## 评论 (14)

### jrmadsen · 2025-01-15

Hi @matinraayai, I do not really support this proposal. When an API table gets registered, there is a runtime initialization tracing service that can be used to identify “runtime X is being used by the application”. If any part of the application contains HIP device code, whenever that shared object gets loaded, there will be a call to register the fat binary. Thus, you will get a runtime initialization callback for the HIP compiler API that you can infer to mean that HIP device code exists _but_ that does not mean that any of the HIP runtime is _actually used by the application_ — the application might just have some HIP device code somewhere for when AMD GPU offloading is available but the application may entirely run on the CPU because there are not any AMD GPUs on the system. The application cannot control the HIP compiler API from being used but it can control whether it uses the HIP runtime API. In this scenario, it would incorrect to report that the HIP runtime API has been initialized. 

### jrmadsen · 2025-01-15

I would also like to note that it was an intentional design decision to not allow tools to make calls to the runtimes within the tool, _especially_ during tool initialization. Doing so is undefined behavior — in some cases, it may work but in others, it will result in a deadlock. 

### matinraayai · 2025-01-15

@jrmadsen thanks for the explanation, I agree regarding why HIP compiler and runtime tables are kept separate. 
What I'm looking for is the "correct way' to handle this specific use-case i.e. trigger the registration of the HIP runtime API on the tool side when the application is not using it.

> I would also like to note that it was an intentional design decision to not allow tools to make calls to the runtimes within the tool, _especially_ during tool initialization. Doing so is undefined behavior — in some cases, it may work but in others, it will result in a deadlock.

I'm confused; Are you saying tools are not allowed to make HIP/HSA calls through the API tables in any circumstances? I understand that it should not be done during tool initialization, at least not until rocprofiler-sdk has provided the API tables, but there's simply no way around calling HSA/HIP APIs on the tool side.



### jrmadsen · 2025-01-15

> Are you saying tools are not allowed to make HIP/HSA calls through the API tables in any circumstances?

No, calling through the API tables is safe. I’m referring to calling the API directly through their public API as one would in an application. 

### matinraayai · 2025-01-15

@jrmadsen that makes sense; I guess the only thing I'm not clear about is how to:
1. Detect if the application is not using the HIP runtime.
2. Triggering the initialization of the HIP runtime on the tool side if HIP is not used by the application.

### matinraayai · 2025-01-24

@jrmadsen the only way I have right now to get around this issue, is to check if the HIP dispatch table has been initialized by the app right before the first packet is submitted to an HSA Queue; If not, I trigger the initialization of the HIP dispatch table myself on the tool side via calling `hipApiName` directly. This is better than doing this during tool initialization, but I think concerns about deadlock will still remain. I can also introduce a flag in my tool, so that the user can trigger this explicitly if they know the application being instrumented does not depend on HIP.

Without a good workaround, I'll be forced to write my own GPU code loader instead of relying on the HIP runtime, which is sub-optimal. 

### jrmadsen · 2025-01-26

How are you loading your tool into the application? If it is via LD_PRELOAD, you could wrap `__libc_start_main` and before invoking the main function, force rocprofiler-sdk initialization if necessary (although it might not be necessary bc of the `__hipRegisterFatBinary` call), and then invoke `hipApiName` to force loading the HIP runtime. With this strategy, there is no danger of deadlock since you aren’t calling HIP within the call-stack of rocprofiler-sdk. 

### matinraayai · 2025-01-27

That's a good idea. A set of follow up questions on this:
1. ~~Does `__libc_start_main` of rocprofiler tools get manipulated by rocprofiler-sdk in any way?~~ Rocprofiler-sdk-tool  manipulates the `__libc_start_main` function it seems. I've experienced some weird bugs where static initialization function of my tool doesn't get invoked when instrumenting some ROCm applications, and I was wondering if I can fix it somehow by introducing my own `__libc_start_main` function .
2. If the concern is not interfering with the rocprofiler-sdk call stack, I might be able to get away with initializing HIP right before the first packet is dispatched. Note that I don't use any rocprofiler-sdk services to view the packets, I manually replace all HSA queues with intercept queues in my tool. Here is the stack trace from rocgdb when I get to my packet submission callback in my tool:
```
#6  0x00007ffff20555fa in queueSubmitWriteInterceptor (Packets=0x7fffe4300040, PktCount=1, UserPktIndex=1, Data=0x7fffe7e46000, Writer=0x7fffe8672c60)
    at /home/matinraayai/Projects/Luthier/build-new-luthier-dev/src/lib/hsa/HsaRuntimeInterceptor.cpp:55
#7  0x00007fffe86735d0 in ?? () from /opt/rocm/lib/libhsa-runtime64.so.1
#8  0x00007fffe8665ddf in ?? () from /opt/rocm/lib/libhsa-runtime64.so.1
#9  0x00007ffff6d3beba in ?? () from /opt/rocm/lib/libamdhip64.so.6
#10 0x00007ffff6d38441 in ?? () from /opt/rocm/lib/libamdhip64.so.6
#11 0x00007ffff6d38b91 in ?? () from /opt/rocm/lib/libamdhip64.so.6
#12 0x00007ffff6cf4239 in ?? () from /opt/rocm/lib/libamdhip64.so.6
#13 0x00007ffff6bd4625 in ?? () from /opt/rocm/lib/libamdhip64.so.6
#14 0x00007ffff6c052e3 in ?? () from /opt/rocm/lib/libamdhip64.so.6
#15 0x00007ffff6bd4abe in ?? () from /opt/rocm/lib/libamdhip64.so.6
#16 0x00007ffff6be03dc in ?? () from /opt/rocm/lib/libamdhip64.so.6
#17 0x0000000000202782 in main ()
```
In the stack trace, rocprofiler-sdk is not present (at least not visible), so I might be able to get away with initializing HIP when I reach my packet interceptor function, unless invoking rocprofiler-sdk here might also cause a deadlock.

### matinraayai · 2025-01-27

@jrmadsen in addition, I have issues with some exit handlers of my library running sooner than rocprofiler-sdk's finalize(), causing issues when I try to print some of my static variables under the `rocprofiler_finalize` function.

### jrmadsen · 2025-01-27

Rocprofiler-SDK does not overload `__libc_start_main`, rocprofv3 does. 

You can fill in those backtraces by installing the `<package-name>-dbgsym` package but rocprofiler-sdk is not in that backtrace. 

If you provide an init function, we will provide you a function pointer to explicitly invoke finalization for your tool. You can also provide a function pointer which we will invoke when we finalize. It’s all in the docs for the return type of `rocprofiler_configure`

### matinraayai · 2025-01-28

> Rocprofiler-SDK does not overload `__libc_start_main`, rocprofv3 does.
> 
> You can fill in those backtraces by installing the `<package-name>-dbgsym` package but rocprofiler-sdk is not in that backtrace.
> 
> If you provide an init function, we will provide you a function pointer to explicitly invoke finalization for your tool. You can also provide a function pointer which we will invoke when we finalize. It’s all in the docs for the return type of `rocprofiler_configure`

I'm already doing this:
```c++
  ClientID->name = ToolName.data();
  rocprofiler_at_intercept_table_registration(
      luthier::apiRegistrationCallback,
      ROCPROFILER_HSA_TABLE | ROCPROFILER_HIP_COMPILER_TABLE |
          ROCPROFILER_HIP_RUNTIME_TABLE,
      nullptr);

  static auto Cfg = rocprofiler_tool_configure_result_t{
      sizeof(rocprofiler_tool_configure_result_t), nullptr,
      &luthier::rocprofilerFinalize, nullptr};
  return &Cfg;
```
I was expecting `luthier::rocprofilerFinalize` to be invoked before the exit handlers of my tool gets called, but it seems that the static variable destructors get called before rocprofiler-sdk's `finalize` is called. I'm not sure if I'm doing something wrong here.

### jrmadsen · 2025-01-28

```cpp
  static auto Cfg = rocprofiler_tool_configure_result_t{
      sizeof(rocprofiler_tool_configure_result_t), &luthier::rocprofilerInitialize,
      &luthier::rocprofilerFinalize, nullptr};
```

If you provide the initialize function, that function contains a function you can call to force your finalize function to be called

### matinraayai · 2025-01-28

> static auto Cfg = rocprofiler_tool_configure_result_t{
>       sizeof(rocprofiler_tool_configure_result_t), &luthier::rocprofilerInitialize,
>       &luthier::rocprofilerFinalize, nullptr};
> 
> If you provide the initialize function, that function contains a function you can call to force your finalize function to be called
I tried doing this, similar to both the rocprofiler-sdk samples and the rocprofv3 tooling.cpp: I stored the function pointer and my client id and added them to the `atexit` handlers. The issue still persists.
For now I'm avoiding any statically initialized globals and allocate every global variable on the heap to avoid any of these issues until I can figure out what exactly is the issue.

### matinraayai · 2025-01-31

@jrmadsen I was able to implement the hip initialization workaround in my tool as it did not interfere with rocprofiler-sdk's call stack. I will re-open this issue if I see any deadlocks occurring. 
With regards to invoking the finalizer, for now I'm avoiding creating any global static variables besides pointers that I explicitly manage through `new` and `delete` on the tool side, which has fixed my issues with the static destructors being called prematurely. I will create a separate issue for this in the future if I encounter it again.
Thanks for the help!
