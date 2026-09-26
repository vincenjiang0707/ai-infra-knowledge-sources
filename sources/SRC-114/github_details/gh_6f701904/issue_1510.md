# [Issue #1510] Request NVIDIA to make container BASE IMAGE links the publicly available links

source: https://github.com/mlcommons/inference/issues/1510
state: closed | updated: 2026-05-11T00:43:12Z
labels: Stale

## 正文

For reproducibility we would request NVIDIA to switch the `BASE_IMAGE` repo links from internal Gitlab links to publicly available repo links. In the `Makefile.docker`, the `BASE_IMAGE` URL is from an internal NVIDIA link. Here is the link to the `Makefile.docker` from the public MLPerf Inference v3.1 results repo:

https://github.com/mlcommons/inference_results_v3.1/blob/main/closed/NVIDIA/Makefile.docker

## 评论 (2)

### nvyihengz · 2023-11-01

Hi, https://github.com/mlcommons/inference_results_v3.1/blob/main/closed/NVIDIA/Makefile.docker#L142 BASE_IMAGE is public, please check if you can download it via docker pull.

### github-actions[bot] · 2026-05-11

🔒 This issue has been **automatically closed** because it has been open for more than 2 years with no activity.
If this is still relevant, you may **reopen it or create a new one**.
