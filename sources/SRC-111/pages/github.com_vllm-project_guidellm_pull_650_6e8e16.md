source: https://github.com/vllm-project/guidellm/pull/650

# Require datasets 4.1.0 - #650

## Conversation

We previously had an unversioned dependency on datasets, and a recent report shows that GuideLLM is not compatible with versions of datasets prior to 3.1.0. Since the "audio" extra already depends on datasets 4.1.0 we know that works and it seems a reasonable target. Signed-off-by: David Butenhof <dbutenho@redhat.com>

|
Starting with ```
async def test_requeue_with_positive_delay(self, worker_instance):
"""Test requeueing with positive delay sleeps then appends to turns_queue.
### WRITTEN BY AI ###
"""
history = [("req1", "resp1")]
conversation = [("req2", RequestInfo(request_id="req2"))]
delay = 0.1
start = time.time()
await worker_instance._wait_then_requeue(history, conversation, delay)
elapsed = time.time() - start
# Should have slept for approximately the delay time
> assert elapsed >= delay
E assert 0.09976863861083984 >= 0.1
``` |

And ... that's what I get for mentioning this. |

I just filed an upstream issue |


**approved these changes**

[sjmonson](https://github.com/sjmonson)Mar 19, 2026

Interesting. It's requeuing too fast. I would expect a minimum to not be flaky because you'd only expect it to exceed the expected value. |

Ouch ... well, get used to occasional random CI failures until they (or we) do something about this. Your 2 PRs passed on the second try ... I had to retrigger this one 4 or 5 times before I got lucky. |

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

## Summary

Update Huggingface datasets dependency: unversioned dependency can break with an old previously installed datasets package.

## Details

We previously had an unversioned dependency on datasets, and a recent report shows that GuideLLM is not compatible with versions of datasets prior to 3.1.0.

Since the "audio" extra already depends on datasets 4.1.0 we know that works and it seems a reasonable target.

## Test Plan

## Related Issues

## Use of AI

`## WRITTEN BY AI ##`

)