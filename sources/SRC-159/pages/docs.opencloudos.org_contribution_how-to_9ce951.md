source: https://docs.opencloudos.org/contribution/how-to/

# 如何贡献

欢迎贡献 OpenCloudOS！

## 贡献 OpenCloudOS

## 贡献文档

- Fork
[文档仓库](https://gitee.com/OpenCloudOS/Document) -
将您 Fork 后的文档仓库 clone 至本地

`git clone git@gitee.com:yourname/OpenCloudOS/Document.git # (1)`

1.（你需要将

`yourname`

更换为你自己的 Gitee 用户名） -
安装环境

- 安装 Python 3.x
- 安装
[mkdocs-material](https://squidfunk.github.io/mkdocs-material/)及多语言插件

`pip install mkdocs-material mkdocs-static-i18n`

- 在本地运行预览服务器

`mkdocs serve`

-
可以开始贡献啦！

-
在本地通过预览服务器确认内容与格式正确后，commit 您的修改。

- 向
[文档仓库](https://gitee.com/OpenCloudOS/Document)提交 Pull Request，待维护者审核通过后，会进行手动合并，或者CI流水线审核通过后自动合并，合并完成稍等片刻后，清除网页缓存后，刷新网页就能看到修改结果，正式网站会每周日同步更新。