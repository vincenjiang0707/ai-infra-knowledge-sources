source: https://docs.mthreads.com/musa-deploy/musa-deploy-doc-online/user_guide/install

# Install/Uninstall

# Install

用于安装指定的 MUSA 相关软件包，musa-deploy 会自动处理依赖关系，并确保版本匹配，简化安装流程。如果依赖包未安装，那么工具会自动安装依赖包。

`sudo musa-deploy -i <Package>[==Version] [-f|--force]`



`Package`

：指定安装的 MUSA 相关软件包名；`Version`

：支持指定具体版本，可省，默认安装最新匹配版本；`-f/--force`

: 如果已存在其他版本的软件包，程序默认会退出并提示错误。使用 -f/--force 参数可跳过检查，强制重新安装。

**支持安装列表**：

| Package | CPU | OS | Version |
|---|---|---|---|
| host | Intel Hygon | Ubuntu | \ |
| driver | Intel Hygon | Ubuntu | 3.1.0 3.1.1 3.0.0-rc4.0.0-server 4.1.0 |
| container_toolkit | Intel Hygon | Ubuntu | 1.9.0 2.0.0 |

注：


- 安装
`host`

时会安装dkms和lightdm，它们是安装驱动必须的依赖；- 安装
`driver`

会自动检测 driver 的依赖包并安装依赖， 即可能会隐式调用`sudo musa-deploy -i host`

；- 如果当前节点被集群纳管， 则安装/更新 driver 会被阻止，请联系集群管理员；
- 如果机器中
`/etc/modprobe.d/drivertoolkit.conf`

文件存在，说明该机器被集群纳管，或者刚被剔除集群，此时工具会阻止 driver 安装，请手动删除改文件，再重试安装。

安装驱动的示例结果如下图所示：

# Uninstall

用于卸载指定的 MUSA 软件包，支持保留依赖或完全卸载。

`sudo musa-deploy -u <Package>`




`Package`

参数同Install章节

卸载 container_toolkit 的示例结果如下图所示：