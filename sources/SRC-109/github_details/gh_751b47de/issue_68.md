# [Issue #68] Unable to run performance analyzer on my model - Request for unknown model: '/models::ensemble' is not found

source: https://github.com/triton-inference-server/perf_analyzer/issues/68
state: closed | updated: 2025-03-03T21:16:08Z
labels: 

## 正文

Unable to run performance analyzer on my model
I am using a sagemaker wrapper image of triton server and am able to serve the model with requests and even validate that it is up, all ports for grpc, http and metrics are up
But when I am run the performance analyzer, it is throwing me an error
`perf_analyzer -m ensemble --input-data data.json --measurement-interval=60000 -v -v `
**Request for unknown model: '/models::ensemble' is not found**

I see that it is doing GET /v2/models/stats 

which fails for me as well 

```
[vvijeth@dev-dsk-vvijeth]~% curl -v localhost:8000/v2/models/stats
*   Trying 127.0.0.1:8000...
* Connected to localhost (127.0.0.1) port 8000
> GET /v2/models/stats HTTP/1.1
> Host: localhost:8000
> User-Agent: curl/8.3.0
> Accept: */*
>
< HTTP/1.1 400 Bad Request
< Content-Type: application/json
< Content-Length: 71
<
* Connection #0 to host localhost left intact
{"error":"Request for unknown model: '/models::ensemble' is not found"}%
```




Where as the curl on ensemble model succeeds.
```
[vvijeth@dev-dsk-vvijeth]~% curl -v localhost:8000/v2/models/ensemble/stats
*   Trying 127.0.0.1:8000...
* Connected to localhost (127.0.0.1) port 8000
> GET /v2/models/ensemble/stats HTTP/1.1
> Host: localhost:8000
> User-Agent: curl/8.3.0
> Accept: */*
>
< HTTP/1.1 200 OK
< Content-Type: application/json
< Content-Length: 602
<
* Connection #0 to host localhost left intact
{"model_stats":[{"name":"ensemble","version":"1","last_inference":1725056057677,"inference_count":6,"execution_count":6,"inference_stats":{"success":{"count":6,"ns":810771011},"fail":{"count":0,"ns":0},"queue":{"count":6,"ns":11563},"compute_input":{"count":6,"ns":2010272},"compute_infer":{"count":6,"ns":795845523},"compute_output":{"count":6,"ns":6497024},"cache_hit":{"count":0,"ns":0},"cache_miss":{"count":0,"ns":0}},"batch_stats":[{"batch_size":1,"compute_input":{"count":6,"ns":2010272},"compute_infer":{"count":6,"ns":795845523},"compute_output":{"count":6,"ns":6497024}}],"memory_usage":[]}]}%
```



What could be wrong?

## 评论 (10)

### debermudez · 2024-08-30

@matthewkotila or @ganeshku1 any ideas?
It looks like the model endpoint is different than what we would expect.


@vijetha35 when you launched the server, did the sagemaker wrapper change the endpoints?

### vijetha35 · 2024-08-30

Which endpoint are you talking about?

On Fri, Aug 30, 2024, 4:07 PM Elias Bermudez ***@***.***>
wrote:

> @matthewkotila <https://github.com/matthewkotila> or @ganeshku1
> <https://github.com/ganeshku1> any ideas?
> It looks like the model endpoint is different than what we would expect.
>
> @vijetha35 <https://github.com/vijetha35> when you launched the server,
> did the sagemaker wrapper change the endpoints?
>
> —
> Reply to this email directly, view it on GitHub
> <https://github.com/triton-inference-server/perf_analyzer/issues/68#issuecomment-2322555836>,
> or unsubscribe
> <https://github.com/notifications/unsubscribe-auth/ABBFIUFB37ZEFZLOKDDYW73ZUD3JJAVCNFSM6AAAAABNNIJX4OVHI2DSMVQWIX3LMV43OSLTON2WKQ3PNVWWK3TUHMZDGMRSGU2TKOBTGY>
> .
> You are receiving this because you were mentioned.Message ID:
> ***@***.***>
>


### debermudez · 2024-08-30

Any of the endpoints that triton uses by default.
I wanted to see if i could quickly rule anything out that might cause this issue.

### nv-hwoo · 2024-09-03

@vijetha35 few questions
1. Which version/release of triton server and perf analyzer are you using?
2. Could you share the model setup of triton server? (e.g. model config and model repository)
3. Could you share the output of your perf analyzer command: `perf_analyzer -m ensemble --input-data data.json --measurement-interval=60000 -v -v `?
4. Could you share your input file `data.json`?

### vijetha35 · 2024-09-03

1. 23.08 version
2. models repository consists of:
models 
|__ensemble
|__preprocess
|__encoder
|__decoder
|__postprocess
3. Output of the command is as follows:
```
root@dev-dsk-vvijeth:/workspace# perf_analyzer -m ensemble --input-data data.json --measurement-interval=60000
 Successfully read data for 1 stream/streams with 1 step/steps.
*** Measurement Settings ***
  Batch size: 1
  Service Kind: Triton
  Using "time_windows" mode for stabilization
  Measurement window: 60000 msec
  Using synchronous calls for inference
  Stabilizing using average latency

Request concurrency: 1
Request for unknown model: '/models::ensemble' is not found
root@dev-dsk-vvijeth-2c-306acd45:/workspace# perf_analyzer -m ensemble --input-data data.json --measurement-interval=60000
 Successfully read data for 1 stream/streams with 1 step/steps.
*** Measurement Settings ***
  Batch size: 1
  Service Kind: Triton
  Using "time_windows" mode for stabilization
  Measurement window: 60000 msec
  Using synchronous calls for inference
  Stabilizing using average latency

Request concurrency: 1
Request for unknown model: '/models::ensemble' is not found
root@dev-dsk-vvijeth-2c-306acd45:/workspace# perf_analyzer -m ensemble --input-data data.json --measurement-interval=60000
 Successfully read data for 1 stream/streams with 1 step/steps.
*** Measurement Settings ***
  Batch size: 1
  Service Kind: Triton
  Using "time_windows" mode for stabilization
  Measurement window: 60000 msec
  Using synchronous calls for inference
  Stabilizing using average latency

Request concurrency: 1
Request for unknown model: '/models::ensemble' is not found
root@dev-dsk-vvijeth-2c-306acd45:/workspace# perf_analyzer -m ensemble --input-data data.json --measurement-interval=60000
 Successfully read data for 1 stream/streams with 1 step/steps.
*** Measurement Settings ***
  Batch size: 1
  Service Kind: Triton
  Using "time_windows" mode for stabilization
  Measurement window: 60000 msec
  Using synchronous calls for inference
  Stabilizing using average latency

Request concurrency: 1
Request for unknown model: '/models::ensemble' is not found
root@dev-dsk-vvijeth-2c-306acd45:/workspace# perf_analyzer -m ensemble --input-data data.json --measurement-interval=60000
 Successfully read data for 1 stream/streams with 1 step/steps.
*** Measurement Settings ***
  Batch size: 1
  Service Kind: Triton
  Using "time_windows" mode for stabilization
  Measurement window: 60000 msec
  Using synchronous calls for inference
  Stabilizing using average latency

Request concurrency: 1
Request for unknown model: '/models::ensemble' is not found
root@dev-dsk-vvijeth-2c-306acd45:/workspace# perf_analyzer -m ensemble --input-data data.json --measurement-interval=60000
 Successfully read data for 1 stream/streams with 1 step/steps.
*** Measurement Settings ***
  Batch size: 1
  Service Kind: Triton
  Using "time_windows" mode for stabilization
  Measurement window: 60000 msec
  Using synchronous calls for inference
  Stabilizing using average latency

Request concurrency: 1
Request for unknown model: '/models::ensemble' is not found
root@dev-dsk-vvijeth-2c-306acd45:/workspace# perf_analyzer -m ensemble --input-data data.json --measurement-interval=60000
 Successfully read data for 1 stream/streams with 1 step/steps.
*** Measurement Settings ***
  Batch size: 1
  Service Kind: Triton
  Using "time_windows" mode for stabilization
  Measurement window: 60000 msec
  Using synchronous calls for inference
  Stabilizing using average latency

Request concurrency: 1
Request for unknown model: '/models::ensemble' is not found
```


### vijetha35 · 2024-09-03

> @matthewkotila or @ganeshku1 any ideas? It looks like the model endpoint is different than what we would expect.
> 
> @vijetha35 when you launched the server, did the sagemaker wrapper change the endpoints?

All the endpoints are up:
```
I0830 23:02:15.966203 709 grpc_server.cc:2451] Started GRPCInferenceService at 0.0.0.0:8001
I0830 23:02:15.966426 709 http_server.cc:3558] Started HTTPService at 0.0.0.0:8000
I0830 23:02:16.007674 709 sagemaker_server.cc:293] Started Sagemaker HTTPService at 0.0.0.0:8080
I0830 23:02:16.048653 709 http_server.cc:187] Started Metrics Service at 0.0.0.0:8002
```

### nv-hwoo · 2024-09-03

@vijetha35 I see that you are using a bit outdated triton version. Does the error persist when you use one of the latest ones? (I'm assuming you are using 23.08 for both server _and_ sdk container)

Also, to help us verify that this is indeed a bug in the codebase, could you provide a small reproducer ensemble model? 

### vijetha35 · 2024-09-05

Correct, I am using the same version for both server and sdk container. 
I dont think this error is specific to it being because of an outdated version as I have been able to previously use the base triton image against another model ensemble model (not the current one, but similar structure ) against the SDK. 
Is there a way I can override the base ping 

### nv-hwoo · 2025-02-03

@vijetha35 sorry for the delayed response. Are you still encountering the same problem?

### the-david-oy · 2025-03-03

Closing due to inactivity. If you would like to reopen this issue for follow-up, let us know.
