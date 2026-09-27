# [Issue #669] [Performance] Question about performance of Deepep v2, the role of the prefer-overlap-with-compute parameter

source: https://github.com/deepseek-ai/DeepEP/issues/669
state: open | updated: 2026-07-27T09:11:54Z
labels: 

## 正文

I would like to ask, what are the execution commands for the performance of the two machines shown in the figure below, and do they need to include --prefer-overlap-with-compute 1 ? 

<img width="1695" height="1245" alt="Image" src="https://github.com/user-attachments/assets/307983c1-2c3e-42cc-ad7b-bf928a0bb814" />

I am not aligned with the official performance data in my local environment, and the following are the test results.
[1]python tests/elastic/test_ep.py --num-processes 8 --allow-hybrid-mode 1  --num-sms 12  --reuse-elastic-buffer --num-topk 8 --num-tokens 8192 -**-prefer-overlap-with-compute 1** --num-qps 65

<img width="2151" height="1509" alt="Image" src="https://github.com/user-attachments/assets/10e3af86-4ccf-48f9-aff2-25dfa5e47ab8" />

[2]python tests/elastic/test_ep.py --num-processes 8 --allow-hybrid-mode 1  --num-sms 12  --reuse-elastic-buffer --num-topk 8 --num-tokens 8192 -**-prefer-overlap-with-compute 0** --num-qps 65

<img width="2076" height="1497" alt="Image" src="https://github.com/user-attachments/assets/e9babbeb-96d8-49ab-8980-5cede77e5e5a" />

## 评论 (3)

### shenhongqian · 2026-06-22

Can you help me take a look at this issue? Thank you @sphish @LyricZhao 

### alpha-baby · 2026-06-23

maybe you could try SMs == 16 , and will Improve the performance of combine

### kzlxd · 2026-07-27

@shenhongqian --prefer-overlap-with-compute 1 is necessary
