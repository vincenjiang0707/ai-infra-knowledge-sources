# [Issue #1691] [Reproducibility] dsr1 0528 dynamo + mtp on b200 / [Reproducibility] DSR1 0528 Dynamo + MTP 在 B200 上的复现

source: https://github.com/SemiAnalysisAI/InferenceX/issues/1691
state: open | updated: 2026-07-04T05:17:17Z
labels: 

## 正文

Hey,

I've been trying to reproduce the results for the following run:
ISL = 1k
OSK = 1k

B200 (Dynamo TRT, MTP)
Date: 2026-01-29
Image: nvcr.io/nvidia/ai-dynamo/tensorrtllm-runtime:0.8.1.post1
Interactivity (tok/s/user): 21.338126345946833
Output Token Throughput per GPU (tok/s/gpu): 10,012.214
Total GPUs: 32
Prefill: 12 GPUs, TP: 4, EP: 4, DPA: True, Workers: 3
Decode: 20 GPUs, TP: 4, EP: 4, DPA: True, Workers: 5
Concurrency: 10860
Precision: FP4
[GitHub Actions Run](https://github.com/SemiAnalysisAI/InferenceX/actions/runs/21484975323/attempts/1)

I have 4 nodes of B200 sxm, i am using K8s to deploy the same configuration as you did here:
https://github.com/NVIDIA/srt-slurm/blob/sa-submission-q2-2026/recipes/trtllm/b200-fp4/1k1k/mtp/ctx3_gen5_dep4_batch512_eplb0_mtp1.yaml

No matter what I did, my results still fall under 10K TPS per GPU. Current best result is ~8.3K per decode gpu.

I have validated the kv transfer is via gpu direct.

The logs of the run already expired and therefore, ask if there is a way to get them or at least share more about how to be able to reproduce the results , e.g, how many frontends were deployed ? or were the system was configured to performance?

Thanks

## 中文说明
用户尝试在 4 节点 B200 SXM（K8s 部署）上复现 DSR1 0528 使用 Dynamo TRT + MTP 的基准测试结果（ISL=1k, OSL=1k, FP4, 32 GPU 分离式推理），但每 GPU 输出吞吐量仅达到约 8.3K tok/s，低于发布的 10,012 tok/s。已确认 KV 传输使用 GPU Direct。由于 GitHub Actions 运行日志已过期，请求提供更多复现信息，例如前端部署数量和系统性能配置。


## 评论 (9)

### functionstackx · 2026-06-11

@OrZipori what networking technology r u using? we r using google cloud B200 VMs with 8x400G ConnectX-7 

### functionstackx · 2026-06-11

> i am using K8s to deploy the same configuration as you did here

we are using slurm, can u triple check that u have ported over to k8s correctly?

### OrZipori · 2026-06-11

> [@OrZipori](https://github.com/OrZipori) what networking technology r u using? we r using google cloud B200 VMs with 8x400G ConnectX-7

Yes , we use the same topology on another cloud provider.
 

### OrZipori · 2026-06-11

> > i am using K8s to deploy the same configuration as you did here
> 
> we are using slurm, can u triple check that u have ported over to k8s correctly?

We are checking. One question, why do you schedule prefill workers and decode workers on separate nodes? isn't it better (kv transfer wise) to have a mix of prefill and decode workers on same node?

### functionstackx · 2026-06-11

@OrZipori what CSP r u using?

### OrZipori · 2026-06-11

> what CSP r u using?

Nebius

### OrZipori · 2026-06-11

> > i am using K8s to deploy the same configuration as you did here
> 
> we are using slurm, can u triple check that u have ported over to k8s correctly?

same. i can paste it here if it's something you'd like

### functionstackx · 2026-06-11

@OrZipori can u try doing it on slurm first and seeing it that works and then once that works, see if ur port to k8s is matching all the env vars?



### OrZipori · 2026-06-14

sure. 

1. in the config files there is "sa-bench", is that the https://github.com/SemiAnalysisAI/InferenceX/blob/main/utils/bench_serving/benchmark_serving.py?
2. in single node, you use 10 x CONC for num of prompts, but i don't see anything like that in the multi node benchmarks. are you using the same method for multi node as well?
3. how many frontends do you deploy per model?
4. do you use 1 client to send all the requests?
5. what was the ttft you guys got with configuration?
