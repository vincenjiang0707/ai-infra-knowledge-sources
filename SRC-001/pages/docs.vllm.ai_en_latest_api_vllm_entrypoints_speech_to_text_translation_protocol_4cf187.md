source: https://docs.vllm.ai/en/latest/api/vllm/entrypoints/speech_to_text/translation/protocol/
lastmod: 2026-09-23

#

`vllm.entrypoints.speech_to_text.translation.protocol`

[¶](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.translation.protocol)

Classes:

-
–[TranslationRequest](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.translation.protocol.TranslationRequest) -
–[TranslationResponse](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.translation.protocol.TranslationResponse) -
–[TranslationResponseVerbose](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.translation.protocol.TranslationResponseVerbose) -
–[TranslationSegment](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.translation.protocol.TranslationSegment) -
–[TranslationWord](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.translation.protocol.TranslationWord)

##

`TranslationRequest`

[¶](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.translation.protocol.TranslationRequest)

Bases: `OpenAIBaseModel`


Attributes:

-
([file](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.translation.protocol.TranslationRequest.file)`UploadFile`

) –The audio file object (not file name) to translate, in one of these

-
([frequency_penalty](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.translation.protocol.TranslationRequest.frequency_penalty)

) –[float](https://docs.python.org/3/builtins/functions.html#float)| NoneThe frequency penalty to use for sampling.

-
([hotwords](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.translation.protocol.TranslationRequest.hotwords)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)| Nonehotwords refers to a list of important words or phrases that the model

-
([include_stop_str_in_output](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.translation.protocol.TranslationRequest.include_stop_str_in_output)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Whether to include the stop strings in output text.

-
([language](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.translation.protocol.TranslationRequest.language)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)| NoneThe language of the input audio we translate from.

-
([length_penalty](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.translation.protocol.TranslationRequest.length_penalty)

) –[float](https://docs.python.org/3/builtins/functions.html#float)Length penalty to be used for beam search.

-
([max_completion_tokens](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.translation.protocol.TranslationRequest.max_completion_tokens)

) –[int](https://docs.python.org/3/builtins/functions.html#int)| NoneThe maximum number of tokens to generate.

-
([min_p](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.translation.protocol.TranslationRequest.min_p)

) –[float](https://docs.python.org/3/builtins/functions.html#float)| NoneFilters out tokens with a probability lower than

`min_p`

, ensuring a -
([model](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.translation.protocol.TranslationRequest.model)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)| NoneID of the model to use.

-
([n](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.translation.protocol.TranslationRequest.n)

) –[int](https://docs.python.org/3/builtins/functions.html#int)The number of beams to be used in beam search.

-
([presence_penalty](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.translation.protocol.TranslationRequest.presence_penalty)

) –[float](https://docs.python.org/3/builtins/functions.html#float)| NoneThe presence penalty to use for sampling.

-
([prompt](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.translation.protocol.TranslationRequest.prompt)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)An optional text to guide the model's style or continue a previous audio

-
([repetition_penalty](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.translation.protocol.TranslationRequest.repetition_penalty)

) –[float](https://docs.python.org/3/builtins/functions.html#float)| NoneThe repetition penalty to use for sampling.

-
([response_format](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.translation.protocol.TranslationRequest.response_format)`AudioResponseFormat`

) –The format of the output, in one of these options:

`json`

,`text`

,`srt`

, -
([seed](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.translation.protocol.TranslationRequest.seed)

) –[int](https://docs.python.org/3/builtins/functions.html#int)| NoneThe seed to use for sampling.

-
([stream](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.translation.protocol.TranslationRequest.stream)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)| NoneCustom field not present in the original OpenAI definition. When set,

-
([temperature](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.translation.protocol.TranslationRequest.temperature)

) –[float](https://docs.python.org/3/builtins/functions.html#float)The sampling temperature, between 0 and 1.

-
([to_language](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.translation.protocol.TranslationRequest.to_language)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)| NoneThe language of the input audio we translate to.

-
([top_k](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.translation.protocol.TranslationRequest.top_k)

) –[int](https://docs.python.org/3/builtins/functions.html#int)| NoneLimits sampling to the

`k`

most probable tokens at each step. -
([top_p](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.translation.protocol.TranslationRequest.top_p)

) –[float](https://docs.python.org/3/builtins/functions.html#float)| NoneEnables nucleus (top-p) sampling, where tokens are selected from the

-
([use_beam_search](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.translation.protocol.TranslationRequest.use_beam_search)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Whether or not beam search should be used.


## Source code in `vllm/entrypoints/speech_to_text/translation/protocol.py`


|
|

###

`file`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.translation.protocol.TranslationRequest.file)

The audio file object (not file name) to translate, in one of these formats: flac, mp3, mp4, mpeg, mpga, m4a, ogg, wav, or webm.

###

`frequency_penalty = 0.0`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.translation.protocol.TranslationRequest.frequency_penalty)

The frequency penalty to use for sampling.

###

`hotwords = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.translation.protocol.TranslationRequest.hotwords)

hotwords refers to a list of important words or phrases that the model should pay extra attention to during transcription.

###

`include_stop_str_in_output = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.translation.protocol.TranslationRequest.include_stop_str_in_output)

Whether to include the stop strings in output text.

###

`language = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.translation.protocol.TranslationRequest.language)

The language of the input audio we translate from.

Supplying the input language in [ISO-639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) format will improve accuracy.

###

`length_penalty = 1.0`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.translation.protocol.TranslationRequest.length_penalty)

Length penalty to be used for beam search.

###

`max_completion_tokens = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.translation.protocol.TranslationRequest.max_completion_tokens)

The maximum number of tokens to generate.

###

`min_p = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.translation.protocol.TranslationRequest.min_p)

Filters out tokens with a probability lower than `min_p`

, ensuring a minimum likelihood threshold during sampling.

###

`model = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.translation.protocol.TranslationRequest.model)

ID of the model to use.

###

`n = 1`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.translation.protocol.TranslationRequest.n)

The number of beams to be used in beam search.

###

`presence_penalty = 0.0`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.translation.protocol.TranslationRequest.presence_penalty)

The presence penalty to use for sampling.

###

`prompt = Field(default='')`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.translation.protocol.TranslationRequest.prompt)

An optional text to guide the model's style or continue a previous audio segment.

The [prompt](https://platform.openai.com/docs/guides/speech-to-text#prompting) should match the audio language.

###

`repetition_penalty = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.translation.protocol.TranslationRequest.repetition_penalty)

The repetition penalty to use for sampling.

###

`response_format = Field(default='json')`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.translation.protocol.TranslationRequest.response_format)

The format of the output, in one of these options: `json`

, `text`

, `srt`

, `verbose_json`

, or `vtt`

.

###

`seed = Field(None, ge=(_LONG_INFO.min), le=(_LONG_INFO.max))`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.translation.protocol.TranslationRequest.seed)

The seed to use for sampling.

###

`stream = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.translation.protocol.TranslationRequest.stream)

Custom field not present in the original OpenAI definition. When set, it will enable output to be streamed in a similar fashion as the Chat Completion endpoint.

###

`temperature = Field(default=0.0)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.translation.protocol.TranslationRequest.temperature)

The sampling temperature, between 0 and 1.

Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused / deterministic. If set to 0, the model will use [log probability](https://en.wikipedia.org/wiki/Log_probability) to automatically increase the temperature until certain thresholds are hit.

###

`to_language = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.translation.protocol.TranslationRequest.to_language)

The language of the input audio we translate to.

Please note that this is not supported by all models, refer to the specific model documentation for more details. For instance, Whisper only supports `to_language=en`

.

###

`top_k = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.translation.protocol.TranslationRequest.top_k)

Limits sampling to the `k`

most probable tokens at each step.

###

`top_p = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.translation.protocol.TranslationRequest.top_p)

Enables nucleus (top-p) sampling, where tokens are selected from the smallest possible set whose cumulative probability exceeds `p`

.

###

`use_beam_search = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.translation.protocol.TranslationRequest.use_beam_search)

Whether or not beam search should be used.

##

`TranslationResponse`

[¶](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.translation.protocol.TranslationResponse)

##

`TranslationResponseVerbose`

[¶](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.translation.protocol.TranslationResponseVerbose)

Bases: `OpenAIBaseModel`


Attributes:

-
([duration](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.translation.protocol.TranslationResponseVerbose.duration)

) –[float](https://docs.python.org/3/builtins/functions.html#float)The duration of the input audio.

-
([language](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.translation.protocol.TranslationResponseVerbose.language)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)The language of the input audio.

-
([segments](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.translation.protocol.TranslationResponseVerbose.segments)

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[TranslationSegment](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.translation.protocol.TranslationSegment)] | NoneSegments of the translated text and their corresponding details.

-
([text](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.translation.protocol.TranslationResponseVerbose.text)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)The translated text.

-
([words](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.translation.protocol.TranslationResponseVerbose.words)

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[TranslationWord](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.translation.protocol.TranslationWord)] | NoneExtracted words and their corresponding timestamps.


## Source code in `vllm/entrypoints/speech_to_text/translation/protocol.py`


###

`duration`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.translation.protocol.TranslationResponseVerbose.duration)

The duration of the input audio.

###

`language`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.translation.protocol.TranslationResponseVerbose.language)

The language of the input audio.

###

`segments = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.translation.protocol.TranslationResponseVerbose.segments)

Segments of the translated text and their corresponding details.

###

`text`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.translation.protocol.TranslationResponseVerbose.text)

The translated text.

###

`words = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.translation.protocol.TranslationResponseVerbose.words)

Extracted words and their corresponding timestamps.

##

`TranslationSegment`

[¶](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.translation.protocol.TranslationSegment)

Bases: `OpenAIBaseModel`


Attributes:

-
([avg_logprob](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.translation.protocol.TranslationSegment.avg_logprob)

) –[float](https://docs.python.org/3/builtins/functions.html#float)Average logprob of the segment.

-
([compression_ratio](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.translation.protocol.TranslationSegment.compression_ratio)

) –[float](https://docs.python.org/3/builtins/functions.html#float)Compression ratio of the segment.

-
([end](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.translation.protocol.TranslationSegment.end)

) –[float](https://docs.python.org/3/builtins/functions.html#float)End time of the segment in seconds.

-
([id](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.translation.protocol.TranslationSegment.id)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Unique identifier of the segment.

-
([no_speech_prob](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.translation.protocol.TranslationSegment.no_speech_prob)

) –[float](https://docs.python.org/3/builtins/functions.html#float)| NoneProbability of no speech in the segment.

-
([seek](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.translation.protocol.TranslationSegment.seek)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Seek offset of the segment.

-
([start](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.translation.protocol.TranslationSegment.start)

) –[float](https://docs.python.org/3/builtins/functions.html#float)Start time of the segment in seconds.

-
([temperature](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.translation.protocol.TranslationSegment.temperature)

) –[float](https://docs.python.org/3/builtins/functions.html#float)Temperature parameter used for generating the segment.

-
([text](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.translation.protocol.TranslationSegment.text)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)Text content of the segment.

-
([tokens](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.translation.protocol.TranslationSegment.tokens)

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)]Array of token IDs for the text content.


## Source code in `vllm/entrypoints/speech_to_text/translation/protocol.py`


###

`avg_logprob`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.translation.protocol.TranslationSegment.avg_logprob)

Average logprob of the segment.

If the value is lower than -1, consider the logprobs failed.

###

`compression_ratio`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.translation.protocol.TranslationSegment.compression_ratio)

Compression ratio of the segment.

If the value is greater than 2.4, consider the compression failed.

###

`end`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.translation.protocol.TranslationSegment.end)

End time of the segment in seconds.

###

`id`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.translation.protocol.TranslationSegment.id)

Unique identifier of the segment.

###

`no_speech_prob = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.translation.protocol.TranslationSegment.no_speech_prob)

Probability of no speech in the segment.

If the value is higher than 1.0 and the `avg_logprob`

is below -1, consider this segment silent.

###

`seek`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.translation.protocol.TranslationSegment.seek)

Seek offset of the segment.

###

`start`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.translation.protocol.TranslationSegment.start)

Start time of the segment in seconds.

###

`temperature`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.translation.protocol.TranslationSegment.temperature)

Temperature parameter used for generating the segment.

###

`text`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.translation.protocol.TranslationSegment.text)

Text content of the segment.

###

`tokens`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.translation.protocol.TranslationSegment.tokens)

Array of token IDs for the text content.