source: https://docs.vllm.ai/en/latest/api/vllm/benchmarks/datasets/datasets/
lastmod: 2026-09-23

#

`vllm.benchmarks.datasets.datasets`

[¶](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets)

This module defines a framework for sampling benchmark requests from various datasets. Each dataset subclass of BenchmarkDataset must implement sample generation. Supported dataset types include: - ShareGPT - Random (synthetic) - Sonnet - BurstGPT - HuggingFace - VisionArena

Classes:

-
–[AIMODataset](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.AIMODataset)Dataset class for processing a AIMO dataset with reasoning questions.

-
–[ASRDataset](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.ASRDataset)Dataset class for processing a ASR dataset for transcription.

-
–[BFCLDataset](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.BFCLDataset)Berkeley Function Calling Leaderboard dataset.

-
–[BenchmarkDataset](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.BenchmarkDataset) -
–[BlazeditDataset](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.BlazeditDataset)Blazedit Dataset.

-
–[BurstGPTDataset](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.BurstGPTDataset)Implements the BurstGPT dataset. Loads data from a CSV file and generates

-
–[ConversationDataset](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.ConversationDataset)Dataset for text-only conversation data.

-
–[CustomAudioDataset](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.CustomAudioDataset)Custom dataset for audio benchmarking. Loads data from a JSONL file. E.g.,

-
–[CustomDataset](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.CustomDataset)Implements the Custom dataset. Loads data from a JSONL file and generates

-
–[CustomImageDataset](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.CustomImageDataset)Implements the Custom image dataset. Loads data from a JSONL file and generates

-
–[GSM8KDataset](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.GSM8KDataset)GSM8K Dataset.

-
–[HuggingFaceDataset](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.HuggingFaceDataset)Base class for datasets hosted on HuggingFace.

-
–[HumanEvalDataset](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.HumanEvalDataset)HumanEvalDataset Dataset.

-
–[InstructCoderDataset](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.InstructCoderDataset)InstructCoder Dataset.

-
–[MLPerfDataset](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.MLPerfDataset)MLPerf Inference Dataset.

-
–[MMStarDataset](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.MMStarDataset)Lin-Chen/MMStar: https://huggingface.co/datasets/Lin-Chen/MMStar

-
–[MMVUDataset](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.MMVUDataset)MMVU Dataset.

-
–[MTBenchDataset](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.MTBenchDataset)MT-Bench Dataset.

-
–[MultiModalConversationDataset](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.MultiModalConversationDataset)Dataset for multimodal conversation data.

-
–[NextEditPredictionDataset](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.NextEditPredictionDataset)Dataset class for processing a Next Edit Prediction dataset.

-
–[RandomDataset](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.RandomDataset)Synthetic text-only dataset for serving/throughput benchmarks.

-
–[RandomDatasetForReranking](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.RandomDatasetForReranking)Random dataset specialized for the needs of scoring:

-
–[RandomMultiModalDataset](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.RandomMultiModalDataset)Synthetic multimodal dataset (text + images) that extends RandomDataset.

-
–[SampleRequest](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.SampleRequest)Represents a single inference request for benchmarking.

-
–[ShareGPTDataset](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.ShareGPTDataset)Implements the ShareGPT dataset. Loads data from a JSON file and generates

-
–[SonnetDataset](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.SonnetDataset)Simplified implementation of the Sonnet dataset. Loads poem lines from a

-
–[SpecBench](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.SpecBench)Implements the SpecBench dataset: https://github.com/hemingkx/Spec-Bench

-
–[SpeedBench](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.SpeedBench)SPEED-Bench dataset: https://huggingface.co/datasets/nvidia/SPEED-Bench.

-
–[TimedTrace](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.TimedTrace)Implements a base class to replay various timed traces.

-
–[VisionArenaDataset](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.VisionArenaDataset)Vision Arena Dataset.


Functions:

-
–[add_random_dataset_base_args](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.add_random_dataset_base_args)Add CLI arguments for base random dataset options.

-
–[add_random_multimodal_dataset_args](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.add_random_multimodal_dataset_args)Add CLI arguments for random multimodal dataset options.

-
–[gen_prompt_decode_to_target_len](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.gen_prompt_decode_to_target_len)Ensure decoded-then-encoded prompt length matches the target token length.

-
–[is_valid_sequence](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.is_valid_sequence)Validate a sequence based on prompt and output lengths.

-
–[process_audio](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.process_audio)Process a single audio input and return a (array, sample_rate) tuple.

-
–[process_image](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.process_image)Process a single image input and return a multimedia content dictionary.

-
–[process_video](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.process_video)Process a single video input and return a multimedia content dictionary.


##

`AIMODataset`

[¶](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.AIMODataset)

Bases: [HuggingFaceDataset](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.HuggingFaceDataset)

Dataset class for processing a AIMO dataset with reasoning questions.

## Source code in `vllm/benchmarks/datasets/datasets.py`


##

`ASRDataset`

[¶](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.ASRDataset)

Bases: [HuggingFaceDataset](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.HuggingFaceDataset)

Dataset class for processing a ASR dataset for transcription. Tested on the following set:

+---------------------------+----------------------------------------+--------------------------+-----------------------------+ | Dataset | Domain | Speaking Style | hf-subset | +---------------------------+----------------------------------------+--------------------------+-----------------------------+ | TED-LIUM | TED talks | Oratory | release1, release2, release3| | | | | release3-speaker-adaptation | | VoxPopuli | European Parliament | Oratory | en, de, it, fr, ... | | LibriSpeech | Audiobook | Narrated | "LIUM/tedlium" | | GigaSpeech | Audiobook, podcast, YouTube | Narrated, spontaneous | xs, s, m, l, xl, dev, test | | SPGISpeech | Financial meetings | Oratory, spontaneous | S, M, L, dev, test | | Earnings22-Cleaned-AA | Long form earnings calls | Prepared remarks, Q&A | test | | Earnings22-Tiny-Filtered | Earnings calls | Prepared remarks, Q&A | validation | | AMI | Meetings | Spontaneous | ihm, sdm | +---------------------------+----------------------------------------+--------------------------+-----------------------------+

## Source code in `vllm/benchmarks/datasets/datasets.py`


|
|

##

`BFCLDataset`

[¶](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.BFCLDataset)

Bases: [HuggingFaceDataset](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.HuggingFaceDataset)

Berkeley Function Calling Leaderboard dataset.

https://huggingface.co/datasets/gorilla-llm/Berkeley-Function-Calling-Leaderboard

BFCL ships one JSON-lines file per category at the repo root (e.g. `BFCL_v3_simple.json`

, `BFCL_v3_live_simple.json`

) rather than a single HuggingFace split. Each record has `{id, question, function}`

where `function`

uses a non-OpenAI schema dialect (`"type": "dict"`

).

## This dataset loader

- downloads the selected per-category files via
`hf_hub_download`

and interleaves rows round-robin so sampling is balanced - translates BFCL function schemas to OpenAI tool format
- sets :attr:
`SampleRequest.chat_messages`

directly and attaches`tools`

/`tool_choice`

via :attr:`SampleRequest.request_overrides`

, producing production-alike tool calling traffic when used with an`openai-chat`

backend

Methods:

-
–[load_data](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.BFCLDataset.load_data)Defer loading to :meth:

`sample`

where categories are known.

## Source code in `vllm/benchmarks/datasets/datasets.py`


|
|

###

`_translate_schema(node)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.BFCLDataset._translate_schema)

Recursively translate BFCL-flavored JSON schema to strict JSON Schema.

## Source code in `vllm/benchmarks/datasets/datasets.py`


##

`BenchmarkDataset`

[¶](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.BenchmarkDataset)

Bases: [ABC](https://docs.python.org/3/library/abc.html#abc.ABC)

Methods:

-
–[__init__](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.BenchmarkDataset.__init__)Initialize the BenchmarkDataset with an optional dataset path and random

-
–[apply_multimodal_chat_transformation](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.BenchmarkDataset.apply_multimodal_chat_transformation)Transform a prompt and optional multimodal content into a chat format.

-
–[get_lora_request](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.BenchmarkDataset.get_lora_request)Select a LoRA request using the specified assignment strategy.

-
–[get_random_lora_request](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.BenchmarkDataset.get_random_lora_request)Optionally select a random LoRA request.

-
–[get_round_robin_lora_request](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.BenchmarkDataset.get_round_robin_lora_request)Optionally select a LoRA request using deterministic round-robin.

-
–[load_data](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.BenchmarkDataset.load_data)Load data from the dataset path into self.data.

-
–[maybe_oversample_requests](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.BenchmarkDataset.maybe_oversample_requests)Oversamples the list of requests if its size is less than the desired

-
–[sample](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.BenchmarkDataset.sample)Abstract method to generate sample requests from the dataset.


## Source code in `vllm/benchmarks/datasets/datasets.py`


|
|

###

`__init__(dataset_path=None, random_seed=DEFAULT_SEED, disable_shuffle=False, **kwargs)`

[¶](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.BenchmarkDataset.__init__)

Initialize the BenchmarkDataset with an optional dataset path and random seed.

Parameters:

-

(`dataset_path`

[¶](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.BenchmarkDataset.__init__(dataset_path))`Optional[`

, default:[str](https://docs.python.org/3/builtins/stdtypes.html#str)]`None`

) –Path to the dataset. If None, it indicates that a default or random dataset might be used.

-

(`random_seed`

[¶](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.BenchmarkDataset.__init__(random_seed))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)`DEFAULT_SEED`

) –Seed value for reproducible shuffling or sampling. Defaults to DEFAULT_SEED.

-

(`disable_shuffle`

[¶](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.BenchmarkDataset.__init__(disable_shuffle))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`False`

) –If True, keep the dataset in its original order instead of shuffling it.


## Source code in `vllm/benchmarks/datasets/datasets.py`


###

`apply_multimodal_chat_transformation(prompt, mm_content=None)`

[¶](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.BenchmarkDataset.apply_multimodal_chat_transformation)

Transform a prompt and optional multimodal content into a chat format. This method is used for chat models that expect a specific conversation format.

## Source code in `vllm/benchmarks/datasets/datasets.py`


###

`get_lora_request(index, max_loras=None, lora_path=None, lora_assignment='random')`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.BenchmarkDataset.get_lora_request)

Select a LoRA request using the specified assignment strategy.

Parameters:

-

(`index`

[¶](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.BenchmarkDataset.get_lora_request(index))

) –[int](https://docs.python.org/3/builtins/functions.html#int)The request index (used for round-robin).

-

(`max_loras`

[¶](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.BenchmarkDataset.get_lora_request(max_loras))`Optional[`

, default:[int](https://docs.python.org/3/builtins/functions.html#int)]`None`

) –The maximum number of LoRAs available.

-

(`lora_path`

[¶](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.BenchmarkDataset.get_lora_request(lora_path))`Optional[`

, default:[str](https://docs.python.org/3/builtins/stdtypes.html#str)]`None`

) –Path to the LoRA parameters on disk.

-

(`lora_assignment`

[¶](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.BenchmarkDataset.get_lora_request(lora_assignment))

, default:[str](https://docs.python.org/3/builtins/stdtypes.html#str)`'random'`

) –Strategy for LoRA selection. 'random' (default) or 'round-robin'.


Returns:

-

–[LoRARequest](https://docs.vllm.ai/lora/request/#vllm.lora.request.LoRARequest)| NoneA new

`LoRARequest`

-

–[LoRARequest](https://docs.vllm.ai/lora/request/#vllm.lora.request.LoRARequest)| None(or

`None`

if not applicable).

## Source code in `vllm/benchmarks/datasets/datasets.py`


###

`get_random_lora_request(max_loras=None, lora_path=None)`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.BenchmarkDataset.get_random_lora_request)

Optionally select a random LoRA request.

This method is used when LoRA parameters are provided. It randomly selects a LoRA based on max_loras.

Parameters:

-

(`max_loras`

[¶](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.BenchmarkDataset.get_random_lora_request(max_loras))`Optional[`

, default:[int](https://docs.python.org/3/builtins/functions.html#int)]`None`

) –The maximum number of LoRAs available. If

`None`

, LoRA is not used. -

(`lora_path`

[¶](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.BenchmarkDataset.get_random_lora_request(lora_path))`Optional[`

, default:[str](https://docs.python.org/3/builtins/stdtypes.html#str)]`None`

) –Path to the LoRA parameters on disk. If

`None`

, LoRA is not used.

Returns:

-

–[LoRARequest](https://docs.vllm.ai/lora/request/#vllm.lora.request.LoRARequest)| NoneA new

`LoRARequest`

-

–[LoRARequest](https://docs.vllm.ai/lora/request/#vllm.lora.request.LoRARequest)| None(or

`None`

if not applicable).

## Source code in `vllm/benchmarks/datasets/datasets.py`


###

`get_round_robin_lora_request(index, max_loras=None, lora_path=None)`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.BenchmarkDataset.get_round_robin_lora_request)

Optionally select a LoRA request using deterministic round-robin.

This method cycles through LoRA IDs in order based on the request index, providing reproducible LoRA assignment.

Parameters:

-

(`index`

[¶](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.BenchmarkDataset.get_round_robin_lora_request(index))

) –[int](https://docs.python.org/3/builtins/functions.html#int)The request index used for round-robin selection.

-

(`max_loras`

[¶](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.BenchmarkDataset.get_round_robin_lora_request(max_loras))`Optional[`

, default:[int](https://docs.python.org/3/builtins/functions.html#int)]`None`

) –The maximum number of LoRAs available. If

`None`

, LoRA is not used. -

(`lora_path`

[¶](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.BenchmarkDataset.get_round_robin_lora_request(lora_path))`Optional[`

, default:[str](https://docs.python.org/3/builtins/stdtypes.html#str)]`None`

) –Path to the LoRA parameters on disk. If

`None`

, LoRA is not used.

Returns:

-

–[LoRARequest](https://docs.vllm.ai/lora/request/#vllm.lora.request.LoRARequest)| NoneA new

`LoRARequest`

-

–[LoRARequest](https://docs.vllm.ai/lora/request/#vllm.lora.request.LoRARequest)| None(or

`None`

if not applicable).

## Source code in `vllm/benchmarks/datasets/datasets.py`


###

`load_data()`

[¶](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.BenchmarkDataset.load_data)

Load data from the dataset path into self.data.

This method must be overridden by subclasses since the method to load data will vary depending on the dataset format and source.

Raises:

-

–[NotImplementedError](https://docs.python.org/3/builtins/exceptions.html#NotImplementedError)If a subclass does not implement this method.


## Source code in `vllm/benchmarks/datasets/datasets.py`


###

`maybe_oversample_requests(requests, num_requests, request_id_prefix='', no_oversample=False)`

[¶](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.BenchmarkDataset.maybe_oversample_requests)

Oversamples the list of requests if its size is less than the desired number.

Parameters:

-

(`requests`

[¶](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.BenchmarkDataset.maybe_oversample_requests(requests))`List[`

) –[SampleRequest](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.SampleRequest)]The current list of sampled requests.

-

(`num_requests`

[¶](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.BenchmarkDataset.maybe_oversample_requests(num_requests))

) –[int](https://docs.python.org/3/builtins/functions.html#int)The target number of requests.

-

(`request_id_prefix`

[¶](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.BenchmarkDataset.maybe_oversample_requests(request_id_prefix))

, default:[str](https://docs.python.org/3/builtins/stdtypes.html#str)`''`

) –The prefix applied to generated request identifiers.

-

(`no_oversample`

[¶](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.BenchmarkDataset.maybe_oversample_requests(no_oversample))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`False`

) –If True, return the requests unchanged instead of oversampling up to num_requests.


## Source code in `vllm/benchmarks/datasets/datasets.py`


###

`sample(tokenizer, num_requests, request_id_prefix='', no_oversample=False, **kwargs)`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.BenchmarkDataset.sample)

Abstract method to generate sample requests from the dataset.

Subclasses must override this method to implement dataset-specific logic for generating a list of SampleRequest objects.

Parameters:

-

(`tokenizer`

[¶](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.BenchmarkDataset.sample(tokenizer))`TokenizerLike`

) –The tokenizer to be used for processing the dataset's text.

-

(`num_requests`

[¶](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.BenchmarkDataset.sample(num_requests))

) –[int](https://docs.python.org/3/builtins/functions.html#int)The number of sample requests to generate.

-

(`request_id_prefix`

[¶](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.BenchmarkDataset.sample(request_id_prefix))

, default:[str](https://docs.python.org/3/builtins/stdtypes.html#str)`''`

) –The prefix of request_id.

-

(`no_oversample`

[¶](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.BenchmarkDataset.sample(no_oversample))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`False`

) –If True, do not oversample the dataset to reach num_requests.


Returns:

-

–[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[SampleRequest](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.SampleRequest)]list[SampleRequest]: A list of sample requests generated from the

-

–[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[SampleRequest](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.SampleRequest)]dataset.


## Source code in `vllm/benchmarks/datasets/datasets.py`


##

`BlazeditDataset`

[¶](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.BlazeditDataset)

Bases: [HuggingFaceDataset](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.HuggingFaceDataset)

Blazedit Dataset. https://github.com/ise-uiuc/blazedit

5k char version: vdaita/edit_5k_char 10k char version: vdaita/edit_10k_char

## Source code in `vllm/benchmarks/datasets/datasets.py`


|
|

##

`BurstGPTDataset`

[¶](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.BurstGPTDataset)

Bases: [BenchmarkDataset](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.BenchmarkDataset)

Implements the BurstGPT dataset. Loads data from a CSV file and generates sample requests based on synthetic prompt generation. Only rows with Model "GPT-4" and positive response tokens are used.

## Source code in `vllm/benchmarks/datasets/datasets.py`


|
|

##

`ConversationDataset`

[¶](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.ConversationDataset)

Bases: [HuggingFaceDataset](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.HuggingFaceDataset)

Dataset for text-only conversation data.

## Source code in `vllm/benchmarks/datasets/datasets.py`


##

`CustomAudioDataset`

[¶](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.CustomAudioDataset)

Bases: [CustomDataset](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.CustomDataset)

Custom dataset for audio benchmarking. Loads data from a JSONL file. E.g.,

Supports both: - Dedicated ASR models (e.g. Whisper) via openai-audio & /v1/audio/transcriptions - Chat-based audio models (e.g. Qwen2-Audio) via openai-chat & /v1/chat/completions

## Source code in `vllm/benchmarks/datasets/datasets.py`


|
|

##

`CustomDataset`

[¶](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.CustomDataset)

Bases: [BenchmarkDataset](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.BenchmarkDataset)

Implements the Custom dataset. Loads data from a JSONL file and generates sample requests based on conversation turns. E.g.,

{"prompt": "What is the capital of India?", "output_tokens": 10}
{"prompt": "What is the capital of Iran?", "output_tokens": 1520}
{"prompt": "What is the capital of China?", "output_tokens": 819}


## Source code in `vllm/benchmarks/datasets/datasets.py`


|
|

##

`CustomImageDataset`

[¶](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.CustomImageDataset)

Bases: [CustomDataset](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.CustomDataset)

Implements the Custom image dataset. Loads data from a JSONL file and generates sample requests based on conversation turns. E.g.,

{
"prompt": "How many red blocks in the given images?",
"image_files": ["path/to/image1.png", "path/to/image2.png"],
}
{
"prompt": "Which country has the most pokemons based on the given graphs?",
"image_files": ["path/to/image.png"],
}
{
"content": [
{"type": "text", "text": "Compare these images: "},
{"type": "image", "image": "path/to/image1.png"},
{"type": "text", "text": " and "},
{"type": "image_url", "image_url": {"url": "path/to/image2.png"}},
],
}


This is used to benchmark multimodal LLMs on arbitrary datasets.

## Source code in `vllm/benchmarks/datasets/datasets.py`


|
|

##

`GSM8KDataset`

[¶](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.GSM8KDataset)

Bases: [HuggingFaceDataset](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.HuggingFaceDataset)

GSM8K Dataset. https://huggingface.co/datasets/openai/gsm8k

We create a single turn dataset for GSM8K.

## Source code in `vllm/benchmarks/datasets/datasets.py`


##

`HuggingFaceDataset`

[¶](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.HuggingFaceDataset)

Bases: [BenchmarkDataset](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.BenchmarkDataset)

Base class for datasets hosted on HuggingFace.

Methods:

-
–[load_data](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.HuggingFaceDataset.load_data)Load data from HuggingFace datasets.


## Source code in `vllm/benchmarks/datasets/datasets.py`


###

`load_data()`

[¶](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.HuggingFaceDataset.load_data)

Load data from HuggingFace datasets.

## Source code in `vllm/benchmarks/datasets/datasets.py`


##

`HumanEvalDataset`

[¶](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.HumanEvalDataset)

Bases: [HuggingFaceDataset](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.HuggingFaceDataset)

HumanEvalDataset Dataset. https://huggingface.co/datasets/openai/openai_humaneval

We create a single turn dataset for HumanEval.

## Source code in `vllm/benchmarks/datasets/datasets.py`


##

`InstructCoderDataset`

[¶](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.InstructCoderDataset)

Bases: [HuggingFaceDataset](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.HuggingFaceDataset)

InstructCoder Dataset. https://huggingface.co/datasets/likaixin/InstructCoder

InstructCoder is the dataset designed for general code editing. It consists of 114,239 instruction-input-output triplets, and covers multiple distinct code editing scenario.

## Source code in `vllm/benchmarks/datasets/datasets.py`


|
|

##

`MLPerfDataset`

[¶](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.MLPerfDataset)

Bases: [HuggingFaceDataset](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.HuggingFaceDataset)

MLPerf Inference Dataset.

Dataset on HF: https://huggingface.co/datasets/mgoin/mlperf-inference-llama2-data https://huggingface.co/datasets/mgoin/mlperf-inference-llama3.1-data

## Each record contains

- "system_prompt": system role instruction.
- "question": user question.
- "output": reference answer.

We combine the system prompt and question into a chat-formatted prompt (using the tokenizer's chat template) and set the expected output length to the tokenized length of the provided reference answer.

## Source code in `vllm/benchmarks/datasets/datasets.py`


|
|

##

`MMStarDataset`

[¶](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.MMStarDataset)

Bases: [HuggingFaceDataset](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.HuggingFaceDataset)

Lin-Chen/MMStar: https://huggingface.co/datasets/Lin-Chen/MMStar refer to: https://github.com/sgl-project/SpecForge/pull/106

## Source code in `vllm/benchmarks/datasets/datasets.py`


|
|

##

`MMVUDataset`

[¶](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.MMVUDataset)

Bases: [HuggingFaceDataset](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.HuggingFaceDataset)

MMVU Dataset. https://huggingface.co/datasets/yale-nlp/MMVU

## Source code in `vllm/benchmarks/datasets/datasets.py`


|
|

##

`MTBenchDataset`

[¶](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.MTBenchDataset)

Bases: [HuggingFaceDataset](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.HuggingFaceDataset)

MT-Bench Dataset. https://huggingface.co/datasets/philschmid/mt-bench

We create a single turn dataset for MT-Bench. This is similar to Spec decoding benchmark setup in vLLM https://github.com/vllm-project/vllm/blob/9d98ab5ec/examples/offline_inference/eagle.py#L14-L18

## Source code in `vllm/benchmarks/datasets/datasets.py`


##

`MultiModalConversationDataset`

[¶](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.MultiModalConversationDataset)

Bases: [HuggingFaceDataset](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.HuggingFaceDataset)

Dataset for multimodal conversation data.

## Source code in `vllm/benchmarks/datasets/datasets.py`


##

`NextEditPredictionDataset`

[¶](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.NextEditPredictionDataset)

Bases: [HuggingFaceDataset](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.HuggingFaceDataset)

Dataset class for processing a Next Edit Prediction dataset.

## Source code in `vllm/benchmarks/datasets/datasets.py`


##

`RandomDataset`

[¶](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.RandomDataset)

Bases: [BenchmarkDataset](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.BenchmarkDataset)

Synthetic text-only dataset for serving/throughput benchmarks.

Strategy: - Sample input/output token lengths per request from integer-uniform ranges around configured means (controlled by range_ratio). - Prepend a fixed random prefix of length prefix_len. - Generate the remaining tokens as a reproducible sequence: (offset + index + arange(input_len)) % vocab_size. - Decode then re-encode/truncate to ensure prompt token counts match. - Uses numpy.default_rng seeded with random_seed for reproducible sampling.

Methods:

-
–[generate_token_sequence](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.RandomDataset.generate_token_sequence)Returns (prompt, total_input_len).

-
–[get_prefix](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.RandomDataset.get_prefix)Get the prefix for the dataset.


## Source code in `vllm/benchmarks/datasets/datasets.py`


|
|

###

`generate_token_sequence(*, tokenizer, prefix_token_ids, prefix_len, vocab_size, input_len, offset, index, allowed_tokens)`

[¶](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.RandomDataset.generate_token_sequence)

Returns (prompt, total_input_len).

NOTE: After decoding the prompt we have to encode and decode it again. This is done because in some cases N consecutive tokens give a string tokenized into != N number of tokens. For example for GPT2Tokenizer: [6880, 6881] -> ['Ġcalls', 'here'] -> [1650, 939, 486] -> ['Ġcall', 'sh', 'ere'] To avoid uncontrolled change of the prompt length, the encoded sequence is truncated before being decoded again.

## Source code in `vllm/benchmarks/datasets/datasets.py`


###

`get_prefix(tokenizer, allowed_tokens, prefix_len)`

[¶](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.RandomDataset.get_prefix)

Get the prefix for the dataset.

## Source code in `vllm/benchmarks/datasets/datasets.py`


##

`RandomDatasetForReranking`

[¶](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.RandomDatasetForReranking)

Bases: [RandomDataset](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.RandomDataset)

Random dataset specialized for the needs of scoring: - Batches of inputs - Inputs composed of pairs

## Source code in `vllm/benchmarks/datasets/datasets.py`


|
|

##

`RandomMultiModalDataset`

[¶](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.RandomMultiModalDataset)

Bases: [RandomDataset](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.RandomDataset)

Synthetic multimodal dataset (text + images) that extends RandomDataset.

Status: - Images: supported via synthetic RGB data. - Video: supported via synthetic RGB data. - Audio: not yet supported.

Sampling overview: 1) Number of items per request is sampled uniformly from the integer range [floor(n·(1−r)), ceil(n·(1+r))], where n is the base count and r is `num_mm_items_range_ratio`

in [0, 1]. r=0 keeps it fixed; r=1 allows 0. The maximum is further clamped to the sum of per-modality limits. 2) Each item’s modality and shape is sampled from `bucket_config`

, a dict mapping (height, width, num_frames) → probability. We treat `num_frames`

=1 as image and `num_frames`

> 1 as video. Entries with zero probability are removed and the rest are renormalized to sum to 1. 3) Per-modality hard caps are enforced via `limit_mm_per_prompt`

. When a modality reaches its cap, all of its buckets are excluded and the remaining probabilities are renormalized.

Example bucket configuration: {(256, 256, 1): 0.5, (720, 1280, 1): 0.4, (720, 1280, 16): 0.1} - Two image buckets (`num_frames`

=1) and one video bucket (`num_frames`

=16). OBS.: Only image sampling is supported for now.

Methods:

-
–[generate_mm_item](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.RandomMultiModalDataset.generate_mm_item)Create synthetic images and videos and

-
–[generate_synthetic_image](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.RandomMultiModalDataset.generate_synthetic_image)Generate synthetic PIL image with random RGB values.

-
–[generate_synthetic_video](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.RandomMultiModalDataset.generate_synthetic_video)Generate synthetic video with random values.

-
–[get_mm_item_iterator](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.RandomMultiModalDataset.get_mm_item_iterator)Iterator over the multimodal items for each request

-
–[get_mm_item_sampling_params](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.RandomMultiModalDataset.get_mm_item_sampling_params)Get the sampling parameters for the multimodal items.

-
–[map_config_to_modality](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.RandomMultiModalDataset.map_config_to_modality)Map the configuration to the modality.

-
–[normalize_bucket_config](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.RandomMultiModalDataset.normalize_bucket_config)Remove zero probability entries


## Source code in `vllm/benchmarks/datasets/datasets.py`


|
|

###

`generate_mm_item(mm_item_config)`

[¶](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.RandomMultiModalDataset.generate_mm_item)

Create synthetic images and videos and apply process_image/process_video respectively. This follows the OpenAI API chat completions https://github.com/openai/openai-python

## Source code in `vllm/benchmarks/datasets/datasets.py`


###

`generate_synthetic_image(width, height)`

[¶](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.RandomMultiModalDataset.generate_synthetic_image)

Generate synthetic PIL image with random RGB values.

NOTE: iid pixel sampling results in worst-case compression (good for stressing I/O), but very unlike real photos. We could consider a “low-freq” mode (e.g., noise blur) to emulate network realism instead of max stress.

## Source code in `vllm/benchmarks/datasets/datasets.py`


###

`generate_synthetic_video(width, height, num_frames)`

[¶](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.RandomMultiModalDataset.generate_synthetic_video)

Generate synthetic video with random values.

Creates a video with random pixel values, encodes it to MP4 format, and returns the content as bytes.

## Source code in `vllm/benchmarks/datasets/datasets.py`


###

`get_mm_item_iterator(min_num_mm_items, max_num_mm_items, bucket_config, limit_mm_per_prompt)`

[¶](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.RandomMultiModalDataset.get_mm_item_iterator)

Iterator over the multimodal items for each request whose size is between min_num_mm_items and max_num_mm_items.

Loop over the bucket config and sample a multimodal item. Loop until the number of multimodal items sampled is equal to request_num_mm_items or limit of multimodal items per prompt for all modalities is reached.

Note: - This function operates on a per-request shallow copy of `bucket_config`

(tuple->float). The original dict passed to `sample`

is not mutated. If this ever changes, a test is implemented and will fail.

## Source code in `vllm/benchmarks/datasets/datasets.py`


###

`get_mm_item_sampling_params(base_items_per_request, num_mm_items_range_ratio, limit_mm_per_prompt, bucket_config)`

[¶](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.RandomMultiModalDataset.get_mm_item_sampling_params)

Get the sampling parameters for the multimodal items.

## Source code in `vllm/benchmarks/datasets/datasets.py`


|
|

###

`map_config_to_modality(config)`

[¶](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.RandomMultiModalDataset.map_config_to_modality)

Map the configuration to the modality.

## Source code in `vllm/benchmarks/datasets/datasets.py`


###

`normalize_bucket_config(bucket_config)`

[¶](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.RandomMultiModalDataset.normalize_bucket_config)

Remove zero probability entries and normalize the bucket config to sum to 1.

## Source code in `vllm/benchmarks/datasets/datasets.py`


##

`SampleRequest`

`dataclass`

[¶](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.SampleRequest)

Represents a single inference request for benchmarking.

## Source code in `vllm/benchmarks/datasets/datasets.py`


##

`ShareGPTDataset`

[¶](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.ShareGPTDataset)

Bases: [BenchmarkDataset](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.BenchmarkDataset)

Implements the ShareGPT dataset. Loads data from a JSON file and generates sample requests based on conversation turns.

## Source code in `vllm/benchmarks/datasets/datasets.py`


|
|

##

`SonnetDataset`

[¶](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.SonnetDataset)

Bases: [BenchmarkDataset](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.BenchmarkDataset)

Simplified implementation of the Sonnet dataset. Loads poem lines from a text file and generates sample requests. Default values here copied from `benchmark_serving.py`

for the sonnet dataset.

## Source code in `vllm/benchmarks/datasets/datasets.py`


|
|

##

`SpecBench`

[¶](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.SpecBench)

Bases: [CustomDataset](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.CustomDataset)

Implements the SpecBench dataset: https://github.com/hemingkx/Spec-Bench Download the dataset using: wget https://raw.githubusercontent.com/hemingkx/Spec-Bench/refs/heads/main/data/spec_bench/question.jsonl

## Source code in `vllm/benchmarks/datasets/datasets.py`


|
|

##

`SpeedBench`

[¶](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.SpeedBench)

Bases: [CustomDataset](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.CustomDataset)

SPEED-Bench dataset: https://huggingface.co/datasets/nvidia/SPEED-Bench.

Download the dataset using:

`curl -LsSf https://raw.githubusercontent.com/NVIDIA-NeMo/Skills/refs/heads/main/nemo_skills/dataset/speed-bench/prepare.py | python3 -`


## Source code in `vllm/benchmarks/datasets/datasets.py`


##

`TimedTrace`

[¶](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.TimedTrace)

Bases: [BenchmarkDataset](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.BenchmarkDataset)

Implements a base class to replay various timed traces. Loads data from a JSON file and generates sample requests based on the timing information in the traces.

## Source code in `vllm/benchmarks/datasets/datasets.py`


|
|

##

`VisionArenaDataset`

[¶](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.VisionArenaDataset)

Bases: [HuggingFaceDataset](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.HuggingFaceDataset)

Vision Arena Dataset.

## Source code in `vllm/benchmarks/datasets/datasets.py`


##

`_format_zeta_prompt(sample, original_start_marker='<|editable_region_start|>')`

[¶](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets._format_zeta_prompt)

Format the zeta prompt for the Next Edit Prediction (NEP) dataset.

This function formats examples from the NEP dataset into prompts and expected outputs. It could be further extended to support more NEP datasets.

Parameters:

-

(`sample`

[¶](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets._format_zeta_prompt(sample))

) –[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)The dataset sample containing events, inputs, and outputs.

-

(`original_start_marker`

[¶](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets._format_zeta_prompt(original_start_marker))

, default:[str](https://docs.python.org/3/builtins/stdtypes.html#str)`'<|editable_region_start|>'`

) –The marker indicating the start of the editable region. Defaults to "<|editable_region_start|>".


Returns:

-

–[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)A dictionary with the formatted prompts and expected outputs.


## Source code in `vllm/benchmarks/datasets/datasets.py`


##

`_parse_range_ratio(value)`

[¶](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets._parse_range_ratio)

Parse a `--random-range-ratio`

CLI string.

Accepts either a plain float (`"0.3"`

) or a JSON dict (`'{"input": 0.3, "output": 0.5}'`

).

## Source code in `vllm/benchmarks/datasets/datasets.py`


##

`add_random_dataset_base_args(parser_or_group)`

[¶](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.add_random_dataset_base_args)

Add CLI arguments for base random dataset options.

This function adds arguments needed for: - random (random dataset) - random-mm (random multimodal dataset) - random-rerank (random dataset for reranking)

Parameters:

-

(`parser_or_group`

[¶](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.add_random_dataset_base_args(parser_or_group))

) –[FlexibleArgumentParser](https://docs.vllm.ai/utils/argparse_utils/#vllm.utils.argparse_utils.FlexibleArgumentParser)| _ArgumentGroupEither a parser or an argument group to add arguments to.


## Source code in `vllm/benchmarks/datasets/datasets.py`


|
|

##

`add_random_multimodal_dataset_args(parser_or_group)`

[¶](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.add_random_multimodal_dataset_args)

Add CLI arguments for random multimodal dataset options.

This function adds arguments needed for: - random-mm (random multimodal dataset)

Parameters:

-

(`parser_or_group`

[¶](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.add_random_multimodal_dataset_args(parser_or_group))

) –[FlexibleArgumentParser](https://docs.vllm.ai/utils/argparse_utils/#vllm.utils.argparse_utils.FlexibleArgumentParser)| _ArgumentGroupEither a parser or an argument group to add arguments to.


## Source code in `vllm/benchmarks/datasets/datasets.py`


|
|

##

`gen_prompt_decode_to_target_len(tokenizer, token_sequence, target_token_len, max_retry=10, add_special_tokens=False, rng=None)`

[¶](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.gen_prompt_decode_to_target_len)

Ensure decoded-then-encoded prompt length matches the target token length.

This function decodes an initial token sequence to text and re-encodes it , iteratively adjusting the token sequence length to match a target. This is necessary because some tokenizers do not guarantee a 1:1 mapping between consecutive tokens and the decoded-then-encoded sequence length. For example, for GPT2Tokenizer: [6880, 6881] -> ['Ġcalls', 'here'] -> [1650, 939, 486] -> ['Ġcall', 'sh', 'ere']

Returns a tuple of the final prompt string, the adjusted token sequence, and the token mismatch (final_len - target_token_len) if the retry budget is exhausted.

## Source code in `vllm/benchmarks/datasets/datasets.py`


##

`is_valid_sequence(prompt_len, output_len, min_len=4, max_prompt_len=1024, max_total_len=2048, skip_min_output_len_check=False)`

[¶](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.is_valid_sequence)

Validate a sequence based on prompt and output lengths.

Default pruning criteria are copied from the original `sample_hf_requests`

and `sample_sharegpt_requests`

functions in benchmark_serving.py, as well as from `sample_requests`

in benchmark_throughput.py.

## Source code in `vllm/benchmarks/datasets/datasets.py`


##

`process_audio(audio)`

[¶](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.process_audio)

Process a single audio input and return a (array, sample_rate) tuple.

Supports: 1. String: treated as a file path, loaded with soundfile. 2. Dict with 'array' and 'sampling_rate' keys: HuggingFace audio format. 3. Tuple (array, sr): passed through directly.

## Source code in `vllm/benchmarks/datasets/datasets.py`


##

`process_image(image, *, ensure_client_side_data=False)`

[¶](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.process_image)

Process a single image input and return a multimedia content dictionary.

Supports the following input types:

-
Dictionary with raw image bytes: - Expects a dict with a 'bytes' key containing raw image data. - Loads the bytes as a PIL.Image.Image.

-
PIL.Image.Image input: - Converts the image to RGB. - Saves the image as a JPEG in memory. - Encodes the JPEG data as a base64 string. - Returns a dictionary with the image as a base64 data URL.

-
String input: - Treats the string as a URL, local file path, or base64 encoded data. - If string starts with "data:image/", treats as base64.

- If string starts with "http://", "https://", or "file://", treats as URL.
- Otherwise treats as local file path and prepends "file://".
- If ensure_client_side_data is True, local and HTTP(S) image references are loaded and encoded as base64 image data URLs. Existing data:image URLs are kept unchanged.
- Returns a dictionary with the image URL or base64 data.

Raises:

-

–[ValueError](https://docs.python.org/3/builtins/exceptions.html#ValueError)If the input is not a supported type.


## Source code in `vllm/benchmarks/datasets/datasets.py`


##

`process_video(video)`

[¶](https://docs.vllm.ai#vllm.benchmarks.datasets.datasets.process_video)

Process a single video input and return a multimedia content dictionary.

Supports the following input types:

-
Dictionary with raw video bytes: - Expects a dict with a 'bytes' key containing raw video data.

-
String input: - Treats the string as a URL or local file path. - Prepends "file://" if the string doesn't start with "http://" or "file://". - Returns a dictionary with the image URL.


Raises:

-

–[ValueError](https://docs.python.org/3/builtins/exceptions.html#ValueError)If the input is not a supported type.