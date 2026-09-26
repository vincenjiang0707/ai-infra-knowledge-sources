# [Issue #1378] Some points to make life easier for new submitters to submit to MLPerf inference

source: https://github.com/mlcommons/inference/issues/1378
state: closed | updated: 2026-05-13T00:44:18Z
labels: Stale

## 正文

- [ ] Reference implementations are not practically usable- while it is not practical to support all the hardware ideally we should have an object-oriented device where a new submitter should be able to extend the device class to add a new device
- [ ] The reference implementation should support dynamic batch sizes and quantization as most submissions need them - it is hard for all the submitters to manage these, especially across all the MLPerf inference tasks
- [ ] The reference implementation should support scalability (CPU cores/ number of GPUs)
- [x] We have a new submitter orientation but usually the most critical points get lost. We should have a checklist for new submitters - our [taskforce on automation and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md) can create this. 

Please feel free to add any more points which can help a new submitter. 

## 评论 (9)

### arjunsuresh · 2023-05-25

@mrmhodak I have added some of the points which I believe are useful for new inference submitters. Can you please review?

### mrmhodak · 2023-05-30

@arjunsuresh: These are great points! For now, I am adding to the agenda tomorrow and we should definitely work on these.

### psyhtest · 2023-06-20

> Reference implementations are not practically usable- while it is not practical to support all the hardware ideally we should have an object oriented device where a new submitter should be able to extend the device class to add a new device

We at KRAI are busy adding new backends to our [KILT](https://www.linkedin.com/pulse/laying-bare-whats-under-kilt-krai/) codebase, which we released under a permissive open-source license after the v3.0 round.

>  The reference implementation should support scalability (CPU cores/ number of GPUs)

KILT has been used to produce some of the fastest and most energy efficient results in the history of MLPerf (with up to 18 Qualcomm Cloud AI 100 accelerators).

I believe KILT would satisfy at least these points and more with community contributions. If there is sufficient interest, we would consider making it an official MLCommons project, like [Collective Knowledge](https://github.com/mlcommons/ck).

### gfursin · 2023-06-20

> > Reference implementations are not practically usable- while it is not practical to support all the hardware ideally we should have an object oriented device where a new submitter should be able to extend the device class to add a new device
> 
> We at KRAI are busy adding new backends to our [KILT](https://www.linkedin.com/pulse/laying-bare-whats-under-kilt-krai/) codebase, which we released under a permissive open-source license after the v3.0 round.
> 
> > The reference implementation should support scalability (CPU cores/ number of GPUs)
> 
> KILT has been used to produce some of the fastest and most energy efficient results in the history of MLPerf (with up to 18 Qualcomm Cloud AI 100 accelerators).
> 
> I believe KILT would satisfy at least these points and more with community contributions. If there is sufficient interest, we would consider making it an official MLCommons project, like [Collective Knowledge](https://github.com/mlcommons/ck).

Thank you @psyhtest. I think KILT will be useful particularly if it supports more hardware backends other than Qualcomm. In fact, we plan to integrate KILT with our Collective Knowledge workflows as an [open MLPerf inference v3.1 challenge](https://github.com/mlcommons/ck/tree/master/cm-mlops/challenge/optimize-mlperf-inference-v3.1-kilt-2023) . Please feel free to join this effort!


### gfursin · 2023-06-20

By the way, @psyhtest, if it's of interest, we already have a project at MLCommons related to KILT (Thomas Zhu, a student from Oxford University, worked with our MLCommons Task Force on Automation and Reprodicibility to provide a first implementation): 
* https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-inference-cpp
* https://github.com/mlcommons/ck/blob/master/cm-mlops/script/app-mlperf-inference-cpp/README-extra.md

It will be interesting to compare it with KILT and extend if needed.

Also, if I am correct, a few companies mentioned during inference v3.0 press briefing that they will release their own open-source and universal C++ implementation of MLPerf benchmarks for inference v3.1. 

Our Task Force will be happy to help consolidate these efforts under existing MLCommons projects and integrate them with our MLCommons CK/CM workflow automation. Looking forward to collaboration!


### psyhtest · 2023-06-20

> I think KILT will be useful particularly if it supports more hardware
> backends other than Qualcomm. 

We are planning to release more backends after the v3.1 round. Some necessary code refactoring is underway. I don't think it will be particularly productive to do anything until then, to be honest.

### gfursin · 2023-06-20

> > I think KILT will be useful particularly if it supports more hardware
> > backends other than Qualcomm.
> 
> We are planning to release more backends after the v3.1 round. Some necessary code refactoring is underway. I don't think it will be particularly productive to do anything until then, to be honest.

Sure. Sounds good! 

### arjunsuresh · 2023-06-20

[Submission Guidelines](https://github.com/mlcommons/inference/blob/master/Submission_Guidelines.md) is added now. 

### github-actions[bot] · 2026-05-13

🔒 This issue has been **automatically closed** because it has been open for more than 2 years with no activity.
If this is still relevant, you may **reopen it or create a new one**.
