# [Issue #48] offline/online serving is stuck at fetching files in paraworkers

source: https://github.com/LLMServe/DistServe/issues/48
state: open | updated: 2024-12-23T07:40:48Z
labels: 

## 正文

Hello guys I have some problems with deploying distserve on docker.

This is command what i used to launch docker env.

docker run --gpus all -it --name dist_bench --network=host --shm-size=10g -v /home/hyunmin/dataset:/workspace/dataset nvcr.io/nvidia/pytorch:24.05-py3 bash

I succefully build DistServe & SwiftTransformer inside my docker too.

However, when I tried to launch distserve online api_server or offline llm inference.
It just stucks in initializing the engine.

![online](https://github.com/user-attachments/assets/4d2362fe-3776-49ae-94d1-a067d89a1747)
![offline](https://github.com/user-attachments/assets/0da48112-f78c-4347-8980-691657dba0a5)

Is this problem related to shm size options?

Can anyone share the env or commands which successfully launch the serving.

Thank you in advance.

## 评论 (2)

### Moxixis · 2024-12-17

Hello, I have also encountered this problem. Have you solved it now? Perhaps we can communicate

### hyuenmin-choi · 2024-12-23

In my case, just waiting solved the problem.. The main cause was just because of slow model loading. :) 
Once you load it, it will run faster using cached data.
