source: https://docs.opencloudos.org/OCS/Network_Guide/NTP_config/

# NTP 配置指南

NTP（网络时间协议）用于同步网络上的计算机和其他设备的时钟。使用 NTP 可以解决如下问题： 1. 大多数机器中的内置硬件时钟，由于温度、电压和其他因素的变化，可能会随着时间的推移而出现漂移，从而给时间敏感的应用程序和服务带来问题。 2. 在网络中，通常需要同步机器的系统时间，但手动调整时间是一种不好的方法，可能会导致一些严重问题，例如向后调整时间将使关键应用程序出现故障。

系统采用 chrony 作为 NTP 的默认实现。

## 1 了解和配置 chrony

系统默认安装chrony，您可以使用 chrony:

- 将系统时钟与 NTP 服务器同步
- 将系统时钟与参考时钟同步
- 将系统时钟与手动输入的时间同步
- 作为 NTP 服务器或 NTP 对等服务器，为网络中的其他计算机提供时间服务

chrony 在各种条件下表现良好。通过互联网同步的两台机器之间的准确性通常在几毫秒之内，对于 LAN 中的机器则为几十微秒。

chrony 包含 chronyd 和 chronyc，chronyd 守护程序可在引导时启动，chronyc 命令行程序用于与chronyd服务器进行交互，查询和调整系统时钟。

### 1.1 chronyd 配置

chronyd 的配置文件位于 /etc/chrony.conf。可以使用文本编辑器打开该文件，并根据需要修改配置选项。

系统的 /etc/chrony.conf 文件的默认配置如下：

```
# Use public servers
server ntp1.tencent.com iburst
server ntp2.tencent.com iburst
server cn.pool.ntp.org iburst
# Use NTP servers from DHCP.
sourcedir /run/chrony-dhcp
# Record the rate at which the system clock gains/losses time.
driftfile /var/lib/chrony/drift
# Allow the system clock to be stepped in the first three updates
# if its offset is larger than 1 second.
makestep 1.0 3
# Enable kernel synchronization of the real-time clock (RTC).
rtcsync
# Specify file containing keys for NTP authentication.
keyfile /etc/chrony.keys
# Save NTS keys and cookies.
ntsdumpdir /var/lib/chrony
# Specify directory for log files.
logdir /var/log/chrony
```


- server：指定NTP服务器的地址，格式为
`server <host> <options>`

，可多个 server 字段指定多个服务器。options 可选设置如下参数：- ibust 会在 chrony 启动的2秒内，去快速poll服务器4次来快速矫正当前系统时间
- prefer 优先使用指定的服务器，若没有指定，则按照文件中的 NTP 的顺序来确定优先级

- sourcedir： chronyd在启动时查找指定目录中的额外配置文件
例如默认设置
`sourcedir /run/chrony-dhcp`

，表示 chronyd 在启动时查找`/run/chrony-dhcp`

目录中的额外配置文件。当 DHCP 客户端获取到 IP 地址时，会解析 DHCP 响应中 NTP 服务器选项，若有 NTP 服务器选项则会创建配置文件到`/run/chrony-dhcp`

目录中。 - makestep ： 指定系统启动时是否使用 makestep 命令。
例如默认设置
`makestep 1.0 3`

，第一个参数设置为1.0，表示系统时钟与NTP服务器的时差如果超过1.0秒，将触发makestep进行立即修正。第二个参数设置为3，表示在整个chrony运行期间最多只允许执行3次这种立即跳变。这种默认设置确保了系统在启动时能够快速修正时钟。 - rtcsync ：chronyd 将实时时钟 (RTC) 同步到系统时钟。确保系统在重新启动时或从低电源状态恢复时具有更准确的时间。
- keyfile：指定了存储加密密钥的文件的位置。这些密钥被用于通过 Message Authentication Code (MAC) 来验证 NTP 协议数据包，以增强安全性。
- ntsdumpdir：指定在系统无法与外部 NTP 服务器通信时，周期性地将NTP服务器数据（即NTP服务器样本）保存的目录目录。当网络重新连接后，chronyd 将从此目录加载保存的 NTP 服务器数据，以改进时钟同步和时间估算的准确性。
- driftfile：指定 chrony 将时钟偏移信息存储在指定的文件中。driftfile 设置对于维持系统时钟的长期准确性非常重要。它让 chrony 能够在重启之间保存和恢复时钟的偏移信息。
- logdir：指定日志文件的路径。
`logdir /var/log/chrony`


默认配置使用 chrony 与 NTP 服务器同步时间，但不作为 NTP 服务器给网络中的其他计算机提供 NTP 服务，可添加 allow 配置项来配置此能力。其他默认未启用的配置项（如 allow）的配置项说明如下：

- allow：指定允许访问 chronyd 的客户端 IP 地址或网段。如果没有配置 allow，那么客户端默认情况下将无法连接到此 chronyd 服务器以进行 NTP 同步。如在局域网中作为 NTP 服务器为其他计算机提供 NTP 服务，允许 192.168.1.0/24 网段的客户端连接以进行 NTP 同步，则添加如下配置项：
`allow 192.168.1.0/24`

- log：指定日志文件要记录的信息。例如：
`log measurements statistics tracking`

- measurements：此选项将原始 NTP 测量以及相关信息记录到名为 measurements.log 的文件。
- statistics：将有关递归处理的信息记录到名为 statistics.log 的文件。
- tracking： 此选项将系统速率或丢失率估算的更改记录到名为 trace.log 的文件。
- rtc： 此选项记录有关系统实时时钟的信息。
- refclocks： 此选项将原始和过滤的参考时钟测量记录到名为 refclocks.log 的文件。
- tempcomp： 此选项将温度测量和系统速率记录到名为 tempcomp.log 的文件


配置文件修改完成后，您需要使用以下命令启动 chronyd 服务：

```
systemctl start chronyd
```


```
systemctl restart chronyd
```


```
systemctl enable chronyd
```


## 1.2 使用 chronyc

chronyc用于与chronyd服务器进行交互，查询和调整系统时钟。 以下是chronyc的一些常用命令和用法：

- chronyc sources：查看当前使用的NTP服务器和它们的状态信息，在下面的示例中，*表示该服务器正在使用，+表示该服务器被选择为备用服务器，-表示被认为可选择用于同步的服务器，但当前被排除在备选服务器列表之外。
`# chronyc sources 210 Number of sources = 3 MS Name/IP address Stratum Poll Reach LastRx Last sample =============================================================================== ^* ntp1.example.com 2 6 17 10 -266us[ -266us] +/- 100ms ^+ ntp2.example.com 2 6 17 10 -123us[ -123us] +/- 100ms ^- ntp3.example.com 2 6 17 10 -345us[ -345us] +/- 100ms`

- chronyc sourcestats：显示目前被 chronyd 检查的每个源的偏移率和误差估算过程的信息。
`# chronyc sourcestats Name/IP Address NP NR Span Frequency Freq Skew Offset Std Dev ============================================================================== ntp1.example.com 48 22 377m +0.012 0.100 +325us 1428us ntp2.example.com 38 14 359m -0.009 0.111 -356us 1297us ntp3.example.com 0 0 0 +0.000 2000.000 +0ns 4000ms`

- chronyc tracking：查看系统时钟的偏差和精度。在下面的示例中，System time表示系统时钟与参考时钟之间的时间差，Last offset表示最近一次的时间偏差，RMS offset表示时间偏差的均方根值，Frequency表示时钟频率的偏差。
`## chronyc tracking Reference ID : 192.168.1.1 (ntp1.example.com) Stratum : 3 Ref time (UTC) : Fri Jul 23 15:07:26 2021 System time : 0.000008782 seconds fast of NTP time Last offset : -0.000000065 seconds RMS offset : 0.000010194 seconds Frequency : 17.065 ppm fast Residual freq : -0.000 ppm Skew : 0.000 ppm Root delay : 0.004033 seconds Root dispersion : 0.000000 seconds Update interval : 64.0 seconds Leap status : Normal`

- chronyc makestep：立即调整系统时钟，使其与参考时钟同步。
`chronyc makestep`