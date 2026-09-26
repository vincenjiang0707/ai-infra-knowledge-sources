source: https://github.com/vllm-project/guidellm/discussions/311

#
How can I reduce `synchronous`

testing time with `--rate-type=sweep`

?
#311

Unanswered

[psydok](https://github.com/psydok)asked this question in

[User Support](https://github.com/vllm-project/guidellm/discussions/categories/user-support)

## Replies: 2 comments

|
We have some in-progress plans on auto-stopping based on metric convergence but its probably at least a few months out. One option is to specify a max-seconds that is large enough to allow 100 requests to complete in other runs e.g. |

0 replies

|
But for other tests, max-seconds of 10 is very small value... |

0 replies

## Uh oh!

There was an error while loading. Please reload this page.

## Uh oh!

There was an error while loading. Please reload this page.

When using sweep, it takes a lot of time for the first test (synchronous), despite the fact that the values (latency, ttft, etc) do not change much.

For other tests, less than 100 requests are unuseful.

## All reactions