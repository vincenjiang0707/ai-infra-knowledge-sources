# [Issue #1026] RCCL and MI250X P2P

source: https://github.com/ROCm/rccl/issues/1026
state: closed | updated: 2024-01-05T15:25:10Z
labels: 

## 正文

On bardpeak (trento+4MI250x) node I have the following issue:
a case where when running on 1 node with all the 8 GCDs (4 MI250X) with NCCL_P2P_LEVEL=XGMI everything works fine but when I scale the same case to 2 nodes, I get some connection error at startup.

I have reduced the issue to when I use more than 1 node and more than 1 MI250X per node (3>= GCDs). Then the only way to pass the case is to use P2P_LEVEL=LOC.

Below are the NCCL logs for a case with 2 nodes and 4 GCD (2 MI250X) per node.
```
g1064:11143:11143 [0] NCCL INFO Bootstrap : Using bond0:10.64.4.21<0>
g1064:11143:11143 [0] NCCL INFO NET/Plugin : No plugin found (librccl-net.so), using internal implementation

g1064:11143:11143 [0] /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/src/init.cpp:120 NCCL WARN Missing "amd_iommu=on" from kernel command line which can lead to system instablity or hang!

g1064:11143:11143 [0] /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/src/init.cpp:122 NCCL WARN Missing "iommu=pt" from kernel command line which can lead to system instablity or hang!

g1064:11143:11143 [0] /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/src/init.cpp:126 NCCL WARN Missing "HSA_FORCE_FINE_GRAIN_PCIE=1" from environment which can lead to low RCCL performance, system instablity or hang!
RCCL version 2.16.5+hip5.6 HEAD:3dcebc7+
g1064:11143:11194 [0] NCCL INFO Setting hipLimitStackSize to 512 maxLocalSizeBytes 0
g1064:11143:11194 [0] NCCL INFO NET/IB : No device found.
g1064:11143:11194 [0] NCCL INFO NET/Socket : Using [0]bond0:10.64.4.21<0> [1]hsn0:10.80.0.205<0> [2]hsn1:10.80.0.154<0> [3]hsn2:10.80.0.148<0> [4]hsn3:10.80.1.80<0>
g1064:11143:11194 [0] NCCL INFO Using network Socket
g1064:11145:11145 [2] NCCL INFO Bootstrap : Using bond0:10.64.4.21<0>
g1064:11145:11145 [2] NCCL INFO NET/Plugin : No plugin found (librccl-net.so), using internal implementation

g1064:11145:11145 [2] /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/src/init.cpp:120 NCCL WARN Missing "amd_iommu=on" from kernel command line which can lead to system instablity or hang!

g1064:11145:11145 [2] /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/src/init.cpp:122 NCCL WARN Missing "iommu=pt" from kernel command line which can lead to system instablity or hang!

g1064:11145:11145 [2] /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/src/init.cpp:126 NCCL WARN Missing "HSA_FORCE_FINE_GRAIN_PCIE=1" from environment which can lead to low RCCL performance, system instablity or hang!
g1072:1263987:1263987 [2] NCCL INFO Bootstrap : Using bond0:10.64.4.23<0>
g1072:1263987:1263987 [2] NCCL INFO NET/Plugin : No plugin found (librccl-net.so), using internal implementation

g1072:1263987:1263987 [2] /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/src/init.cpp:120 NCCL WARN Missing "amd_iommu=on" from kernel command line which can lead to system instablity or hang!

g1072:1263987:1263987 [2] /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/src/init.cpp:122 NCCL WARN Missing "iommu=pt" from kernel command line which can lead to system instablity or hang!

g1072:1263987:1263987 [2] /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/src/init.cpp:126 NCCL WARN Missing "HSA_FORCE_FINE_GRAIN_PCIE=1" from environment which can lead to low RCCL performance, system instablity or hang!
g1064:11144:11144 [1] NCCL INFO Bootstrap : Using bond0:10.64.4.21<0>
g1064:11146:11146 [3] NCCL INFO Bootstrap : Using bond0:10.64.4.21<0>
g1064:11144:11144 [1] NCCL INFO NET/Plugin : No plugin found (librccl-net.so), using internal implementation
g1064:11146:11146 [3] NCCL INFO NET/Plugin : No plugin found (librccl-net.so), using internal implementation

g1064:11144:11144 [1] /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/src/init.cpp:120 NCCL WARN Missing "amd_iommu=on" from kernel command line which can lead to system instablity or hang!

g1064:11146:11146 [3] /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/src/init.cpp:120 NCCL WARN Missing "amd_iommu=on" from kernel command line which can lead to system instablity or hang!

g1064:11144:11144 [1] /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/src/init.cpp:122 NCCL WARN Missing "iommu=pt" from kernel command line which can lead to system instablity or hang!

g1064:11146:11146 [3] /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/src/init.cpp:122 NCCL WARN Missing "iommu=pt" from kernel command line which can lead to system instablity or hang!

g1064:11144:11144 [1] /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/src/init.cpp:126 NCCL WARN Missing "HSA_FORCE_FINE_GRAIN_PCIE=1" from environment which can lead to low RCCL performance, system instablity or hang!

g1064:11146:11146 [3] /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/src/init.cpp:126 NCCL WARN Missing "HSA_FORCE_FINE_GRAIN_PCIE=1" from environment which can lead to low RCCL performance, system instablity or hang!
g1072:1263988:1263988 [3] NCCL INFO Bootstrap : Using bond0:10.64.4.23<0>
g1072:1263988:1263988 [3] NCCL INFO NET/Plugin : No plugin found (librccl-net.so), using internal implementation

g1072:1263988:1263988 [3] /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/src/init.cpp:120 NCCL WARN Missing "amd_iommu=on" from kernel command line which can lead to system instablity or hang!

g1072:1263988:1263988 [3] /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/src/init.cpp:122 NCCL WARN Missing "iommu=pt" from kernel command line which can lead to system instablity or hang!

g1072:1263988:1263988 [3] /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/src/init.cpp:126 NCCL WARN Missing "HSA_FORCE_FINE_GRAIN_PCIE=1" from environment which can lead to low RCCL performance, system instablity or hang!
g1072:1263985:1263985 [0] NCCL INFO Bootstrap : Using bond0:10.64.4.23<0>
g1072:1263985:1263985 [0] NCCL INFO NET/Plugin : No plugin found (librccl-net.so), using internal implementation

g1072:1263985:1263985 [0] /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/src/init.cpp:120 NCCL WARN Missing "amd_iommu=on" from kernel command line which can lead to system instablity or hang!

g1072:1263985:1263985 [0] /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/src/init.cpp:122 NCCL WARN Missing "iommu=pt" from kernel command line which can lead to system instablity or hang!

g1072:1263985:1263985 [0] /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/src/init.cpp:126 NCCL WARN Missing "HSA_FORCE_FINE_GRAIN_PCIE=1" from environment which can lead to low RCCL performance, system instablity or hang!
g1072:1263986:1263986 [1] NCCL INFO Bootstrap : Using bond0:10.64.4.23<0>
g1072:1263986:1263986 [1] NCCL INFO NET/Plugin : No plugin found (librccl-net.so), using internal implementation

g1072:1263986:1263986 [1] /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/src/init.cpp:120 NCCL WARN Missing "amd_iommu=on" from kernel command line which can lead to system instablity or hang!

g1072:1263986:1263986 [1] /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/src/init.cpp:122 NCCL WARN Missing "iommu=pt" from kernel command line which can lead to system instablity or hang!

g1072:1263986:1263986 [1] /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/src/init.cpp:126 NCCL WARN Missing "HSA_FORCE_FINE_GRAIN_PCIE=1" from environment which can lead to low RCCL performance, system instablity or hang!
g1064:11145:11195 [2] NCCL INFO Setting hipLimitStackSize to 512 maxLocalSizeBytes 0
g1064:11145:11195 [2] NCCL INFO NET/IB : No device found.
g1064:11145:11195 [2] NCCL INFO NET/Socket : Using [0]bond0:10.64.4.21<0> [1]hsn0:10.80.0.205<0> [2]hsn1:10.80.0.154<0> [3]hsn2:10.80.0.148<0> [4]hsn3:10.80.1.80<0>
g1064:11145:11195 [2] NCCL INFO Using network Socket
g1072:1263987:1264005 [2] NCCL INFO Setting hipLimitStackSize to 512 maxLocalSizeBytes 0
g1064:11144:11196 [1] NCCL INFO Setting hipLimitStackSize to 512 maxLocalSizeBytes 0
g1072:1263987:1264005 [2] NCCL INFO NET/IB : No device found.
g1064:11144:11196 [1] NCCL INFO NET/IB : No device found.
g1072:1263987:1264005 [2] NCCL INFO NET/Socket : Using [0]bond0:10.64.4.23<0> [1]hsn0:10.80.0.118<0> [2]hsn1:10.80.0.103<0> [3]hsn2:10.80.0.101<0> [4]hsn3:10.80.0.117<0>
g1072:1263987:1264005 [2] NCCL INFO Using network Socket
g1064:11144:11196 [1] NCCL INFO NET/Socket : Using [0]bond0:10.64.4.21<0> [1]hsn0:10.80.0.205<0> [2]hsn1:10.80.0.154<0> [3]hsn2:10.80.0.148<0> [4]hsn3:10.80.1.80<0>
g1064:11144:11196 [1] NCCL INFO Using network Socket
g1064:11146:11197 [3] NCCL INFO Setting hipLimitStackSize to 512 maxLocalSizeBytes 0
g1064:11146:11197 [3] NCCL INFO NET/IB : No device found.
g1064:11146:11197 [3] NCCL INFO NET/Socket : Using [0]bond0:10.64.4.21<0> [1]hsn0:10.80.0.205<0> [2]hsn1:10.80.0.154<0> [3]hsn2:10.80.0.148<0> [4]hsn3:10.80.1.80<0>
g1064:11146:11197 [3] NCCL INFO Using network Socket
g1072:1263988:1264006 [3] NCCL INFO Setting hipLimitStackSize to 512 maxLocalSizeBytes 0
g1072:1263985:1264007 [0] NCCL INFO Setting hipLimitStackSize to 512 maxLocalSizeBytes 0
g1072:1263988:1264006 [3] NCCL INFO NET/IB : No device found.
g1072:1263988:1264006 [3] NCCL INFO NET/Socket : Using [0]bond0:10.64.4.23<0> [1]hsn0:10.80.0.118<0> [2]hsn1:10.80.0.103<0> [3]hsn2:10.80.0.101<0> [4]hsn3:10.80.0.117<0>
g1072:1263988:1264006 [3] NCCL INFO Using network Socket
g1072:1263985:1264007 [0] NCCL INFO NET/IB : No device found.
g1072:1263985:1264007 [0] NCCL INFO NET/Socket : Using [0]bond0:10.64.4.23<0> [1]hsn0:10.80.0.118<0> [2]hsn1:10.80.0.103<0> [3]hsn2:10.80.0.101<0> [4]hsn3:10.80.0.117<0>
g1072:1263985:1264007 [0] NCCL INFO Using network Socket
g1072:1263986:1264008 [1] NCCL INFO Setting hipLimitStackSize to 512 maxLocalSizeBytes 0
g1072:1263986:1264008 [1] NCCL INFO NET/IB : No device found.
g1072:1263986:1264008 [1] NCCL INFO NET/Socket : Using [0]bond0:10.64.4.23<0> [1]hsn0:10.80.0.118<0> [2]hsn1:10.80.0.103<0> [3]hsn2:10.80.0.101<0> [4]hsn3:10.80.0.117<0>
g1072:1263986:1264008 [1] NCCL INFO Using network Socket
g1072:1263986:1264008 [1] NCCL INFO rocm_smi_lib: version 5.0.0.0
g1072:1263985:1264007 [0] NCCL INFO rocm_smi_lib: version 5.0.0.0
g1072:1263988:1264006 [3] NCCL INFO rocm_smi_lib: version 5.0.0.0
g1072:1263987:1264005 [2] NCCL INFO rocm_smi_lib: version 5.0.0.0
g1072:1263986:1264008 [1] NCCL INFO NCCL_P2P_LEVEL set by environment to XGMI
g1072:1263985:1264007 [0] NCCL INFO NCCL_P2P_LEVEL set by environment to XGMI
g1072:1263986:1264008 [1] NCCL INFO Setting affinity for GPU 1 to ffff0000,00000000,ffff0000,00000000
g1072:1263988:1264006 [3] NCCL INFO NCCL_P2P_LEVEL set by environment to XGMI
g1072:1263985:1264007 [0] NCCL INFO Setting affinity for GPU 0 to ffff0000,00000000,ffff0000,00000000
g1064:11144:11196 [1] NCCL INFO rocm_smi_lib: version 5.0.0.0
g1072:1263987:1264005 [2] NCCL INFO NCCL_P2P_LEVEL set by environment to XGMI
g1072:1263988:1264006 [3] NCCL INFO Setting affinity for GPU 3 to ffff0000,00000000,ffff0000
g1064:11146:11197 [3] NCCL INFO rocm_smi_lib: version 5.0.0.0
g1072:1263987:1264005 [2] NCCL INFO Setting affinity for GPU 2 to ffff0000,00000000,ffff0000
g1064:11143:11194 [0] NCCL INFO rocm_smi_lib: version 5.0.0.0
g1064:11145:11195 [2] NCCL INFO rocm_smi_lib: version 5.0.0.0
g1064:11144:11196 [1] NCCL INFO NCCL_P2P_LEVEL set by environment to XGMI
g1064:11144:11196 [1] NCCL INFO Setting affinity for GPU 1 to ffff0000,00000000,ffff0000,00000000
g1064:11146:11197 [3] NCCL INFO NCCL_P2P_LEVEL set by environment to XGMI
g1064:11143:11194 [0] NCCL INFO NCCL_P2P_LEVEL set by environment to XGMI
g1064:11145:11195 [2] NCCL INFO NCCL_P2P_LEVEL set by environment to XGMI
g1064:11143:11194 [0] NCCL INFO Setting affinity for GPU 0 to ffff0000,00000000,ffff0000,00000000
g1064:11146:11197 [3] NCCL INFO Setting affinity for GPU 3 to ffff0000,00000000,ffff0000
g1064:11145:11195 [2] NCCL INFO Setting affinity for GPU 2 to ffff0000,00000000,ffff0000
g1064:11146:11197 [3] NCCL INFO Trees [0] 2/-1/-1->3->1 [1] 1/-1/-1->3->2 [2] 2/-1/-1->3->1 [3] 1/-1/-1->3->2 comm 0xaa09f20 nRanks 08 busId ce000
g1064:11146:11197 [3] NCCL INFO P2P Chunksize set to 131072
g1064:11145:11195 [2] NCCL INFO Trees [0] -1/-1/-1->2->3 [1] 3/6/-1->2->-1 [2] -1/-1/-1->2->3 [3] 3/-1/-1->2->6 comm 0x10a5a9f0 nRanks 08 busId c9000
g1064:11145:11195 [2] NCCL INFO P2P Chunksize set to 131072
g1072:1263988:1264006 [3] NCCL INFO Trees [0] 6/-1/-1->7->5 [1] 5/-1/-1->7->6 [2] 6/-1/-1->7->5 [3] 5/-1/-1->7->6 comm 0xfb16e30 nRanks 08 busId ce000
g1072:1263986:1264008 [1] NCCL INFO Trees [0] 7/-1/-1->5->4 [1] 4/-1/-1->5->7 [2] 7/-1/-1->5->4 [3] 4/-1/-1->5->7 comm 0xa5bff40 nRanks 08 busId c6000
g1072:1263986:1264008 [1] NCCL INFO P2P Chunksize set to 131072
g1072:1263988:1264006 [3] NCCL INFO P2P Chunksize set to 131072
g1072:1263987:1264005 [2] NCCL INFO Trees [0] -1/-1/-1->6->7 [1] 7/-1/-1->6->2 [2] -1/-1/-1->6->7 [3] 7/2/-1->6->-1 comm 0x9b02320 nRanks 08 busId c9000
g1072:1263987:1264005 [2] NCCL INFO P2P Chunksize set to 131072
g1072:1263985:1264007 [0] NCCL INFO Trees [0] 5/-1/-1->4->0 [1] -1/-1/-1->4->5 [2] 5/0/-1->4->-1 [3] -1/-1/-1->4->5 comm 0x95cdeb0 nRanks 08 busId c1000
g1072:1263985:1264007 [0] NCCL INFO P2P Chunksize set to 131072
g1064:11145:11195 [2] NCCL INFO Channel 00/0 : 2[c9000] -> 3[ce000] via P2P/IPC comm 0x10a5a9f0 nRanks 08
g1072:1263987:1264005 [2] NCCL INFO Channel 00/0 : 6[c9000] -> 7[ce000] via P2P/IPC comm 0x9b02320 nRanks 08
g1072:1263985:1264007 [0] NCCL INFO Channel 01/0 : 4[c1000] -> 5[c6000] via P2P/IPC comm 0x95cdeb0 nRanks 08
g1064:11143:11194 [0] NCCL INFO Channel 00/04 :    0   2   3   1   4   6   7   5
g1064:11143:11194 [0] NCCL INFO Channel 01/04 :    0   1   3   6   4   5   7   2
g1064:11143:11194 [0] NCCL INFO Channel 02/04 :    0   2   3   1   4   6   7   5
g1064:11143:11194 [0] NCCL INFO Channel 03/04 :    0   1   3   6   4   5   7   2
g1064:11143:11194 [0] NCCL INFO Trees [0] 1/4/-1->0->-1 [1] -1/-1/-1->0->1 [2] 1/-1/-1->0->4 [3] -1/-1/-1->0->1 comm 0xf37f2e0 nRanks 08 busId c1000
g1064:11143:11194 [0] NCCL INFO P2P Chunksize set to 131072
g1064:11144:11196 [1] NCCL INFO Trees [0] 3/-1/-1->1->0 [1] 0/-1/-1->1->3 [2] 3/-1/-1->1->0 [3] 0/-1/-1->1->3 comm 0x9e4d8d0 nRanks 08 busId c6000
g1064:11144:11196 [1] NCCL INFO P2P Chunksize set to 131072
g1064:11143:11194 [0] NCCL INFO Channel 01/0 : 0[c1000] -> 1[c6000] via P2P/IPC comm 0xf37f2e0 nRanks 08
g1072:1263987:1264005 [2] NCCL INFO Channel 02/0 : 6[c9000] -> 7[ce000] via P2P/IPC comm 0x9b02320 nRanks 08
g1064:11145:11195 [2] NCCL INFO Channel 02/0 : 2[c9000] -> 3[ce000] via P2P/IPC comm 0x10a5a9f0 nRanks 08
g1072:1263985:1264007 [0] NCCL INFO Channel 03/0 : 4[c1000] -> 5[c6000] via P2P/IPC comm 0x95cdeb0 nRanks 08
g1064:11143:11194 [0] NCCL INFO Channel 03/0 : 0[c1000] -> 1[c6000] via P2P/IPC comm 0xf37f2e0 nRanks 08
g1072:1263985:1264007 [0] NCCL INFO Channel 00/0 : 4[c1000] -> 6[c9000] via P2P/IPC comm 0x95cdeb0 nRanks 08
g1072:1263986:1264008 [1] NCCL INFO Channel 01/0 : 5[c6000] -> 7[ce000] via P2P/IPC comm 0xa5bff40 nRanks 08
g1064:11143:11194 [0] NCCL INFO Channel 00/0 : 0[c1000] -> 2[c9000] via P2P/IPC comm 0xf37f2e0 nRanks 08
g1064:11144:11196 [1] NCCL INFO Channel 01/0 : 1[c6000] -> 3[ce000] via P2P/IPC comm 0x9e4d8d0 nRanks 08
g1072:1263985:1264007 [0] NCCL INFO Channel 02/0 : 4[c1000] -> 6[c9000] via P2P/IPC comm 0x95cdeb0 nRanks 08
g1072:1263986:1264008 [1] NCCL INFO Channel 03/0 : 5[c6000] -> 7[ce000] via P2P/IPC comm 0xa5bff40 nRanks 08
g1064:11143:11194 [0] NCCL INFO Channel 02/0 : 0[c1000] -> 2[c9000] via P2P/IPC comm 0xf37f2e0 nRanks 08
g1064:11144:11196 [1] NCCL INFO Channel 03/0 : 1[c6000] -> 3[ce000] via P2P/IPC comm 0x9e4d8d0 nRanks 08
g1072:1263986:1264008 [1] NCCL INFO Channel 00/0 : 5[c6000] -> 0[c1000] [send] via NET/Socket/1 comm 0xa5bff40 nRanks 08
g1072:1263988:1264006 [3] NCCL INFO Channel 01/0 : 7[ce000] -> 2[c9000] [send] via NET/Socket/2 comm 0xfb16e30 nRanks 08
g1072:1263987:1264005 [2] NCCL INFO Channel 01/0 : 3[ce000] -> 6[c9000] [receive] via NET/Socket/2 comm 0x9b02320 nRanks 08
g1072:1263985:1264007 [0] NCCL INFO Channel 00/0 : 1[c6000] -> 4[c1000] [receive] via NET/Socket/1 comm 0x95cdeb0 nRanks 08
g1064:11144:11196 [1] NCCL INFO Channel 00/0 : 1[c6000] -> 4[c1000] [send] via NET/Socket/1 comm 0x9e4d8d0 nRanks 08
g1064:11146:11197 [3] NCCL INFO Channel 01/0 : 3[ce000] -> 6[c9000] [send] via NET/Socket/2 comm 0xaa09f20 nRanks 08
g1064:11143:11194 [0] NCCL INFO Channel 00/0 : 5[c6000] -> 0[c1000] [receive] via NET/Socket/1 comm 0xf37f2e0 nRanks 08
g1064:11145:11195 [2] NCCL INFO Channel 01/0 : 7[ce000] -> 2[c9000] [receive] via NET/Socket/2 comm 0x10a5a9f0 nRanks 08
g1064:11143:11194 [0] NCCL INFO Channel 02/0 : 5[c6000] -> 0[c1000] [receive] via NET/Socket/1 comm 0xf37f2e0 nRanks 08
g1064:11145:11195 [2] NCCL INFO Channel 03/0 : 7[ce000] -> 2[c9000] [receive] via NET/Socket/2 comm 0x10a5a9f0 nRanks 08
g1072:1263988:1264006 [3] NCCL INFO Channel 03/0 : 7[ce000] -> 2[c9000] [send] via NET/Socket/2 comm 0xfb16e30 nRanks 08
g1072:1263986:1264008 [1] NCCL INFO Channel 02/0 : 5[c6000] -> 0[c1000] [send] via NET/Socket/1 comm 0xa5bff40 nRanks 08
g1072:1263985:1264007 [0] NCCL INFO Channel 02/0 : 1[c6000] -> 4[c1000] [receive] via NET/Socket/1 comm 0x95cdeb0 nRanks 08
g1072:1263987:1264005 [2] NCCL INFO Channel 03/0 : 3[ce000] -> 6[c9000] [receive] via NET/Socket/2 comm 0x9b02320 nRanks 08
g1064:11144:11196 [1] NCCL INFO Channel 02/0 : 1[c6000] -> 4[c1000] [send] via NET/Socket/1 comm 0x9e4d8d0 nRanks 08
g1064:11146:11197 [3] NCCL INFO Channel 03/0 : 3[ce000] -> 6[c9000] [send] via NET/Socket/2 comm 0xaa09f20 nRanks 08
g1072:1263988:1264006 [3] NCCL INFO Channel 00/0 : 7[ce000] -> 5[c6000] via P2P/IPC comm 0xfb16e30 nRanks 08
g1072:1263988:1264006 [3] NCCL INFO Channel 02/0 : 7[ce000] -> 5[c6000] via P2P/IPC comm 0xfb16e30 nRanks 08
g1064:11145:11195 [2] NCCL INFO Channel 01/0 : 2[c9000] -> 0[c1000] via P2P/IPC comm 0x10a5a9f0 nRanks 08
g1064:11145:11195 [2] NCCL INFO Channel 03/0 : 2[c9000] -> 0[c1000] via P2P/IPC comm 0x10a5a9f0 nRanks 08
g1072:1263986:1264008 [1] NCCL INFO Connected all rings comm 0xa5bff40 nRanks 08 busId c6000
g1064:11145:11195 [2] NCCL INFO Connected all rings comm 0x10a5a9f0 nRanks 08 busId c9000
g1064:11145:11195 [2] NCCL INFO Channel 01/0 : 2[c9000] -> 3[ce000] via P2P/IPC comm 0x10a5a9f0 nRanks 08
g1072:1263988:1264006 [3] NCCL INFO Connected all rings comm 0xfb16e30 nRanks 08 busId ce000
g1064:11143:11194 [0] NCCL INFO Connected all rings comm 0xf37f2e0 nRanks 08 busId c1000
g1064:11143:11194 [0] NCCL INFO Channel 00/0 : 0[c1000] -> 1[c6000] via P2P/IPC comm 0xf37f2e0 nRanks 08
g1064:11145:11195 [2] NCCL INFO Channel 03/0 : 2[c9000] -> 3[ce000] via P2P/IPC comm 0x10a5a9f0 nRanks 08
g1064:11143:11194 [0] NCCL INFO Channel 02/0 : 0[c1000] -> 1[c6000] via P2P/IPC comm 0xf37f2e0 nRanks 08
g1064:11146:11200 [3] NCCL INFO /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/src/misc/socket.cpp:572 -> 2
g1064:11146:11200 [3] NCCL INFO /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/src/misc/socket.cpp:591 -> 2
g1064:11146:11200 [3] NCCL INFO /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/src/transport/net_socket.cpp:336 -> 2
g1064:11146:11200 [3] NCCL INFO /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/src/include/net.h:26 -> 2
g1064:11146:11200 [3] NCCL INFO /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/src/transport/net.cpp:550 -> 2
g1064:11146:11200 [3] NCCL INFO /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/src/proxy.cpp:1016 -> 2
g1064:11146:11200 [3] /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/src/proxy.cpp:1177 NCCL WARN [Proxy Service 3] Failed to execute operation Connect from rank 3, retcode 2
g1064:11146:11197 [3] /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/src/misc/socket.cpp:57 NCCL WARN socketProgress: Connection closed by remote peer g1064.hostmgmt2001.xxxxx.xxxxx.fr<57521>
g1064:11146:11197 [3] NCCL INFO /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/src/misc/socket.cpp:65 -> 6
g1064:11146:11197 [3] NCCL INFO /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/src/misc/socket.cpp:825 -> 6
g1064:11146:11197 [3] NCCL INFO /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/src/proxy.cpp:909 -> 6
g1064:11146:11197 [3] /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/src/proxy.cpp:912 NCCL WARN Proxy Call to rank 3 failed (Connect)
g1064:11146:11197 [3] NCCL INFO /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/src/transport/net.cpp:294 -> 6
g1064:11146:11197 [3] NCCL INFO /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/src/transport.cpp:136 -> 6
g1064:11146:11197 [3] NCCL INFO /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/src/init.cpp:1264 -> 6
g1064:11146:11197 [3] NCCL INFO /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/src/init.cpp:1481 -> 6
g1064:11146:11197 [3] NCCL INFO /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/src/group.cpp:68 -> 6 [Async thread]
g1064:11146:11146 [3] NCCL INFO /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/src/group.cpp:440 -> 3
g1064:11146:11146 [3] NCCL INFO /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/src/group.cpp:118 -> 3
g1064:11146:11146 [3] NCCL INFO comm 0xaa09f20 rank 3 nranks 8 cudaDev 3 busId ce000 - Abort COMPLETE
```

## 评论 (2)

### etiennemlb · 2023-12-20

Additionally, as the machine I'm targeting is equipped with the HPE Slingshot interconnect, how can I make sure I'm using it ?

### etiennemlb · 2024-01-05

Using https://github.com/ROCmSoftwarePlatform/aws-ofi-rccl solved the issue.
