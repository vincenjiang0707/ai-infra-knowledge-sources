# [Issue #228] awq_inference_engine.cpython-310-x86_64-linux-gnu.so: undefined symbol: _ZN3c1021throwNullDataPtrErrorEv

source: https://github.com/mit-han-lab/llm-awq/issues/228
state: closed | updated: 2025-05-08T09:48:56Z
labels: 

## 正文

When I run the example，I first install flash_atten ,then I met the question
what should I do?
![微信图片_20241022163048](https://github.com/user-attachments/assets/6be9b3d5-9de7-4641-a3b1-84d579c8e304)


## 评论 (4)

### ShobhaRajanna · 2024-11-12

> When I run the example，I first install flash_atten ,then I met the question what should I do? ![微信图片_20241022163048](https://private-user-images.githubusercontent.com/66714627/378752176-6be9b3d5-9de7-4641-a3b1-84d579c8e304.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MzE0MTQ2MTMsIm5iZiI6MTczMTQxNDMxMywicGF0aCI6Ii82NjcxNDYyNy8zNzg3NTIxNzYtNmJlOWIzZDUtOWRlNy00NjQxLWEzYjEtODRkNTc5YzhlMzA0LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDExMTIlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQxMTEyVDEyMjUxM1omWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWFlMGIyNDhhZDE2OGUxZWUyOGU5ZGI0ZTY2M2IzYjU2YmY4YWVmYzAxYWVjYzk5YmZlYjA1MzhiMjJmNzU1OTkmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.UuZMZAPSEmmk6oni2KbIsBKn1RPnqYhD4PBkGEzgBqw)



how did you resolved?

### zhaosiyuan1098 · 2024-12-11

Hi,I have met the same problem, can you tell me how you solve it?Thanks!

### Leymore · 2025-01-29

Hey, I think I fixed this by the following steps:
1. pip uninstall awq/kernels, and remove the build and dist folders
2. git clone the llava repo and install: https://github.com/haotian-liu/LLaVA
3. reinstall awq/kernels
I'm not sure if the above steps is relevant to this error, but I can run the codes after that. 

### whcjb · 2025-05-08

> Hey, I think I fixed this by the following steps:
> 
> 1. pip uninstall awq/kernels, and remove the build and dist folders
> 2. git clone the llava repo and install: https://github.com/haotian-liu/LLaVA
> 3. reinstall awq/kernels
>    I'm not sure if the above steps is relevant to this error, but I can run the codes after that.

use your method, but still error
