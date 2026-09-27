# [Issue #2685] Deprecate: Pause control/cli

source: https://github.com/ModelCloud/GPTQModel/issues/2685
state: closed | updated: 2026-04-12T09:37:33Z
labels: 

## 正文

@avtc  I want to let you know before I actually do the refractor but right now I want to remove the `pause|resume` ui control from the lifecycle and instead replace it in the future with per module, per layer `callback` hooks that you can install/do whatever you want after each module/layer is about to start work or done quantization. That should cover this feature overlap and many others. 

## 评论 (3)

### avtc · 2026-04-08

Ok, I do not not how the UI will be integrated to have same or similar UX

### Qubitium · 2026-04-08

> Ok, I do not not how the UI will be integrated to have same or similar UX

In the future callback you can just idle block (so the callback never returns). Kind of like low cpu usage for loop that sleeps and wakes up every 100ms or 200ms to check for "p" button.  We can pass a logger arg to the callable so you have access to the logger and print to ui. LogBar is pretty powerful. 

### Qubitium · 2026-04-09

@avtc The only issue is that the callbacks do not fully resolve the problem of you need to capture keystrokes to trigger next-step pause state. So quant is running..and you need to do some UI to say, ok, I know you are doing work, but please pause at the next pausable point. 
