# HQQ

source: https://github.com/dropbox/hqq/releases

# Releases: dropbox/hqq

Releases · dropbox/hqq

## Release list

## v0.2.8.post1

Minor toml file patch

## v0.2.8

## v0.2.7.post1

## v0.2.7

## v0.2.6

- Fix cuda build
`torchcompile()`

support for hqq_aten- bfloat16 support for vllm/hqq
- Update vllm utils to support
`hqq_gemlite`

and`hqq_torch`

aliases - FIx vLLM v1 issues
- Extend
`save_to_safetensors`

to VLMs

**Full Changelog**: `v0.2.5...0.2.6`

## v0.2.5

## v.0.2.3.post1

Bug fixes:

- Check
`W_q`

in state dict to fix peft issue[#151](https://github.com/dropbox/hqq/issues/151) - Fix bugs related to
`AutoHQQHFModel.save_to_safetensors`


## v0.2.3

- VLLM support via patching - GemLite backend + on-the-fly quantization
- Add support for Aria
- Add support to load quantized SequenceClassification
- Faster decoding via (custom cudagraphs, sdpa math backend, etc.)
- Fix bugs related torch compile and hf_generator related to the newer transformers versions
- Fix bugs related to saving quantized models with no grouping
- Fix bugs related to saving large quantized models
- Update examples
- Add support for HQQLinear
`.to(device)`


## v0.2.2

## v.0.2.1

## HQQ v0.2.1

`HQQLinear.state_dict()`

for non-initialized layers. Mainly used in for[huggingface/transformers#33141](https://github.com/huggingface/transformers/pull/33141)