# [Issue #22] Names of the c packages to be included are missing

source: https://github.com/gpu-mode/lectures/issues/22
state: closed | updated: 2024-10-25T03:40:04Z
labels: 

## 正文

In the nb for lecture 3, the names of the c packages to be included are missing - see picture
![CleanShot 2024-05-29 at 15 37 28@2x](https://github.com/cuda-mode/lectures/assets/40663591/2b7e81a4-696e-4244-ac18-356541d46e91)


## 评论 (1)

### msaroufim · 2024-10-25

This is kinda funny since if you look at the raw text the cuda is there - this is just some rendering quirk in notebooks because of the number of quotations. Gonna close since while this is annoying the code should urn correctly

```

    "cuda_begin = r'''\n",
    "#include <torch/extension.h>\n",
    "#include <stdio.h>\n",
    "#include <c10/cuda/CUDAException.h>\n",
```
