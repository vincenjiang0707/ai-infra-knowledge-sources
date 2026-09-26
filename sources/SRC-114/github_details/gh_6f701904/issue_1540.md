# [Issue #1540] need to run this command from the toplevel of the working tree.

source: https://github.com/mlcommons/inference/issues/1540
state: closed | updated: 2026-05-10T00:42:52Z
labels: Stale

## 正文

[root@poc4 bert]# make setup
make[1]: Entering directory '/home/sunyu/benchmark/MLPerf/inference/language/bert'
You need to run this command from the toplevel of the working tree.
make[1]: *** [init_submodule] Error 1
make[1]: Leaving directory '/home/sunyu/benchmark/MLPerf/inference/language/bert'
make: *** [setup] Error 2

--------------------------------------
Why did I get this error when I ran `make setup` on node 68, but it worked on node 69? The 68-node configuration is identical to the 69-node configuration.
Although this error has been fixed, the solution:
1.`rm -rf DeepLearningExamples`
2.`git submodule add < repository_url> DeepLearningExamples`
3.`make setup`

So my question is why did it go wrong at 68-node, and why did my approach work?

## 评论 (1)

### github-actions[bot] · 2026-05-10

🔒 This issue has been **automatically closed** because it has been open for more than 2 years with no activity.
If this is still relevant, you may **reopen it or create a new one**.
