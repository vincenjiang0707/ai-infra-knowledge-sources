# [Issue #1609] SDXL model download link broken

source: https://github.com/mlcommons/inference/issues/1609
state: closed | updated: 2026-05-08T00:40:42Z
labels: Stale

## 正文

https://cloud.mlcommons.org/index.php/s/LCdW5RM6wgGWbxC 
https://cloud.mlcommons.org/index.php/s/DjnCSGyNBkWA4Ro
Pages Not Found error for SDXL model links.

## 评论 (6)

### arjunsuresh · 2024-02-05

Not only SDXL but all MLCommons hosted links like GPTJ, DLRMv2 are also broken via wget. MLCommons admins have suggested to use the rclone link which are wrapped in the CM comment [here](https://github.com/mlcommons/inference/issues/1600#issuecomment-1924812135)

### nvyihengz · 2024-02-05

`cm pull repo ctuning@mlcommons-ck`

Does every submitter need to use the ctuning account or they can use their own accounts?

### arjunsuresh · 2024-02-05

@nvyihengz Please use `cm pull repo mlcommons@ck` - the ctuning one was a temporal link until the PR was merged.

`mlcommons@ck` is a short hand for `https://github.com/mlcommons/ck`  

### nvyihengz · 2024-02-07

Known affected workloads @mrmhodak @pgmpablo157321 
SDXL https://github.com/mlcommons/inference/tree/master/text_to_image 
GPTJ https://github.com/mlcommons/inference/tree/master/language/gpt-j
DLRMv2 https://github.com/mlcommons/inference/tree/master/recommendation/dlrm_v2/pytorch#downloading-model-weights

### arjunsuresh · 2024-02-07

@nvyihengz We do have the cloudflare rclone commands for all. (wget links are still broken though)

```
python3 -m pip install cmind
cm pull repo mlcommons@ck
cm run script --tags=get,ml-model,gptj,_pytorch,_rclone -j
cm run script --tags=get,ml-model,dlrm,_pytorch,_weight_sharded,_rclone -j
cm run script --tags=get,ml-model,sdxl,_fp16,_rclone -j
cm run script --tags=get,ml-model,sdxl,_fp32,_rclone -j
```

Running `cm` command will print the underlying rclone config but it is better to use `cm` commands as the configs can change later but cm commands won't. 

### github-actions[bot] · 2026-05-08

🔒 This issue has been **automatically closed** because it has been open for more than 2 years with no activity.
If this is still relevant, you may **reopen it or create a new one**.
