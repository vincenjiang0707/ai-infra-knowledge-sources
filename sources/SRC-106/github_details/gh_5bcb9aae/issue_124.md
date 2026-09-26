# [Issue #124] need to include iomanip

source: https://github.com/ROCm/amdsmi/issues/124
state: closed | updated: 2025-11-13T21:21:44Z
labels: status: assessed

## 正文

Building with testing on Fedora has this error

/builddir/build/BUILD/amdsmi-7.0.0-build/amdsmi-rocm-7.0.0/tests/amd_smi_test/functional/frequencies_read.cc: In function ‘void print_frequencies(amdsmi_frequencies_t*, uint32_t*)’:
/builddir/build/BUILD/amdsmi-7.0.0-build/amdsmi-rocm-7.0.0/tests/amd_smi_test/functional/frequencies_read.cc:73:12: error: ‘setw’ is not a member of ‘std’
   73 |       std::setw(2) << std::right << clk_i_str << ": " <<
      |            ^~~~
/builddir/build/BUILD/amdsmi-7.0.0-build/amdsmi-rocm-7.0.0/tests/amd_smi_test/functional/frequencies_read.cc:31:1: note: ‘std::setw’ is defined in header ‘<iomanip>’; this is probably fixable by adding ‘#include <iomanip>’
   30 | #include "../test_common.h"
  +++ |+#include <iomanip>

This can be resolved with
sed -i '/#include <string.*/a#include <iomanip>' tests/amd_smi_test/test_common.h


## 评论 (2)

### AngryLoki · 2025-10-18

Seems to fixed in master branch (iomanip was included somewhere else...)

### darren-amd · 2025-11-11

Hi @trixirt,

This appears to be fixed with: https://github.com/ROCm/amdsmi/commit/982737a85255a4f42b4e460a1c90c3a6986dbc41, thanks for the report!
