source: https://docs.mthreads.com/musacode/musacode-doc-online/Desktop使用

# Desktop 使用

同一用户下安装的 TUI 和 Desktop 配置共享。

## 模型配置[](https://docs.mthreads.com#模型配置)

-
"提供商 ID" 和 "显示名称" 按需填写，无固定标准

-
基础 URL、API 秘钥、模型必填，且必须正确


## Agent 配置[](https://docs.mthreads.com#agent配置)

MUSACODE Desktop 配置路径示例：

-
Linux：

`/home/<username>/.config/musacode`

-
Windows：

`C:\Users\<username>\.config\musacode`


添加成功后会显示在上图的 Agent 列表中，如果添加的主 Agent，还会显示在输入框下的 Agent 选择列表中。

## Skill 配置[](https://docs.mthreads.com#skill配置)

-
选择要添加的 skill 目录 -> 选择目标作用域 -> 添加，添加成功后可显示在上图的 skill 列表中

-
项目 skill 存储在所选项目的 .musacode/skills/ 下

-
全局 skill 对所有项目可用，存储在 ~/.config/musacode/skills/（如：

`/home/<username>/.config/musacode`

）

## Agent 群聊[](https://docs.mthreads.com#agent群聊)

**（1）解决了什么问题**

当多个 Agent（subagent）并行执行任务时，用户难以跟踪谁在做什么、各自的进度如何、输出是什么。传统单线程聊天界面无法展示 multi-agent 并发工作场景。

Agent Group Chat 将所有 Agent 的输出合并到一个时间轴视图，可视化 MUSACODE 执行任务过程中 Agent 与 Agent、Agent 与用户的交互过程，将原本“黑盒”的 Agent 执行过程转化为直观的群聊，极大提升了开发者的可观测性和控制力。

-
以

**说话人视图**组织：每个 Agent（含主 Agent 和 subagent）显示为独立的"聊天气泡"分组 -
使用不同颜色区分 Agent

-
实时更新：新消息流式追加

-
支持嵌套（subagent 的 subagent）


**（2）如何开启**

默认开启。当 session 中有 Agent 运行时自动有内容。无需额外配置。

**（3）如何怎么使用**

在桌面 App 的 session 页面中，点击右上角的 **气泡图标** 按钮即可打开 Agent 群聊面板。再次点击关闭。

**（4）使用示例**

## Session Dashboard[](https://docs.mthreads.com#sessiondashboard)

**（1）解决了什么问题**

用户在终端中启动多个 Session 后，无法快速查看全局状态——哪些正在运行、哪些被阻塞等待权限、哪些已完成。每次切换 Session 都需要记住 Session ID 或用命令查询。

Session Dahboard 是一个统一管理所有 MUSACODE 会话的终端仪表盘，支持查看所有 Session 的状态、快速跳转、管理生命周期，多 session、多工作区一目了然。

**（2）如何开启**

TUI、Desktop 内置功能，默认可用。无需配置。

**（3）如何使用**

TUI：在 TUI 中命令 `/dashboard`

或直接在终端执行 musacode --dashboard，进入 Dashboard 视图。

Desktop：在桌面 App 中点击左侧边栏的 **Dashboard** 入口。

**（4）使用示例**

TUI 显示效果（执行 musacode --dashboard）：

## 桌面宠物[](https://docs.mthreads.com#桌面宠物)

**（1）解决什么问题**

长时间编码时，用户容易忘记休息、喝水、站起身。Agent 运行时用户可能分心去做其他事，回来时需要知道当前进度。此外，桌面应用的趣味性和陪伴感不足。

MUSAPet 是 MUSACODE 桌面应用中内建的桌面宠物系统。宠物以透明、置顶、无边框的 Electron 窗口悬浮在桌面上，通过精灵动画展示多种状态，与 AI Agent 的实时状态联动，并提供休息提醒、专注模式、分心检测等生产力辅助功能。

**（2）如何开启与配置**

默认开启。关闭方式：

-
桌面 App → 设置 → Pet Management → 关闭开关

-
或设置

`MUSACODE_DISABLE_PET=true`

环境变量

休息提醒、喝水提醒、专注模式的配置

管理已安装的宠物

**（3）如何使用**

-
桌面 App 启动后，宠物自动出现在屏幕右下角

-
鼠标拖动可移动位置

-
Agent 工作时宠物会切换到"工作中"动画

-
定时弹出休息/喝水提醒气泡

-
点击气泡可执行操作（开始休息/喝水/小睡一会��）


## Recap[](https://docs.mthreads.com#recap)

**（1）解决什么问题**

**Recap** 功能，解决「多开党」（同时开多个 MUSACODE 会话）的核心痛点：

当用户在多个 Session 之间切换时（例如中断 A 去处理 B，然后再回到 A），需要快速理解之前的上下文——做了什么、卡在哪里、下一步做什么。逐条翻看历史消息低效且容易丢失重点。


**Recap 功能做的事情**：当用户切回一个 MUSACODE 会话窗口时，手动执行 recap 命令可弹出一行摘要，用一句话说清楚：

-
**做了什么**（已完成的工作） -
**进度如何**（当前状态） -
**有什么问题**（阻塞项） -
**下一步该做什么**（待办事项）

**（2）如何开启**

内置功能，默认可用。无需配置。

**（3）如何使用**

在 TUI/Desktop 中使用 `/recap`

命令。

**（4）使用示例**

## Goal[](https://docs.mthreads.com#goal)

**（1）解决什么问题**

在长周期、多轮次的 Agent 任务中，Agent 可能会"忘记"最初的用户意图，或者在没有明确完成标准的情况下无休止地运行、或者提前宣称完成。用户需要��一个机制来设定清晰目标、追踪进度、在达成条件满足时才标记完成。

Goal 系统提供了**带约束的长期任务管理**机制。**一个 session 同时只能存在一个 goal 任务**。

**Goal 生命周期：**

`active → paused → active（暂停/恢复）`

active → complete（完成）

active → budget_limited（Token 预算耗尽）



**示例流程**：

-
用户：

`/goal "为 auth 模块添加完整的集成测试"`

-
Agent 调用

`goal.create({ condition: "所有 auth 集成测试通过且覆盖登录、注册、Token 刷新三个场景", tokenBudget: 50000 })`

-
Agent 持续工作，每轮自动记录 token 消耗

-
Agent 完成后调用

`goal.complete()`

（或评估器判定达成） -
系统记录完成状态、总轮次数、总 Token 消耗


**（2）如何开启**

配置文件（`musacode.json`

）：

`{`

"goal": { "enabled": true }

}




**（3）如何使用**

**TUI/Desktop 中**：

`/goal 完成 packages/auth 目录下所有测试的重构`

/goal # 查看当前目标状态

/goal clear # 清除目标

/goal pause # 暂停（不追踪 token）

/goal resume # 恢复




**Agent 行为**：AI 收到 `/goal`

后：

-
先探索代码库确认条件的可行性

-
设定目标

-
工作过程中检查目标条件

-
条件满足时标记完成

-
如果目标无法在当前 turn 完成，自动汇报进度


## Dynamic Workflow[](https://docs.mthreads.com#dynamicworkflow)

**（1）解决什么问题**

传统方式中，MUSACODE 作为编排者每一步都要在上下文里推理"下一步该做什么"，中间结果也全部堆积在上下文窗口中。另外，单个 Agent turn 的能力有限——复杂任务（如代码审查、重构、多文件搜索）需要多个 Agent 分工协作。但手动协调 Agent 的顺序和并行度是繁琐且容易出错的，需要一个机制来自动化 multi-agent 编排。

Dynamic Workflow 是一个**脚本化 Agent 编排引擎。**Dynamic Workflow 把这个编排逻辑写成一个可读、可保存、可重跑的 JavaScript 脚本，由 Runtime 独立驱动，中间结果存储在脚本变量中而非 MUSACODE 的 context 中。

**Workflow 执行模型**：

`Agent 生成 JS 脚本`

Workflow 运行时编译执行

脚本通过 API 调度子 Agent

结果汇总



| 痛点 | Dynamic Workflow 的解决方案 |
|---|---|
| 上下文污染 | 中间结果存储在脚本变量中，MUSACODE 上下文只拿到最终答案 |
| 编排开销 | 编排逻辑写在 JS 脚本中，由 Runtime 执行，不消耗 MUSACODE 的 token |
| 不可重复 | 脚本保存为 `/workflow-name` 命令，可反复执行、可版本控制、可团队共享 |
| 规模限制 | 支持单次运行 最多 1000 个 agent，16 个并发 |
| 结果可靠性 | 支持"对抗性验证"（adversarial review）：独立 agent 交叉检查彼此的发现，只有存活的结论才上报 |

**典型使用场景**：

-
全仓库代码审计（安全漏洞扫描、认证检查）

-
大规模迁移/重构（500+ 文件）

-
需要多源交叉验证的深度研究

-
需要多角度独立规划后才能决策的复杂任务

-
需要定期重复执行的标准化流程（SEC review、dependency audit）


**（2）如何开启**

配置文件（`musacode.json`

）：

`{`

"workflow": {

"enabled": true, // 启用动态工作流

"maxConcurrentAgents": 8, // 最大并发 Agent（默认 16）

"maxAgentsPerRun": 500, // 单次 Agent 总数上限（默认 1000）

"agentTimeoutMs": 120000 // 单个 Agent 超时（默认 300s）

}

}



**（3）如何使用**

在 TUI/Desktop 中通过关键词 `**ultracode**`

、显示指定使用 Dynamic Workflow 或 Agent 主动使用的方式触发 Dynamic Workflow。

方式 | 示例 |
|---|---|
| 关键词 | `**ultracode** audit all routes` |
| 显式 | `use a workflow to refactor` |
| Agent 主动使用 | `用 10 个 agent 并��行审计全部 API` |

**CLI 管理**：

`musacode workflows list # 列出最近运行`

musacode workflows status # 查看当前运行状态

musacode workflows cancel # 取消当前运行




**（4）使用示例**

下图是使用 Desktop Dynamic Workflow 完成任务的示例，主 Agent 生成 JS 脚本，JS 脚本中创建多个子 Agent 并行完成任务。

**Dynamic Workflow 创建的 JS 脚本：**

以下是完成某任务时在工作目录下的 .musacode 目录下创建的 JS 脚本。

## WeChat 接入[](https://docs.mthreads.com#wechat接入)

**（1）解决什么问题**

用户不在电脑前时仍需要与� MUSACODE 交互，通过微信即可向 MUSACODE 发送消息、开关会话、切换 Agent/Model，与在 TUI/Desktop 中输入的效果一致。将 AI 编程助手从桌面延伸到移动端。

微信在 2026 年 3 月通过 ClawBot 插件 正式开放了 iLink Bot API。这是一套基于 HTTP/JSON 的协议，允许第三方程序通过二维码扫码授权后，以 Bot 身份接入个人微信账号。

**（2）如何开启**

TUI、Desktop 内置功能，默认可用。无需配置。

**（3）如何使用**

**扫码连接**：

-
启动 MUSACODE（TUI / Desktop）

-
TUI 中执行

`/wechat`

命令弹出 QR 码 -
微信扫码完成认证

-
向 Bot 发消息即可开始对话


**微信内命令**：

| 命令 | 效果 |
|---|---|
| 普通文本 | 与 AI 对话（同 TUI 输入框） |
`/goal xxx` / `/task xxx` | 斜杠命令（与 Desktop/TUI 一致） |
`/new` | 新建 Session |
`/exit` | 断开连接 |
`@新建` / `@new` | 创建新对话 |
`@切换 2` | 切换到第 2 个对话 |
`@列出` | 查看所有对话 |
`设置` | 选择语言 / Agent / Model |

**（4）使用示例**

**Desktop 侧 WeChat 连接流程：**

**TUI 侧 WeChat 连接流程：**