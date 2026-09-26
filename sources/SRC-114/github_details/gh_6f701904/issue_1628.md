# [Issue #1628] Understanding the Benchmarking Scenarios for DLRmv2

source: https://github.com/mlcommons/inference/issues/1628
state: closed | updated: 2026-05-08T00:40:38Z
labels: Stale

## 正文

Hi!
I've been delving into the DLRMv2 benchmark, and I want to confirm my understanding of the scenarios. For the Server scenario, my understanding is that it runs this command
```
./run_local.sh pytorch dlrm multihot-criteo cpu --scenario Server --max-ind-range=40000000 --samples-to-aggregate-quantile-file=./tools/dist_quantile.txt --max-batchsize=2048
```

Each query contains one sample, and the sample has B user-item pairs. The number of user-item pairs, B, is variable and determined based on a distribution sampled from dist_quantile.txt, ranging between 100-700. Is it corrrect to say that the reported throughput in Queries Per Second (QPS) reflects the samples processed per second ([like these ones](https://mlcommons.org/benchmarks/inference-datacenter/)), and the throughput in terms of the number of user-item pairs processed per second is greater than QPS (around B * QPS) because each sample contains multiple user-item pairs? 

Also, for the Offline scenario, it seems like the number of user-item pairs per sample is also drawn from the dist_quantile.txt. I was wondering what number is used for the number of samples per query. 

Thanks! 



## 评论 (1)

### github-actions[bot] · 2026-05-08

🔒 This issue has been **automatically closed** because it has been open for more than 2 years with no activity.
If this is still relevant, you may **reopen it or create a new one**.
