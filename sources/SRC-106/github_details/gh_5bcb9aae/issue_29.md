# [Issue #29] Build fails for amdsmi using Amazon Linux 2

source: https://github.com/ROCm/amdsmi/issues/29
state: closed | updated: 2024-10-28T19:00:03Z
labels: 

## 正文

### Problem Description

Followed build procedure with amdsmi that worked with rocm-smi v6.1.0 or v6.0.2 (https://github.com/ROCm/rocm_smi_lib) on same machine, with same versions of cmake (v3.29.2) and g++ (v7.3.1). Build fails at 'cmake' step indicating that libdrm is missing. However, the machine also has libdrm is installed (libdrm-2.4.97-2.amzn2.x86_64).

### Operating System
Amazon Linux 2

### CPU
2nd generation AMD EPYC (using g4ad.4xlarge instance on AWS)

### GPU
AMD Radeon Pro V520

### ROCm Version
ROCm 6.1.1, 6.1.0, 6.0.2

### ROCm Component
amdsmi

### Steps to Reproduce
Perform the following:
```
git clone https://github.com/ROCm/amdsmi.git
mkdir -p build
cd build
cmake ..
```

Output:
```
-- Found PkgConfig: /usr/bin/pkg-config (found version "0.27.1")
fatal: No names found, cannot describe anything.
usage: git rev-list [<options>] <commit>... [--] [<path>...]

  limiting output:
    --max-count=<n>
    --max-age=<epoch>
    --min-age=<epoch>
    --sparse
    --no-merges
    --min-parents=<n>
    --no-min-parents
    --max-parents=<n>
    --no-max-parents
    --remove-empty
    --all
    --branches
    --tags
    --remotes
    --stdin
    --exclude-hidden=[receive|uploadpack]
    --quiet
  ordering output:
    --topo-order
    --date-order
    --reverse
  formatting output:
    --parents
    --children
    --objects | --objects-edge
    --disk-usage[=human]
    --unpacked
    --header | --pretty
    --[no-]object-names
    --abbrev=<n> | --no-abbrev
    --abbrev-commit
    --left-right
    --count
  special purpose:
    --bisect
    --bisect-vars
    --bisect-all
usage: git rev-list [<options>] <commit>... [--] [<path>...]

  limiting output:
    --max-count=<n>
    --max-age=<epoch>
    --min-age=<epoch>
    --sparse
    --no-merges
    --min-parents=<n>
    --no-min-parents
    --max-parents=<n>
    --no-max-parents
    --remove-empty
    --all
    --branches
    --tags
    --remotes
    --stdin
    --exclude-hidden=[receive|uploadpack]
    --quiet
  ordering output:
    --topo-order
    --date-order
    --reverse
  formatting output:
    --parents
    --children
    --objects | --objects-edge
    --disk-usage[=human]
    --unpacked
    --header | --pretty
    --[no-]object-names
    --abbrev=<n> | --no-abbrev
    --abbrev-commit
    --left-right
    --count
  special purpose:
    --bisect
    --bisect-vars
    --bisect-all
0 were found since previous release
Package version: 24.5.2.0-local-build-0-ca520ac
-- The C compiler identification is GNU 7.3.1
-- The CXX compiler identification is GNU 7.3.1
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /usr/bin/cc - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Check for working CXX compiler: /usr/bin/c++ - skipped
-- Detecting CXX compile features
-- Detecting CXX compile features - done
Using CPACK_DEBIAN_PACKAGE_RELEASE
Using CPACK_RPM_PACKAGE_RELEASE
Cloning into '/home/ec2-user/amdsmi/esmi_ib_library'...
Note: switching to '1cc7a252d75b4037549218b1014d077282998ef3'.

You are in 'detached HEAD' state. You can look around, make experimental
changes and commit them, and you can discard any commits you make in this
state without impacting any branches by switching back to a branch.

If you want to create a new branch to retain commits you create, you may
do so (now or later) by using -c with the switch command. Example:

  git switch -c <new-branch-name>

Or undo this operation with:

  git switch -

Turn off this advice by setting config variable advice.detachedHead to false

-- Checking for module 'libdrm'
--   No package 'libdrm' found
CMake Error at /usr/local/share/cmake-3.29/Modules/FindPkgConfig.cmake:645 (message):
  The following required packages were not found:

   - libdrm

Call Stack (most recent call first):
  /usr/local/share/cmake-3.29/Modules/FindPkgConfig.cmake:873 (_pkg_check_modules_internal)
  CMakeLists.txt:135 (pkg_check_modules)


-- Configuring incomplete, errors occurred!
```

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support
No response

### Additional Information
No response


## 评论 (2)

### harkgill-amd · 2024-09-17

Hi @wkneewalden, from what I can see from both SMI tools requirements, only amd-smi requires libdrm (see [here](https://github.com/ROCm/amdsmi/blob/amd-staging/CMakeLists.txt#L135C1-L136C1)). This is likely why you were able to successfully build rocm-smi but not amd-smi. 

It looks like the `libdrm` packaged in the Amazon Linux distro doesn't provide the correct files that pkg-config is searching for. Could you try to install the `libdrm-devel` package to see if the build error is resolved?

### harkgill-amd · 2024-10-28

Closing this issue due to lack of response. @wkneewalden, if you are unable to resolve the error after installing the `libdrm-devel` package, please leave a comment and I will re-open this issues. Thanks!
