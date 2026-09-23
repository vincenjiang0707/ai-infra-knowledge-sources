source: https://docs.vllm.ai/en/latest/api/vllm/entrypoints/speech_to_text/realtime/protocol/
lastmod: 2026-09-23

#

`vllm.entrypoints.speech_to_text.realtime.protocol`

[¶](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.realtime.protocol)

Classes:

-
–[ErrorEvent](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.realtime.protocol.ErrorEvent)Error notification.

-
–[InputAudioBufferAppend](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.realtime.protocol.InputAudioBufferAppend)Append audio chunk to buffer.

-
–[InputAudioBufferCommit](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.realtime.protocol.InputAudioBufferCommit)Process accumulated audio buffer.

-
–[SessionCreated](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.realtime.protocol.SessionCreated)Connection established notification.

-
–[SessionUpdate](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.realtime.protocol.SessionUpdate)Configure session parameters.

-
–[TranscriptionDelta](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.realtime.protocol.TranscriptionDelta)Incremental transcription text.

-
–[TranscriptionDone](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.realtime.protocol.TranscriptionDone)Final transcription with usage stats.


##

`ErrorEvent`

[¶](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.realtime.protocol.ErrorEvent)

##

`InputAudioBufferAppend`

[¶](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.realtime.protocol.InputAudioBufferAppend)

Bases: `OpenAIBaseModel`


Append audio chunk to buffer.

## Source code in `vllm/entrypoints/speech_to_text/realtime/protocol.py`


##

`InputAudioBufferCommit`

[¶](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.realtime.protocol.InputAudioBufferCommit)

Bases: `OpenAIBaseModel`


Process accumulated audio buffer.

## Source code in `vllm/entrypoints/speech_to_text/realtime/protocol.py`


##

`SessionCreated`

[¶](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.realtime.protocol.SessionCreated)

Bases: `OpenAIBaseModel`


Connection established notification.

## Source code in `vllm/entrypoints/speech_to_text/realtime/protocol.py`


##

`SessionUpdate`

[¶](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.realtime.protocol.SessionUpdate)

##

`TranscriptionDelta`

[¶](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.realtime.protocol.TranscriptionDelta)

Bases: `OpenAIBaseModel`


Incremental transcription text.

## Source code in `vllm/entrypoints/speech_to_text/realtime/protocol.py`


##

`TranscriptionDone`

[¶](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.realtime.protocol.TranscriptionDone)

Bases: `OpenAIBaseModel`


Final transcription with usage stats.