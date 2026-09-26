# [Issue #704] Display benchmark progress in non-interactive consoles

source: https://github.com/vllm-project/guidellm/issues/704
state: closed | updated: 2026-09-11T20:44:12Z
labels: priority-low, internal, feature

## 正文

### Problem Statement

When running GuideLLM in a non-interactive environment such as a K8s Pod there is no indication of benchmark progress until the entire run completes.

### Proposed Solution

Create a system for emitting status updates in non-interactive mode.

### Alternatives Considered

_No response_

### Usage Examples

```markdown

```

### Additional Context

_No response_

## 评论 (7)

### dbutenhof · 2026-04-22

Is this a duplicate of #518?

### sjmonson · 2026-04-22

Oh yes it is. I misinterpreted the original issue back when I responded to it. I assumed it was about getting a full live metrics readout. Rereading now I guess that is not the case.

### thameem-abbas · 2026-04-27

I wouldn't classify it as a duplicate. This is not about recording in a file. We should have some progress be displayed on the terminal at regular intervals. In cases where the benchmark is long -> multiple minutes, there is no visibility into the progression of the benchmark. Writing it to a file isn't very useful for observability without creating another layer to read and emit that. 

I think it would be ideal if we can emit some log at every 0.1 x benchmark load (duration or requests). I'm not sure how this could apply directly in multi-turn and a couple of complex scenarios. For a normal user though, this would help a lot. 

Another note is that most systems expect some progress for automation to understand that the benchmark is still alive. So this could also help with those systems

### dbutenhof · 2026-04-27

Perhaps. I think that, at least, there's a substantive overlap, which is what made me search for the existing "non-interactive feedback" issue when I saw this. It may be that we can look at this as a well-defined subset of the fairly loose scope of #518 ... in which case it would probably make sense to operate on this first and then expand/generalize.

### ardecode · 2026-07-23

Hey, I would like to take a crack at this one.

I spent some time reading through how progress works. `BenchmarkerProgress` in `benchmark/progress.py` is already an abstract base with the ifecycle hooks (on_initialize, on_benchmark_start, on_benchmark_update, on_benchmark_complete, on_finalize), and the current `GenerativeConsoleBenchmarkerProgress` is just the live version of it. So rather than touch the interactive path, I could add a second implementation alongside it.

The idea: a logging style progress tracker that emits a compact one line summary on an
interval instead of a live updating UI, something like:

    [sweep 2/7 · synchronous] running 42.3% | req/s=12.4 lat=0.81s conc=10.0 | TTFT=53ms ITL=8ms | ok=512 inc=0 err=1

One thing I noticed is that on_benchmark_update gets called on every request event in the
benchmarker loop, so this would need to throttle and only emit every N seconds (and always
on start/complete), otherwise it would flood the logs.

A few things I wanted to check before writing code:
- Should the output go through the loguru logger, or just print to the console directly?
- Would you rather this kick in automatically when there's no TTY, or be behind an explicit
  flag?
- For the interval, is a value in settings.py the right place, or would you prefer a CLI flag?

### dbutenhof · 2026-07-24

> A few things I wanted to check before writing code:
> 
> * Should the output go through the loguru logger, or just print to the console directly?

I'm not trying to "lay down a law" here, but expressing a speculative opinion ... I'd love to hear what others think. (And particularly from @sjmonson, who's on PTO this week.)

I think, from the requirements I've seen, that this should be text written ... somewhere. You can see the brief exchange in comments about the relationship to #518, which wants periodic status to a *file* that can be externally observed. That one seems to be interested in programmatic observation, so flushing structured JSON records might make sense, and I suppose structured loguru records would fit; but I don't think that's necessary and it definitely needs to be separate from the existing file-directed debug logging.

But for *this* PR, I think readable console text is more appropriate.

> * Would you rather this kick in automatically when there's no TTY, or be behind an explicit
>   flag?

Let's stick with an explicit option. Trying to second-guess from the environment usually doesn't work out well. How to structure that option, in combination with the console options we already have, is a trickier question. E.g., does this interact with/supersede `--disable-console` and/or `--disable-console-interactive`? I can see normal console logging being completely compatible with a file progress update ala #518, but certainly not with the console logging here -- so it probably forces `--disable-console-interactive` at least.

This is really sounding like a version of `GenerativeConsoleBenchmarkerProgress` that just dumps periodic updates to stdout rather than using the Rich console windowing package. And that might suggest a new `--console kind=(rich|simple)[,params...]` registry with `GenerativeConsoleBenchmarkerProgress` and something like `GenerativeSimpleBenchmarkerProgress` as discriminated subclasses, tapping into the registry mechanism. (The default would be `--console kind=rich` unless `--disable-console-interactive` was specified.)

> * For the interval, is a value in settings.py the right place, or would you prefer a CLI flag?

If, hypothetically, this were attacked as an alternate progress registry mechanism, the update interval would be a parameter, like `--console kind=simple,interval=10`. (In theory there could be a `path` also to direct the output somewhere other than `stdout`.)

### sjmonson · 2026-07-27

The idea I have floated in the past was to implement this as started logging and in interactive mode we add a new window in rich that carries logs. I just did some testing and unfortunately one of the complications is that worker processes would have to synchronize with the main thread to send log messages. I don't think that is worth the overhead so we might need to keep digging for ideas.
