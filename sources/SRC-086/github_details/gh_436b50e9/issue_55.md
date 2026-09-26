# [Issue #55] TypeError: __init__() got an unexpected keyword argument 'medusa_num_heads'

source: https://github.com/FasterDecoding/Medusa/issues/55
state: closed | updated: 2025-07-27T07:29:42Z
labels: 

## 正文

I try to run the medusa_inference_explained.ipynb but when I load the pretrained model from local, I got the error message

## 评论 (7)

### leeyeehoo · 2023-10-23

Can you provide further information? General answer based on my interpretation: you can simply modify the Medusa model load from pretrain code or override the number of heads. 

### HackGiter · 2023-11-03

> Can you provide further information? General answer based on my interpretation: you can simply modify the Medusa model load from pretrain code or override the number of heads.

I solve that problem by installing the package from source instread of pip. Is it because they're different versions? I'm not sure.

### harveyp123 · 2023-11-21

> > Can you provide further information? General answer based on my interpretation: you can simply modify the Medusa model load from pretrain code or override the number of heads.
> 
> I solve that problem by installing the package from source instread of pip. Is it because they're different versions? I'm not sure.

Yes, currently it's better to install from source instead of pip. 

### Jianwei-Lv · 2024-08-02

 I also got the error message "TypeError: __init__() got an unexpected keyword argument 'medusa_num_heads'". 

![f81da765-a58a-469b-9547-b1247e4f3575](https://github.com/user-attachments/assets/c4608fe2-7c2c-4ce9-9aa9-e87312e013c4)
How to fix? Thanks in advance!

### YunSeoHwan · 2024-10-28

> I also got the error message "TypeError: **init**() got an unexpected keyword argument 'medusa_num_heads'".
> 
> ![f81da765-a58a-469b-9547-b1247e4f3575](https://private-user-images.githubusercontent.com/76138339/354530674-c4608fe2-7c2c-4ce9-9aa9-e87312e013c4.jpeg?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MzAwODcyODQsIm5iZiI6MTczMDA4Njk4NCwicGF0aCI6Ii83NjEzODMzOS8zNTQ1MzA2NzQtYzQ2MDhmZTItN2MyYy00Y2U5LTlhYTktZTg3MzEyZTAxM2M0LmpwZWc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQxMDI4JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MTAyOFQwMzQzMDRaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1hNGQwZTAwZWRlZGZhZTMyYmRiMWYyZjU0YWIwY2Y0MmYzMDkzMzEwMWE5NTU5NDZmYWViMzBkYjkyNDQ4N2M5JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.z0ioZ7-NHwrFgbSPp4m4V49TP-iE9bsxfcJbEpyaI_8) How to fix? Thanks in advance!

Have you resolved this issue? I faced the same problem.

### dnhkng · 2024-12-01

Same here:

TypeError: MedusaModelABC.__init__() got an unexpected keyword argument 'medusa_num_heads'

I installed using the github repo, not pip.


### PKUfreshman · 2025-07-27

me too, but I found that simply change the __init__ function of MedusaModelABC in medusa_model.py as follow may help:
```
def __init__(
        self,
        config,
        *args,
        **kwargs,
    ):
```
