# [Issue #2963] Ruler QA tasks do not work for `max_seq_lengths` < 4096

source: https://github.com/EleutherAI/lm-evaluation-harness/issues/2963
state: closed | updated: 2026-08-27T18:14:55Z
labels: bug, good first issue

## 正文

when `max_seq_lengths` is set to 2048, the program will hang on a `while true` loop forever.  4096 or beyond works normally

## 评论 (11)

### mdciofalo · 2025-07-04

Hi! If no one is currently working on this issue, I’d love to take a look and see how I can contribute. Let me know if there are any guidelines or preferred approaches I should follow. Thanks!

### Andy0422 · 2025-09-05

> when `max_seq_lengths` is set to 2048, the program will hang on a `while true` loop forever. 4096 or beyond works normally

Yes, 4096 is the shortest length in RULER.

### vnayakde · 2025-10-12



Hi! I'd like to work on this issue if it's still open.
Could you please assign me? I'll begin by reproducing the bug for `max_seq_length < 4096` and then investigate the cause of the infinite loop.

 Also, if possible, could you please point me to the file or section of the code where the Ruler QA logic is implemented? That would help me get started more efficiently.

 @baberabb @sustcsonglin 




### baberabb · 2025-10-14

> Hi! I'd like to work on this issue if it's still open. Could you please assign me? I'll begin by reproducing the bug for `max_seq_length < 4096` and then investigate the cause of the infinite loop.
> 
> Also, if possible, could you please point me to the file or section of the code where the Ruler QA logic is implemented? That would help me get started more efficiently.
> 
> [@baberabb](https://github.com/baberabb) [@sustcsonglin](https://github.com/sustcsonglin)

Hi! thanks for your interest! It's in this [script](https://github.com/EleutherAI/lm-evaluation-harness/blob/main/lm_eval/tasks/ruler/prepare_niah.py), which is in turn mostly copied from the original [RULER](https://github.com/NVIDIA/RULER) repo

### vnayakde · 2025-10-14

thank you for assigning me this issue , i will be working on it from now on.

### vnayakde · 2025-10-26



Hi @baberabb,

 I’m really sorry for the delay in my contributions — I was a bit unwell in between.

 I’ve now gone through the code thoroughly and understood the underlying issue. I’ve implemented a safety check to prevent the infinite loop when `max_seq_length  <4096`.

 The only challenge I’m facing right now is that installing the full dependencies via `pip install lm_eval[dev]` is quite large and heavy for my current setup.

 Would it be okay if I just push the code changes and open a pull request for you to test on your end? Or is there a lighter way I can locally test my changes without setting up the full environment?

 Thanks for your patience and understanding!



### vnayakde · 2025-10-26

@baberabb I ran the command

```bash
pytest lm_eval/tasks/ruler/test_prepare_niah_local.py -s -vv
```

as mentioned in the [contribution guidelines](https://github.com/EleutherAI/lm-evaluation-harness/blob/main/docs/CONTRIBUTING.md), and it completed successfully without entering any infinite loop.

Does this confirm that my changes are working correctly?
If so, should I go ahead and open a pull request accordingly?


### vnayakde · 2025-10-27

@baberabb @sustcsonglin can anybody please verify my task it would be very helpful 

### baberabb · 2025-10-27

> Hi [@baberabb](https://github.com/baberabb),
> 
> I’m really sorry for the delay in my contributions — I was a bit unwell in between.
> 
> I’ve now gone through the code thoroughly and understood the underlying issue. I’ve implemented a safety check to prevent the infinite loop when `max_seq_length <4096`.
> 
> The only challenge I’m facing right now is that installing the full dependencies via `pip install lm_eval[dev]` is quite large and heavy for my current setup.
> 
> Would it be okay if I just push the code changes and open a pull request for you to test on your end? Or is there a lighter way I can locally test my changes without setting up the full environment?
> 
> Thanks for your patience and understanding!

Hi! Thanks for looking into this! And yeah, would be great if you can PR, and I'll review.

### vnayakde · 2025-10-28

@baberabb hello sir i have just created the PR #3372 , can you please check it . Please do tell me if there is any issues.

### vnayakde · 2025-10-29

@baberabb sir can you please verify my PR.
