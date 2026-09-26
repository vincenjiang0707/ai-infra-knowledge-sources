# [Issue #1563] [Stable Diffusion Reference]: `qps` can't set to float

source: https://github.com/mlcommons/inference/issues/1563
state: closed | updated: 2026-05-09T00:41:11Z
labels: Stale

## 正文

I run and have an error:
```
 time python3 main.py --dataset "coco-1024" --dataset-path coco2014_full --profile stable-diffusion-xl-pytorch --model-path model/stable_diffusion
_fp16/  --dtype fp16 --device cuda  --scenario SingleStream --model-name stable-diffusion-xl --qps 0.022  --output results --ids-path tools/sample_ids.txt

usage: main.py [-h] [--dataset {coco-1024}] --dataset-path DATASET_PATH [--profile {defaults,debug,stable-diffusion-xl-pytorch,stable-diffusion-xl-pytorch-dist}] [--scenario SCENARIO] [--max-batchsize MAX_BATCHSIZE] [--threads THREADS]
               [--accuracy] [--find-peak-performance] [--backend BACKEND] [--model-name MODEL_NAME] [--output OUTPUT] [--qps QPS] [--model-path MODEL_PATH] [--dtype {fp32,fp16,bf16}] [--device {cuda,cpu}]                                                [--latent-framework {torch,numpy}] [--mlperf_conf MLPERF_CONF] [--user_conf USER_CONF] [--audit_conf AUDIT_CONF] [--ids-path IDS_PATH] [--time TIME] [--count COUNT] [--debug]
               [--performance-sample-count PERFORMANCE_SAMPLE_COUNT] [--max-latency MAX_LATENCY] [--samples-per-query SAMPLES_PER_QUERY]
main.py: error: argument --qps: invalid int value: '0.022'
```
Here https://github.com/mlcommons/inference/blob/master/text_to_image/main.py#L102
qps should be `int`.

We need to set `qps` to `float` in some cases.


## 评论 (3)

### arjunsuresh · 2024-01-17

Ideally we should just delete that option and just use `user.conf` right? Handling qps/latency etc inside the implementation is unnecessary extra work. 

### maria-18-git · 2024-01-18

@arjunsuresh , thank you. It is better to use user.conf only.

### github-actions[bot] · 2026-05-09

🔒 This issue has been **automatically closed** because it has been open for more than 2 years with no activity.
If this is still relevant, you may **reopen it or create a new one**.
