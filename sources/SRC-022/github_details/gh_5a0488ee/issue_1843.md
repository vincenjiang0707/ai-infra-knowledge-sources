# [Issue #1843] [Issue]: RCCL building logs are broken

source: https://github.com/ROCm/rccl/issues/1843
state: closed | updated: 2025-08-26T14:12:37Z
labels: 

## 正文

### Problem Description

When running RCCL builds
./install.sh --local_gpu_only --disable-colltrace --disable-msccl-kernel --disable-mscclpp --dependencies, 
part of the output logs are broken, which caused developers hard to capture the actual errors. 

Part of the logs from the output
"
/data/users/ycui1984/fbsource/third-party/ossrccl/mytest/rccl/build/release/hipify/src/device/prims_ll.h:152:14: warning: unused variable 'data1' [-Wunused-variable]
  152 |     uint32_   t90  | da ta 1,  f la g1 ,  da ta2b, aflragr2i;er
_g      e| ne             ^~~~~
ric(__thread/data/users/ycui1984/fbsource/third-party/ossrccl/mytest/rccl/build/release/hipify/src/device/prims_ll.hf:e152nc:e21():,  warning: nwunused variable 'flag1' [-Wunused-variable]o
rkers, barrier_n  ex152tIn file included from  | ,/data/users/ycui1984/fbsource/third-party/ossrccl/mytest/rccl/build/release/hipify/gensrc/all_gather_sum_i8.cpp :  b2a:
rIn file included from r i/data/users/ycui1984/fbsource/third-party/ossrccl/mytest/rccl/build/release/hipify/src/device/all_gather.he:r11s ):
;uIn file included from 
      i| n        ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~t/data/users/ycui1984/fbsource/third-party/ossrccl/mytest/rccl/build/release/hipify/src/device/primitives.h
3:2189_t:
 d/data/users/ycui1984/fbsource/third-party/ossrccl/mytest/rccl/build/release/hipify/src/device/primitives.h/data/users/ycui1984/fbsource/third-party/ossrccl/mytest/rccl/build/release/hipify/src/device/prims_ll.ha:t:23a152:115,::14In file included from   :note: /data/users/ycui1984/fbsource/third-party/ossrccl/mytest/rccl/build/release/hipify/gensrc/all_reduce_premulsum_u32.cppf lIn file included from warning: expanded from macro 'barrier_generic':
a/data/users/ycui1984/fbsource/third-party/ossrccl/mytest/rccl/build/release/hipify/gensrc/all_reduce_minmax_u32.cppunused variable 'data1' [-Wunused-variable]2In file included from :
g
1:,    /data/users/ycui1984/fbsource/third-party/ossrccl/mytest/rccl/build/release/hipify/gensrc/all_reduce_minmax_u8.cppIn file included from 223d:
aIn file included from t/data/users/ycui1984/fbsource/third-party/ossrccl/mytest/rccl/build/release/hipify/src/device/all_reduce.h::2  /data/users/ycui1984/fbsource/third-party/ossrccl/mytest/rccl/build/release/hipify/src/device/all_reduce.h | :a1111:
:
152    const |     uin2:
In file included from  i/data/users/ycui1984/fbsource/third-party/ossrccl/mytest/rccl/build/release/hipify/src/device/primitives.ht,In file included from n:3 /data/users/ycui1984/fbsource/third-party/ossrccl/mytest/rccl/build/release/hipify/src/device/primitives.ht:1892f 188:
:
wl_at/data/users/ycui1984/fbsource/third-party/ossrccl/mytest/rccl/build/release/hipify/src/device/prims_ll.h/data/users/ycui1984/fbsource/third-party/ossrccl/mytest/rccl/build/release/hipify/src/device/prims_simple.h =g  t::1522:;14dha88
::r t      9| ewarning: a:                    ^~~~~aunused variable 'data1' [-Wunused-variable]1 ,
 d
Iwarning: dfxl.unused variable 'w' [-Wunused-variable]/data/users/ycui1984/fbsource/third-party/ossrccl/mytest/rccl/build/release/hipify/src/device/prims_ll.haxg
1  :/,W152A152R P | _ : d S I28autZ:    i88n | a E warning: tunused variable 'data2' [-Wunused-variable]3
22_;   ,t   \
  In file included from 152       /data/users/ycui1984/fbsource/third-party/ossrccl/mytest/rccl/build/release/hipify/src/device/all_reduce.hf:lda | g | 11a 2               ^t:
 ;b
a      
aIn file included from /data/users/ycui1984/fbsource/third-party/ossrccl/mytest/rccl/build/release/hipify/src/device/primitives.h : ru| i1189r,i             ^~~~~e
rn:
 _t/data/users/ycui1984/fbsource/third-party/ossrccl/mytest/rccl/build/release/hipify/src/device/prims_ll.h/data/users/ycui1984/fbsource/third-party/ossrccl/mytest/rccl/build/release/hipify/src/device/prims_ll.hfge3n2e_::152lrt152::21aig 114::cd(a,t a  _d1warning: warning: a_t,unused variable 'data1' [-Wunused-variable]unused variable 'flag1' [-Wunused-variable]ta 

2hf,r  e152 l  a152 |  | falda      gfge u 12nuin,t ;ci3d
ae_tn2a      2b,l t_f3l2| o             ^~~~~ta_gc
k td2 (dat;/data/users/ycui1984/fbsource/third-party/ossrccl/mytest/rccl/build/release/hipify/src/device/prims_ll.h):aa
,1521t,a       | :                           ^~~~~ 1fn21
l, w:afgo/data/users/ycui1984/fbsource/third-party/ossrccl/mytest/rccl/build/release/hipify/src/device/prims_ll.hr k1l:warning: ,er adg152unused variable 'flag1' [-Wunused-variable]:
35s:1, data  a,  2152,tbaawarning:  | unused variable 'flag2' [-Wunused-variable] 
2,r flr    aigf2l152 e;ag2 | ; ru
        
 _i|                    ^~~~~|  nn
                    ^~~~~uetx
i3t/data/users/ycui1984/fbsource/third-party/ossrccl/mytest/rccl/build/release/hipify/src/device/prims_ll.hn/data/users/ycui1984/fbsource/third-party/ossrccl/mytest/rccl/build/release/hipify/src/device/prims_ll.ht2,:: 3_152152:b2atr:2128_: r:t  warning: warning: dia unused variable 'flag1' [-Wunused-variable]unused variable 'data2' [-Wunused-variable]edt
a
ra1  st,  152152 | )a  |    ;1,
f     uu       liintfl3| 2a_na        ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~gttg1
13 ,,2dat /data/users/ycui1984/fbsource/third-party/ossrccl/mytest/rccl/build/release/hipify/src/device/primitives.h :_atd dd23:a1taaa15t:,  t1,anote: fa2 ,expanded from macro 'barrier_generic'l2,f  
falgfl1ala   g23,g1a,2 |  dga t; 
2      ;daa2 In file included from  /data/users/ycui1984/fbsource/third-party/ossrccl/mytest/rccl/build/release/hipify/gensrc/all_reduce_minmax_u32.cpp| 
                    ^~~~~      ,t  :
2| afc:
                                  ^~~~~In file included from 2l/data/users/ycui1984/fbsource/third-party/ossrccl/mytest/rccl/build/release/hipify/src/device/prims_ll.hon:s152
:/data/users/ycui1984/fbsource/third-party/ossrccl/mytest/rccl/build/release/hipify/src/device/all_reduce.h28,at: :i gf11 ntl2a:
 In file included from warning: g;2w/data/users/ycui1984/fbsource/third-party/ossrccl/mytest/rccl/build/release/hipify/src/device/primitives.hunused variable 'data2' [-Wunused-variable];

       :=
 |                                  ^~~~~188t| 
                    ^~~~~
:
  h/data/users/ycui1984/fbsource/third-party/ossrccl/mytest/rccl/build/release/hipify/src/device/prims_simple.h152/data/users/ycui1984/fbsource/third-party/ossrccl/mytest/rccl/build/release/hipify/src/device/prims_ll.h/data/users/ycui1984/fbsource/third-party/ossrccl/mytest/rccl/build/release/hipify/src/device/prims_ll.hr::152: | e 103 :152a::287:: 35d   warning: :Iwarning: dunused variable 'data2' [-Wunused-variable]xu
iunused variable 'w' [-Wunused-variable] .n
warning: xunused variable 'flag2' [-Wunused-variable]  
152t/3 | W2   _  A103152 |   tR |    P     _ du iuSi a nttI3nZbEa12t_a;, t3 2r \d_
rfatt      i| la 1e              ^ra,gd
_ 1,ageflna tegrdia1act1,( a2d,_,_a  ttffhlaalr2g,1ae,  gafdla2datga;f22;,

e             f| l                           ^~~~~n| a
g2c                           ^~~~~;e
(/data/users/ycui1984/fbsource/third-party/ossrccl/mytest/rccl/build/release/hipify/src/device/prims_ll.h
"


### Operating System

Linux

### CPU

N/A

### GPU

MI300

### ROCm Version

Rocm 6.4

### ROCm Component

_No response_

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_

## 评论 (3)

### thananon · 2025-08-05

We are aware of this and I think PR just got merged today to address some of these issues. In the meantime, you can go in /build/release directory and call `make -j1` to get serialized output.

### ycui1984 · 2025-08-21

> We are aware of this and I think PR just got merged today to address some of these issues. In the meantime, you can go in /build/release directory and call `make -j1` to get serialized output.

Hey @thananon are you able to share the PR? wanted to cherry pick into meta's env, the current debugging process is painful. make -j1 is too slow. 

### thananon · 2025-08-26

@ycui1984 The PR is https://github.com/ROCm/rccl/pull/1801 and https://github.com/ROCm/rccl/pull/1727.

> make -j1 is too slow.

You can run `./install.sh` script to build in parallel until it error out, then go to `/build/release/` and run `make -j1`. This should be faster.

We are closing this issue as the PRs above have been merged into develop branch. The output is now better for debugging.
