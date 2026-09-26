# [Issue #6406] Reading Memory Domain config fails with Project Panama Java bindings

source: https://github.com/openucx/ucx/issues/6406
state: closed | updated: 2026-02-09T09:39:39Z
labels: Bug

## 正文

### Describe the bug

> :information_source: &nbsp; **Note**
> &nbsp;
> I don't know if this is the right place for this issue, since the cause might not be ucx itself. Please excuse if this is the wrong place.

I use Oracle's [Project Panama](https://github.com/openjdk/panama-foreign) (which will replace JNI in the near feature) to generate Java bindings for ucp. Everything works pretty well until I try to switch to InfiniBand hardware (ConnectX-5). The weird thing I notice while running `ucp_init` from Java (in fact, I use `ucp_init_version` since `ucp_init` is inline and therefore the symbol can't be looked up inside the shared library at runtime) is, that some warnings are logged which do not appear with a compiled C binary executing the same functions in the same order. I looked up where those warnings are coming from and concluded that the library is trying to detect the InfiniBand hardware, but fails at parsing some configuration value (which I do not touch at all) due to an invalid format which doesn't seem wrong to me.

```
[1614368918.117231] [host:16342:0]         parser.c:928  UCX  ERROR Invalid value for MEM_REG_GROWTH: '0.06ns'. Expected: time value: <number>[s|us|ms|ns]
[1614368918.117243] [host:16342:0]         uct_md.c:270  UCX  ERROR Failed to read MD config
[1614368918.117251] [host:16342:0]         parser.c:928  UCX  ERROR Invalid value for MEM_REG_GROWTH: '0.06ns'. Expected: time value: <number>[s|us|ms|ns]
[1614368918.117254] [host:16342:0]         uct_md.c:270  UCX  ERROR Failed to read MD config
[1614368918.117259] [host:16342:0]         parser.c:928  UCX  ERROR Invalid value for MEM_REG_GROWTH: '0.06ns'. Expected: time value: <number>[s|us|ms|ns]
[1614368918.117262] [host:16342:0]         uct_md.c:270  UCX  ERROR Failed to read MD config
```

Are there any pitfalls I have to look out for when calling ucx  functions from other languages than C?

### Steps to Reproduce

Here are the source files I use for a minimal example reproducing the problem I describe.

`ucx.h`
```c
#include <ucp/api/ucp.h>

#include <string.h> 
#include <unistd.h>
#include <stdlib.h>
```

`info.c`
```c
#include "ucx.h"

int main(int argc, char **argv) {

    ucp_context_h ucp_context;
    ucp_params_t ucp_params;
    ucs_status_t status;
    int ret = 0;

    memset(&ucp_params, 0, sizeof(ucp_params));

    ucp_params.field_mask = UCP_PARAM_FIELD_FEATURES;
    ucp_params.features = UCP_FEATURE_TAG;

    status = ucp_init(&ucp_params, NULL, &ucp_context);
    if (status != UCS_OK) {
        fprintf(stderr, "failed to ucp_init (%s)\n", ucs_status_string(status));
        ret = -1;
        goto err;
    }
    
    ucp_context_print_info(ucp_context, stdout);


    ucp_cleanup(ucp_context);
err:
    return ret;
}
```

`Info.java`
```java

import jdk.incubator.foreign.*;

import static org.openucx.ucx_h.*;

public class Info {

  public static void main(String... args) {
    var ucp_context = MemorySegment.allocateNative(CLinker.C_POINTER);
    var ucp_params = ucp_params_t.allocate();

    ucp_params_t.field_mask$set(ucp_params, UCP_PARAM_FIELD_FEATURES());
    ucp_params_t.features$set(ucp_params, UCP_FEATURE_TAG());

    var status = ucp_init_version(UCP_API_MAJOR(), UCP_API_MINOR(),
            ucp_params, MemoryAddress.NULL, ucp_context);

    if (status != UCS_OK()) {
        System.err.printf("failed to ucp_init (%s)\n", CLinker.toJavaStringRestricted(ucs_status_string(status)));
        System.exit(-1);
    }

    ucp_context_print_info(ucp_context, stdout$get());

    ucp_cleanup(ucp_context);
  }
}
```

Running the C example yields the expected output.

```
$> gcc -lucp -lucs info.c -o info
$> ./info
...
#            md 5  :  component 5  mlx5_0
...
#      resource 6  :  md 5  dev 4  flags -- rc_verbs/mlx5_0:1
#      resource 7  :  md 5  dev 4  flags -- rc_mlx5/mlx5_0:1
#      resource 8  :  md 5  dev 4  flags -- dc_mlx5/mlx5_0:1
#      resource 9  :  md 5  dev 4  flags -- ud_verbs/mlx5_0:1
#      resource 10 :  md 5  dev 4  flags -- ud_mlx5/mlx5_0:1
...
```

Running the Java example logs some warnings while trying to detect the IninifBand hardware and doesn't list it under the resources like in the C example.

```
$> jextract -t org.openucx -lucp ucx.h  # This generates the bindings
$> java -Dforeign.restricted=permit --add-modules jdk.incubator.foreign Info.java
...
[1614368918.117231] [host:16342:0]         parser.c:928  UCX  ERROR Invalid value for MEM_REG_GROWTH: '0.06ns'. Expected: time value: <number>[s|us|ms|ns]
[1614368918.117243] [host:16342:0]         uct_md.c:270  UCX  ERROR Failed to read MD config
[1614368918.117251] [host:16342:0]         parser.c:928  UCX  ERROR Invalid value for MEM_REG_GROWTH: '0.06ns'. Expected: time value: <number>[s|us|ms|ns]
[1614368918.117254] [host:16342:0]         uct_md.c:270  UCX  ERROR Failed to read MD config
[1614368918.117259] [host:16342:0]         parser.c:928  UCX  ERROR Invalid value for MEM_REG_GROWTH: '0.06ns'. Expected: time value: <number>[s|us|ms|ns]
[1614368918.117262] [host:16342:0]         uct_md.c:270  UCX  ERROR Failed to read MD config
...
```

### Operating System

  * Operating System : `CentOS Linux release 8.1.1911 (Core)`
  * Kernel : `4.18.0-277.el8.x86_64`

### Packages

  * `rdma-core-32.0-4.el8.x86_64`
  * `ucx-1.9.0-1.el8.x86_64`
  * `ucx-ib-1.9.0-1.el8.x86_64`
  * `ucx-rdmacm-1.9.0-1.el8.x86_64`
  * `ucx-cma-1.9.0-1.el8.x86_64`
  * `ucx-devel-1.9.0-1.el8.x86_64`

### Hardware

  * `ibstat`

    ```
    CA 'mlx5_0'
	    CA type: MT4119
	    Number of ports: 1
	    Firmware version: 16.29.2002
	    Hardware version: 0
	    Node GUID: 0x0c42a10300547792
	    System image GUID: 0x0c42a10300547792
	    Port 1:
		    State: Active
		    Physical state: LinkUp
		    Rate: 56
		    Base lid: 197
		    LMC: 0
		    SM lid: 8
		    Capability mask: 0x2659e848
		    Port GUID: 0x0c42a10300547792
		    Link layer: InfiniBand
    ```

### Additional information

  * `ucx_info -d`
    ```
    #
    # Memory domain: posix
    #     Component: posix
    #             allocate: unlimited
    #           remote key: 24 bytes
    #           rkey_ptr is supported
    #
    #   Transport: posix
    #      Device: memory
    #
    #      capabilities:
    #            bandwidth: 0.00/ppn + 12179.00 MB/sec
    #              latency: 80 nsec
    #             overhead: 10 nsec
    #            put_short: <= 4294967295
    #            put_bcopy: unlimited
    #            get_bcopy: unlimited
    #             am_short: <= 100
    #             am_bcopy: <= 8256
    #               domain: cpu
    #           atomic_add: 32, 64 bit
    #           atomic_and: 32, 64 bit
    #            atomic_or: 32, 64 bit
    #           atomic_xor: 32, 64 bit
    #          atomic_fadd: 32, 64 bit
    #          atomic_fand: 32, 64 bit
    #           atomic_for: 32, 64 bit
    #          atomic_fxor: 32, 64 bit
    #          atomic_swap: 32, 64 bit
    #         atomic_cswap: 32, 64 bit
    #           connection: to iface
    #      device priority: 0
    #     device num paths: 1
    #              max eps: inf
    #       device address: 8 bytes
    #        iface address: 8 bytes
    #       error handling: none
    #
    #
    # Memory domain: sysv
    #     Component: sysv
    #             allocate: unlimited
    #           remote key: 12 bytes
    #           rkey_ptr is supported
    #
    #   Transport: sysv
    #      Device: memory
    #
    #      capabilities:
    #            bandwidth: 0.00/ppn + 12179.00 MB/sec
    #              latency: 80 nsec
    #             overhead: 10 nsec
    #            put_short: <= 4294967295
    #            put_bcopy: unlimited
    #            get_bcopy: unlimited
    #             am_short: <= 100
    #             am_bcopy: <= 8256
    #               domain: cpu
    #           atomic_add: 32, 64 bit
    #           atomic_and: 32, 64 bit
    #            atomic_or: 32, 64 bit
    #           atomic_xor: 32, 64 bit
    #          atomic_fadd: 32, 64 bit
    #          atomic_fand: 32, 64 bit
    #           atomic_for: 32, 64 bit
    #          atomic_fxor: 32, 64 bit
    #          atomic_swap: 32, 64 bit
    #         atomic_cswap: 32, 64 bit
    #           connection: to iface
    #      device priority: 0
    #     device num paths: 1
    #              max eps: inf
    #       device address: 8 bytes
    #        iface address: 8 bytes
    #       error handling: none
    #
    #
    # Memory domain: self
    #     Component: self
    #             register: unlimited, cost: 0 nsec
    #           remote key: 0 bytes
    #
    #   Transport: self
    #      Device: memory
    #
    #      capabilities:
    #            bandwidth: 0.00/ppn + 6911.00 MB/sec
    #              latency: 0 nsec
    #             overhead: 10 nsec
    #            put_short: <= 4294967295
    #            put_bcopy: unlimited
    #            get_bcopy: unlimited
    #             am_short: <= 8K
    #             am_bcopy: <= 8K
    #               domain: cpu
    #           atomic_add: 32, 64 bit
    #           atomic_and: 32, 64 bit
    #            atomic_or: 32, 64 bit
    #           atomic_xor: 32, 64 bit
    #          atomic_fadd: 32, 64 bit
    #          atomic_fand: 32, 64 bit
    #           atomic_for: 32, 64 bit
    #          atomic_fxor: 32, 64 bit
    #          atomic_swap: 32, 64 bit
    #         atomic_cswap: 32, 64 bit
    #           connection: to iface
    #      device priority: 0
    #     device num paths: 1
    #              max eps: inf
    #       device address: 0 bytes
    #        iface address: 8 bytes
    #       error handling: none
    #
    #
    # Memory domain: tcp
    #     Component: tcp
    #             register: unlimited, cost: 0 nsec
    #           remote key: 0 bytes
    #
    #   Transport: tcp
    #      Device: eno1
    #
    #      capabilities:
    #            bandwidth: 113.16/ppn + 0.00 MB/sec
    #              latency: 5776 nsec
    #             overhead: 50000 nsec
    #            put_zcopy: <= 18446744073709551590, up to 6 iov
    #  put_opt_zcopy_align: <= 1
    #        put_align_mtu: <= 0
    #             am_short: <= 8K
    #             am_bcopy: <= 8K
    #             am_zcopy: <= 64K, up to 6 iov
    #   am_opt_zcopy_align: <= 1
    #         am_align_mtu: <= 0
    #            am header: <= 8037
    #           connection: to iface
    #      device priority: 1
    #     device num paths: 1
    #              max eps: 256
    #       device address: 4 bytes
    #        iface address: 2 bytes
    #       error handling: none
    #
    #   Transport: tcp
    #      Device: ib0
    #
    #      capabilities:
    #            bandwidth: 6239.81/ppn + 0.00 MB/sec
    #              latency: 5210 nsec
    #             overhead: 50000 nsec
    #            put_zcopy: <= 18446744073709551590, up to 6 iov
    #  put_opt_zcopy_align: <= 1
    #        put_align_mtu: <= 0
    #             am_short: <= 8K
    #             am_bcopy: <= 8K
    #             am_zcopy: <= 64K, up to 6 iov
    #   am_opt_zcopy_align: <= 1
    #         am_align_mtu: <= 0
    #            am header: <= 8037
    #           connection: to iface
    #      device priority: 1
    #     device num paths: 1
    #              max eps: 256
    #       device address: 4 bytes
    #        iface address: 2 bytes
    #       error handling: none
    #
    #
    # Connection manager: tcp
    #      max_conn_priv: 2032 bytes
    #
    # Memory domain: sockcm
    #     Component: sockcm
    #           supports client-server connection establishment via sockaddr
    #   < no supported devices found >
    #
    # Memory domain: i40iw0
    #     Component: ib
    #             register: unlimited, cost: 180 nsec
    #           remote key: 8 bytes
    #           local memory handle is required for zcopy
    #   < no supported devices found >
    #
    # Memory domain: i40iw1
    #     Component: ib
    #             register: unlimited, cost: 180 nsec
    #           remote key: 8 bytes
    #           local memory handle is required for zcopy
    #   < no supported devices found >
    #
    # Memory domain: mlx5_0
    #     Component: ib
    #             register: unlimited, cost: 180 nsec
    #           remote key: 8 bytes
    #           local memory handle is required for zcopy
    #
    #   Transport: rc_verbs
    #      Device: mlx5_0:1
    #
    #      capabilities:
    #            bandwidth: 6433.22/ppn + 0.00 MB/sec
    #              latency: 700 + 1.000 * N nsec
    #             overhead: 75 nsec
    #            put_short: <= 124
    #            put_bcopy: <= 8256
    #            put_zcopy: <= 1G, up to 3 iov
    #  put_opt_zcopy_align: <= 512
    #        put_align_mtu: <= 4K
    #            get_bcopy: <= 8256
    #            get_zcopy: 65..1G, up to 3 iov
    #  get_opt_zcopy_align: <= 512
    #        get_align_mtu: <= 4K
    #             am_short: <= 123
    #             am_bcopy: <= 8255
    #             am_zcopy: <= 8255, up to 2 iov
    #   am_opt_zcopy_align: <= 512
    #         am_align_mtu: <= 4K
    #            am header: <= 127
    #               domain: device
    #           atomic_add: 64 bit
    #          atomic_fadd: 64 bit
    #         atomic_cswap: 64 bit
    #           connection: to ep
    #      device priority: 38
    #     device num paths: 1
    #              max eps: 256
    #       device address: 3 bytes
    #           ep address: 17 bytes
    #       error handling: peer failure
    #
    #
    #   Transport: rc_mlx5
    #      Device: mlx5_0:1
    #
    #      capabilities:
    #            bandwidth: 6433.22/ppn + 0.00 MB/sec
    #              latency: 700 + 1.000 * N nsec
    #             overhead: 40 nsec
    #            put_short: <= 2K
    #            put_bcopy: <= 8256
    #            put_zcopy: <= 1G, up to 14 iov
    #  put_opt_zcopy_align: <= 512
    #        put_align_mtu: <= 4K
    #            get_bcopy: <= 8256
    #            get_zcopy: 65..1G, up to 14 iov
    #  get_opt_zcopy_align: <= 512
    #        get_align_mtu: <= 4K
    #             am_short: <= 2046
    #             am_bcopy: <= 8254
    #             am_zcopy: <= 8254, up to 3 iov
    #   am_opt_zcopy_align: <= 512
    #         am_align_mtu: <= 4K
    #            am header: <= 186
    #               domain: device
    #           atomic_add: 32, 64 bit
    #           atomic_and: 32, 64 bit
    #            atomic_or: 32, 64 bit
    #           atomic_xor: 32, 64 bit
    #          atomic_fadd: 32, 64 bit
    #          atomic_fand: 32, 64 bit
    #           atomic_for: 32, 64 bit
    #          atomic_fxor: 32, 64 bit
    #          atomic_swap: 32, 64 bit
    #         atomic_cswap: 32, 64 bit
    #           connection: to ep
    #      device priority: 38
    #     device num paths: 1
    #              max eps: 256
    #       device address: 3 bytes
    #           ep address: 7 bytes
    #       error handling: buffer (zcopy), remote access, peer failure
    #
    #
    #   Transport: dc_mlx5
    #      Device: mlx5_0:1
    #
    #      capabilities:
    #            bandwidth: 6433.22/ppn + 0.00 MB/sec
    #              latency: 760 nsec
    #             overhead: 40 nsec
    #            put_short: <= 2K
    #            put_bcopy: <= 8256
    #            put_zcopy: <= 1G, up to 11 iov
    #  put_opt_zcopy_align: <= 512
    #        put_align_mtu: <= 4K
    #            get_bcopy: <= 8256
    #            get_zcopy: 65..1G, up to 11 iov
    #  get_opt_zcopy_align: <= 512
    #        get_align_mtu: <= 4K
    #             am_short: <= 2046
    #             am_bcopy: <= 8254
    #             am_zcopy: <= 8254, up to 3 iov
    #   am_opt_zcopy_align: <= 512
    #         am_align_mtu: <= 4K
    #            am header: <= 138
    #               domain: device
    #           atomic_add: 32, 64 bit
    #           atomic_and: 32, 64 bit
    #            atomic_or: 32, 64 bit
    #           atomic_xor: 32, 64 bit
    #          atomic_fadd: 32, 64 bit
    #          atomic_fand: 32, 64 bit
    #           atomic_for: 32, 64 bit
    #          atomic_fxor: 32, 64 bit
    #          atomic_swap: 32, 64 bit
    #         atomic_cswap: 32, 64 bit
    #           connection: to iface
    #      device priority: 38
    #     device num paths: 1
    #              max eps: inf
    #       device address: 3 bytes
    #        iface address: 5 bytes
    #       error handling: buffer (zcopy), remote access, peer failure
    #
    #
    #   Transport: ud_verbs
    #      Device: mlx5_0:1
    #
    #      capabilities:
    #            bandwidth: 6433.22/ppn + 0.00 MB/sec
    #              latency: 730 nsec
    #             overhead: 105 nsec
    #             am_short: <= 116
    #             am_bcopy: <= 4088
    #             am_zcopy: <= 4088, up to 1 iov
    #   am_opt_zcopy_align: <= 512
    #         am_align_mtu: <= 4K
    #            am header: <= 3952
    #           connection: to ep, to iface
    #      device priority: 38
    #     device num paths: 1
    #              max eps: inf
    #       device address: 3 bytes
    #        iface address: 3 bytes
    #           ep address: 6 bytes
    #       error handling: peer failure
    #
    #
    #   Transport: ud_mlx5
    #      Device: mlx5_0:1
    #
    #      capabilities:
    #            bandwidth: 6433.22/ppn + 0.00 MB/sec
    #              latency: 730 nsec
    #             overhead: 80 nsec
    #             am_short: <= 180
    #             am_bcopy: <= 4088
    #             am_zcopy: <= 4088, up to 3 iov
    #   am_opt_zcopy_align: <= 512
    #         am_align_mtu: <= 4K
    #            am header: <= 132
    #           connection: to ep, to iface
    #      device priority: 38
    #     device num paths: 1
    #              max eps: inf
    #       device address: 3 bytes
    #        iface address: 3 bytes
    #           ep address: 6 bytes
    #       error handling: peer failure
    #
    #
    # Memory domain: rdmacm
    #     Component: rdmacm
    #           supports client-server connection establishment via sockaddr
    #   < no supported devices found >
    #
    # Connection manager: rdmacm
    #      max_conn_priv: 54 bytes
    #
    # Memory domain: cma
    #     Component: cma
    #             register: unlimited, cost: 9 nsec
    #
    #   Transport: cma
    #      Device: memory
    #
    #      capabilities:
    #            bandwidth: 0.00/ppn + 11145.00 MB/sec
    #              latency: 80 nsec
    #             overhead: 400 nsec
    #            put_zcopy: unlimited, up to 16 iov
    #  put_opt_zcopy_align: <= 1
    #        put_align_mtu: <= 1
    #            get_zcopy: unlimited, up to 16 iov
    #  get_opt_zcopy_align: <= 1
    #        get_align_mtu: <= 1
    #           connection: to iface
    #      device priority: 0
    #     device num paths: 1
    #              max eps: inf
    #       device address: 8 bytes
    #        iface address: 4 bytes
    #       error handling: none
    #
    ```

  * `ucx_info -b`
    ```
    #define UCX_CONFIG_H              
    #define ENABLE_BUILTIN_MEMCPY     1
    #define ENABLE_DEBUG_DATA         0
    #define ENABLE_MT                 0
    #define ENABLE_PARAMS_CHECK       0
    #define ENABLE_SYMBOL_OVERRIDE    1
    #define HAVE_1_ARG_BFD_SECTION_SIZE 0
    #define HAVE_ALLOCA               1
    #define HAVE_ALLOCA_H             1
    #define HAVE_ATTRIBUTE_NOOPTIMIZE 1
    #define HAVE_CLEARENV             1
    #define HAVE_CPU_SET_T            1
    #define HAVE_DC_DV                1
    #define HAVE_DECL_ASPRINTF        1
    #define HAVE_DECL_BASENAME        1
    #define HAVE_DECL_BFD_GET_SECTION_FLAGS 0
    #define HAVE_DECL_BFD_GET_SECTION_VMA 0
    #define HAVE_DECL_BFD_SECTION_FLAGS 0
    #define HAVE_DECL_BFD_SECTION_VMA 0
    #define HAVE_DECL_CPU_ISSET       1
    #define HAVE_DECL_CPU_ZERO        1
    #define HAVE_DECL_ETHTOOL_CMD_SPEED 1
    #define HAVE_DECL_FMEMOPEN        1
    #define HAVE_DECL_F_SETOWN_EX     1
    #define HAVE_DECL_IBV_ACCESS_ON_DEMAND 1
    #define HAVE_DECL_IBV_ACCESS_RELAXED_ORDERING 1
    #define HAVE_DECL_IBV_ADVISE_MR   1
    #define HAVE_DECL_IBV_ALLOC_DM    1
    #define HAVE_DECL_IBV_ALLOC_TD    1
    #define HAVE_DECL_IBV_CMD_MODIFY_QP 0
    #define HAVE_DECL_IBV_CREATE_CQ_ATTR_IGNORE_OVERRUN 1
    #define HAVE_DECL_IBV_CREATE_QP_EX 1
    #define HAVE_DECL_IBV_CREATE_SRQ  1
    #define HAVE_DECL_IBV_CREATE_SRQ_EX 1
    #define HAVE_DECL_IBV_EVENT_GID_CHANGE 1
    #define HAVE_DECL_IBV_EVENT_TYPE_STR 1
    #define HAVE_DECL_IBV_EXP_ACCESS_ALLOCATE_MR 0
    #define HAVE_DECL_IBV_EXP_ACCESS_ON_DEMAND 0
    #define HAVE_DECL_IBV_EXP_ALLOC_DM 0
    #define HAVE_DECL_IBV_EXP_ATOMIC_HCA_REPLY_BE 0
    #define HAVE_DECL_IBV_EXP_CQ_IGNORE_OVERRUN 0
    #define HAVE_DECL_IBV_EXP_CQ_MODERATION 0
    #define HAVE_DECL_IBV_EXP_CREATE_QP 0
    #define HAVE_DECL_IBV_EXP_CREATE_SRQ 0
    #define HAVE_DECL_IBV_EXP_DCT_OOO_RW_DATA_PLACEMENT 0
    #define HAVE_DECL_IBV_EXP_DEVICE_ATTR_PCI_ATOMIC_CAPS 0
    #define HAVE_DECL_IBV_EXP_DEVICE_ATTR_RESERVED_2 0
    #define HAVE_DECL_IBV_EXP_DEVICE_DC_TRANSPORT 0
    #define HAVE_DECL_IBV_EXP_DEVICE_MR_ALLOCATE 0
    #define HAVE_DECL_IBV_EXP_MR_FIXED_BUFFER_SIZE 0
    #define HAVE_DECL_IBV_EXP_MR_INDIRECT_KLMS 0
    #define HAVE_DECL_IBV_EXP_ODP_SUPPORT_IMPLICIT 0
    #define HAVE_DECL_IBV_EXP_POST_SEND 0
    #define HAVE_DECL_IBV_EXP_PREFETCH_MR 0
    #define HAVE_DECL_IBV_EXP_PREFETCH_WRITE_ACCESS 0
    #define HAVE_DECL_IBV_EXP_QPT_DC_INI 0
    #define HAVE_DECL_IBV_EXP_QP_CREATE_UMR 0
    #define HAVE_DECL_IBV_EXP_QP_INIT_ATTR_ATOMICS_ARG 0
    #define HAVE_DECL_IBV_EXP_QP_OOO_RW_DATA_PLACEMENT 0
    #define HAVE_DECL_IBV_EXP_QUERY_DEVICE 0
    #define HAVE_DECL_IBV_EXP_QUERY_GID_ATTR 0
    #define HAVE_DECL_IBV_EXP_REG_MR  0
    #define HAVE_DECL_IBV_EXP_SEND_EXT_ATOMIC_INLINE 0
    #define HAVE_DECL_IBV_EXP_SETENV  0
    #define HAVE_DECL_IBV_EXP_WR_EXT_MASKED_ATOMIC_CMP_AND_SWP 0
    #define HAVE_DECL_IBV_EXP_WR_EXT_MASKED_ATOMIC_FETCH_AND_ADD 0
    #define HAVE_DECL_IBV_EXP_WR_NOP  0
    #define HAVE_DECL_IBV_GET_ASYNC_EVENT 1
    #define HAVE_DECL_IBV_GET_DEVICE_NAME 1
    #define HAVE_DECL_IBV_LINK_LAYER_ETHERNET 1
    #define HAVE_DECL_IBV_LINK_LAYER_INFINIBAND 1
    #define HAVE_DECL_IBV_ODP_SUPPORT_IMPLICIT 1
    #define HAVE_DECL_IBV_QPF_GRH_REQUIRED 1
    #define HAVE_DECL_IBV_QUERY_DEVICE_EX 1
    #define HAVE_DECL_IBV_QUERY_GID   1
    #define HAVE_DECL_IBV_WC_STATUS_STR 1
    #define HAVE_DECL_MADV_FREE       1
    #define HAVE_DECL_MADV_REMOVE     1
    #define HAVE_DECL_MLX5DV_CQ_INIT_ATTR_MASK_CQE_SIZE 1
    #define HAVE_DECL_MLX5DV_CREATE_QP 1
    #define HAVE_DECL_MLX5DV_DCTYPE_DCT 1
    #define HAVE_DECL_MLX5DV_DEVX_SUBSCRIBE_DEVX_EVENT 1
    #define HAVE_DECL_MLX5DV_INIT_OBJ 1
    #define HAVE_DECL_MLX5DV_IS_SUPPORTED 1
    #define HAVE_DECL_MLX5DV_OBJ_AH   1
    #define HAVE_DECL_MLX5DV_QP_CREATE_ALLOW_SCATTER_TO_CQE 1
    #define HAVE_DECL_POSIX_MADV_DONTNEED 1
    #define HAVE_DECL_PR_SET_PTRACER  1
    #define HAVE_DECL_RDMA_ESTABLISH  1
    #define HAVE_DECL_RDMA_INIT_QP_ATTR 1
    #define HAVE_DECL_SPEED_UNKNOWN   1
    #define HAVE_DECL_STRERROR_R      1
    #define HAVE_DECL_SYS_BRK         1
    #define HAVE_DECL_SYS_IPC         0
    #define HAVE_DECL_SYS_MADVISE     1
    #define HAVE_DECL_SYS_MMAP        1
    #define HAVE_DECL_SYS_MREMAP      1
    #define HAVE_DECL_SYS_MUNMAP      1
    #define HAVE_DECL_SYS_SHMAT       1
    #define HAVE_DECL_SYS_SHMDT       1
    #define HAVE_DECL___PPC_GET_TIMEBASE_FREQ 0
    #define HAVE_DEVX                 1
    #define HAVE_DLFCN_H              1
    #define HAVE_HW_TIMER             1
    #define HAVE_IB                   1
    #define HAVE_IBV_DM               1
    #define HAVE_IN6_ADDR_S6_ADDR32   1
    #define HAVE_INFINIBAND_MLX5DV_H  1
    #define HAVE_INFINIBAND_TM_TYPES_H 1
    #define HAVE_INTTYPES_H           1
    #define HAVE_IP_IP_DST            1
    #define HAVE_LIBGEN_H             1
    #define HAVE_LIBRT                1
    #define HAVE_LINUX_FUTEX_H        1
    #define HAVE_LINUX_IP_H           1
    #define HAVE_LINUX_MMAN_H         1
    #define HAVE_MALLOC_H             1
    #define HAVE_MALLOC_HOOK          1
    #define HAVE_MALLOC_TRIM          1
    #define HAVE_MEMALIGN             1
    #define HAVE_MEMORY_H             1
    #define HAVE_MLX5_HW              1
    #define HAVE_MLX5_HW_UD           1
    #define HAVE_MREMAP               1
    #define HAVE_NETINET_IP_H         1
    #define HAVE_NET_ETHERNET_H       1
    #define HAVE_NUMA                 1
    #define HAVE_NUMAIF_H             1
    #define HAVE_NUMA_H               1
    #define HAVE_ODP                  1
    #define HAVE_ODP_IMPLICIT         1
    #define HAVE_POSIX_MEMALIGN       1
    #define HAVE_PREFETCH             1
    #define HAVE_RDMACM_QP_LESS       1
    #define HAVE_SCHED_GETAFFINITY    1
    #define HAVE_SCHED_SETAFFINITY    1
    #define HAVE_SIGACTION_SA_RESTORER 1
    #define HAVE_SIGEVENT_SIGEV_UN_TID 1
    #define HAVE_SIGHANDLER_T         1
    #define HAVE_STDINT_H             1
    #define HAVE_STDLIB_H             1
    #define HAVE_STRERROR_R           1
    #define HAVE_STRINGS_H            1
    #define HAVE_STRING_H             1
    #define HAVE_STRUCT_BITMASK       1
    #define HAVE_STRUCT_DL_PHDR_INFO  1
    #define HAVE_STRUCT_IBV_DEVICE_ATTR_EX_PCI_ATOMIC_CAPS 1
    #define HAVE_STRUCT_IBV_TM_CAPS_FLAGS 1
    #define HAVE_STRUCT_MLX5DV_CQ_CQ_UAR 1
    #define HAVE_SYS_EPOLL_H          1
    #define HAVE_SYS_EVENTFD_H        1
    #define HAVE_SYS_STAT_H           1
    #define HAVE_SYS_TYPES_H          1
    #define HAVE_SYS_UIO_H            1
    #define HAVE_TL_DC                1
    #define HAVE_TL_RC                1
    #define HAVE_TL_UD                1
    #define HAVE_UCM_PTMALLOC286      1
    #define HAVE_UNISTD_H             1
    #define HAVE___CLEAR_CACHE        1
    #define HAVE___CURBRK             1
    #define HAVE___SIGHANDLER_T       1
    #define IBV_HW_TM                 1
    #define LT_OBJDIR                 ".libs/"
    #define NVALGRIND                 1
    #define PACKAGE                   "ucx"
    #define PACKAGE_BUGREPORT         ""
    #define PACKAGE_NAME              "ucx"
    #define PACKAGE_STRING            "ucx 1.9"
    #define PACKAGE_TARNAME           "ucx"
    #define PACKAGE_URL               ""
    #define PACKAGE_VERSION           "1.9"
    #define STDC_HEADERS              1
    #define STRERROR_R_CHAR_P         1
    #define UCM_BISTRO_HOOKS          1
    #define UCS_MAX_LOG_LEVEL         UCS_LOG_LEVEL_INFO
    #define UCT_UD_EP_DEBUG_HOOKS     0
    #define UCX_CONFIGURE_FLAGS       "--build=x86_64-redhat-linux-gnu --host=x86_64-redhat-linux-gnu --program-prefix= --disable-dependency-tracking --prefix=/usr --exec-prefix=/usr --bindir=/usr/bin --sbindir=/usr/sbin --sysconfdir=/etc --datadir=/usr/share --includedir=/usr/include --libdir=/usr/lib64 --libexecdir=/usr/libexec --localstatedir=/var --sharedstatedir=/var/lib --mandir=/usr/share/man --infodir=/usr/share/info --disable-optimizations --disable-logging --disable-debug --disable-assertions --disable-params-check --enable-examples --without-java --enable-cma --without-cuda --without-gdrcopy --with-verbs --without-cm --without-knem --with-rdmacm --without-rocm --without-xpmem --without-ugni"
    #define UCX_MODULE_SUBDIR         "ucx"
    #define VERSION                   "1.9"
    #define restrict                  __restrict
    #define test_MODULES              ":module"
    #define ucm_MODULES               ""
    #define uct_MODULES               ":ib:rdmacm:cma"
    #define uct_cuda_MODULES          ""
    #define uct_ib_MODULES            ""
    #define uct_rocm_MODULES          ""
    #define ucx_perftest_MODULES      ""
    ```


## 评论 (13)

### yosefe · 2021-02-26

@krakowski can you trace whether ucs_config_sscanf_time() function is being called to parse the '0.06ns' value? and if yes, on which line it fails?

### krakowski · 2021-02-26

Don't really know how to do this at the moment (since this is running in the JVM), but I will try to find out and report back! :slightly_smiling_face: 

### krakowski · 2021-02-26

@yosefe Does [`ucs_config_sscanf_time`](https://github.com/openucx/ucx/blob/01a08661bd8dcfe921afd25c16d7e25d90639599/src/ucs/config/parser.c#L415-L446) return `1` on success? If so, it doesn't seem to fail in my case. `rax` contains `1` on return.

![gdb](https://i.imgur.com/1lIhAVW.png)

(unfortunately I don't have debug informationen, so I had to look at the assembly)

### yosefe · 2021-02-26

@krakowski ucs_config_sscanf_time returns 1 on success. but it can be called several times. does it return 1 when the error shows up?
can you pls set UCX_LOG_LEVEL_TRIGGER=error and UCX_HANDLE_ERRORS=freeze env vars?
it would freeze the program when parser error happened, on `ucs_error("Invalid value for %s:...` in `ucs_config_parser_parse_field`
then, need to attach with gdb and print `*field`

### krakowski · 2021-02-26

@yosefe Yes, you are right. This was probably one of the other Memory Domains being processed.

I tried your suggestion which is working until the point when gdb attaches. After this I am stuck inside `ucs_debug_freeze` and can't seem to print `*field` (`No symbol "field" in current context.`). I think this is caused because I don't have debug symbols?

![gdb](https://i.imgur.com/OYOU7zI.png)

### yosefe · 2021-02-26

@krakowski need to to "thread apply all bt" and go to the thread which is calling ucs_config_parser_parse_field , and then go to relevant frame number by "frame N" (typically N would be 7 or so). The stack trace you've posted is from another Java thread which is also being stopped.


### krakowski · 2021-02-26

@yosefe Sorry, haven't used gdb in a while :smile: 

![gdb](https://i.imgur.com/MhJwGTn.png)

Unfortunately, I still can't print the parameter.

### yosefe · 2021-02-26

no debug symbols :(
i'd suggest rebuilding UCX SRC RPM from https://github.com/openucx/ucx/releases/tag/v1.9.0 ("Assets" section) and reinstalling it. And installing also the "-debuginfo" RPM.



### krakowski · 2021-02-26

I will get the debug symbols tomorrow and report back. Thanks for bearing with me! :) 

### krakowski · 2021-02-27

Got the debug symbols :)

![gdb](https://i.imgur.com/yAlWaf4.png)

I also set a breakpoint inside `ucs_config_sscanf_time` when `0.06ns` is parsed. The weird thing here is, that after the call to `sscanf` the variable `units` seems to have a wrong value.

```
>>> print units
$6 = ".0"
```

This is the state before calling `sscanf` whit `units` still having the old (correct) value.

![gdb](https://i.imgur.com/5SmHUgu.png)

After the call `units` is set to `.0`.

![gdb](https://i.imgur.com/mMEXR9J.png)

Also made sure that it is indeed `sscanf` from `libc` which is getting called.

```
0x0000150992eabdd0 in sscanf () from /lib64/libc.so.6
```

### krakowski · 2021-02-27

@yosefe Someone at the Project Panama mailing list pointed me in the right direction.

Seems this is caused by a wrong locale setting (when running from Java). Changing the system's locale to English solved the problem... Sorry for taking your time with such a stupid error :smile: 

### yosefe · 2021-02-28

great, thanks for the update!

### gsanchezgallegos · 2026-02-09

I had the same issue in a rocky linux 8.10 and UCX 1.18, but without running from Java. After running "export LANG=en_US.UTF-8" the error "UCX  ERROR Invalid value for MEM_REG_GROWTH" dissapeared. 
