# [Issue #38] fail to run examples/offline.py, load model weight error.

source: https://github.com/LLMServe/DistServe/issues/38
state: closed | updated: 2024-08-13T06:15:24Z
labels: 

## 正文

below image shows the error detail.

![image](https://github.com/user-attachments/assets/3c5fc072-1c35-4a5c-a007-a2762d55883b)


I predownload and cache model weights on disk. then load offline. how to solve this problem?

## 评论 (3)

### Youhe-Jiang · 2024-08-12

Maybe you can check issue #35 for detailed solution, it works for me.

### ddqspace-xyz · 2024-08-13

thanks a lot. It works! 

### ddqspace-xyz · 2024-08-13

<img width="668" alt="1723529680690" src="https://github.com/user-attachments/assets/e9aeaaa6-cf8a-47dd-8dfa-335454037314">

/distserve/downloader/downloader.py

here is my code. hope it can help others.
