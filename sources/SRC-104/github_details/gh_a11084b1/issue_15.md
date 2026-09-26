# [Issue #15] [Issue]: Problems with "agent profiling" mode in Rocprofiler-SDK

source: https://github.com/ROCm/rocprofiler-sdk/issues/15
state: closed | updated: 2025-01-30T15:09:46Z
labels: Under Investigation

## 正文

### Problem Description

A) I only get non-zero values for the first event that I have added to
the profile.

B) I start two agents for two distinct GPUs, I submit my kernel on
only one GPU, but I get the same measurements from both agents.

C) When I get the measurements I have no way of distinguishing which
measurement came from which agent.

D) When using watermark equal to zero, the buffer callback is triggered as soon as there is one entry in the buffer, but before all the entries have been in the buffer. As a result we see the entries "out of order." We would like the data to be accessible synchronously when we get a sample without having to go through buffers. 

### Operating System

Rocky Linux 9.4 (Blue Onyx)

### CPU

AMD EPYC 7413 24-Core Processor

### GPU

AMD Instinct MI210

### ROCm Version

ROCm 6.2.0

### ROCm Component

rocprofiler

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_

## 评论 (12)

### bwelton · 2024-09-13

I suspect A/B may be related. Can you post the code where you call rocprofiler_configure_agent_profile_counting_service?

C has an internal patch that resolves this issue that should be published shortly. D has a patch in the works that should be available soon. 

### adanalis · 2024-09-25

In addition to the problems discussed above, I'm now getting a segfault inside rocprof-sdk code.
I created a PR in the PAPI repo that enables the agent profiling mode and comes with tests. The PR is here:
https://github.com/icl-utk-edu/papi/pull/249

To reproduce the segfault please do the following:

1) clone PAPI, go into the directory "$papi_root/src" and run
./configure --with-components=rocp_sdk

2) run make

3) export RPSDK_MODE_AGENT_PROFILE=1

4) go to $papi_root/src/components/rocp_sdk/tests

5) run ./advanced

Here is the backtrace from my runs:
#0  0x00007fffebc3d819 in rocr::HSA::hsa_signal_store_relaxed(hsa_signal_s, long) ()
   from /apps/rocm/rocm-6.3afar6/lib/llvm/bin/../../../lib/libhsa-runtime64.so.1
#1  0x00007fffeb87648e in rocprofiler::counters::read_agent_ctx(rocprofiler::context::context const*, rocprofiler_user_data_t, rocprofiler_counter_flag_t) () from /apps/rocm/rocm-6.3afar6/lib/librocprofiler-sdk.so
#2  0x00000000004a90d7 in papi_rocpsdk::read_sample () at components/rocp_sdk/sdk_class.cpp:632
#3  0x00000000004a9f7d in rocprofiler_sdk_ctx_read (ctx=0xc18410, counters=0x7fffffff6ac8) at components/rocp_sdk/sdk_class.cpp:1110
#4  0x000000000047d23f in _papi_hwi_read (context=<optimized out>, ESI=ESI@entry=0x655710, values=values@entry=0x7fffffff6b90)
    at papi_internal.c:1713
#5  0x000000000047866c in PAPI_read (EventSet=<optimized out>, values=0x7fffffff6b90) at papi.c:3127
#6  0x0000000000476e4f in main ()


### darren-amd · 2025-01-02

Hi @adanalis,

I gave the code a try and was able to run the highlighted example successfully on ROCm 6.3 with a few changes. Firstly, we transitioned from agent_profile to agent_profile_counting_service with a change to the docs here: https://github.com/ROCm/rocprofiler-sdk/commit/4204042ac6358abc0b8f2cabc2efe3b436bc3811. You can run the command:

`"find . -type f -exec sed -i 's/rocprofiler_agent_profile_callback_t/rocprofiler_device_counting_service_callback_t/g; s/rocprofiler_configure_agent_profile_counting_service/rocprofiler_configure_device_counting_service/g; s/agent_profile.h/device_counting_service.h/g; s/rocprofiler_sample_agent_profile_counting_service/rocprofiler_sample_device_counting_service/g' {} +"` to do the renaming of the functions for you.

Additionally, there was a change to rocprofiler_sample_device_counting_service to allow returning data as a part of the API call: [Change to API](https://github.com/ROCm/rocprofiler-sdk/commit/253c9adfc17d0ede33cadc79515d2c2bd2b18ebc#diff-2a59544f9219b48330bf58e8b310d53120e5000645ae59e84ef14ace77130725L118). You need to change line 56 in sdk_class.cpp to
```
typedef rocprofiler_status_t (* rocprofiler_sample_device_counting_service_t) (rocprofiler_context_id_t context_id,
rocprofiler_user_data_t user_data,
rocprofiler_counter_flag_t flags,
rocprofiler_record_counter_t * output_records,
unsigned long * rec_count );
```

and the read_sample() function to:
   ```
 int ret_val = rocprofiler_sample_device_counting_service_FPTR(
                get_client_ctx(),
                {},
                ROCPROFILER_COUNTER_FLAG_NONE,
                nullptr,
                nullptr);
```

I also had to set `PAPI_ROCP_SDK_ROOT` to `/opt/rocm`.

I can push the code to your branch if you'd like. Please give that a try and let me know if you run into any issues, thanks!

### adanalis · 2025-01-03

Thanks for your comments. I have since updated the code significantly and have incorporated the API changes you mentioned. You can find the latest version at my fork of PAPI under the branch 2024.06.rocprof_sdk:

https://github.com/adanalis/papi/tree/2024.06.rocprof_sdk

### darren-amd · 2025-01-06

Awesome! Are you running into any more issues?

### adanalis · 2025-01-07

The AMD internal repo has fixed most issues. However, the code released in 6.3.1 still has problems in device profiling mode. The only remaining issue that we are aware of is a core dump caused by DumpStackTraceAndExit() when the program exits abnormally.

### darren-amd · 2025-01-07

Hi @adanalis,

What problems are you facing with device profiling mode? Could you provide the code that you're running into issues with? Thanks!

### adanalis · 2025-01-09

The code can be accessed here: https://github.com/icl-utk-edu/papi/pull/249

Setting the env variable RPSDK_MODE_AGENT_PROFILE=1 and running any of the tests under src/components/rocp_sdk/tests will result in zero values when using rocm-6.3.1, but correct values when using the container with the latest internal code. The culprit is the following call:

    ret_val = rocprofiler_sample_device_counting_service_FPTR(
                get_client_ctx(), {}, ROCPROFILER_COUNTER_FLAG_NONE,
                output_records, &rec_count);
 
Specifically, when I enable debugging output, I see that with 6.3.1 I get results such as:
 output_records[0].id: 269358112 -> counter_id: 0 Value= 0.000000
 output_records[1].id: 140437274450893 -> counter_id: 0 Value= 0.000000
 output_records[2].id: 140437419585632 -> counter_id: 0 Value= -95464729768441765169582325556663888886439126050506914520428295204372480.000000
 output_records[3].id: 0 -> counter_id: 0 Value= 0.000000 
 output_records[4].id: 2 -> counter_id: 0 Value= 0.000000 

versus the same code built with the container prints:
 output_records[0].id: 174514485560606720 -> counter_id: 620 Value= 306521271.000000
 output_records[1].id: 174514485560610816 -> counter_id: 620 Value= 306521271.000000
 output_records[2].id: 174514485560614912 -> counter_id: 620 Value= 306521271.000000
 output_records[3].id: 174514485560619008 -> counter_id: 620 Value= 306521271.000000
 output_records[4].id: 174514485560623104 -> counter_id: 620 Value= 306521271.000000

### darren-amd · 2025-01-09

Interesting, are you building the latest code directly from the amd-mainline branch? Perhaps there was a patch that hasn't been cherry picked into release yet, let me check with the team.

### adanalis · 2025-01-10

I have a container that Benjamin Welton built for us from the AMD repo.

### darren-amd · 2025-01-17

Hi @adanalis,

The fix for the above issue should be in the next minor release, ROCm 6.3.2. Please let me know if there are any other issues I can help with, thanks!

### darren-amd · 2025-01-30

I'm going to close this ticket, but please feel free to create another one if you run into issues in the future, thanks!
