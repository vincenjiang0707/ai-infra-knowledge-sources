# [Issue #34] Down Detector

source: https://github.com/gpu-mode/kernelbot/issues/34
state: closed | updated: 2024-11-23T01:30:08Z
labels: 

## 正文

* Nov 21: AMD jobs stuck in queue  https://github.com/gpu-mode/discord-cluster-manager/actions/runs/11958587509
* As of Nov 20: NVIDIA jobs stuck in queue forever https://github.com/gpu-mode/discord-cluster-manager/actions/runs/11944808187
* Nov 20: AMD jobs can't find a hip GPU https://github.com/gpu-mode/discord-cluster-manager/actions/runs/11945340557 - cc @saienduri - fixed

## 评论 (1)

### saienduri · 2024-11-21

Logged into the runner and simple rocm commands weren't working. Possible that one of the jobs crashed rocm. Anyways, gave it a reboot and should be good now
