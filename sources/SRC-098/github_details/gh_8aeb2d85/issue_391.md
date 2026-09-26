# [Issue #391] Consider adding an `MPI_INCLUDE` check in the `src/Makefile`

source: https://github.com/NVIDIA/nccl-tests/issues/391
state: closed | updated: 2026-08-05T09:00:31Z
labels: 

## 正文

Currently:
> If you want to compile the tests with MPI support, you need to set `MPI=1` and set `MPI_HOME` to the path where MPI is installed.

In some distributions, OpenMPI's header files may not reside in `MPI_HOME`. For example, in Fedora, binaries and libraries are provided by the `openmpi` package, while header files are provided by the `openmpi-devel` package:
```bash
$ module load mpi/openmpi-$(uname -m)
## MPI_HOME, MPI_INCLUDE, etc. will be set

$ echo $MPI_HOME && ls $MPI_HOME
/usr/lib64/openmpi
bin  include  lib  share

$ ls $MPI_HOME/include ## nothing resides here

$ echo $MPI_INCLUDE && ls $MPI_INCLUDE
/usr/include/openmpi-aarch64
mpi-ext.h mpif-externals.h mpif-io-constants.h mpi.h ## ... skipped
```
---
Currently in `src/Makefile`:
https://github.com/NVIDIA/nccl-tests/blob/a0b82b2260cf5152b9f8c061bbf7eaf0ba096432/src/Makefile#L23-L26
It only checks `$MPI_HOME/include` for headers, which will fail in Fedora:
```
In file included from util.h:9,
                 from util.cu:19:
common.h:20:10: fatal error: mpi.h: No such file or directory
   20 | #include "mpi.h"
      |          ^~~~~~~
compilation terminated.
```

Adding a `$MPI_INCLUDE` check will resolve this issue. For example:
```makefile
ifeq ($(MPI), 1)
MPI_INCLUDE ?= $(MPI_HOME)/include
NVCUFLAGS += -DMPI_SUPPORT -I$(MPI_INCLUDE)
NVLDFLAGS += -L$(MPI_HOME)/lib -L$(MPI_HOME)/lib64 -lmpi 
endif 
```

## 评论 (1)

### hiroshi-ya · 2026-08-05

The PR was merged. Issue no longer persists after pulling the [latest commit](https://github.com/NVIDIA/nccl-tests/commit/717b68318278e93f371d8ffb46b076069d7c7851). Closing the issue.
