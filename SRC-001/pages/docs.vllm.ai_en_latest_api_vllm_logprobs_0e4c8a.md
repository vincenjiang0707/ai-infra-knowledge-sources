source: https://docs.vllm.ai/en/latest/api/vllm/logprobs/
lastmod: 2026-09-23

#

`vllm.logprobs`

[¶](https://docs.vllm.ai#vllm.logprobs)

Classes:

-
–[FlatLogprobs](https://docs.vllm.ai#vllm.logprobs.FlatLogprobs)Flat logprobs of a request into multiple primitive type lists.

-
–[Logprob](https://docs.vllm.ai#vllm.logprobs.Logprob)Infos for supporting OpenAI compatible logprobs and token ranks.


Functions:

-
–[append_logprobs_for_next_position](https://docs.vllm.ai#vllm.logprobs.append_logprobs_for_next_position)Appends logprobs for the next position.

-
–[create_prompt_logprobs](https://docs.vllm.ai#vllm.logprobs.create_prompt_logprobs)Creates a container to store prompt logprobs for a request.

-
–[create_sample_logprobs](https://docs.vllm.ai#vllm.logprobs.create_sample_logprobs)Creates a container to store decode logprobs for a request.


##

`FlatLogprobs`

`dataclass`

[¶](https://docs.vllm.ai#vllm.logprobs.FlatLogprobs)

Bases: [MutableSequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.MutableSequence)[LogprobsOnePosition | None]

Flat logprobs of a request into multiple primitive type lists.

Compared to list[dict[int, Logprob]], this data structure reduced GC overhead significantly. As it flattened logprob information for all positions and ranks in to multiple primitive type lists (i.e. logprobs, token_ids, ranks per token_ids, decoded_tokens). So regardless of the sequence length and top_logprobs setup, FlatLogprobs would only introduce a constant amount of objects.

As each position might contains different amount of ranks, start_indices_per_position would be used to access the logprob ranges for different positions.

NOTE: To reduce the migration overhead and improve backward compatibility, we support the key Sequence APIs of list, so it could act as list[LogprobsOnePosition]

Methods:

-
–[__getitem__](https://docs.vllm.ai#vllm.logprobs.FlatLogprobs.__getitem__)Extracts logprobs of a given position or slice.

-
–[__iter__](https://docs.vllm.ai#vllm.logprobs.FlatLogprobs.__iter__)Iterates the container and yields LogprobsOnePosition for

-
–[__len__](https://docs.vllm.ai#vllm.logprobs.FlatLogprobs.__len__)Gets number of positions stored in the container.

-
–[append](https://docs.vllm.ai#vllm.logprobs.FlatLogprobs.append)Appends the container with logprobs for the next position.

-
–[append_fast](https://docs.vllm.ai#vllm.logprobs.FlatLogprobs.append_fast)Appends logprobs for the next position without creating

-
–[extend](https://docs.vllm.ai#vllm.logprobs.FlatLogprobs.extend)Extends the container with logprobs for the next multiple positions.


## Source code in `vllm/logprobs.py`


|
|

###

`__getitem__(index)`

[¶](https://docs.vllm.ai#vllm.logprobs.FlatLogprobs.__getitem__)

Extracts logprobs of a given position or slice.

## Source code in `vllm/logprobs.py`


###

`__iter__()`

[¶](https://docs.vllm.ai#vllm.logprobs.FlatLogprobs.__iter__)

Iterates the container and yields LogprobsOnePosition for each position.

###

`__len__()`

[¶](https://docs.vllm.ai#vllm.logprobs.FlatLogprobs.__len__)

###

`append(logprobs_one_position)`

[¶](https://docs.vllm.ai#vllm.logprobs.FlatLogprobs.append)

Appends the container with logprobs for the next position.

## Source code in `vllm/logprobs.py`


###

`append_fast(token_ids, logprobs, ranks, decoded_tokens)`

[¶](https://docs.vllm.ai#vllm.logprobs.FlatLogprobs.append_fast)

Appends logprobs for the next position without creating the intermediate logprob dictionary.

## Source code in `vllm/logprobs.py`


###

`extend(logprobs_multi_positions)`

[¶](https://docs.vllm.ai#vllm.logprobs.FlatLogprobs.extend)

Extends the container with logprobs for the next multiple positions.

##

`Logprob`

`dataclass`

[¶](https://docs.vllm.ai#vllm.logprobs.Logprob)

Infos for supporting OpenAI compatible logprobs and token ranks.

Attributes:

-
(`logprob`


) –[float](https://docs.python.org/3/builtins/functions.html#float)The logprob of chosen token

-
(`rank`


) –[int](https://docs.python.org/3/builtins/functions.html#int)| NoneThe vocab rank of chosen token (>=1)

-
(`decoded_token`


) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)| NoneThe decoded chosen token index


## Source code in `vllm/logprobs.py`


##

`append_logprobs_for_next_position(request_logprobs, token_ids, logprobs, decoded_tokens, rank, num_logprobs)`

[¶](https://docs.vllm.ai#vllm.logprobs.append_logprobs_for_next_position)

Appends logprobs for the next position.

## Source code in `vllm/logprobs.py`


##

`create_prompt_logprobs(flat_logprobs)`

[¶](https://docs.vllm.ai#vllm.logprobs.create_prompt_logprobs)

Creates a container to store prompt logprobs for a request.