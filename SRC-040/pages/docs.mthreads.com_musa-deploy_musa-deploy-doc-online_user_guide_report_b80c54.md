source: https://docs.mthreads.com/musa-deploy/musa-deploy-doc-online/user_guide/report

# Report

report 功能是输出当前环境下重要的软硬件信息报告，命令如下：

`sudo musa-deploy [ -r | --report ]`



下图是 s4000 GPU 服务器，host 上生成的 report 结果：

下面解释其中重要的条目：

- 条目 0~6 是对应组件的安装状态。上图显示的是 host 上执行结果，如果不在 host 上直接开发，那么没有安装是正常的。如果在 docker 容器中开发，可以在 docker 容器中执行 report 命令查看组件状态。
- 条目 7~9 显示的是驱动版本信息。
- 条目 17 显示的是操作系统 kernel 版本，对于 s4000 GPU，建议 kernel 是 5.15.0-xxx。
- 条目 20 显示的是 IOMMU 的状态，对于 s4000 GPU，这里必须是开启状态，如果显示 disable，可通过 sudo musa-deploy -c host 获取开启 IOMMU 方法。
- 条目 24 显示服务器是否被集群纳管。如果服务器被集群纳管，那么不能私自手动更换驱动，需要联系集群管理员来更换服务器驱动，此时请谨慎使用该工具。
- 条目 25 显示当前用户是否在 Render group。如果当前用户不在 Render group，那么可能会导致 musa 环境搭建失败。