# zai-org/MathGLM

source: https://huggingface.co/zai-org/MathGLM

---
license: afl-3.0
---


## Model description
MathGLM-10B is finetuned from GLM-10B on a dataset with additional multi-step arithmetic operations and math problems described in text, achieves similar performance to GPT-4 on a 5,000-samples Chinese math problem
test set.


## How to use 
First, you shoud run the following command to pip sat.
```
pip install SwissArmyTransformer
```
Second, you run the inference code to evaluate our MathGLM-10B.
```
bash inference.sh
```


## Citation
Please cite our paper if you find this code useful for your research:
```
@article{yang2023gpt,
  title={GPT Can Solve Mathematical Problems Without a Calculator},
  author={Yang, Zhen and Ding, Ming and Lv, Qingsong and Jiang, Zhihuan and He, Zehai and Guo, Yuyi and Bai, Jinfeng and Tang, Jie},
  journal={arXiv preprint arXiv:2309.03241},
  year={2023}
}
```


