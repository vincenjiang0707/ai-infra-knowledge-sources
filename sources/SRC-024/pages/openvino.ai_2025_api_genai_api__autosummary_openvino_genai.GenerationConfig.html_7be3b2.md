source: https://docs.openvino.ai/2025/api/genai_api/_autosummary/openvino_genai.GenerationConfig.html
lastmod: 

# openvino_genai.GenerationConfig[#](https://docs.openvino.ai#openvino-genai-generationconfig)

-
*class*openvino_genai.GenerationConfig[#](https://docs.openvino.ai#openvino_genai.GenerationConfig) Bases:

`pybind11_object`

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
__init__(
**args*,***kwargs*)[#](https://docs.openvino.ai#openvino_genai.GenerationConfig.__init__) Overloaded function.

__init__(self: openvino_genai.py_openvino_genai.GenerationConfig, json_path: os.PathLike | str | bytes) -> None


path where generation_config.json is stored

__init__(self: openvino_genai.py_openvino_genai.GenerationConfig,

[**](https://docs.openvino.ai#id1)kwargs) -> None


Methods

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

(self)`is_assisting_generation`

(self)`is_beam_search`

(self)`is_greedy_decoding`

(self)`is_multinomial`

(self)`is_prompt_lookup`

(self, tokenizer_eos_token_id)`set_eos_token_id`

(self, **kwargs)`update_generation_config`

(self)`validate`

Attributes

-
__annotations__
*= {}*[#](https://docs.openvino.ai#openvino_genai.GenerationConfig.__annotations__)

-
__class__
[#](https://docs.openvino.ai#openvino_genai.GenerationConfig.__class__) alias of

`pybind11_type`


-
__delattr__(
*name*,*/*)[#](https://docs.openvino.ai#openvino_genai.GenerationConfig.__delattr__) Implement delattr(self, name).


-
__dir__()
[#](https://docs.openvino.ai#openvino_genai.GenerationConfig.__dir__) Default dir() implementation.


-
__eq__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.GenerationConfig.__eq__) Return self==value.


-
__format__(
*format_spec*,*/*)[#](https://docs.openvino.ai#openvino_genai.GenerationConfig.__format__) Default object formatter.

Return str(self) if format_spec is empty. Raise TypeError otherwise.


-
__ge__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.GenerationConfig.__ge__) Return self>=value.


-
__getattribute__(
*name*,*/*)[#](https://docs.openvino.ai#openvino_genai.GenerationConfig.__getattribute__) Return getattr(self, name).


-
__getstate__()
[#](https://docs.openvino.ai#openvino_genai.GenerationConfig.__getstate__) Helper for pickle.


-
__gt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.GenerationConfig.__gt__) Return self>value.


-
__hash__()
[#](https://docs.openvino.ai#openvino_genai.GenerationConfig.__hash__) Return hash(self).


-
__init__(
**args*,***kwargs*)[#](https://docs.openvino.ai#id0) Overloaded function.

__init__(self: openvino_genai.py_openvino_genai.GenerationConfig, json_path: os.PathLike | str | bytes) -> None


path where generation_config.json is stored

__init__(self: openvino_genai.py_openvino_genai.GenerationConfig,

[**](https://docs.openvino.ai#id3)kwargs) -> None


-
__init_subclass__()
[#](https://docs.openvino.ai#openvino_genai.GenerationConfig.__init_subclass__) This method is called when a class is subclassed.

The default implementation does nothing. It may be overridden to extend subclasses.


-
__le__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.GenerationConfig.__le__) Return self<=value.


-
__lt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.GenerationConfig.__lt__) Return self<value.


-
__ne__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.GenerationConfig.__ne__) Return self!=value.


-
__new__(
***kwargs*)[#](https://docs.openvino.ai#openvino_genai.GenerationConfig.__new__)

-
__reduce__()
[#](https://docs.openvino.ai#openvino_genai.GenerationConfig.__reduce__) Helper for pickle.


-
__reduce_ex__(
*protocol*,*/*)[#](https://docs.openvino.ai#openvino_genai.GenerationConfig.__reduce_ex__) Helper for pickle.


-
__repr__()
[#](https://docs.openvino.ai#openvino_genai.GenerationConfig.__repr__) Return repr(self).


-
__setattr__(
*name*,*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.GenerationConfig.__setattr__) Implement setattr(self, name, value).


-
__sizeof__()
[#](https://docs.openvino.ai#openvino_genai.GenerationConfig.__sizeof__) Size of object in memory, in bytes.


-
__str__()
[#](https://docs.openvino.ai#openvino_genai.GenerationConfig.__str__) Return str(self).


-
__subclasshook__()
[#](https://docs.openvino.ai#openvino_genai.GenerationConfig.__subclasshook__) Abstract classes can override this to customize issubclass().

This is invoked early on by abc.ABCMeta.__subclasscheck__(). It should return True, False or NotImplemented. If it returns NotImplemented, the normal algorithm is used. Otherwise, it overrides the normal algorithm (and the outcome is cached).


-
_pybind11_conduit_v1_()
[#](https://docs.openvino.ai#openvino_genai.GenerationConfig._pybind11_conduit_v1_)

-
*property*adapters[#](https://docs.openvino.ai#openvino_genai.GenerationConfig.adapters)

-
*property*apply_chat_template[#](https://docs.openvino.ai#openvino_genai.GenerationConfig.apply_chat_template)

-
*property*assistant_confidence_threshold[#](https://docs.openvino.ai#openvino_genai.GenerationConfig.assistant_confidence_threshold)

-
*property*diversity_penalty[#](https://docs.openvino.ai#openvino_genai.GenerationConfig.diversity_penalty)

-
*property*do_sample[#](https://docs.openvino.ai#openvino_genai.GenerationConfig.do_sample)

-
*property*echo[#](https://docs.openvino.ai#openvino_genai.GenerationConfig.echo)

-
*property*eos_token_id[#](https://docs.openvino.ai#openvino_genai.GenerationConfig.eos_token_id)

-
*property*frequency_penalty[#](https://docs.openvino.ai#openvino_genai.GenerationConfig.frequency_penalty)

-
*property*ignore_eos[#](https://docs.openvino.ai#openvino_genai.GenerationConfig.ignore_eos)

-
*property*include_stop_str_in_output[#](https://docs.openvino.ai#openvino_genai.GenerationConfig.include_stop_str_in_output)

-
is_assisting_generation(
*self:*) bool[openvino_genai.py_openvino_genai.GenerationConfig](https://docs.openvino.ai#openvino_genai.GenerationConfig)[#](https://docs.openvino.ai#openvino_genai.GenerationConfig.is_assisting_generation)

-
is_beam_search(
*self:*) bool[openvino_genai.py_openvino_genai.GenerationConfig](https://docs.openvino.ai#openvino_genai.GenerationConfig)[#](https://docs.openvino.ai#openvino_genai.GenerationConfig.is_beam_search)

-
is_greedy_decoding(
*self:*) bool[openvino_genai.py_openvino_genai.GenerationConfig](https://docs.openvino.ai#openvino_genai.GenerationConfig)[#](https://docs.openvino.ai#openvino_genai.GenerationConfig.is_greedy_decoding)

-
is_multinomial(
*self:*) bool[openvino_genai.py_openvino_genai.GenerationConfig](https://docs.openvino.ai#openvino_genai.GenerationConfig)[#](https://docs.openvino.ai#openvino_genai.GenerationConfig.is_multinomial)

-
is_prompt_lookup(
*self:*) bool[openvino_genai.py_openvino_genai.GenerationConfig](https://docs.openvino.ai#openvino_genai.GenerationConfig)[#](https://docs.openvino.ai#openvino_genai.GenerationConfig.is_prompt_lookup)

-
*property*length_penalty[#](https://docs.openvino.ai#openvino_genai.GenerationConfig.length_penalty)

-
*property*logprobs[#](https://docs.openvino.ai#openvino_genai.GenerationConfig.logprobs)

-
*property*max_length[#](https://docs.openvino.ai#openvino_genai.GenerationConfig.max_length)

-
*property*max_new_tokens[#](https://docs.openvino.ai#openvino_genai.GenerationConfig.max_new_tokens)

-
*property*max_ngram_size[#](https://docs.openvino.ai#openvino_genai.GenerationConfig.max_ngram_size)

-
*property*min_new_tokens[#](https://docs.openvino.ai#openvino_genai.GenerationConfig.min_new_tokens)

-
*property*no_repeat_ngram_size[#](https://docs.openvino.ai#openvino_genai.GenerationConfig.no_repeat_ngram_size)

-
*property*num_assistant_tokens[#](https://docs.openvino.ai#openvino_genai.GenerationConfig.num_assistant_tokens)

-
*property*num_beam_groups[#](https://docs.openvino.ai#openvino_genai.GenerationConfig.num_beam_groups)

-
*property*num_beams[#](https://docs.openvino.ai#openvino_genai.GenerationConfig.num_beams)

-
*property*num_return_sequences[#](https://docs.openvino.ai#openvino_genai.GenerationConfig.num_return_sequences)

-
*property*parsers[#](https://docs.openvino.ai#openvino_genai.GenerationConfig.parsers)

-
*property*presence_penalty[#](https://docs.openvino.ai#openvino_genai.GenerationConfig.presence_penalty)

-
*property*repetition_penalty[#](https://docs.openvino.ai#openvino_genai.GenerationConfig.repetition_penalty)

-
*property*rng_seed[#](https://docs.openvino.ai#openvino_genai.GenerationConfig.rng_seed)

-
set_eos_token_id(
*self:*,[openvino_genai.py_openvino_genai.GenerationConfig](https://docs.openvino.ai#openvino_genai.GenerationConfig)*tokenizer_eos_token_id: SupportsInt*) None[#](https://docs.openvino.ai#openvino_genai.GenerationConfig.set_eos_token_id)

-
*property*stop_criteria[#](https://docs.openvino.ai#openvino_genai.GenerationConfig.stop_criteria)

-
*property*stop_strings[#](https://docs.openvino.ai#openvino_genai.GenerationConfig.stop_strings)

-
*property*stop_token_ids[#](https://docs.openvino.ai#openvino_genai.GenerationConfig.stop_token_ids)

-
*property*structured_output_config[#](https://docs.openvino.ai#openvino_genai.GenerationConfig.structured_output_config)

-
*property*temperature[#](https://docs.openvino.ai#openvino_genai.GenerationConfig.temperature)

-
*property*top_k[#](https://docs.openvino.ai#openvino_genai.GenerationConfig.top_k)

-
*property*top_p[#](https://docs.openvino.ai#openvino_genai.GenerationConfig.top_p)

-
update_generation_config(
*self:*,[openvino_genai.py_openvino_genai.GenerationConfig](https://docs.openvino.ai#openvino_genai.GenerationConfig)***kwargs*) None[#](https://docs.openvino.ai#openvino_genai.GenerationConfig.update_generation_config)

-
validate(
*self:*) None[openvino_genai.py_openvino_genai.GenerationConfig](https://docs.openvino.ai#openvino_genai.GenerationConfig)[#](https://docs.openvino.ai#openvino_genai.GenerationConfig.validate)

-
__init__(