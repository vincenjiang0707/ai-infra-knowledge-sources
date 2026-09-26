# [Issue #5611] Help with UCX and Intel/GNU Backtrace

source: https://github.com/openucx/ucx/issues/5611
state: open | updated: 2026-04-14T02:12:01Z
labels: 

## 正文

All,

This is a bit of an open-ended issue as I'm looking for advice. Namely, I have an issue open with Intel (currently internal, though here is the [original Forum Post](https://community.intel.com/t5/Intel-Fortran-Compiler/Change-in-Traceback-Output-in-Recent-Intel-Fortran/td-p/1184875)) where even if you compile a small program with ifort/Intel MPI that has an overflow with just a hint of MPI:
```fortran
program ovf

   use MPI

   real*4 x(5),y(5)
   integer*4 i

   call MPI_Init(i)
   call MPI_Finalize(i)

   x(1) = -1e32
   x(2) = 1e38
   x(3) = 1e38
   x(4) = 1e38
   x(5) = -36.0
   do i=1,5
      y(i) = 100.0*(x(i))
      print *, 'x = ', x(i), ' x*100.0 = ',y(i)
   end do
end
```
it changes the traceback from the Intel format to the GNU format. After quite a few backs-and-forth with Intel, it was found that the issue is due to the presence of `libmlx.so` in the `FI_PROVIDER_PATH`. Remove it, and you get Intel traceback, but have it around and you get GNU traceback. (And the engineer I guess are suggesting libmlx has ucx underneath?)

Now, in the end, much of this is beyond UCX, but the MPI engineers suggested a few things:

> If the loading of libucs is the issue on OPA cluster, then the option is to copy $IMPI_ROOT/intel64/libfabric/lib/prov/libpsmx2-fi.so and set FI_PROVIDER_PATH to the folder where the copy would reside (on shared folder).

This led to the experiment with `FI_PROVIDER_PATH`. The engineers then added:

One of the ideas from development was:

> Getting UCX sources (it is open source), removing all related backtrace functions and rebuilding it ($HPCX_UCX_DIR/bin/ucx_info -v provides configure options). I know that it sounds not convenient at all... But I haven't found better workaround yet. 
> 
> Maybe creating an issue on UCX github page to add that feature could be a good idea?

Now, I have never built UCX, so I'm not exactly sure what they are suggesting. But, I figured I'd ask here because while I see this issue with Intel Fortran/Intel MPI, I have a colleague at Harvard who is seeing the same thing with Intel Fortran/Open MPI! So he avoids Intel MPI, but he did say:

> > Perhaps you can build UCX with a complete Intel stack? icc, icpc, etc.? Maybe then GNU can't infect it?
>
> That’s the scary thing – I did exactly that! My UCX build is floor-to-ceiling Intel. But we are well past the point of my understanding..

So while I might be in the weeds, I wondered if I might help him (and, perhaps, help Intel if we can help him). To wit, is there a way he can build UCX such that GNU doesn't have a chance to infect the traceback? I tried looking at [the wiki](https://github.com/openucx/ucx/wiki/OpenMPI-and-OpenSHMEM-installation-with-UCX) and saw:

> NOTE: For best performance configuration, use `../contrib/configure-release.`
> This will strip all debugging and profiling code.

Would building with `configure-release` perhaps avoid any backtrace functions as the engineer suggested?

## 评论 (21)

### yosefe · 2020-08-24

@mathomp4 pls try to set env var: `UCX_HANDLE_ERRORS=none`

### mathomp4 · 2020-08-24

> UCX_HANDLE_ERRORS=none

@yosefe Would that be a runtime flag? Or configure/build for UCX? It doesn't seem to work at runtime for me. To wit, without `UCX_HANDLE_ERRORS`:

```
$ mpiifort -g -traceback -fpe0 -o ovf_with_MPI.x ovf_with_MPI.F90

$ mpirun -np 1 ./ovf_with_MPI.x
srun: cluster configuration lacks support for cpu binding
 x =  -1.0000000E+32  x*100.0 =  -1.0000000E+34
[borgd130:67780:0:67780] Caught signal 8 (Floating point exception: floating-point overflow)
==== backtrace ====
    0  /usr/lib64/libucs.so.0(+0x1935c) [0x2aaab163935c]
    1  /usr/lib64/libucs.so.0(+0x19613) [0x2aaab1639613]
    2  ./ovf_with_MPI.x() [0x402e2b]
    3  ./ovf_with_MPI.x() [0x402d22]
    4  /lib64/libc.so.6(__libc_start_main+0xf5) [0x2aaaacbf0725]
    5  ./ovf_with_MPI.x() [0x402c29]
===================
```
With `UCX_HANDLE_ERRORS=none`:
```
$ UCX_HANDLE_ERRORS=none mpirun -np 1 ./ovf_with_MPI.x
srun: cluster configuration lacks support for cpu binding
 x =  -1.0000000E+32  x*100.0 =  -1.0000000E+34
[borgd130:67826:0:67826] Caught signal 8 (Floating point exception: floating-point overflow)
==== backtrace ====
    0  /usr/lib64/libucs.so.0(+0x1935c) [0x2aaab163935c]
    1  /usr/lib64/libucs.so.0(+0x19613) [0x2aaab1639613]
    2  ./ovf_with_MPI.x() [0x402e2b]
    3  ./ovf_with_MPI.x() [0x402d22]
    4  /lib64/libc.so.6(__libc_start_main+0xf5) [0x2aaaacbf0725]
    5  ./ovf_with_MPI.x() [0x402c29]
===================
```

For reference this is the "expected" traceback:
```
$ mpirun -np 1 ./ovf_with_MPI.x
srun: cluster configuration lacks support for cpu binding
 x =  -1.0000000E+32  x*100.0 =  -1.0000000E+34
forrtl: error (72): floating overflow
Image              PC                Routine            Line        Source
ovf_with_MPI.x     0000000000403E4B  Unknown               Unknown  Unknown
libpthread-2.22.s  00002AAAAC6C6C10  Unknown               Unknown  Unknown
ovf_with_MPI.x     0000000000402E2B  MAIN__                     17  ovf_with_MPI.F90
ovf_with_MPI.x     0000000000402D22  Unknown               Unknown  Unknown
libc-2.22.so       00002AAAACBF0725  __libc_start_main     Unknown  Unknown
ovf_with_MPI.x     0000000000402C29  Unknown               Unknown  Unknown
```

### yosefe · 2020-08-24

@mathomp4 this seems the correct usage. What is the UCX version (ucx_info -v)?

### mathomp4 · 2020-08-24

@yosefe looks to be 1.6.0. 

Note: the tests above you see are on an Omnipath system using Intel MPI and the PSM2 provider.

### mathomp4 · 2020-08-24

@yosefe I've also ask my Harvard colleague to try it out on his Intel Fortran/Open MPI system. It might do something for him!

### mathomp4 · 2020-08-24

@yosefe I asked my colleague (@sdeastham) to try `UCX_HANDLE_ERRORS=none` on his Intel Fortran/Open MPI system as well, but no help there either sadly.

(Though I went back and determined that I expressly don't build Open MPI with UCX on my Omnipath system because of #750. Which probably tells me I keep my `configure` lines for Open MPI the same for perhaps too long as that was from 2016!) 

### sdeastham · 2020-08-24

Hi all - as described by @mathomp4, I'm getting this issue, and unfortunately UCX_HANDLE_ERRORS did not resolve it. Versions: UCT version 1.6.1, Intel fortran/C/C++ 19.0.5.281, and OpenMPI v4.0.2.

### yosefe · 2020-08-24

Is it possible to test a newer version of UCX? There were some related to this flag

### mathomp4 · 2020-08-24

@yosefe More info including...a new oddity. So, I decided, what the heck, I can build UCX and so I do, 1.8.1. And if I load the module which exposes that to my path I get:
```
$ mpirun -np 1 ./ovf_with_MPI.x
srun: cluster configuration lacks support for cpu binding
 x =  -1.0000000E+32  x*100.0 =  -1.0000000E+34
[borgd130:151176:0:151176] Caught signal 8 (Floating point exception: floating-point overflow)
==== backtrace (tid: 151176) ====
 0  /discover/swdev/gmao_SIteam/other/SLES12.3/ucx/1.8.1/lib/libucs.so.0(ucs_handle_error+0x19c) [0x2aaab169cabc]
 1  /discover/swdev/gmao_SIteam/other/SLES12.3/ucx/1.8.1/lib/libucs.so.0(+0x26dec) [0x2aaab169cdec]
 2  /discover/swdev/gmao_SIteam/other/SLES12.3/ucx/1.8.1/lib/libucs.so.0(+0x27173) [0x2aaab169d173]
 3  ./ovf_with_MPI.x() [0x402e2b]
 4  ./ovf_with_MPI.x() [0x402d22]
 5  /lib64/libc.so.6(__libc_start_main+0xf5) [0x2aaaacbf0725]
 6  ./ovf_with_MPI.x() [0x402c29]
=================================
forrtl: error (75): floating point exception
Image              PC                Routine            Line        Source
ovf_with_MPI.x     0000000000403E4B  Unknown               Unknown  Unknown
libpthread-2.22.s  00002AAAAC6C6C10  Unknown               Unknown  Unknown
ovf_with_MPI.x     0000000000402E2B  MAIN__                     17  ovf_with_MPI.F90
ovf_with_MPI.x     0000000000402D22  Unknown               Unknown  Unknown
libc-2.22.so       00002AAAACBF0725  __libc_start_main     Unknown  Unknown
ovf_with_MPI.x     0000000000402C29  Unknown               Unknown  Unknown
```
So...two tracebacks for the price of one! Again not ideal, but might point to something. It does perhaps presage hope for @sdeastham, but not a perfect fix for my case.

I'll try and contact our sysadmins and see if we can find a spare node to try updating the system level UCX and see if perhaps what we are seeing is a UCX bug in disguise. And the reason Intel didn't see is was they had a newer version?

### mathomp4 · 2020-08-24

Did a few more tests. I decided to build and install UCX 1.6.0, 1.6.1, and 1.7.0 along with my 1.8.1. 

If I have 1.6.0 or 1.6.1 loaded, I get the GNU traceback only. With 1.7.0 (and 1.8.1), I get the double traceback. So perhaps there was a "fix" or something in 1.7.0 regarding tracebacks?


### sdeastham · 2020-08-24

I can confirm this behavior - excellent news for me! I'm going to try building a larger case and double-check that this means I still get "full" tracebacks.

### yosefe · 2020-08-24

@mathomp4 can you pls try UCX v1.8.0 along with `UCX_HANDLE_ERRORS=none`?

### mathomp4 · 2020-08-25

@yosefe Sadly, no change:
```
$ ucx_info -v
# UCT version=1.8.0 revision c30b7da
# configured with: --prefix=/discover/swdev/gmao_SIteam/other/SLES12.3/ucx/1.8.0

$ UCX_HANDLE_ERRORS=none mpirun -np 1 ./ovf_with_MPI.x
srun: cluster configuration lacks support for cpu binding
 x =  -1.0000000E+32  x*100.0 =  -1.0000000E+34
[borge038:199502:0:199502] Caught signal 8 (Floating point exception: floating-point overflow)
==== backtrace (tid: 199502) ====
 0  /discover/swdev/gmao_SIteam/other/SLES12.3/ucx/1.8.0/lib/libucs.so.0(ucs_handle_error+0x19c) [0x2aaab169cabc]
 1  /discover/swdev/gmao_SIteam/other/SLES12.3/ucx/1.8.0/lib/libucs.so.0(+0x26dec) [0x2aaab169cdec]
 2  /discover/swdev/gmao_SIteam/other/SLES12.3/ucx/1.8.0/lib/libucs.so.0(+0x27173) [0x2aaab169d173]
 3  ./ovf_with_MPI.x() [0x402e2b]
 4  ./ovf_with_MPI.x() [0x402d22]
 5  /lib64/libc.so.6(__libc_start_main+0xf5) [0x2aaaacbf0725]
 6  ./ovf_with_MPI.x() [0x402c29]
=================================
forrtl: error (75): floating point exception
Image              PC                Routine            Line        Source
ovf_with_MPI.x     0000000000403E4B  Unknown               Unknown  Unknown
libpthread-2.22.s  00002AAAAC6C6C10  Unknown               Unknown  Unknown
ovf_with_MPI.x     0000000000402E2B  MAIN__                     17  ovf_with_MPI.F90
ovf_with_MPI.x     0000000000402D22  Unknown               Unknown  Unknown
libc-2.22.so       00002AAAACBF0725  __libc_start_main     Unknown  Unknown
ovf_with_MPI.x     0000000000402C29  Unknown               Unknown  Unknown

===================================================================================
=   BAD TERMINATION OF ONE OF YOUR APPLICATION PROCESSES
=   RANK 0 PID 199502 RUNNING AT borge038
=   KILLED BY SIGNAL: 6 (Aborted)
===================================================================================
```

### phil-blain · 2021-10-14

Hi, just a small datapoint, but I  have a different behaviour than @mathomp4  gets:
~~~shell
$ ucx_info -v | \grep version
# UCT version=1.8.0 revision c0a9704
$ mpirun --version
Intel(R) MPI Library for Linux* OS, Version 2021.3 Build 20210601 (id: 6f90181f1)
Copyright 2003-2021, Intel Corporation.
$ mpiifort --version
ifort (IFORT) 2021.3.0 20210609
Copyright (C) 1985-2021 Intel Corporation.  All rights reserved.
~~~~

Just like @mathomp4, I get *both* backtraces, with either of 
- `mpirun ...`
-  `UCX_HANDLE_ERRORS=none mpirun ...` 
-  `mpirun -genv UCX_HANDLE_ERRORS none ...`. 

But, the GNU backtrace does have subroutine and file information: 
~~~
[<redacted node info>] Caught signal 8 (Floating point exception: floating-point invalid operation)
==== backtrace (tid:2429260) ====
 0 0x00000000000532f9 ucs_debug_print_backtrace()  ???:0
 1 0x0000000000012b20 .annobin_sigaction.c()  sigaction.c:0
 2 0x00000000011c7411 ice_init_column_mp_init_shortwave_()  /<redacted>/code/cice3/cicecore/shared/ice_init_column.F90:433
 3 0x0000000000405992 cice_initmod_mp_cice_init_()  /<redacted>/code/cice3/cicecore/drivers/standalone/cice/CICE_InitMod.F90:220
 4 0x0000000000403f93 cice_initmod_mp_cice_initialize_()  /<redacted>/code/cice3/cicecore/drivers/standalone/cice/CICE_InitMod.F90:52
 5 0x0000000000403c21 MAIN__()  /<redacted>/code/cice3/cicecore/drivers/standalone/cice/CICE.F90:43
 6 0x0000000000403ba2 main()  ???:0
 7 0x0000000000023493 __libc_start_main()  ???:0
 8 0x0000000000403aae _start()  ???:0
=================================
forrtl: error (75): floating point exception
Image              PC                Routine            Line        Source             
cice               0000000001A3016B  Unknown               Unknown  Unknown
libpthread-2.28.s  00007FA3E16F6B20  Unknown               Unknown  Unknown
cice               00000000011C7411  ice_init_column_m         433  ice_init_column.F90
cice               0000000000405992  cice_initmod_mp_c         220  CICE_InitMod.F90
cice               0000000000403F93  cice_initmod_mp_c          52  CICE_InitMod.F90
cice               0000000000403C21  MAIN__                     43  CICE.F90
cice               0000000000403BA2  Unknown               Unknown  Unknown
libc-2.28.so       00007FA3E0FC0493  __libc_start_main     Unknown  Unknown
cice               0000000000403AAE  Unknown               Unknown  Unknown

### yosefe · 2021-10-14

@phil-blain can you try `UCX_HANDLE_ERRORS=""` (empty string)?
UCX_HANDLE_ERRORS=none was fixed by https://github.com/openucx/ucx/pull/6624/commits/5ea95780987e87a7af9053f9ec4a6feee81331c2 for UCX v1.11

### phil-blain · 2021-10-14

With `UCX_HANDLE_ERRORS="" mpirun ...` or `mpirun -genv UCX_HANDLE_ERRORS "" ....`, I confirm I get only the Intel traceback. 

I have to say I think prefer the GNU traceback now since I get the full subroutine name and the full path to the source file, with `:line` syntax :P

Any idea why I would get this info in the GNU traceback but not @mathomp4 ? One thing I notice is that my glibc is more recent (2.28 vs 2.22)...

FWIW this is the full output from `uxc_info` (installed with the system package manager on RHEL 8.2):
~~~
# configured with: --build=x86_64-redhat-linux-gnu --host=x86_64-redhat-linux-gnu --program-prefix= 
--disable-dependency-tracking --prefix=/usr --exec-prefix=/usr --bindir=/usr/bin --sbindir=/usr/sbin 
--sysconfdir=/etc --datadir=/usr/share --includedir=/usr/include --libdir=/usr/lib64 --libexecdir=/usr/libexec 
--localstatedir=/var --sharedstatedir=/var/lib --mandir=/usr/share/man --infodir=/usr/share/info 
--disable-optimizations --disable-logging --disable-debug --disable-assertions --enable-mt 
--disable-params-check --enable-cma --with-cuda --without-gdrcopy --with-verbs --with-cm 
--with-knem --with-rdmacm --without-rocm --without-xpmem --without-ugni --without-java 
--with-cuda=/usr/local/cuda-10.2
~~~

### yosefe · 2021-10-14

The GNU traceback is coming from UCX. The second traceback is coming from (AFAIK) Fortran runtime library

### phil-blain · 2021-10-15

Yes, I understand that now. In fact, I had a look at the code, and I understand that the traceback generated by UCX will have detailed information (line number, source file, function name) only if `HAVE_DETAILED_BACKTRACE` is defined at compilation. This is set by autoconf based on availability of symbols found in package `binutils-devel`, from what I could grasp. 

I checked that my version of UCX was indeed compiled with detailed backtrace support:
~~~shell
$ ucx_info -v -b |\grep -e DETAILED -e version
# UCT version=1.8.0 revision c0a9704
#define HAVE_DETAILED_BACKTRACE   1
~~~

I also checked on another older system that shows the same symptoms as @mathomp4 describes (i.e. only non-detailed UCX backtrace):
~~~shell
$ ucx_info -v -b |\grep -e DETAILED -e version
# UCT version=1.6.0 revision 818ad89  
$ mpirun --version
mpirun (Open MPI) 3.1.2
$ mpif90 --version
ifort (IFORT) 19.0.3.199 20190206
Copyright (C) 1985-2019 Intel Corporation.  All rights reserved.
~~~
On this system, I get _only_ a non-detailed UCX backtrace by default, and _only_ an Intel Fortran backtrace if I set  `UCX_HANDLE_ERRORS=""` in the environmment.

So I guess the only remaining question is:

- Why did UCX "hijack" the backtrace by default in older UCX versions (circa v1.6.0) so that the Intel Fortan was not shown at all unless using `UCX_HANDLE_ERRORS=""`  ? (this changed starting in in 1.7 according to @mathomp4'S testing since  *both* backtraces are shown by default)

### yosefe · 2021-10-16

> * Why did UCX "hijack" the backtrace by default in older UCX versions (circa v1.6.0) so that the Intel Fortan was not shown at all unless using `UCX_HANDLE_ERRORS=""`  ? (this changed starting in in 1.7 according to @mathomp4'S testing since  _both_ backtraces are shown by default)

At the time, the error handler in UCX did not save and call the previously installed error handler (such as the one from Fortran runtime library)

### bangerth · 2026-04-14

Since this has been open for a while now, it's probably worth saving others the time of searching: The underlying issue, I believe, is that MPI during initialization reads some XML file during which libxml calls libucs functionality that causes the floating point exception:
https://stackoverflow.com/questions/79739650/libxml2-throws-sigfpe-in-debian-13
That's unfortunate: people may have set floating point exceptions for good reasons at program start before they initialize MPI. UCX shouldn't perform invalid floating point operations without clearing FP exception flags.

For reference, the backtrace I have in a program of mine that (I assume) corresponds to the one here is this:
```
==== backtrace (tid: 254025) ====
 0  /lib/x86_64-linux-gnu/libucs.so.0(ucs_handle_error+0x2ec) [0x72f8e4ec8f2c]
 1  /lib/x86_64-linux-gnu/libucs.so.0(+0x3530d) [0x72f8e4eca30d]
 2  /lib/x86_64-linux-gnu/libucs.so.0(+0x3572a) [0x72f8e4eca72a]
 3  /lib/x86_64-linux-gnu/libc.so.6(+0x458d0) [0x72f8edc458d0]
 4  /lib/x86_64-linux-gnu/libxml2.so.2(+0x61d73) [0x72f8db7e1d73]
 5  /lib/x86_64-linux-gnu/libxml2.so.2(xmlCheckVersion+0x26) [0x72f8db7b9256]
 6  /usr/lib/x86_64-linux-gnu/hwloc/hwloc_xml_libxml.so(+0x2feb) [0x72f8dc440feb]
 7  /lib/x86_64-linux-gnu/libhwloc.so.15(+0x3cd05) [0x72f8e75ccd05]
 8  /lib/x86_64-linux-gnu/libhwloc.so.15(+0x1f74f) [0x72f8e75af74f]
 9  /lib/x86_64-linux-gnu/libpmix.so.2(+0x4cc4b) [0x72f8e184cc4b]
10  /lib/x86_64-linux-gnu/libpmix.so.2(pmix_hwloc_setup_topology+0x3fc) [0x72f8e184d36c]
11  /lib/x86_64-linux-gnu/libpmix.so.2(PMIx_Init+0x2343) [0x72f8e18579c3]
12  /lib/x86_64-linux-gnu/libmpi.so.40(ompi_rte_init+0x1155) [0x72f8ee48fd45]
13  /lib/x86_64-linux-gnu/libmpi.so.40(+0x94010) [0x72f8ee494010]
14  /lib/x86_64-linux-gnu/libmpi.so.40(ompi_mpi_instance_init+0x6c) [0x72f8ee494ddc]
15  /lib/x86_64-linux-gnu/libmpi.so.40(ompi_mpi_init+0x80) [0x72f8ee48be30]
16  /lib/x86_64-linux-gnu/libmpi.so.40(PMPI_Init_thread+0x56) [0x72f8ee4be0d6]
17  /home/bangerth/p/deal.II/1/build/lib/libdeal_II.g.so.9.8.0-pre(_ZN6dealii12InitFinalizeC2ERiRPPcRKNS_17InitializeLibraryEj+0x378) [0x72f91a0fd304]
```

### bangerth · 2026-04-14

See also https://github.com/dealii/dealii/pull/19518
