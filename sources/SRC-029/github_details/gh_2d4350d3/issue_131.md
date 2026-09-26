# [Issue #131] Clean up Model Conversion Script

source: https://github.com/AI-Hypercomputer/JetStream/issues/131
state: open | updated: 2024-12-18T19:13:16Z
labels: 

## 正文

Currently the model conversion script will [create a bucket](https://github.com/google/JetStream/blob/main/jetstream/tools/maxtext/model_ckpt_conversion.sh#L36) `export MODEL_BUCKET=gs://${USER}-maxtext`. However, it may be the case that the `gs://${USER}-maxtext` path already exists, which I imagine would break the script. 

Solution: Be able to read in a few more arguments `MODEL_BUCKET` and `BASE_OUTPUT_DIRECTORY`. We should also delete references to `DATASET_PATH`.

## 评论 (2)

### JoeZijunZhou · 2024-08-16

If the bucket exists, the script will continue and use the existing ones IIRC. But feel free to refactor it to improve UX.

### yeandy · 2024-08-19

> If the bucket exists, the script will continue and use the existing ones IIRC

Yes, but only if the current `USER` is the original creator/owner of bucket, right? A different user could have the same value for `USER`, which I think would break the workflow.
