# [Issue #48] Leaderboard Creation and Submission Flow

source: https://github.com/gpu-mode/kernelbot/issues/48
state: closed | updated: 2025-03-01T05:06:44Z
labels: documentation

## 正文

There are a few components of the leaderboard that we need to converge on as a team. Specifically, what exactly entails a "leaderboard problem", how this is stored in the DB, and what this looks like to the problem creator and problem submitter. This is an open doc, so feel free to modify or provide feedback on any desired changes.

We also need to figure out how runners (e.g. modal vs. GitHub actions) factor into the leaderboard. Currently, you can use either runner to submit to the leaderboard, but it's unclear whether they will lead to performance differences. I'm not sure how we should factor this in, because in theory the choice of runners should not be affecting kernel performance. I personally think we should fix a runner for the leaderboard / not allow submitting to multiple different runners for the same leaderboard.

CC: @S1ro1 @b9r5 @msaroufim 

## Leaderboard Creation
The general leaderboard creation scheme should include a unique leaderboard ID / name, a leaderboard deadline, and reference code that contains a 1) input data generators with fixed shapes, 2) reference code for the kernel, 3) a verifier function that checks the user submission against the reference code, and 4) a function `metric()` that gets called to verify (using 3) and evaluate the runtime of the user submitted kernel. It is currently the responsibility of the problem creator to provide this reference code. The problem writer also needs to specify a metric(s) (e.g. runtime, peak activation memory) that they care about -- this unfortunately has not been implemented, and is just abstracted as a "score" currently. [@S1ro1 @b9r5 We should sync on this.]

@msaroufim Not sure what you had in mind, but we also shouldn't allow arbitrary users to just create leaderboards, at least for the main channel because of spam. There should be some kind of simple / quick verification process on our end.

Current proposed command: `/leaderboard create [leaderboard_name] [deadline] [reference code]`
> Each leaderboard problem with `leaderboard_name` should be inherently associated / tied to a `GPU_type` and a `dtype`. Currently, @b9r5 and I agree that the leaderboard creator should only have to specify the `leaderboard_name`, and all `GPU_type` and a `dtype` information is populated when a user submits to the leaderboard. In other words, every leaderboard implicitly also contains separate categories for each combination of (`GPU_type`, `dtype`), which are populated when the first user submits to this leaderboard.

Alternative command 1: `/leaderboard create [leaderboard_name] [list of gpu_types] [list of dtypes] [deadline] [reference code]`
> Here, we restrict the the leaderboard to only have a list of available GPU types and a list of available dtypes. So if `[list of gpus]` is {T4, A100}, and a leaderboard submits an H100 job, the runner should just deny this submission.

Alternative command 2: `/leaderboard create [leaderboard_name] [gpu_type] [dtype] [deadline] [reference code]`
> In this setting, the leaderboard creator must create a unique problem leaderboard for every GPU and every dtype that they want to test for. If we believe leaderboards have to be this fine-grained, then this is a plausible method, but I personally think this is quite tedious because the reference code is generally GPU and dtype agnostic.

## Leaderboard Submission
Current proposed command: `/leaderboard submit [runner] [leaderboard_name] [gpu_type] [dtype] [script]`
> A big restriction in leaderboard submissions is that the script has to follow a specific format (e.g. it needs to define a function named `train()`) so the reference code can handle it. Because the problem writer creates the reference code, the submission specifications are per leaderboard. If for whatever reason a score (e.g. runtime) is not produced, the runner should not error out -- instead, it will just not write to the database.

Note on `score`. Currently, the meaning and computation of a score is all based on the reference code that a leaderboard creator provides. We don't have a good way of scraping this information for the runners right now, so this is also an important TODO for someone to figure out. Right now, we print out a `score: {score:.f}` and look for this pattern in the logs to extract the final score. This is obviously hackable and should not be the final solution.

## Leaderboard Display
Currently, the leaderboard display just spits out the top "scores". We can either have the leaderboard spit out the scores (e.g. Wall-clock speed) for a specific GPU type and dtype, or for all available GPU types and dtypes of a particular leaderboard name. 

Current proposed command: `/leaderboard show [leaderboard_name] [gpu_type] [dtype]`
> The only issue is the user has to know beforehand what what GPU types and dtypes are available for a particular leaderboard_name beforehand. We can discuss in more detail how this will work.

## Leaderboard List
We also want to list / provide users with a list of all available leaderboards. TBD

Current proposed command: `/leaderboard list`


## 评论 (4)

### msaroufim · 2024-12-12

Some quick thoughts
1. For the launch we should fix Modal as our primary runner, I'd want us to actually measure small differences between vendors in practice though so we can have some sense of the percentage differences for runtime if any. There's some common issues that pop up like for example the overhead of containerization and power settings that can have a big impact. That said we can use other schedulers IF for that leaderboard no other scheduler is used so there's no mix and matching. I'm also hoping we can do things like consumer GPU deployments and Modal doesn't support a bring your own GPU kind of setup
2. Ideally we'd want problem submittors to submit reference code and correctness checks, we could also potentially by default have the correctness check be an allclose from the reference kernel stdout. I'd make the same argument for peak vram, we can just measure that for people and report it. Some metrics won't make sense as top level ranking metrics like for peak vram you can game it by putting the model on CPU and then we'll get into the business of a weighted sum of metrics and that's all very bleh, to keep things focused we just focus on: is the code correct, and is the code faster than the reference kernel
3. Regarding spam submissions of kernels: we could do this in steps, basically when a new kernel gets submitted, we get some notification, we review it and if it looks good we approve, I'm not looking forward to meme submissions here lol
4. I don't think dtype should be an explicit thing people submit, that's kind of a detail for the reference check, GPU type indeed is probably the most important aspect
5. I'd be fine with not allowing list inputs, you can generate multiple variants using some simple bash script
6. Score should be for now, time it takes to run the code, and we should not rely on custom instrumentation for this, we should always run timings ourselves
7. for leaderboard show, we should just have a long name that uniqueley determines what something is so you could do `leaderboard list` and then `leaderboard show softmax_fp8_v100`

### S1ro1 · 2024-12-12

**Runners**: I feel like runners would have a lot of impact on the performance, as well as there might be different GPUs per runner, I would be open to have leaderboard per (GPU x Runner)

**Leaderboard definition**: I mostly agree with what you wrote, however as Mark said, I'd scratch dtype, should have it defined by the example input. 
I'd go with leaderboard being explicitly defined across all GPUs, resp. all (GPUs x Runners), there's no harm in that for anyone involved, to be able to submit code to different types of runners. The leaderboard creator can just choose which kernels are relevant to his problem and only take those as valid, i.e. by just doing `/leaderboard show [leaderboard_name] [gpu_name]`

**Auth**: Maybe I'm just naive, but I'd try going with like a Discord role that we just give to people for now when they ask for it, granted we need some Admin utils (i.e. `/leaderboard delete {id}`. In case this doesn't work, we can just go with accepting submissions.

**Score**: I think score should be run time for now, we can also add a column to the DB, something like "user_defined_score" and that would be extracted in a way similar to current, but would be optional.

### b9r5 · 2024-12-13

One thing I have wondered (but it is somewhat off-topic at this stage) is whether we should allow multiple runs per (user, problem) combination, and if so how we determine the score.

I could imagine that someone puts a lot of work into making a fast kernel (and has something riding on the result, like a prize or whatever), but gets unlucky because the machine they get in Modal is running hot and is underclocked. I don't know if that exact scenario can occur, but surely some operational condition could cause the performance to fall below expected performance. And conversely, someone else could get lucky and have better than expected performance on a kernel that is not optimal. 

To ameliorate such situations we might consider (and perhaps you've already considered) allowing multiple runs per combination of user and problem. If we do that, we'd have to think about how to determine the score. If you buy the above reasoning, min and max of the list of scores are bad choices; but median or perhaps average could be good choices.

### alexzhang13 · 2024-12-13

> for leaderboard show, we should just have a long name that uniquely determines what something is so you could do leaderboard list and then leaderboard show softmax_fp8_v100

In the case of `/leaderboard list`, would we show something like `softmax_fp8   ...   [t4, v100, a100]`?

> Auth: Maybe I'm just naive, but I'd try going with like a Discord role that we just give to people for now when they ask for it, granted we need some Admin utils (i.e. /leaderboard delete {id}. In case this doesn't work, we can just go with accepting submissions

So I think when we run a competition this isn't a concern at all and we should be the ones proofreading and verifying each leaderboard. However, in the general case (e.g. we want this to permanently be on GPU mode as a channel or thing for people to do) then I think the best thing to do is to have maintainers that can accept new competitions, but Mark should probably be the final decider on this because it's his Discord.

> could imagine that someone puts a lot of work into making a fast kernel (and has something riding on the result, like a prize or whatever), but gets unlucky because the machine they get in Modal is running hot and is underclocked. I don't know if that exact scenario can occur, but surely some operational condition could cause the performance to fall below expected performance. And conversely, someone else could get lucky and have better than expected performance on a kernel that is not optimal.

This is a very fair point. In general, I think a user should be allowed to have unlimited submissions for a specific kernel, and the hope is that the reference code should reduce variance by capturing runtime averaged over many runs.

The alternative @b9r5 which I think might be cool is to have a public leaderboard (this is just for the competition) that basically has immediate scores, but the final standings are actually determined after we re-run all of the submissions at the very end. The idea being it should in theory get rid of variance in machine stability, but idk this was just a thought.
