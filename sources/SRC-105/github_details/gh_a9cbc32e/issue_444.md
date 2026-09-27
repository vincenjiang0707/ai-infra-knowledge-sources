# [Issue #444] How does Omniperf profile a kernel launched in multiple streams?

source: https://github.com/ROCm/rocprofiler-compute/issues/444
state: closed | updated: 2024-11-29T20:01:43Z
labels: question, Under Investigation

## 正文

Hello, I have a kernel that is launched across four HIP streams. When profiling with Omniperf, how are streams handled?

## 评论 (4)

### coleramos425 · 2024-10-22

Copying @nartmada for triage and issue assignment

### ppanchad-amd · 2024-10-23

@ashesh2512 @coleramos425 - Internal ticket has been created to assist with this issue. Thanks!

### sohaibnd · 2024-11-01

Hi @ashesh2512, sorry for the delay. Currently, you can filter collection of counters by kernel name or dispatch id (see [documentation](https://rocm.docs.amd.com/projects/omniperf/en/latest/how-to/profile/mode.html#filtering)) but not by stream. In your case, if you are launching a single kernel in each stream, I believe it should be sufficient to filter by dispatch id.


### sohaibnd · 2024-11-29

@ashesh2512 I'm going to close this issue due to inactivity. If you have any follow-up questions, feel free to re-open this issue.
