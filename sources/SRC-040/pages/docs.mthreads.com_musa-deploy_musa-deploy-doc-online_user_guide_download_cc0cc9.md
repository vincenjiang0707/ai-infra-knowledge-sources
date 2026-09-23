source: https://docs.mthreads.com/musa-deploy/musa-deploy-doc-online/user_guide/download

# Download

Download 是用来下载摩尔线程对外发布的 AI 计算相关软件包。下载时，musa-deploy 会自动检测当前环境的 CPU 型号和操作系统版本，并下载与之匹配的软件包。若未指定版本号，将默认下载匹配的最新版本。

`sudo musa-deploy -d|--download <Package>[==<Version>] [--dir /target/path]`



参数说明：

`-d/--download`

: 指定需要下载的软件包名称以及版本号，其中版本号可缺省`--dir`

: 指定下载目录，缺省

**支持下载列表：**

| Package | CPU | OS | Version |
|---|---|---|---|
| sdk musa | Intel | Ubuntu | 3.1.1 3.1.0 3.0.1 4.0.0 4.1.0 |
| sdk musa | Hygon | Kylin V10 | 2.5.0 |
| sdk musa | Kunpeng920 | Kylin V10 | 2.5.0 |
| mudnn | Intel | Ubuntu | 2.7.0 2.6.1 |
| mudnn | Hygon | Kylin V10 | 2.3.1 |
| mudnn | Kunpeng920 | Kylin V10 | 2.3.1 |
| mccl | Intel | Ubuntu | 1.7.0 1.6.1 |
| container_toolkit | Intel Hygon | Ubuntu | 1.9.0 2.0.0 |
| smartio | Intel | Ubuntu | 1.2 |
| mutriton | Intel | Ubuntu | 1.0.0 |

下载 container_toolkit 的示例结果如下图：