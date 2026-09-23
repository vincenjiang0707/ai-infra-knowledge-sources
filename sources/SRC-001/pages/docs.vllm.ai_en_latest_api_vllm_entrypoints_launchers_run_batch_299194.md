source: https://docs.vllm.ai/en/latest/api/vllm/entrypoints/launchers/run_batch/
lastmod: 2026-09-23

#

`vllm.entrypoints.launchers.run_batch`

[¶](https://docs.vllm.ai#vllm.entrypoints.launchers.run_batch)

Classes:

-
–[BatchFrontendArgs](https://docs.vllm.ai#vllm.entrypoints.launchers.run_batch.BatchFrontendArgs)Arguments for the batch runner frontend.

-
–[BatchRequestInput](https://docs.vllm.ai#vllm.entrypoints.launchers.run_batch.BatchRequestInput)The per-line object of the batch input file.

-
–[BatchRequestOutput](https://docs.vllm.ai#vllm.entrypoints.launchers.run_batch.BatchRequestOutput)The per-line object of the batch output and error files

-
–[BatchTranscriptionRequest](https://docs.vllm.ai#vllm.entrypoints.launchers.run_batch.BatchTranscriptionRequest)Batch transcription request that uses file_url instead of file.

-
–[BatchTranslationRequest](https://docs.vllm.ai#vllm.entrypoints.launchers.run_batch.BatchTranslationRequest)Batch translation request that uses file_url instead of file.


Functions:

-
–[build_endpoint_registry](https://docs.vllm.ai#vllm.entrypoints.launchers.run_batch.build_endpoint_registry)Build the endpoint registry with all serving objects and handler configurations.

-
–[download_bytes_from_url](https://docs.vllm.ai#vllm.entrypoints.launchers.run_batch.download_bytes_from_url)Download data from a URL or decode from a data URL.

-
–[handle_endpoint_request](https://docs.vllm.ai#vllm.entrypoints.launchers.run_batch.handle_endpoint_request)Generic handler for endpoint requests.

-
–[make_transcription_wrapper](https://docs.vllm.ai#vllm.entrypoints.launchers.run_batch.make_transcription_wrapper)Factory function to create a wrapper for transcription/translation handlers.

-
–[upload_data](https://docs.vllm.ai#vllm.entrypoints.launchers.run_batch.upload_data)Upload a local file to a URL.

-
–[write_file](https://docs.vllm.ai#vllm.entrypoints.launchers.run_batch.write_file)Write batch_outputs to a file or upload to a URL.

-
–[write_local_file](https://docs.vllm.ai#vllm.entrypoints.launchers.run_batch.write_local_file)Write the responses to a local file.


##

`BatchFrontendArgs`

[¶](https://docs.vllm.ai#vllm.entrypoints.launchers.run_batch.BatchFrontendArgs)

Bases: [BaseFrontendArgs](https://docs.vllm.ai/cli_args/#vllm.entrypoints.launchers.cli_args.BaseFrontendArgs)

Arguments for the batch runner frontend.

Attributes:

-
([enable_metrics](https://docs.vllm.ai#vllm.entrypoints.launchers.run_batch.BatchFrontendArgs.enable_metrics)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Enable Prometheus metrics

-
([host](https://docs.vllm.ai#vllm.entrypoints.launchers.run_batch.BatchFrontendArgs.host)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)| NoneHost name for the Prometheus metrics server

-
([input_file](https://docs.vllm.ai#vllm.entrypoints.launchers.run_batch.BatchFrontendArgs.input_file)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)| NoneThe path or url to a single input file. Currently supports local file

-
([output_file](https://docs.vllm.ai#vllm.entrypoints.launchers.run_batch.BatchFrontendArgs.output_file)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)| NoneThe path or url to a single output file. Currently supports

-
([output_tmp_dir](https://docs.vllm.ai#vllm.entrypoints.launchers.run_batch.BatchFrontendArgs.output_tmp_dir)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)| NoneThe directory to store the output file before uploading it

-
([port](https://docs.vllm.ai#vllm.entrypoints.launchers.run_batch.BatchFrontendArgs.port)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Port number for the Prometheus metrics server

-
([url](https://docs.vllm.ai#vllm.entrypoints.launchers.run_batch.BatchFrontendArgs.url)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)[DEPRECATED] Host name for the Prometheus metrics server


## Source code in `vllm/entrypoints/launchers/run_batch.py`


###

`enable_metrics = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.launchers.run_batch.BatchFrontendArgs.enable_metrics)

Enable Prometheus metrics

###

`host = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.launchers.run_batch.BatchFrontendArgs.host)

Host name for the Prometheus metrics server (only needed if enable-metrics is set).

###

`input_file = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.launchers.run_batch.BatchFrontendArgs.input_file)

The path or url to a single input file. Currently supports local file paths, or the http protocol (http or https). If a URL is specified, the file should be available via HTTP GET.

###

`output_file = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.launchers.run_batch.BatchFrontendArgs.output_file)

The path or url to a single output file. Currently supports local file paths, or web (http or https) urls. If a URL is specified, the file should be available via HTTP PUT.

###

`output_tmp_dir = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.launchers.run_batch.BatchFrontendArgs.output_tmp_dir)

The directory to store the output file before uploading it to the output URL.

###

`port = 8000`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.launchers.run_batch.BatchFrontendArgs.port)

Port number for the Prometheus metrics server (only needed if enable-metrics is set).

###

`url = '0.0.0.0'`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.launchers.run_batch.BatchFrontendArgs.url)

[DEPRECATED] Host name for the Prometheus metrics server (only needed if enable-metrics is set). Use --host instead.

##

`BatchRequestInput`

[¶](https://docs.vllm.ai#vllm.entrypoints.launchers.run_batch.BatchRequestInput)

Bases: `OpenAIBaseModel`


The per-line object of the batch input file.

NOTE: Currently only the `/v1/chat/completions`

endpoint is supported.

## Source code in `vllm/entrypoints/launchers/run_batch.py`


##

`BatchRequestOutput`

[¶](https://docs.vllm.ai#vllm.entrypoints.launchers.run_batch.BatchRequestOutput)

Bases: `OpenAIBaseModel`


The per-line object of the batch output and error files

## Source code in `vllm/entrypoints/launchers/run_batch.py`


##

`BatchTranscriptionRequest`

[¶](https://docs.vllm.ai#vllm.entrypoints.launchers.run_batch.BatchTranscriptionRequest)

Bases: [TranscriptionRequest](https://docs.vllm.ai/speech_to_text/transcription/protocol/#vllm.entrypoints.speech_to_text.transcription.protocol.TranscriptionRequest)

Batch transcription request that uses file_url instead of file.

This class extends TranscriptionRequest but replaces the file field with file_url to support batch processing from audio files written in JSON format.

Methods:

-
–[validate_no_file](https://docs.vllm.ai#vllm.entrypoints.launchers.run_batch.BatchTranscriptionRequest.validate_no_file)Ensure file field is not provided in batch requests.


## Source code in `vllm/entrypoints/launchers/run_batch.py`


###

`validate_no_file(data)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.entrypoints.launchers.run_batch.BatchTranscriptionRequest.validate_no_file)

Ensure file field is not provided in batch requests.

## Source code in `vllm/entrypoints/launchers/run_batch.py`


##

`BatchTranslationRequest`

[¶](https://docs.vllm.ai#vllm.entrypoints.launchers.run_batch.BatchTranslationRequest)

Bases: [TranslationRequest](https://docs.vllm.ai/speech_to_text/translation/protocol/#vllm.entrypoints.speech_to_text.translation.protocol.TranslationRequest)

Batch translation request that uses file_url instead of file.

This class extends TranslationRequest but replaces the file field with file_url to support batch processing from audio files written in JSON format.

Methods:

-
–[validate_no_file](https://docs.vllm.ai#vllm.entrypoints.launchers.run_batch.BatchTranslationRequest.validate_no_file)Ensure file field is not provided in batch requests.


## Source code in `vllm/entrypoints/launchers/run_batch.py`


###

`validate_no_file(data)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.entrypoints.launchers.run_batch.BatchTranslationRequest.validate_no_file)

Ensure file field is not provided in batch requests.

## Source code in `vllm/entrypoints/launchers/run_batch.py`


##

`build_endpoint_registry(engine_client, args)`

`async`

[¶](https://docs.vllm.ai#vllm.entrypoints.launchers.run_batch.build_endpoint_registry)

Build the endpoint registry with all serving objects and handler configurations.

Parameters:

-

(`engine_client`

[¶](https://docs.vllm.ai#vllm.entrypoints.launchers.run_batch.build_endpoint_registry(engine_client))

) –[EngineClient](https://docs.vllm.ai/engine/protocol/#vllm.engine.protocol.EngineClient)The engine client

-

(`args`

[¶](https://docs.vllm.ai#vllm.entrypoints.launchers.run_batch.build_endpoint_registry(args))

) –[Namespace](https://docs.python.org/3/library/argparse.html#argparse.Namespace)Command line arguments


Returns:

## Source code in `vllm/entrypoints/launchers/run_batch.py`


|
|

##

`download_bytes_from_url(url, allowed_media_domains=None)`

`async`

[¶](https://docs.vllm.ai#vllm.entrypoints.launchers.run_batch.download_bytes_from_url)

Download data from a URL or decode from a data URL.

Parameters:

-

(`url`

[¶](https://docs.vllm.ai#vllm.entrypoints.launchers.run_batch.download_bytes_from_url(url))

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)Either an HTTP/HTTPS URL or a data URL (data:...;base64,...)

-

(`allowed_media_domains`

[¶](https://docs.vllm.ai#vllm.entrypoints.launchers.run_batch.download_bytes_from_url(allowed_media_domains))

, default:[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)] | None`None`

) –If set, only HTTP/HTTPS URLs whose hostname is in this list are permitted. data: URLs are not subject to this restriction.


Returns:

-

–[bytes](https://docs.python.org/3/builtins/stdtypes.html#bytes)Data as bytes


## Source code in `vllm/entrypoints/launchers/run_batch.py`


##

`handle_endpoint_request(request, tracker, url_matcher, handler_getter, wrapper_fn=None)`

[¶](https://docs.vllm.ai#vllm.entrypoints.launchers.run_batch.handle_endpoint_request)

Generic handler for endpoint requests.

Parameters:

-

(`request`

[¶](https://docs.vllm.ai#vllm.entrypoints.launchers.run_batch.handle_endpoint_request(request))

) –[BatchRequestInput](https://docs.vllm.ai#vllm.entrypoints.launchers.run_batch.BatchRequestInput)The batch request input

-

(`tracker`

[¶](https://docs.vllm.ai#vllm.entrypoints.launchers.run_batch.handle_endpoint_request(tracker))`BatchProgressTracker`

) –Progress tracker for the batch

-

(`url_matcher`

[¶](https://docs.vllm.ai#vllm.entrypoints.launchers.run_batch.handle_endpoint_request(url_matcher))

) –[Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[[str](https://docs.python.org/3/builtins/stdtypes.html#str)],[bool](https://docs.python.org/3/builtins/functions.html#bool)]Function that takes a URL and returns True if it matches

-

(`handler_getter`

[¶](https://docs.vllm.ai#vllm.entrypoints.launchers.run_batch.handle_endpoint_request(handler_getter))

) –[Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[],[Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)| None]Function that returns the handler function or None

-

(`wrapper_fn`

[¶](https://docs.vllm.ai#vllm.entrypoints.launchers.run_batch.handle_endpoint_request(wrapper_fn))`WrapperFn | None`

, default:`None`

) –Optional function to wrap the handler (e.g., for transcriptions)


Returns:

-

–[Awaitable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Awaitable)[[BatchRequestOutput](https://docs.vllm.ai#vllm.entrypoints.launchers.run_batch.BatchRequestOutput)] | NoneAwaitable[BatchRequestOutput] if the request was handled,

-

–[Awaitable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Awaitable)[[BatchRequestOutput](https://docs.vllm.ai#vllm.entrypoints.launchers.run_batch.BatchRequestOutput)] | NoneNone if URL didn't match


## Source code in `vllm/entrypoints/launchers/run_batch.py`


##

`make_transcription_wrapper(is_translation, allowed_media_domains=None)`

[¶](https://docs.vllm.ai#vllm.entrypoints.launchers.run_batch.make_transcription_wrapper)

Factory function to create a wrapper for transcription/translation handlers. The wrapper converts BatchTranscriptionRequest or BatchTranslationRequest to TranscriptionRequest or TranslationRequest and calls the appropriate handler.

Parameters:

-

(`is_translation`

[¶](https://docs.vllm.ai#vllm.entrypoints.launchers.run_batch.make_transcription_wrapper(is_translation))

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)If True, process as translation; otherwise process as transcription

-

(`allowed_media_domains`

[¶](https://docs.vllm.ai#vllm.entrypoints.launchers.run_batch.make_transcription_wrapper(allowed_media_domains))

, default:[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)] | None`None`

) –If set, only URLs from these domains are permitted for HTTP/HTTPS fetches.


Returns:

-
`WrapperFn`

–A function that takes a handler and returns a wrapped handler


## Source code in `vllm/entrypoints/launchers/run_batch.py`


##

`upload_data(output_url, data_or_file, from_file)`

`async`

[¶](https://docs.vllm.ai#vllm.entrypoints.launchers.run_batch.upload_data)

Upload a local file to a URL. output_url: The URL to upload the file to. data_or_file: Either the data to upload or the path to the file to upload. from_file: If True, data_or_file is the path to the file to upload.

## Source code in `vllm/entrypoints/launchers/run_batch.py`


##

`write_file(path_or_url, batch_outputs, output_tmp_dir)`

`async`

[¶](https://docs.vllm.ai#vllm.entrypoints.launchers.run_batch.write_file)

Write batch_outputs to a file or upload to a URL. path_or_url: The path or URL to write batch_outputs to. batch_outputs: The list of batch outputs to write. output_tmp_dir: The directory to store the output file before uploading it to the output URL.

## Source code in `vllm/entrypoints/launchers/run_batch.py`


##

`write_local_file(output_path, batch_outputs)`

`async`

[¶](https://docs.vllm.ai#vllm.entrypoints.launchers.run_batch.write_local_file)

Write the responses to a local file. output_path: The path to write the responses to. batch_outputs: The list of batch outputs to write.