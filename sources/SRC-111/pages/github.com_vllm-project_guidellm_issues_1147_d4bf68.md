source: https://github.com/vllm-project/guidellm/issues/1147

### Bug Description

When passing, for example,

*--data kind=synthetic_text,prompt_tokens=64,output_tokens=32*

--data kind=synthetic_image,resolution=720p,format=jpeg,seed=11

(and any other synth** options) - everything besides synthetic_text will be dropped.

### Expected Behavior

When synthetic_image/video are passed, the output should contain their statistics too. Today they're completely ignored because they're not passed initially.

### Steps to Reproduce

- run guidellm mock-server --host 127.0.0.1 --port 8000 --model gpt2 --request-latency 0.05 --ttft-ms 20 --itl-ms 2 --output-tokens 3 --image-tokens 576 --video-tokens 1024
- add

--data kind=synthetic_text,prompt_tokens=64,output_tokens=32

--data kind=synthetic_image,resolution=720p,format=jpeg,seed=11

parameters to the guidellm run (client side)
- Image-related statistics is not displayed in the benchmark report

### Operating System

Fedora v44

### Python Version

Python 3.14

### GuideLLM Version

0.8.0.dev19

### Installation Method

pip install guidellm[all]

### Installation Details

*No response*

### Error Messages or Stack Traces

### Additional Context

*No response*

## Bug Description

When passing, for example,

--data kind=synthetic_text,prompt_tokens=64,output_tokens=32--data kind=synthetic_image,resolution=720p,format=jpeg,seed=11

(and any other synth** options) - everything besides synthetic_text will be dropped.

## Expected Behavior

When synthetic_image/video are passed, the output should contain their statistics too. Today they're completely ignored because they're not passed initially.

## Steps to Reproduce

--data kind=synthetic_text,prompt_tokens=64,output_tokens=32

--data kind=synthetic_image,resolution=720p,format=jpeg,seed=11

parameters to the guidellm run (client side)

## Operating System

Fedora v44

## Python Version

Python 3.14

## GuideLLM Version

0.8.0.dev19

## Installation Method

pip install guidellm[all]

## Installation Details

No response## Error Messages or Stack Traces

## Additional Context

No response