source: https://docs.vllm.ai/en/latest/api/vllm/entrypoints/speech_to_text/base/utils/
lastmod: 2026-09-23

#

`vllm.entrypoints.speech_to_text.base.utils`

[¶](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.base.utils)

Shared utilities for speech-to-text API routes.

Functions:

-
–[read_upload_with_limit](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.base.utils.read_upload_with_limit)Read an uploaded file enforcing a size limit

*before*full

##

`read_upload_with_limit(file, max_size_mb=None)`

`async`

[¶](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.base.utils.read_upload_with_limit)

Read an uploaded file enforcing a size limit *before* full materialization.

The function first checks the Content-Length header (`file.size`

) when available. Regardless, it then performs a chunked read that stops as soon as the accumulated bytes exceed the limit, ensuring that an oversized upload never fully materializes in memory.

Parameters:

-

(`file`

[¶](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.base.utils.read_upload_with_limit(file))`UploadFile`

) –The FastAPI/Starlette

`UploadFile`

object. -

(`max_size_mb`

[¶](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.base.utils.read_upload_with_limit(max_size_mb))

, default:[float](https://docs.python.org/3/builtins/functions.html#float)| None`None`

) –Maximum allowed compressed file size in megabytes. Defaults to

`envs.VLLM_MAX_AUDIO_CLIP_FILESIZE_MB`

.

Returns:

-

–[bytes](https://docs.python.org/3/builtins/stdtypes.html#bytes)The file content as

`bytes`

.

Raises:

-

–[VLLMValidationError](https://docs.vllm.ai/exceptions/#vllm.exceptions.VLLMValidationError)If the file exceeds the configured size limit.