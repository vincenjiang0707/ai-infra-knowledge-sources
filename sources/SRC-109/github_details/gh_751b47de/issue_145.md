# [Issue #145] How to send binary data (audio file) in perf_analyzer?

source: https://github.com/triton-inference-server/perf_analyzer/issues/145
state: open | updated: 2025-09-02T17:30:11Z
labels: question

## 正文

**Description**
(same issue https://github.com/triton-inference-server/server/issues/3206)

I have a triton model that accepts a binary string. I want to send a wav file, if I do it through the client - everything works, if through the perf analyzer - it does not work.

**Triton Information**

Triton: `nvcr.io/nvidia/tritonserver:23.01-py3`
Triton SDK for perf analyzer: `nvcr.io/nvidia/tritonserver:23.07-py3-sdk`

**To Reproduce**

config.pbtxt
```
name: "conformer_full_model"
backend: "python"

input [
  {
    name: "IN"
    data_type: TYPE_STRING 
    dims: [1]
  }
]

output [
  {
    name: "OUT"
    data_type: TYPE_STRING
    dims: [1]
  }
]

instance_group [
  { 
    count: 1
    kind: KIND_GPU 
  }
]
```

If I'm trying to send a `wav` file:
```
perf_analyzer -m conformer_full_model --input-data data/ -u audio-triton.ap-triton.svc:8000
error: Failed to init manager inputs: provided data for input IN has 29 elements, expect 1
```
  
If I'm trying to send a binary string of a `wav` file:
Generated as follows
```
with open("data/in.wav", "rb") as content_file:
    content = content_file.read()
with open('IN', 'w') as f:
    f.write(str(content))
# RIFFx\x15\x00\x00WAVEfmt \x10\x00\x00\x00\x01\x00\x01\x00@\x1f...
```

```
perf_analyzer -m conformer_full_model --input-data data/ -u audio-triton.ap-triton.svc:8000
```

The string is forwarded, but after `in_0.as_numpy()[0]` it looks like `b'RIFFx\\x15\\x00\\x00WAVEfmt \\x10\\x00\\x00\\x00\\x01\\x00\\x01\\x00@\\x1f...'`.
But it should look like this `b'RIFFx\x15\x00\x00WAVEfmt \x10\x00\x00\x00\x01\x00\x01\x00@\x1f`




client.py is working
```
import tritonclient.grpc as grpcclient
import numpy as np
triton_client = grpcclient.InferenceServerClient(url="audio-triton.ap-triton.svc:8001")
model_name = 'conformer_full_model'
inputs = []
outputs = []
with open("data/in.wav", 'rb') as content_file:
    content = content_file.read()
input0_data = np.asarray(content)
inputs.append(grpcclient.InferInput('IN', [1], "BYTES"))
inputs[0].set_data_from_numpy(input0_data.reshape([1]))
outputs.append(grpcclient.InferRequestedOutput('OUT'))
results = triton_client.infer(
        model_name=model_name,
        inputs=inputs,
        outputs=outputs)
result = results.as_numpy('OUT')
```

## 评论 (18)

### oandreeva-nv · 2023-12-15

@matthewkotila, by any chance would you happen to know the solution for this issue?

### the-david-oy · 2024-02-20

CC: @matthewkotila 

### lucidyan · 2024-03-12

Experienced the same issue of inability to profile my model with native tools. @dyastremsky Any ideas where it could be answered? 

### the-david-oy · 2024-03-12

The team working on Tools who would know more (like @matthewkotila) is quite occupied at the moment, so there will be a delay in response.

I am not familiar with the specific requirements of PA input files, especially in an audio context, but I did see [this unofficial solution](https://github.com/pehonnet/sherpa/blob/894b73acedec522b8d566f866525bdecc1f25c9c/triton/client/generate_perf_input.py#L1) available that may be helpful in the meantime. Instructions for running these are [here](https://github.com/pehonnet/sherpa/blob/894b73acedec522b8d566f866525bdecc1f25c9c/triton/client/generate_perf_input.py#L1). This solution may also provide some direction, though note that it's for older versions of Triton.

### lucidyan · 2024-03-12

Thanks for the information! 

Looks like the library examples use JSON to send WAV PCM data instead of the more efficient raw binary WAV format. Not ideal since it requires changing Triton model signatures, but could work as a temporary fix if there aren't better options right now.

### the-david-oy · 2024-03-12

Thanks for responding. Some more information for this use case here as well: https://github.com/triton-inference-server/server/issues/3206

### MatthieuToulemont · 2024-06-14

I have the same issue for images, I usually send the images as encoded bytes to Triton and I would like to be able to use the perf analyzer to benchmark my pipelines. 


### kzelias · 2024-07-26

There is a solution for a single file.
Take the `.wav` file, rename it to the name of our input. For example `IN` for config above. And put it in an empty folder `data`. Find out shape or take any.
Then try
`perf_analyzer -m {MODEL_NAME} -b 1 --input-data data/ --shape IN:{SHAPE} -u {podname.namespace.svc}:8000`

After that you may get an error with shape.
`error: Failed to init manager inputs: provided data for input IN has 5255 elements, expect 29`
You'll just have to change the shape.

But I still don't understand how to get this to work on multiple files.

### matthewkotila · 2024-08-06

> @kzelias: ... But I still don't understand how to get this to work on multiple files.

Could you elaborate? If your model has multiple inputs that you want to supplied binary data for, you should be able to include one file per input in the `data/` directory, and Perf Analyzer will use each respective input binary file as the data for those inputs when sending inference requests to the model.

### kzelias · 2024-08-07

@matthewkotila, It's not about multiple inputs. It's about multiple requests.
With the --input-data parameter, I can only send 1 file per input from the `data/` folder.
But I want to send many different files iteratively.

Like here.
https://docs.nvidia.com/deeplearning/triton-inference-server/archives/triton-inference-server-2280/user-guide/docs/user_guide/perf_analyzer.html#real-input-data

### matthewkotila · 2024-08-07

Unfortunately we don't support supplying binary files for more than one request, but you should be able to convert the binary data into b64 representation and include that in an input data JSON supplied to PA. That will allow you to supply more than one request's worth of input data.

I agree, what you've request would be good to have--I've noted the feature request but don't have a timeline of when we would be able to work on it/deliver it.

### kzelias · 2024-08-08

@matthewkotila 
If I use b64 + json, I will need to change the logic of the triton service, right? Would need to decode b64.

### MatthieuToulemont · 2024-08-08

> If I use b64 + json, I will need to change the logic of the triton service, right? Would need to decode b64.


I am doing this for encoded images for benchmarking, but in production I sent bytes directly. The cost of decoding b64 is not that big so the benchmark should not be too far off 

### matthewkotila · 2024-08-08

> @kzelias: @matthewkotila
> If I use b64 + json, I will need to change the logic of the triton service, right? Would need to decode b64.

The decoding of the b64 data happens inside Perf Analyzer (the client) before sending to the server. You wouldn't have to change anything regarding how you set up your triton service. But yes, it is client-side computational time that theoretically could impact PA's ability to maintain concurrency or a desired request rate (but unlikely as above person mentioned), and could be lessened with the feature request you made.

### Prots · 2024-10-18

@matthewkotila hello, do you have an example how to convert wav file to b64 json which supported by PA. I've tried different ways but received errors like `Thread [0] had error: incomplete string data for inference input 'input', expecting string of length 808333357 but only 4881420 bytes available`

### the-david-oy · 2025-02-06

@nv-hwoo, do you happen to have an example of this? You worked on a related problem recently.

### DataXujing · 2025-08-30

 have the same issue for images, I usually send the images as encoded bytes to Triton and I would like to be able to use the perf analyzer to benchmark my pipelines.

### the-david-oy · 2025-09-02

In case it's helpful, you can look at how GenAI-Perf generates and encodes [audio](https://github.com/triton-inference-server/perf_analyzer/blob/main/genai-perf/genai_perf/inputs/retrievers/synthetic_audio_generator.py) and [image](https://github.com/triton-inference-server/perf_analyzer/blob/main/genai-perf/genai_perf/inputs/retrievers/synthetic_image_generator.py) data. That data then gets sent as is to Perf Analyzer in payloads compiled [here](https://github.com/triton-inference-server/perf_analyzer/blob/main/genai-perf/genai_perf/inputs/converters/openai_chat_completions_converter.py).
