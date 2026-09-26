source: https://github.com/vllm-project/guidellm/issues/602

### Bug Description

### Description

I am benchmarking Llama 3.1 8B on an NVIDIA H100 GPU. When running in concurrent mode, I observed highly inconsistent metrics:

- A significant discrepancy between Mean and Median RPS and TPUT metrics.
- The Standard Deviation (std) for the RPS metric reached ~900, even though the actual maximum RPS was around 50.

### Observations

### Debug

I suppose the problem is caused by a very low [threshold](https://github.com/vllm-project/guidellm/blob/4786a12d17f8c9c9a6de87e429c1d926085a0ceb/src/guidellm/schemas/statistics.py#L318) for merging. In concurrent mode, many requests can finish almost simultaneously, which leads to *durations* being as low as 1e-4 in [this line](https://github.com/vllm-project/guidellm/blob/4786a12d17f8c9c9a6de87e429c1d926085a0ceb/src/guidellm/schemas/statistics.py#L380), resulting in an inflated rate. I set the threshold to 1.0 and received more stable results.

### Expected Behavior

Stable quantile metrics and low variance

### Steps to Reproduce

Below code for reproducing problem: start model in sglang and benchmark scenario

model start:

```
python3 -m sglang.launch_server \
--model-path /models/Llama/Llama3.1-8B-Instruct/ \
--tp=1 \
--dp=1 \
--enable-metrics \
--disable-radix-cache \
```


scenario.json:

```
{
"profile": "concurrent",
"rate": 50,
"max_seconds": 10,
"target": "http://localhost:30000",
"data": "prompt_tokens=128,output_tokens=128",
"processor": "/models/Llama/Llama3.1-8B-Instruct/",
}
```


### Operating System

Ubunty 22.04

### Python Version

Python 3.12.12

### GuideLLM Version

guidellm version: 0.6.0.dev75

### Installation Method

pip install guidellm

### Installation Details

*No response*

### Error Messages or Stack Traces

### Additional Context

*No response*

## Bug Description

## Description

I am benchmarking Llama 3.1 8B on an NVIDIA H100 GPU. When running in concurrent mode, I observed highly inconsistent metrics:

## Observations

## Debug

I suppose the problem is caused by a very low threshold for merging. In concurrent mode, many requests can finish almost simultaneously, which leads to

durationsbeing as low as 1e-4 in this line, resulting in an inflated rate. I set the threshold to 1.0 and received more stable results.## Expected Behavior

Stable quantile metrics and low variance

## Steps to Reproduce

Below code for reproducing problem: start model in sglang and benchmark scenario

model start:

scenario.json:

## Operating System

Ubunty 22.04

## Python Version

Python 3.12.12

## GuideLLM Version

guidellm version: 0.6.0.dev75

## Installation Method

pip install guidellm

## Installation Details

No response## Error Messages or Stack Traces

## Additional Context

No response