source: https://docs.openvino.ai/2025/api/genai_api/_autosummary/openvino_genai.Tokenizer.html
lastmod: 

# openvino_genai.Tokenizer[#](https://docs.openvino.ai#openvino-genai-tokenizer)

-
*class*openvino_genai.Tokenizer[#](https://docs.openvino.ai#openvino_genai.Tokenizer) Bases:

`pybind11_object`

The class is used to encode prompts and decode resulting tokens

Chat template is initialized from sources in the following order overriding the previous value: 1. chat_template entry from tokenizer_config.json 2. chat_template entry from processor_config.json 3. chat_template entry from chat_template.json 4. chat_template entry from rt_info section of openvino.Model 5. If the template is known to be not supported by GenAI, it’s

replaced with a simplified supported version.

-
__init__(
**args*,***kwargs*)[#](https://docs.openvino.ai#openvino_genai.Tokenizer.__init__) Overloaded function.

__init__(self: openvino_genai.py_openvino_genai.Tokenizer, tokenizer_path: os.PathLike | str | bytes, properties: collections.abc.Mapping[str, object] = {},

[**](https://docs.openvino.ai#id1)kwargs) -> None__init__(self: openvino_genai.py_openvino_genai.Tokenizer, tokenizer_model: str, tokenizer_weights: openvino._pyopenvino.Tensor, detokenizer_model: str, detokenizer_weights: openvino._pyopenvino.Tensor,

[**](https://docs.openvino.ai#id3)kwargs) -> None


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

(self, history, ...[, ...])`apply_chat_template`

Applies a chat template to format chat history into a prompt string.

(*args, **kwargs)`decode`

Overloaded function.

(*args, **kwargs)`encode`

Overloaded function.

(self)`get_bos_token`

(self)`get_bos_token_id`

(self)`get_eos_token`

(self)`get_eos_token_id`

(self)`get_pad_token`

(self)`get_pad_token_id`

(self)`get_vocab`

Returns the vocabulary as a Python dictionary with bytes keys and integer values.

(self)`get_vocab_vector`

Returns the vocabulary as list of strings, where position of a string represents token ID.

(self, chat_template)`set_chat_template`

Override a chat_template read from tokenizer_config.json.

(self)`supports_paired_input`

Returns true if the tokenizer supports paired input, false otherwise.

Attributes

-
__annotations__
*= {}*[#](https://docs.openvino.ai#openvino_genai.Tokenizer.__annotations__)

-
__class__
[#](https://docs.openvino.ai#openvino_genai.Tokenizer.__class__) alias of

`pybind11_type`


-
__delattr__(
*name*,*/*)[#](https://docs.openvino.ai#openvino_genai.Tokenizer.__delattr__) Implement delattr(self, name).


-
__dir__()
[#](https://docs.openvino.ai#openvino_genai.Tokenizer.__dir__) Default dir() implementation.


-
__eq__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.Tokenizer.__eq__) Return self==value.


-
__format__(
*format_spec*,*/*)[#](https://docs.openvino.ai#openvino_genai.Tokenizer.__format__) Default object formatter.

Return str(self) if format_spec is empty. Raise TypeError otherwise.


-
__ge__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.Tokenizer.__ge__) Return self>=value.


-
__getattribute__(
*name*,*/*)[#](https://docs.openvino.ai#openvino_genai.Tokenizer.__getattribute__) Return getattr(self, name).


-
__getstate__()
[#](https://docs.openvino.ai#openvino_genai.Tokenizer.__getstate__) Helper for pickle.


-
__gt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.Tokenizer.__gt__) Return self>value.


-
__hash__()
[#](https://docs.openvino.ai#openvino_genai.Tokenizer.__hash__) Return hash(self).


-
__init__(
**args*,***kwargs*)[#](https://docs.openvino.ai#id0) Overloaded function.

__init__(self: openvino_genai.py_openvino_genai.Tokenizer, tokenizer_path: os.PathLike | str | bytes, properties: collections.abc.Mapping[str, object] = {},

[**](https://docs.openvino.ai#id5)kwargs) -> None__init__(self: openvino_genai.py_openvino_genai.Tokenizer, tokenizer_model: str, tokenizer_weights: openvino._pyopenvino.Tensor, detokenizer_model: str, detokenizer_weights: openvino._pyopenvino.Tensor,

[**](https://docs.openvino.ai#id7)kwargs) -> None


-
__init_subclass__()
[#](https://docs.openvino.ai#openvino_genai.Tokenizer.__init_subclass__) This method is called when a class is subclassed.

The default implementation does nothing. It may be overridden to extend subclasses.


-
__le__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.Tokenizer.__le__) Return self<=value.


-
__lt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.Tokenizer.__lt__) Return self<value.


-
__ne__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.Tokenizer.__ne__) Return self!=value.


-
__new__(
***kwargs*)[#](https://docs.openvino.ai#openvino_genai.Tokenizer.__new__)

-
__reduce__()
[#](https://docs.openvino.ai#openvino_genai.Tokenizer.__reduce__) Helper for pickle.


-
__reduce_ex__(
*protocol*,*/*)[#](https://docs.openvino.ai#openvino_genai.Tokenizer.__reduce_ex__) Helper for pickle.


-
__repr__()
[#](https://docs.openvino.ai#openvino_genai.Tokenizer.__repr__) Return repr(self).


-
__setattr__(
*name*,*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.Tokenizer.__setattr__) Implement setattr(self, name, value).


-
__sizeof__()
[#](https://docs.openvino.ai#openvino_genai.Tokenizer.__sizeof__) Size of object in memory, in bytes.


-
__str__()
[#](https://docs.openvino.ai#openvino_genai.Tokenizer.__str__) Return str(self).


-
__subclasshook__()
[#](https://docs.openvino.ai#openvino_genai.Tokenizer.__subclasshook__) Abstract classes can override this to customize issubclass().

This is invoked early on by abc.ABCMeta.__subclasscheck__(). It should return True, False or NotImplemented. If it returns NotImplemented, the normal algorithm is used. Otherwise, it overrides the normal algorithm (and the outcome is cached).


-
_pybind11_conduit_v1_()
[#](https://docs.openvino.ai#openvino_genai.Tokenizer._pybind11_conduit_v1_)

-
apply_chat_template(
*self:*,[openvino_genai.py_openvino_genai.Tokenizer](https://docs.openvino.ai#openvino_genai.Tokenizer)*history:*,[openvino_genai.py_openvino_genai.ChatHistory](https://docs.openvino.ai/openvino_genai.ChatHistory.html#openvino_genai.ChatHistory)| collections.abc.Sequence[dict]*add_generation_prompt: bool*,*chat_template: str = ''*,*tools: collections.abc.Sequence[dict] | None = None*,*extra_context: dict | None = None*) str[#](https://docs.openvino.ai#openvino_genai.Tokenizer.apply_chat_template) Applies a chat template to format chat history into a prompt string.


-
*property*chat_template[#](https://docs.openvino.ai#openvino_genai.Tokenizer.chat_template)

-
decode(
**args*,***kwargs*)[#](https://docs.openvino.ai#openvino_genai.Tokenizer.decode) Overloaded function.

decode(self: openvino_genai.py_openvino_genai.Tokenizer, tokens: collections.abc.Sequence[typing.SupportsInt], skip_special_tokens: bool = True) -> str


Decode a sequence into a string prompt.

decode(self: openvino_genai.py_openvino_genai.Tokenizer, tokens: openvino._pyopenvino.Tensor, skip_special_tokens: bool = True) -> list[str]


Decode tensor into a list of string prompts.

decode(self: openvino_genai.py_openvino_genai.Tokenizer, tokens: collections.abc.Sequence[collections.abc.Sequence[typing.SupportsInt]], skip_special_tokens: bool = True) -> list[str]


Decode a batch of tokens into a list of string prompt.


-
encode(
**args*,***kwargs*)[#](https://docs.openvino.ai#openvino_genai.Tokenizer.encode) Overloaded function.

encode(self: openvino_genai.py_openvino_genai.Tokenizer, prompts: collections.abc.Sequence[str], add_special_tokens: bool = True, pad_to_max_length: bool = False, max_length: typing.SupportsInt | None = None, padding_side: str | None = None) -> openvino_genai.py_openvino_genai.TokenizedInputs


Encodes a list of prompts into tokenized inputs. Args:

‘prompts’ - list of prompts to encode ‘add_special_tokens’ - whether to add special tokens like BOS, EOS, PAD. Default is True. ‘pad_to_max_length’ - whether to pad the sequence to the maximum length. Default is False. ‘max_length’ - maximum length of the sequence. If None (default), the value will be taken from the IR (where default value from original HF/GGUF model is stored). ‘padding_side’ - side to pad the sequence, can be ‘left’ or ‘right’. If None (default), the value will be taken from the IR (where default value from original HF/GGUF model is stored).

- Returns:
TokenizedInputs object containing input_ids and attention_mask tensors.


encode(self: openvino_genai.py_openvino_genai.Tokenizer, prompt: str, add_special_tokens: bool = True, pad_to_max_length: bool = False, max_length: typing.SupportsInt | None = None, padding_side: str | None = None) -> openvino_genai.py_openvino_genai.TokenizedInputs


Encodes a single prompt into tokenized input. Args:

‘prompt’ - prompt to encode ‘add_special_tokens’ - whether to add special tokens like BOS, EOS, PAD. Default is True. ‘pad_to_max_length’ - whether to pad the sequence to the maximum length. Default is False. ‘max_length’ - maximum length of the sequence. If None (default), the value will be taken from the IR (where default value from original HF/GGUF model is stored). ‘padding_side’ - side to pad the sequence, can be ‘left’ or ‘right’. If None (default), the value will be taken from the IR (where default value from original HF/GGUF model is stored).

- Returns:
TokenizedInputs object containing input_ids and attention_mask tensors.


encode(self: openvino_genai.py_openvino_genai.Tokenizer, prompts_1: collections.abc.Sequence[str], prompts_2: collections.abc.Sequence[str], add_special_tokens: bool = True, pad_to_max_length: bool = False, max_length: typing.SupportsInt | None = None, padding_side: str | None = None) -> openvino_genai.py_openvino_genai.TokenizedInputs


Encodes a list of prompts into tokenized inputs. The number of strings must be the same, or one of the inputs can contain one string. In the latter case, the single-string input will be broadcast into the shape of the other input, which is more efficient than repeating the string in pairs.) Args:

‘prompts_1’ - list of prompts to encode ‘prompts_2’ - list of prompts to encode ‘add_special_tokens’ - whether to add special tokens like BOS, EOS, PAD. Default is True. ‘pad_to_max_length’ - whether to pad the sequence to the maximum length. Default is False. ‘max_length’ - maximum length of the sequence. If None (default), the value will be taken from the IR (where default value from original HF/GGUF model is stored). ‘padding_side’ - side to pad the sequence, can be ‘left’ or ‘right’. If None (default), the value will be taken from the IR (where default value from original HF/GGUF model is stored).

- Returns:
TokenizedInputs object containing input_ids and attention_mask tensors.


encode(self: openvino_genai.py_openvino_genai.Tokenizer, prompts: list, add_special_tokens: bool = True, pad_to_max_length: bool = False, max_length: typing.SupportsInt | None = None, padding_side: str | None = None) -> openvino_genai.py_openvino_genai.TokenizedInputs


Encodes a list of paired prompts into tokenized inputs. Input format is same as for HF paired input [[prompt_1, prompt_2], …]. Args:

‘prompts’ - list of prompts to encoden ‘add_special_tokens’ - whether to add special tokens like BOS, EOS, PAD. Default is True. ‘pad_to_max_length’ - whether to pad the sequence to the maximum length. Default is False. ‘max_length’ - maximum length of the sequence. If None (default), the value will be taken from the IR (where default value from original HF/GGUF model is stored). ‘padding_side’ - side to pad the sequence, can be ‘left’ or ‘right’. If None (default), the value will be taken from the IR (where default value from original HF/GGUF model is stored).

- Returns:
TokenizedInputs object containing input_ids and attention_mask tensors.



-
get_bos_token(
*self:*) str[openvino_genai.py_openvino_genai.Tokenizer](https://docs.openvino.ai#openvino_genai.Tokenizer)[#](https://docs.openvino.ai#openvino_genai.Tokenizer.get_bos_token)

-
get_bos_token_id(
*self:*) int[openvino_genai.py_openvino_genai.Tokenizer](https://docs.openvino.ai#openvino_genai.Tokenizer)[#](https://docs.openvino.ai#openvino_genai.Tokenizer.get_bos_token_id)

-
get_eos_token(
*self:*) str[openvino_genai.py_openvino_genai.Tokenizer](https://docs.openvino.ai#openvino_genai.Tokenizer)[#](https://docs.openvino.ai#openvino_genai.Tokenizer.get_eos_token)

-
get_eos_token_id(
*self:*) int[openvino_genai.py_openvino_genai.Tokenizer](https://docs.openvino.ai#openvino_genai.Tokenizer)[#](https://docs.openvino.ai#openvino_genai.Tokenizer.get_eos_token_id)

-
get_original_chat_template(
*self:*) str[openvino_genai.py_openvino_genai.Tokenizer](https://docs.openvino.ai#openvino_genai.Tokenizer)[#](https://docs.openvino.ai#openvino_genai.Tokenizer.get_original_chat_template)

-
get_pad_token(
*self:*) str[openvino_genai.py_openvino_genai.Tokenizer](https://docs.openvino.ai#openvino_genai.Tokenizer)[#](https://docs.openvino.ai#openvino_genai.Tokenizer.get_pad_token)

-
get_pad_token_id(
*self:*) int[openvino_genai.py_openvino_genai.Tokenizer](https://docs.openvino.ai#openvino_genai.Tokenizer)[#](https://docs.openvino.ai#openvino_genai.Tokenizer.get_pad_token_id)

-
get_vocab(
*self:*) dict[openvino_genai.py_openvino_genai.Tokenizer](https://docs.openvino.ai#openvino_genai.Tokenizer)[#](https://docs.openvino.ai#openvino_genai.Tokenizer.get_vocab) - Returns the vocabulary as a Python dictionary with bytes keys and integer values.
Bytes are used for keys because not all vocabulary entries might be valid UTF-8 strings.



-
get_vocab_vector(
*self:*) list[str][openvino_genai.py_openvino_genai.Tokenizer](https://docs.openvino.ai#openvino_genai.Tokenizer)[#](https://docs.openvino.ai#openvino_genai.Tokenizer.get_vocab_vector) Returns the vocabulary as list of strings, where position of a string represents token ID.


-
set_chat_template(
*self:*,[openvino_genai.py_openvino_genai.Tokenizer](https://docs.openvino.ai#openvino_genai.Tokenizer)*chat_template: str*) None[#](https://docs.openvino.ai#openvino_genai.Tokenizer.set_chat_template) Override a chat_template read from tokenizer_config.json.


-
supports_paired_input(
*self:*) bool[openvino_genai.py_openvino_genai.Tokenizer](https://docs.openvino.ai#openvino_genai.Tokenizer)[#](https://docs.openvino.ai#openvino_genai.Tokenizer.supports_paired_input) Returns true if the tokenizer supports paired input, false otherwise.


-
__init__(