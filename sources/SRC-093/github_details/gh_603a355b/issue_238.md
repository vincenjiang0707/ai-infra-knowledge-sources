# [Issue #238] Should ModelAdapter displays the `Status` on the result of get command

source: https://github.com/vllm-project/aibrix/issues/238
state: open | updated: 2026-08-26T08:04:56Z
labels: good first issue, help wanted, kind/support, area/lora

## 正文

### 🚀 Feature Description and Motivation

ModelAdapter, like a Pod, displays the status  on the result of get command.
Displaying the status in this way will be more user-friendly.

[image](https://github.com/user-attachments/assets/981696c4-8745-437a-8c1a-6ca388f1fa8c)


### Use Case

_No response_

### Proposed Solution

_No response_

## 评论 (5)

### Jeffwan · 2024-09-26

@brosoul I am trying to understand the question. you mean implementing a plugin to show the status? I think that's reasonable, this requires some kubectl plugin I think. 

```
kubectl get modeladapter
xxxx
```

this can be definitely enriched.

### brosoul · 2024-09-27

> you mean implementing a plugin to show the status?

Yes @Jeffwan 

### newhans · 2025-05-29




> [@brosoul](https://github.com/brosoul) I am trying to understand the question. you mean implementing a plugin to show the status? I think that's reasonable, this requires some kubectl plugin I think.
> 
> ```
> kubectl get modeladapter
> xxxx
> ```
> 
> this can be definitely enriched.

I found this issue in the v0.4.0 roadmap. Do you agree that simply modifying the CRD to include 'additionalPrinterColumns' can achieve this functionality? If so, could you assign this issue to me? @Jeffwan




### yaojiejia · 2026-08-24

Hi @Jeffwan is this issue still valid? if so can i work on this?

### Jeffwan · 2026-08-26

@yaojiejia yes, please pick it up. I remember we added some fields but may still lack of some, please try it out. 
