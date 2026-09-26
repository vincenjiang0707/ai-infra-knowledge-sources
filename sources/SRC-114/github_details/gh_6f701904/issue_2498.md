# [Issue #2498] Support for RGAT with abandoned DGL dependency

source: https://github.com/mlcommons/inference/issues/2498
state: open | updated: 2026-04-10T19:42:30Z
labels: 

## 正文

Hi,

DGL which is used in the RGAT seems abandoned:

the last release for DGL was in September 2024 https://github.com/dmlc/dgl/releases  which is [v2.4.0](https://github.com/dmlc/dgl/releases/tag/v2.4.0)
and relate issue https://github.com/dmlc/dgl/issues/7904. Most of the issues have also been marked stale.

Is there plans to update RGAT with something else?
@pgmpablo157321 

## 评论 (3)

### cfRod · 2026-02-10

@mrmhodak 

### attafosu · 2026-04-07

Given that 6.1 is too close to make any meaningful changes, I suggest we keep it as is (and specify the dgl branch/commit in the reference implementation if required). We can re-evaluate for post 6.1 submissions

### hanyunfan · 2026-04-10

Thank you Thomas. I’ll bring this up and briefly discuss it at the next WG meeting.
