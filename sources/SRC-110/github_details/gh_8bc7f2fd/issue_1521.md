# [Issue #1521] [功能请求] web页面支持删除历史记录

source: https://github.com/modelscope/evalscope/issues/1521
state: closed | updated: 2026-07-28T02:13:07Z
labels: enhancement

## 正文

功能描述 / Feature Description
为 Performance 历史记录列表添加删除功能。当前 WebUI 的 /performance 页面列出了所有历史 perf 运行记录，但没有任何方式删除不需要的条目（比如测试用的错误配置、重复运行等）。用户只能手动去文件系统删除 outputs 下的目录，而如果 Web 服务正在运行，Windows 下还会因为文件占用无法删除。

需求背景 / Background
日常使用中经常会产生无用的 perf 记录：

测试时填错参数（API URL、model name 写错）
重复运行只保留最优的一次
想清理过期数据但不想 rm -rf 手动操作
目前 evalscope 的 eval 任务和 perf 任务都没有任何删除 API，缺少基本的生命周期管理能力。

预期行为 / Expected Behavior
后端：新增 DELETE /api/v1/perf/run 端点：

入参：root_path（outputs 根目录）、path（相对于 root 的运行目录）
安全检查：防路径穿越（realpath 校验）、运行中任务保护（409）
响应：{ success: true, path: "..." }

前端： 再考虑放哪儿

其他信息 / Additional Information
eval 任务同样缺少删除功能，可以后续一起补充

## 评论 (1)

### Yunnglin · 2026-07-28

Implemented in #1526, exactly along the lines you proposed:

- `DELETE /api/v1/perf/run` with `root_path` + `path`, realpath-based
  path-traversal rejection, and running-task protection (409);
- response: `{ "success": true, "path": "..." }`;
- frontend: a delete action in the selection tray on the /performance page,
  with an in-app confirmation dialog listing the affected runs.

Bonus: eval report deletion (`DELETE /api/v1/reports/report`) is included in
the same PR as well, so both record types can now be managed from the Web UI.

This issue will be closed automatically when #1526 is merged.

