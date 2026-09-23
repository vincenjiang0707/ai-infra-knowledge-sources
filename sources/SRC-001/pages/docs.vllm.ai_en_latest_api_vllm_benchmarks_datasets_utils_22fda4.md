source: https://docs.vllm.ai/en/latest/api/vllm/benchmarks/datasets/utils/
lastmod: 2026-09-23

#

`vllm.benchmarks.datasets.utils`

[¶](https://docs.vllm.ai#vllm.benchmarks.datasets.utils)

Shared utilities for benchmark dataset sampling.

Functions:

-
–[get_sampling_params](https://docs.vllm.ai#vllm.benchmarks.datasets.utils.get_sampling_params)Sample per-request input/output token lengths and vocab offsets.


##

`_resolve_range_ratios(range_ratio)`

[¶](https://docs.vllm.ai#vllm.benchmarks.datasets.utils._resolve_range_ratios)

Return `(input_range_ratio, output_range_ratio)`

from *range_ratio*.

*range_ratio* is either a single float (used for both input and output) or a dict with `"input"`

and `"output"`

keys.

## Source code in `vllm/benchmarks/datasets/utils.py`


##

`get_sampling_params(rng, num_requests, range_ratio, input_len, output_len, tokenizer)`

[¶](https://docs.vllm.ai#vllm.benchmarks.datasets.utils.get_sampling_params)

Sample per-request input/output token lengths and vocab offsets.

Lengths are drawn uniformly from integer ranges around the configured means, controlled by *range_ratio*. It may be a single `float`

(applied to both input and output) or a `dict`

with `"input"`

and `"output"`

keys for independent control.

Tokenizer special tokens are subtracted from `input_len`

before computing the sampling interval.

Returns:

-

–[ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray)(input_lens, output_lens, offsets) – three 1-D

`np.ndarray`

of -

–[ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray)shape

`(num_requests,)`

.