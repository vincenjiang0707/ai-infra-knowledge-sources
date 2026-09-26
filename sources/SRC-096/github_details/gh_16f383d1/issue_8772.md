# [Issue #8772] Simultaneous connection requests fail from multiple clients to multiple servers

source: https://github.com/openucx/ucx/issues/8772
state: closed | updated: 2025-10-28T14:49:08Z
labels: Bug

## 正文

### Describe the bug
A clear and concise description of what the bug is.

I have a node with four IB interfaces. The goal is to have a UCP server for 
each. Each of these four servers should accept connection requests from 
any number of UCP clients.

I am having a problem with the connection requests occasionally getting
overwritten prior to their use in the server in creating an endpoint 
to the client.

That problem is due to the server connection handler, which can only
take a static function. I tried unsuccessfully to make the connection handler non-static.

I tried synchronizing the connection requests by taking a lock at the beginning of the 
connection handler and holding it until after creating the server's endpoint to the client.

The synchronization attempt did not make a difference in that the same 
connection request object was being used by two different servers (listeners).

The question, in general, is how to handle multiple simultaneous connection requests from
different clients by multiple servers (listeners).

Server connection handler prototype: 
   void static server_conn_handle_cb(ucp_conn_request_h  conn_request,
                                     void               *arg);
									 
ucs_status_t server_create_ep(const ucp_worker_h         data_worker,
                              const ucp_conn_request_h   conn_request,                        
                              ucp_ep_h                  *server_ep)
{
   ucp_ep_params_t ep_params;
   ucs_status_t    status = UCS_OK;

   // Server endpoint
   ep_params.field_mask      = UCP_EP_PARAM_FIELD_CONN_REQUEST;
   ep_params.conn_request    = conn_request;

   status = ucp_ep_create(data_worker, &ep_params, server_ep);	
   ...   
									 
Server's listener creation code snippet:
   params.field_mask         = UCP_LISTENER_PARAM_FIELD_SOCK_ADDR |
                               UCP_LISTENER_PARAM_FIELD_CONN_HANDLER;
   params.sockaddr.addr      = (const struct sockaddr*)&server_addr;
   params.sockaddr.addrlen   = sizeof(struct sockaddr);
   params.conn_handler.cb    = server_conn_handle_cb;
   params.conn_handler.arg   = nullptr;
   status = ucp_listener_create(ucp_worker, &params, &ucp_listener_);
   ...
   
Client's endpoint creation code snippet:
   ep_params.field_mask       =  UCP_EP_PARAM_FIELD_FLAGS       |
                                 UCP_EP_PARAM_FIELD_SOCK_ADDR   |
                                 UCP_EP_PARAM_FIELD_USER_DATA   |
                                 UCP_EP_PARAM_FIELD_ERR_HANDLER |
                                 UCP_EP_PARAM_FIELD_ERR_HANDLING_MODE;
   ep_params.err_mode         =  UCP_ERR_HANDLING_MODE_PEER;
   ep_params.err_handler.cb   =  client_err_cb;
   ep_params.err_handler.arg  =  nullptr;
   ep_params.user_data        =  nullptr;
   ep_params.flags            =  UCP_EP_PARAMS_FLAGS_CLIENT_SERVER |
                                 UCP_EP_PARAMS_FLAGS_NO_LOOPBACK   |
                                 UCP_EP_PARAMS_FLAGS_SEND_CLIENT_ID;
   ep_params.sockaddr.addr    = (struct sockaddr*) &connect_addr;
   ep_params.sockaddr.addrlen = sizeof(connect_addr);
   // client endpoint
   status = ucp_ep_create(ucp_worker, &ep_params, &ucp_client_ep);
   ...
   

### Steps to Reproduce
- Command line
- UCX version used (from github branch XX or release YY) + UCX configure flags (can be checked by `ucx_info -v`)

$ ucx_info -v
 Version 1.13.0
 Git branch '', revision 6765970
 Configured with: --disable-logging --disable-debug --disable-assertions --disable-params-check --with-rdmacm

- **Any UCX environment variables used**
UCX_LOGLEVEL=INFO

### Setup and versions
- OS version (e.g Linux distro) + CPU architecture (x86_64/aarch64/ppc64le/...)
   - `cat /etc/issue` or `cat /etc/redhat-release` + `uname -a`

$ cat /etc/redhat-release
Red Hat Enterprise Linux Server release 7.4 (Maipo)

$ uname -a
Linux dbfsparbe21 3.10.0-693.17.1.rt56.636.el7.x86_64 #1 SMP PREEMPT RT Tue Jan 16 16:25:18 UTC 2018 x86_64 x86_64 x86_64 GNU/Linux

   - For Nvidia Bluefield SmartNIC include `cat /etc/mlnx-release` (the string identifies software and firmware setup)
- For RDMA/IB/RoCE related issues:
    - Driver version:
        - `rpm -q rdma-core` or `rpm -q libibverbs`
$ rpm -q rdma-core
rdma-core-55mlnx37-1.55103.x86_64

$ rpm -q libibverbs
libibverbs-55mlnx37-1.55103.x86_64

        - or: MLNX_OFED version `ofed_info -s`
$ ofed_info -s
MLNX_OFED_LINUX-5.5-1.0.3.2:

   - HW information from `ibstat` or `ibv_devinfo -vv` command

$ ibstat
CA 'mlx5_0'
        CA type: MT4119
        Number of ports: 1
        Firmware version: 16.32.1010
        Hardware version: 0
        Node GUID: 0xec0d9a0300431464
        System image GUID: 0xec0d9a0300431464
        Port 1:
                State: Active
                Physical state: LinkUp
                Rate: 100
                Base lid: 44
                LMC: 0
                SM lid: 1
                Capability mask: 0x2651e848
                Port GUID: 0xec0d9a0300431464
                Link layer: InfiniBand
CA 'mlx5_1'
        CA type: MT4119
        Number of ports: 1
        Firmware version: 16.32.1010
        Hardware version: 0
        Node GUID: 0xec0d9a0300431465
        System image GUID: 0xec0d9a0300431464
        Port 1:
                State: Active
                Physical state: LinkUp
                Rate: 100
                Base lid: 105
                LMC: 0
                SM lid: 1
                Capability mask: 0x2651e848
                Port GUID: 0xec0d9a0300431465
                Link layer: InfiniBand
CA 'mlx5_2'
        CA type: MT4119
        Number of ports: 1
        Firmware version: 16.32.1010
        Hardware version: 0
        Node GUID: 0xec0d9a030043170c
        System image GUID: 0xec0d9a030043170c
        Port 1:
                State: Down
                Physical state: Disabled
                Rate: 10
                Base lid: 65535
                LMC: 0
                SM lid: 0
                Capability mask: 0x2651e848
                Port GUID: 0xec0d9a030043170c
                Link layer: InfiniBand
CA 'mlx5_3'
        CA type: MT4119
        Number of ports: 1
        Firmware version: 16.32.1010
        Hardware version: 0
        Node GUID: 0xec0d9a030043170d
        System image GUID: 0xec0d9a030043170c
        Port 1:
                State: Down
                Physical state: Disabled
                Rate: 10
                Base lid: 65535
                LMC: 0
                SM lid: 0
                Capability mask: 0x2651e848
                Port GUID: 0xec0d9a030043170d
                Link layer: InfiniBand


- For GPU related issues:
  - GPU type
  - Cuda: 
      - Drivers version
      - Check if peer-direct is loaded: `lsmod|grep nv_peer_mem` and/or gdrcopy: `lsmod|grep gdrdrv`

### Additional information (depending on the issue)
- OpenMPI version
- Output of `ucx_info -d` to show transports and devices recognized by UCX
`
$ ucx_info -d

Memory domain: self
     Component: self
             register: unlimited, cost: 0 nsec
           remote key: 0 bytes

      Transport: self
         Device: memory0
           Type: loopback
  System device: <unknown>

      capabilities:
            bandwidth: 0.00/ppn + 6911.00 MB/sec
              latency: 0 nsec
             overhead: 10 nsec
            put_short: <= 4294967295
            put_bcopy: unlimited
            get_bcopy: unlimited
             am_short: <= 8K
             am_bcopy: <= 8K
               domain: cpu
           atomic_add: 32, 64 bit
           atomic_and: 32, 64 bit
            atomic_or: 32, 64 bit
           atomic_xor: 32, 64 bit
          atomic_fadd: 32, 64 bit
          atomic_fand: 32, 64 bit
           atomic_for: 32, 64 bit
          atomic_fxor: 32, 64 bit
          atomic_swap: 32, 64 bit
         atomic_cswap: 32, 64 bit
           connection: to iface
      device priority: 0
     device num paths: 1
              max eps: inf
       device address: 0 bytes
        iface address: 8 bytes
       error handling: ep_check


 Memory domain: tcp
     Component: tcp
             register: unlimited, cost: 0 nsec
           remote key: 0 bytes

      Transport: tcp
         Device: lo
           Type: network
  System device: <unknown>

      capabilities:
            bandwidth: 11.91/ppn + 0.00 MB/sec
              latency: 10960 nsec
             overhead: 50000 nsec
            put_zcopy: <= 18446744073709551590, up to 6 iov
  put_opt_zcopy_align: <= 1
        put_align_mtu: <= 0
             am_short: <= 8K
             am_bcopy: <= 8K
             am_zcopy: <= 64K, up to 6 iov
   am_opt_zcopy_align: <= 1
         am_align_mtu: <= 0
            am header: <= 8037
           connection: to ep, to iface
      device priority: 1
     device num paths: 1
              max eps: 256
       device address: 18 bytes
        iface address: 2 bytes
           ep address: 10 bytes
       error handling: peer failure, ep_check, keepalive

      Transport: tcp
         Device: ib0
           Type: network
  System device: <unknown>

      capabilities:
            bandwidth: 11142.51/ppn + 0.00 MB/sec
              latency: 5206 nsec
             overhead: 50000 nsec
            put_zcopy: <= 18446744073709551590, up to 6 iov
  put_opt_zcopy_align: <= 1
        put_align_mtu: <= 0
             am_short: <= 8K
             am_bcopy: <= 8K
             am_zcopy: <= 64K, up to 6 iov
   am_opt_zcopy_align: <= 1
         am_align_mtu: <= 0
            am header: <= 8037
           connection: to ep, to iface
      device priority: 1
     device num paths: 1
              max eps: 256
       device address: 6 bytes
        iface address: 2 bytes
           ep address: 10 bytes
       error handling: peer failure, ep_check, keepalive

      Transport: tcp
         Device: ib1
           Type: network
  System device: <unknown>

      capabilities:
            bandwidth: 11142.51/ppn + 0.00 MB/sec
              latency: 5206 nsec
             overhead: 50000 nsec
            put_zcopy: <= 18446744073709551590, up to 6 iov
  put_opt_zcopy_align: <= 1
        put_align_mtu: <= 0
             am_short: <= 8K
             am_bcopy: <= 8K
             am_zcopy: <= 64K, up to 6 iov
   am_opt_zcopy_align: <= 1
         am_align_mtu: <= 0
            am header: <= 8037
           connection: to ep, to iface
      device priority: 1
     device num paths: 1
              max eps: 256
       device address: 6 bytes
        iface address: 2 bytes
           ep address: 10 bytes
       error handling: peer failure, ep_check, keepalive

      Transport: tcp
         Device: net0
           Type: network
  System device: <unknown>

      capabilities:
            bandwidth: 113.16/ppn + 0.00 MB/sec
              latency: 5776 nsec
             overhead: 50000 nsec
            put_zcopy: <= 18446744073709551590, up to 6 iov
  put_opt_zcopy_align: <= 1
        put_align_mtu: <= 0
             am_short: <= 8K
             am_bcopy: <= 8K
             am_zcopy: <= 64K, up to 6 iov
   am_opt_zcopy_align: <= 1
         am_align_mtu: <= 0
            am header: <= 8037
           connection: to ep, to iface
      device priority: 1
     device num paths: 1
              max eps: 256
       device address: 6 bytes
        iface address: 2 bytes
           ep address: 10 bytes
       error handling: peer failure, ep_check, keepalive


 Connection manager: tcp
      max_conn_priv: 2064 bytes

 Memory domain: sysv
     Component: sysv
             allocate: unlimited
           remote key: 12 bytes
           rkey_ptr is supported

      Transport: sysv
         Device: memory
           Type: intra-node
  System device: <unknown>

      capabilities:
            bandwidth: 0.00/ppn + 12179.00 MB/sec
              latency: 80 nsec
             overhead: 10 nsec
            put_short: <= 4294967295
            put_bcopy: unlimited
            get_bcopy: unlimited
             am_short: <= 100
             am_bcopy: <= 8256
               domain: cpu
           atomic_add: 32, 64 bit
           atomic_and: 32, 64 bit
            atomic_or: 32, 64 bit
           atomic_xor: 32, 64 bit
          atomic_fadd: 32, 64 bit
          atomic_fand: 32, 64 bit
           atomic_for: 32, 64 bit
          atomic_fxor: 32, 64 bit
          atomic_swap: 32, 64 bit
         atomic_cswap: 32, 64 bit
           connection: to iface
      device priority: 0
     device num paths: 1
              max eps: inf
       device address: 8 bytes
        iface address: 8 bytes
       error handling: ep_check


 Memory domain: posix
     Component: posix
             allocate: <= 98072212K
           remote key: 24 bytes
           rkey_ptr is supported

      Transport: posix
         Device: memory
           Type: intra-node
  System device: <unknown>

      capabilities:
            bandwidth: 0.00/ppn + 12179.00 MB/sec
              latency: 80 nsec
             overhead: 10 nsec
            put_short: <= 4294967295
            put_bcopy: unlimited
            get_bcopy: unlimited
             am_short: <= 100
             am_bcopy: <= 8256
               domain: cpu
           atomic_add: 32, 64 bit
           atomic_and: 32, 64 bit
            atomic_or: 32, 64 bit
           atomic_xor: 32, 64 bit
          atomic_fadd: 32, 64 bit
          atomic_fand: 32, 64 bit
           atomic_for: 32, 64 bit
          atomic_fxor: 32, 64 bit
          atomic_swap: 32, 64 bit
         atomic_cswap: 32, 64 bit
           connection: to iface
      device priority: 0
     device num paths: 1
              max eps: inf
       device address: 8 bytes
        iface address: 8 bytes
       error handling: ep_check


 Memory domain: mlx5_0
     Component: ib
             register: unlimited, cost: 180 nsec
           remote key: 8 bytes
           local memory handle is required for zcopy

      Transport: dc_mlx5
         Device: mlx5_0:1
           Type: network
  System device: mlx5_0 (0)

      capabilities:
            bandwidth: 11794.23/ppn + 0.00 MB/sec
              latency: 660 nsec
             overhead: 40 nsec
            put_short: <= 2K
            put_bcopy: <= 8256
            put_zcopy: <= 1G, up to 11 iov
  put_opt_zcopy_align: <= 512
        put_align_mtu: <= 4K
            get_bcopy: <= 8256
            get_zcopy: 65..1G, up to 11 iov
  get_opt_zcopy_align: <= 512
        get_align_mtu: <= 4K
             am_short: <= 2046
             am_bcopy: <= 8254
             am_zcopy: <= 8254, up to 3 iov
   am_opt_zcopy_align: <= 512
         am_align_mtu: <= 4K
            am header: <= 138
               domain: device
           atomic_add: 32, 64 bit
           atomic_and: 32, 64 bit
            atomic_or: 32, 64 bit
           atomic_xor: 32, 64 bit
          atomic_fadd: 32, 64 bit
          atomic_fand: 32, 64 bit
           atomic_for: 32, 64 bit
          atomic_fxor: 32, 64 bit
          atomic_swap: 32, 64 bit
         atomic_cswap: 32, 64 bit
           connection: to iface
      device priority: 38
     device num paths: 1
              max eps: inf
       device address: 3 bytes
        iface address: 5 bytes
       error handling: buffer (zcopy), remote access, peer failure, ep_check


      Transport: rc_verbs
         Device: mlx5_0:1
           Type: network
  System device: mlx5_0 (0)

      capabilities:
            bandwidth: 11794.23/ppn + 0.00 MB/sec
              latency: 600 + 1.000 * N nsec
             overhead: 75 nsec
            put_short: <= 124
            put_bcopy: <= 8256
            put_zcopy: <= 1G, up to 5 iov
  put_opt_zcopy_align: <= 512
        put_align_mtu: <= 4K
            get_bcopy: <= 8256
            get_zcopy: 65..1G, up to 5 iov
  get_opt_zcopy_align: <= 512
        get_align_mtu: <= 4K
             am_short: <= 123
             am_bcopy: <= 8255
             am_zcopy: <= 8255, up to 4 iov
   am_opt_zcopy_align: <= 512
         am_align_mtu: <= 4K
            am header: <= 127
               domain: device
           atomic_add: 64 bit
          atomic_fadd: 64 bit
         atomic_cswap: 64 bit
           connection: to ep
      device priority: 38
     device num paths: 1
              max eps: 256
       device address: 3 bytes
           ep address: 5 bytes
       error handling: peer failure, ep_check


      Transport: rc_mlx5
         Device: mlx5_0:1
           Type: network
  System device: mlx5_0 (0)

      capabilities:
            bandwidth: 11794.23/ppn + 0.00 MB/sec
              latency: 600 + 1.000 * N nsec
             overhead: 40 nsec
            put_short: <= 2K
            put_bcopy: <= 8256
            put_zcopy: <= 1G, up to 14 iov
  put_opt_zcopy_align: <= 512
        put_align_mtu: <= 4K
            get_bcopy: <= 8256
            get_zcopy: 65..1G, up to 14 iov
  get_opt_zcopy_align: <= 512
        get_align_mtu: <= 4K
             am_short: <= 2046
             am_bcopy: <= 8254
             am_zcopy: <= 8254, up to 3 iov
   am_opt_zcopy_align: <= 512
         am_align_mtu: <= 4K
            am header: <= 186
               domain: device
           atomic_add: 32, 64 bit
           atomic_and: 32, 64 bit
            atomic_or: 32, 64 bit
           atomic_xor: 32, 64 bit
          atomic_fadd: 32, 64 bit
          atomic_fand: 32, 64 bit
           atomic_for: 32, 64 bit
          atomic_fxor: 32, 64 bit
          atomic_swap: 32, 64 bit
         atomic_cswap: 32, 64 bit
           connection: to ep
      device priority: 38
     device num paths: 1
              max eps: 256
       device address: 3 bytes
           ep address: 7 bytes
       error handling: buffer (zcopy), remote access, peer failure, ep_check


      Transport: ud_verbs
         Device: mlx5_0:1
           Type: network
  System device: mlx5_0 (0)

      capabilities:
            bandwidth: 11794.23/ppn + 0.00 MB/sec
              latency: 630 nsec
             overhead: 105 nsec
             am_short: <= 116
             am_bcopy: <= 4088
             am_zcopy: <= 4088, up to 5 iov
   am_opt_zcopy_align: <= 512
         am_align_mtu: <= 4K
            am header: <= 3952
           connection: to ep, to iface
      device priority: 38
     device num paths: 1
              max eps: inf
       device address: 3 bytes
        iface address: 3 bytes
           ep address: 6 bytes
       error handling: peer failure, ep_check


      Transport: ud_mlx5
         Device: mlx5_0:1
           Type: network
  System device: mlx5_0 (0)

      capabilities:
            bandwidth: 11794.23/ppn + 0.00 MB/sec
              latency: 630 nsec
             overhead: 80 nsec
             am_short: <= 180
             am_bcopy: <= 4088
             am_zcopy: <= 4088, up to 3 iov
   am_opt_zcopy_align: <= 512
         am_align_mtu: <= 4K
            am header: <= 132
           connection: to ep, to iface
      device priority: 38
     device num paths: 1
              max eps: inf
       device address: 3 bytes
        iface address: 3 bytes
           ep address: 6 bytes
       error handling: peer failure, ep_check


 Memory domain: mlx5_1
     Component: ib
             register: unlimited, cost: 180 nsec
           remote key: 8 bytes
           local memory handle is required for zcopy

      Transport: dc_mlx5
         Device: mlx5_1:1
           Type: network
  System device: mlx5_1 (1)

      capabilities:
            bandwidth: 11794.23/ppn + 0.00 MB/sec
              latency: 660 nsec
             overhead: 40 nsec
            put_short: <= 2K
            put_bcopy: <= 8256
            put_zcopy: <= 1G, up to 11 iov
  put_opt_zcopy_align: <= 512
        put_align_mtu: <= 4K
            get_bcopy: <= 8256
            get_zcopy: 65..1G, up to 11 iov
  get_opt_zcopy_align: <= 512
        get_align_mtu: <= 4K
             am_short: <= 2046
             am_bcopy: <= 8254
             am_zcopy: <= 8254, up to 3 iov
   am_opt_zcopy_align: <= 512
         am_align_mtu: <= 4K
            am header: <= 138
               domain: device
           atomic_add: 32, 64 bit
           atomic_and: 32, 64 bit
            atomic_or: 32, 64 bit
           atomic_xor: 32, 64 bit
          atomic_fadd: 32, 64 bit
          atomic_fand: 32, 64 bit
           atomic_for: 32, 64 bit
          atomic_fxor: 32, 64 bit
          atomic_swap: 32, 64 bit
         atomic_cswap: 32, 64 bit
           connection: to iface
      device priority: 38
     device num paths: 1
              max eps: inf
       device address: 3 bytes
        iface address: 5 bytes
       error handling: buffer (zcopy), remote access, peer failure, ep_check


      Transport: rc_verbs
         Device: mlx5_1:1
           Type: network
  System device: mlx5_1 (1)

      capabilities:
            bandwidth: 11794.23/ppn + 0.00 MB/sec
              latency: 600 + 1.000 * N nsec
             overhead: 75 nsec
            put_short: <= 124
            put_bcopy: <= 8256
            put_zcopy: <= 1G, up to 5 iov
  put_opt_zcopy_align: <= 512
        put_align_mtu: <= 4K
            get_bcopy: <= 8256
            get_zcopy: 65..1G, up to 5 iov
  get_opt_zcopy_align: <= 512
        get_align_mtu: <= 4K
             am_short: <= 123
             am_bcopy: <= 8255
             am_zcopy: <= 8255, up to 4 iov
   am_opt_zcopy_align: <= 512
         am_align_mtu: <= 4K
            am header: <= 127
               domain: device
           atomic_add: 64 bit
          atomic_fadd: 64 bit
         atomic_cswap: 64 bit
           connection: to ep
      device priority: 38
     device num paths: 1
              max eps: 256
       device address: 3 bytes
           ep address: 5 bytes
       error handling: peer failure, ep_check


      Transport: rc_mlx5
         Device: mlx5_1:1
           Type: network
  System device: mlx5_1 (1)

      capabilities:
            bandwidth: 11794.23/ppn + 0.00 MB/sec
              latency: 600 + 1.000 * N nsec
             overhead: 40 nsec
            put_short: <= 2K
            put_bcopy: <= 8256
            put_zcopy: <= 1G, up to 14 iov
  put_opt_zcopy_align: <= 512
        put_align_mtu: <= 4K
            get_bcopy: <= 8256
            get_zcopy: 65..1G, up to 14 iov
  get_opt_zcopy_align: <= 512
        get_align_mtu: <= 4K
             am_short: <= 2046
             am_bcopy: <= 8254
             am_zcopy: <= 8254, up to 3 iov
   am_opt_zcopy_align: <= 512
         am_align_mtu: <= 4K
            am header: <= 186
               domain: device
           atomic_add: 32, 64 bit
           atomic_and: 32, 64 bit
            atomic_or: 32, 64 bit
           atomic_xor: 32, 64 bit
          atomic_fadd: 32, 64 bit
          atomic_fand: 32, 64 bit
           atomic_for: 32, 64 bit
          atomic_fxor: 32, 64 bit
          atomic_swap: 32, 64 bit
         atomic_cswap: 32, 64 bit
           connection: to ep
      device priority: 38
     device num paths: 1
              max eps: 256
       device address: 3 bytes
           ep address: 7 bytes
       error handling: buffer (zcopy), remote access, peer failure, ep_check


      Transport: ud_verbs
         Device: mlx5_1:1
           Type: network
  System device: mlx5_1 (1)

      capabilities:
            bandwidth: 11794.23/ppn + 0.00 MB/sec
              latency: 630 nsec
             overhead: 105 nsec
             am_short: <= 116
             am_bcopy: <= 4088
             am_zcopy: <= 4088, up to 5 iov
   am_opt_zcopy_align: <= 512
         am_align_mtu: <= 4K
            am header: <= 3952
           connection: to ep, to iface
      device priority: 38
     device num paths: 1
              max eps: inf
       device address: 3 bytes
        iface address: 3 bytes
           ep address: 6 bytes
       error handling: peer failure, ep_check


      Transport: ud_mlx5
         Device: mlx5_1:1
           Type: network
  System device: mlx5_1 (1)

      capabilities:
            bandwidth: 11794.23/ppn + 0.00 MB/sec
              latency: 630 nsec
             overhead: 80 nsec
             am_short: <= 180
             am_bcopy: <= 4088
             am_zcopy: <= 4088, up to 3 iov
   am_opt_zcopy_align: <= 512
         am_align_mtu: <= 4K
            am header: <= 132
           connection: to ep, to iface
      device priority: 38
     device num paths: 1
              max eps: inf
       device address: 3 bytes
        iface address: 3 bytes
           ep address: 6 bytes
       error handling: peer failure, ep_check


 Memory domain: mlx5_2
     Component: ib
             register: unlimited, cost: 180 nsec
           remote key: 8 bytes
           local memory handle is required for zcopy
   < no supported devices found >

 Memory domain: mlx5_3
     Component: ib
             register: unlimited, cost: 180 nsec
           remote key: 8 bytes
           local memory handle is required for zcopy
   < no supported devices found >

 Connection manager: rdmacm
      max_conn_priv: 54 bytes

 Memory domain: cma
     Component: cma
             register: unlimited, cost: 9 nsec

      Transport: cma
         Device: memory
           Type: intra-node
  System device: <unknown>

      capabilities:
            bandwidth: 0.00/ppn + 11145.00 MB/sec
              latency: 80 nsec
             overhead: 2000 nsec
            put_zcopy: unlimited, up to 16 iov
  put_opt_zcopy_align: <= 1
        put_align_mtu: <= 1
            get_zcopy: unlimited, up to 16 iov
  get_opt_zcopy_align: <= 1
        get_align_mtu: <= 1
           connection: to iface
      device priority: 0
     device num paths: 1
              max eps: inf
       device address: 8 bytes
        iface address: 4 bytes
       error handling: peer failure, ep_check


 Memory domain: knem
     Component: knem
             register: unlimited, cost: 180 nsec
           remote key: 16 bytes

      Transport: knem
         Device: memory
           Type: intra-node
  System device: <unknown>

      capabilities:
            bandwidth: 13862.00/ppn + 0.00 MB/sec
              latency: 80 nsec
             overhead: 2000 nsec
            put_zcopy: unlimited, up to 16 iov
  put_opt_zcopy_align: <= 1
        put_align_mtu: <= 1
            get_zcopy: unlimited, up to 16 iov
  get_opt_zcopy_align: <= 1
        get_align_mtu: <= 1
           connection: to iface
      device priority: 0
     device num paths: 1
              max eps: inf
       device address: 8 bytes
        iface address: 0 bytes
       error handling: none

`
- Configure result - config.log
- 
 Configured with: --disable-logging --disable-debug --disable-assertions --disable-params-check --with-rdmacm

- Log file - configure UCX with "--enable-logging" - and run with "UCX_LOG_LEVEL=data"

Currently, we have an installation that is configured with --disable-logging
If necessary to resolve this, we may able to configure with --enable-logging




## 评论 (3)

### yosefe · 2022-12-20

@rrgargeya can you pls share the code of server_conn_handle_cb?

### rrgargeya · 2023-01-05

> @rrgargeya can you pls share the code of server_conn_handle_cb?

void
UCP::SERVER_THREAD_CT::server_conn_handle_cb(ucp_conn_request_h  conn_request,
                       			                                          void               * /* arg */)
{
   ucp_conn_request_attr_t attr;
   ucs_status_t status;

   ::UCP::SERVER_THREAD_CT::server_ctx.conn_request = conn_request;

   attr.field_mask = UCP_CONN_REQUEST_ATTR_FIELD_CLIENT_ADDR;
   status = ucp_conn_request_query(conn_request, &attr);
   if (status != UCS_OK) {
      // log: "failed to query the connection request, status: " << ucs_status_string(status)
      return;
   }

   if (!::UCP::SERVER_THREAD_CT::client_connected_) {
      ::UCP::SERVER_THREAD_CT::client_connected_ = true;
   }
}

### yosefe · 2023-01-07

@rrgargeya you should not override the global connection request `::UCP::SERVER_THREAD_CT::server_ctx.conn_request` when new connection arrives. Probably should associate the connection request with a context passed in "arg" parameter, and allocate a separate context for each listener, or have a list of connection requests. 
