# [Issue #236] Cannot clone from Efficient-Large-Model/VILA.git, Dependency Issues with alternative

source: https://github.com/mit-han-lab/llm-awq/issues/236
state: open | updated: 2026-02-10T09:15:23Z
labels: 

## 正文

When executing `git clone git@github.com:Efficient-Large-Model/VILA.git`, I reach the error that I am not authenticated or the repository does not exist. 

When I install the similar repository at NVlabs/VILA, there is a dependency issue: 
awq requires pydantic 2.9.2, but VILA requires pydantic <2, >= 1. 

With the incompatible versions, I receive an error in running the inference script:
`miniconda3/envs/awq/lib/python3.10/site-packages/awq_inference_engine-0.0.0-py3.10-linux-x86_64.egg/awq_inference_engine.cpython-310-x86_64-linux-gnu.so: undefined symbol: _ZN3c1021throwNullDataPtrErrorEv`

How do we resolve these dependencies? 

## 评论 (2)

### Gokulakrishnan-DL-CV · 2024-12-17

Hi @rossgreer!  I am facing dependency issues too! There are many branches in this repo now! The structure of VILA's repo has also changed. I don't know which one goes with what! 
I am working with Orin NX devices and would like to run VILA-1.5 with AWQ & tinychat. It would be great if the authors could drop a correspondance table between the different branches that work together on different platforms! @kentang-mit @tonylins 



### ZhangJinghe-AI · 2026-02-10

@Gokulakrishnan-DL-CV May I ask which branch of VILA you finally chose？

