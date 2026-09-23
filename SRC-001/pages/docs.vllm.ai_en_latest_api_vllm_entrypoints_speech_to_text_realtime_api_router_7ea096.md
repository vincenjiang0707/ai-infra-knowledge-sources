source: https://docs.vllm.ai/en/latest/api/vllm/entrypoints/speech_to_text/realtime/api_router/
lastmod: 2026-09-23

#

`vllm.entrypoints.speech_to_text.realtime.api_router`

[¶](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.realtime.api_router)

Functions:

-
–[realtime_endpoint](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.realtime.api_router.realtime_endpoint)WebSocket endpoint for realtime audio transcription.


##

`realtime_endpoint(websocket)`

`async`

[¶](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.realtime.api_router.realtime_endpoint)

WebSocket endpoint for realtime audio transcription.

Protocol: 1. Client connects to ws://host/v1/realtime 2. Server sends session.created event 3. Client optionally sends session.update with model/params 4. Client sends input_audio_buffer.commit when ready 5. Client sends input_audio_buffer.append events with base64 PCM16 chunks 6. Server processes and sends transcription.delta events 7. Server sends transcription.done with final text + usage 8. Repeat from step 5 for next utterance 9. Optionally, client sends input_audio_buffer.commit with final=True to signal audio input is finished. Useful when streaming audio files

Audio format: PCM16, 16kHz, mono, base64-encoded