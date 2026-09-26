# [Issue #4099] [Feature] Autoscale VLLm Pipeline Paralle

source: https://github.com/ray-project/kuberay/issues/4099
state: open | updated: 2026-09-22T16:57:03Z
labels: enhancement, stale

## 正文

### Search before asking

- [x] I had searched in the [issues](https://github.com/ray-project/kuberay/issues) and found no similar feature requirement.


### Description

I have used below link to deploy llm model via vllm and kuberay.
[https://docs.vllm.ai/projects/production-stack/en/latest/use_cases/pipeline-parallelism-kuberay.html]()
Following yaml I have used and sucessfully deployed my application
```
servingEngineSpec:
  runtimeClassName: ""
  modelSpec:
  - name: "distilgpt2"
    repository: "vllm/vllm-openai"
    tag: "latest"
    modelURL: "distilbert/distilgpt2"

    replicaCount: 1

    requestCPU: 2
    requestMemory: "20Gi"
    requestGPU: 2

    vllmConfig:
      tensorParallelSize: 2
      pipelineParallelSize: 2

    shmSize: "20Gi"

    raySpec:
      headNode:
        requestCPU: 2
        requestMemory: "20Gi"
        requestGPU: 2

    hf_token: <YOUR HF TOKEN>
```



### Use case

Now for the next stage, I want to move to autoscaling (using number of request in queue). I found a vllm tutorial but this is not suitable for my use case where llm is deployed on ray cluster using kuberay . In my current setup I am using two ray pods (1 head node pod and 1 worker node pod) with two gpu on each
[https://github.com/vllm-project/production-stack/blob/main/tutorials/10-horizontal-autoscaling.md](url)
From my understanding we are looking at cluster autoscaling but I am unable to understand how to achieve it.
[https://docs.ray.io/en/latest/cluster/kubernetes/user-guides/configuring-autoscaling.html](url).
[https://github.com/ray-project/kuberay/blob/v1.4.2/ray-operator/config/samples/ray-cluster.autoscaler.yaml](url)

I have following questions:
1. **_The Autoscaler decides to add a Ray worker Pod to satisfy the workload’s resource requirement._**. As per statement, autoscalar will add one more worker node that have 2 gpu. So total I have 6 gpu now (2 gpu on head pod, 2 gpu on woker pod and 2 gpu on new worker pod). So will my model now be distributed on 6 gpu (4 before) which results in faster inference?
2. How can I set request based trigger to increase the worker pods?

### Related issues

_No response_

### Are you willing to submit a PR?

- [ ] Yes I am willing to submit a PR!

## 评论 (3)

### Future-Outlier · 2025-09-27

can you pass the questions to ray slack, kuberay-questions channel?

### ishanExtreme · 2026-02-26

@akash-syook 

Example file: https://github.com/ray-project/kuberay/blob/master/ray-operator/config/samples/ray-cluster.autoscaler-v2.yaml

Assumptions:
1. Each node(for now lets say 1 worker = 1 node) has "2GPUs"
2. Our model requires total "4GPUs"
3. We are using CPUs in head node
4. We are using GPUs in worker nodes

Working:  
Lets assume we are using ray autoscaling, 
1. `enableInTreeAutoscaling` is set to true in ray cluster's config
2. We have set our `autoscalerOptions`
3. We have set `maxReplicas` in worker as `4`
4. In our serve config we have defined `replica=1`, `minReplica=1`, and `maxReplica=3`
5. We have set TP=2, PP=2 in serve config
6. We deploy our model, and "1" replica is runnning, we can see 2 workers spawned and running (This is because we need 4 GPUs for distributed inference of our model as defined by TP and PP in serve config, each worker have 2GPUs, resulting in 2X2=4GPUs)
7. Number of inference request increases, and our autoscaler signals for a scaling, since we have set `maxReplica=3` in serve config, one more "replica" of the same model get ready, which makes 2 more workers to spawn (2X2=4GPUs as defined in ray config)
8. Now to answer you question, we now have "2" replica of same model, and NOT distributing the first replica (in step 6) into 8GPUS (4 workers X2 = 8GPUs).
9. Again we have even more inferencing request, autoscaler fires up one more replica (`maxReplica=3` in serve config <=3), BUT this time we don't have anymore worker to startup, (worker's maxReplicas is set to 4 which is achieved in step 7) so the 3rd replica will keep waiting for the resource

In short ray autoscaler creates the replica of the model defined in serve config, and the loadbalancer routes the request to these replica making concurrent requests faster

Please correct me where ever I am wrong, this the setup I am using and observed in my system.
Thanks!

Ref: https://docs.ray.io/en/latest/serve/autoscaling-guide.html
https://docs.ray.io/en/latest/serve/api/doc/ray.serve.config.AutoscalingConfig.html

### github-actions[bot] · 2026-09-22

This issue has been automatically marked as stale because it has not had
any activity for 120 days. It will be closed in 14 days if no further activity occurs.

If you'd like to keep this issue open, just leave any comment, and the stale label will be removed.
If you'd like to get more attention on this issue, please tag one of the KubeRay maintainers.

You can always ask for help on [Ray's public Slack channel](https://github.com/ray-project/kuberay#getting-involved).
