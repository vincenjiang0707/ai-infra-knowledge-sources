source: https://github.com/vllm-project/guidellm/pull/783

# Fix report serialization for nested paths - #783

Merged

[mergify[bot]](https://github.com/mergify[bot])merged 1 commit into

Merged

## Conversation

Assisted-by: Codex Signed-off-by: jinhyuk9714 <jinhyuk9714@gmail.com>


**approved these changes**

[sjmonson](https://github.com/sjmonson)Jun 9, 2026

###
**
**[sjmonson](https://github.com/sjmonson)
left a comment

**left a comment**

[sjmonson](https://github.com/sjmonson)
Collaborator


There was a problem hiding this comment.

Reading through the [documentation](https://pydantic.dev/docs/validation/latest/api/pydantic/base_model/#pydantic.BaseModel.model_dump(mode)) it seems like this should work.

Collaborator

|
|

Contributor

## Merge Queue Status
This pull request spent ## Required conditions to merge
|

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

## Summary

Fixes #781.

Benchmark report persistence currently dumps the report in Python mode, so nested

`Path`

values in benchmark args can remain as`PosixPath`

objects and break JSON output or emit unsafe YAML tags. This switches report persistence to Pydantic's JSON mode so nested path values are converted before writing JSON/YAML files.## Details

`model_dump(mode="json")`

before serializing benchmark reports.`json_file`

data paths and`output_dir`

path values in JSON and YAML report output.## Test Plan

`uv run pytest tests/unit/benchmark/test_serialized_output.py -k nested_paths`

`uv run pytest tests/unit/benchmark/test_serialized_output.py`

`uv run pytest tests/unit/benchmark`

`uv run ruff check src/guidellm/benchmark/schemas/generative/report.py tests/unit/benchmark/test_serialized_output.py && uv run ruff format --check src/guidellm/benchmark/schemas/generative/report.py tests/unit/benchmark/test_serialized_output.py`

`uv run tox -e test-unit -- tests/unit/benchmark/test_serialized_output.py -k nested_paths`

(failed before test collection in this local checkout because`.tox/test-unit/bin/python`

had no`pytest`

module installed).## Related Issues

## Use of AI

Note: I used Codex while preparing this change, reviewed the final diff, and ran the listed checks locally.

## git log

commit

3777733Author: jinhyuk9714 jinhyuk9714@gmail.com

Date: Wed Jun 10 00:15:40 2026 +0900

Assisted-by: Codex

Signed-off-by: jinhyuk9714 jinhyuk9714@gmail.com