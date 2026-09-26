# [Issue #153] Support dstack scheduler

source: https://github.com/gpu-mode/kernelbot/issues/153
state: closed | updated: 2025-06-26T20:27:13Z
labels: 

## 正文

I wonder if you’d be interested in supporting [dstack](https://github.com/dstackai/dstack) as a scheduler—a lightweight, streamlined alternative to K8s/Slurm, focused on GPUs. It supports most clouds (including cost-effective providers) and works easily with any on-prem servers.

If needed, dstack can also be used with [dstack Sky](https://dstack.ai/#get-started)—dstack’s own marketplace offering affordable compute from multiple providers.
I’m a core member of the team, and if you integrate it, we’d be happy to support you with some compute credits.

## 评论 (4)

### msaroufim · 2025-02-04

Hi @peterschmidt85! We're always looking for more credits and easy schedulers, do you mind if we chat more about this on our Discord? https://discord.gg/keekPwuK

Basically right now one of our real problems is we can't super easily integrate into traditional non serverless cloud vendors because we've punted on capacity planning

### peterschmidt85 · 2025-02-05

@msaroufim Joined the Discord, happy to chat! dstack offers containers all the way, so that's why I see there a fit

### peterschmidt85 · 2025-06-26

@msaroufim Is this still relevant? Need help with this?

### msaroufim · 2025-06-26

Hey @peterschmidt85 not yet! We've abused GitHub actions enough that it solves most of our needs 
