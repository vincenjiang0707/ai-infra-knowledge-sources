# [Issue #674] llama_or_mistral_ckpt.py file requiring checkpoints in local file system

source: https://github.com/AI-Hypercomputer/maxtext/issues/674
state: closed | updated: 2026-05-05T21:24:52Z
labels: feature request

## 正文

The llama_or_mistral_ckpt.py requires --base-model-path to be in local file system, whereas the --maxtext-model-path is GCS.
It would be good to change the implmentation to use fsspec or tf GFile or some universal file reader that can read file from gcs and local filepath.



## 评论 (1)

### YixuanWang-99 · 2026-05-05

Please find our new consolidated [checkpoint conversion module](https://maxtext.readthedocs.io/en/maxtext-v0.2.1/guides/checkpointing_solutions/convert_checkpoint.html), we recently solved another similar issue that is to convert local huggingface ckpt to maxtext ckpt [here](https://github.com/AI-Hypercomputer/maxtext/issues/3061). And you can find the example command usage and expected output. 
