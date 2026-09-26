# [Issue #260] Can I submit a python file with package dependencies ?

source: https://github.com/gpu-mode/kernelbot/issues/260
state: closed | updated: 2025-06-03T14:39:46Z
labels: 

## 正文

## Extend single file testing machenisam

I have developed a pytorch extension with a lot cuda functions.

So is it possible to let envrionment install this package from pypi and we use it as the test codes submitted from Discord gpu-mode /leaderboard command ?

## 评论 (1)

### msaroufim · 2025-04-25

Hi @yiakwy-xpu-ml-framework-team generally speaking it's easy to use `import pip` to download whatever you want inline although we strongly discourage this in the submission platform because it makes results not reproducible and security challenging

Could you please tell me more about your code looks like? Could you share something privately over DM so we can better understand how bad the situation is?
