# [Issue #1481] 性能压测之后的可视化结果查询

source: https://github.com/modelscope/evalscope/issues/1481
state: closed | updated: 2026-07-14T10:25:03Z
labels: 

## 正文

使用Eval scope进行大模型性能压测，成功之后可查看基准测试报告：

<img width="1240" height="1180" alt="Image" src="https://github.com/user-attachments/assets/1b4a2178-784a-456f-b56a-41248fddb267" />

但是对于可视化页面，好像并么有像评测一样的归档，再登录可视化系统就查不到之前的性能压测了，看板只有针对于数据集的评测

<img width="469" height="204" alt="Image" src="https://github.com/user-attachments/assets/662416a7-f3f0-423a-8b16-a1fdc0e372ee" />

## 评论 (1)

### Yunnglin · 2026-07-14

你好 @wsh-sun，感谢反馈 🙏

该需求已实现并合入 `main`（#1484）。Web 看板新增了 **Performance** 标签，可归档并查看历史性能压测结果（列表 / 详情图表 / 多 run 对比 / 完整 HTML 报告），兼容 CLI 与 service 两种输出布局。

使用：`evalscope service --outputs <你的 outputs 目录>`，打开后点顶部 **Performance** 即可。下个发布版本会带上。

