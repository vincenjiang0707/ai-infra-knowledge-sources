source: https://docs.vllm.ai/en/latest/api/vllm/entrypoints/pooling/scoring/utils/
lastmod: 2026-09-24

#

`vllm.entrypoints.pooling.scoring.utils`

[¶](https://docs.vllm.ai#vllm.entrypoints.pooling.scoring.utils)

Functions:

-
–[compress_token_type_ids](https://docs.vllm.ai#vllm.entrypoints.pooling.scoring.utils.compress_token_type_ids)Return position of the first 1 or the length of the list

-
–[compute_maxsim_score](https://docs.vllm.ai#vllm.entrypoints.pooling.scoring.utils.compute_maxsim_score)Compute ColBERT MaxSim score.

-
–[get_num_special_tokens_for_pair](https://docs.vllm.ai#vllm.entrypoints.pooling.scoring.utils.get_num_special_tokens_for_pair)Get number of special tokens added for a text pair encoding.

-
–[parse_score_data](https://docs.vllm.ai#vllm.entrypoints.pooling.scoring.utils.parse_score_data)Parse a query-document pair into text prompts and shared multi-modal

-
–[parse_score_data_single](https://docs.vllm.ai#vllm.entrypoints.pooling.scoring.utils.parse_score_data_single)Parse

**one**ScoreData into a text prompt and its own multi-modal -
–[score_data_to_prompts](https://docs.vllm.ai#vllm.entrypoints.pooling.scoring.utils.score_data_to_prompts)Convert a list of ScoreData into PromptType objects.

-
–[truncate_text_to_tokens](https://docs.vllm.ai#vllm.entrypoints.pooling.scoring.utils.truncate_text_to_tokens)Truncate text to a maximum number of content tokens.


##

`_ensure_str(content)`

[¶](https://docs.vllm.ai#vllm.entrypoints.pooling.scoring.utils._ensure_str)

Extract a single string prompt from parsed conversation content.

## Source code in `vllm/entrypoints/pooling/scoring/utils.py`


##

`compress_token_type_ids(token_type_ids)`

[¶](https://docs.vllm.ai#vllm.entrypoints.pooling.scoring.utils.compress_token_type_ids)

Return position of the first 1 or the length of the list if not found.

## Source code in `vllm/entrypoints/pooling/scoring/utils.py`


##

`compute_maxsim_score(q_emb, d_emb)`

[¶](https://docs.vllm.ai#vllm.entrypoints.pooling.scoring.utils.compute_maxsim_score)

Compute ColBERT MaxSim score.

Parameters:

-

(`q_emb`

[¶](https://docs.vllm.ai#vllm.entrypoints.pooling.scoring.utils.compute_maxsim_score(q_emb))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Query token embeddings [query_len, dim]

-

(`d_emb`

[¶](https://docs.vllm.ai#vllm.entrypoints.pooling.scoring.utils.compute_maxsim_score(d_emb))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Document token embeddings [doc_len, dim]


Returns:

-

–[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)MaxSim score (sum over query tokens of max similarity to any doc token)


## Source code in `vllm/entrypoints/pooling/scoring/utils.py`


##

`get_num_special_tokens_for_pair(tokenizer)`

[¶](https://docs.vllm.ai#vllm.entrypoints.pooling.scoring.utils.get_num_special_tokens_for_pair)

Get number of special tokens added for a text pair encoding.

## Source code in `vllm/entrypoints/pooling/scoring/utils.py`


##

`parse_score_data(data_1, data_2, model_config)`

[¶](https://docs.vllm.ai#vllm.entrypoints.pooling.scoring.utils.parse_score_data)

Parse a query-document pair into text prompts and shared multi-modal data.

Uses a **single** :class:`MultiModalItemTracker`

so that multi-modal items from both inputs are merged into one `mm_data`

dict. This is the correct behaviour for cross-encoder scoring, where query and document are concatenated into a single model prompt.

## Source code in `vllm/entrypoints/pooling/scoring/utils.py`


##

`parse_score_data_single(data, role, model_config)`

[¶](https://docs.vllm.ai#vllm.entrypoints.pooling.scoring.utils.parse_score_data_single)

Parse **one** ScoreData into a text prompt and its own multi-modal data.

Unlike :func:`parse_score_data`

, each call creates an **independent** :class:`MultiModalItemTracker`

so multi-modal items are kept separate. This is the correct behaviour for late-interaction scoring, where query and document are encoded independently.

## Source code in `vllm/entrypoints/pooling/scoring/utils.py`


##

`score_data_to_prompts(data_list, role, model_config)`

[¶](https://docs.vllm.ai#vllm.entrypoints.pooling.scoring.utils.score_data_to_prompts)

Convert a list of ScoreData into PromptType objects.

For plain text inputs, returns the string directly. For multimodal inputs (list of content parts), parses them into a :class:`TextPrompt`

with attached `multi_modal_data`

/ `multi_modal_uuids`

.

This is used by late-interaction scoring where each query/document is encoded independently.

## Source code in `vllm/entrypoints/pooling/scoring/utils.py`


##

`truncate_text_to_tokens(text, tokenizer, max_tokens)`

[¶](https://docs.vllm.ai#vllm.entrypoints.pooling.scoring.utils.truncate_text_to_tokens)

Truncate text to a maximum number of content tokens.

Uses offset_mapping to slice the original text at the exact character boundary, avoiding lossy encode→decode round-trips that can shift the token count by 1-3 tokens due to BPE merge boundary changes.