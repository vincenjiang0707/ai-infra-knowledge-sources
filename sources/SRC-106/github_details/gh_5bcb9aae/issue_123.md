# [Issue #123] need to include cstdint

source: https://github.com/ROCm/amdsmi/issues/123
state: closed | updated: 2025-11-26T16:15:38Z
labels: 

## 正文

Building 7.0 on fedora, there is this error.

/builddir/build/BUILD/amdsmi-7.0.0-build/amdsmi-rocm-7.0.0/rocm_smi/include/rocm_smi/rocm_smi_common.h:127:5: error: ‘uintptr_t’ does not name a type
  127 |     uintptr_t func_id_iter;
      |     ^~~~~~~~~
/builddir/build/BUILD/amdsmi-7.0.0-build/amdsmi-rocm-7.0.0/rocm_smi/include/rocm_smi/rocm_smi_common.h:31:1: note: ‘uintptr_t’ is defined in header ‘<cstdint>’; this is probably fixable by adding ‘#include <cstdint>’
   30 | #include <unordered_set>
  +++ |+#include <cstdint>
   31 | 

The issue can be resolved with
sed -i '/#include <unordered_set.*/a#include <cstdint>' rocm_smi/include/rocm_smi/rocm_smi_common.h


## 评论 (2)

### AngryLoki · 2025-10-18

Seems to be fixed in https://github.com/ROCm/amdsmi/commit/902667db3cafe72e2009287cb96b160854ab9d81

### darren-amd · 2025-11-26

Hi @trixirt,

Thanks for the report, this appears to be fixed as mentioned above, but please reopen if the issue persists, thanks!
