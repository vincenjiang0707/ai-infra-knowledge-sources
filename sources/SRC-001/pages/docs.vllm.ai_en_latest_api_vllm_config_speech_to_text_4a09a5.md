source: https://docs.vllm.ai/en/latest/api/vllm/config/speech_to_text/
lastmod: 2026-09-23

#

`vllm.config.speech_to_text`

[¶](https://docs.vllm.ai#vllm.config.speech_to_text)

Classes:

-
–[SpeechToTextConfig](https://docs.vllm.ai#vllm.config.speech_to_text.SpeechToTextConfig)Configuration for speech-to-text models.

-
–[SpeechToTextParams](https://docs.vllm.ai#vllm.config.speech_to_text.SpeechToTextParams)All parameters consumed by

`get_generation_prompt()`

.

##

`SpeechToTextConfig`

[¶](https://docs.vllm.ai#vllm.config.speech_to_text.SpeechToTextConfig)

Configuration for speech-to-text models.

Attributes:

-
([max_audio_clip_s](https://docs.vllm.ai#vllm.config.speech_to_text.SpeechToTextConfig.max_audio_clip_s)

) –[int](https://docs.python.org/3/builtins/functions.html#int)| NoneMaximum duration in seconds for a single audio clip without chunking.

-
([min_energy_split_window_size](https://docs.vllm.ai#vllm.config.speech_to_text.SpeechToTextConfig.min_energy_split_window_size)

) –[int](https://docs.python.org/3/builtins/functions.html#int)| NoneWindow size in samples for finding low-energy (quiet) regions to split

-
([overlap_chunk_second](https://docs.vllm.ai#vllm.config.speech_to_text.SpeechToTextConfig.overlap_chunk_second)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Overlap duration in seconds between consecutive audio chunks when

-
([sample_rate](https://docs.vllm.ai#vllm.config.speech_to_text.SpeechToTextConfig.sample_rate)

) –[float](https://docs.python.org/3/builtins/functions.html#float)Sample rate (Hz) to resample input audio to. Most speech models expect


## Source code in `vllm/config/speech_to_text.py`


###

`max_audio_clip_s = 30`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.speech_to_text.SpeechToTextConfig.max_audio_clip_s)

Maximum duration in seconds for a single audio clip without chunking. Audio longer than this will be split into smaller chunks if `allow_audio_chunking`

evaluates to True, otherwise it will be rejected. `None`

means audio duration can be unlimited and won't be chunked.

###

`min_energy_split_window_size = 1600`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.speech_to_text.SpeechToTextConfig.min_energy_split_window_size)

Window size in samples for finding low-energy (quiet) regions to split audio chunks. The algorithm looks for the quietest moment within this window to minimize cutting through speech. Default 1600 samples ≈ 100ms at 16kHz. If None, no chunking will be done.

###

`overlap_chunk_second = 1`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.speech_to_text.SpeechToTextConfig.overlap_chunk_second)

Overlap duration in seconds between consecutive audio chunks when splitting long audio. This helps maintain context across chunk boundaries and improves transcription quality at split points.

###

`sample_rate = 16000`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.speech_to_text.SpeechToTextConfig.sample_rate)

Sample rate (Hz) to resample input audio to. Most speech models expect 16kHz audio input. The input audio will be automatically resampled to this rate before processing.

##

`SpeechToTextParams`

`dataclass`

[¶](https://docs.vllm.ai#vllm.config.speech_to_text.SpeechToTextParams)

All parameters consumed by `get_generation_prompt()`

.

`TranscriptionRequest.build_stt_params()`

constructs this object, mapping API-level fields into typed attributes. Models only receive this object, so new parameters can be added here without changing the `get_generation_prompt`

signature.

Attributes:

-
([audio](https://docs.vllm.ai#vllm.config.speech_to_text.SpeechToTextParams.audio)

) –[ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray)Resampled audio waveform for a single chunk.

-
([hotwords](https://docs.vllm.ai#vllm.config.speech_to_text.SpeechToTextParams.hotwords)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)| Nonehotwords refers to a list of important words or phrases that the model

-
([language](https://docs.vllm.ai#vllm.config.speech_to_text.SpeechToTextParams.language)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)| NoneISO 639-1 language code (validated / auto-detected).

-
([model_config](https://docs.vllm.ai#vllm.config.speech_to_text.SpeechToTextParams.model_config)

) –[ModelConfig](https://docs.vllm.ai/model/#vllm.config.model.ModelConfig)Model configuration.

-
([request_prompt](https://docs.vllm.ai#vllm.config.speech_to_text.SpeechToTextParams.request_prompt)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)Optional text prompt to guide the model.

-
([stt_config](https://docs.vllm.ai#vllm.config.speech_to_text.SpeechToTextParams.stt_config)

) –[SpeechToTextConfig](https://docs.vllm.ai#vllm.config.speech_to_text.SpeechToTextConfig)Server-level speech-to-text configuration.

-
([task_type](https://docs.vllm.ai#vllm.config.speech_to_text.SpeechToTextParams.task_type)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)`"transcribe"`

or`"translate"`

. -
([to_language](https://docs.vllm.ai#vllm.config.speech_to_text.SpeechToTextParams.to_language)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)| NoneTarget language for translation (model-dependent).


## Source code in `vllm/config/speech_to_text.py`


###

`audio`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.speech_to_text.SpeechToTextParams.audio)

Resampled audio waveform for a single chunk.

###

`hotwords = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.speech_to_text.SpeechToTextParams.hotwords)

hotwords refers to a list of important words or phrases that the model should pay extra attention to during transcription.

###

`language = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.speech_to_text.SpeechToTextParams.language)

ISO 639-1 language code (validated / auto-detected).

###

`model_config`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.speech_to_text.SpeechToTextParams.model_config)

Model configuration.

###

`request_prompt = ''`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.speech_to_text.SpeechToTextParams.request_prompt)

Optional text prompt to guide the model.

###

`stt_config`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.speech_to_text.SpeechToTextParams.stt_config)

Server-level speech-to-text configuration.

###

`task_type = 'transcribe'`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.speech_to_text.SpeechToTextParams.task_type)

`"transcribe"`

or `"translate"`

.

###

`to_language = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.speech_to_text.SpeechToTextParams.to_language)

Target language for translation (model-dependent).