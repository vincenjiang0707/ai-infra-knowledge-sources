source: https://docs.vllm.ai/en/latest/api/vllm/benchmarks/datasets/create_txt_slices_dataset/
lastmod: 2026-09-23

#

`vllm.benchmarks.datasets.create_txt_slices_dataset`

[¶](https://docs.vllm.ai#vllm.benchmarks.datasets.create_txt_slices_dataset)

Convert a plain-text file (local path or URL) into a JSONL dataset compatible with `CustomDataset`

(`--dataset-name custom`

), by randomly slicing the tokenized text into prompts.

Each line of the output JSONL contains a `prompt`

(decoded from a random slice of the tokenized source text) and an `output_tokens`

count.

### Usage[¶](https://docs.vllm.ai#vllm.benchmarks.datasets.create_txt_slices_dataset--usage)

::

```
python -m vllm.benchmarks.datasets.create_txt_slices_dataset \
--input sonnet.txt \
--output sonnet_dataset.jsonl \
--tokenizer gpt2 \
--num-prompts 1000 \
--input-len 1024 \
--output-len 128
```


The resulting JSONL file can then be used with the serving benchmark::

```
python -m vllm.benchmarks.serve \
--dataset-name custom \
--dataset-path sonnet_dataset.jsonl \
...
```


Functions:

-
–[create_txt_slices_jsonl](https://docs.vllm.ai#vllm.benchmarks.datasets.create_txt_slices_dataset.create_txt_slices_jsonl)Read

*input_path*, slice it into prompts, and write JSONL to -
–[load_text](https://docs.vllm.ai#vllm.benchmarks.datasets.create_txt_slices_dataset.load_text)Load text from a local file or URL.


##

`create_txt_slices_jsonl(*, input_path, output_path, tokenizer_name, num_prompts, input_len, output_len, range_ratio=0.0, seed=0, trust_remote_code=False)`

[¶](https://docs.vllm.ai#vllm.benchmarks.datasets.create_txt_slices_dataset.create_txt_slices_jsonl)

Read *input_path*, slice it into prompts, and write JSONL to *output_path*.

## Source code in `vllm/benchmarks/datasets/create_txt_slices_dataset.py`


##

`load_text(path)`

[¶](https://docs.vllm.ai#vllm.benchmarks.datasets.create_txt_slices_dataset.load_text)

Load text from a local file or URL.