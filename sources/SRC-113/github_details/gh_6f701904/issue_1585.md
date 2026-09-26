# [Issue #1585] use MLPerf inference benchmark testing on NPU

source: https://github.com/mlcommons/inference/issues/1585
state: closed | updated: 2026-05-22T00:46:15Z
labels: Stale

## 正文

May I ask if I can use MLPerf inference benchmark testing on NPU? What do I need to do? Is there any relevant documentation available？

## 评论 (2)

### AaronSomeone · 2024-05-21

I am also wondering this. It looks like we would have to modify the `backend` files, e.g. for classification and detection, modifying `inference/vision/classification_and_detection/python/backend_[backend].py`. For example if you're using onnxruntime, check if your hardware is supported here: https://onnxruntime.ai/docs/execution-providers/. If not, we have to modify the `backend_[backend].py` file and implement those functions, importantly `load` and `predict`. But what else: what output formats, etc.; guidance would be helpful.

### github-actions[bot] · 2026-05-22

🔒 This issue has been **automatically closed** because it has been open for more than 2 years with no activity.
If this is still relevant, you may **reopen it or create a new one**.
