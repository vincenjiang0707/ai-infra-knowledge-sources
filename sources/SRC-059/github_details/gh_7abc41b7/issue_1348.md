# [Issue #1348] paddleocr-vl finetuning dataset format

source: https://github.com/PaddlePaddle/ERNIE/issues/1348
state: closed | updated: 2026-02-09T12:02:16Z
labels: 

## 正文

Hi, I've been reading the instructions on how to finetune the paddleocr-VL model and I have some questions regarding how to prepare the finetuning dataset: https://github.com/PaddlePaddle/ERNIE/blob/release/v1.4/docs/paddleocr_vl_sft.md

<img width="748" height="930" alt="Image" src="https://github.com/user-attachments/assets/e72a54cd-722b-4770-8643-a6404e7aa650" />

1. Let's say I have a single page pdf image with some text, table, and images (see above). How should I generate the finetuning data in this case? Do I have to separate all text, tables, and images and create a finetuning dataset for each task?
2. is it possible to train the paddleocr-VL model from scratch using ERNIE?
3. Assume that my finetuning dataset only contains 1 task (say Table Recognition), how do you think this will impact the overall model performance?

Thank you so much!


## 评论 (3)

### jerrywind · 2025-11-09

@Theophylline ,
Based on my experience, you shoulde get the crops of images(based on bboxes and labels) from a layout model , like PP-DocLayoutV2 here : https://github.com/PaddlePaddle/PaddleX/blob/release/3.3/paddlex/configs/pipelines/PaddleOCR-VL.yaml .
If you use the official vllm docker , it is easy to get the instance to access.
BR

### Sunting78 · 2025-11-10

1. You can use a layout detection model to crop out individual elements. As mentioned above, you can use the PP-DocLayoutV2 model for this purpose. Then, you can annotate each area separately. Alternatively, you can directly use PaddleOCR-VL, save the results in a JSON file to obtain the coordinates and recognition results of sub-areas, crop them out, and then adjust the labels based on the recognition results.

2. You can set `from_scratch=1`.

3. Yes, if you fine-tune only one specific task, theoretically, the model might experience some forgetting, leading to a decrease in accuracy for other tasks.

### nepeplwu · 2026-02-09

The issue has no response for a long time and will be closed. You can reopen or new another issue if are still confused.

---
_From Bot_
