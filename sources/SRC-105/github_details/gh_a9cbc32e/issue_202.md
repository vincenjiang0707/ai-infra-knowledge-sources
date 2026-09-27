# [Issue #202] Running `omniperf profile` after `omniperf profile --roof-only` erases all roofline pdfs

source: https://github.com/ROCm/rocprofiler-compute/issues/202
state: closed | updated: 2025-07-04T15:36:01Z
labels: bug, Profiling, Roofline, Under Investigation

## 正文

**Describe the bug**
If we profiled the application with `omniperf profile` and then obtained roofline chart PDFs using `omniperf profile --kernel-names --roof-only`, then we have both the profiling data and the roofline PDFs. If we reversed the order of these two operations, we lose the PDFs and legend. Could this be fixed that the user does not have to remember this ordering detail?

**Development Environment:**
 - Linux Distribution: SLES
 - Omniperf Version: 1.0.10
 - GPU: MI250X
 - Custer (if applicable): Frontier

**To Reproduce**
Steps to reproduce the behavior:
1. `omniperf profile -n new --roof-only --kernel-names --device 0 -- ./exe
          ^--- this will create the roofline PDFs and legend
2. `omniperf profile -n new --device 0 -- ./exe
          ^--- this will collect all other profiling data, but erase the PDFs collected in the previous step.

If you did the steps in the opposite order, we will have all profiling data intact.

**Expected behavior**
If we profile and collect different things in different commands but save to the same workload, nothing should be erased by subsequent profile steps unless the subsequent step collects the same info and has to overwrite the data collected. I can see how the second command above would have assumed that all roofline data collected earlier has to be overwritten.. but could we have the PDFs regenerated in this case?



## 评论 (4)

### ppanchad-amd · 2024-10-04

Hi @gsitaram. Internal ticket has been created to investigate your issue. Thanks!

### zichguan-amd · 2024-10-07

Hi @gsitaram, the default behaviour is to clear the workload directory if it exists during setup, see [this line](https://github.com/ROCm/omniperf/blob/fb210abcd0133586b0b96bbb99678b6ea8491ef0/src/omniperf_soc/soc_base.py#L206). If you run multiple workloads with the same name, the directory will be cleared in-between runs. This does not happen with the `--roof-only` flag so you should run the roofline after you have done the profiling.

### gsitaram · 2024-10-16

It is not a good idea to ask users to remember an order of issuing commands. I can think of some possibilities. Please comment on them.
- Instead of clearing an existing workload completely, warn the user or abort informing the user about the existence of that workload. Maybe we can add an option to force overwrite an output workload.
- If the tool is deciding to clear an existing workload assuming that the user may have used the same name by mistake, then is it possible to identify this particular situation that I reported? If the user did a `--roof-only` first, then can that be identified when running the second command? Clearly, `--roof-only` is the only way to generate those roofline PDFs and legends. The command in step 2 does not generate those. So, why erase them if they exist? 
  - If this situation is identifiable, could a warning can be presented to the user that those files are now going to be cleared and that they have to regenerate those? Or could those roofline plots could be left alone? Or could a command with the right set of options be recommended so that they can generate both the profiling data and the roofline plots?


### zichguan-amd · 2025-07-04

Hi @gsitaram, changes have been made to roofline generation, now roofline is generated in all profile mode cases unless `--no-roof` is used, see https://github.com/ROCm/rocprofiler-compute/commit/630bc149ff00c4d2b0c8ba2fa9ea4b94ceb98a37.
Closing the issue now as I believe this should address your concerns, please let me know if you think otherwise.
