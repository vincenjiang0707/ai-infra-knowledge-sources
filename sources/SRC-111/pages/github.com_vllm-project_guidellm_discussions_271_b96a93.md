source: https://github.com/vllm-project/guidellm/discussions/271

# Different benchmark results when comparing instruments. What should I trust and why? #271

## Replies: 1 comment

|
I configured the tests little differently. |

0 replies

|
I configured the tests little differently. |

## Uh oh!

There was an error while loading. Please reload this page.

## Uh oh!

There was an error while loading. Please reload this page.

I am comparing

`vllm/benchmarks/benchmark_serving.py`

with`guidellm benchmark`

. I get different RPS and Ouput TPS under the same scenarios. But to run the guidellm test, I had to increase the max_seconds from 60 seconds to 300 seconds.- Can you tell me, please, do you have any idea why this might be? And how to fix it? As if there shouldn't be such a difference (about 10 RPS and about 100 TPS).
- I also ran 2 different types of tests: sweep and concurrent. In the report, I see that the calculated metrics (TTFT, TPS, Time per request) for both cases are very different, despite the fact that the values turned out to be for the same RPS.

sweep:Perhaps I don't understand why the results are so different? Could you help me figure it out, please?

concurrent:

concurent seems to parse the results incorrectly. because table in console shows that ttft should be 89458.3ms at 0.5 rps.

## All reactions