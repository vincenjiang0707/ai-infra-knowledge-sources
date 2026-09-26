# [Issue #44] rocprofiler::counters::callback_thread_start does not issue pre_create/post_create callbacks

source: https://github.com/ROCm/rocprofiler-sdk/issues/44
state: closed | updated: 2025-05-07T18:57:47Z
labels: Under Investigation

## 正文

rocprofiler::counters::callback_thread_start does not issue pre_create/post_create callbacks in the rocm 6.4.0 AFAR VII.

This causes hpctoolkit to try to monitor a pthread created as part of context initialization. That causes deadlock because hpctoolkit is in the middle of rocprofiler initialization and is not in a state where it can start monitoring a created thread.

Below is a callstack snippet to show where this problem occurs.

```
#0  pthread_create (t=0x7fffffff83c0, a=0x0, s=0x7ffff5820940 <execute_native_thread_routine>, d=0x1280760) at ../src/hpcrun/foil/libc-preload.c:209
#1  0x00007ffff5820cdc in std::thread::_M_start_thread(std::unique_ptr<std::thread::_State, std::default_delete<std::thread::_State> >, void (*)()) ()
   from /projects/deploy/install/linux-rhel8-zen/gcc-8.5.0/gcc-12.3.0-divrsxygeh66lizjnxflsbszif3tfrr5/lib64/libstdc++.so.6
#2  0x00007fffe6a75edf in rocprofiler::counters::callback_thread_start() () from /opt/rocm-6.4.0/lib/librocprofiler-sdk.so.0
#3  0x00007fffe6a6e021 in rocprofiler::counters::start_context(rocprofiler::context::context const*) () from /opt/rocm-6.4.0/lib/librocprofiler-sdk.so.0
#4  0x00007fffe6a4ebc7 in rocprofiler::context::start_context(rocprofiler_context_id_t) () f
```

## 评论 (2)

### ppanchad-amd · 2025-02-10

Hi @jmellorcrummey. Internal ticket has been created to investigate this issue. Thanks!

### darren-amd · 2025-05-07

Hi @jmellorcrummey,

This has been fixed in 6.4, thanks for creating the ticket!
