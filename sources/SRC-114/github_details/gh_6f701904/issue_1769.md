# [Issue #1769] SDXL one of the ten reference images' caption generates a disturbing image

source: https://github.com/mlcommons/inference/issues/1769
state: closed | updated: 2026-07-27T00:37:07Z
labels: Stale

## 正文

Hi, caption id `1303` generates an image that looks a bit disturbing. Since in 4.0, we disclosed the images to the public, e.g. https://github.com/mlcommons/inference_results_v4.0/tree/main/closed/NVIDIA/results/DGX-H100_H100-SXM-80GBx8_TRT/stable-diffusion-xl/Offline/accuracy/images, I would like to ask if we can replace 1303 with a different caption or just avoid showing the images in the results directory? We can remove the images after the review period if the latter is preferred. Thanks!

## 评论 (3)

### nvyihengz · 2024-07-08

Also I think the taskforce agreed to not disclose the compliance images to the public.

### pgmpablo157321 · 2024-07-09

@pgmpablo157321 
- Add option in submission checker to remove all the stable diffusion images folder, and skip the checks done for the images folder
- Remove the images from the inference_results_v4.0 repository

### github-actions[bot] · 2026-07-27

🔒 This issue has been **automatically closed** because it has been open for more than 2 years with no activity.
If this is still relevant, you may **reopen it or create a new one**.
