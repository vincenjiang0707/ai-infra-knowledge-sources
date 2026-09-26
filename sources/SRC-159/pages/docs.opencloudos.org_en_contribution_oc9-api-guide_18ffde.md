source: https://docs.opencloudos.org/en/contribution/oc9-api-guide/

# OpenCloudOS 9 API 文档

## 基础库部分

| 序号 | 介绍 | 包名 | 版本 | 共享对象名 |
|---|---|---|---|---|
| 1 | 核心系统函数库，实现了C语言国际标准（ISO/IEC 9899）与操作系统接口规范，为应用程序提供内存、文件和进程等基础系统服务的编程接口。 | glibc | 2.38 | libBrokenLocale.so.1 |
| libanl.so.1 | ||||
| libc.so.6 | ||||
| libdl.so.2 | ||||
| libm.so.6 | ||||
| libnsl.so.1 | ||||
| libnss_compat.so.2 | ||||
| libnss_dns.so.2 | ||||
| libnss_files.so.2 | ||||
| libnss_hesiod.so.2 | ||||
| libpthread.so.0 | ||||
| libresolv.so.2 | ||||
| librt.so.1 | ||||
| libthread_db.so.1 | ||||
| libutil.so.1 | ||||
| 密码安全函数库，为应用程序安全处理密码哈希提供生成、验证和算法管理等标准编程接口。 | libxcrypt | 4.4.36 | libcrypt.so.1 | |
| 2 | 可插拔认证模块，为系统及应用软件提供统一的身份认证服务接口。 | pam | 1.5.3 | libpamc.so.0 |
| libpam_misc.so.0 | ||||
| libpam.so.0 | ||||
| 3 | ELF（可执行与可链接格式，Executable and Linkable Format）文件分析工具集，提供读写、解析及诊断ELF格式文件的底层库与实用工具。 | elfutils | 0.190 | libasm.so.1 |
| libdw.so.1 | ||||
| libelf.so.1 | ||||
| 4 | 数据压缩库，实现了 DEFLATE 压缩算法，支持 ZLIB和GZIP标准数据压缩格式，为应用程序提供通用的数据压缩与解压缩编程接口。 | zlib | 1.2.13 | libz.so.1 |
| 5 | GNU编译器套件，实现了C、C++等编程语言的国际标准，为应用程序开发提供标准化的编译器和C++标准库。 | gcc | 12.3.0 | libatomic.so.1 |
| libgcc_s.so.1 | ||||
| libgomp.so.1 | ||||
| libstdc++.so.6 | ||||
| 6 | 网络身份认证系统，实现了Kerberos网络认证协议，为应用程序提供安全的身份验证、凭据管理与加密通信编程接口。 | krb5 | 1.21.2 | libgssapi_krb5.so.2 |
| libgssrpc.so.4 | ||||
| libk5crypto.so.3 | ||||
| libkrad.so.0 | ||||
| libkrb5.so.3 | ||||
| libkrb5support.so.0 | ||||
| 7 | 系统安全审计框架，提供内核级系统调用与安全事件的监控、记录及规则配置能力。为应用程序提供生成与查询审计日志的编程接口。 | audit | 3.1.2 | libaudit.so.1 |
| libauparse.so.0 | ||||
| 8 | 高质量数据压缩库，采用Burrows-Wheeler块排序算法进行无损数据压缩，为应用程序提供高效的压缩与解压缩编程接口。 | bzip2 | 1.0.8 | libbz2.so.1 |
| 9 | 消息总线系统，为应用程序与服务提供进程间通信机制，实现服务间的消息传递与生命周期协调。 | dbus | 1.14.8 | libdbus-1.so.3 |
| 10 | XML解析库，通过流式解析技术实现对大型XML文档的高效处理，为应用程序提供XML文档解析编程接口。 | expat | 2.5.0 | libexpat.so.1 |
| 11 | 提供一个核心编程的基础库，包含数据结构、类型转换、字符串处理、跨平台支持等通用工具函数集合。 | glib2 | 2.78.3 | libgio-2.0.so.0 |
| libglib-2.0.so.0 | ||||
| libgmodule-2.0.so.0 | ||||
| libgobject-2.0.so.0 | ||||
| libgthread-2.0.so.0 | ||||
| 12 | 鼠标指针控制程序，用于在终端（命令行界面）下提供鼠标操作支持。 | gmp | 6.3.0 | libgmp.so.10 |
| 13 | 主要对国际化域名进行编码和解码，用于处理和转换支持非ASCII字符的域名。 | libidn2 | 2.3.4 | libidn2.so.0 |
| 14 | 终端界面处理库，允许开发者创建基于文本的用户界面，控制光标和界面显示。 | ncurses | 6.4 | libform.so.6 |
| libformw.so.6 | ||||
| libmenu.so.6 | ||||
| libmenuw.so.6 | ||||
| libncurses.so.6 | ||||
| libncursesw.so.6 | ||||
| libpanel.so.6 | ||||
| libpanelw.so.6 | ||||
| libtic.so.6 | ||||
| libtinfo.so.6 | ||||
| 15 | 提供高性能的数据压缩工具库，基于LZMA2算法实现对文件的压缩和解压缩，一般包名为"xz"或"xz-utils" | xz | 5.4.4 | liblzma.so.5 |
| 16 | 提供了对进程权限的管理能力，支持权限分离和管控，保障系统资源访问的安全。 | libcap | 2.69 | libcap.so.2 |
| 17 | 命令行参数解析库，用于简化应用程序从命令行接收和处理配置选项的过程。 | popt | 1.19 | libpopt.so.0 |
| 18 | 网络配置和管理库，用于与内核的网络配置接口进行通信和交互。 | libnl3 | 3.7.0 | libnl-3.so.200 |
| libnl-cli-3.so.200 | ||||
| libnl-genl-3.so.200 | ||||
| libnl-idiag-3.so.200 | ||||
| libnl-nf-3.so.200 | ||||
| libnl-route-3.so.200 | ||||
| libnl-xfrm-3.so.200 | ||||
| 19 | 密钥和敏感信息存储库，提供一个标准接口用于应用程序安全地存储密码或密钥。 | libsecret | 0.20.5 | libsecret-1.so.0 |
| 21 | 通用内存池管理库，用于管理动态分配的内存块，简化内存的分配和释放。 | libtalloc | 2.4.1 | libtalloc.so.2 |
| 22 | 一个事件系统的实现库，提供基于talloc的内存管理功能，支持如计时器、信号、经典文件描述符等事件类型。talloc：一个轻量级内存管理库，它提供了一种层次化内存分配机制。 | libtevent | 0.16.0 | libtevent.so.0 |
| 23 | 一个基于通用基础库（GLib）的进程间通信扩展库，用于实现基于消息总线的消息传递与事件循环。一般包名为"dbus-glib"或"libdbus-glib-1-2"等。<br>GLib(General Utility Library）：是通用基础函数库，提供数据结构、内存管理、事件循环、线程及对象系统等基础功能，为上层图形界面库和应用程序提供底层支持。 | dbus-glib | — | — |
| 24 | 一个用于管理文件系统扩展属性的工具，提供查询与设置文件扩展属性的功能，用于支持文件的附加元数据操作。 | attr | 2.5.1 | libattr.so.1 |
| 25 | 一个异步事件通知库，提供事件监听与回调机制，可在文件描述符事件或定时事件触发时执行回调，用于构建事件驱动的网络与系统程序。 | libevent | 2.1.12 | libevent-2.1.so.7 |
| libevent_core-2.1.so.7 | ||||
| libevent_extra-2.1.so.7 | ||||
| libevent_openssl-2.1.so.7 | ||||
| libevent_pthreads-2.1.so.7 | ||||
| 26 | 提供基于 D-Bus（桌面总线系统）的用户账户信息查询与管理接口，用于支持系统中用户账户的创建、修改与删除操作。<br>D-Bus，英文全称Desktop Bus，中文全称桌面总线系统 | accountsservice | 22.08.8 | libaccountsservice.so.0 |
| 27 | 一个用于任意高精度复数运算且能正确舍入结果、在高精度下保持运算速度的 C 语言库。一般包名为"libmpc3"或"libmpc"等。 | libmpc | 1.3.1 | libmpc.so.3 |
| 28 | 一个用于多精度浮点计算且具备正确舍入功能、兼具高效性与严谨语义的C语言库。一般包名为"mpfr4"或"mpfr"等。 | mpfr | 4.2.1 | libmpfr.so.6 |
| 29 | 一个用于管理内核中非易失性内存设备子系统的实用工具库。 | ndctl | 78 | libdaxctl.so.1 |
| 30 | 一个命令行式的文件类型识别器，通过命令行以文字形式告知文件所含数据类型的工具，根据文件包含的数据类型来识别特定文件。 | file | 5.45 | libmagic.so.1 |
| 31 | 一个采用可扩展哈希算法的数据库函数库，用于将键值对存储在数据文件中。一般包名为"gdbm"或"gdbm-libs"等。 | gdbm | 1.23 | libgdbm.so.6 |
| libgdbm_compat.so.4 | ||||
| 32 | 一组命令行工具集和库，用于与系统内核的 密钥管理服务（Key Retention Service） 进行交互，提供用户空间访问这些密钥的接口。 | keyutils | 1.6.3 | libkeyutils.so.1 |
| 33 | 一个轻量、高效的命令行输入编辑库，提供 交互式文本编辑和历史记录功能。 | libedit | 3.1 | libedit.so.0 |
| 34 | 一个在系统中用于控制NUMA（Non-Uniform Memory Access，非统一内存访问）策略的命令行工具，同时提供简单的编程接口。 | numactl | 2.0.16 | libnuma.so.1 |
| 35 | 系统中一个核心且基础的工具集合包，包含了大量用于系统管理、磁盘操作、进程控制、终端交互等日常任务的命令行实用程序。 | util-linux | 2.39.1 | libuuid.so.1 |
| libblkid.so.1 | ||||
| libmount.so.1 |

## 操作系统安全库

| 序号 | 介绍 | 包名 | 版本 | 共享对象名 |
|---|---|---|---|---|
| 1 | 管理访问控制列表工具库，可以对同一个文件或目录同时为多个不同的用户或组设置不同的访问权限，从而提高系统的安全性。 | acl | 2.3.1 | libacl.so.1 |
| 2 | 实现了简单认证和安全层规范的函数库，用于为网络应用提供客户端与服务器端的身份认证能力。其通过一个通用框架整合了多种认证机制，使得应用程序可以更容易地集成安全功能。其软件包名称通常为 cyrus-sasl 或 cyrus-sasl2。 | cyrus-sasl | 2.1.28 | libsasl2.so.3 |
| libanonymous.so.3 | ||||
| libsasldb.so.3 | ||||
| libcrammd5.so.3 | ||||
| libdigestmd5.so.3 | ||||
| libgs2.so.3 | ||||
| libgssapiv2.so.3 | ||||
| libldapdb.so.3 | ||||
| liblogin.so.3 | ||||
| libntlm.so.3 | ||||
| libplain.so.3 | ||||
| libscram.so.3 | ||||
| 3 | 通用加解密方法实现库，支持多种加密算法，包括对称加密算法、非对称加密算法、哈希算法以及随机数生成器等。提供高度安全的加密功能，同时保持高性能和易用性。一般包名"libgcrypt20"或"libgcrypt"等。 | libgcrypt | 1.10.2 | libgcrypt.so.20 |
| 4 | 传输层安全协议库，支持多种加密协议和算法，提供一种简单的接口，使得应用程序更容易实现安全数据传输。一般包名为"gnutls28"或"gnutls"等。 | gnutls | 3.8.2 | libgnutls-dane.so.0 |
| libgnutls.so.30 | ||||
| libgnutlsxx.so.30 | ||||
| 5 | 一个用来访问SSH(Secure Shell 、安全外壳协议)服务的实现库，支持多种协议，支持执行远程命令、文件传输，并能为远程的程序提供安全的传输通道。libssh易于使用、可移植性好、性能高、安全可靠，应用于网络管理、远程维护、云计算等多个领域。 | libssh | 0.10.5 | libssh.so.4 |
| libssh_threads.so.4 | ||||
| C语言函数库，实现SSH2（Secure Shell Protocol Version 2 、安全外壳协议版本 2）协议，支持密钥交换方法、主机密钥类型、密码套件、压缩方法等，提供了更完善的SSH（Secure Shell、 安全外壳协议） 接口和更先进的功能。 | libssh2 | 1.11.0 | libssh2.so.1 | |
| 6 | 密码安全性测试工具库，用于增强用户密码的强度。可以检查用户输入的密码强度，并根据预设的规则提示用户输入更加安全的密码，防止密码被破解，提高系统的安全性。一般包名为"cracklib2"或"cracklib"等。 | cracklib | 2.9.11 | libcrack.so.2 |
| 密码安全性测试工具库，用于检测用户密码的强度。它提供了一组函数，开发人员可以根据需求和配置来检查密码规则，以保证密码的强度和安全性。一般包名为"libpwquality1"或"libpwquality"等。 | libpwquality | 1.4.5 | libpwquality.so.1 | |
| 7 | 一个为底层系统操作提供跨平台抽象接口的运行时库，主要用于屏蔽不同操作系统在基础功能上的差异。其提供的跨平台进程和线程抽象，是构建这种强大安全隔离机制的基础。 | nspr | 4.35.0 | libnspr4.so |
| libplc4.so | ||||
| libplds4.so | ||||
| 通用加密库的实现库，支持多种加密算法和协议。用于安全通信，能避免密码窃听及进行通信者身份确认，保护网络通信的隐私和完整性。 | openssl | 3.0.12 | libcrypto.so.3 | |
| libssl.so.3 | ||||
| 8 | 为系统调用过滤机制提供了一个易于使用的接口。libseccomp 接口允许应用程序指定允许执行的系统调用以及可选的系统调用参数。 | libseccomp | 2.5.4 | libseccomp.so.2 |

## OS网络库

| 序号 | 介绍 | 包名 | 版本 | 共享对象名 |
|---|---|---|---|---|
| 1 | 操作系统中的网络连接和管理服务，能自动配置和管理有线、无线等多种类型的网络连接，并允许用户对IP地址、路由等参数进行设置与管理。 | NetworkManager | 1.44.2 | libnm-device-plugin-adsl.so |
| libnm-device-plugin-ovs.so | ||||
| libnm-device-plugin-team.so | ||||
| libnm-settings-plugin-ifcfg-rh.so | ||||
| libnm.so.0 | ||||
| 2 | 提供一组守护进程来管理对远程目录和身份验证机制，用于集中管理身份认证、访问授权和信息查询。 | sssd | 2.9.4 | libipa_hbac.so.0 |
| libsss_certmap.so.0 | ||||
| libsss_idmap.so.0 | ||||
| libsss_nss_idmap.so.0 | ||||
| 3 | 独立于传输的远程过程调用库，是实现网络计算中进程间通信的基础运行库，不依赖于特定传输协议。 | libtirpc | 1.3.4 | libtirpc.so.3 |
| 4 | 网络安全服务是一组安全库，提供传输层安全协议实现、证书管理及加密算法等功能，支撑安全通信应用。 | nss | 3.94.0 | libnss3.so |
| libnsssysinit.so | ||||
| libsmime3.so | ||||
| libssl3.so | ||||
| 5 | 跨平台的数据包捕获函数库，为上层网络工具提供底层抓包接口。支持多种网络协议，可直接与网卡驱动交互，实现原始数据包的捕获、过滤和分析。 | libpcap | 1.10.4 | libpcap.so.1 |
| 6 | 客户端命令行网页数据传输工具，支持多种网络通信协议，用于获取网页内容、文件下载上传等操作。提供代理服务器支持、用户身份验证、数据缓存管理等功能。 | curl | 8.4.0 | libcurl.so.4 |
| 7 | 内核内置的数据包处理框架，具备包过滤、网络地址转换与流量管控能力。通过规则链定义网络访问策略，是构建系统防火墙、管理网络流量的核心工具。 | iptables | 1.8.9 | libarpt_mangle.so |
| libebt_802_3.so | ||||
| libebt_arp.so | ||||
| libebt_dnat.so | ||||
| libebt_ip6.so | ||||
| libebt_ip.so | ||||
| libebt_log.so | ||||
| libebt_mark_m.so | ||||
| libebt_mark.so | ||||
| libebt_nflog.so | ||||
| libebt_pkttype.so | ||||
| libebt_redirect.so | ||||
| libebt_snat.so | ||||
| libebt_stp.so | ||||
| libebt_vlan.so | ||||
| libip6t_ah.so | ||||
| libip6t_mh.so | ||||
| libip6t_NETMAP.so | ||||
| libip6t_REJECT.so | ||||
| libip6t_rt.so | ||||
| libip6t_SNPT.so | ||||
| libip6t_srh.so | ||||
| libipt_ah.so | ||||
| libipt_CLUSTERIP.so | ||||
| libipt_ECN.so | ||||
| libipt_icmp.so | ||||
| libipt_NETMAP.so | ||||
| libipt_realm.so | ||||
| libipt_REJECT.so | ||||
| libipt_ttl.so | ||||
| libipt_TTL.so | ||||
| libipt_ULOG.so | ||||
| libxt_addrtype.so | ||||
| libxt_AUDIT.so | ||||
| libxt_bpf.so | ||||
| libxt_cgroup.so | ||||
| libxt_CHECKSUM.so | ||||
| libxt_CLASSIFY.so | ||||
| libxt_cluster.so | ||||
| libxt_comment.so | ||||
| libxt_connbytes.so | ||||
| libxt_connlabel.so | ||||
| libxt_connlimit.so | ||||
| libxt_connmark.so | ||||
| libxt_CONNMARK.so | ||||
| libxt_CONNSECMARK.so | ||||
| libxt_conntrack.so | ||||
| libxt_cpu.so | ||||
| libxt_CT.so | ||||
| libxt_dccp.so | ||||
| libxt_devgroup.so | ||||
| libxt_dscp.so | ||||
| libxt_DSCP.so | ||||
| libxt_ecn.so | ||||
| libxt_esp.so | ||||
| libxt_hashlimit.so | ||||
| libxt_helper.so | ||||
| libxt_HMARK.so | ||||
| libxt_IDLETIMER.so | ||||
| libxt_ipcomp.so | ||||
| libxt_iprange.so | ||||
| libxt_ipvs.so | ||||
| libxt_LED.so | ||||
| libxt_length.so | ||||
| libxt_limit.so | ||||
| libxt_mac.so | ||||
| libxt_mark.so | ||||
| libxt_MARK.so | ||||
| libxt_multiport.so | ||||
| libxt_nfacct.so | ||||
| libxt_NFLOG.so | ||||
| libxt_NFQUEUE.so | ||||
| libxt_NOTRACK.so | ||||
| libxt_osf.so | ||||
| libxt_owner.so | ||||
| libxt_physdev.so | ||||
| libxt_pkttype.so | ||||
| libxt_policy.so | ||||
| libxt_quota.so | ||||
| libxt_rateest.so | ||||
| libxt_RATEEST.so | ||||
| libxt_recent.so | ||||
| libxt_rpfilter.so | ||||
| libxt_sctp.so | ||||
| libxt_SECMARK.so | ||||
| libxt_set.so | ||||
| libxt_SET.so | ||||
| libxt_socket.so | ||||
| libxt_standard.so | ||||
| libxt_state.so | ||||
| libxt_statistic.so | ||||
| libxt_string.so | ||||
| libxt_SYNPROXY.so | ||||
| libxt_tcpmss.so | ||||
| libxt_TCPMSS.so | ||||
| libxt_TCPOPTSTRIP.so | ||||
| libxt_tcp.so | ||||
| libxt_TEE.so | ||||
| libxt_time.so | ||||
| libxt_tos.so | ||||
| libxt_TOS.so | ||||
| libxt_TPROXY.so | ||||
| libxt_TRACE.so | ||||
| libxt_u32.so | ||||
| libxt_udp.so | ||||
| libip4tc.so.2 | ||||
| libip6tc.so.2 | ||||
| libxtables.so.12 | ||||
| 8 | 提供支持通用互联网文件系统的工具集，允许系统访问和挂载网络上的共享文件和打印机。 | cifs-utils | 7.0 | idmapwb.so |
| pam_cifscreds.so | ||||
| 9 | 基于C++语言的可访问性编程接口库，为软件开发人员提供完整支持，帮助实现应用程序对辅助技术的兼容，让残障用户便捷操作各类软件界面。 | atkmm | 2.28.3 | libatkmm-1.6.so.1 |
| 10 | 用户空间与内核网络过滤子系统交互的库，提供对内核网络连接状态表的查询、监视和动态修改功能，为开发防火墙、数据包处理等工具提供编程接口。 | libnetfilter_conntrack | 1.0.9 | libnetfilter_conntrack.so.3 |

## OS编程语言库

| 序号 | 介绍 | 包名 | 版本 | 共享对象名 |
|---|---|---|---|---|
| 1 | 一种高级、面向对象、跨平台的通用编程语言。 | java | 11 | 无 |
| 17 | 无 | |||
| 21 | 无 | |||
| 1.8.0 | 无 | |||
| 2 | 一种解释型的动态编程语言，具有强大的文本处理能力。perl库用于开发嵌入Perl解释器的应用程序的文件。 | perl | 5.36.0 | 无 |
| 4 | 一种高级、通用、解释型的编程语言。python库用于Python解释器和运行Python程序时的运行库。 | Python | 3.11.6 | 无 |

## OS coding开发库

| 序号 | 介绍 | 包名 | 版本 | 共享对象名 |
|---|---|---|---|---|
| 1 | 一个用 C 语言编写的软件库，它提供了对可扩展标记语言（XML） 和超文本标记语言（HTML）文件的解析、验证、操作及生成等一系列强大功能。 | libxml2 | 2.11.5 | libxml2.so.2 |
| 2 | 一个用于堆栈展开和异常处理的库，支持跨平台的函数调用栈解析，应用于C++异常处理、性能分析等领域。 | libunwind | 1.6.2 | libunwind.so.8 |
| 3 | 一个用C语言编写的函数库，提供了与Perl语言正则表达式语法高度兼容的正则表达式解释器和执行器，一般包名为"pre3"或"pre" | pcre | 8.45 | libpcre.so.1 |

## OS基础数学计算库

| 序号 | 介绍 | 包名 | 版本 | 共享对象名 |
|---|---|---|---|---|
| 1 | 一个用于求解数值线性代数问题的函数库，主要功能包括求解线性方程组、线性最小二乘问题、特征值问题和奇异值分解等。 | lapack | 3.11.0 | libblas.so.3 |
| liblapack.so.3 | ||||
| liblapacke.so.3 |

## 分布式存储相关库

| 序号 | 介绍 | 包名 | 版本 | 共享对象名 |
|---|---|---|---|---|
| 1 | 一个分布式存储系统，支持块存储、对象存储和文件系统存储等方式，适用于大规模数据存储场景。 | ceph | 17.2.0 | libcls_cephfs.so.1 |
| libcls_hello.so.1 | ||||
| libcls_journal.so.1 | ||||
| libcls_lock.so.1 | ||||
| libcls_log.so.1 | ||||
| libcls_lua.so.1 | ||||
| libcls_numops.so.1 | ||||
| libcls_rbd.so.1 | ||||
| libcls_refcount.so.1 | ||||
| libcls_rgw.so.1 | ||||
| libcls_sdk.so.1 | ||||
| libcls_timeindex.so.1 | ||||
| libcls_user.so.1 | ||||
| libcls_version.so.1 | ||||
| libceph_snappy.so.2 | ||||
| libceph_zlib.so | ||||
| libceph_zstd.so | ||||
| libec_jerasure.so | ||||
| libec_jerasure_generic.so | ||||
| libec_lrc.so | ||||
| libec_shec.so | ||||
| libec_shec_generic.so | ||||
| libosd_tp.so | ||||
| libos_tp.so | ||||
| 2 | 一个基于内核的异步输入输出接口，允许应用程序在等待输入输出操作完成期间继续执行其他任务，提升输入输出性能。 | libaio | 0.3.113 | libaio.so.1 |
| 3 | 一个高性能异步输入输出框架，通过共享内存环形队列实现用户空间与内核空间的高效通信 | liburing | 2.3 | liburing.so.2 |

## OS虚拟化管理库

| 序号 | 介绍 | 包名 | 版本 | 共享对象名 |
|---|---|---|---|---|
| 1 | 虚拟化管理工具库，通过应用程序编程接口、守护进程和命令行工具实现对多种虚拟化技术的统一管理 | libvirt | 9.10.0 | libvirt-admin.so.0 |
| libvirt-lxc.so.0 | ||||
| libvirt-qemu.so.0 | ||||
| libvirt.so.0 | ||||
| libvirt_driver_interface.so | ||||
| libvirt_driver_network.so | ||||
| libvirt_driver_nodedev.so | ||||
| libvirt_driver_nwfilter.so | ||||
| libvirt_driver_qemu.so | ||||
| libvirt_driver_secret.so | ||||
| libvirt_driver_storage.so | ||||
| lockd.so | ||||
| libvirt_storage_backend_disk.so | ||||
| libvirt_storage_backend_fs.so | ||||
| libvirt_storage_backend_iscsi.so | ||||
| libvirt_storage_backend_iscsi-direct.so | ||||
| libvirt_storage_backend_logical.so | ||||
| libvirt_storage_backend_mpath.so | ||||
| libvirt_storage_backend_scsi.so | ||||
| libvirt_storage_backend_gluster.so | ||||
| libvirt_storage_file_fs.so |