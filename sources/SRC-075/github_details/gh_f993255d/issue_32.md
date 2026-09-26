# [Issue #32] Case study question

source: https://github.com/ScalingIntelligence/KernelBench/issues/32
state: closed | updated: 2025-03-25T07:02:07Z
labels: 

## 正文

Hello,

Are there instructions/scripts for generating results shown in Figure 5 and Figure 6 in your paper (https://arxiv.org/html/2502.10517v1) ?

Thanks.


## 评论 (1)

### simonguozirui · 2025-03-25

Hi there, thanks for taking interest in our work. 
 
For Figure 5 and 6 you mentioned here, aka test-time methods such as **repeated sampling** and **iterative refinement** with execution feedback, the code lives in an orchestration framework we built on top of KernelBench. 

We try to keep this KernelBench repo to a minimum and clean in its functionality as this is a reference eval codebase.
However, all the necessary functions to build such a system are here in this repo (eval, getting execution log), or the details are included in the paper (specific prompt). The orchestration framework just adds a lot more logic regarding data management, parallelization, and scalability on our limited lab compute resource, etc.

I am starting to release a minimum set of scripts you can use to try such approaches (not at scale, just as demonstration). For example, see PR #33 for the most basic form of repeated sampling. Will keep cleaning things up and release them.

A helpful resource is the [Large Language Monkeys](https://github.com/ScalingIntelligence/large_language_monkeys) codebase. I heavily built the orchestration framework based on this. Hope this helps!
