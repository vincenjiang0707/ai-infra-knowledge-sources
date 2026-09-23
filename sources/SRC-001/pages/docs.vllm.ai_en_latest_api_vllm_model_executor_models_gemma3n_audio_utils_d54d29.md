source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/gemma3n_audio_utils/
lastmod: 2026-09-23

#

`vllm.model_executor.models.gemma3n_audio_utils`

[¶](https://docs.vllm.ai#vllm.model_executor.models.gemma3n_audio_utils)

Lightweight utility functions for Gemma3n audio processing.

This module is separate from gemma3n_mm.py to avoid heavy CUDA dependencies, making it testable without a full vLLM build.

Functions:

-
–[adjust_audio_features_to_expected_length](https://docs.vllm.ai#vllm.model_executor.models.gemma3n_audio_utils.adjust_audio_features_to_expected_length)Adjust audio features to expected token length via padding or truncation.


##

`adjust_audio_features_to_expected_length(audio_features, expected_tokens, audio_padding_embs)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.gemma3n_audio_utils.adjust_audio_features_to_expected_length)

Adjust audio features to expected token length via padding or truncation.

The Gemma3nProcessor expects all audio will be ~30s in length and inserts a fixed number of audio soft tokens into the text. However, the audio preprocessing and encoder do not guarantee they will produce exactly that many soft tokens; they may produce fewer tokens (for shorter audio) or more tokens (for longer audio or due to BOA/EOA special tokens).

This function handles both cases: - If fewer tokens: pad with the provided padding embeddings - If more tokens: truncate to the expected count

Parameters:

-

(`audio_features`

[¶](https://docs.vllm.ai#vllm.model_executor.models.gemma3n_audio_utils.adjust_audio_features_to_expected_length(audio_features))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Audio embeddings tensor of shape (batch_size, seq_len, embed_dim)

-

(`expected_tokens`

[¶](https://docs.vllm.ai#vllm.model_executor.models.gemma3n_audio_utils.adjust_audio_features_to_expected_length(expected_tokens))

) –[int](https://docs.python.org/3/builtins/functions.html#int)The expected number of audio tokens (e.g., 188)

-

(`audio_padding_embs`

[¶](https://docs.vllm.ai#vllm.model_executor.models.gemma3n_audio_utils.adjust_audio_features_to_expected_length(audio_padding_embs))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Padding embeddings tensor of shape (1, 1, embed_dim)


Returns:

-

–[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Tuple of:

-

–[int](https://docs.python.org/3/builtins/functions.html#int)- adjusted_features: Audio features adjusted to expected_tokens length

-

–[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor),[int](https://docs.python.org/3/builtins/functions.html#int)]- tokens_truncated: Number of tokens truncated (0 if padding was applied)