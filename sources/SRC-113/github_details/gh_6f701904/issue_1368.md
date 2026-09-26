# [Issue #1368] TensorFlow v1 API warning

source: https://github.com/mlcommons/inference/issues/1368
state: closed | updated: 2026-05-14T00:45:48Z
labels: Stale

## 正文

When running `vision/classification_and_detection/run_local.py` with TensorFlow as the backend, the following warning is produced...
```shell
WARNING:tensorflow:From /.../inference/vision/classification_and_detection/python/backend_tf.py:47: FastGFile.__init__ (from tensorflow.python.platform.gfile) is deprecated and will be removed in a future version.
Instructions for updating:
Use tf.gfile.GFile.
WARNING:tensorflow:From /.../python3-venv/lib/python3.10/site-packages/tensorflow/python/tools/strip_unused_lib.py:84:extract_sub_graph (from tensorflow.python.framework.graph_util_impl) is deprecated and will be removed in a future version. 
Instructions for updating:
This API was designed for TensorFlow v1. See https://www.tensorflow.org/guide/migrate for instructions on how to migrate your 
code to TensorFlow v2.
WARNING:tensorflow:From /.../python3-venv/lib/python3.10/site-packages/tensorflow/python/tools/optimize_for_inference_lib.py:112: remove_training_nodes (from tensorflow.python.framework.graph_util_impl) is deprecated and will be removed in a future version.
Instructions for updating:
This API was designed for TensorFlow v1. See https://www.tensorflow.org/guide/migrate for instructions on how to migrate your code to TensorFlow v2.
```
Are there any plans to patch the code if it could soon stop working?

## 评论 (2)

### arjunsuresh · 2023-05-03

Can you please do a PR for the change? 

### github-actions[bot] · 2026-05-14

🔒 This issue has been **automatically closed** because it has been open for more than 2 years with no activity.
If this is still relevant, you may **reopen it or create a new one**.
