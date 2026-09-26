# [Issue #1581] [Question] Instructions to contribute FPGA integration

source: https://github.com/mlc-ai/mlc-llm/issues/1581
state: open | updated: 2026-08-07T09:54:32Z
labels: question

## 正文

## ❓ General Questions

Hey I was wondering if you had any guidelines on how to integrate with other AI accelerators? Trying to figure out where is the low level code for this.

I want to make a FPGA compatible fork, mostly for fun/education, no guarantee I'll send a PR

Any guidelines on where I should look to do such integration or different steps would be super helpful thanks!



## 评论 (1)

### RyanX0198 · 2026-08-07

Following up on this integration question in light of the recent MLC/TVM runtime and FFI synchronization work: for a new accelerator, what is the most useful first upstreamable milestone today?

Would maintainers prefer (1) a TVM target/codegen plus runtime path, (2) an MLC device path that proves one reproducible model workload, (3) a BYOC/external-runtime integration, or (4) a smaller reference backend before broader model support?

What minimum evidence should accompany that first milestone—operator coverage, dynamic-shape behavior, numerical regression, profiling/debugging, CI hardware, or a named long-term maintainer? I am trying to understand the current project-side acceptance boundary before choosing an integration layer. @MasterJH5574
