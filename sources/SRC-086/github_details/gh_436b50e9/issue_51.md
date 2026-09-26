# [Issue #51] errors occurred when running simple_gradio_interface.py

source: https://github.com/FasterDecoding/Medusa/issues/51
state: closed | updated: 2023-09-29T09:32:57Z
labels: 

## 正文

I tried with the simple_gradio_interface.py,but to found 
![image](https://github.com/FasterDecoding/Medusa/assets/135443303/e635b3cb-2262-4af6-830d-d213d840f613)
I googled it ,and it says the operand doesn't support fp16
However having changing the dtype here,
![image](https://github.com/FasterDecoding/Medusa/assets/135443303/6414669b-6d20-46ef-861a-6ce38c576661)
gives me a new error
![image](https://github.com/FasterDecoding/Medusa/assets/135443303/f46dba1b-9494-4cde-804f-1470ab7e0b55)


## 评论 (2)

### ctlllll · 2023-09-26

Hi, I saw you removed the `device_map` argument, in this case, you may need to manually move the model to the GPU with `model.cuda()` or `model.to(your_device)`.

### MeWannaSleep · 2023-09-29

@ctlllll  thx for your reply
