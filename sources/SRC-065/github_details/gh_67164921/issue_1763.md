# [Issue #1763] Recursion depth exceeded with large kernel

source: https://github.com/triton-lang/triton/issues/1763
state: closed | updated: 2026-09-18T18:23:03Z
labels: enhancement

## 正文

Hi team,

I generated a pretty large kernel (has ~370 arguments) and generates a long sequence of if statements and I get a recursion depth exceeded error while trying to compile it. 

[repro](https://gist.github.com/mlazos/458c43c86ccd8812e45b323e3e9a9227)

Increasing the depth/making the kernel smaller are workarounds I can try which will let me keep going, curious whether you think this is worth fixing.

## 评论 (5)

### Jokeren · 2023-06-09

You generated the kernel using inductor right? 

> get a recursion depth

A recursion in triton or inductor?

### mlazos · 2023-06-09

> You generated the kernel using inductor right? 
> 
> 
> 
> > get a recursion depth
> 
> 
> 
> A recursion in triton or inductor?

Oh wait lemme get the better stack trace, pretty sure it's in triton. Im an inductor dev so I'd fix it if it were in inductor ;) haha 

### mlazos · 2023-06-09

I just updated the repro above with an actual triton stack trace

### Jokeren · 2023-06-09

OK, I think we can improve triton a bit to handle this.

The take away is that it has nothing to do with the number of arguments. Instead, inductor can reduce the length of the kernel to get around, there are a lot of if/else statements that caused the problem.

### peterbell10 · 2026-09-18

Closing as won't fix. The better solution is to codegen an if-else tree that splits the search range. I believe inductor already does this.
