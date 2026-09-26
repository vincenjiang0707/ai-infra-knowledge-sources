# [Issue #105] perf_analyzer with real input data byte size mismatch

source: https://github.com/triton-inference-server/perf_analyzer/issues/105
state: closed | updated: 2025-03-05T06:17:18Z
labels: 

## 正文

when i use input-data by perf
```
perf_analyzer -m bls --input-data input --shape INPUT:63
```
it is failing with the following error:
```
error: Failed to init manager inputs: provided data for input INPUT has 67 byte elements, expect 63
```
This is how I get input-data
```
  req_data = {
      "url": "test22",
      "room_id": 22986256,
      "timestamp": 1726638260
  }
  req_json = json.dumps(req_data).encode("utf-8")
  req_numpy = np.array([[req_json]]) # this is input
  req_numpy.tofile("input/INPUT") #this is my input binary file
  print(len(req_json)). # result is 63
```
I check this binary file by 'cat input/INPUT'
```
{"url": "test22", "room_id": 22986256, "timestamp": 1726638260}
```
This is my bls config.pbtxt
```
name: "bls"
backend: "python"
max_batch_size: 16
input [
  {
    name: "INPUT"
    data_type: TYPE_STRING
    dims: [ -1 ]
  }
]
output [
  {
    name: "OUTPUT"
    data_type: TYPE_STRING
    dims: [ -1 ]
  }
]

instance_group [
  {
    count: 1
    kind: KIND_CPU
  }
]
```
Has anyone seen it before ?

## 评论 (5)

### matthewkotila · 2024-09-30

You may need to use `--shape INPUT:67` to account for the 4-byte unsigned integer prepended to the front containing the length of the following bytes:

https://github.com/triton-inference-server/perf_analyzer/blob/main/docs/input_data.md#real-input-data

> Note that for STRING type, an element is represented by a 4-byte unsigned integer giving the length followed by the actual bytes. The byte array to be encoded using base64 must include the 4-byte unsigned integers.

### XIAO-FAN-5257 · 2024-10-01

> You may need to use `--shape INPUT:67` to account for the 4-byte unsigned integer prepended to the front containing the length of the following bytes:
> 
> https://github.com/triton-inference-server/perf_analyzer/blob/main/docs/input_data.md#real-input-data
> 
> > Note that for STRING type, an element is represented by a 4-byte unsigned integer giving the length followed by the actual bytes. The byte array to be encoded using base64 must include the 4-byte unsigned integers.

I tried to modify this shape parameter, but it still reported the following error
```
perf_analyzer -m bls --input-data input --shape INPUT:67
```
```
error: Failed to init manager inputs: provided data for input INPUT has 67 byte elements, expect 67
```


### XIAO-FAN-5257 · 2024-10-03

> > You may need to use `--shape INPUT:67` to account for the 4-byte unsigned integer prepended to the front containing the length of the following bytes:
> > https://github.com/triton-inference-server/perf_analyzer/blob/main/docs/input_data.md#real-input-data
> > > Note that for STRING type, an element is represented by a 4-byte unsigned integer giving the length followed by the actual bytes. The byte array to be encoded using base64 must include the 4-byte unsigned integers.
> 
> I tried to modify this shape parameter, but it still reported the following error
> 
> ```
> perf_analyzer -m bls --input-data input --shape INPUT:67
> ```
> 
> ```
> error: Failed to init manager inputs: provided data for input INPUT has 67 byte elements, expect 67
> ```
@matthewkotila this error is so strange

### nv-hwoo · 2025-02-03

@XIAO-FAN-5257 Sorry for delayed response. Are you still encountering the same problem? 

### XIAO-FAN-5257 · 2025-03-04

> [@XIAO-FAN-5257](https://github.com/XIAO-FAN-5257) Sorry for delayed response. Are you still encountering the same problem?

Thanks!  @nv-hwoo 
I noticed that you have a new commit. I pulled the project again and compiled it. Now there is no problem.
```
 /workspace/perf_analyzer/build/perf_analyzer/src/perf-analyzer-build/perf_analyzer -m bls  --input-data ./client/input --shape INPUT:1
```
