# [Issue #4325] [Q] Is it legal to fork after initialization?

source: https://github.com/openucx/ucx/issues/4325
state: closed | updated: 2026-07-17T11:35:30Z
labels: 

## 正文

After creating `ucp_context_h` and `ucp_worker_h`, is it legal to fork the process? If yes, what is the semantic? Is it as if they were created separately?

What about forking after calls to `ucp_ep_create()` and `ucp_listener_create()`?

cc @pentschev

## 评论 (6)

### yosefe · 2019-10-23

@madsbk it's OK to fork as long as no RDMA or UCX API are used in the child process

### madsbk · 2019-10-23

Thanks for the clarification!

### bistack · 2022-06-23

@yosefe Hi. Is it possible that chid process cleans up env and then re-connects new ucx RDMA connections?

### yosefe · 2022-06-23

> @yosefe Hi. Is it possible that chid process cleans up env and then re-connects new ucx RDMA connections?

it may work, but it's not officially supported/tested at the moment.

### bistack · 2022-06-23

@yosefe Thanks. We had tried once without success. A big problem was that we did not understand the ucx code. Is there some demo code? Maybe we could try second times.

### gsanchezgallegos · 2026-07-17

Any updates? What works for me was making the connections after fork. Trying to close the conections before forking did not work.
