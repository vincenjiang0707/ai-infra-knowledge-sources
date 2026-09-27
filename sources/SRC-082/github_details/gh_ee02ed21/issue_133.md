# [Issue #133] 2 bit AWQ results?

source: https://github.com/mit-han-lab/llm-awq/issues/133
state: open | updated: 2025-02-20T07:15:57Z
labels: 

## 正文

Hi, do you have any 2 bit numbers for AWQ? I'm interested in seeing how AWQ holds up at low bitrates and it would be easy to adapt AWQ to 2 bit by just changing the codebook to 2 bits from 4. 

## 评论 (1)

### mattam301 · 2025-02-20

Hi, I am interested in that question too, since I have successfully reproduce int4 and int3 results in the paper, but when it came to int2, the ppl is totally broken of about 200,000
