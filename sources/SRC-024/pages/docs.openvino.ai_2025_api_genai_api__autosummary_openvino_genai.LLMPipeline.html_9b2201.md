source: https://docs.openvino.ai/2025/api/genai_api/_autosummary/openvino_genai.LLMPipeline.html
lastmod: 

# openvino_genai.LLMPipeline[#](https://docs.openvino.ai#openvino-genai-llmpipeline)

-
*class*openvino_genai.LLMPipeline[#](https://docs.openvino.ai#openvino_genai.LLMPipeline) Bases:

`pybind11_object`

This class is used for generation with LLMs

-
__init__(
**args*,***kwargs*)[#](https://docs.openvino.ai#openvino_genai.LLMPipeline.__init__) Overloaded function.

__init__(self: openvino_genai.py_openvino_genai.LLMPipeline, models_path: os.PathLike | str | bytes, tokenizer: openvino_genai.py_openvino_genai.Tokenizer, device: str, config: collections.abc.Mapping[str, object] = {},

[**](https://docs.openvino.ai#id1)kwargs) -> NoneLLMPipeline class constructor for manually created openvino_genai.Tokenizer. models_path (os.PathLike): Path to the model file. tokenizer (openvino_genai.Tokenizer): tokenizer object. device (str): Device to run the model on (e.g., CPU, GPU). Default is ‘CPU’. Add {“scheduler_config”: ov_genai.SchedulerConfig} to config properties to create continuous batching pipeline. kwargs: Device properties.

__init__(self: openvino_genai.py_openvino_genai.LLMPipeline, models_path: os.PathLike | str | bytes, device: str, config: collections.abc.Mapping[str, object] = {},

[**](https://docs.openvino.ai#id3)kwargs) -> NoneLLMPipeline class constructor. models_path (os.PathLike): Path to the model file. device (str): Device to run the model on (e.g., CPU, GPU). Default is ‘CPU’. Add {“scheduler_config”: ov_genai.SchedulerConfig} to config properties to create continuous batching pipeline. kwargs: Device properties.

__init__(self: openvino_genai.py_openvino_genai.LLMPipeline, model: str, weights: openvino._pyopenvino.Tensor, tokenizer: openvino_genai.py_openvino_genai.Tokenizer, device: str, generation_config: openvino_genai.py_openvino_genai.GenerationConfig | None = None,

[**](https://docs.openvino.ai#id5)kwargs) -> NoneLLMPipeline class constructor. model (str): Pre-read model. weights (ov.Tensor): Pre-read model weights. tokenizer (str): Genai Tokenizers. device (str): Device to run the model on (e.g., CPU, GPU). generation_config {ov_genai.GenerationConfig} Genai GenerationConfig. Default is an empty config. kwargs: Device properties.



Methods

(self, inputs[, generation_config, ...])`__call__`

Generates sequences or tokens for LLMs.

(name, /)`__delattr__`

Implement delattr(self, name).

()`__dir__`

Default dir() implementation.

(value, /)`__eq__`

Return self==value.

(format_spec, /)`__format__`

Default object formatter.

(value, /)`__ge__`

Return self>=value.

(name, /)`__getattribute__`

Return getattr(self, name).

Helper for pickle.

(value, /)`__gt__`

Return self>value.

()`__hash__`

Return hash(self).

(*args, **kwargs)`__init__`

Overloaded function.

This method is called when a class is subclassed.

(value, /)`__le__`

Return self<=value.

(value, /)`__lt__`

Return self<value.

(value, /)`__ne__`

Return self!=value.

(**kwargs)`__new__`

Helper for pickle.

(protocol, /)`__reduce_ex__`

Helper for pickle.

()`__repr__`

Return repr(self).

(name, value, /)`__setattr__`

Implement setattr(self, name, value).

Size of object in memory, in bytes.

()`__str__`

Return str(self).

Abstract classes can override this to customize issubclass().

(self)`finish_chat`

(self, inputs[, generation_config, ...])`generate`

Generates sequences or tokens for LLMs.

(self)`get_generation_config`

(self)`get_tokenizer`

(self, config)`set_generation_config`

(self[, system_message])`start_chat`

Attributes

-
__annotations__
*= {}*[#](https://docs.openvino.ai#openvino_genai.LLMPipeline.__annotations__)

-
__call__(
*self:*,[openvino_genai.py_openvino_genai.LLMPipeline](https://docs.openvino.ai#openvino_genai.LLMPipeline)*inputs:*,[openvino._pyopenvino.Tensor](https://docs.openvino.ai/ie_python_api/_autosummary/openvino.Tensor.html#openvino.Tensor)|[openvino_genai.py_openvino_genai.TokenizedInputs](https://docs.openvino.ai/openvino_genai.TokenizedInputs.html#openvino_genai.TokenizedInputs)| str | collections.abc.Sequence[str] |[openvino_genai.py_openvino_genai.ChatHistory](https://docs.openvino.ai/openvino_genai.ChatHistory.html#openvino_genai.ChatHistory)*generation_config:*,[openvino_genai.py_openvino_genai.GenerationConfig](https://docs.openvino.ai/openvino_genai.GenerationConfig.html#openvino_genai.GenerationConfig)| None = None*streamer: collections.abc.Callable[[str], int | None] |*,[openvino_genai.py_openvino_genai.StreamerBase](https://docs.openvino.ai/openvino_genai.StreamerBase.html#openvino_genai.StreamerBase)| None = None***kwargs*)[openvino_genai.py_openvino_genai.EncodedResults](https://docs.openvino.ai/openvino_genai.EncodedResults.html#openvino_genai.EncodedResults)|[openvino_genai.py_openvino_genai.DecodedResults](https://docs.openvino.ai/openvino_genai.DecodedResults.html#openvino_genai.DecodedResults)[#](https://docs.openvino.ai#openvino_genai.LLMPipeline.__call__) Generates sequences or tokens for LLMs. If input is a string or list of strings then resulting sequences will be already detokenized.

- Parameters:
**inputs**(*str**,**list**[**str**]**,**ov.genai.TokenizedInputs**, or**ov.Tensor*) – inputs in the form of string, list of strings, chat history or tokenized input_ids**generation_config**(*GenerationConfig**or**a dict*) – generation_config**streamer**– streamer either as a lambda with a boolean returning flag whether generation should be stopped


:type : Callable[[str], bool], ov.genai.StreamerBase

- Parameters:
**kwargs**– arbitrary keyword arguments with keys corresponding to GenerationConfig fields.

:type : dict

- Returns:
return results in encoded, or decoded form depending on inputs type

- Return type:
[DecodedResults](https://docs.openvino.ai/openvino_genai.DecodedResults.html#openvino_genai.DecodedResults),[EncodedResults](https://docs.openvino.ai/openvino_genai.EncodedResults.html#openvino_genai.EncodedResults), str

Structure to keep generation config parameters. For a selected method of decoding, only parameters from that group and generic parameters are used. For example, if do_sample is set to true, then only generic parameters and random sampling parameters will be used while greedy and beam search parameters will not affect decoding at all.

Parameters: max_length: the maximum length the generated tokens can have. Corresponds to the length of the input prompt +

max_new_tokens. Its effect is overridden by max_new_tokens, if also set.

max_new_tokens: the maximum numbers of tokens to generate, excluding the number of tokens in the prompt. max_new_tokens has priority over max_length. min_new_tokens: set 0 probability for eos_token_id for the first eos_token_id generated tokens. ignore_eos: if set to true, then generation will not stop even if <eos> token is met. eos_token_id: token_id of <eos> (end of sentence) stop_strings: a set of strings that will cause pipeline to stop generating further tokens. include_stop_str_in_output: if set to true stop string that matched generation will be included in generation output (default: false) stop_token_ids: a set of tokens that will cause pipeline to stop generating further tokens. echo: if set to true, the model will echo the prompt in the output. logprobs: number of top logprobs computed for each position, if set to 0, logprobs are not computed and value 0.0 is returned.

Currently only single top logprob can be returned, so any logprobs > 1 is treated as logprobs == 1. (default: 0).

apply_chat_template: whether to apply chat_template for non-chat scenarios

repetition_penalty: the parameter for repetition penalty. 1.0 means no penalty. presence_penalty: reduces absolute log prob if the token was generated at least once. frequency_penalty: reduces absolute log prob as many times as the token was generated.

Beam search specific parameters: num_beams: number of beams for beam search. 1 disables beam search. num_beam_groups: number of groups to divide num_beams into in order to ensure diversity among different groups of beams. diversity_penalty: value is subtracted from a beam’s score if it generates the same token as any beam from other group at a particular time. length_penalty: exponential penalty to the length that is used with beam-based generation. It is applied as an exponent to

the sequence length, which in turn is used to divide the score of the sequence. Since the score is the log likelihood of the sequence (i.e. negative), length_penalty > 0.0 promotes longer sequences, while length_penalty < 0.0 encourages shorter sequences.

num_return_sequences: the number of sequences to return for grouped beam search decoding. no_repeat_ngram_size: if set to int > 0, all ngrams of that size can only occur once. stop_criteria: controls the stopping condition for grouped beam search. It accepts the following values:

“openvino_genai.StopCriteria.EARLY”, where the generation stops as soon as there are num_beams complete candidates; “openvino_genai.StopCriteria.HEURISTIC” is applied and the generation stops when is it very unlikely to find better candidates; “openvino_genai.StopCriteria.NEVER”, where the beam search procedure only stops when there cannot be better candidates (canonical beam search algorithm).

Random sampling parameters: temperature: the value used to modulate token probabilities for random sampling. top_p: if set to float < 1, only the smallest set of most probable tokens with probabilities that add up to top_p or higher are kept for generation. top_k: the number of highest probability vocabulary tokens to keep for top-k-filtering. do_sample: whether or not to use multinomial random sampling that add up to top_p or higher are kept. num_return_sequences: the number of sequences to generate from a single prompt.


-
__class__
[#](https://docs.openvino.ai#openvino_genai.LLMPipeline.__class__) alias of

`pybind11_type`


-
__delattr__(
*name*,*/*)[#](https://docs.openvino.ai#openvino_genai.LLMPipeline.__delattr__) Implement delattr(self, name).


-
__dir__()
[#](https://docs.openvino.ai#openvino_genai.LLMPipeline.__dir__) Default dir() implementation.


-
__eq__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.LLMPipeline.__eq__) Return self==value.


-
__format__(
*format_spec*,*/*)[#](https://docs.openvino.ai#openvino_genai.LLMPipeline.__format__) Default object formatter.

Return str(self) if format_spec is empty. Raise TypeError otherwise.


-
__ge__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.LLMPipeline.__ge__) Return self>=value.


-
__getattribute__(
*name*,*/*)[#](https://docs.openvino.ai#openvino_genai.LLMPipeline.__getattribute__) Return getattr(self, name).


-
__getstate__()
[#](https://docs.openvino.ai#openvino_genai.LLMPipeline.__getstate__) Helper for pickle.


-
__gt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.LLMPipeline.__gt__) Return self>value.


-
__hash__()
[#](https://docs.openvino.ai#openvino_genai.LLMPipeline.__hash__) Return hash(self).


-
__init__(
**args*,***kwargs*)[#](https://docs.openvino.ai#id0) Overloaded function.

__init__(self: openvino_genai.py_openvino_genai.LLMPipeline, models_path: os.PathLike | str | bytes, tokenizer: openvino_genai.py_openvino_genai.Tokenizer, device: str, config: collections.abc.Mapping[str, object] = {},

[**](https://docs.openvino.ai#id7)kwargs) -> NoneLLMPipeline class constructor for manually created openvino_genai.Tokenizer. models_path (os.PathLike): Path to the model file. tokenizer (openvino_genai.Tokenizer): tokenizer object. device (str): Device to run the model on (e.g., CPU, GPU). Default is ‘CPU’. Add {“scheduler_config”: ov_genai.SchedulerConfig} to config properties to create continuous batching pipeline. kwargs: Device properties.

__init__(self: openvino_genai.py_openvino_genai.LLMPipeline, models_path: os.PathLike | str | bytes, device: str, config: collections.abc.Mapping[str, object] = {},

[**](https://docs.openvino.ai#id9)kwargs) -> NoneLLMPipeline class constructor. models_path (os.PathLike): Path to the model file. device (str): Device to run the model on (e.g., CPU, GPU). Default is ‘CPU’. Add {“scheduler_config”: ov_genai.SchedulerConfig} to config properties to create continuous batching pipeline. kwargs: Device properties.

__init__(self: openvino_genai.py_openvino_genai.LLMPipeline, model: str, weights: openvino._pyopenvino.Tensor, tokenizer: openvino_genai.py_openvino_genai.Tokenizer, device: str, generation_config: openvino_genai.py_openvino_genai.GenerationConfig | None = None,

[**](https://docs.openvino.ai#id11)kwargs) -> NoneLLMPipeline class constructor. model (str): Pre-read model. weights (ov.Tensor): Pre-read model weights. tokenizer (str): Genai Tokenizers. device (str): Device to run the model on (e.g., CPU, GPU). generation_config {ov_genai.GenerationConfig} Genai GenerationConfig. Default is an empty config. kwargs: Device properties.



-
__init_subclass__()
[#](https://docs.openvino.ai#openvino_genai.LLMPipeline.__init_subclass__) This method is called when a class is subclassed.

The default implementation does nothing. It may be overridden to extend subclasses.


-
__le__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.LLMPipeline.__le__) Return self<=value.


-
__lt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.LLMPipeline.__lt__) Return self<value.


-
__ne__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.LLMPipeline.__ne__) Return self!=value.


-
__new__(
***kwargs*)[#](https://docs.openvino.ai#openvino_genai.LLMPipeline.__new__)

-
__reduce__()
[#](https://docs.openvino.ai#openvino_genai.LLMPipeline.__reduce__) Helper for pickle.


-
__reduce_ex__(
*protocol*,*/*)[#](https://docs.openvino.ai#openvino_genai.LLMPipeline.__reduce_ex__) Helper for pickle.


-
__repr__()
[#](https://docs.openvino.ai#openvino_genai.LLMPipeline.__repr__) Return repr(self).


-
__setattr__(
*name*,*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.LLMPipeline.__setattr__) Implement setattr(self, name, value).


-
__sizeof__()
[#](https://docs.openvino.ai#openvino_genai.LLMPipeline.__sizeof__) Size of object in memory, in bytes.


-
__str__()
[#](https://docs.openvino.ai#openvino_genai.LLMPipeline.__str__) Return str(self).


-
__subclasshook__()
[#](https://docs.openvino.ai#openvino_genai.LLMPipeline.__subclasshook__) Abstract classes can override this to customize issubclass().

This is invoked early on by abc.ABCMeta.__subclasscheck__(). It should return True, False or NotImplemented. If it returns NotImplemented, the normal algorithm is used. Otherwise, it overrides the normal algorithm (and the outcome is cached).


-
_pybind11_conduit_v1_()
[#](https://docs.openvino.ai#openvino_genai.LLMPipeline._pybind11_conduit_v1_)

-
finish_chat(
*self:*) None[openvino_genai.py_openvino_genai.LLMPipeline](https://docs.openvino.ai#openvino_genai.LLMPipeline)[#](https://docs.openvino.ai#openvino_genai.LLMPipeline.finish_chat)

-
generate(
*self:*,[openvino_genai.py_openvino_genai.LLMPipeline](https://docs.openvino.ai#openvino_genai.LLMPipeline)*inputs:*,[openvino._pyopenvino.Tensor](https://docs.openvino.ai/ie_python_api/_autosummary/openvino.Tensor.html#openvino.Tensor)|[openvino_genai.py_openvino_genai.TokenizedInputs](https://docs.openvino.ai/openvino_genai.TokenizedInputs.html#openvino_genai.TokenizedInputs)| str | collections.abc.Sequence[str] |[openvino_genai.py_openvino_genai.ChatHistory](https://docs.openvino.ai/openvino_genai.ChatHistory.html#openvino_genai.ChatHistory)*generation_config:*,[openvino_genai.py_openvino_genai.GenerationConfig](https://docs.openvino.ai/openvino_genai.GenerationConfig.html#openvino_genai.GenerationConfig)| None = None*streamer: collections.abc.Callable[[str], int | None] |*,[openvino_genai.py_openvino_genai.StreamerBase](https://docs.openvino.ai/openvino_genai.StreamerBase.html#openvino_genai.StreamerBase)| None = None***kwargs*)[openvino_genai.py_openvino_genai.EncodedResults](https://docs.openvino.ai/openvino_genai.EncodedResults.html#openvino_genai.EncodedResults)|[openvino_genai.py_openvino_genai.DecodedResults](https://docs.openvino.ai/openvino_genai.DecodedResults.html#openvino_genai.DecodedResults)[#](https://docs.openvino.ai#openvino_genai.LLMPipeline.generate) Generates sequences or tokens for LLMs. If input is a string or list of strings then resulting sequences will be already detokenized.

- Parameters:
**inputs**(*str**,**list**[**str**]**,**ov.genai.TokenizedInputs**, or**ov.Tensor*) – inputs in the form of string, list of strings, chat history or tokenized input_ids**generation_config**(*GenerationConfig**or**a dict*) – generation_config**streamer**– streamer either as a lambda with a boolean returning flag whether generation should be stopped


:type : Callable[[str], bool], ov.genai.StreamerBase

- Parameters:
**kwargs**– arbitrary keyword arguments with keys corresponding to GenerationConfig fields.

:type : dict

- Returns:
return results in encoded, or decoded form depending on inputs type

- Return type:
[DecodedResults](https://docs.openvino.ai/openvino_genai.DecodedResults.html#openvino_genai.DecodedResults),[EncodedResults](https://docs.openvino.ai/openvino_genai.EncodedResults.html#openvino_genai.EncodedResults), str

Structure to keep generation config parameters. For a selected method of decoding, only parameters from that group and generic parameters are used. For example, if do_sample is set to true, then only generic parameters and random sampling parameters will be used while greedy and beam search parameters will not affect decoding at all.

Parameters: max_length: the maximum length the generated tokens can have. Corresponds to the length of the input prompt +

max_new_tokens. Its effect is overridden by max_new_tokens, if also set.

max_new_tokens: the maximum numbers of tokens to generate, excluding the number of tokens in the prompt. max_new_tokens has priority over max_length. min_new_tokens: set 0 probability for eos_token_id for the first eos_token_id generated tokens. ignore_eos: if set to true, then generation will not stop even if <eos> token is met. eos_token_id: token_id of <eos> (end of sentence) stop_strings: a set of strings that will cause pipeline to stop generating further tokens. include_stop_str_in_output: if set to true stop string that matched generation will be included in generation output (default: false) stop_token_ids: a set of tokens that will cause pipeline to stop generating further tokens. echo: if set to true, the model will echo the prompt in the output. logprobs: number of top logprobs computed for each position, if set to 0, logprobs are not computed and value 0.0 is returned.

Currently only single top logprob can be returned, so any logprobs > 1 is treated as logprobs == 1. (default: 0).

apply_chat_template: whether to apply chat_template for non-chat scenarios

repetition_penalty: the parameter for repetition penalty. 1.0 means no penalty. presence_penalty: reduces absolute log prob if the token was generated at least once. frequency_penalty: reduces absolute log prob as many times as the token was generated.

Beam search specific parameters: num_beams: number of beams for beam search. 1 disables beam search. num_beam_groups: number of groups to divide num_beams into in order to ensure diversity among different groups of beams. diversity_penalty: value is subtracted from a beam’s score if it generates the same token as any beam from other group at a particular time. length_penalty: exponential penalty to the length that is used with beam-based generation. It is applied as an exponent to

the sequence length, which in turn is used to divide the score of the sequence. Since the score is the log likelihood of the sequence (i.e. negative), length_penalty > 0.0 promotes longer sequences, while length_penalty < 0.0 encourages shorter sequences.

num_return_sequences: the number of sequences to return for grouped beam search decoding. no_repeat_ngram_size: if set to int > 0, all ngrams of that size can only occur once. stop_criteria: controls the stopping condition for grouped beam search. It accepts the following values:

“openvino_genai.StopCriteria.EARLY”, where the generation stops as soon as there are num_beams complete candidates; “openvino_genai.StopCriteria.HEURISTIC” is applied and the generation stops when is it very unlikely to find better candidates; “openvino_genai.StopCriteria.NEVER”, where the beam search procedure only stops when there cannot be better candidates (canonical beam search algorithm).

Random sampling parameters: temperature: the value used to modulate token probabilities for random sampling. top_p: if set to float < 1, only the smallest set of most probable tokens with probabilities that add up to top_p or higher are kept for generation. top_k: the number of highest probability vocabulary tokens to keep for top-k-filtering. do_sample: whether or not to use multinomial random sampling that add up to top_p or higher are kept. num_return_sequences: the number of sequences to generate from a single prompt.


-
get_generation_config(
*self:*)[openvino_genai.py_openvino_genai.LLMPipeline](https://docs.openvino.ai#openvino_genai.LLMPipeline)[openvino_genai.py_openvino_genai.GenerationConfig](https://docs.openvino.ai/openvino_genai.GenerationConfig.html#openvino_genai.GenerationConfig)[#](https://docs.openvino.ai#openvino_genai.LLMPipeline.get_generation_config)

-
get_tokenizer(
*self:*)[openvino_genai.py_openvino_genai.LLMPipeline](https://docs.openvino.ai#openvino_genai.LLMPipeline)[openvino_genai.py_openvino_genai.Tokenizer](https://docs.openvino.ai/openvino_genai.Tokenizer.html#openvino_genai.Tokenizer)[#](https://docs.openvino.ai#openvino_genai.LLMPipeline.get_tokenizer)

-
set_generation_config(
*self:*,[openvino_genai.py_openvino_genai.LLMPipeline](https://docs.openvino.ai#openvino_genai.LLMPipeline)*config:*) None[openvino_genai.py_openvino_genai.GenerationConfig](https://docs.openvino.ai/openvino_genai.GenerationConfig.html#openvino_genai.GenerationConfig)[#](https://docs.openvino.ai#openvino_genai.LLMPipeline.set_generation_config)

-
start_chat(
*self:*,[openvino_genai.py_openvino_genai.LLMPipeline](https://docs.openvino.ai#openvino_genai.LLMPipeline)*system_message: str = ''*) None[#](https://docs.openvino.ai#openvino_genai.LLMPipeline.start_chat)

-
__init__(