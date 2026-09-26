# [Issue #181] Delimiters to profile blocks of application code

source: https://github.com/ROCm/rocprofiler-compute/issues/181
state: closed | updated: 2025-08-06T18:38:25Z
labels: Omniperf Revamp

## 正文

**Describe the suggestion**
Allow breakpoint/delimiters to specify "blocks" for profiling in application source code

**Justification**
This came up in the context of training ML models and enabling users to target specific stages in their ML training pipeline. In these multi-stage codes it would be helpful for users to understand performance and bottlenecks in different areas of execution

**Implementation**
There's a few ways this could be done, but the first that comes to mind is by leveraging rocscope. A modified version of the rocomni plugin could be used to gather counters for these user-defined blocks.

See internal planning page for more info...

**Additional Notes**
This would also lend itself nicely to an eventual VSCode extension

_Originally posted by @coleramos425 in https://github.com/AMDResearch/omniperf/discussions/153#discussioncomment-6846892_

## 评论 (3)

### jrmadsen · 2023-08-29

This would be easily supportable with working `hipProfilerStart()` and `hipProfilerStop()` functions. I’ll make sure those functions are actually handled properly in rocprofiler v2. 

### systems-assistant[bot] · 2025-08-06

This issue has been migrated to: https://github.com/ROCm/rocm-systems/issues/76

### amd-hsivasun · 2025-08-06

Imported to ROCm/rocm-systems
