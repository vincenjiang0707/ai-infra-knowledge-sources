source: https://docs.vllm.ai/en/latest/api/vllm/entrypoints/generate/beam_search/utils/
lastmod: 2026-09-24

#

`vllm.entrypoints.generate.beam_search.utils`

[¶](https://docs.vllm.ai#vllm.entrypoints.generate.beam_search.utils)

Classes:

-
–[BeamSearchOutput](https://docs.vllm.ai#vllm.entrypoints.generate.beam_search.utils.BeamSearchOutput)The output of beam search.

-
–[BeamSearchSequence](https://docs.vllm.ai#vllm.entrypoints.generate.beam_search.utils.BeamSearchSequence)A sequence for beam search.


Functions:

-
–[get_beam_search_score](https://docs.vllm.ai#vllm.entrypoints.generate.beam_search.utils.get_beam_search_score)Calculate the beam search score with length penalty.


##

`BeamSearchOutput`

`dataclass`

[¶](https://docs.vllm.ai#vllm.entrypoints.generate.beam_search.utils.BeamSearchOutput)

The output of beam search. It contains the list of the best beam search sequences. The length of the list is equal to the beam width.

## Source code in `vllm/entrypoints/generate/beam_search/utils.py`


##

`BeamSearchSequence`

`dataclass`

[¶](https://docs.vllm.ai#vllm.entrypoints.generate.beam_search.utils.BeamSearchSequence)

A sequence for beam search. It keeps track of the tokens and the log probability of the sequence. The text field is optional and will only be filled when the sequence is about to be returned to the user.

## Source code in `vllm/entrypoints/generate/beam_search/utils.py`


###

`_build_encoder_decoder_inputs(prompt)`

[¶](https://docs.vllm.ai#vllm.entrypoints.generate.beam_search.utils.BeamSearchSequence._build_encoder_decoder_inputs)

Rebuild the encoder-decoder inputs with the current beam search sequence's tokens.

FIXME (alex) - the encoder multimodal cache is not properly wired up yet, which means that currently we are running the encoder on every new beam because num_computed_tokens is 0 on each new request. This will be fixed once the cache is correctly implemented.

## Source code in `vllm/entrypoints/generate/beam_search/utils.py`


##

`get_beam_search_score(tokens, cumulative_logprob, eos_token_id, length_penalty=1.0)`

[¶](https://docs.vllm.ai#vllm.entrypoints.generate.beam_search.utils.get_beam_search_score)

Calculate the beam search score with length penalty.

Adapted from

https://github.com/huggingface/transformers/blob/ccb92be23def445f2afdea94c31286f84b89eb5b/src/transformers/generation/beam_search.py#L938