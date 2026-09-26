# [Issue #40] [Feature]: rocprofv3 output

source: https://github.com/ROCm/rocprofiler-sdk/issues/40
state: closed | updated: 2025-06-24T21:07:51Z
labels: Under Investigation, Feature Request

## 正文

### Suggestion Description

We have been experimenting with the new `rocprofv3` provided by `roc profiler-sdk`. We use `ROCm` 6.3.1. It's really great to see such good progress! We have been using it for "application tracing" and "kernel profiling" of a `Kokkos`-based code. We have been using the `Perfetto` `traceprocessor` in `Python` for post processing.

These are a few suggestions for the output from `rocprofv3`:

i) The workgroup and grid sizes are currently provided as a reduced product:

- https://github.com/ROCm/rocprofiler-sdk/blob/042c761b6431d1b069768385545830c3607af711/source/lib/output/generatePerfetto.cpp#L518-L521

It may be interesting to pass them as triples of integers.

ii) The counters are currently provided in the `csv` output, but not in the `pftrace` output. It may be interesting to output them in the `pftrace` table too, e.g. in the `args` table, similar to how the `corr_id` is currently handled.

 iii) The way the counters are currently provided in the `csv` output appears somewhat inefficient when multiple counters are asked for. In such a case, entire rows in the csv file are replicated entirely several times, with only a different counter name and value for each counter. It. may be interesting to provide the counter results by extending the rows with multiple (name, value) pairs, thus avoiding duplication.

iv) It may be interesting to highlight in the docs the use of the `Perfetto` `traceprocessor` in `Python` as a way to postprocess the results from the `pftrace` file. I.e., I think that currently, the docs mention the `perfetto UI`, but they do not yet mention the `traceprocessor`.

### Operating System

Ubuntu 24.04

### GPU

VEGA906

### ROCm Component

HPC using Kokkos with HIP backend

## 评论 (3)

### jrmadsen · 2025-02-04

We are working on (ii). Yes, for (iii) it is inefficient but trivial to combine for multi-node data and application replay when the counters change between runs. We are working on a conversion script. For (iv), we are working on a SQL database schema + a Python package for post-processing. We do not intend to rely on Perfetto for numerous reasons. I’ll make a note of (i)

### maartenarnst · 2025-02-04

Sounds great! Thanks for the feedback!

### harkgill-amd · 2025-06-24

Closing this out, as the requested items are already in progress internally. Feel free to leave a comment if you have any further questions.
