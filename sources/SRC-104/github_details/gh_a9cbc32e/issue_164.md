# [Issue #164] Adding adiditonal arguments for rocprof

source: https://github.com/ROCm/rocprofiler-compute/issues/164
state: closed | updated: 2024-11-29T18:57:05Z
labels: enhancement, Under Investigation

## 正文

I'm trying to profile an application that does run-time code generation and that does some of its own internal rudimental profiling. As a result, I'd like to be able to start the profile only after a tracer start has been called, this is possible in rocprof, but I don't see a way to do that in onmiperf. 

Would it be possible to add an option to add additional arguments to rocprof from the omniperf cli?


## 评论 (2)

### sohaibnd · 2024-11-15

Hi @WillTrojak, sorry for the delay. Regarding profiling only after a tracer start has been called in rocprof, can you point me to where you saw this? If you are referring to using the [ROCTracer API](https://rocm.docs.amd.com/projects/rocprofiler/en/latest/how-to/using-rocprof.html#tracing-control-for-api-or-code-block), note that this specific to the application tracing mode (which is not relevant for omniperf) and not kernel profiling mode which is used by omniperf.

### sohaibnd · 2024-11-29

@WillTrojak I'm going to close this issue due to inactivity. If you have any follow-up questions, feel free to re-open this issue.
