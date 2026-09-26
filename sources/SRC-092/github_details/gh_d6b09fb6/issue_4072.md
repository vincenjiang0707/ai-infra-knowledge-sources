# [Issue #4072] [Bug] -DUSE_NOF=ON build and NoF e2e do not work out of the box on Ubuntu

source: https://github.com/kvcache-ai/Mooncake/issues/4072
state: closed | updated: 2026-09-16T04:29:16Z
labels: 

## 正文

## Summary

A `USE_NOF` build cannot be produced or exercised out of the box by following the documented build path (`docs/source/getting_started/build.md`). On a clean Ubuntu 22.04 machine the documented steps fail at four separate points, all of them missing build/dependency wiring.

## Status

Addressed by #4079 (pending merge), with the latest dependency-scoping commit `c3308edb` (Ubuntu 22.04.5, gcc 11.4.0, cmake 3.22.1, SPDK v23.01.1 built by `dependencies.sh --with-spdk`):

| # | Failure | Fix |
| --- | --- | --- |
| 1 | `--with-rdma requires libverbs and librdmacm` | `dependencies.sh --with-spdk` now invokes SPDK's `pkgdep.sh --rdma`, which installs `librdmacm-dev` without changing the common dependency list |
| 2 | `cannot find -lisal`, `cannot find -lelf` | `libelf-dev` is installed in the Ubuntu/Debian `INSTALL_SPDK` branch for `-lelf`; isa-l is taken from the SPDK build tree with `-L extern/spdk/isa-l/.libs -lisal` — the same flags SPDK's own `mk/spdk.common.mk` uses — instead of installing a second `libisal.a` into `/usr/local/lib` |
| 3 | undefined `SpdkWrapper::GetInstance()` / `ProbeNofSegment()` / `SpdkControllerConfig::FromEnvironment()` | the SPDK wrapper sources, the controller options parser, the SPDK/DPDK include directories and `${SPDK_STATIC_LIBS}` are now part of the reduced `mooncake_store_master` library |
| 4 | `ImportError: libasio.so: cannot open shared object file` | the NoF e2e script exports `$BUILD_DIR/mooncake-common` on `LD_LIBRARY_PATH` |

The documented path in `docs/source/getting_started/build.md` works as written, so no documentation
change is needed: the packages and the SPDK build are both handled by `dependencies.sh --with-spdk`.

Verification on the latest `c3308edb`: `dependencies.sh --with-spdk`, the `USE_NOF=ON` configuration, the full Mooncake build, and installation all succeed. The focused NoF/SPDK tests (`nof_heartbeat_test`, `nof_register_config_test`, and `spdk_controller_config_test`) pass 3/3, and `mooncake_master`, `nof_worker_pool_bench`, and SPDK's bundled `libisal.a` are present. The original NoF e2e verification on `edbb692b` reaches `rc=0` with the master logging `action=unmount_nof_segment_by_heartbeat, last_error_reason=open_fail`. Relinking with the distro `libisal-dev` package installed still links SPDK's static copy (50 isa-l symbols, no `libisal` entry in `DT_NEEDED`), while a missing `extern/spdk/isa-l/.libs/libisal.a` fails at configure time with an actionable message.

## Reproduction environment

| Item | Value |
| --- | --- |
| OS | Ubuntu 22.04.5 LTS |
| Kernel | 5.15.0-181-generic |
| compiler| gcc 11.4.0 |
| SPDK | v23.01.1 |
| Branch | master |

## Reproduction steps

```bash
git clone https://github.com/kvcache-ai/Mooncake.git
cd Mooncake

# 1) dependency + SPDK install
sudo bash dependencies.sh --with-spdk

# 2) configure + build
mkdir build && cd build
cmake .. -DCMAKE_BUILD_TYPE=Release -DUSE_NOF=ON -DBUILD_BENCHMARK=ON
make -j28 nof_worker_pool_bench
make -j28 mooncake_master

# 3) NoF end-to-end test
ln -s ~/spdk ../extern/spdk
BUILD_DIR=$PWD bash ../mooncake-store/tests/e2e/run_nof_heartbeat_tcp_e2e.sh
```

## `configure --with-rdma` aborts: `librdmacm-dev` missing

```
$ ./configure --with-rdma
Using default SPDK env in .../spdk/lib/env_dpdk
Using default DPDK in .../spdk/dpdk/build
--with-rdma requires libverbs and librdmacm.
Please install then re-run this script.
```

Before #4079, `dependencies.sh` installed `libibverbs-dev` but not `librdmacm-dev`. SPDK installs the pair only when `pkgdep.sh` is invoked with `--rdma`:

```bash
# extern/spdk/scripts/pkgdep/ubuntu.sh
if [[ $INSTALL_RDMA == "true" ]]; then
	apt-get install -y libibverbs-dev librdmacm-dev
fi
```

Before #4079, `INSTALL_RDMA` defaulted to `false`, and `dependencies.sh` called `./scripts/pkgdep.sh` without `--rdma`, then immediately configured with `--with-rdma`.

## linking a `USE_NOF` target: `cannot find -lisal`, `cannot find -lelf`

```
/usr/bin/ld: cannot find -lisal: No such file or directory
/usr/bin/ld: cannot find -lelf: No such file or directory
collect2: error: ld returned 1 exit status
make[3]: *** [mooncake-store/benchmarks/CMakeFiles/nof_worker_pool_bench.dir/build.make:152: mooncake-store/benchmarks/nof_worker_pool_bench] Error 1
```

`mooncake-store/src/CMakeLists.txt` ends the NoF link list with bare library names:

```cmake
      z
      isal
      elf
      ibverbs
      rdmacm
```

- Before #4079, `libelf-dev` was missing from the common Ubuntu package list even though the RHEL branch listed `elfutils-libelf-devel`; it is now installed only in the Ubuntu/Debian `INSTALL_SPDK` branch.
- isa-l is not provided at all: SPDK builds it as a submodule, but `make install` does not install it, so `/usr/local/lib/libisal.a` never appears, and no distro isa-l package is installed either. (fixed in #4079 by pointing the link list at the SPDK build tree — see **Status**)

## `make mooncake_master` fails to link

```
/usr/bin/ld: libmooncake_store_master.a(master_service.cpp.o): in function `mooncake::MasterService::MasterService(...)::{lambda(...)}':
    undefined reference to `mooncake::SpdkWrapper::GetInstance()'
    undefined reference to `mooncake::SpdkWrapper::ProbeNofSegment(std::string const&, unsigned int, std::string*)'
/usr/bin/ld: libmooncake_store_master.a(spdk_wrapper.cpp.o): undefined reference to `mooncake::SpdkControllerConfig::FromEnvironment()'
collect2: error: ld returned 1 exit status
make[3]: *** [mooncake-store/src/CMakeFiles/mooncake_master.dir/build.make:112: mooncake-store/src/mooncake_master] Error 1
```

`master_service.cpp` installs the NoF heartbeat probe through `SpdkWrapper`, but the reduced `mooncake_store_master` library is built from the shared and master object lists only: the SPDK wrapper sources are added to the client object list, and `${SPDK_STATIC_LIBS}` is linked into the full `mooncake_store` target only.

This blocks the NoF e2e as well, because the script executes `$BUILD_DIR/mooncake-store/src/mooncake_master`.

## NoF e2e aborts from a source build

```
$ BUILD_DIR=$PWD/build bash mooncake-store/tests/e2e/run_nof_heartbeat_tcp_e2e.sh; echo rc=$?
rc=1

$ cat /tmp/mooncake_nof_heartbeat_e2e/register.log
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: libasio.so: cannot open shared object file: No such file or directory
```

```
$ readelf -d build/mooncake-integration/store.cpython-310-x86_64-linux-gnu.so | grep -E "RUNPATH|NEEDED.*asio"
 0x0000000000000001 (NEEDED)             Shared library: [libasio.so]
 0x000000000000001d (RUNPATH)            Library runpath: [$ORIGIN]
```

The pybind module links `libasio.so` from `build/mooncake-common` but only carries an `$ORIGIN` RUNPATH, which resolves in the installed layout only. The script exports `PYTHONPATH` but nothing for the loader, and `set -euo pipefail` ends the run at the first failed import.





## 评论 (1)

### github-actions[bot] · 2026-09-13

Thanks for opening this issue, @Ziy1-Tan!

| Field | Value |
|-------|-------|
| **Issue** | #4072 |
| **GitHub user ID** | `49604965` |
| **Reporter** | @Ziy1-Tan |

A maintainer will triage this when possible. To help us respond faster, please include:

- Mooncake version or commit SHA
- Environment (OS, CUDA/driver, RDMA stack if relevant)
- Steps to reproduce and expected vs. actual behavior

Useful links: [Documentation](https://kvcache-ai.github.io/Mooncake/) · [Contributing guide](https://github.com/kvcache-ai/Mooncake/blob/main/CONTRIBUTING.md)

> This message was posted automatically by the issue bot.
