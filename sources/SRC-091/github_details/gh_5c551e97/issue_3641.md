# [Issue #3641] [Discussion][Feature] Add new store/prefetch policy options

source: https://github.com/LMCache/LMCache/issues/3641
state: closed | updated: 2026-09-22T02:23:11Z
labels: stale

## 正文

 ## Background

LMCache currently offers only limited policy choices for writing chunks to storage adapters (store) and for keeping prefetched chunks in the L1 runtime cache (prefetch).

  **Store side:** every newly computed chunk is asynchronously written to L2, both registered StorePolicies (`default`, `skip_l1`)  store all keys to adapters.

  **Prefetch side:** L1 retention of prefetched chunks is all-or-nothing , `default` drops everything after read (so hot prefixes are re-fetched from L2 on every request), `retain` keeps everything.

  ## Problems

  Write/read amplification and unnecessary I/O on the (often I/O-bound) L2 tier:

  1. Chunks that are never hit again even after are still written to L2.  Ideally we skip them,  at the cost of recomputing if they do show up later.
  2. Chunks that are hit frequently should be allowed to stay in L1 after prefetch, while cold ones should not,  they shall have different treatment.
  3. When the prefetch queue is overwhelmed, fetching from remote storage can take longer than simply recomputing.

  ## Proposed solutions

  1. **Gated store admission**: configurable , only write a chunk to L2 after it has been hit at least N (>=1) times.
  2. **Selective L1 retention**: same philosophy . only retain a prefetched chunk in L1 after it has been hit at least N (>=1) times.
     - (2b) For known-hot keys, we could additionally "pin" them in L1 and never evict. Note "pin" is already used in this project for a refcount, which is a different concept. 
     
  3. **Prefetch load shedding**: when the prefetch queue is too long, drop short hits and report them as misses (engine recomputes).

For frequency counting, a Count-Min Sketch is a common choice 

  ## Trade-offs

The philosophy behind this project is that loading is cheaper than recomputing, even for remote backends. These policies would violate that principle. (a little bit

  - For 1: extra recompute if hot chunks are evicted from L1 before being re-hit .
  - For 2: retained chunks occupy the L1 pool, which is shared with transfer buffers and may already be tight.
- For 3: shed hits are recomputed; only worthwhile when L2 is the bottleneck and GPU has headroom.

All policies would be opt-in; default behavior unchanged.

  ## Notes

  - 1 & 2 are well-established ideas (TinyLFU-style admission; S3FIFO, flash admission).
  - 2b exists in some KV-cache projects but the upside seems limited -- Probably won't do.
  - 3 likely only matters for industrial-scale deployments' edge cases. -- not sure shall we do this now


## 评论 (6)

### zhengfeihe · 2026-06-11

@sammshen 

I rethought on the discussion topic I tried to raise in this week’s meeting. I consolidated my thoughts a bit, it now looks more like an RFC though.

Please correct me if any of my thinking is wrong, and let me know whether you like the idea or not.

Thank you!


### yoo-kumaneko · 2026-06-21

Hmm, these are some solid suggestions. definitely worth a discussion.

### zhengfeihe · 2026-06-22

> Hmm, these are some solid suggestions. definitely worth a discussion.

@yoo-kumaneko 

Thank you for the comment. I guess I will make a implementation first and test it across different scenarios to see how much improvement we can actually get. Then we’ll have concrete results to discuss.

### yoo-kumaneko · 2026-06-22

> > Hmm, these are some solid suggestions. definitely worth a discussion.
> 
> [@yoo-kumaneko](https://github.com/yoo-kumaneko)
> 
> Thank you for the comment. I guess I will make a implementation first and test it across different scenarios to see how much improvement we can actually get. Then we’ll have concrete results to discuss.

sounds great. Feel free to find me on Slack or email me when you want a discussion.

### github-actions[bot] · 2026-08-22

This issue has been automatically marked as stale because it has not had activity within 60 days. It will be automatically closed if no further activity occurs within 30 days.

### github-actions[bot] · 2026-09-22

This issue has been automatically closed due to inactivity. Please feel free to reopen if you feel it is still relevant!
