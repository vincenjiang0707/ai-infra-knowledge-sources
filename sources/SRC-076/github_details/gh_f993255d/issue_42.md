# [Issue #42] [Feature] Add benchmark for AWS Trainium and Inferentia accelerators

source: https://github.com/ScalingIntelligence/KernelBench/issues/42
state: closed | updated: 2025-06-01T22:04:37Z
labels: 

## 正文

Libraries such as [Optimum Neuron](https://pypi.org/project/optimum-neuron/) and the [AWS Neuron SDK](https://github.com/aws-neuron/aws-neuron-sdk) do not have efficient kernel implementations for full coverage of `pytorch`.

This benchmark could serve as a community driven development accelerator for this missing support.

## 评论 (1)

### simonguozirui · 2025-06-01

Thank you for taking an interest in our project and the suggestion!
We spoke with the AWS Trainium team this spring and are interested in adding [NKI](https://awsdocs-neuron.readthedocs-hosted.com/en/latest/general/nki/nki_faq.html) as a supported backend for KernelBench. We welcome contributions towards that!
