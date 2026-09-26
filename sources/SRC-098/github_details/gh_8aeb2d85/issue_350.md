# [Issue #350] Unexpected performance drop-off for large workload sizes

source: https://github.com/NVIDIA/nccl-tests/issues/350
state: closed | updated: 2025-10-20T21:14:20Z
labels: 

## 正文

I am seeing consistent, unexpected performance drop-offs for large workload sizes with NCCL tests.

My topology is a 4-node setup with a single A100 40 GB in each, with Mellanox ConnectX-5 200 Gbps and doing nccl-tests between 2 of them.

We see expected bandwidth at around 22 GB/s for workload sizes up to around 6 GB, however after it drops significantly. 

The machines have 2 sockets, but relevant GPUs and NICs are on the same socket (socket 1). I have set `NCCL_NET_GDR_LEVEL=SYS` to force P2P and GDR, because without it, bandwidth peaks at around 13 GB/s. 

PFA a bunch of relevant info. There is nothing that stands out to me there. Please let me know if you need more. 

- Nvidia driver version: 570.172.08
- CUDA toolkit version: 12.8
- NCCL version: 2.16.5

```
NCCL_NET_GDR_LEVEL=SYS NCCL_DEBUG=TRACE NCCL_DEBUG_SUBSYS=INIT,GRAPH,NET mpirun -np 2 -N 1 --host n013,n014 -x CUDA_HOME -x LD_LIBRARY_PATH ~/nccl-tests/build/gather_perf                  --minbytes 128M         --maxbytes 12G         --stepbytes 128M         --ngpus 1         --warmup_iters 5
``` 

```
# Collective test starting: gather_perf
# nThread 1 nGpus 1 minBytes 134217728 maxBytes 12884901888 step: 134217728(bytes) warmup iters: 5 iters: 20 agg iters: 1 validation: 1 graph: 0
#
# Using devices
#  Rank  0 Group  0 Pid 101855 on       n013 device  0 [0000:81:00] NVIDIA A100-PCIE-40GB
#  Rank  1 Group  0 Pid  34424 on       n014 device  0 [0000:81:00] NVIDIA A100-PCIE-40GB
#
# Reducing maxBytes to 12703978837 due to memory limitation
n013:101855:101855 [0] NCCL INFO Bootstrap : Using ibp209s0f0:10.128.3.13<0>
n013:101855:101855 [0] NCCL INFO NET/Plugin : No plugin found (libnccl-net.so), using internal implementation
n013:101855:101855 [0] NCCL INFO cudaDriverVersion 12080
NCCL version 2.16.5+cuda11.8
n013:101855:101885 [0] NCCL INFO NET/IB : Using [0]mlx5_0:1/RoCE [1]mlx5_2:1/IB [RO]; OOB ibp209s0f0:10.128.3.13<0>
n013:101855:101885 [0] NCCL INFO Using network IB
n013:101855:101885 [0] NCCL INFO DMA-BUF is available on GPU device 0
n013:101855:101885 [0] NCCL INFO NET/IB : GPU Direct RDMA Enabled for HCA 0 'mlx5_0'
n013:101855:101885 [0] NCCL INFO NET/IB : GPU Direct RDMA Enabled for HCA 1 'mlx5_2'
n013:101855:101885 [0] NCCL INFO NCCL_NET_GDR_LEVEL set by environment to SYS
n013:101855:101885 [0] NCCL INFO GPU Direct RDMA Enabled for GPU 81000 / HCA 1 (distance 6 <= 7), read 0
n013:101855:101885 [0] NCCL INFO GPU Direct RDMA Enabled for GPU 81000 / HCA 0 (distance 7 <= 7), read 0
n013:101855:101885 [0] NCCL INFO GPU Direct RDMA Enabled for GPU 81000 / HCA 1 (distance 6 <= 7), read 0
n013:101855:101885 [0] NCCL INFO GPU Direct RDMA Enabled for GPU 81000 / HCA 0 (distance 7 <= 7), read 0
n013:101855:101885 [0] NCCL INFO === System : maxBw 24.0 totalBw 24.0 ===
n013:101855:101885 [0] NCCL INFO CPU/1 (1/2/-1)
n013:101855:101885 [0] NCCL INFO + SYS[5000.0] - CPU/0
n013:101855:101885 [0] NCCL INFO + PCI[24.0] - GPU/81000 (0)
n013:101855:101885 [0] NCCL INFO + PCI[24.0] - NIC/D1000
n013:101855:101885 [0] NCCL INFO               + NET[25.0] - NET/1 (7a852d0003f6ceb8/1/25.000000)
n013:101855:101885 [0] NCCL INFO CPU/0 (1/2/-1)
n013:101855:101885 [0] NCCL INFO + SYS[5000.0] - CPU/1
n013:101855:101885 [0] NCCL INFO + PCI[6.0] - NIC/21000
n013:101855:101885 [0] NCCL INFO              + NET[3.1] - NET/0 (b8e2ce0003f6ceb8/1/3.125000)
n013:101855:101885 [0] NCCL INFO ==========================================
n013:101855:101885 [0] NCCL INFO GPU/81000 :GPU/81000 (0/5000.000000/LOC) CPU/1 (1/24.000000/PHB) CPU/0 (2/24.000000/SYS) NET/1 (3/24.000000/PHB) NET/0 (4/3.125000/SYS) 
n013:101855:101885 [0] NCCL INFO NET/1 :GPU/81000 (3/24.000000/PHB) CPU/1 (2/24.000000/PHB) CPU/0 (3/24.000000/SYS) NET/1 (0/5000.000000/LOC) NET/0 (5/3.125000/SYS) 
n013:101855:101885 [0] NCCL INFO NET/0 :GPU/81000 (4/3.125000/SYS) CPU/1 (3/3.125000/SYS) CPU/0 (2/3.125000/PHB) NET/1 (5/3.125000/SYS) NET/0 (0/5000.000000/LOC) 
n013:101855:101885 [0] NCCL INFO Pattern 4, crossNic 0, nChannels 1, bw 24.000000/24.000000, type LOC/PHB, sameChannels 1
n013:101855:101885 [0] NCCL INFO  0 : NET/1 GPU/0 NET/1
n013:101855:101885 [0] NCCL INFO Pattern 3, crossNic 0, nChannels 1, bw 48.000000/24.000000, type LOC/PHB, sameChannels 1
n013:101855:101885 [0] NCCL INFO  0 : NET/1 GPU/0 NET/1
n013:101855:101885 [0] NCCL INFO Pattern 3, crossNic 0, nChannels 0, bw 0.000000/0.000000, type LOC/PIX, sameChannels 1
n013:101855:101885 [0] NCCL INFO Tree 0 : -1 -> 0 -> 1/-1/-1
n013:101855:101885 [0] NCCL INFO Tree 1 : 1 -> 0 -> -1/-1/-1
n013:101855:101885 [0] NCCL INFO Channel 00/02 :    0   1
n013:101855:101885 [0] NCCL INFO Channel 01/02 :    0   1
n013:101855:101885 [0] NCCL INFO Ring 00 : 1 -> 0 -> 1
n013:101855:101885 [0] NCCL INFO Ring 01 : 1 -> 0 -> 1
n013:101855:101885 [0] NCCL INFO Trees [0] 1/-1/-1->0->-1 [1] -1/-1/-1->0->1
n013:101855:101885 [0] NCCL INFO P2P Chunksize set to 131072
n013:101855:101885 [0] NCCL INFO GPU Direct RDMA Enabled for GPU 81000 / HCA 1 (distance 6 <= 7), read 0
n013:101855:101888 [0] NCCL INFO New proxy recv connection 0 from local rank 0, transport 2
n013:101855:101885 [0] NCCL INFO Connection to proxy localRank 0 -> connection 0x1554e8000d50
n013:101855:101885 [0] NCCL INFO Channel 00/0 : 1[81000] -> 0[81000] [receive] via NET/IB/1/GDRDMA
n013:101855:101885 [0] NCCL INFO GPU Direct RDMA Enabled for GPU 81000 / HCA 1 (distance 6 <= 7), read 0
n013:101855:101888 [0] NCCL INFO New proxy recv connection 1 from local rank 0, transport 2
n013:101855:101885 [0] NCCL INFO Connection to proxy localRank 0 -> connection 0x1554e8000d90
n013:101855:101885 [0] NCCL INFO Channel 01/0 : 1[81000] -> 0[81000] [receive] via NET/IB/1/GDRDMA
n013:101855:101885 [0] NCCL INFO GPU Direct RDMA Enabled for GPU 81000 / HCA 1 (distance 6 <= 7), read 1
n013:101855:101888 [0] NCCL INFO New proxy send connection 2 from local rank 0, transport 2
n013:101855:101885 [0] NCCL INFO Connection to proxy localRank 0 -> connection 0x1554e8000dd0
n013:101855:101885 [0] NCCL INFO Channel 00/0 : 0[81000] -> 1[81000] [send] via NET/IB/1/GDRDMA
n013:101855:101885 [0] NCCL INFO GPU Direct RDMA Enabled for GPU 81000 / HCA 1 (distance 6 <= 7), read 1
n013:101855:101888 [0] NCCL INFO New proxy send connection 3 from local rank 0, transport 2
n013:101855:101885 [0] NCCL INFO Connection to proxy localRank 0 -> connection 0x1554e8000e10
n013:101855:101885 [0] NCCL INFO Channel 01/0 : 0[81000] -> 1[81000] [send] via NET/IB/1/GDRDMA
n013:101855:101888 [0] NCCL INFO NET/IB: Dev 1 Port 1 qpn 3038 mtu 5 LID 37
n013:101855:101888 [0] NCCL INFO NET/IB: Dev 1 Port 1 qpn 3039 mtu 5 LID 37
n013:101855:101885 [0] NCCL INFO Connected all rings
n013:101855:101885 [0] NCCL INFO Connected all trees
n013:101855:101885 [0] NCCL INFO threadThresholds 8/8/64 | 16/8/64 | 512 | 512
n013:101855:101885 [0] NCCL INFO 2 coll channels, 2 p2p channels, 2 p2p channels per peer
n013:101855:101888 [0] NCCL INFO New proxy send connection 4 from local rank 0, transport 2
n013:101855:101885 [0] NCCL INFO Connection to proxy localRank 0 -> connection 0x1554e8000e50
n013:101855:101885 [0] NCCL INFO comm 0x72a6b00 rank 0 nranks 2 cudaDev 0 busId 81000 commId 0xb2f794396f6d0bd1 - Init COMPLETE
#
#                                                              out-of-place                       in-place          
#       size         count      type   redop    root     time   algbw   busbw #wrong     time   algbw   busbw #wrong
#        (B)    (elements)                               (us)  (GB/s)  (GB/s)            (us)  (GB/s)  (GB/s)       
n013:101855:101890 [0] NCCL INFO GPU Direct RDMA Enabled for GPU 81000 / HCA 1 (distance 6 <= 7), read 0
n013:101855:101888 [0] NCCL INFO New proxy recv connection 5 from local rank 0, transport 2
n013:101855:101890 [0] NCCL INFO Connection to proxy localRank 0 -> connection 0x1554e8000e90
n013:101855:101890 [0] NCCL INFO Channel 00/1 : 1[81000] -> 0[81000] [receive] via NET/IB/1/GDRDMA/Shared
n013:101855:101890 [0] NCCL INFO GPU Direct RDMA Enabled for GPU 81000 / HCA 1 (distance 6 <= 7), read 0
n013:101855:101888 [0] NCCL INFO New proxy recv connection 6 from local rank 0, transport 2
n013:101855:101890 [0] NCCL INFO Connection to proxy localRank 0 -> connection 0x1554e8000ed0
n013:101855:101890 [0] NCCL INFO Channel 01/1 : 1[81000] -> 0[81000] [receive] via NET/IB/1/GDRDMA/Shared
   134217728      16777216     float    none       0   3324.7   40.37   20.19      0   3003.4   44.69   22.34      0
   268435456      33554432     float    none       0   6430.2   41.75   20.87      0   5893.6   45.55   22.77      0
   402653184      50331648     float    none       0    10258   39.25   19.63      0   8708.6   46.24   23.12      0
   536870912      67108864     float    none       0    13608   39.45   19.73      0    12111   44.33   22.16      0
   671088640      83886080     float    none       0    16260   41.27   20.64      0    16075   41.75   20.87      0
   805306368     100663296     float    none       0    20248   39.77   19.89      0    17788   45.27   22.64      0
   939524096     117440512     float    none       0    23721   39.61   19.80      0    21599   43.50   21.75      0
  1073741824     134217728     float    none       0    27257   39.39   19.70      0    23752   45.21   22.60      0
  1207959552     150994944     float    none       0    30606   39.47   19.73      0    27265   44.31   22.15      0
  1342177280     167772160     float    none       0    33588   39.96   19.98      0    29836   44.98   22.49      0
  1476395008     184549376     float    none       0    37296   39.59   19.79      0    32636   45.24   22.62      0
  1610612736     201326592     float    none       0    40866   39.41   19.71      0    34107   47.22   23.61      0
  1744830464     218103808     float    none       0    44513   39.20   19.60      0    38717   45.07   22.53      0
  1879048192     234881024     float    none       0    45718   41.10   20.55      0    41351   45.44   22.72      0
  2013265920     251658240     float    none       0    51368   39.19   19.60      0    44701   45.04   22.52      0
  2147483648     268435456     float    none       0    54511   39.40   19.70      0    48063   44.68   22.34      0
  2281701376     285212672     float    none       0    55666   40.99   20.49      0    51324   44.46   22.23      0
  2415919104     301989888     float    none       0    61683   39.17   19.58      0    53988   44.75   22.37      0
  2550136832     318767104     float    none       0    65144   39.15   19.57      0    57591   44.28   22.14      0
  2684354560     335544320     float    none       0    68336   39.28   19.64      0    60310   44.51   22.25      0
  2818572288     352321536     float    none       0    71938   39.18   19.59      0    63553   44.35   22.17      0
  2952790016     369098752     float    none       0    75381   39.17   19.59      0    66497   44.40   22.20      0
  3087007744     385875968     float    none       0    79402   38.88   19.44      0    69400   44.48   22.24      0
  3221225472     402653184     float    none       0    80327   40.10   20.05      0    73501   43.83   21.91      0
  3355443200     419430400     float    none       0    86066   38.99   19.49      0    77897   43.08   21.54      0
  3489660928     436207616     float    none       0    88027   39.64   19.82      0    79127   44.10   22.05      0
  3623878656     452984832     float    none       0    94523   38.34   19.17      0    82057   44.16   22.08      0
  3758096384     469762048     float    none       0    99864   37.63   18.82      0    86778   43.31   21.65      0
  3892314112     486539264     float    none       0    99991   38.93   19.46      0    89749   43.37   21.68      0
  4026531840     503316480     float    none       0   107382   37.50   18.75      0    96493   41.73   20.86      0
  4160749568     520093696     float    none       0   105443   39.46   19.73      0    98821   42.10   21.05      0
  4294967296     536870912     float    none       0   111114   38.65   19.33      0   112195   38.28   19.14      0
  4429185024     553648128     float    none       0   120452   36.77   18.39      0   107779   41.10   20.55      0
  4563402752     570425344     float    none       0   117945   38.69   19.35      0   108677   41.99   21.00      0
  4697620480     587202560     float    none       0   121553   38.65   19.32      0   125554   37.42   18.71      0
  4831838208     603979776     float    none       0   124061   38.95   19.47      0   116900   41.33   20.67      0
  4966055936     620756992     float    none       0   137979   35.99   18.00      0   119431   41.58   20.79      0
  5100273664     637534208     float    none       0   142845   35.70   17.85      0   118809   42.93   21.46      0
  5234491392     654311424     float    none       0   140954   37.14   18.57      0   125961   41.56   20.78      0
  5368709120     671088640     float    none       0   149268   35.97   17.98      0   127920   41.97   20.98      0
  5502926848     687865856     float    none       0   147914   37.20   18.60      0   139528   39.44   19.72      0
  5637144576     704643072     float    none       0   151145   37.30   18.65      0   136162   41.40   20.70      0
  5771362304     721420288     float    none       0   167124   34.53   17.27      0   136346   42.33   21.16      0
  5905580032     738197504     float    none       0   174402   33.86   16.93      0   140619   42.00   21.00      0
  6039797760     754974720     float    none       0   156288   38.65   19.32      0   141323   42.74   21.37      0
  6174015488     771751936     float    none       0   175408   35.20   17.60      0   152634   40.45   20.22      0
  6308233216     788529152     float    none       0   176003   35.84   17.92      0   153359   41.13   20.57      0
  6442450944     805306368     float    none       0   306351   21.03   10.51      0   273828   23.53   11.76      0
  6576668672     822083584     float    none       0   301792   21.79   10.90      0   301575   21.81   10.90      0
  6710886400     838860800     float    none       0   309970   21.65   10.83      0   304582   22.03   11.02      0
  6845104128     855638016     float    none       0   304117   22.51   11.25      0   279451   24.49   12.25      0
  6979321856     872415232     float    none       0   330908   21.09   10.55      0   331245   21.07   10.53      0
  7113539584     889192448     float    none       0   317414   22.41   11.21      0   316468   22.48   11.24      0
  7247757312     905969664     float    none       0   331690   21.85   10.93      0   301408   24.05   12.02      0
  7381975040     922746880     float    none       0   318830   23.15   11.58      0   313779   23.53   11.76      0
  7516192768     939524096     float    none       0   313273   23.99   12.00      0   316973   23.71   11.86      0
  7650410496     956301312     float    none       0   340277   22.48   11.24      0   347428   22.02   11.01      0
  7784628224     973078528     float    none       0   360704   21.58   10.79      0   338876   22.97   11.49      0
  7918845952     989855744     float    none       0   351401   22.54   11.27      0   359738   22.01   11.01      0
  8053063680    1006632960     float    none       0   365968   22.00   11.00      0   346385   23.25   11.62      0
  8187281408    1023410176     float    none       0   377021   21.72   10.86      0   375012   21.83   10.92      0
  8321499136    1040187392     float    none       0   389544   21.36   10.68      0   369483   22.52   11.26      0
  8455716864    1056964608     float    none       0   363928   23.23   11.62      0   353444   23.92   11.96      0
  8589934592    1073741824     float    none       0   386991   22.20   11.10      0   369719   23.23   11.62      0
  8724152320    1090519040     float    none       0   374592   23.29   11.64      0   413864   21.08   10.54      0
  8858370048    1107296256     float    none       0   416598   21.26   10.63      0   404116   21.92   10.96      0
  8992587776    1124073472     float    none       0   404761   22.22   11.11      0   350925   25.63   12.81      0
  9126805504    1140850688     float    none       0   419431   21.76   10.88      0   422423   21.61   10.80      0
  9261023232    1157627904     float    none       0   425034   21.79   10.89      0   412996   22.42   11.21      0
  9395240960    1174405120     float    none       0   381593   24.62   12.31      0   304994   30.80   15.40      0
  9529458688    1191182336     float    none       0   438666   21.72   10.86      0   427969   22.27   11.13      0
  9663676416    1207959552     float    none       0   453328   21.32   10.66      0   437396   22.09   11.05      0
  9797894144    1224736768     float    none       0   426711   22.96   11.48      0   431443   22.71   11.35      0
  9932111872    1241513984     float    none       0   446263   22.26   11.13      0   444847   22.33   11.16      0
 10066329600    1258291200     float    none       0   434423   23.17   11.59      0   454409   22.15   11.08      0
 10200547328    1275068416     float    none       0   445690   22.89   11.44      0   447690   22.78   11.39      0
 10334765056    1291845632     float    none       0   467901   22.09   11.04      0   465812   22.19   11.09      0
 10468982784    1308622848     float    none       0   476271   21.98   10.99      0   490963   21.32   10.66      0
 10603200512    1325400064     float    none       0   466551   22.73   11.36      0   474781   22.33   11.17      0
 10737418240    1342177280     float    none       0   504689   21.28   10.64      0   466925   23.00   11.50      0
 10871635968    1358954496     float    none       0   497065   21.87   10.94      0   473553   22.96   11.48      0
 11005853696    1375731712     float    none       0   472796   23.28   11.64      0   499943   22.01   11.01      0
 11140071424    1392508928     float    none       0   517481   21.53   10.76      0   421829   26.41   13.20      0
 11274289152    1409286144     float    none       0   525805   21.44   10.72      0   492491   22.89   11.45      0
 11408506880    1426063360     float    none       0   522721   21.83   10.91      0   524916   21.73   10.87      0

``` 



```
	     GPU0	         NIC0	NIC1	 NIC2	NIC3	CPU Affinity	NUMA Affinity	GPU NUMA ID
GPU0	 X 	          SYS	SYS	        NODE	NODE	64-127,192-255	1		N/A
NIC0	SYS	             X 	PIX	          SYS	SYS				
NIC1	SYS	           PIX	 X  	          SYS	SYS				
NIC2	NODE	   SYS	SYS	           X 	        PIX				
NIC3	NODE	   SYS	SYS	         PIX	         X 				

Legend:

  X    = Self
  SYS  = Connection traversing PCIe as well as the SMP interconnect between NUMA nodes (e.g., QPI/UPI)
  NODE = Connection traversing PCIe as well as the interconnect between PCIe Host Bridges within a NUMA node
  PHB  = Connection traversing PCIe as well as a PCIe Host Bridge (typically the CPU)
  PXB  = Connection traversing multiple PCIe bridges (without traversing the PCIe Host Bridge)
  PIX  = Connection traversing at most a single PCIe bridge
  NV#  = Connection traversing a bonded set of # NVLinks

NIC Legend:

  NIC0: mlx5_0
  NIC1: mlx5_1
  NIC2: mlx5_2
  NIC3: mlx5_3
``` 

```
CA 'mlx5_0'
        CA type: MT4117
        Number of ports: 1
        Firmware version: 14.32.1010
        Hardware version: 0
        Node GUID: 0xb8cef60300cee2b8
        System image GUID: 0xb8cef60300cee2b8
        Port 1:
                State: Active
                Physical state: LinkUp
                Rate: 25
                Base lid: 0
                LMC: 0
                SM lid: 0
                Capability mask: 0x00010000
                Port GUID: 0xbacef6fffecee2b8
                Link layer: Ethernet
CA 'mlx5_1'
        CA type: MT4117
        Number of ports: 1
        Firmware version: 14.32.1010
        Hardware version: 0
        Node GUID: 0xb8cef60300cee2b9
        System image GUID: 0xb8cef60300cee2b8
        Port 1:
                State: Down
                Physical state: Disabled
                Rate: 40
                Base lid: 0
                LMC: 0
                SM lid: 0
                Capability mask: 0x00010000
                Port GUID: 0xbacef6fffecee2b9
                Link layer: Ethernet
CA 'mlx5_2'
        CA type: MT4123
        Number of ports: 1
        Firmware version: 20.43.1014
        Hardware version: 0
        Node GUID: 0xb8cef603002d857a
        System image GUID: 0xb8cef603002d857a
        Port 1:
                State: Active
                Physical state: LinkUp
                Rate: 200
                Base lid: 37
                LMC: 0
                SM lid: 26
                Capability mask: 0xa651e848
                Port GUID: 0xb8cef603002d857a
                Link layer: InfiniBand
CA 'mlx5_3'
        CA type: MT4123
        Number of ports: 1
        Firmware version: 20.43.1014
        Hardware version: 0
        Node GUID: 0xb8cef603002d857b
        System image GUID: 0xb8cef603002d857a
        Port 1:
                State: Down
                Physical state: Disabled
                Rate: 10
                Base lid: 65535
                LMC: 0
                SM lid: 0
                Capability mask: 0xa651e848
                Port GUID: 0xb8cef603002d857b
                Link layer: InfiniBand

``` 

## 评论 (1)

### eng9433 · 2025-10-20

Forgot to pass `NCCL_NET_GDR_LEVEL` environment variable to remote nodes. 

Closing.
