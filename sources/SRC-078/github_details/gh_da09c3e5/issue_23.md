# [Issue #23] Job Queue

source: https://github.com/gpu-mode/kernelbot/issues/23
state: closed | updated: 2025-07-24T05:14:10Z
labels: 

## 正文

I recently read @TimDettmers [thread on quantization scaling](https://x.com/Tim_Dettmers/status/1856338240099221674). Very inspiring. I think that this is the sort of research, research on how to do research, and popularizing the methods and results, is what's probably the highest impact right now.

I want to train a few thousand small models to rediscover scaling laws. I describe the problem [here](https://apaz-cli.github.io/blog/Hyperparameter_Heuristics.html). I think that the techniques can be figured out at small scale, before scaling up. But there is a sort of compute floor. You do need to be able to train thousands, perhaps tens of thousands of models before truly understanding how these things scale. And if better tooling is to exist, these experiments need to be done.

So, I'd like to use whatever spare GPU time is available. Doesn't matter if it takes a few months. This is a "set and forget" sort of thing. People who are doing perf benchmarking require fast iteration cycles, and their time is more important. But as far as I know, there's no way to prioritize one job over another.

Or maybe I should go get a compute sponsor, and this isn't the place to do it.

It might be possible to do this with github actions. I know next to nothing about Github actions. I don't know if there's an API that you can submit workflows through. But since the parameters of a job are dependent on the results of a previous one (in bayesian search or similar), the code needs somewhere to live.

I've never actually used traditional HPC job orchestration, but the lightning studios SDK is very good at this. You can actually just type something like
```py
s = Studio()
s.install_plugin("multi-machine-training")
jobs_plugin = s.installed_plugins["multi-machine-training"]

futures = [jobs_plugin.run(f"I={i} python script.py", Machine.A10G) for i in range(n_jobs)]
```

This does what you would expect it to. I don't need quite this level of control, or even any control over what hardware I'm running on, but I would like some level of programmatic ability to submit jobs to a queue and wait for them.

So, let me know if you know a way to implement this with github actions, or write a queue from scratch, or if I should look for a sponsor.


## 评论 (2)

### msaroufim · 2024-11-15

So I do like the idea of a "keep the gpus warm job" that's useful - with github actions you can indeed trigger jobs from code without making a commit and you can skim `discord-bot.py` as an example

One reason why I picked Github actions (beyond just being familiar with them) is that it's quite easy for me to hook up any GPU a sponsor might offer. Whereas if I'm using some SDK then I lose that control. Granted I'm sure there's better ways of doing this but it was just the fastest thing I could think about

### apaz-cli · 2024-11-16

@msaroufim Yeah, I don't think there's any one standardized way of controlling compute clusters. Except for slurm, but not everybody even supports slurm, and it's not particularly fun to use by default. So I have no moral objections to a wrapper over github actions.

Do you think I should try to implement a job queue in the bot? When a user submits a train.py it would check the status of the running pipeline. If it's one of the "keep warm" jobs it would immediately submit the job with `cancel-in-progress: true`. If it isn't, it would add it to the queue and asynchronously submit once the previous job is done.

Interestingly, github actions only allows there to be one `pending` job at a time. Otherwise it gets skipped. Yay github actions. We couldn't use it as a job queue if we tried. But we could write one and use it to submit things one at a time per machine.

