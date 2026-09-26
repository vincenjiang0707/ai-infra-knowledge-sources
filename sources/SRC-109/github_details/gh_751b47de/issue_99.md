# [Issue #99] perf_analyzer with real input data byte size mismatch 

source: https://github.com/triton-inference-server/perf_analyzer/issues/99
state: closed | updated: 2024-09-29T03:44:02Z
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

## 评论 (1)

### XIAO-FAN-5257 · 2024-09-29

No reply，just close
