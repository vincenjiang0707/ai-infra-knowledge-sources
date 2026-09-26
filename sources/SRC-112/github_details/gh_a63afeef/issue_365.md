# [Issue #365] Contents of CONFIG_DIR path as used in launch_gb200-nv.sh is undisclosed / launch_gb200-nv.sh 使用的 CONFIG_DIR 路径内容未公开

source: https://github.com/SemiAnalysisAI/InferenceX/issues/365
state: closed | updated: 2026-07-08T15:57:35Z
labels: 

## 正文

The current logic sets `CONFIG_DIR="/mnt/lustre01/artifacts/sglang-configs/1k1k"`. I don't believe the contents of this directory is disclosed anywhere (though please correct me if I'm wrong!), meaning it's not possible to reproduce or audit the configuration. 

https://github.com/InferenceMAX/InferenceMAX/blob/ff7dfc7365034aa84245f41c517c38618860d484/runners/launch_gb200-nv.sh#L26

## 中文说明
launch_gb200-nv.sh 使用的 CONFIG_DIR 路径内容未公开。


## 评论 (2)

### cquil11 · 2025-12-21

We are actively working on making the disagg stuff more first-class for v2 of InferenceMAX.

### chaitanyapk · 2026-01-05

+1, I've been trying to replicate the disaggregated sglang numbers on GB200 for DSR1 and it'd be of great help if you can share the 1k1k config artefacts
