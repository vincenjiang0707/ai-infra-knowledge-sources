# [Issue #2253] Install PyTorch again where installing gptqmodel

source: https://github.com/ModelCloud/GPTQModel/issues/2253
state: closed | updated: 2025-12-12T10:17:00Z
labels: 

## 正文

When I try to install gptqmodel, it seems to automatically installed torch==2.9.1(even I have installed torch==2.6.0), and I wonder how to solve the problem. Thanks!

## 评论 (1)

### Qubitium · 2025-12-11

@Hugo-cell111 please modify pyproject.yaml and modify the torch depend to your version and compile from source. by default we try to pair with latest torch. 
