# [Issue #182] Combining Granfana and standalone GUI

source: https://github.com/ROCm/rocprofiler-compute/issues/182
state: closed | updated: 2025-08-06T18:35:44Z
labels: Omniperf Revamp

## 正文

**Describe the suggestion**
Combining the best of Granfana and standalone GUI

**Justification**
There are clear benefits to each of the GUI options we offer today. That being said, having two options (packaged separately in client & server side packages) can cause confusion.

- Grafana GUI
(+) DB backend enables teams to share workload data for collaborative analysis
(+) Long-term benefits to building a central repository of performance data
(+) More performant and larger threshold for high dispatch workloads
(-) Queries dependent on a more niche MongoQL
(-) Requires a server-side setup
 
- Standalone GUI
(+) Usage is straightforward
(+) Piggybacks directly off existing YAML infrastructure used in CLI
(+) HTML-based stack presents more flexibility for future development
(-) Less mature and lower threshold for high dispatch workloads

If we were able to re-think the Standalone GUI to include some of the best parts of the Grafana solution we'd be offering a much clearer solution to customer.

Additionally, axing Granfana would mean an unequivocal source of metric definitions - the YAML files. No more jumping between MongoQL and yaml.

**Implementation**
At the moment, the clear benefit in Grafana is the DB backend. If we were to offer options at the install level to bring up a DB backend. We could configure the standalone GUI to read workload data from that source, i.e.
```console
$ omniperf analyze --host dummyhost --user amd --gui
```
Here the user could interact with a dropdown menu for workload selection similar to today's Grafana. If you're not interested in that, you could skip the flag at install stage (to ignore docker DB setup) and interact via CLI or Standalone GUI in today's "offline" manner.

**Additional Notes**
We could market this as an "online" vs. "offline" analysis in Omniperf docs

_Originally posted by @coleramos425 in https://github.com/AMDResearch/omniperf/discussions/153#discussioncomment-6855471_

## 评论 (2)

### systems-assistant[bot] · 2025-08-06

This issue has been migrated to: https://github.com/ROCm/rocm-systems/issues/72

### amd-hsivasun · 2025-08-06

Imported to ROCm/rocm-systems
