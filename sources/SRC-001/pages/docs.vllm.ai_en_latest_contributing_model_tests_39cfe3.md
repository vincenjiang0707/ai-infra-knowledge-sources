source: https://docs.vllm.ai/en/latest/contributing/model/tests/
lastmod: 2026-09-24

# Unit Testing[¶](https://docs.vllm.ai#unit-testing)

This page explains how to write unit tests to verify the implementation of your model.

## Required Tests[¶](https://docs.vllm.ai#required-tests)

These tests are necessary to get your PR merged into vLLM library. Without them, the CI for your PR will fail.

### Model loading[¶](https://docs.vllm.ai#model-loading)

Include an example HuggingFace repository for your model in [ tests/models/registry.py](https://github.com/vllm-project/vllm/blob/main/tests/models/registry.py). This enables a unit test that loads dummy weights to ensure that the model can be initialized in vLLM.

Important

The list of models in each section should be maintained in alphabetical order.

Tip

If your model requires a development version of HF Transformers, you can set `min_transformers_version`

to skip the test in CI until the model is released.

## Optional Tests[¶](https://docs.vllm.ai#optional-tests)

These tests are optional to get your PR merged into vLLM library. Passing these tests provides more confidence that your implementation is correct, and helps avoid future regressions.

### Model correctness[¶](https://docs.vllm.ai#model-correctness)

These tests compare the model outputs of vLLM against [HF Transformers](https://github.com/huggingface/transformers). You can add new tests under the subdirectories of [ tests/models](https://github.com/vllm-project/vllm/tree/main/tests/models).

#### Generative models[¶](https://docs.vllm.ai#generative-models)

For [generative models](https://docs.vllm.ai/models/generative_models/), there are two levels of correctness tests, as defined in [ tests/models/utils.py](https://github.com/vllm-project/vllm/blob/main/tests/models/utils.py):

- Exact correctness (
`check_outputs_equal`

): The text outputted by vLLM should exactly match the text outputted by HF. - Logprobs similarity (
`check_logprobs_close`

): The logprobs outputted by vLLM should be in the top-k logprobs outputted by HF, and vice versa.

#### Pooling models[¶](https://docs.vllm.ai#pooling-models)

For [pooling models](https://docs.vllm.ai/models/pooling_models/), we simply check the cosine similarity, as defined in [ tests/models/utils.py](https://github.com/vllm-project/vllm/blob/main/tests/models/utils.py).

### Multi-modal processing[¶](https://docs.vllm.ai#multi-modal-processing)

#### Common tests[¶](https://docs.vllm.ai#common-tests)

Adding your model to [ tests/models/multimodal/processing/test_common.py](https://github.com/vllm-project/vllm/blob/main/tests/models/multimodal/processing/test_common.py) verifies that the following input combinations result in the same outputs:

- Text + multi-modal data
- Tokens + multi-modal data
- Text + cached multi-modal data
- Tokens + cached multi-modal data

#### Model-specific tests[¶](https://docs.vllm.ai#model-specific-tests)

You can add a new file under [ tests/models/multimodal/processing](https://github.com/vllm-project/vllm/tree/main/tests/models/multimodal/processing) to run tests that only apply to your model.

For example, if the HF processor for your model accepts user-specified keyword arguments, you can verify that the keyword arguments are being applied correctly, such as in [ tests/models/multimodal/processing/test_phi3v.py](https://github.com/vllm-project/vllm/blob/main/tests/models/multimodal/processing/test_phi3v.py).