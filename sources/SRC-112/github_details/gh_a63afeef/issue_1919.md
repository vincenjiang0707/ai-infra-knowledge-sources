# [Issue #1919] Front End: Select Date Range too often / 前端：日期范围选择过于频繁

source: https://github.com/SemiAnalysisAI/InferenceX/issues/1919
state: open | updated: 2026-07-04T05:16:49Z
labels: 

## 正文

When there is 1 date available, the front end asks the user to confirm they want that date. The user obviously wants to see the data for that date and shouldn't be prompted. In general I think the comparison date range should default to latest point.




Repro:
https://inferencex.semianalysis.com/inference
select model and gpu config
get forced to make useless decisions about date range.
<img width="1665" height="848" alt="Image" src="https://github.com/user-attachments/assets/5742a6d5-8f8e-4108-b42a-8dc713649508" />
<img width="1272" height="1307" alt="Image" src="https://github.com/user-attachments/assets/7023a098-5955-427e-8ba7-71124681a777" />

## 中文说明
前端在仅有一个可用日期时仍要求用户确认选择该日期，这是不必要的交互。用户显然想查看该日期的数据，不应被迫做无意义的选择。日期范围比较应默认选择最新数据点。复现步骤：访问 inferencex.semianalysis.com/inference，选择模型和 GPU 配置后，会被强制进行无用的日期范围选择。


## 评论 (1)

### functionstackx · 2026-06-24

good suggestion? if u would like, do u wanna try to do the first attempt at PRing it? https://github.com/SemiAnalysisAI/InferenceX-app

