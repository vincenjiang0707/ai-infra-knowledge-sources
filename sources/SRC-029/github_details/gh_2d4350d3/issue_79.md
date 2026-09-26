# [Issue #79] Support I/O with text and token ids

source: https://github.com/AI-Hypercomputer/JetStream/issues/79
state: closed | updated: 2024-05-14T23:11:25Z
labels: 

## 正文

- Customer request: We use multiple languages for clients and cannot implement detokenization in each one. Need to have server-side detokenization support.


## 评论 (2)

### kiratp · 2024-05-12

Just chiming in here that the customer quoted is us :). The main challenger is that we have clients in multiple languages that don’t always have tokenizer implementations readily available. Every other prominent model server does detokenization, hence the request. 

Doesn’t hurt that there are so many CPU cores on the TPU VMs that are mostly idle during inference anyway. 

Thanks @JoeZijunZhou !

### JoeZijunZhou · 2024-05-14

Resolved this issue in #78 . It's available in main.
