# [Issue #4400] [Bug] 在lmdeploy中加载glm-4.7-flash参数如何配置？

source: https://github.com/InternLM/lmdeploy/issues/4400
state: closed | updated: 2026-08-05T03:34:25Z
labels: 

## 正文

### Checklist

- [x] 1. I have searched related issues but cannot get the expected help.
- [x] 2. The bug has not been fixed in the latest version.
- [x] 3. Please note that if the bug-related issue you submitted lacks corresponding environment info and a minimal reproducible demo, it will be challenging for us to reproduce and resolve the issue, reducing the likelihood of receiving feedback.

### Describe the bug

glm模型的工具调用参数， 这两个在lmdeploy中如何调用？
--tool-call-parser glm47
--reasoning-parser glm45 \

现在有例子可以参考吗？

### Reproduction

我现在使用了lmdeploy 0.12.1-cu12.8版本的docker 镜像文件，可以加载glm 4.7了，但是有几个问题不知道怎么解决.1.glm的下面两个参数怎么配置？
--tool-call-parser glm47
--reasoning-parser glm45 \
2.我遇到一个问题就是我设置了session-len长度是192k，但是在程序启动后，又提示我因为长度超长，给自动截断了，这个怎么办？我是否有其他的参数来控制不让他截断？

### Environment

```Shell
unbuntu 22.04 v100*8 lmdeploy 0.12.1
```

### Error traceback

```Shell

```

## 评论 (6)

### lvhan028 · 2026-03-10

LMDeploy 忘记添加 GLM 的 reasoning parser 和 tool call parser了。我们添加下。
关于截断的问题，你是源码编译的 lmdeploy 么？main 分支最近对 GLM 的显存占用做过一些优化



### simonjhy · 2026-03-10

不是，直接使用你们发布的docker image

### simonjhy · 2026-03-14

那我基于docker image，可以在配置参数里直接给glm 4.7 flash的配置参数加上下面的参数吗？

--tool-call-parser glm47
--reasoning-parser glm45 \

### simonjhy · 2026-03-14

我加上之后，提示
The reasoning parser glm45 is not in the parser list: dict_keys(['deepseek-r1', 'qwen-qwq', 'intern-s1'])

这个你们计划给glm 4.7 添加上这个支持吗？

### lvhan028 · 2026-03-20

后续会加

### lvhan028 · 2026-08-05

已支持
