# [Issue #296] Write metrics to file per model of an ensemble

source: https://github.com/triton-inference-server/perf_analyzer/issues/296
state: open | updated: 2025-02-27T18:50:46Z
labels: 

## 正文

When I run `perf_analyzer -u inference-server:8000 -m my_ensemble --input-data /data/data_for_my_ensemble/ --shape image_arrays:0:720,1280,3` then I get this very nice report printed that contains the values for each model of the ensemble (actual latencies and throughput of the ensemble replaced with xxx, and the ones of the models with yyy):
```*** Measurement Settings ***
  Batch size: 1
  Service Kind: TRITON
  Using "time_windows" mode for stabilization
  Stabilizing using average latency and throughput
  Measurement window: 5000 msec
  Using synchronous calls for inference

Request concurrency: 1
  Client:
    Request count: 697
    Throughput: xxx infer/sec
    Avg latency: xxx usec (standard deviation xxx usec)
    p50 latency: xxx usec
    p90 latency: xxx usec
    p95 latency: xxx usec
    p99 latency: xxx usec
    Avg HTTP time: xxx usec (send/recv xxx usec + response wait xxx usec)
  Server:
    Inference count: 698
    Execution count: 698
    Successful request count: 698
    Avg request latency: xxx usec (overhead xxx usec + queue xxx usec + compute xxx usec)

  Composing models:
  model_of_ensemble_1, version: 1
      Inference count: 698
      Execution count: 698
      Successful request count: 698
      Avg request latency: yyy usec (overhead yyy usec + queue yyy usec + compute input yyy usec + compute infer yyy usec + compute output yyy usec)

### [more composing models of the ensemble that I removed due to brevity] ###

  model_of_ensemble_n, version: 1
      Inference count: 698
      Execution count: 698
      Successful request count: 698
      Avg request latency: yyy usec (overhead yyy usec + queue yyy usec + compute input yyy usec + compute infer yyy usec + compute output yyy usec)

Inferences/Second vs. Client Average Batch Latency
Concurrency: 1, throughput: xxx infer/sec, latency xxx use
```

Yet, when I run it with `-f` or with `--verbose-csv`, I only get the results of the whole ensemble, like:
```
# -f
Concurrency,Inferences/Second,Client Send,Network+Server Send/Recv,Server Queue,Server Compute Input,Server Compute Infer,Server Compute Output,Client Recv,p50 latency,p90 latency,p95 latency,p99 latency
# --verbose-csv
Concurrency,Inferences/Second,Client Send,Network+Server Send/Recv,Server Queue,Server Compute Input,Server Compute Infer,Server Compute Output,Client Recv,p50 latency,p90 latency,p95 latency,p99 latency,Avg latency,request/response,response wait
```
Is there a way to get the results that are printed per model directly to file? E.g. with a column `model` and then the individual values, or as a json? 

Currently I am piping the outputs to a file and then filtering, but it would be great to do it directly with the cli.

Setup:
- perf_analyzer 24.12
- triton-inference-server 24.12

Thank you very much in advance!

## 评论 (1)

### the-david-oy · 2025-02-27

CC: @matthewkotila 
