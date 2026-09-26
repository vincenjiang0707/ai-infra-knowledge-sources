source: https://github.com/vllm-project/guidellm/pull/1143

# Fix mock-server Hugging Face tokenizer compatibility - #1143

Open

[tayoogunbiyi](https://github.com/tayoogunbiyi)wants to merge 6 commits into

Open

[tayoogunbiyi](https://github.com/tayoogunbiyi) wants to merge 6 commits into

[tayoogunbiyi](https://github.com/tayoogunbiyi)wants to merge 6 commits into

## Conversation

[tayoogunbiyi](https://github.com/tayoogunbiyi)marked this pull request as ready for review

September 12, 2026 13:00

Contributor

|
Hi |

[tayoogunbiyi](https://github.com/tayoogunbiyi)

[force-pushed](https://github.com/vllm-project/guidellm/compare/cb69099f9ad7a31202ba7cc028a0cfe071a71cef..56d747887540db91c7dec22a67336b9a604e310e)the fix/mock-server-huggingface-tokenizer branch from

[to](https://github.com/vllm-project/guidellm/commit/cb69099f9ad7a31202ba7cc028a0cfe071a71cef)

`cb69099`


`56d7478`

[Compare](https://github.com/vllm-project/guidellm/compare/cb69099f9ad7a31202ba7cc028a0cfe071a71cef..56d747887540db91c7dec22a67336b9a604e310e)

September 12, 2026 13:06

## Context Running the mock server with a Hugging Face tokenizer failed before the server started: ```bash uv run guidellm mock-server --processor Qwen/Qwen2.5-0.5B-Instruct ``` The command raised `NotImplementedError` from `PreTrainedTokenizer.get_vocab()`. The mock-server handlers were loading the configured processor through the PreTrainedTokenizer base class. This changes: - Uses `AutoTokenizer` to initialize configured processors in mock-server handlers. - Add an regression test covering mock-server initialization with tokenizer in MINIMAL_TOKENIZER_DIR ## Follow-up The mock server still calls `AutoTokenizer.from_pretrained` once for each of its four handlers and produces four tokenizer objects. Reducing this duplication can be handled in a separate commit. Signed-off-by: Tayo Ogunbiyi <eyitayoogunbiyi@gmail.com> Generated-by: Claude Opus 5

Signed-off-by: Tayo Ogunbiyi <eyitayoogunbiyi@gmail.com> Generated-by: Claude Opus 5

Signed-off-by: Tayo Ogunbiyi <eyitayoogunbiyi@gmail.com> Generated-by: Claude Opus 5

Signed-off-by: Tayo Ogunbiyi <eyitayoogunbiyi@gmail.com> Generated-by: Claude Opus 5

Signed-off-by: Tayo Ogunbiyi <eyitayoogunbiyi@gmail.com> Generated-by: Claude Opus 5

[tayoogunbiyi](https://github.com/tayoogunbiyi)

[force-pushed](https://github.com/vllm-project/guidellm/compare/56d747887540db91c7dec22a67336b9a604e310e..355a2a8e353e5e64584b3f5daf5d38404df0f329)the fix/mock-server-huggingface-tokenizer branch from

[to](https://github.com/vllm-project/guidellm/commit/56d747887540db91c7dec22a67336b9a604e310e)

`56d7478`


`355a2a8`

[Compare](https://github.com/vllm-project/guidellm/compare/56d747887540db91c7dec22a67336b9a604e310e..355a2a8e353e5e64584b3f5daf5d38404df0f329)

September 19, 2026 14:44

Use the existing subprocess fixture and health endpoint instead of constructing MockServer in the pytest process. This prevents forked server processes from inheriting a registered Sanic app and failing with a duplicate app name. Generated-by: OpenAI Codex Signed-off-by: Tayo Ogunbiyi <eyitayoogunbiyi@gmail.com>

### This branch has not been deployed

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

## Summary

Fix mock-server startup and request handling when

`--processor`

selects a real Hugging Face tokenizer. On upstream`main`

, initialization raises`NotImplementedError`

from`PreTrainedTokenizer.get_vocab()`

before the server can start. After startup is fixed, the handlers also need compatible chat-template calls and token counting, and generated text needs detokenization before being returned to clients.## Details

`AutoTokenizer.from_pretrained(...)`

in the chat completions, completions, and Responses handlers.`encode()`

, with the same interface supported by the mock tokenizer.Rebased onto upstream

`main`

at`4601968d`

(September 19, 2026). The tokenizer patch is unchanged by the rebase; the branch now also contains the already-merged logging fix from #1142.## Test Plan

Validated on macOS with Python 3.12.11:

`uv run tox -e tests -- tests/unit/mock_server tests/e2e/test_huggingface_tokenizer_offline.py`

:84 passed. Covers real-tokenizer startup, prompt/input usage for all three endpoints, decoded output chunks, existing mock-server behaviour, and offline tokenizer resolution.`uv run tox -e lint-check,type-check`

:passed, including type checks for 226 source files.`uv run tox -e tests`

:3,311 passed, 31 skipped, 188 xfailed. The run reported a Pydantic deprecation warning and a multiprocessing semaphore-cleanup warning at shutdown; tox exited successfully.Offline reproduction from the repository root, using the vendored tokenizer:

`uv run python -c 'from guidellm.mock_server.server import MockServer; from guidellm.schemas.mock_server.config import MockServerConfig; MockServer(MockServerConfig(processor="tests/fixtures/tokenizers/minimal"))'`

The initialization above fails on unmodified upstream

`4601968d`

with`NotImplementedError`

from`PreTrainedTokenizer.get_vocab()`

. The PR's initialization regression passes with the same tokenizer. No model download or inference server is required.## Related Issues

No linked issue. Related logging fix: #1142 (already merged).

## Use of AI

Claude Opus 5 assisted with the original implementation and tests; all five commits now include

`Generated-by: Claude Opus 5`

alongside their DCO sign-offs. Codex assisted with this rebase, validation, and PR-description update.## git log

commit

65b961aAuthor: Tayo Ogunbiyi eyitayoogunbiyi@gmail.com

Date: Fri Sep 11 17:41:54 2026 +0100

commit

53d4153Author: Tayo Ogunbiyi eyitayoogunbiyi@gmail.com

Date: Sat Sep 12 11:36:41 2026 +0100

commit

67da762Author: Tayo Ogunbiyi eyitayoogunbiyi@gmail.com

Date: Sat Sep 12 11:37:44 2026 +0100

commit

cee1840Author: Tayo Ogunbiyi eyitayoogunbiyi@gmail.com

Date: Sat Sep 12 13:25:05 2026 +0100

commit

355a2a8Author: Tayo Ogunbiyi eyitayoogunbiyi@gmail.com

Date: Sat Sep 12 13:58:56 2026 +0100

commit

70b4e33Author: Tayo Ogunbiyi eyitayoogunbiyi@gmail.com

Date: Sat Sep 19 16:54:10 2026 +0100

Generated-by: Claude Opus 5

Generated-by: OpenAI Codex

Signed-off-by: Tayo Ogunbiyi eyitayoogunbiyi@gmail.com