source: https://github.com/vllm-project/guidellm/pull/816

# Switch BenchmarksArgs to BenchmarkScernario in output - #816

Merged

Merged

## Conversation

Fix serialized output exporting last BenchmarkArgs rather then BenchmarkScenario for the global config. Assisted-by: GitHub Copilot GPT-4.1 Signed-off-by: Samuel Monson <smonson@redhat.com>


**approved these changes**

[dbutenhof](https://github.com/dbutenhof)Jun 18, 2026

Collaborator
Author

|
|

Contributor

## Merge Queue Status
This pull request spent ## Required conditions to merge
|

[SkiHatDuckie](https://github.com/SkiHatDuckie)pushed a commit to SkiHatDuckie/guidellm that referenced this pull request

Jun 23, 2026

## Summary Fix serialized output exporting last BenchmarkArgs rather then BenchmarkScenario for the global config. --- - [x] "I certify that all code in this PR is my own, except as noted below." ## Use of AI - [ ] Includes code generated or substantially modified by an AI agent - [ ] Includes tests generated or substantially modified by an AI agent > NOTE: the `Generated-by` or `Assisted-by` trailers should be used in git commit messages when code or tests were generated or substantially modified by an AI agent, as described in the project's [`DEVELOPING.md`]([https://github.com/vllm-project/guidellm/blob/main/DEVELOPING.md]) file. --- # git log commit[Author: Samuel Monson <smonson@redhat.com> Date: Thu Jun 18 14:06:36 2026 -0400 Switch BenchmarksArgs to Scernario in output Fix serialized output exporting last BenchmarkArgs rather then BenchmarkScenario for the global config. Assisted-by: GitHub Copilot GPT-4.1 Signed-off-by: Samuel Monson <smonson@redhat.com> commit]8f5da02[Author: Samuel Monson <smonson@redhat.com> Date: Thu Jun 18 14:09:40 2026 -0400 Fix tests Assisted-by: GitHub Copilot GPT-4.1 Signed-off-by: Samuel Monson <smonson@redhat.com> --------- Assisted-by: GitHub Copilot GPT-4.1 Signed-off-by: Samuel Monson <smonson@redhat.com>]f546f97

[SkiHatDuckie](https://github.com/SkiHatDuckie)pushed a commit to SkiHatDuckie/guidellm that referenced this pull request

Jun 24, 2026

## Summary Fix serialized output exporting last BenchmarkArgs rather then BenchmarkScenario for the global config. --- - [x] "I certify that all code in this PR is my own, except as noted below." ## Use of AI - [ ] Includes code generated or substantially modified by an AI agent - [ ] Includes tests generated or substantially modified by an AI agent > NOTE: the `Generated-by` or `Assisted-by` trailers should be used in git commit messages when code or tests were generated or substantially modified by an AI agent, as described in the project's [`DEVELOPING.md`]([https://github.com/vllm-project/guidellm/blob/main/DEVELOPING.md]) file. --- # git log commit[Author: Samuel Monson <smonson@redhat.com> Date: Thu Jun 18 14:06:36 2026 -0400 Switch BenchmarksArgs to Scernario in output Fix serialized output exporting last BenchmarkArgs rather then BenchmarkScenario for the global config. Assisted-by: GitHub Copilot GPT-4.1 Signed-off-by: Samuel Monson <smonson@redhat.com> commit]8f5da02[Author: Samuel Monson <smonson@redhat.com> Date: Thu Jun 18 14:09:40 2026 -0400 Fix tests Assisted-by: GitHub Copilot GPT-4.1 Signed-off-by: Samuel Monson <smonson@redhat.com> --------- Assisted-by: GitHub Copilot GPT-4.1 Signed-off-by: Samuel Monson <smonson@redhat.com>]f546f97

[SkiHatDuckie](https://github.com/SkiHatDuckie)pushed a commit to SkiHatDuckie/guidellm that referenced this pull request

Jul 6, 2026

## Summary Fix serialized output exporting last BenchmarkArgs rather then BenchmarkScenario for the global config. --- - [x] "I certify that all code in this PR is my own, except as noted below." ## Use of AI - [ ] Includes code generated or substantially modified by an AI agent - [ ] Includes tests generated or substantially modified by an AI agent > NOTE: the `Generated-by` or `Assisted-by` trailers should be used in git commit messages when code or tests were generated or substantially modified by an AI agent, as described in the project's [`DEVELOPING.md`]([https://github.com/vllm-project/guidellm/blob/main/DEVELOPING.md]) file. --- # git log commit[Author: Samuel Monson <smonson@redhat.com> Date: Thu Jun 18 14:06:36 2026 -0400 Switch BenchmarksArgs to Scernario in output Fix serialized output exporting last BenchmarkArgs rather then BenchmarkScenario for the global config. Assisted-by: GitHub Copilot GPT-4.1 Signed-off-by: Samuel Monson <smonson@redhat.com> commit]8f5da02[Author: Samuel Monson <smonson@redhat.com> Date: Thu Jun 18 14:09:40 2026 -0400 Fix tests Assisted-by: GitHub Copilot GPT-4.1 Signed-off-by: Samuel Monson <smonson@redhat.com> --------- Assisted-by: GitHub Copilot GPT-4.1 Signed-off-by: Samuel Monson <smonson@redhat.com>]f546f97

6 tasks

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

## Summary

Fix serialized output exporting last BenchmarkArgs rather then BenchmarkScenario for the global config.

## Use of AI

## git log

commit

8f5da02Author: Samuel Monson smonson@redhat.com

Date: Thu Jun 18 14:06:36 2026 -0400

commit

f546f97Author: Samuel Monson smonson@redhat.com

Date: Thu Jun 18 14:09:40 2026 -0400

Assisted-by: GitHub Copilot GPT-4.1

Signed-off-by: Samuel Monson smonson@redhat.com