# [Issue #80] About the number of messages chunked in IBGDA

source: https://github.com/deepseek-ai/DeepEP/issues/80
state: closed | updated: 2026-09-18T10:05:24Z
labels: 

## 正文

![Image](https://github.com/user-attachments/assets/16f9c42b-fdc2-42eb-ae9c-9fe9b8954909)
Why theoretically 3 for maximum?

## 评论 (2)

### LyricZhao · 2025-03-21

Assuming the message size (maximum ~KB level) is much smaller than the page size (i.e. `NVSHMEM_CUMEM_GRANULARITY`, normally very large >100 MB). So the worst case of getting local/remote key is, the message is splitted into two pages at local, two pages at remote, totally 3 pages.

e.g.

| chunk 0 --- | chunk 1 ------ | chunk 2 --------- |
| local page i | local page i + 1 ------------------ |
| remote page j ------------- | remote page j + 1 |

### LyricZhao · 2025-03-21

You can ignore that note as the while loop can proceed more than 3 chunks. But we tried some code simplication and optimizations here for the theretical maximum, but it didn't work.
