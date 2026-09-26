# [Issue #84] Memory leak when using perf_analyser at high throughput

source: https://github.com/triton-inference-server/perf_analyzer/issues/84
state: open | updated: 2025-07-09T09:56:02Z
labels: 

## 正文

**Description**
When using the perf_analyser in a high throughput case (30 000+ QPS), it usually gets killed because of OOM issues. Another behavior that arises is that the measurements consolidations seem to take an exponential amount of time along the experiment.
During the load testing, server-side the queues stay empty, the resources are used way below what is allocated, nothing show any sign of contention that could explain some instability client side.

using tcmalloc has been tested without any change in behavior
CPU usage is around 5 cpu cores, memory consistently increase throughout the measurement session

Example of such a run (added time measurements for each pass in the log, to show exponential growth): 
```
*** Measurement Settings ***
  Batch size: 1
  Service Kind: TRITON
  Using "time_windows" mode for stabilization
  Stabilizing using p75 latency
  Measurement window: 1000 msec
  Latency limit: 0 msec
  Request Rate limit: 60000 requests per seconds
  Using uniform distribution on request generation
  Using asynchronous calls for inference

Request Rate: 35000 inference requests per seconds
  Pass [1] throughput: 34975.1 infer/sec. p75 latency: 999 usec (*** 2 sec ***)
  Pass [2] throughput: 34998.8 infer/sec. p75 latency: 955 usec (*** 2 sec ***)
  Pass [3] throughput: 35002.1 infer/sec. p75 latency: 941 usec (*** 3.4 sec ***)
  Client: 
    Request count: 172873
    Throughput: 34994.5 infer/sec
    Avg client overhead: 0.00%
    p50 latency: 830 usec
    p75 latency: 960 usec
    p90 latency: 1090 usec
    p95 latency: 1172 usec
    p99 latency: 1337 usec
    Avg gRPC time: 848 usec (marshal 3 usec + response wait 845 usec + unmarshal 0 usec)
  Server: 
    Inference count: 172878
    Execution count: 37008
    Successful request count: 172878
    Avg request latency: 657 usec (overhead 140 usec + queue 117 usec + compute input 100 usec + compute infer 287 usec + compute output 12 usec)

Request Rate: 37500 inference requests per seconds
  Pass [1] throughput: 37506 infer/sec. p75 latency: 977 usec       (*** 2 sec ***)
  Pass [2] throughput: 37498.6 infer/sec. p75 latency: 982 usec    (*** 4.2 sec ***)
  Pass [3] throughput: 37502.8 infer/sec. p75 latency: 984 usec    (*** 11 sec ***)
  Client: 
    Request count: 284738
    Throughput: 37502.1 infer/sec
    Avg client overhead: 0.00%
    p50 latency: 856 usec
    p75 latency: 982 usec
    p90 latency: 1109 usec
    p95 latency: 1182 usec
    p99 latency: 1326 usec
    Avg gRPC time: 869 usec (marshal 3 usec + response wait 866 usec + unmarshal 0 usec)
  Server: 
    Inference count: 284736
    Execution count: 55428
    Successful request count: 284737
    Avg request latency: 672 usec (overhead 152 usec + queue 119 usec + compute input 105 usec + compute infer 283 usec + compute output 12 usec)

Request Rate: 40000 inference requests per seconds```
  Pass [1] throughput: 40053.9 infer/sec. p75 latency: 1046 usec     (*** 8 sec ***)
  Pass [2] throughput: 39999.6 infer/sec. p75 latency: 1038 usec     (*** 40 sec ***)

*** Process killed because OOM after 7:40 min**
```

Another run starting directly at 40000 QPS (where the process failed in the previous experiment) shows the following behavior (log abbreviated):

```
Request Rate: 40000 inference requests per seconds
  Pass [1] throughput: 39966.9 infer/sec. p75 latency: 1042 usec     (*** 2 sec ***)
  Pass [2] throughput: 39992 infer/sec. p75 latency: 996 usec          (*** 2.8 sec ***)
  Pass [3] throughput: 40006.9 infer/sec. p75 latency: 989 usec       (*** 7.4 sec ***)
  
Request Rate: 42500 inference requests per seconds
  Pass [1] throughput: 42532.3 infer/sec. p75 latency: 1023 usec     (*** 7.8 sec ***)
  Pass [2] throughput: 42501.7 infer/sec. p75 latency: 1052 usec    

*** Process killed because OOM after 6:3 min ***
```

**Runtime information**
Running in py3-sdk offical container, version 24.06, on a Kube container with 16 Cpus and 32GB RAM. 
The container running the perf_analyser is on a separate node from the triton server

**To Reproduce**
run a very simple model (we use a simple scalar cast as Onnx model) and load it with the following command: 
`perf_analyzer -v -m <model_name> --percentile=75 --request-rate-range=35000:60000:2500 -a -u <server_address -i grpc --input-data random --measurement-interval 1000 --max-threads=32 --string-length=16 --stability-percentage=70`

**Expected behavior**
The perf_analyser does't exponentially slow down when doing measurements and does not eventually crash


## 评论 (4)

### jcuquemelle · 2025-02-05

Proposed workaround: switch to container version 24.02

### debermudez · 2025-02-06

Have you had a chance to try a version more recent than 24.06?

### jcuquemelle · 2025-02-06

The workaround was suggested by Nvidia enterprise support, for now we're fine with it, and we're waiting for an explicit ping from them to test again with a more recent version

### DenDiv · 2025-07-09

I received OOM in version 25.06 but not in version 24.02.
