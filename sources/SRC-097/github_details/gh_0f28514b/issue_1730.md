# [Issue #1730] FILE_SEG filename option - NIXLBench Support

source: https://github.com/ai-dynamo/nixl/issues/1730
state: open | updated: 2026-06-09T07:44:00Z
labels: 

## 正文

@lluki please add support for this option in the PR in the CI tests - .gitlab/test_cpp.sh.
Also add nixlbench support for this one. We will need QA to test the path option correctly. Its a new feature for FILE_SEG API - separate PR is fine.

_Originally posted by @aranadive in https://github.com/ai-dynamo/nixl/issues/1635#issuecomment-4624115413_
            

## 评论 (3)

### lluki · 2026-06-05

Functional testing is already included in the [original PR](https://github.com/ai-dynamo/nixl/pull/1635), lets make this issue and follow up PR solely on the `nixlbench` modifications

### alokprasad · 2026-06-08

@lluki @aranadive how can i use this commit , does it add FILE_SEG option to nixlbench besided VRAM/DRAM?
https://github.com/ai-dynamo/nixl/issues/1707#issuecomment-4648916499


### lluki · 2026-06-09

Hi @alokprasad  

I might not fully understand your question, but from other comments I have gathered you're interested in GDS.

This issue and PR #1734 that fixes it is about the "path-mode" that was recently merged #1635 . #1635 supports GDS, but nixlbench does not as run any tests on GDS. Hence, #1734 does not add GDS nixlbench support either (it just duplicates the POSIX backend evaluation).

The invocation of #1734 should be clear from the CI script update. Let me know if you have questions about that. 

Can you give us some context what you are interested in?
