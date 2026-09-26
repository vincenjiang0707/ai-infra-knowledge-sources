# [Issue #406] Using genai-perf to test the performance of dynamo-run failed.

source: https://github.com/triton-inference-server/perf_analyzer/issues/406
state: open | updated: 2025-06-27T09:22:55Z
labels: 

## 正文

1. I'm running an official dynamo-run example, as shown in the image below：
Terminal 1：

![Image](https://github.com/user-attachments/assets/fa37ada7-e523-4b53-b71e-343257785cce)

Terminal 2：

![Image](https://github.com/user-attachments/assets/e38acc7e-6bd2-47b6-a695-fd7be3042576)

2.
Terminal 3：
start a docker container with "dynamo:latest-vllm" docker image, run "

![Image](https://github.com/user-attachments/assets/a8777919-6f99-4d3c-945d-98609a2d88f0)

"
but I got ERROR message, as shown below:

![Image](https://github.com/user-attachments/assets/68bfd79c-52b1-400a-97cd-68b7c12341e2)

How to fix it? Thank you!

## 评论 (6)

### Dmax001 · 2025-06-26

I referred to the official documentation of genai-perf: https://github.com/triton-inference-server/perf_analyzer/blob/main/genai-perf/docs/dynamo.md

### debermudez · 2025-06-26

Because you are hitting a localhost ip address, can you try removing the `--endpoint` option for now?


### Dmax001 · 2025-06-26

> Because you are hitting a localhost ip address, can you try removing the `--endpoint` option for now?

Still not working. When using the dynamo-run command, I can't see its HTTP service address and port number. It feels like using the genai-perf profile command is just a shot in the dark. Need official help.

### ajcasagrande · 2025-06-26

@Dmax001 you need to specify `in=http` in your dynamo-run to serve dynamo in an OpenAI friendly format. `dynamo-run in=http out=...`

And then in genai-perf, use `--url localhost:8080` like you did, but remove the `--endpoint dyn...`

### Dmax001 · 2025-06-27

@ajcasagrande 
Thank you! 
The previous issue has been resolved. But a new problem has come up:

![Image](https://github.com/user-attachments/assets/a9e58720-5181-4a1f-a584-1219beb223b4)

Do you know what might be causing this? And how can it be solved?

### Dmax001 · 2025-06-27

@debermudez @ajcasagrande 
Oh my god!
I modified the temperature in sampling_params in server_vllm.py under the dynamo/lib/bindings/python/examples/hello_world directory of the Dynamo library, fixing it to 1.0. 
Then, after rerunning it, I actually managed to successfully generate the performance benchmark data. But I still don’t quite understand—why did this make genai-perf profile work?

![Image](https://github.com/user-attachments/assets/ce9e5da4-aa4b-43e5-8f2c-c9daaba2b1ba)
