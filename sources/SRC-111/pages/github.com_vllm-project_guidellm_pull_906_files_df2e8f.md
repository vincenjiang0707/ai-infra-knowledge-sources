source: https://github.com/vllm-project/guidellm/pull/906/files

-
[Notifications](https://github.com/login?return_to=%2Fvllm-project%2Fguidellm)You must be signed in to change notification settings -
[Fork 238](https://github.com/login?return_to=%2Fvllm-project%2Fguidellm)

# Support ShareGPT datasets #906

## New issue

**Have a question about this project?** Sign up for a free GitHub account to open an issue and contact its maintainers and the community.

By clicking “Sign up for GitHub”, you agree to our [terms of service](https://docs.github.com/terms) and
[privacy statement](https://docs.github.com/privacy). We’ll occasionally send you account related emails.

Already on GitHub?
[Sign in](https://github.com/login?return_to=%2Fvllm-project%2Fguidellm%2Fissues%2Fnew%2Fchoose)
to your account

[jaredoconnell](https://github.com/jaredoconnell)wants to merge 1 commit into

[vllm-project:main](https://github.com/vllm-project/guidellm/tree/main)

##
*base:*
main

**{{ refName }}**

### Are you sure you want to change the base?

[jaredoconnell:feat/sharegpt-dataset-support](https://github.com/jaredoconnell/guidellm/tree/feat/sharegpt-dataset-support)

## Changes from **all commits**

##
**
File filter
**

### Filter by extension

## **Conversations**

## **Jump to**

##### Diff view

##### Diff view

## There are no files selected for viewing

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

| Original file line number | Diff line number | Diff line change |
|---|---|---|
| @@ -1,10 +1,11 @@ | ||
| from __future__ import annotations | ||
|
|
||
| import json | ||
| import re | ||
| from collections import defaultdict | ||
| from typing import Any, ClassVar, Literal, TypeAlias, cast | ||
|
|
||
| from datasets import Dataset, IterableDataset | ||
| from datasets import Dataset, DatasetDict, IterableDataset, IterableDatasetDict | ||
| from pydantic import Field | ||
|
|
||
| from guidellm.data.preprocessors.preprocessor import ( | ||
|
|

There was a problem hiding this comment.

### Choose a reason for hiding this comment

The reason will be displayed to describe this comment to others. [Learn more](https://docs.github.com/articles/managing-disruptive-comments/#hiding-a-comment).

While this will work for ShareGPT, there's no guarantee that the column(s!) containing JSON-dicts in other dataset formats will be in the first column.

There was a problem hiding this comment.

### Choose a reason for hiding this comment

The reason will be displayed to describe this comment to others. [Learn more](https://docs.github.com/articles/managing-disruptive-comments/#hiding-a-comment).

Three separate methods using `json.loads`

-- can we avoid the duplication by consolidating some of these paths??

There was a problem hiding this comment.

### Choose a reason for hiding this comment

The reason will be displayed to describe this comment to others. [Learn more](https://docs.github.com/articles/managing-disruptive-comments/#hiding-a-comment).

If we wish to standardize the JSON unwrapper/detector for use across GuideLLM, we'll have to make as few assumptions about the location(s) of target columns as possible.

A future dataset might have multiple columns with JSON-wrapped dicts, for example.

There was a problem hiding this comment.

### Choose a reason for hiding this comment

The reason will be displayed to describe this comment to others. [Learn more](https://docs.github.com/articles/managing-disruptive-comments/#hiding-a-comment).

This won't work as intended if some, but not all of the target columns are found before checking wrappers.

dbutenhofThere was a problem hiding this comment.

## Choose a reason for hiding this comment

The reason will be displayed to describe this comment to others. Learn more.

This is great, although I suspect we should do this earlier when we first load the dataset. E.g., if you don't specify

`load_kwargs.split=<name>`

on`--data`

, and the datasethassplits, apply this unwrapping right off rather than deferring it to here.