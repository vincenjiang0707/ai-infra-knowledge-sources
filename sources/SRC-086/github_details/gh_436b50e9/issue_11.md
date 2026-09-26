# [Issue #11] AttributeError: module 'collections' has no attribute 'MutableMapping'

source: https://github.com/FasterDecoding/Medusa/issues/11
state: closed | updated: 2023-09-13T22:47:45Z
labels: 

## 正文

WHen I run `python -m medusa.inference.cli --model FasterDecoding/medusa-vicuna-13b-v1.3', I get `AttributeError: module 'collections' has no attribute 'MutableMapping'`

Seems like a fastchat related issue?
Using WSL python 3.11.5 in a n anaconda environment

## 评论 (2)

### leeyeehoo · 2023-09-13

I searched it and seems like [python version issue](https://stackoverflow.com/a/71902541). It happens when your python >= 3.10.

### beingPurple · 2023-09-13

ah thank you, I was overthinking it!
