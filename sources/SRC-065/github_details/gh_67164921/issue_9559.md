# [Issue #9559] Possibly a typo in WSDataPartition.cpp

source: https://github.com/triton-lang/triton/issues/9559
state: closed | updated: 2026-09-22T23:09:12Z
labels: bug

## 正文

### Describe the bug

Just reading through this part of code, based on the context, I think possibly a `!` is missing in this condition?
 
<img width="800" height="785" alt="Image" src="https://github.com/user-attachments/assets/02117dd3-c068-40bd-9f6a-b77d69fe6233" />

### Environment details

Latest triton commit in main branch

## 评论 (2)

### TBodyAltra · 2026-02-25

@htyu 

### htyu · 2026-02-25

Yes it is. Thanks for identifying that!
