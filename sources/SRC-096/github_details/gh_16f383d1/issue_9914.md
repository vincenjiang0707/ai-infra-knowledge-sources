# [Issue #9914] Performance regression in collectives due to UCX_PROTO_ENABLE

source: https://github.com/openucx/ucx/issues/9914
state: open | updated: 2026-03-25T14:15:38Z
labels: Bug

## 正文

I noticed a performance regression in OSU benchmark (OpenMPI with UCX and HCOLL) when using HPCX 2.17.1 compared to 2.14. It is due to the fact that now the `UCX_PROTO_ENABLE=y` by default. Setting it to `n` improves performance. Here are some results of `osu_alltoall`, but I have also tested and see problems for `allreduce`, `allgather`, `bcast`.

Results with HPCX 2.14 (`UCX_PROTO_ENABLE=n` by default)
```
mpirun -mca coll_hcoll_enable 1 ./osu_alltoall

# Size       Avg Latency(us)
1                      51.36
2                      53.33
4                      70.10
8                      94.39
16                    122.07
32                    172.27
64                    327.78
128                   723.52
256                  1186.84
512                  2497.48
1024                 4592.47
2048                 9028.02
4096                17379.87

mpirun -x UCX_PROTO_ENABLE=y -mca coll_hcoll_enable 1 ./osu_alltoall

# Size       Avg Latency(us)
1                      53.52
2                      50.51
4                     297.10
8                     268.56
16                    358.80
32                    438.63
64                    546.04
128                   766.01
256                  1372.77
512                  2476.39
1024                 4832.84
2048                 9732.90
4096                18742.74
```

Results with HPCX 2.17.1 (`UCX_PROTO_ENABLE=y` by default)
```
mpirun -x UCX_PROTO_ENABLE=n -mca coll_hcoll_enable 1  ./osu_alltoall

# Size       Avg Latency(us)
1                      52.17
2                      51.06
4                      82.29
8                     101.19
16                    122.21
32                    184.21
64                    434.94
128                   852.04
256                  1194.11
512                  2630.28
1024                 4827.78
2048                 8851.22
4096                17323.42


mpirun -mca coll_hcoll_enable 1 ./osu_alltoall

# Size       Avg Latency(us)
1                      51.98
2                     260.72
4                     259.26
8                     373.33
16                    337.10
32                    225.67
64                    412.54
128                  1025.74
256                  1369.04
512                  2850.56
1024                 5107.12
2048                 9550.65
4096                19212.82
```

## 评论 (18)

### ivankochin · 2024-06-03

Hi, could you please completely fill the bug template that is described during issue creation?

### angainor · 2024-06-04

@ivankochin Of course! here comes. Let me know if you need more info.

### Steps to Reproduce
- Command line: see error report
- UCX version used (from github branch XX or release YY) + UCX configure flags (can be checked by `ucx_info -v`)
```
bash-4.2$ ucx_info -v
# Library version: 1.16.0
# Library path: /cluster/software/hpcx/2.17.1/ucx/mt/lib/libucs.so.0
# API headers version: 1.16.0
# Git branch '', revision 02432d3
# Configured with: --disable-logging --disable-debug --disable-assertions --disable-params-check --enable-mt --with-knem --with-xpmem=/hpc/local/oss/xpmem/v2.7.1 --without-java --enable-devel-headers --with-fuse3-static --with-cuda=/hpc/local/oss/cuda12.2.2 --with-gdrcopy --prefix=/build-result/hpcx-v2.17.1-gcc-mlnx_ofed-redhat7-cuda12-x86_64/ucx/mt --with-bfd=/hpc/local/oss/binutils/2.37
```
- **Any UCX environment variables used**
`UCX_TLS=dc,sm,cuda,self`, or `UCX_TLS=ud,sm,cuda,self`, or without setting `UCX_TLS`

### Setup and versions
- OS version (e.g Linux distro) + CPU architecture (x86_64/aarch64/ppc64le/...)
   - `Red Hat Enterprise Linux Server release 7.7 (Maipo)`
   - `Linux b1331.betzy.sigma2.no 3.10.0-1062.9.1.el7.x86_64 #1 SMP Mon Dec 2 08:31:54 EST 2019 x86_64 x86_64 x86_64 GNU/Linux`
- For RDMA/IB/RoCE related issues:
    - Driver version:
        - ` MLNX_OFED_LINUX-5.5-1.0.3.2`
   - HW information from `ibstat` or `ibv_devinfo -vv` command
```
hca_id:	mlx5_0
	transport:			InfiniBand (0)
	fw_ver:				20.32.1010
	node_guid:			0800:3803:00b8:b188
	sys_image_guid:			0800:3803:00b8:b188
	vendor_id:			0x119f
	vendor_part_id:			4123
	hw_ver:				0x0
	board_id:			BL_12001644
	phys_port_cnt:			1
		port:	1
			state:			PORT_ACTIVE (4)
			max_mtu:		4096 (5)
			active_mtu:		4096 (5)
			sm_lid:			24
			port_lid:		386
			port_lmc:		0x00
			link_layer:		InfiniBand
```


### angainor · 2024-06-04

@ivankochin FYI, I have tried the same test on our older system (ConnectX-4), Rocky Linux release 9.2, MLNX_OFED_LINUX-5.8-3.0.7.0. It seems the performance is similar with both `UCX_PROTO_ENABLE=y` and `n`.

It seems in our case only the `ConnectX-6` is affected.

### angainor · 2024-06-04

I attach the output of `ucx_info -d` on the affected system.

[ucx_info.txt](https://github.com/user-attachments/files/15554811/ucx_info.txt)


### ivankochin · 2024-06-06

@angainor could you please also specify `UCX_PROTO_INFO=y UCX_PROTO_INFO_DIR=<path_to_dir_for_additional_logs>` for execution with `UCX_PROTO_ENABLE=y` and share the stdout + logs from directory specified for `_INFO_DIR` with me?

### angainor · 2024-06-06

@ivankochin This turned out to be a rather large file (70MB), too large to attach here. I've made it available for download here:

https://filesender.uio.no/?s=download&token=226c039d-abf0-4e8d-93ab-df04a8fee91e

Please let me know if you have problems accessing it.

### ivankochin · 2024-06-07

@angainor 
Thanks for the logs, they brought the sched of lite on how does PROTO_ENABLE select protocols in your case.
Also, I observe degradation on similar setup but it looks differently. 

So it would be great if you are able to do some extra experiments. I want to ask you to download the latest UCX master, build it in release mode (using `./contrib/configure-release`) and check that degradation still exists. If it is on place, pls recompile it in debug mode (using `./contib/configure-devel`) then run the reproducer with `UCX_PROTO_ENABLE=n UCX_LOG_LEVEL=req UCX_LOG_FILE=<path_to_log_dir>/osu_alltoall_v1_%h_%p.log` and share the generated files with me.

### angainor · 2024-06-07

The regression is still there, looks similar +- some glitches. I will recompile with debug and collect the logs.
```
mpirun -x UCX_PROTO_ENABLE=y -mca oob_tcp_if_include ib0 -mca coll_hcoll_enable 1 ./osu_alltoall -m 1:1024

# OSU MPI All-to-All Personalized Exchange Latency Test v7.4
# Datatype: MPI_CHAR.
# Size       Avg Latency(us)
1                      51.55
2                     248.02
4                     259.39
8                     339.29
16                    686.65
32                    278.23
64                    548.20
128                  1269.82
256                  1703.37
512                  2797.68
1024                 5200.94
```
```
ucx_info -v
# Library version: 1.18.0
# Library path: /cluster/home/marcink/software/ucx/master_2024/lib/libucs.so.0
# API headers version: 1.18.0
# Git branch '<unknown>', revision 0000000
# Configured with: --disable-logging --disable-debug --disable-assertions --disable-params-check --enable-mt --prefix=/cluster/home/marcink/software/ucx/master_2024
```
```
configure:34449: =========================================================
configure:34458: UCX build configuration:
configure:34460:         Build prefix:   /cluster/home/marcink/software/ucx/master_2024
configure:34462:    Configuration dir:   ${prefix}/etc/ucx
configure:34464:   Preprocessor flags:   -DCPU_FLAGS="" -I${abs_top_srcdir}/src -I${abs_top_builddir} -I${abs_top_builddir}/src
configure:34466:           C compiler:   gcc -O3 -g -Wall -Werror -funwind-tables -Wno-missing-field-initializers -Wno-unused-parameter -Wno-unused-label -Wno-long-long -Wno-endif-labels -Wno-sign-compare -Wno-multichar -Wno-deprecated-declarations -Winvalid-pch -Wno-language-extension-token -fno-finite-math-only -Wno-recommended-option -Wno-c99-extensions -Wno-pointer-sign -Werror-implicit-function-declaration -Wno-format-zero-length -Wnested-externs -Wshadow -Werror=declaration-after-statement
configure:34468:         C++ compiler:   g++ -O3 -g -Wall -Werror -funwind-tables -Wno-missing-field-initializers -Wno-unused-parameter -Wno-unused-label -Wno-long-long -Wno-endif-labels -Wno-sign-compare -Wno-multichar -Wno-deprecated-declarations -Winvalid-pch -Wno-language-extension-token -fno-finite-math-only -Wno-recommended-option -Wno-c99-extensions
configure:34470:           ASAN check:   no
configure:34472:         Multi-thread:   enabled
configure:34474:            MPI tests:   disabled
configure:34476:          VFS support:   no
configure:34478:        Devel headers:   no
configure:34480: io_demo CUDA support:   no
configure:34482:             Bindings:   < >
configure:34484:          UCS modules:   < >
configure:34486:          UCT modules:   < ib rdmacm cma knem >
configure:34488:         CUDA modules:   < >
configure:34490:         ROCM modules:   < >
configure:34492:           IB modules:   < >
configure:34494:          UCM modules:   < >
configure:34496:         Perf modules:   < mad >
configure:34505: =========================================================
```

### angainor · 2024-06-07

Here are logs from one process. I hope this is enough, otherwise the entire file is rather large. 

Note that this time I only ran the benchmark with message sizes up to 8 bytes due to the amount of logs.

Please let me know if this is ok, or if you need more.
[osu_alltoall_v1_b1238_90547.log.gz](https://github.com/user-attachments/files/15738353/osu_alltoall_v1_b1238_90547.log.gz)


### ivankochin · 2024-06-11

Thanks for all your efforts. 

Do I understand correctly that all the logs mentioned here were collected with `UCX_TLS=ud,sm,cuda,self`?

> Note that this time I only ran the benchmark with message sizes up to 8 bytes due to the amount of logs.

Are you sure? I see messages up to 2048 bytes in that log.

Root cause isn't still defined since according to logs both protov1 and protov2 uses same protocols. Could you please also re-measure `UCX_PROTO_ENABLE=y` separately with:
1) UCX_BCOPY_THRESH=1
2) UCX_ZCOPY_THRESH=1
3) UCX_RNDV_THRESH=1

### angainor · 2024-06-11


> Do I understand correctly that all the logs mentioned here were collected with `UCX_TLS=ud,sm,cuda,self`?

Yes, but as I mentioned before, this happens also if I specify DC, or if I don't set `UCX_TLS` at all. Here are results for `dc,sm,self`:

```
mpirun -x UCX_TLS=dc,sm,self -x UCX_PROTO_ENABLE=n -mca oob_tcp_if_include ib0 -mca coll_hcoll_enable 1 ./osu_alltoall -m 1:1024

# OSU MPI All-to-All Personalized Exchange Latency Test v7.4
# Datatype: MPI_CHAR.
# Size       Avg Latency(us)
1                      89.41
2                      65.75
4                      76.88
8                     106.66
16                    131.42
32                    225.34
64                    412.10
128                   957.36
256                  1704.20
512                  3377.45
1024                 8725.43
```
log file: 
[osu_alltoall_v1_b2236_112522.log.gz](https://github.com/user-attachments/files/15788833/osu_alltoall_v1_b2236_112522.log.gz)


```
mpirun -x UCX_TLS=dc,sm,self -x UCX_PROTO_ENABLE=y -mca oob_tcp_if_include ib0 -mca coll_hcoll_enable 1 ./osu_alltoall -m 1:1024

# OSU MPI All-to-All Personalized Exchange Latency Test v7.4
# Datatype: MPI_CHAR.
# Size       Avg Latency(us)
1                      88.21
2                     296.96
4                     296.48
8                     391.46
16                    508.68
32                    335.05
64                    611.42
128                  1195.06
256                  1766.87
512                  3566.42
1024                 5783.99
```
log file: 
[osu_alltoall_v1_b2236_111517.log.gz](https://github.com/user-attachments/files/15788814/osu_alltoall_v1_b2236_111517.log.gz)

Note that in the logged runs `osu_alltoall` is sending messages up to size 8 bytes (`-m 1:8`).

> > Note that this time I only ran the benchmark with message sizes up to 8 bytes due to the amount of logs.
> 
> Are you sure? I see messages up to 2048 bytes in that log.

At least this is what I asked OSU benchmark to test. But I guess it might send other messages during the run time, I don't know.

> Root cause isn't still defined since according to logs both protov1 and protov2 uses same protocols. Could you please also re-measure `UCX_PROTO_ENABLE=y` separately with:

These are for `UCX_TLS=ud,sm,self`:

>     1. UCX_BCOPY_THRESH=1
```
mpirun -x UCX_BCOPY_THRESH=1 -x UCX_TLS=ud,sm,self -x UCX_PROTO_ENABLE=Y -mca oob_tcp_if_include ib0 -mca coll_hcoll_enable 1 ./osu_alltoall -m 1:1024

# OSU MPI All-to-All Personalized Exchange Latency Test v7.4
# Datatype: MPI_CHAR.
# Size       Avg Latency(us)
1                     104.82
2                     339.35
4                     338.64
8                     386.39
16                    483.35
32                    438.18
64                    633.02
128                  1187.00
256                  1789.47
512                  3184.98
1024                 5770.11
```
>     2. UCX_ZCOPY_THRESH=1
```
time mpirun -x UCX_ZCOPY_THRESH=1 -x UCX_TLS=ud,sm,self -x UCX_PROTO_ENABLE=Y -mca oob_tcp_if_include ib0 -mca coll_hcoll_enable 1 ./osu_alltoall -m 1:1024

# OSU MPI All-to-All Personalized Exchange Latency Test v7.4
# Datatype: MPI_CHAR.
# Size       Avg Latency(us)
1                     428.77
2                     552.18
4                     388.84
8                     506.84
16                    754.83
32                    369.32
64                    589.83
128                   871.58
256                  1699.39
512                  3099.05
1024                 6047.78
```
>     3. UCX_RNDV_THRESH=1
```
mpirun -x UCX_RNDV_THRESH=1 -x UCX_TLS=ud,sm,self -x UCX_PROTO_ENABLE=Y -mca oob_tcp_if_include ib0 -mca coll_hcoll_enable 1 ./osu_alltoall -m 1:1024

# OSU MPI All-to-All Personalized Exchange Latency Test v7.4
# Datatype: MPI_CHAR.
# Size       Avg Latency(us)
1                     107.16
2                     397.32
4                     367.12
8                     513.64
16                    520.46
32                    439.59
64                    628.95
128                  1190.54
256                  1739.27
512                  4012.02
1024                 5776.53
```

For reference, here are results with `UCX_TLS=dc,sm,self`:
>     1. UCX_BCOPY_THRESH=1
```
mpirun -x UCX_BCOPY_THRESH=1 -x UCX_TLS=dc,sm,self -x UCX_PROTO_ENABLE=Y -mca oob_tcp_if_include ib0 -mca coll_hcoll_enable 1 ./osu_alltoall -m 1:1024

# OSU MPI All-to-All Personalized Exchange Latency Test v7.4
# Datatype: MPI_CHAR.
# Size       Avg Latency(us)
1                      63.07
2                      64.43
4                     231.03
8                     240.34
16                    275.29
32                    446.19
64                    849.55
128                  1092.76
256                  1847.63
512                  4922.05
1024                 5498.93
```

>     2. UCX_ZCOPY_THRESH=1
```
mpirun -x UCX_ZCOPY_THRESH=1 -x UCX_TLS=dc,sm,self -x UCX_PROTO_ENABLE=Y -mca oob_tcp_if_include ib0 -mca coll_hcoll_enable 1 ./osu_alltoall -m 1:1024

# OSU MPI All-to-All Personalized Exchange Latency Test v7.4
# Datatype: MPI_CHAR.
# Size       Avg Latency(us)
1                     245.10
2                     303.88
4                     389.24
8                     358.88
16                    473.86
32                    237.15
64                    694.15
128                  1303.12
256                  1837.86
512                  3494.33
1024                 5651.72
```

>     3. UCX_RNDV_THRESH=1
```
mpirun -x UCX_RNDV_THRESH=1 -x UCX_TLS=dc,sm,self -x UCX_PROTO_ENABLE=Y -mca oob_tcp_if_include ib0 -mca coll_hcoll_enable 1 ./osu_alltoall -m 1:1024

# OSU MPI All-to-All Personalized Exchange Latency Test v7.4
# Datatype: MPI_CHAR.
# Size       Avg Latency(us)
1                    4028.24
2                    3995.13
4                    4106.96
8                    4137.44
16                   3908.93
32                    369.96
64                    870.47
128                  1163.54
256                  1767.12
512                  3620.55
1024                 7069.85
```


### angainor · 2024-08-01

@ivankochin Is there any further info about this? 

### ivankochin · 2024-08-01

@angainor thanks for you patience!

I have successfully reproduced that problem on my setup and found a reason of degradation. But fixing of that requires changes HCOLL codebase (which is unlikely to happen), so workaround can be using UCC collectives instead of HCOLL which also need to be patched to fix that degradation.

The problem is that current solution shows degradation on bigger sizes which I am checking right now.

### angainor · 2024-08-01

UCC in their current form are much slower than HCOLL in many cases, so it is not an option. I guess I will force `UCX_PROTO_ENABLE=N` on newer UCX versions. Do you think this is a good idea? or will this impact performance in other scenarios?

### ivankochin · 2024-08-01

UCX_PROTO_ENABLE=n is not supported anymore, so it surely can impact performance in other scenarios (we don't have data whether it will or won't in your case).

### angainor · 2024-08-01

This looks like an important performance issue. If a fix is unlikely anytime soon, and I should not use `UCX_PROTO_ENABLE=n` with new UCX versions, then maybe we should consider staying on HPCX 2.14 instead?

In either case, please let me know when you have any solution / update for this.

### ivankochin · 2024-08-05

@angainor I think setting `UCX_PROTO_ENABLE=n` seems better than staying on HPCX 2.14. 

Regarding the update, as I said previously it is not possible to patch HCOLL, and we are considering patching UCC right now, but it likely will take some time.

### TheWitness · 2026-03-25

Any updates on this guys.  1.5 years without an update.  Thanks!
