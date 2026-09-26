# [Issue #706] The codebase is not compatible with its own clang-format settings

source: https://github.com/ai-dynamo/nixl/issues/706
state: open | updated: 2026-05-05T12:51:19Z
labels: Utilities/Infra, traning

## 正文

My pull request is being rejected by the clang-format checker in places where I haven't made any modifications. Moreover, applying clang-format to the codebase results in over 70 source files being modified, increasing the PR size to XL due to the lack of conformance to the formatting rules. 

Could clang-format be applied to the entire NIXL codebase?

## 评论 (1)

### yosefe · 2025-08-26

For now in order to make PR pass, need to update the code style in the surrounding area according to the clang-format style.
