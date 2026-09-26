source: https://github.com/vllm-project/guidellm/pull/713

# Realtime transcription endpoint - #713

[mergify[bot]](https://github.com/mergify[bot])merged 20 commits into

[mergify[bot]](https://github.com/mergify[bot]) merged 20 commits into

[mergify[bot]](https://github.com/mergify[bot])merged 20 commits into

## Conversation

|
You can do this by running: |

## Realtime ASR Benchmarking Test Results ✅Hi! I'm ## Test Configuration
## Results Summary ✅
## Realtime Streaming Metrics
## Audio Input Metrics
## Network Verification
## Key Findings
## Implementation Notes
```
pip3 install --force-reinstall \
"git+https://github.com/ushaket/guidellm.git@uris/realtime-transcription-endpoint#egg=guidellm[audio]"
``` ## Full Documentation & ResultsFor complete implementation details, configuration examples, and benchmark reports:
## ConclusionThis PR enables Excellent work on this feature! 🎉
|

[ushaket](https://github.com/ushaket)marked this pull request as ready for review

May 4, 2026 13:51


**requested changes**

[sjmonson](https://github.com/sjmonson)May 4, 2026

###
**
**[sjmonson](https://github.com/sjmonson)
left a comment

**left a comment**

[sjmonson](https://github.com/sjmonson)

There was a problem hiding this comment.

Few changes to get started. This is not a full review still working on the core code.

[src/guidellm/backends/openai/openai_common.py](https://github.com/vllm-project/guidellm/pull/713/files#diff-817be8c76eb251491c612d6050728c70faa80323a97f6022e3600d69899ed3f9)Outdated

[src/guidellm/backends/openai/openai_common.py](https://github.com/vllm-project/guidellm/pull/713/files#diff-817be8c76eb251491c612d6050728c70faa80323a97f6022e3600d69899ed3f9)Outdated

[src/guidellm/backends/openai/openai_common.py](https://github.com/vllm-project/guidellm/pull/713/files#diff-817be8c76eb251491c612d6050728c70faa80323a97f6022e3600d69899ed3f9)Outdated

[src/guidellm/backends/openai/common.py](https://github.com/vllm-project/guidellm/pull/713/files#diff-4ffccc25dabb5d520bd15afa8d392f27ad77531b3e78da3ba05ccac169ec2d42)

[src/guidellm/backends/openai/common.py](https://github.com/vllm-project/guidellm/pull/713/files#diff-4ffccc25dabb5d520bd15afa8d392f27ad77531b3e78da3ba05ccac169ec2d42)

[src/guidellm/backends/openai/websocket.py](https://github.com/vllm-project/guidellm/pull/713/files#diff-ce76e5332e87221068f6a789b2c09640b449b060910ccddd57b86baa91512c3d)

[src/guidellm/backends/openai/realtime_ws.py](https://github.com/vllm-project/guidellm/pull/713/files#diff-1d7fd610723d9ab8c3c447721728bd33f274ee05a988c10b9c3c7a7e9079fb0f)Outdated

[src/guidellm/backends/openai/realtime_ws.py](https://github.com/vllm-project/guidellm/pull/713/files#diff-1d7fd610723d9ab8c3c447721728bd33f274ee05a988c10b9c3c7a7e9079fb0f)Outdated

[pyproject.toml](https://github.com/vllm-project/guidellm/pull/713/files#diff-50c86b7ed8ac2cf95bd48334961bf0530cdc77b5a56f852c5c61b89d735fd711)Outdated

[pyproject.toml](https://github.com/vllm-project/guidellm/pull/713/files#diff-50c86b7ed8ac2cf95bd48334961bf0530cdc77b5a56f852c5c61b89d735fd711)Outdated

|
Thanks |

[ushaket](https://github.com/ushaket)

[force-pushed](https://github.com/vllm-project/guidellm/compare/2d3d24733547a68c169f11759fceb5ddbbcb310a..fc4ee667e0fbfbf10a67461a555e4b9181a6d452)the uris/realtime-transcription-endpoint branch from

[to](https://github.com/vllm-project/guidellm/commit/2d3d24733547a68c169f11759fceb5ddbbcb310a)

`2d3d247`


`fc4ee66`

[Compare](https://github.com/vllm-project/guidellm/compare/2d3d24733547a68c169f11759fceb5ddbbcb310a..fc4ee667e0fbfbf10a67461a555e4b9181a6d452)

May 4, 2026 16:45


**reviewed**

[dbutenhof](https://github.com/dbutenhof)May 4, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)

There was a problem hiding this comment.

Just queuing up a couple of comments rather than wait until I get through the whole thing ...

[src/guidellm/backends/openai/websocket.py](https://github.com/vllm-project/guidellm/pull/713/files#diff-ce76e5332e87221068f6a789b2c09640b449b060910ccddd57b86baa91512c3d)Outdated

[src/guidellm/backends/openai/common.py](https://github.com/vllm-project/guidellm/pull/713/files#diff-4ffccc25dabb5d520bd15afa8d392f27ad77531b3e78da3ba05ccac169ec2d42)Outdated

[src/guidellm/backends/openai/websocket.py](https://github.com/vllm-project/guidellm/pull/713/files#diff-ce76e5332e87221068f6a789b2c09640b449b060910ccddd57b86baa91512c3d)Outdated

[src/guidellm/backends/openai/websocket.py](https://github.com/vllm-project/guidellm/pull/713/files#diff-ce76e5332e87221068f6a789b2c09640b449b060910ccddd57b86baa91512c3d)Outdated

|
Thanks |


**requested changes**

[dbutenhof](https://github.com/dbutenhof)May 5, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)

There was a problem hiding this comment.

Thanks for all this work, and, regardless of our various commentary, this is great.

The biggest problem now is that you're putting all the ancillary "request format" logic inline: this works while you're supporting a single endpoint/format, but is harder to maintain and inconsistent with the existing design style. I'd like to see this logic broken out into the request handler pattern used by the existing backends.

I'd like to see better use of meaningful docstrings, too.

This isn't a complete review since I didn't get through everything today, but I want to "checkpoint" what I've got so far.

[src/guidellm/backends/openai/websocket.py](https://github.com/vllm-project/guidellm/pull/713/files#diff-ce76e5332e87221068f6a789b2c09640b449b060910ccddd57b86baa91512c3d)Outdated

[src/guidellm/backends/openai/websocket.py](https://github.com/vllm-project/guidellm/pull/713/files#diff-ce76e5332e87221068f6a789b2c09640b449b060910ccddd57b86baa91512c3d)Outdated

[src/guidellm/backends/openai/websocket.py](https://github.com/vllm-project/guidellm/pull/713/files#diff-ce76e5332e87221068f6a789b2c09640b449b060910ccddd57b86baa91512c3d)Outdated

[src/guidellm/backends/openai/websocket.py](https://github.com/vllm-project/guidellm/pull/713/files#diff-ce76e5332e87221068f6a789b2c09640b449b060910ccddd57b86baa91512c3d)Outdated

[src/guidellm/backends/openai/websocket.py](https://github.com/vllm-project/guidellm/pull/713/files#diff-ce76e5332e87221068f6a789b2c09640b449b060910ccddd57b86baa91512c3d)Outdated

[ushaket](https://github.com/ushaket)

[force-pushed](https://github.com/vllm-project/guidellm/compare/9ed9d2be86234ebf41569dd4099e76ec7733793d..16c1a99d27f8e33e914a6362c6f08592ded78304)the uris/realtime-transcription-endpoint branch 3 times, most recently from

[to](https://github.com/vllm-project/guidellm/commit/9ed9d2be86234ebf41569dd4099e76ec7733793d)

`9ed9d2b`


`16c1a99`

[Compare](https://github.com/vllm-project/guidellm/compare/9ed9d2be86234ebf41569dd4099e76ec7733793d..16c1a99d27f8e33e914a6362c6f08592ded78304)

May 11, 2026 18:33

|
Thanks |

[sjmonson](https://github.com/sjmonson)self-requested a review

May 26, 2026 18:39

|
This pull request has merge conflicts that must be resolved before it can be |


**requested changes**

[dbutenhof](https://github.com/dbutenhof)May 26, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)

There was a problem hiding this comment.

I feel some minor discomfort about the way you did the `append_pcm16_chunks`

late binding, but I won't block on that.

However, you do now need to resolve conflicts on the dependencies due to some other changes, so I can't "approve", yet. (Or rather, it wouldn't do much good.)

[src/guidellm/backends/openai/websocket.py](https://github.com/vllm-project/guidellm/pull/713/files#diff-ce76e5332e87221068f6a789b2c09640b449b060910ccddd57b86baa91512c3d)Outdated


**requested changes**

[sjmonson](https://github.com/sjmonson)May 26, 2026

[src/guidellm/backends/openai/websocket.py](https://github.com/vllm-project/guidellm/pull/713/files#diff-ce76e5332e87221068f6a789b2c09640b449b060910ccddd57b86baa91512c3d)Outdated

[src/guidellm/backends/openai/websocket.py](https://github.com/vllm-project/guidellm/pull/713/files#diff-ce76e5332e87221068f6a789b2c09640b449b060910ccddd57b86baa91512c3d)Outdated

[src/guidellm/backends/openai/websocket.py](https://github.com/vllm-project/guidellm/pull/713/files#diff-ce76e5332e87221068f6a789b2c09640b449b060910ccddd57b86baa91512c3d)Outdated

[src/guidellm/backends/openai/websocket.py](https://github.com/vllm-project/guidellm/pull/713/files#diff-ce76e5332e87221068f6a789b2c09640b449b060910ccddd57b86baa91512c3d)Outdated

[src/guidellm/backends/backend.py](https://github.com/vllm-project/guidellm/pull/713/files#diff-5c24e7ba3bcac69581ff50255450d871c262dddfc1a230cd42aeac92882d4bc5)Outdated

[src/guidellm/backends/openai/websocket.py](https://github.com/vllm-project/guidellm/pull/713/files#diff-ce76e5332e87221068f6a789b2c09640b449b060910ccddd57b86baa91512c3d)Outdated

[src/guidellm/backends/openai/request_handlers.py](https://github.com/vllm-project/guidellm/pull/713/files#diff-60cfc62dcd68426ebab8f6d637eba19d6423ac6fe297be59efdfb943b9f0d79f)Outdated

[src/guidellm/backends/openai/request_handlers.py](https://github.com/vllm-project/guidellm/pull/713/files#diff-60cfc62dcd68426ebab8f6d637eba19d6423ac6fe297be59efdfb943b9f0d79f)Outdated

[src/guidellm/backends/openai/websocket.py](https://github.com/vllm-project/guidellm/pull/713/files#diff-ce76e5332e87221068f6a789b2c09640b449b060910ccddd57b86baa91512c3d)Outdated

[src/guidellm/backends/openai/websocket.py](https://github.com/vllm-project/guidellm/pull/713/files#diff-ce76e5332e87221068f6a789b2c09640b449b060910ccddd57b86baa91512c3d)Outdated

[ushaket](https://github.com/ushaket)

[force-pushed](https://github.com/vllm-project/guidellm/compare/16c1a99d27f8e33e914a6362c6f08592ded78304..4636a53a0b5777e411ddb47e738cb9d500154c24)the uris/realtime-transcription-endpoint branch from

[to](https://github.com/vllm-project/guidellm/commit/16c1a99d27f8e33e914a6362c6f08592ded78304)

`16c1a99`


`4636a53`

[Compare](https://github.com/vllm-project/guidellm/compare/16c1a99d27f8e33e914a6362c6f08592ded78304..4636a53a0b5777e411ddb47e738cb9d500154c24)

June 1, 2026 08:21

|
Hi In round 2, "This inline mapping is a bit messy, and breaks existing widespread patterns in GuideLLM. Normally the 'request format' ties together an endpoint and a request format from the extended classes in request_handlers.py." I added RealtimeWebSocketRequestHandler to address that. Now in this round, "This is not using OpenAIRequestHandler as intended. I think those classes don't make sense here. Instead of doing this weird back and forth, move the relevant functions into the backend." I'm happy to go either way — could you align on which approach you'd prefer? Keep the handler pattern — clean up RealtimeWebSocketRequestHandler to better match how OpenAIRequestHandler is used in the HTTP backend. |

I think the assumption was that there could be a clean separation between formatting / parsing the request and actually sending the request, but the problem is that does not seem to be the case. You don't even use the class for parsing anything but usage metrics. Our hope was that we could eventually reuse some of this code for
The other issues I see is |

|
Thanks for the detailed explanation Before I inline everything, I'd like to propose an alternative that fixes those issues while keeping the handler pattern useful, including for future
The proposed lifecycle for a single WS request would be:
This fixes the specific issues you flagged:
On the reuse question: while the event
That said, if you'd still prefer inlining, I'm happy to go that route. Let me know which direction you'd like. |

I think this makes sense however because the usage pattern is still different from HTTP, I think its better to have a separate base class for websocket handlers. You could do a mixin pattern for some of the shared functions, so maybe something like: ```
class RequestHandlerMixin(Protocol):
def format(...): ...
def compile_non_streaming(...): ...
def compile_streaming(...): ...
class OpenAIHTTPRequestHandler(Protocol, RequestHandlerMixin):
def add_streaming_line(...): ...
class OpenAIWSRequestHandler(Protocol, RequestHandlerMixin):
def add_streaming_event(event: dict) -> int | None: ...
class OpenAIHandlerFactory(RegistryMixin[type[OpenAIHTTPRequestHandler] | type[OpenAIWSRequestHandler]]): ...
``` Maybe even take this further and have separate mixins for streaming vs non-streaming which are added at the concrete handler implementation rather then the base protocol. Also might make more sense for now to have separate |

|
Also one housekeeping note: the code you added to Anywhere you lazy load from extras like: For the websockets library; if we were keeping it as part of the audio extras it should go in the shim. But I think its probably better to just add it to the core package list since its not really audio specific and we will need it for responses eventually. So I think just move it into core requirements and drop all the |

[ushaket](https://github.com/ushaket)

[force-pushed](https://github.com/vllm-project/guidellm/compare/17747ca6f31981cab1cca9946343040b9770b46d..08dd09461ed4371ca3051b31d05af434d79330fe)the uris/realtime-transcription-endpoint branch from

[to](https://github.com/vllm-project/guidellm/commit/17747ca6f31981cab1cca9946343040b9770b46d)

`17747ca`


`08dd094`

[Compare](https://github.com/vllm-project/guidellm/compare/17747ca6f31981cab1cca9946343040b9770b46d..08dd09461ed4371ca3051b31d05af434d79330fe)

June 8, 2026 08:00

Co-authored-by: Samuel Monson <smonson@irbash.net> Signed-off-by: Uri Shaket <ushaket@redhat.com>

…main rebase - OpenAIWebSocketBackend takes OpenAIWebSocketBackendArgs; register args type - Drop request_format path aliases; fix validate() header merge for httpx mocks - Update unit/e2e tests and entrypoint expectations for discriminator + CLI layout Co-authored-by: Cursor <cursoragent@cursor.com> Signed-off-by: Uri Shaket <ushaket@redhat.com>

…ltime - Resolve stash pop conflicts: keep thin __main__ + guidellm.cli entrypoint - WebSocket: allowlist request_format, RealtimeWebSocketRequestHandler in resolve, append_pcm16_chunks static hook; merge request_handlers + tests from stash Co-authored-by: Cursor <cursoragent@cursor.com> Signed-off-by: Uri Shaket <ushaket@redhat.com>

…ckend - RealtimeWebSocketRequestHandler: ALLOWED_REQUEST_PATHS, validation classmethods - OpenAIWebSocketBackendArgs delegates to handler; remove inline path helpers - OpenAIWebSocketBackend: class and method docstrings aligned with OpenAIHTTPBackend - Unit tests for handler request_format helpers Co-authored-by: Cursor <cursoragent@cursor.com> Signed-off-by: Uri Shaket <ushaket@redhat.com> Co-authored-by: Cursor <cursoragent@cursor.com>

Signed-off-by: Uri Shaket <ushaket@redhat.com> Co-authored-by: Cursor <cursoragent@cursor.com>

…websockets a core dep Signed-off-by: Uri Shaket <ushaket@redhat.com>

Signed-off-by: Uri Shaket <ushaket@redhat.com>

[ushaket](https://github.com/ushaket)

[force-pushed](https://github.com/vllm-project/guidellm/compare/15f83063360547471fd56feea03162bf928acc0a..3b8434d3eaabc5bd6cca259fe1ae6077d0a9c057)the uris/realtime-transcription-endpoint branch from

[to](https://github.com/vllm-project/guidellm/commit/15f83063360547471fd56feea03162bf928acc0a)

`15f8306`


`3b8434d`

[Compare](https://github.com/vllm-project/guidellm/compare/15f83063360547471fd56feea03162bf928acc0a..3b8434d3eaabc5bd6cca259fe1ae6077d0a9c057)

June 21, 2026 06:06


**approved these changes**

[sjmonson](https://github.com/sjmonson)Jun 22, 2026

## Merge Queue Status
This pull request spent ## Required conditions to merge
|

[SkiHatDuckie](https://github.com/SkiHatDuckie)pushed a commit to SkiHatDuckie/guidellm that referenced this pull request

Jun 23, 2026

## Summary Adds an **`openai_realtime_ws`** backend that drives **vLLM-compatible `/v1/realtime` WebSocket** audio transcription: PCM chunking, `session.update` / `input_audio_buffer.*` flow, handling of `transcription.delta` / `transcription.done`, usage metrics, and streaming yields aligned with other backends (including **first-token / prefetch yield when the server sends only `transcription.done`**). Refactors shared OpenAI HTTP concerns into **`openai_common.py`** (validate kwargs, headers, fallback timeout) and extends **`extras/audio.py`** with helpers used for realtime PCM. **`websockets`** is wired under the **`[audio]`** optional extra. Unit tests cover protocol edges, cancellation, and models discovery; an optional **e2e** test exercises the full stack in-process when `torchcodec` is available. ## Details - [ ] Register **`openai_realtime_ws`** on `Backend` and extend **`BackendType`**. - [ ] Add **`OpenAIRealtimeWebSocketBackend`** + **`OpenAIRealtimeWsBackendArgs`** (`realtime_ws.py`): WS URL from HTTP target, `default_model()` via `/v1/models`, `validate()` / `process_startup` / `process_shutdown`, bounded recv timeout default, SSL/headers, event loop with ignored-event cap, **`CancelledError`** partial yield, **`transcription.done`-only** first-token timing + `yield None, request_info`. - [ ] Add **`openai_common.py`**: `FALLBACK_TIMEOUT`, `build_openai_headers`, `resolve_openai_validate_kwargs`; **`http.py`** delegates to these helpers. - [ ] Extend **`extras/audio.py`**: PCM16 chunking / decoding path used by realtime (e.g. `pcm16_append_b64_chunks`, sample-rate handling as implemented). - [ ] **`pyproject.toml` / `uv.lock`**: optional **`websockets`** (and lock updates as generated). - [ ] **`tests/unit/backends/openai/test_realtime_ws.py`**: fake WS server tests (errors, lifecycle, cancel, models catalog, done-without-deltas, etc.). - [ ] **`tests/e2e/test_realtime_ws_e2e.py`**: in-process full stack with real WAV + `torchcodec` (marked e2e / timeout). - [ ] **`tests/unit/extras/test_audio.py`**, **`test_backend.py`**, **`test_entrypoints.py`**: coverage / registration / CLI args for the new backend. ## Test Plan - `uv run pytest tests/unit/backends/openai/test_realtime_ws.py -v` - `uv run pytest tests/unit/extras/test_audio.py tests/unit/backends/test_backend.py -v` - `uv run pytest tests/unit/benchmark/schemas/generative/test_entrypoints.py -k realtime -v` - `uv run pytest tests/e2e/test_realtime_ws_e2e.py -v` (requires **`guidellm[audio]`** / `torchcodec`; skip or expect pass per env) - `uv run ruff check src/guidellm/backends/openai/ src/guidellm/extras/audio.py tests/unit/backends/openai/` ## Related Issues - Resolves[vllm-project#706]--- - [X] "I certify that all code in this PR is my own, except as noted below." ## Use of AI - [X] Includes AI-assisted code completion - [X] Includes code generated by an AI application - [X] Includes AI-generated tests (NOTE: AI written tests should have a docstring that includes `## WRITTEN BY AI ##`) --- # git log commit[Author: Uri Shaket <ushaket@redhat.com> Date: Mon May 4 10:08:55 2026 +0300 initial commit Signed-off-by: Uri Shaket <ushaket@redhat.com> commit]f77f39e[Author: Uri Shaket <ushaket@redhat.com> Date: Mon May 4 10:21:58 2026 +0300 missing files Signed-off-by: Uri Shaket <ushaket@redhat.com> commit]78038d4[Author: Uri Shaket <ushaket@redhat.com> Date: Mon May 4 10:37:19 2026 +0300 lint Signed-off-by: Uri Shaket <ushaket@redhat.com> commit]3afd7c5[Author: Uri Shaket <ushaket@redhat.com> Date: Mon May 4 17:25:03 2026 +0300 Update src/guidellm/backends/openai/openai_common.py Co-authored-by: Samuel Monson <smonson@irbash.net> Signed-off-by: Uri Shaket <ushaket@redhat.com> commit]e122e9c[Author: Uri Shaket <ushaket@redhat.com> Date: Mon May 4 17:25:14 2026 +0300 Update src/guidellm/backends/openai/openai_common.py Co-authored-by: Samuel Monson <smonson@irbash.net> Signed-off-by: Uri Shaket <ushaket@redhat.com> commit]1e2ab9b[Author: Uri Shaket <ushaket@redhat.com> Date: Mon May 4 17:35:38 2026 +0300 CR Signed-off-by: Uri Shaket <ushaket@redhat.com> commit]51940e7[Author: Uri Shaket <ushaket@redhat.com> Date: Mon May 4 17:35:47 2026 +0300 CR Signed-off-by: Uri Shaket <ushaket@redhat.com> commit]2dd7a63[Author: Uri Shaket <ushaket@redhat.com> Date: Mon May 4 17:49:56 2026 +0300 CR Signed-off-by: Uri Shaket <ushaket@redhat.com> commit]ca21039[Author: Uri Shaket <ushaket@redhat.com> Date: Tue May 5 12:54:47 2026 +0300 CR Signed-off-by: Uri Shaket <ushaket@redhat.com> commit]7e77e08[Author: Uri Shaket <ushaket@redhat.com> Date: Tue May 5 13:02:03 2026 +0300 lint Signed-off-by: Uri Shaket <ushaket@redhat.com> commit]8bcc239[Author: Uri Shaket <ushaket@redhat.com> Date: Tue May 5 13:23:55 2026 +0300 CR Signed-off-by: Uri Shaket <ushaket@redhat.com> commit]78e195b[Author: Uri Shaket <ushaket@redhat.com> Date: Mon May 11 20:43:20 2026 +0300 Align openai_websocket backend with BackendArgs/Backend.create after main rebase - OpenAIWebSocketBackend takes OpenAIWebSocketBackendArgs; register args type - Drop request_format path aliases; fix validate() header merge for httpx mocks - Update unit/e2e tests and entrypoint expectations for discriminator + CLI layout Co-authored-by: Cursor <cursoragent@cursor.com> Signed-off-by: Uri Shaket <ushaket@redhat.com> commit]c05c840[Author: Uri Shaket <ushaket@redhat.com> Date: Mon May 11 20:48:16 2026 +0300 Apply pre-rebase stash: realtime WS handler wiring and strict /v1/realtime - Resolve stash pop conflicts: keep thin __main__ + guidellm.cli entrypoint - WebSocket: allowlist request_format, RealtimeWebSocketRequestHandler in resolve, append_pcm16_chunks static hook; merge request_handlers + tests from stash Co-authored-by: Cursor <cursoragent@cursor.com> Signed-off-by: Uri Shaket <ushaket@redhat.com> commit]3a934f8[Author: Uri Shaket <ushaket@redhat.com> Date: Mon May 11 20:58:18 2026 +0300 Move realtime request_format policy to handler; document WebSocket backend - RealtimeWebSocketRequestHandler: ALLOWED_REQUEST_PATHS, validation classmethods - OpenAIWebSocketBackendArgs delegates to handler; remove inline path helpers - OpenAIWebSocketBackend: class and method docstrings aligned with OpenAIHTTPBackend - Unit tests for handler request_format helpers Co-authored-by: Cursor <cursoragent@cursor.com> Signed-off-by: Uri Shaket <ushaket@redhat.com> Co-authored-by: Cursor <cursoragent@cursor.com> commit]ff846ff[Author: Uri Shaket <ushaket@redhat.com> Date: Mon May 11 21:30:19 2026 +0300 fix: ruff format and import order for CI quality gates Signed-off-by: Uri Shaket <ushaket@redhat.com> Co-authored-by: Cursor <cursoragent@cursor.com> commit]6cae2aa[Author: Uri Shaket <ushaket@redhat.com> Date: Mon Jun 1 13:07:09 2026 +0300 CR Signed-off-by: Uri Shaket <ushaket@redhat.com> commit]d5e50c3[Author: Uri Shaket <ushaket@redhat.com> Date: Mon Jun 8 10:55:49 2026 +0300 Refactor realtime WebSocket backend behind WS handler protocol; make websockets a core dep Signed-off-by: Uri Shaket <ushaket@redhat.com> commit]e1704f6[Author: Uri Shaket <ushaket@redhat.com> Date: Mon Jun 8 11:21:50 2026 +0300 lint Signed-off-by: Uri Shaket <ushaket@redhat.com> commit]9c7f10e[Author: Uri Shaket <ushaket@redhat.com> Date: Mon Jun 8 12:42:20 2026 +0300 self CR Signed-off-by: Uri Shaket <ushaket@redhat.com> commit]97e0feb[Author: Uri Shaket <ushaket@redhat.com> Date: Wed Jun 17 08:21:02 2026 +0300 Fix pcm16_append_b64_chunks for _decode_audio tuple return Signed-off-by: Uri Shaket <ushaket@redhat.com> --------- Co-authored-by: Cursor <cursoragent@cursor.com> Co-authored-by: Samuel Monson <smonson@irbash.net> Signed-off-by: Uri Shaket <ushaket@redhat.com>]3b8434d

[SkiHatDuckie](https://github.com/SkiHatDuckie)pushed a commit to SkiHatDuckie/guidellm that referenced this pull request

Jun 24, 2026

## Summary Adds an **`openai_realtime_ws`** backend that drives **vLLM-compatible `/v1/realtime` WebSocket** audio transcription: PCM chunking, `session.update` / `input_audio_buffer.*` flow, handling of `transcription.delta` / `transcription.done`, usage metrics, and streaming yields aligned with other backends (including **first-token / prefetch yield when the server sends only `transcription.done`**). Refactors shared OpenAI HTTP concerns into **`openai_common.py`** (validate kwargs, headers, fallback timeout) and extends **`extras/audio.py`** with helpers used for realtime PCM. **`websockets`** is wired under the **`[audio]`** optional extra. Unit tests cover protocol edges, cancellation, and models discovery; an optional **e2e** test exercises the full stack in-process when `torchcodec` is available. ## Details - [ ] Register **`openai_realtime_ws`** on `Backend` and extend **`BackendType`**. - [ ] Add **`OpenAIRealtimeWebSocketBackend`** + **`OpenAIRealtimeWsBackendArgs`** (`realtime_ws.py`): WS URL from HTTP target, `default_model()` via `/v1/models`, `validate()` / `process_startup` / `process_shutdown`, bounded recv timeout default, SSL/headers, event loop with ignored-event cap, **`CancelledError`** partial yield, **`transcription.done`-only** first-token timing + `yield None, request_info`. - [ ] Add **`openai_common.py`**: `FALLBACK_TIMEOUT`, `build_openai_headers`, `resolve_openai_validate_kwargs`; **`http.py`** delegates to these helpers. - [ ] Extend **`extras/audio.py`**: PCM16 chunking / decoding path used by realtime (e.g. `pcm16_append_b64_chunks`, sample-rate handling as implemented). - [ ] **`pyproject.toml` / `uv.lock`**: optional **`websockets`** (and lock updates as generated). - [ ] **`tests/unit/backends/openai/test_realtime_ws.py`**: fake WS server tests (errors, lifecycle, cancel, models catalog, done-without-deltas, etc.). - [ ] **`tests/e2e/test_realtime_ws_e2e.py`**: in-process full stack with real WAV + `torchcodec` (marked e2e / timeout). - [ ] **`tests/unit/extras/test_audio.py`**, **`test_backend.py`**, **`test_entrypoints.py`**: coverage / registration / CLI args for the new backend. ## Test Plan - `uv run pytest tests/unit/backends/openai/test_realtime_ws.py -v` - `uv run pytest tests/unit/extras/test_audio.py tests/unit/backends/test_backend.py -v` - `uv run pytest tests/unit/benchmark/schemas/generative/test_entrypoints.py -k realtime -v` - `uv run pytest tests/e2e/test_realtime_ws_e2e.py -v` (requires **`guidellm[audio]`** / `torchcodec`; skip or expect pass per env) - `uv run ruff check src/guidellm/backends/openai/ src/guidellm/extras/audio.py tests/unit/backends/openai/` ## Related Issues - Resolves[vllm-project#706]--- - [X] "I certify that all code in this PR is my own, except as noted below." ## Use of AI - [X] Includes AI-assisted code completion - [X] Includes code generated by an AI application - [X] Includes AI-generated tests (NOTE: AI written tests should have a docstring that includes `## WRITTEN BY AI ##`) --- # git log commit[Author: Uri Shaket <ushaket@redhat.com> Date: Mon May 4 10:08:55 2026 +0300 initial commit Signed-off-by: Uri Shaket <ushaket@redhat.com> commit]f77f39e[Author: Uri Shaket <ushaket@redhat.com> Date: Mon May 4 10:21:58 2026 +0300 missing files Signed-off-by: Uri Shaket <ushaket@redhat.com> commit]78038d4[Author: Uri Shaket <ushaket@redhat.com> Date: Mon May 4 10:37:19 2026 +0300 lint Signed-off-by: Uri Shaket <ushaket@redhat.com> commit]3afd7c5[Author: Uri Shaket <ushaket@redhat.com> Date: Mon May 4 17:25:03 2026 +0300 Update src/guidellm/backends/openai/openai_common.py Co-authored-by: Samuel Monson <smonson@irbash.net> Signed-off-by: Uri Shaket <ushaket@redhat.com> commit]e122e9c[Author: Uri Shaket <ushaket@redhat.com> Date: Mon May 4 17:25:14 2026 +0300 Update src/guidellm/backends/openai/openai_common.py Co-authored-by: Samuel Monson <smonson@irbash.net> Signed-off-by: Uri Shaket <ushaket@redhat.com> commit]1e2ab9b[Author: Uri Shaket <ushaket@redhat.com> Date: Mon May 4 17:35:38 2026 +0300 CR Signed-off-by: Uri Shaket <ushaket@redhat.com> commit]51940e7[Author: Uri Shaket <ushaket@redhat.com> Date: Mon May 4 17:35:47 2026 +0300 CR Signed-off-by: Uri Shaket <ushaket@redhat.com> commit]2dd7a63[Author: Uri Shaket <ushaket@redhat.com> Date: Mon May 4 17:49:56 2026 +0300 CR Signed-off-by: Uri Shaket <ushaket@redhat.com> commit]ca21039[Author: Uri Shaket <ushaket@redhat.com> Date: Tue May 5 12:54:47 2026 +0300 CR Signed-off-by: Uri Shaket <ushaket@redhat.com> commit]7e77e08[Author: Uri Shaket <ushaket@redhat.com> Date: Tue May 5 13:02:03 2026 +0300 lint Signed-off-by: Uri Shaket <ushaket@redhat.com> commit]8bcc239[Author: Uri Shaket <ushaket@redhat.com> Date: Tue May 5 13:23:55 2026 +0300 CR Signed-off-by: Uri Shaket <ushaket@redhat.com> commit]78e195b[Author: Uri Shaket <ushaket@redhat.com> Date: Mon May 11 20:43:20 2026 +0300 Align openai_websocket backend with BackendArgs/Backend.create after main rebase - OpenAIWebSocketBackend takes OpenAIWebSocketBackendArgs; register args type - Drop request_format path aliases; fix validate() header merge for httpx mocks - Update unit/e2e tests and entrypoint expectations for discriminator + CLI layout Co-authored-by: Cursor <cursoragent@cursor.com> Signed-off-by: Uri Shaket <ushaket@redhat.com> commit]c05c840[Author: Uri Shaket <ushaket@redhat.com> Date: Mon May 11 20:48:16 2026 +0300 Apply pre-rebase stash: realtime WS handler wiring and strict /v1/realtime - Resolve stash pop conflicts: keep thin __main__ + guidellm.cli entrypoint - WebSocket: allowlist request_format, RealtimeWebSocketRequestHandler in resolve, append_pcm16_chunks static hook; merge request_handlers + tests from stash Co-authored-by: Cursor <cursoragent@cursor.com> Signed-off-by: Uri Shaket <ushaket@redhat.com> commit]3a934f8[Author: Uri Shaket <ushaket@redhat.com> Date: Mon May 11 20:58:18 2026 +0300 Move realtime request_format policy to handler; document WebSocket backend - RealtimeWebSocketRequestHandler: ALLOWED_REQUEST_PATHS, validation classmethods - OpenAIWebSocketBackendArgs delegates to handler; remove inline path helpers - OpenAIWebSocketBackend: class and method docstrings aligned with OpenAIHTTPBackend - Unit tests for handler request_format helpers Co-authored-by: Cursor <cursoragent@cursor.com> Signed-off-by: Uri Shaket <ushaket@redhat.com> Co-authored-by: Cursor <cursoragent@cursor.com> commit]ff846ff[Author: Uri Shaket <ushaket@redhat.com> Date: Mon May 11 21:30:19 2026 +0300 fix: ruff format and import order for CI quality gates Signed-off-by: Uri Shaket <ushaket@redhat.com> Co-authored-by: Cursor <cursoragent@cursor.com> commit]6cae2aa[Author: Uri Shaket <ushaket@redhat.com> Date: Mon Jun 1 13:07:09 2026 +0300 CR Signed-off-by: Uri Shaket <ushaket@redhat.com> commit]d5e50c3[Author: Uri Shaket <ushaket@redhat.com> Date: Mon Jun 8 10:55:49 2026 +0300 Refactor realtime WebSocket backend behind WS handler protocol; make websockets a core dep Signed-off-by: Uri Shaket <ushaket@redhat.com> commit]e1704f6[Author: Uri Shaket <ushaket@redhat.com> Date: Mon Jun 8 11:21:50 2026 +0300 lint Signed-off-by: Uri Shaket <ushaket@redhat.com> commit]9c7f10e[Author: Uri Shaket <ushaket@redhat.com> Date: Mon Jun 8 12:42:20 2026 +0300 self CR Signed-off-by: Uri Shaket <ushaket@redhat.com> commit]97e0feb[Author: Uri Shaket <ushaket@redhat.com> Date: Wed Jun 17 08:21:02 2026 +0300 Fix pcm16_append_b64_chunks for _decode_audio tuple return Signed-off-by: Uri Shaket <ushaket@redhat.com> --------- Co-authored-by: Cursor <cursoragent@cursor.com> Co-authored-by: Samuel Monson <smonson@irbash.net> Signed-off-by: Uri Shaket <ushaket@redhat.com>]3b8434d

[SkiHatDuckie](https://github.com/SkiHatDuckie)pushed a commit to SkiHatDuckie/guidellm that referenced this pull request

Jul 6, 2026

## Summary Adds an **`openai_realtime_ws`** backend that drives **vLLM-compatible `/v1/realtime` WebSocket** audio transcription: PCM chunking, `session.update` / `input_audio_buffer.*` flow, handling of `transcription.delta` / `transcription.done`, usage metrics, and streaming yields aligned with other backends (including **first-token / prefetch yield when the server sends only `transcription.done`**). Refactors shared OpenAI HTTP concerns into **`openai_common.py`** (validate kwargs, headers, fallback timeout) and extends **`extras/audio.py`** with helpers used for realtime PCM. **`websockets`** is wired under the **`[audio]`** optional extra. Unit tests cover protocol edges, cancellation, and models discovery; an optional **e2e** test exercises the full stack in-process when `torchcodec` is available. ## Details - [ ] Register **`openai_realtime_ws`** on `Backend` and extend **`BackendType`**. - [ ] Add **`OpenAIRealtimeWebSocketBackend`** + **`OpenAIRealtimeWsBackendArgs`** (`realtime_ws.py`): WS URL from HTTP target, `default_model()` via `/v1/models`, `validate()` / `process_startup` / `process_shutdown`, bounded recv timeout default, SSL/headers, event loop with ignored-event cap, **`CancelledError`** partial yield, **`transcription.done`-only** first-token timing + `yield None, request_info`. - [ ] Add **`openai_common.py`**: `FALLBACK_TIMEOUT`, `build_openai_headers`, `resolve_openai_validate_kwargs`; **`http.py`** delegates to these helpers. - [ ] Extend **`extras/audio.py`**: PCM16 chunking / decoding path used by realtime (e.g. `pcm16_append_b64_chunks`, sample-rate handling as implemented). - [ ] **`pyproject.toml` / `uv.lock`**: optional **`websockets`** (and lock updates as generated). - [ ] **`tests/unit/backends/openai/test_realtime_ws.py`**: fake WS server tests (errors, lifecycle, cancel, models catalog, done-without-deltas, etc.). - [ ] **`tests/e2e/test_realtime_ws_e2e.py`**: in-process full stack with real WAV + `torchcodec` (marked e2e / timeout). - [ ] **`tests/unit/extras/test_audio.py`**, **`test_backend.py`**, **`test_entrypoints.py`**: coverage / registration / CLI args for the new backend. ## Test Plan - `uv run pytest tests/unit/backends/openai/test_realtime_ws.py -v` - `uv run pytest tests/unit/extras/test_audio.py tests/unit/backends/test_backend.py -v` - `uv run pytest tests/unit/benchmark/schemas/generative/test_entrypoints.py -k realtime -v` - `uv run pytest tests/e2e/test_realtime_ws_e2e.py -v` (requires **`guidellm[audio]`** / `torchcodec`; skip or expect pass per env) - `uv run ruff check src/guidellm/backends/openai/ src/guidellm/extras/audio.py tests/unit/backends/openai/` ## Related Issues - Resolves[vllm-project#706]--- - [X] "I certify that all code in this PR is my own, except as noted below." ## Use of AI - [X] Includes AI-assisted code completion - [X] Includes code generated by an AI application - [X] Includes AI-generated tests (NOTE: AI written tests should have a docstring that includes `## WRITTEN BY AI ##`) --- # git log commit[Author: Uri Shaket <ushaket@redhat.com> Date: Mon May 4 10:08:55 2026 +0300 initial commit Signed-off-by: Uri Shaket <ushaket@redhat.com> commit]f77f39e[Author: Uri Shaket <ushaket@redhat.com> Date: Mon May 4 10:21:58 2026 +0300 missing files Signed-off-by: Uri Shaket <ushaket@redhat.com> commit]78038d4[Author: Uri Shaket <ushaket@redhat.com> Date: Mon May 4 10:37:19 2026 +0300 lint Signed-off-by: Uri Shaket <ushaket@redhat.com> commit]3afd7c5[Author: Uri Shaket <ushaket@redhat.com> Date: Mon May 4 17:25:03 2026 +0300 Update src/guidellm/backends/openai/openai_common.py Co-authored-by: Samuel Monson <smonson@irbash.net> Signed-off-by: Uri Shaket <ushaket@redhat.com> commit]e122e9c[Author: Uri Shaket <ushaket@redhat.com> Date: Mon May 4 17:25:14 2026 +0300 Update src/guidellm/backends/openai/openai_common.py Co-authored-by: Samuel Monson <smonson@irbash.net> Signed-off-by: Uri Shaket <ushaket@redhat.com> commit]1e2ab9b[Author: Uri Shaket <ushaket@redhat.com> Date: Mon May 4 17:35:38 2026 +0300 CR Signed-off-by: Uri Shaket <ushaket@redhat.com> commit]51940e7[Author: Uri Shaket <ushaket@redhat.com> Date: Mon May 4 17:35:47 2026 +0300 CR Signed-off-by: Uri Shaket <ushaket@redhat.com> commit]2dd7a63[Author: Uri Shaket <ushaket@redhat.com> Date: Mon May 4 17:49:56 2026 +0300 CR Signed-off-by: Uri Shaket <ushaket@redhat.com> commit]ca21039[Author: Uri Shaket <ushaket@redhat.com> Date: Tue May 5 12:54:47 2026 +0300 CR Signed-off-by: Uri Shaket <ushaket@redhat.com> commit]7e77e08[Author: Uri Shaket <ushaket@redhat.com> Date: Tue May 5 13:02:03 2026 +0300 lint Signed-off-by: Uri Shaket <ushaket@redhat.com> commit]8bcc239[Author: Uri Shaket <ushaket@redhat.com> Date: Tue May 5 13:23:55 2026 +0300 CR Signed-off-by: Uri Shaket <ushaket@redhat.com> commit]78e195b[Author: Uri Shaket <ushaket@redhat.com> Date: Mon May 11 20:43:20 2026 +0300 Align openai_websocket backend with BackendArgs/Backend.create after main rebase - OpenAIWebSocketBackend takes OpenAIWebSocketBackendArgs; register args type - Drop request_format path aliases; fix validate() header merge for httpx mocks - Update unit/e2e tests and entrypoint expectations for discriminator + CLI layout Co-authored-by: Cursor <cursoragent@cursor.com> Signed-off-by: Uri Shaket <ushaket@redhat.com> commit]c05c840[Author: Uri Shaket <ushaket@redhat.com> Date: Mon May 11 20:48:16 2026 +0300 Apply pre-rebase stash: realtime WS handler wiring and strict /v1/realtime - Resolve stash pop conflicts: keep thin __main__ + guidellm.cli entrypoint - WebSocket: allowlist request_format, RealtimeWebSocketRequestHandler in resolve, append_pcm16_chunks static hook; merge request_handlers + tests from stash Co-authored-by: Cursor <cursoragent@cursor.com> Signed-off-by: Uri Shaket <ushaket@redhat.com> commit]3a934f8[Author: Uri Shaket <ushaket@redhat.com> Date: Mon May 11 20:58:18 2026 +0300 Move realtime request_format policy to handler; document WebSocket backend - RealtimeWebSocketRequestHandler: ALLOWED_REQUEST_PATHS, validation classmethods - OpenAIWebSocketBackendArgs delegates to handler; remove inline path helpers - OpenAIWebSocketBackend: class and method docstrings aligned with OpenAIHTTPBackend - Unit tests for handler request_format helpers Co-authored-by: Cursor <cursoragent@cursor.com> Signed-off-by: Uri Shaket <ushaket@redhat.com> Co-authored-by: Cursor <cursoragent@cursor.com> commit]ff846ff[Author: Uri Shaket <ushaket@redhat.com> Date: Mon May 11 21:30:19 2026 +0300 fix: ruff format and import order for CI quality gates Signed-off-by: Uri Shaket <ushaket@redhat.com> Co-authored-by: Cursor <cursoragent@cursor.com> commit]6cae2aa[Author: Uri Shaket <ushaket@redhat.com> Date: Mon Jun 1 13:07:09 2026 +0300 CR Signed-off-by: Uri Shaket <ushaket@redhat.com> commit]d5e50c3[Author: Uri Shaket <ushaket@redhat.com> Date: Mon Jun 8 10:55:49 2026 +0300 Refactor realtime WebSocket backend behind WS handler protocol; make websockets a core dep Signed-off-by: Uri Shaket <ushaket@redhat.com> commit]e1704f6[Author: Uri Shaket <ushaket@redhat.com> Date: Mon Jun 8 11:21:50 2026 +0300 lint Signed-off-by: Uri Shaket <ushaket@redhat.com> commit]9c7f10e[Author: Uri Shaket <ushaket@redhat.com> Date: Mon Jun 8 12:42:20 2026 +0300 self CR Signed-off-by: Uri Shaket <ushaket@redhat.com> commit]97e0feb[Author: Uri Shaket <ushaket@redhat.com> Date: Wed Jun 17 08:21:02 2026 +0300 Fix pcm16_append_b64_chunks for _decode_audio tuple return Signed-off-by: Uri Shaket <ushaket@redhat.com> --------- Co-authored-by: Cursor <cursoragent@cursor.com> Co-authored-by: Samuel Monson <smonson@irbash.net> Signed-off-by: Uri Shaket <ushaket@redhat.com>]3b8434d

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

## Summary

Adds an

backend that drives`openai_realtime_ws`

vLLM-compatibleaudio transcription: PCM chunking,`/v1/realtime`

WebSocket`session.update`

/`input_audio_buffer.*`

flow, handling of`transcription.delta`

/`transcription.done`

, usage metrics, and streaming yields aligned with other backends (includingfirst-token / prefetch yield when the server sends only).`transcription.done`

Refactors shared OpenAI HTTP concerns into

(validate kwargs, headers, fallback timeout) and extends`openai_common.py`

with helpers used for realtime PCM.`extras/audio.py`

is wired under the`websockets`

optional extra. Unit tests cover protocol edges, cancellation, and models discovery; an optional`[audio]`

e2etest exercises the full stack in-process when`torchcodec`

is available.## Details

on`openai_realtime_ws`

`Backend`

and extend.`BackendType`

+`OpenAIRealtimeWebSocketBackend`

(`OpenAIRealtimeWsBackendArgs`

`realtime_ws.py`

): WS URL from HTTP target,`default_model()`

via`/v1/models`

,`validate()`

/`process_startup`

/`process_shutdown`

, bounded recv timeout default, SSL/headers, event loop with ignored-event cap,partial yield,`CancelledError`

first-token timing +`transcription.done`

-only`yield None, request_info`

.:`openai_common.py`

`FALLBACK_TIMEOUT`

,`build_openai_headers`

,`resolve_openai_validate_kwargs`

;delegates to these helpers.`http.py`

: PCM16 chunking / decoding path used by realtime (e.g.`extras/audio.py`

`pcm16_append_b64_chunks`

, sample-rate handling as implemented).: optional`pyproject.toml`

/`uv.lock`

(and lock updates as generated).`websockets`

: fake WS server tests (errors, lifecycle, cancel, models catalog, done-without-deltas, etc.).`tests/unit/backends/openai/test_realtime_ws.py`

: in-process full stack with real WAV +`tests/e2e/test_realtime_ws_e2e.py`

`torchcodec`

(marked e2e / timeout).,`tests/unit/extras/test_audio.py`

,`test_backend.py`

: coverage / registration / CLI args for the new backend.`test_entrypoints.py`

## Test Plan

`uv run pytest tests/unit/backends/openai/test_realtime_ws.py -v`

`uv run pytest tests/unit/extras/test_audio.py tests/unit/backends/test_backend.py -v`

`uv run pytest tests/unit/benchmark/schemas/generative/test_entrypoints.py -k realtime -v`

`uv run pytest tests/e2e/test_realtime_ws_e2e.py -v`

(requires/`guidellm[audio]`

`torchcodec`

; skip or expect pass per env)`uv run ruff check src/guidellm/backends/openai/ src/guidellm/extras/audio.py tests/unit/backends/openai/`

## Related Issues

## Use of AI

`## WRITTEN BY AI ##`

)## git log

commit

f77f39eAuthor: Uri Shaket ushaket@redhat.com

Date: Mon May 4 10:08:55 2026 +0300

commit

78038d4Author: Uri Shaket ushaket@redhat.com

Date: Mon May 4 10:21:58 2026 +0300

commit

3afd7c5Author: Uri Shaket ushaket@redhat.com

Date: Mon May 4 10:37:19 2026 +0300

commit

e122e9cAuthor: Uri Shaket ushaket@redhat.com

Date: Mon May 4 17:25:03 2026 +0300

commit

1e2ab9bAuthor: Uri Shaket ushaket@redhat.com

Date: Mon May 4 17:25:14 2026 +0300

commit

51940e7Author: Uri Shaket ushaket@redhat.com

Date: Mon May 4 17:35:38 2026 +0300

commit

2dd7a63Author: Uri Shaket ushaket@redhat.com

Date: Mon May 4 17:35:47 2026 +0300

commit

ca21039Author: Uri Shaket ushaket@redhat.com

Date: Mon May 4 17:49:56 2026 +0300

commit

7e77e08Author: Uri Shaket ushaket@redhat.com

Date: Tue May 5 12:54:47 2026 +0300

commit

8bcc239Author: Uri Shaket ushaket@redhat.com

Date: Tue May 5 13:02:03 2026 +0300

commit

78e195bAuthor: Uri Shaket ushaket@redhat.com

Date: Tue May 5 13:23:55 2026 +0300

commit

c05c840Author: Uri Shaket ushaket@redhat.com

Date: Mon May 11 20:43:20 2026 +0300

commit

3a934f8Author: Uri Shaket ushaket@redhat.com

Date: Mon May 11 20:48:16 2026 +0300

commit

ff846ffAuthor: Uri Shaket ushaket@redhat.com

Date: Mon May 11 20:58:18 2026 +0300

commit

6cae2aaAuthor: Uri Shaket ushaket@redhat.com

Date: Mon May 11 21:30:19 2026 +0300

commit

d5e50c3Author: Uri Shaket ushaket@redhat.com

Date: Mon Jun 1 13:07:09 2026 +0300

commit

e1704f6Author: Uri Shaket ushaket@redhat.com

Date: Mon Jun 8 10:55:49 2026 +0300

commit

9c7f10eAuthor: Uri Shaket ushaket@redhat.com

Date: Mon Jun 8 11:21:50 2026 +0300

commit

97e0febAuthor: Uri Shaket ushaket@redhat.com

Date: Mon Jun 8 12:42:20 2026 +0300

commit

3b8434dAuthor: Uri Shaket ushaket@redhat.com

Date: Wed Jun 17 08:21:02 2026 +0300

Co-authored-by: Cursor cursoragent@cursor.com

Co-authored-by: Samuel Monson smonson@irbash.net

Signed-off-by: Uri Shaket ushaket@redhat.com