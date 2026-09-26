# [Issue #419] Allow MongoDB TLS Connection options to be passed into omniperf import

source: https://github.com/ROCm/rocprofiler-compute/issues/419
state: closed | updated: 2025-08-06T18:25:11Z
labels: enhancement, Grafana GUI, Under Investigation

## 正文

**Is your feature request related to a problem? Please describe.**
It is a problem for me, because I am trying to connect to a MongoDB where TLS is enabled.

**Describe the solution you'd like**
I would like to have several tls connection options during import. 
Like: `tls=true, tlsAllowInvalidCertificates=true/false , --tlsAllowInvalidHostnames=true/false, --tlsCAFile , etc '

**Describe alternatives you've considered**
We forked this repo and implemented a solution for previous version but it is hard to keep up with so much refactor code.

**Additional context**
Thank you for any consideration.


## 评论 (7)

### coleramos425 · 2024-08-29

Thank you for the feature request. I've assigned the ticket to the project PM who will delegate it to an engineer. Once we've triaged, we'll follow up with an ETA.
CC: @nartmada 

### ppanchad-amd · 2024-10-04

Hi @ELCapitanLLNL. Internal ticket has been created to assist with your request. Thanks!

### taylding-amd · 2024-10-08

Hi, @ELCapitanLLNL. I wanted to update you on the feature request. I've followed up with the Omniperf team, and it is likely to be included in version 6.6. Please keep an eye out for further updates in the release notes.

### ELCapitanLLNL · 2024-10-08

Sounds good, also I wondering if it is need it to use the `admin` account or can the upload workloads using regular MongoDB user account with access to a database name: `omniperf` . 

### taylding-amd · 2024-10-11

Hi, @ELCapitanLLNL, sorry I can't provide an answer now. We have not yet made a design decision regarding that feature. Once it is released, we will ensure comprehensive documentation is available to guide its usage.

### systems-assistant[bot] · 2025-08-06

This issue has been migrated to: https://github.com/ROCm/rocm-systems/issues/49

### amd-hsivasun · 2025-08-06

Imported to ROCm/rocm-systems
