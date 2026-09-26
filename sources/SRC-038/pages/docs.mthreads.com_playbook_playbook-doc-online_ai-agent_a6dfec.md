source: https://docs.mthreads.com/playbook/playbook-doc-online/ai-agent

# 【中级】AI 智能体构建入门

## 更新日志[](https://docs.mthreads.com#更新日志)

| 版本 | 日期 | 变更描述 |
|---|---|---|
| 1.0.0 | 2026-01-30 | 初始版本，包含在 MTT AIBOOK（型号 A141）上从零构建一个 AI 智能体的完整开发指南。 |

## 1. 项目简介[](https://docs.mthreads.com#1-项目简介)

本教程将指导开发者从零开始构建一个极简但完整的 AI 智能体，通过分步拆解让您理解每个模块的设计逻辑，最终独立完成一个包含 **「思考 - 行动 - 记忆」** 核心要素的智能助手原型。

**难度：中级，适合有编程基础的开发者体验**

**AI 智能体简介：** AI 智能体是一种能够通过 **「感知环境 → 思考决策 → 执行动作」** 循环实现目标的智能系统。无论多简单的 AI 智能体，都必须具备三大核心能力：

**思考（Think）**：分析用户输入，识别意图并生成行动计划。**行动（Act）**：根据计划执行具体动作（如回复、调用工具）。**记忆（Memory）**：存储历史对话，为多轮交互提供上下文支持。

## 2. 前置条件[](https://docs.mthreads.com#2-前置条件)

在开始本教程之前，请确保您已满足以下所有条件：

**硬件:**- AI 算力本 MTT AIBOOK, 型号 A141
- 网络连接（用于下载依赖包）

**软件:**- MTT AIBOOK 操作系统 AIOS(1.3.1-B15) 及以上版本。
- 已安装 Python 3.10 或更高版本（
`python --version`

验证）。 - 已安装 pip 包管理工具（
`pip --version`

验证）。 - 已安装 Conda 环境管理工具（可选，推荐使用）。
- 具备 Python 编程基础知识（熟悉类、方法、循环等基本概念）。
- 了解面向对象编程的基本原理（可选，教程中会详细说明）。


## 3. 环境部署[](https://docs.mthreads.com#3-环境部署)

本章节描述如何创建项目目录并安装必要的依赖组件。

### 3.1 创建项目目录[](https://docs.mthreads.com#31-创建项目目录)

-
打开终端（Linux Terminal）。

-
创建项目目录并进入：

mkdir my_first_agent && cd my_first_agent

项目目录将用于存放所有代码文件。

### 3.2 安装依赖[](https://docs.mthreads.com#32-安装依赖)

-
安装依赖包：

pip install colorama pyfiglet**依赖说明：**`colorama`

：用于控制台彩色输出`pyfiglet`

：用于生成艺术字体，美化控制台输出

-
验证依赖安装成功：

pip list | grep -E "colorama|pyfiglet"若输出包含这两个包及其版本信息，说明依赖安装成功。


## 4. 最佳实践[](https://docs.mthreads.com#4-最佳实践)

本章节指导您逐步构建 AI 智能体的核心功能模块。

### 场景 1: 构建智能体基础框架[](https://docs.mthreads.com#场景-1-构建智能体基础框架)

创建 SimpleAgent 类并实现初始化功能：

-
创建代码文件：

touch simple_agent.py或使用您喜欢的编辑器创建

`simple_agent.py`

文件。 -
编写基础框架代码：

import timefrom typing import List, Dictfrom colorama import Fore, Style, initfrom pyfiglet import Figlet# 初始化控制台美化工具init()class SimpleAgent:def __init__(self, name):self.name = nameself.memory = [] # 记忆存储列表# 欢迎语f = Figlet(font='slant')print(Fore.CYAN + f.renderText(self.name) + Style.RESET_ALL)print(f"我是 {Fore.GREEN}{self.name}{Style.RESET_ALL}，一个简单的 AI 助手！") -
添加主程序入口（用于测试）：

if __name__ == "__main__":agent = SimpleAgent("SimpleBot") -
运行测试：

python simple_agent.py**预期效果：**控制台将打印艺术字标题和欢迎语，标志智能体初始化完成。**代码解析：**`__init__`

方法定义了 SimpleAgent 类的构造函数。- 当创建智能体实例时，会传入
`name`

参数作为智能体的名称。 `self.memory = []`

初始化一个空列表，用于存储后续的对话历史。- 通过 Figlet 类创建艺术字体生成器，将智能体名称转换为斜体艺术字并以青色打印输出。


### 场景 2: 实现思考能力[](https://docs.mthreads.com#场景-2-实现思考能力)

为智能体添加 `think`

方法，实现意图识别功能：

-
在 SimpleAgent 类中添加

`think`

方法：def think(self, user_input: str) -> str:"""分析用户输入，生成行动计划"""user_input = user_input.lower() # 统一小写处理if "你好" in user_input or "hello" in user_input:return "greeting" # 问候意图elif "天气" in user_input or "weather" in user_input:return "weather" # 天气查询意图else:return "default" # 默认意图 -
测试思考功能：

if __name__ == "__main__":agent = SimpleAgent("SimpleBot")# 测试思考功能print(agent.think("你好")) # 输出：greetingprint(agent.think("今天天气如何？")) # 输出：weatherprint(agent.think("你能做什么？")) # 输出：default**设计思考：**- 通过关键词匹配实现意图分类，返回字符串作为「行动指令」。
- 解耦「意图识别」与「回复生成」，便于后续扩展复杂逻辑。
**思考题：**为何不直接返回回复内容？（提示：分离决策与执行）。

**代码解析：**`think`

方法负责分析用户输入并识别其意图。- 首先将用户输入转换为小写，以避免大小写敏感问题。
- 通过条件判断检查输入中是否包含特定关键词。
- 返回意图标签（"greeting"、"weather" 或 "default"），而不是直接返回回复内容。


### 场景 3: 实现行动能力[](https://docs.mthreads.com#场景-3-实现行动能力)

为智能体添加 `act`

方法，根据意图生成具体回复：

-
在 SimpleAgent 类中添加

`act`

方法：def act(self, plan: str) -> str:"""根据计划执行具体动作"""response_map = {"greeting": f"你好！我是{Fore.YELLOW}{self.name}{Style.RESET_ALL}，很高兴为你服务！","weather": "抱歉，我暂时还不具备查询天气的能力 😔","default": "对不起，这个问题我还在学习中～可以换个话题吗？"}return response_map.get(plan, "发生未知错误，请重新输入") # 安全兜底 -
测试行动功能：

if __name__ == "__main__":agent = SimpleAgent("SimpleBot")# 测试完整流程plan = agent.think("你好")response = agent.act(plan)print(response) # 输出：你好！我是 SimpleBot，很高兴为你服务！**设计思考：**- 使用字典映射计划与回复，提高可维护性。
- 分离「意图」与「回复内容」，方便后续修改话术或添加多语言支持。

**代码解析：**`act`

方法根据`think`

模块返回的意图标签生成具体回复。- 通过字典
`response_map`

建立意图标签与对应回复内容的映射关系。 - 使用字典的
`get`

方法获取对应回复，若意图标签不存在则返回错误提示，确保系统的健壮性。


### 场景 4: 构建主循环[](https://docs.mthreads.com#场景-4-构建主循环)

实现智能体的核心交互循环，完成「感知 → 思考 → 行动 → 记忆」的完整流程：

-
**在 SimpleAgent 类中添加 run 方法**：def run(self):"""智能体主循环：感知→思考→行动→记忆"""while True:user_input = input(f"\n{Fore.BLUE}[{self.name}] 请输入你的问题（输入'exit'退出）：{Style.RESET_ALL}")if user_input.lower() == "exit":print(Fore.RED + "再见！期待下次相遇～" + Style.RESET_ALL)break# 核心循环plan = self.think(user_input)response = self.act(plan)print(f"\n{Fore.GREEN}[{self.name}回复]{Style.RESET_ALL} {response}")# 存储对话到记忆self.memory.append({"timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),"user_input": user_input,"response": response}) -
**更新主程序入口**：if __name__ == "__main__":agent = SimpleAgent("SimpleBot")agent.run() # 启动主循环**循环解析：****感知**：获取用户输入（通过`input`

函数）。**思考**：调用`think`

方法生成行动计划。**行动**：调用`act`

方法生成回复。**记忆**：以字典形式存储对话记录（含时间戳）。

**代码解析：**`run`

方法实现了智能体的核心交互循环。- 通过无限循环持续获取用户输入。
- 当检测到用户输入
**"exit"**时，打印红色的退出提示并终止循环。 - 在每次循环中，先调用
`think`

方法分析用户意图，再将意图标签传递给`act`

方法生成回复。 - 最后，将当前对话的时间戳、用户输入和智能体回复以字典形式存入
`memory`

列表，实现对话历史的记录功能。


### 场景 5: 测试与验证[](https://docs.mthreads.com#场景-5-测试与验证)

运行完整的智能体程序并进行功能测试：

-
**运行智能体程序**：python simple_agent.py -
**测试用例**：

| 用户输入 | 预期回复 |
|---|---|
| "你好" | "你好！我是 SimpleBot，很高兴为你服务！" |
| “今天天气如何？” | “抱歉，我暂时还不具备查询天气的能力 😔” |
| “你能做什么？” | “对不起，这个问题我还在学习中～可以换个话题吗？” |
| “exit” | “再见！期待下次相遇～” |

-
**验证记忆功能**：在程序运行过程中，所有对话记录都会自动保存到

`self.memory`

列表中。可在

`run`

方法中添加以下代码查看记忆内容：# 在 run 方法中添加（可选）if len(self.memory) > 0:print(f"\n[记忆] 已记录 {len(self.memory)} 条对话")

## 完整代码清单[](https://docs.mthreads.com#完整代码清单)

以下是完整的 `simple_agent.py`

代码：

`import time`

from typing import List, Dict

from colorama import Fore, Style, init

from pyfiglet import Figlet


# 初始化控制台美化工具

init()


class SimpleAgent:

def __init__(self, name):

self.name = name

self.memory = []

f = Figlet(font='slant')

print(Fore.CYAN + f.renderText(name) + Style.RESET_ALL)

print(f"我是 {Fore.GREEN}{name}{Style.RESET_ALL}，一个简单的 AI 助手！")


def think(self, user_input: str) -> str:

"""

分析用户输入，生成行动计划

"""

user_input = user_input.lower()

if "你好" in user_input or "hello" in user_input:

return "greeting"

elif "天气" in user_input or "weather" in user_input:

return "weather"

else:

return "default"


def act(self, plan: str) -> str:

"""

根据计划执行具体动作

"""

response_map = {

"greeting": f"你好！我是{Fore.YELLOW}{self.name}{Style.RESET_ALL}，很高兴为你服务！",

"weather": "抱歉，我暂时还不具备查询天气的能力 😔",

"default": "对不起，这个问题我还在学习中～可以换个话题吗？"

}

return response_map.get(plan, "发生未知错误，请重新输入")


def run(self):

"""智能体主循环：感知→思考→行动→记忆"""

while True:

user_input = input(f"\n{Fore.BLUE}[{self.name}] 请输入你的问题（输入'exit'退出）：{Style.RESET_ALL}")

if user_input.lower() == "exit":

print(Fore.RED + "再见！期待下次相遇～" + Style.RESET_ALL)

break

plan = self.think(user_input)

response = self.act(plan)

print(f"\n{Fore.GREEN}[{self.name}回复]{Style.RESET_ALL} {response}")

self.memory.append({

"timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),

"user_input": user_input,

"response": response

})


if __name__ == "__main__":

agent = SimpleAgent("SimpleBot")

agent.run()



## 常用操作命令[](https://docs.mthreads.com#常用操作命令)

| 操作 | 命令 |
|---|---|
| 创建项目目录 | `mkdir my_first_agent && cd my_first_agent` |
| 安装依赖 | `pip install colorama pyfiglet` |
| 运行智能体 | `python simple_agent.py` |
| 退出智能体 | 在交互界面输入 `exit` |

## 5. 附录[](https://docs.mthreads.com#5-附录)

### 5.1 项目亮点[](https://docs.mthreads.com#51-项目亮点)

**原理导向学习**：从基础概念到代码实现逐步拆解，拒绝「复制粘贴」，确保知其然且知其所以然。**渐进式成就感**：每完成一个方法即可看到智能体能力提升，学习过程充满反馈。**极简完整架构**：包含「思考 (Think)-行动 (Act)」核心循环（即 AI 智能体的「感知 - 决策 - 执行」核心循环），代码简洁但原理清晰易读。**可扩展框架**：预留功能扩展接口，为后续添加复杂能力（如多轮对话、工具调用）奠定基础。

### 5.2 核心学习成果[](https://docs.mthreads.com#52-核心学习成果)

通过本项目，您将扎实掌握：

- AI 智能体的「感知 - 决策 - 执行」核心循环：理解智能体的基本工作原理
- 基于规则的意图识别方法：学会使用关键词匹配实现简单的意图分类
- 对话记忆系统的设计与实现：掌握如何存储和管理对话历史
- 面向对象编程在智能系统中的应用模式：理解如何使用类和方法组织智能体代码

### 5.3 AI 智能体的三要素[](https://docs.mthreads.com#53-ai-智能体的三要素)

无论多简单的 AI 智能体，都必须具备如下三大核心能力：

**思考（Think）**：分析用户输入，识别意图并生成行动计划**行动（Act）**：根据计划执行具体动作（如回复、调用工具）**记忆（Memory）**：存储历史对话，为多轮交互提供上下文支持

### 5.4 扩展挑战（进阶方向）[](https://docs.mthreads.com#54-扩展挑战进阶方向)

完成基础实现后，您可以尝试以下升级：

#### 1. 意图扩展[](https://docs.mthreads.com#1-意图扩展)

在 `think`

方法中添加更多意图（如时间查询、数学计算）：

`def think(self, user_input: str) -> str:`

user_input = user_input.lower()

if "你好" in user_input or "hello" in user_input:

return "greeting"

elif "天气" in user_input or "weather" in user_input:

return "weather"

elif "时间" in user_input or "time" in user_input:

return "time_query"

elif "计算" in user_input or "calculate" in user_input:

return "calculation"

else:

return "default"



#### 2. 记忆增强[](https://docs.mthreads.com#2-记忆增强)

利用 `memory`

实现多轮对话上下文（如："刚才你说天气不具备能力，那其他功能呢？"）：

`def think(self, user_input: str) -> str:`

user_input = user_input.lower()

# 检查记忆中的上下文

if "刚才" in user_input or "之前" in user_input:

if len(self.memory) > 0:

last_topic = self.memory[-1].get("response", "")

# 基于上下文进行回复

return "context_followup"

# ... 其他意图识别逻辑



#### 3. 工具集成[](https://docs.mthreads.com#3-工具集成)

在 `act`

方法中调用外部 API（如天气接口、计�算器接口）：

`def act(self, plan: str) -> str:`

if plan == "weather":

# 调用天气 API

weather_data = get_weather_api()

return f"今天天气：{weather_data}"

elif plan == "calculation":

# 调用计算器功能

result = calculate_expression(user_input)

return f"计算结果：{result}"

# ... 其他回复逻辑



#### 4. 个性化定制[](https://docs.mthreads.com#4-个性化定制)

为智能体添加性格设定（如幽默风、专业风）：

`class SimpleAgent:`

def __init__(self, name, personality="friendly"):

self.name = name

self.personality = personality # "humorous", "professional", "friendly"

# ...


def act(self, plan: str) -> str:

if self.personality == "humorous":

response_map = {

"greeting": f"哈哈，你好！我是{self.name}，一个有趣的 AI 助手！",

# ...

}

# ...



### 5.5 常见问题[](https://docs.mthreads.com#55-常见问题)

| 问题描述 | 可能原因 | 解决方案 |
|---|---|---|
运行时报错 ModuleNotFoundError: No module named 'colorama' | 依赖包未安装 | 执行 `pip install colorama pyfiglet` 安装依赖。 |
| 控制台输出乱码 | 终端编码设置问题 | Linux：确保终端支持 UTF-8 编码。 |
| 艺术字体显示异常 | pyfiglet 字体问题 | 尝试修改字体：`f = Figlet(font='standard')` 或 `f = Figlet(font='small')` 。 |
| 输入中文后程序报错 | Python 版本或编码问题 | 1. 确保使用 Python 3.10+；2. 在文件开头添加 `# -*- coding: utf-8 -*-` 。 |
| 记忆功能不工作 | 代码逻辑错误 | 检查 `self.memory.append()` 是否在 `run` 方法中正确调用。 |
| 意图识别不准确 | 关键词匹配过于简单 | 1. 添加更多关键词；2. 考虑使用正则表达式或更复杂的匹配逻辑。 |

### 5.6 相关资源[](https://docs.mthreads.com#56-相关资源)

- Python 官方文档：
[https://docs.python.org/3/](https://docs.python.org/3/)（学习 Python 基础语法） - LangChain 框架：
[https://python.langchain.com/](https://python.langchain.com/)（深入学习复杂智能体框架）

### 5.7 学习路径建议[](https://docs.mthreads.com#57-学习路径建议)

通过亲手搭建这个极简智能体，您将打通从「理论认知」到「代码实现」的关键链路。建议后续学习路径：

**巩固基础**：深入理解面向对象编程和设计模式**扩展功能**：尝试实现上述扩展挑战中的功能**学习框架**：深入学习 LangChain、AutoGPT 等复杂智能体框架**实战项目**：将智能体应用到实际场景中（如客服机器人、个人助手等）

立即开始您的 AI 开发之旅吧！