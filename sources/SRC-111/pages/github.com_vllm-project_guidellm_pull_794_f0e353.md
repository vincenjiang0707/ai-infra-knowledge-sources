source: https://github.com/vllm-project/guidellm/pull/794

# Infer audio encoding format from source instead of defaulting to MP3 - #794

Merged

Merged

## Conversation

Generated-by: Cursor AI Claude Opus 4.6 Signed-off-by: Jared O'Connell <joconnel@redhat.com>

[jaredoconnell](https://github.com/jaredoconnell)

[force-pushed](https://github.com/vllm-project/guidellm/compare/0f43c0e0b0f022bb84e05e6d807ef310940b1919..6cc6e9fa72178752632956b5b193a4107c3aee98)the fix/audio-formats branch from

[to](https://github.com/vllm-project/guidellm/commit/0f43c0e0b0f022bb84e05e6d807ef310940b1919)

`0f43c0e`


`6cc6e9f`

[Compare](https://github.com/vllm-project/guidellm/compare/0f43c0e0b0f022bb84e05e6d807ef310940b1919..6cc6e9fa72178752632956b5b193a4107c3aee98)

June 12, 2026 22:46


**previously approved these changes**

[dbutenhof](https://github.com/dbutenhof)Jun 15, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)
Collaborator


There was a problem hiding this comment.

A minor comment and a minor question ... but looks OK.

[src/guidellm/utils/audio.py](https://github.com/vllm-project/guidellm/pull/794/files/6cc6e9fa72178752632956b5b193a4107c3aee98#diff-3dbf8fd7d753e8e0495b1e5111e5f9fb7e82040a5f92666eb1a72d679d3bfd32)

[src/guidellm/utils/audio.py](https://github.com/vllm-project/guidellm/pull/794/files/6cc6e9fa72178752632956b5b193a4107c3aee98#diff-3dbf8fd7d753e8e0495b1e5111e5f9fb7e82040a5f92666eb1a72d679d3bfd32)Outdated


**requested changes**

[sjmonson](https://github.com/sjmonson)Jun 15, 2026

[src/guidellm/backends/vllm_python/vllm.py](https://github.com/vllm-project/guidellm/pull/794/files/6cc6e9fa72178752632956b5b193a4107c3aee98#diff-6469481616de32d01585d227edd34721157d75fb5b6b89c628e0269430dd91f0)

[src/guidellm/utils/audio.py](https://github.com/vllm-project/guidellm/pull/794/files/6cc6e9fa72178752632956b5b193a4107c3aee98#diff-3dbf8fd7d753e8e0495b1e5111e5f9fb7e82040a5f92666eb1a72d679d3bfd32)Outdated

[src/guidellm/utils/audio.py](https://github.com/vllm-project/guidellm/pull/794/files/6cc6e9fa72178752632956b5b193a4107c3aee98#diff-3dbf8fd7d753e8e0495b1e5111e5f9fb7e82040a5f92666eb1a72d679d3bfd32)Outdated

[jaredoconnell](https://github.com/jaredoconnell)

[force-pushed](https://github.com/vllm-project/guidellm/compare/fd02451075d76bc1a8b17f1ba9d716d7b09d5591..13745bc24bb5fe7a25daeebd13f9f906261ec6e5)the fix/audio-formats branch from

[to](https://github.com/vllm-project/guidellm/commit/fd02451075d76bc1a8b17f1ba9d716d7b09d5591)

`fd02451`


`13745bc`

[Compare](https://github.com/vllm-project/guidellm/compare/fd02451075d76bc1a8b17f1ba9d716d7b09d5591..13745bc24bb5fe7a25daeebd13f9f906261ec6e5)

June 16, 2026 03:51


**reviewed**

[dbutenhof](https://github.com/dbutenhof)Jun 16, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)
Collaborator


There was a problem hiding this comment.

Looks good, aside from

2 files would be reformatted, 254 files already formatted


Signed-off-by: Jared O'Connell <joconnel@redhat.com>

[jaredoconnell](https://github.com/jaredoconnell)

[force-pushed](https://github.com/vllm-project/guidellm/compare/13745bc24bb5fe7a25daeebd13f9f906261ec6e5..09d77d0bd91ad68ad5424b6c3a46554cf0f20c8b)the fix/audio-formats branch from

[to](https://github.com/vllm-project/guidellm/commit/13745bc24bb5fe7a25daeebd13f9f906261ec6e5)

`13745bc`


`09d77d0`

[Compare](https://github.com/vllm-project/guidellm/compare/13745bc24bb5fe7a25daeebd13f9f906261ec6e5..09d77d0bd91ad68ad5424b6c3a46554cf0f20c8b)

June 16, 2026 13:54


**approved these changes**

[sjmonson](https://github.com/sjmonson)Jun 16, 2026


**approved these changes**

[dbutenhof](https://github.com/dbutenhof)Jun 16, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)
Collaborator


There was a problem hiding this comment.

Hopefully the CI will be happy -- if it is, let's ship it.

Contributor

## Merge Queue Status
This pull request spent ## Required conditions to merge
|

[SkiHatDuckie](https://github.com/SkiHatDuckie)pushed a commit to SkiHatDuckie/guidellm that referenced this pull request

Jun 23, 2026

[…llm-project#794]) ## Summary Uses the source's audio format rather than defaulting to MP3 ## Details - If no format is provided by the user, and it cannot be inferred, it defaults to WAV and warns the user. - Simply uses the format read from the dataset if none is provided. - Includes a fix for a missing super call in the response handler. ## Test Plan Make sure you install vLLM with the audio features. You can run this with multiple datasets. Some options include: ```bash guidellm benchmark run --target "http://localhost:8000" --request-type /v1/audio/transcriptions --profile kind=synchronous --max-requests 10 --data '{"kind": "huggingface", "source": "google/fleurs", "load_kwargs": {"name": "en_us", "split": "test"}}' --data-column-mapper '{"column_mappings": {"audio_column": "audio"}}' --disable-progress ``` ```bash guidellm benchmark run --target "http://localhost:8000" --request-type /v1/audio/transcriptions --profile kind=synchronous --max-requests 10 --data '{"kind": "huggingface", "source": "openslr/librispeech_asr", "load_kwargs": {"name": "clean", "split": "test"}}' --data-column-mapper '{"column_mappings": {"audio_column": "audio"}}' --disable-progress ``` To explicitly use MP3 like it used to, do: ```bash guidellm benchmark run \ --target "http://localhost:8000" \ --request-type /v1/audio/transcriptions \ --profile kind=synchronous \ --max-requests 10 \ --data '{"kind": "huggingface", "source": "openslr/librispeech_asr", "load_kwargs": {"name": "clean", "split": "test"}}' \ --data-column-mapper '{"column_mappings": {"audio_column": "audio"}}' \ --data-preprocessors '{"kind": "encode_media", "audio_kwargs": {"audio_format": "mp3"}}' \ --disable-progress ``` ## Related Issues - Resolves[vllm-project#623]--- - [x] "I certify that all code in this PR is my own, except as noted below." ## Use of AI - [x] Includes code generated or substantially modified by an AI agent - [x] Includes tests generated or substantially modified by an AI agent > NOTE: the `Generated-by` or `Assisted-by` trailers should be used in git commit messages when code or tests were generated or substantially modified by an AI agent, as described in the project's [`DEVELOPING.md`]([https://github.com/vllm-project/guidellm/blob/main/DEVELOPING.md]) file. --- # git log commit[Author: Jared O'Connell <joconnel@redhat.com> Date: Thu Jun 11 15:00:08 2026 -0400 Infer audio encoding format from source instead of defaulting to MP3 Generated-by: Cursor AI Claude Opus 4.6 Signed-off-by: Jared O'Connell <joconnel@redhat.com> commit]6cc6e9f[Author: Jared O'Connell <joconnel@redhat.com> Date: Mon Jun 15 19:13:30 2026 -0400 Address review feedback Signed-off-by: Jared O'Connell <joconnel@redhat.com> --------- Generated-by: Cursor AI Claude Opus 4.6 Signed-off-by: Jared O'Connell <joconnel@redhat.com>]09d77d0

[SkiHatDuckie](https://github.com/SkiHatDuckie)pushed a commit to SkiHatDuckie/guidellm that referenced this pull request

Jun 24, 2026

[…llm-project#794]) ## Summary Uses the source's audio format rather than defaulting to MP3 ## Details - If no format is provided by the user, and it cannot be inferred, it defaults to WAV and warns the user. - Simply uses the format read from the dataset if none is provided. - Includes a fix for a missing super call in the response handler. ## Test Plan Make sure you install vLLM with the audio features. You can run this with multiple datasets. Some options include: ```bash guidellm benchmark run --target "http://localhost:8000" --request-type /v1/audio/transcriptions --profile kind=synchronous --max-requests 10 --data '{"kind": "huggingface", "source": "google/fleurs", "load_kwargs": {"name": "en_us", "split": "test"}}' --data-column-mapper '{"column_mappings": {"audio_column": "audio"}}' --disable-progress ``` ```bash guidellm benchmark run --target "http://localhost:8000" --request-type /v1/audio/transcriptions --profile kind=synchronous --max-requests 10 --data '{"kind": "huggingface", "source": "openslr/librispeech_asr", "load_kwargs": {"name": "clean", "split": "test"}}' --data-column-mapper '{"column_mappings": {"audio_column": "audio"}}' --disable-progress ``` To explicitly use MP3 like it used to, do: ```bash guidellm benchmark run \ --target "http://localhost:8000" \ --request-type /v1/audio/transcriptions \ --profile kind=synchronous \ --max-requests 10 \ --data '{"kind": "huggingface", "source": "openslr/librispeech_asr", "load_kwargs": {"name": "clean", "split": "test"}}' \ --data-column-mapper '{"column_mappings": {"audio_column": "audio"}}' \ --data-preprocessors '{"kind": "encode_media", "audio_kwargs": {"audio_format": "mp3"}}' \ --disable-progress ``` ## Related Issues - Resolves[vllm-project#623]--- - [x] "I certify that all code in this PR is my own, except as noted below." ## Use of AI - [x] Includes code generated or substantially modified by an AI agent - [x] Includes tests generated or substantially modified by an AI agent > NOTE: the `Generated-by` or `Assisted-by` trailers should be used in git commit messages when code or tests were generated or substantially modified by an AI agent, as described in the project's [`DEVELOPING.md`]([https://github.com/vllm-project/guidellm/blob/main/DEVELOPING.md]) file. --- # git log commit[Author: Jared O'Connell <joconnel@redhat.com> Date: Thu Jun 11 15:00:08 2026 -0400 Infer audio encoding format from source instead of defaulting to MP3 Generated-by: Cursor AI Claude Opus 4.6 Signed-off-by: Jared O'Connell <joconnel@redhat.com> commit]6cc6e9f[Author: Jared O'Connell <joconnel@redhat.com> Date: Mon Jun 15 19:13:30 2026 -0400 Address review feedback Signed-off-by: Jared O'Connell <joconnel@redhat.com> --------- Generated-by: Cursor AI Claude Opus 4.6 Signed-off-by: Jared O'Connell <joconnel@redhat.com>]09d77d0

[SkiHatDuckie](https://github.com/SkiHatDuckie)pushed a commit to SkiHatDuckie/guidellm that referenced this pull request

Jul 6, 2026

[…llm-project#794]) ## Summary Uses the source's audio format rather than defaulting to MP3 ## Details - If no format is provided by the user, and it cannot be inferred, it defaults to WAV and warns the user. - Simply uses the format read from the dataset if none is provided. - Includes a fix for a missing super call in the response handler. ## Test Plan Make sure you install vLLM with the audio features. You can run this with multiple datasets. Some options include: ```bash guidellm benchmark run --target "http://localhost:8000" --request-type /v1/audio/transcriptions --profile kind=synchronous --max-requests 10 --data '{"kind": "huggingface", "source": "google/fleurs", "load_kwargs": {"name": "en_us", "split": "test"}}' --data-column-mapper '{"column_mappings": {"audio_column": "audio"}}' --disable-progress ``` ```bash guidellm benchmark run --target "http://localhost:8000" --request-type /v1/audio/transcriptions --profile kind=synchronous --max-requests 10 --data '{"kind": "huggingface", "source": "openslr/librispeech_asr", "load_kwargs": {"name": "clean", "split": "test"}}' --data-column-mapper '{"column_mappings": {"audio_column": "audio"}}' --disable-progress ``` To explicitly use MP3 like it used to, do: ```bash guidellm benchmark run \ --target "http://localhost:8000" \ --request-type /v1/audio/transcriptions \ --profile kind=synchronous \ --max-requests 10 \ --data '{"kind": "huggingface", "source": "openslr/librispeech_asr", "load_kwargs": {"name": "clean", "split": "test"}}' \ --data-column-mapper '{"column_mappings": {"audio_column": "audio"}}' \ --data-preprocessors '{"kind": "encode_media", "audio_kwargs": {"audio_format": "mp3"}}' \ --disable-progress ``` ## Related Issues - Resolves[vllm-project#623]--- - [x] "I certify that all code in this PR is my own, except as noted below." ## Use of AI - [x] Includes code generated or substantially modified by an AI agent - [x] Includes tests generated or substantially modified by an AI agent > NOTE: the `Generated-by` or `Assisted-by` trailers should be used in git commit messages when code or tests were generated or substantially modified by an AI agent, as described in the project's [`DEVELOPING.md`]([https://github.com/vllm-project/guidellm/blob/main/DEVELOPING.md]) file. --- # git log commit[Author: Jared O'Connell <joconnel@redhat.com> Date: Thu Jun 11 15:00:08 2026 -0400 Infer audio encoding format from source instead of defaulting to MP3 Generated-by: Cursor AI Claude Opus 4.6 Signed-off-by: Jared O'Connell <joconnel@redhat.com> commit]6cc6e9f[Author: Jared O'Connell <joconnel@redhat.com> Date: Mon Jun 15 19:13:30 2026 -0400 Address review feedback Signed-off-by: Jared O'Connell <joconnel@redhat.com> --------- Generated-by: Cursor AI Claude Opus 4.6 Signed-off-by: Jared O'Connell <joconnel@redhat.com>]09d77d0

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

## Summary

Uses the source's audio format rather than defaulting to MP3

## Details

## Test Plan

Make sure you install vLLM with the audio features.

You can run this with multiple datasets. Some options include:

To explicitly use MP3 like it used to, do:

## Related Issues

## Use of AI

## git log

commit

6cc6e9fAuthor: Jared O'Connell joconnel@redhat.com

Date: Thu Jun 11 15:00:08 2026 -0400

commit

09d77d0Author: Jared O'Connell joconnel@redhat.com

Date: Mon Jun 15 19:13:30 2026 -0400

Generated-by: Cursor AI Claude Opus 4.6

Signed-off-by: Jared O'Connell joconnel@redhat.com