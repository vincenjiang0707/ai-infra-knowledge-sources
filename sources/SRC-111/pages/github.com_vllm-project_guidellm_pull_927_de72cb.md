source: https://github.com/vllm-project/guidellm/pull/927

# Modernize benchmark from-file - #927

## Conversation


**previously approved these changes**

[jaredoconnell](https://github.com/jaredoconnell)Jul 13, 2026

###
**
**[jaredoconnell](https://github.com/jaredoconnell)
left a comment

**left a comment**

[jaredoconnell](https://github.com/jaredoconnell)

There was a problem hiding this comment.

It works well. One thing to consider is that it overwrites the old benchmark, which is fine, but if there is ever a bug in it then it could corrupt the results file.

|
Queued — the merge queue status continues in |

Certainly true -- but not new. I had a couple of ideas along the way that I decided not to pursue, but I'm not sure any of it makes much sense. The user controls the output file, and if they don't want to overwrite the input on |


**approved these changes**

[SkiHatDuckie](https://github.com/SkiHatDuckie)Jul 14, 2026

###
**
**[SkiHatDuckie](https://github.com/SkiHatDuckie)
left a comment

**left a comment**

[SkiHatDuckie](https://github.com/SkiHatDuckie)

There was a problem hiding this comment.

Works for me as well. I wonder if it would be a good idea to fix the tests in test_benchmark_from_file_entrypoint.py at some point, so that manual testing isn't as necessary.

I hadn't actually noticed that there |

[pyproject.toml](https://github.com/vllm-project/guidellm/pull/927/files#diff-50c86b7ed8ac2cf95bd48334961bf0530cdc77b5a56f852c5c61b89d735fd711)


**previously approved these changes**

[jaredoconnell](https://github.com/jaredoconnell)Jul 14, 2026

###
**
**[jaredoconnell](https://github.com/jaredoconnell)
left a comment

**left a comment**

[jaredoconnell](https://github.com/jaredoconnell)

There was a problem hiding this comment.

I don't love the use of a new test dependency, but it's a test dependency. It seems okay.

What I find interesting is that we're doing similar things in product code. Possibly not directly in |


**approved these changes**

[SkiHatDuckie](https://github.com/SkiHatDuckie)Jul 15, 2026

Signed-off-by: David Butenhof <dbutenho@redhat.com>

Signed-off-by: David Butenhof <dbutenho@redhat.com>

Replace the disabled re-export tests with working code. Signed-off-by: David Butenhof <dbutenho@redhat.com>

Signed-off-by: David Butenhof <dbutenho@redhat.com>


**approved these changes**

[SkiHatDuckie](https://github.com/SkiHatDuckie)Jul 15, 2026


**approved these changes**

[jaredoconnell](https://github.com/jaredoconnell)Jul 15, 2026

|
|

## Merge Queue Status
This pull request spent ## Required conditions to merge
|

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

## Summary

Modernize

`guidellm benchmark from-file`

by adopting the full registry typed`--output`

style.## Details

The

`guidellm benchmark from-file`

command in 0.7.0`--output-formats console`

due to an attempt to inject a path`guidellm run`

Replace the old

`--output-formats`

with the modern`--output kind=<kind>,...`

style.## Test Plan

Manual command testing + tox

## Related Issues

`guidellm benchmark from-file`

crashes with`ValidationError`

when output includes`console`

format #925## Use of AI

## git log

commit

1ef3077Author: David Butenhof dbutenho@redhat.com

Date: Mon Jul 13 10:03:20 2026 -0400

commit

e35f0a8Author: David Butenhof dbutenho@redhat.com

Date: Mon Jul 13 12:33:42 2026 -0400

commit

49128acAuthor: David Butenhof dbutenho@redhat.com

Date: Tue Jul 14 15:32:14 2026 -0400

commit

bfd6e5dAuthor: David Butenhof dbutenho@redhat.com

Date: Wed Jul 15 14:48:14 2026 -0400

Signed-off-by: David Butenhof dbutenho@redhat.com