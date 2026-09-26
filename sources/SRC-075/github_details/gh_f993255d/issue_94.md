# [Issue #94] Would there be a potential Mojo Support

source: https://github.com/ScalingIntelligence/KernelBench/issues/94
state: open | updated: 2025-12-22T16:01:30Z
labels: 

## 正文

Hi Team, 

First of all thanks for the incredible work, you folks are putting out. 

Just was wondering if there are any plans in adding support for mojo, as it is getting quite performant especially for gpu programming. 

Also more than happy to see if i can contribute on bringing this, if the backend addition is straight forward or needs a bit of change in approach. 

Thanks in advance!

## 评论 (4)

### simonguozirui · 2025-11-19

Hi @rajuptvs thank you for reaching out! Indeed we found Mojo quite intersting (haven't had too much time to play around with it yet). I can add Mojo on the near roadmap.

@nathanjpaek has been leading a lot of the DSL support (we have added `cute`, `triton`, and `tilelang` so far, there are so many DSLs!). Check out some of the PRs we did for different DSLs (#35 #80) as reference, feel free to start a PR on that and the team can work with it. We basically need a sample prompt and a backend logic for eval if it is any different from the current inline approach. 


### rajuptvs · 2025-12-01

> Hi [@rajuptvs](https://github.com/rajuptvs) thank you for reaching out! Indeed we found Mojo quite intersting (haven't had too much time to play around with it yet). I can add Mojo on the near roadmap.
> 
> [@nathanjpaek](https://github.com/nathanjpaek) has been leading a lot of the DSL support (we have added `cute`, `triton`, and `tilelang` so far, there are so many DSLs!). Check out some of the PRs we did for different DSLs ([#35](https://github.com/ScalingIntelligence/KernelBench/pull/35) [#80](https://github.com/ScalingIntelligence/KernelBench/pull/80)) as reference, feel free to start a PR on that and the team can work with it. We basically need a sample prompt and a backend logic for eval if it is any different from the current inline approach.

Thanks for that.. will probably try to get started with a PR shortly as suggested above. 

### simonguozirui · 2025-12-03

Awesome, let us know! Would be curious to see what Mojo format would be like. Let me know if you want to discuss with the team (@nathanjpaek, Willy, and I, etc) on how backend implementation should look. 

### rajuptvs · 2025-12-22

hi @simonguozirui, that sounds awesome, it would be great if i could discuss how the backend might look like. 
