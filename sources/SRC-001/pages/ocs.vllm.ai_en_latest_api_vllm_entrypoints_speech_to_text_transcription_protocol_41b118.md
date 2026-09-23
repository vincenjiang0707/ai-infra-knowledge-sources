source: https://docs.vllm.ai/en/latest/api/vllm/entrypoints/speech_to_text/transcription/protocol/
lastmod: 2026-09-23

#

`vllm.entrypoints.speech_to_text.transcription.protocol`

[¶](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.transcription.protocol)

Classes:

-
–[TranscriptionDiarizedSegment](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.transcription.protocol.TranscriptionDiarizedSegment)A speaker-attributed transcription segment.

-
–[TranscriptionRequest](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.transcription.protocol.TranscriptionRequest) -
–[TranscriptionResponse](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.transcription.protocol.TranscriptionResponse) -
–[TranscriptionResponseDiarized](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.transcription.protocol.TranscriptionResponseDiarized)OpenAI-compatible diarized transcription response.

-
–[TranscriptionResponseVerbose](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.transcription.protocol.TranscriptionResponseVerbose) -
–[TranscriptionSegment](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.transcription.protocol.TranscriptionSegment) -
–[TranscriptionWord](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.transcription.protocol.TranscriptionWord)

##

`TranscriptionDiarizedSegment`

[¶](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.transcription.protocol.TranscriptionDiarizedSegment)

Bases: `OpenAIBaseModel`


A speaker-attributed transcription segment.

## Source code in `vllm/entrypoints/speech_to_text/transcription/protocol.py`


##

`TranscriptionRequest`

[¶](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.transcription.protocol.TranscriptionRequest)

Bases: `OpenAIBaseModel`


Attributes:

-
([file](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.transcription.protocol.TranscriptionRequest.file)`UploadFile`

) –The audio file object (not file name) to transcribe, in one of these

-
([frequency_penalty](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.transcription.protocol.TranscriptionRequest.frequency_penalty)

) –[float](https://docs.python.org/3/builtins/functions.html#float)| NoneThe frequency penalty to use for sampling.

-
([hotwords](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.transcription.protocol.TranscriptionRequest.hotwords)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)| Nonehotwords refers to a list of important words or phrases that the model

-
([include_stop_str_in_output](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.transcription.protocol.TranscriptionRequest.include_stop_str_in_output)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Whether to include the stop strings in output text.

-
([language](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.transcription.protocol.TranscriptionRequest.language)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)| NoneThe language of the input audio.

-
([length_penalty](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.transcription.protocol.TranscriptionRequest.length_penalty)

) –[float](https://docs.python.org/3/builtins/functions.html#float)Length penalty to be used for beam search.

-
([max_completion_tokens](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.transcription.protocol.TranscriptionRequest.max_completion_tokens)

) –[int](https://docs.python.org/3/builtins/functions.html#int)| NoneThe maximum number of tokens to generate.

-
([min_p](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.transcription.protocol.TranscriptionRequest.min_p)

) –[float](https://docs.python.org/3/builtins/functions.html#float)| NoneFilters out tokens with a probability lower than

`min_p`

, ensuring a -
([model](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.transcription.protocol.TranscriptionRequest.model)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)| NoneID of the model to use.

-
([n](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.transcription.protocol.TranscriptionRequest.n)

) –[int](https://docs.python.org/3/builtins/functions.html#int)The number of beams to be used in beam search.

-
([presence_penalty](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.transcription.protocol.TranscriptionRequest.presence_penalty)

) –[float](https://docs.python.org/3/builtins/functions.html#float)| NoneThe presence penalty to use for sampling.

-
([prompt](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.transcription.protocol.TranscriptionRequest.prompt)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)An optional text to guide the model's style or continue a previous audio

-
([repetition_penalty](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.transcription.protocol.TranscriptionRequest.repetition_penalty)

) –[float](https://docs.python.org/3/builtins/functions.html#float)| NoneThe repetition penalty to use for sampling.

-
([response_format](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.transcription.protocol.TranscriptionRequest.response_format)`TranscriptionResponseFormat`

) –The format of the output, in one of these options:

`json`

,`text`

,`srt`

, -
([seed](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.transcription.protocol.TranscriptionRequest.seed)

) –[int](https://docs.python.org/3/builtins/functions.html#int)| NoneThe seed to use for sampling.

-
([stream](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.transcription.protocol.TranscriptionRequest.stream)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)| NoneWhen set, it will enable output to be streamed in a similar fashion

-
([temperature](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.transcription.protocol.TranscriptionRequest.temperature)

) –[float](https://docs.python.org/3/builtins/functions.html#float)The sampling temperature, between 0 and 1.

-
([timestamp_granularities](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.transcription.protocol.TranscriptionRequest.timestamp_granularities)

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['word', 'segment']]The timestamp granularities to populate for this transcription.

-
([to_language](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.transcription.protocol.TranscriptionRequest.to_language)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)| NoneThe language of the output audio we transcribe to.

-
([top_k](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.transcription.protocol.TranscriptionRequest.top_k)

) –[int](https://docs.python.org/3/builtins/functions.html#int)| NoneLimits sampling to the

`k`

most probable tokens at each step. -
([top_p](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.transcription.protocol.TranscriptionRequest.top_p)

) –[float](https://docs.python.org/3/builtins/functions.html#float)| NoneEnables nucleus (top-p) sampling, where tokens are selected from the

-
([use_beam_search](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.transcription.protocol.TranscriptionRequest.use_beam_search)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Whether or not beam search should be used.


## Source code in `vllm/entrypoints/speech_to_text/transcription/protocol.py`


|
|

###

`file`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.transcription.protocol.TranscriptionRequest.file)

The audio file object (not file name) to transcribe, in one of these formats: flac, mp3, mp4, mpeg, mpga, m4a, ogg, wav, or webm.

###

`frequency_penalty = 0.0`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.transcription.protocol.TranscriptionRequest.frequency_penalty)

The frequency penalty to use for sampling.

###

`hotwords = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.transcription.protocol.TranscriptionRequest.hotwords)

hotwords refers to a list of important words or phrases that the model should pay extra attention to during transcription.

###

`include_stop_str_in_output = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.transcription.protocol.TranscriptionRequest.include_stop_str_in_output)

Whether to include the stop strings in output text.

###

`language = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.transcription.protocol.TranscriptionRequest.language)

The language of the input audio.

Supplying the input language in [ISO-639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) format will improve accuracy and latency.

###

`length_penalty = 1.0`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.transcription.protocol.TranscriptionRequest.length_penalty)

Length penalty to be used for beam search.

###

`max_completion_tokens = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.transcription.protocol.TranscriptionRequest.max_completion_tokens)

The maximum number of tokens to generate.

###

`min_p = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.transcription.protocol.TranscriptionRequest.min_p)

Filters out tokens with a probability lower than `min_p`

, ensuring a minimum likelihood threshold during sampling.

###

`model = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.transcription.protocol.TranscriptionRequest.model)

ID of the model to use.

###

`n = 1`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.transcription.protocol.TranscriptionRequest.n)

The number of beams to be used in beam search.

###

`presence_penalty = 0.0`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.transcription.protocol.TranscriptionRequest.presence_penalty)

The presence penalty to use for sampling.

###

`prompt = Field(default='')`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.transcription.protocol.TranscriptionRequest.prompt)

An optional text to guide the model's style or continue a previous audio segment.

The [prompt](https://platform.openai.com/docs/guides/speech-to-text#prompting) should match the audio language.

###

`repetition_penalty = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.transcription.protocol.TranscriptionRequest.repetition_penalty)

The repetition penalty to use for sampling.

###

`response_format = Field(default='json')`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.transcription.protocol.TranscriptionRequest.response_format)

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

[¶](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.transcription.protocol.TranscriptionRequest.seed)

The seed to use for sampling.

###

`stream = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.transcription.protocol.TranscriptionRequest.stream)

When set, it will enable output to be streamed in a similar fashion as the Chat Completion endpoint.

###

`temperature = Field(default=0.0)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.transcription.protocol.TranscriptionRequest.temperature)

The sampling temperature, between 0 and 1.

Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused / deterministic. If set to 0, the model will use [log probability](https://en.wikipedia.org/wiki/Log_probability) to automatically increase the temperature until certain thresholds are hit.

###

`timestamp_granularities = Field(alias='timestamp_granularities[]', default=[])`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.transcription.protocol.TranscriptionRequest.timestamp_granularities)

The timestamp granularities to populate for this transcription.

`response_format`

must be set `verbose_json`

to use timestamp granularities. Either or both of these options are supported: `word`

, or `segment`

. Note: There is no additional latency for segment timestamps, but generating word timestamps incurs additional latency.

###

`to_language = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.transcription.protocol.TranscriptionRequest.to_language)

The language of the output audio we transcribe to.

Please note that this is not currently used by supported models at this time, but it is a placeholder for future use, matching translation api.

###

`top_k = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.transcription.protocol.TranscriptionRequest.top_k)

Limits sampling to the `k`

most probable tokens at each step.

###

`top_p = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.transcription.protocol.TranscriptionRequest.top_p)

Enables nucleus (top-p) sampling, where tokens are selected from the smallest possible set whose cumulative probability exceeds `p`

.

###

`use_beam_search = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.transcription.protocol.TranscriptionRequest.use_beam_search)

Whether or not beam search should be used.

##

`TranscriptionResponse`

[¶](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.transcription.protocol.TranscriptionResponse)

Bases: `OpenAIBaseModel`


Attributes:

## Source code in `vllm/entrypoints/speech_to_text/transcription/protocol.py`


###

`text`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.transcription.protocol.TranscriptionResponse.text)

The transcribed text.

##

`TranscriptionResponseDiarized`

[¶](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.transcription.protocol.TranscriptionResponseDiarized)

Bases: `OpenAIBaseModel`


OpenAI-compatible diarized transcription response.

## Source code in `vllm/entrypoints/speech_to_text/transcription/protocol.py`


##

`TranscriptionResponseVerbose`

[¶](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.transcription.protocol.TranscriptionResponseVerbose)

Bases: `OpenAIBaseModel`


Attributes:

-
([duration](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.transcription.protocol.TranscriptionResponseVerbose.duration)

) –[float](https://docs.python.org/3/builtins/functions.html#float)The duration of the input audio.

-
([language](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.transcription.protocol.TranscriptionResponseVerbose.language)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)The language of the input audio.

-
([segments](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.transcription.protocol.TranscriptionResponseVerbose.segments)

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[TranscriptionSegment](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.transcription.protocol.TranscriptionSegment)] | NoneSegments of the transcribed text and their corresponding details.

-
([text](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.transcription.protocol.TranscriptionResponseVerbose.text)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)The transcribed text.

-
([words](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.transcription.protocol.TranscriptionResponseVerbose.words)

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[TranscriptionWord](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.transcription.protocol.TranscriptionWord)] | NoneExtracted words and their corresponding timestamps.


## Source code in `vllm/entrypoints/speech_to_text/transcription/protocol.py`


###

`duration`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.transcription.protocol.TranscriptionResponseVerbose.duration)

The duration of the input audio.

###

`language`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.transcription.protocol.TranscriptionResponseVerbose.language)

The language of the input audio.

###

`segments = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.transcription.protocol.TranscriptionResponseVerbose.segments)

Segments of the transcribed text and their corresponding details.

###

`text`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.transcription.protocol.TranscriptionResponseVerbose.text)

The transcribed text.

###

`words = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.transcription.protocol.TranscriptionResponseVerbose.words)

Extracted words and their corresponding timestamps.

##

`TranscriptionSegment`

[¶](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.transcription.protocol.TranscriptionSegment)

Bases: `OpenAIBaseModel`


Attributes:

-
([avg_logprob](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.transcription.protocol.TranscriptionSegment.avg_logprob)

) –[float](https://docs.python.org/3/builtins/functions.html#float)Average logprob of the segment.

-
([compression_ratio](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.transcription.protocol.TranscriptionSegment.compression_ratio)

) –[float](https://docs.python.org/3/builtins/functions.html#float)Compression ratio of the segment.

-
([end](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.transcription.protocol.TranscriptionSegment.end)

) –[float](https://docs.python.org/3/builtins/functions.html#float)End time of the segment in seconds.

-
([id](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.transcription.protocol.TranscriptionSegment.id)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Unique identifier of the segment.

-
([no_speech_prob](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.transcription.protocol.TranscriptionSegment.no_speech_prob)

) –[float](https://docs.python.org/3/builtins/functions.html#float)| NoneProbability of no speech in the segment.

-
([seek](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.transcription.protocol.TranscriptionSegment.seek)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Seek offset of the segment.

-
([start](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.transcription.protocol.TranscriptionSegment.start)

) –[float](https://docs.python.org/3/builtins/functions.html#float)Start time of the segment in seconds.

-
([temperature](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.transcription.protocol.TranscriptionSegment.temperature)

) –[float](https://docs.python.org/3/builtins/functions.html#float)Temperature parameter used for generating the segment.

-
([text](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.transcription.protocol.TranscriptionSegment.text)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)Text content of the segment.

-
([tokens](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.transcription.protocol.TranscriptionSegment.tokens)

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)]Array of token IDs for the text content.


## Source code in `vllm/entrypoints/speech_to_text/transcription/protocol.py`


###

`avg_logprob`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.transcription.protocol.TranscriptionSegment.avg_logprob)

Average logprob of the segment.

If the value is lower than -1, consider the logprobs failed.

###

`compression_ratio`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.transcription.protocol.TranscriptionSegment.compression_ratio)

Compression ratio of the segment.

If the value is greater than 2.4, consider the compression failed.

###

`end`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.transcription.protocol.TranscriptionSegment.end)

End time of the segment in seconds.

###

`id`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.transcription.protocol.TranscriptionSegment.id)

Unique identifier of the segment.

###

`no_speech_prob = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.transcription.protocol.TranscriptionSegment.no_speech_prob)

Probability of no speech in the segment.

If the value is higher than 1.0 and the `avg_logprob`

is below -1, consider this segment silent.

###

`seek`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.transcription.protocol.TranscriptionSegment.seek)

Seek offset of the segment.

###

`start`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.transcription.protocol.TranscriptionSegment.start)

Start time of the segment in seconds.

###

`temperature`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.transcription.protocol.TranscriptionSegment.temperature)

Temperature parameter used for generating the segment.

###

`text`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.transcription.protocol.TranscriptionSegment.text)

Text content of the segment.

###

`tokens`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.transcription.protocol.TranscriptionSegment.tokens)

Array of token IDs for the text content.