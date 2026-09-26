source: https://github.com/vllm-project/guidellm/pull/906

# Support ShareGPT datasets - #906

[jaredoconnell](https://github.com/jaredoconnell)wants to merge 1 commit into

[jaredoconnell](https://github.com/jaredoconnell) wants to merge 1 commit into

[jaredoconnell](https://github.com/jaredoconnell)wants to merge 1 commit into

## Conversation

Generated-by: Cursor AI Claude Opus 4.6 Signed-off-by: Jared O'Connell <joconnel@redhat.com>


**requested changes**

[dbutenhof](https://github.com/dbutenhof)Jul 7, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)

There was a problem hiding this comment.

I've seen the unhandled errors when a dataset has splits we don't process -- it's ugly. I like the idea of assuming a default split, and "train" is certainly commin -- though I'm not sure all split datasets necessarily have a "train" split, and we should handle that case gracefully as long as we're trying to be graceful.

- I think we should handle this default unwrapping earlier, when we load the data -- basically, in the absence of
`load_kwargs.split=<name>`

(when we receive a split dataset) we should resolve it right there. - If "train" is not in the split keys, we could use an arbitrary split that
*does*exist or perhaps we should instead raise an error exception advising the user that they need to specify a split for that dataset.

[src/guidellm/data/preprocessors/mappers.py](https://github.com/vllm-project/guidellm/pull/906/files/613dc9a5839f461f3781bda9aca11e5c446ae887#diff-2099c62bd0e1315d94f5ca565b50198a0507b9f2818feba33fd14d29641e6deb)

| :return: A single Dataset or IterableDataset. | ||
| """ | ||
| if isinstance(dataset, DatasetDict | IterableDatasetDict): | ||
| if "train" in dataset: |

There was a problem hiding this comment.

This is great, although I suspect we should do this earlier when we first load the dataset. E.g., if you don't specify `load_kwargs.split=<name>`

on `--data`

, and the dataset *has* splits, apply this unwrapping right off rather than deferring it to here.

[src/guidellm/data/preprocessors/mappers.py](https://github.com/vllm-project/guidellm/pull/906/files/613dc9a5839f461f3781bda9aca11e5c446ae887#diff-2099c62bd0e1315d94f5ca565b50198a0507b9f2818feba33fd14d29641e6deb)

| return None | ||
|
|
||
| try: | ||
| parsed = json.loads(value) |

There was a problem hiding this comment.

Three separate methods using `json.loads`

-- can we avoid the duplication by consolidating some of these paths??


**reviewed**

[SkiHatDuckie](https://github.com/SkiHatDuckie)Jul 7, 2026


There was a problem hiding this comment.

I haven't ran anything yet, but I did take a look at the code involved in detecting/unwrapping JSON dictionary columns. Regardless of what we choose to do with the column mapper, it'll help to make the unwrapper as general-purpose as possible, so that it may hopefully be useful regardless of the situation it's called in.

Edit: In other words, I think the JSON unwrapper has potential to be it's own utility function(s).

[src/guidellm/data/preprocessors/mappers.py](https://github.com/vllm-project/guidellm/pull/906/files/613dc9a5839f461f3781bda9aca11e5c446ae887#diff-2099c62bd0e1315d94f5ca565b50198a0507b9f2818feba33fd14d29641e6deb)

| if len(dataset_columns) != 1: | ||
| return None | ||
|
|
||
| candidate = dataset_columns[0] |

There was a problem hiding this comment.

While this will work for ShareGPT, there's no guarantee that the column(s!) containing JSON-dicts in other dataset formats will be in the first column.

[src/guidellm/data/preprocessors/mappers.py](https://github.com/vllm-project/guidellm/pull/906/files/613dc9a5839f461f3781bda9aca11e5c446ae887#diff-2099c62bd0e1315d94f5ca565b50198a0507b9f2818feba33fd14d29641e6deb)

| if not base_match: | ||
| continue | ||
| # Fallback: if no matches found, try JSON unwrapping | ||
| if not matched: |

There was a problem hiding this comment.

This won't work as intended if some, but not all of the target columns are found before checking wrappers.

[src/guidellm/data/preprocessors/mappers.py](https://github.com/vllm-project/guidellm/pull/906/files/613dc9a5839f461f3781bda9aca11e5c446ae887#diff-2099c62bd0e1315d94f5ca565b50198a0507b9f2818feba33fd14d29641e6deb)

| When a dataset has no direct column matches but contains a single | ||
| JSON-string column, the inner keys of that JSON are used as virtual | ||
| column names and matching is retried. | ||
|
|

There was a problem hiding this comment.

If we wish to standardize the JSON unwrapper/detector for use across GuideLLM, we'll have to make as few assumptions about the location(s) of target columns as possible.

A future dataset might have multiple columns with JSON-wrapped dicts, for example.

### This branch has not been deployed

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

## Summary

Adds support for ShareGPT datasets. This is a format commonly used for tool call datasets.

These changes were pulled from my prior PR.

This change highlights some limitations of the current design, and as such I've put it in draft in case we decide to refactor the code. The current column mapper design results in two column mapping steps, basically.

## Details

## Test Plan

## Use of AI

## git log

commit

613dc9aAuthor: Jared O'Connell joconnel@redhat.com

Date: Mon Jul 6 18:05:25 2026 -0400

Generated-by: Cursor AI Claude Opus 4.6

Signed-off-by: Jared O'Connell joconnel@redhat.com