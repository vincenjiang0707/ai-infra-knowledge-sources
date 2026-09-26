# [Issue #36] [New feature] Fine-tune Medusa heads during SFT

source: https://github.com/FasterDecoding/Medusa/issues/36
state: closed | updated: 2024-01-24T13:58:34Z
labels: enhancement

## 正文

(empty)

## 评论 (4)

### santhosh97 · 2023-09-19

What does this exactly mean? Does this mean training all the parameters including the original model (unfreezing the original model) parameters + medusa heads from scratch?

### ctlllll · 2023-09-19

> What does this exactly mean? Does this mean training all the parameters including the original model (unfreezing the original model) parameters + medusa heads from scratch?

Ah yes. I'll make it clearer, thanks!

### ctlllll · 2023-10-09

Track:
I added initial support for Medusa to the popular fine-tuning codebase.
See commit: https://github.com/ctlllll/axolotl

### ctlllll · 2024-01-24

Added in v1.0.
