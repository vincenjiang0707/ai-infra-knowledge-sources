# [Issue #14] Feature request: improve documentation

source: https://github.com/AI-Hypercomputer/JetStream/issues/14
state: closed | updated: 2024-03-21T23:06:50Z
labels: 

## 正文

Hey, how do I use this library with llama or mistral/mixtral?
thanks!


## 评论 (5)

### vipannalla · 2024-03-19

Hi Ohad,
     This library can used as orchestration layer that provides inference features such as continuous batching, disaggregation etc. You would need to implement a runtime engine that supports LLama or Mistral/Mixtral forward pass for inference and integrate it with JetStream by supporting these APIs -- https://github.com/google/JetStream/blob/main/jetstream/engine/engine_api.py. 

Having said that, this is a new codebase and we are working on a user guide that should provide more details. cc @JoeZijunZhou 
     

### borisdayma · 2024-03-19

This looks cool and I see it being used by maxtext.
My main confusion is if it's meant to send requests of single item at a time or if it will also support sending directly a batch of inputs?

### vipannalla · 2024-03-19

The server current expects a single request and does the (continuous) batching for the user. This is primarily targetting the online serving usecase. You are correct, maxtext is a reference engine implementation that works with JetStream.

### borisdayma · 2024-03-19

So in the case I want to process 10k inputs, can they be submitted fast enough to maximize tpu utilization but still avoiding failure due to too much backlog?

### vipannalla · 2024-03-20

JetStream uses grpc server framework and the requests are subject to the timeouts/limits set at the service level. Internally, it will process as many requests as it can to provide the best throughput/latency as possible. 
Each model is different and the tpu utilization and performance numbers also depend on how the model is setup (num params, activations, quantization settings, HBM used, sharding etc.) in the engine (maxtext) for a given hardware used (eg. TPU v5e-16). We should have tuned configs for some of publicly available models such as LLama fairly soon.

