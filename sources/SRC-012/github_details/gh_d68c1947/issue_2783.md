# [Issue #2783] very slow on Mac m3

source: https://github.com/mlc-ai/mlc-llm/issues/2783
state: closed | updated: 2026-03-01T20:45:36Z
labels: bug

## 正文

## 🐛 Bug

When I ask first few questions in chat, the app (with  Mistral 7b model) is able to generate answers very fast - 2000 tokens/min. But at some point, it starts slow down, and I am getting about 5tokens/min. The same model work very fast with another solution - LLMFarm. Even Gemma model work only for first 10-20 questions next it starts slow down to 5tokens/min.

## To Reproduce

Steps to reproduce the behavior:

1. Download  MLC Chat from Apple store to Mac with m3
2. Choose Mistral 7b model
3. Aks few questions in chat


<!-- A clear and concise description of what you expected to happen. -->

## Environment

 - Operating system (e.g. Ubuntu/Windows/MacOS/...): Macos
 - Device (e.g. iPhone 12 Pro, PC+RTX 3090, ...): Macbook Pro
 - How you installed MLC-LLM (`conda`, source): Apple store



## 评论 (2)

### caishiqing · 2024-09-06

The same problem on android, minicpm model. First two questions are fast, then become very slow. Do you solve it?

### aiakubovich · 2024-09-06

@caishiqing nope, I do not...
