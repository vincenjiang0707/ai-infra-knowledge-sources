# [Issue #2577] Power proposal 2 - Enabling software based power measurements

source: https://github.com/mlcommons/inference/issues/2577
state: open | updated: 2026-09-04T14:43:34Z
labels: 

## 正文

This topic has been discussed by the working group for several weeks, but there does not appear to be sufficient momentum to proceed at this time. As a result, we will move the discussion offline for now.

The detailed proposal can be found here (members only):
https://docs.google.com/document/d/1GMeMD4oXoL0KeXjXm4h-kpsbqNccEKvBvwHYOM7CUTw/edit?tab=t.0#heading=h.wt5klpyit9pz

Please leave a comment if you are interested, and we can continue the discussion offline. If we are unable to gather sufficient interest, this PR will be closed automatically.

## 评论 (14)

### araghun · 2026-05-12

@hanyunfan we bought this topic up in the PowerWG a few times I am hoping to start seeing engagement on this issue.



### guthrieg · 2026-05-12

Software based measurements will make it significantly easier for organizations to demonstrate the power usage of their inference and other submissions. Instead of purchasing and adding an outside power measurement device, they can leverage the existing software to accurately measure power.

### Sreebhargavibalijaa · 2026-05-12

@hanyunfan @araghun , 
The proposal states that aggregation rules will "ensure proportional weighting if nodes handle uneven workloads," but provides no concrete methodology. This is a critical gap for multi-node inference configurations. Specifically:

How will workload distribution be measured and logged, by token throughput, batch count, or wall-clock active time and who is responsible for instrumenting this per node?
If a node is partially idle during an inference run (e.g., a prefill-heavy vs. decode-heavy split), will its idle power be included in the submission total, and under what accounting rules?

The Working Group should define a normative aggregation specification, not leave it to submitters to prevent divergent interpretations that could make multi-node results incomparable across organizations.

### zhangbinbj2048-design · 2026-05-12

The proposal will reduce the dependence on expensive physical power  meters,but there are two issues that need attention:

1.When using software to read power, it is necessary to unify the sampling frequency, collect duration, and calculation method for data collection. This avoids excessive deviation of results caused by inconsistent collection logic among different customers.
2.It is required to distinguish the adaptation rules of software power consumption under DC and AC power supply, and mandatorily mark the power supply type in the reporting template.

### ShaohuiLiu · 2026-05-12

Agree with @guthrieg. Software-based measurements could significantly lower the barrier for organizations to report power usage, especially when external power meters introduce additional cost and difficulty of deploy.

One caveat is that software measurements may introduce additional error or bias depending on the tool, firmware, driver stack, and platform-specific exposure. This may make standardization and cross-submission comparability more difficult. The practical difficulty also varies by platform: for example, IPMI availability/exposure is not always consistent; some HGX servers may require sudo/root access for RAPL or other telemetry; while GH200/GB200/GB300 platforms can often expose node-level power more conveniently through DCGM.

So I support enabling software-based measurements, but it would be helpful to define clear requirements around accepted telemetry sources, calibration/validation expectations, sampling frequency, and how uncertainty/error should be reported.

### hanyunfan · 2026-06-02

Just my two cents: 

1. We may need more clarity on how this can be implemented in details.


2. Hardware calibration with SPEC meters is not straightforward and still the roadblocker. It would be ideal if we could eliminate or simplify this validation requirement.


3. We need a reliable way to ensure that software-based measurements are trustworthy and consistent. i.e., that all tools measure the same metrics in the same way. Standardizing a single tool or methodology may help address this.


4. If the above criteria cannot be fully met, we should consider treating software-based measurements as reference-only data points, rather than allowing direct comparisons between systems, or maybe first allow it in Open division only.

### guthrieg · 2026-06-08

@hanyunfan any recommendations on what is required to sufficiently validate the software-based approach? We have some initial data that suggested the software approach is >97% accurate (quoting from memory).

### hanyunfan · 2026-06-08

> [@hanyunfan](https://github.com/hanyunfan) any recommendations on what is required to sufficiently validate the software-based approach? We have some initial data that suggested the software approach is >97% accurate (quoting from memory).

This is one of the more challenging aspects. We would either need to rely on IPMI/DCMI or Redfish implementations from system vendors, as it is ultimately their responsibility to ensure accurate power data is exposed to end users, or/and classify software-based measurements as unverified. We could consider automatically integrating a unified power command into inference submission runs, either in-band or out-of-band, where feasible.

While there is no perfect solution today due to the lack of standardized OOB power implementations, I believe this approach is simple enough to encourage power submissions without introducing significant overhead.

### dslik · 2026-06-08

One approach is to cross-reference the power data reported by a RedFish-enabled PDU and reported by IPMI/RedFish enabled BMC for each of the servers to see if there is agreement within a certain bound.

I am working on a power data collector for RedFish that will be capable of doing this. The submitter would need to launch this on each host and provide read-only RedFish credentials for each host, plus the IP address(es) and credentials for the PDU(s).

We will also need to do a survey of how widely the RedFish SensorEnergykWhExcerpt LifetimeReading property is supported by BMC and PDU vendors, how many significant figures are provided, and if the vendors will provide/stand behind any accuracy numbers, since cumulative power measurements will be required, along with enough significant figures to accurately measure the consumed power.

### manunicholasjacob · 2026-09-02

On the validation question from June: this is what has held up for me when the ground truth is a hardware rail rather than a wall meter. My own work, not connected to my employer.

The reference has to be upstream of the software path it validates, so the PDU-against-BMC cross-check proposed above is the right shape for the BMC layer; the same step is then needed one level down, BMC or PSU reading against the in-band counter (RAPL, NVML, DCGM), since that is the number a software submission would actually report. On the boards I measure the reference is the PMIC's per-rail ADC at about 44 Hz, and the check is the same at any scale: integrate both over the timed window and compare joules, not watts.

The bound should therefore be on energy, stated separately for idle and loaded. In-band counters disagree with the rail most at idle, where a fixed offset of a few watts is a large fraction, and least under sustained load, so ">97%" is only meaningful once it says which. "Integrated energy within X% of the reference over the timed window, idle floor reported and excluded from the bound" is checkable.

Three failure modes need a rule, because each has produced a wrong number for me:

1. Counter wrap. Linux RAPL `energy_uj` wraps at `max_energy_range_uj`, about 65 kJ on common parts, under five minutes at 250 W. Subtracting consecutive samples without correcting the wrap gives a large negative delta once per cycle; polling slowly misses whole wraps silently. Rule: sample faster than half the wrap period and log the raw counter.
2. Permissions. Since CVE-2020-8694 the powercap `energy_uj` files are mode 0400, so an unprivileged harness reads nothing and some tools fall back to a model-based estimate without saying so. A submission should record whether the counter was read or estimated.
3. Rail scope. Package domains and GPU board power leave out fans, storage, NICs and PSU loss, so an in-band total is a lower bound on wall power by a platform-dependent margin. Either the scope is declared per submission, or the rules ask for a one-time per-platform offset against a wall meter, which is a far smaller ask than a SPEC meter on every run.

For reference: the host collector I wrote for the aiperf load generator (ai-dynamo/aiperf PR #1341) implements the wrap correction and the permission check, and the PMIC-referenced dataset is public (10.5281/zenodo.21987261, Raspberry Pi 5, 831 runs). I am not a member and this is not an attempt to steer what the WG accepts.


### hanyunfan · 2026-09-03

@manunicholasjacob Just wanted to let you know that Dell is a member of MLCommons (MLC). Would you be interested in presenting your work to either the MLPerf Inference Working Group or the Power Working Group?

### manunicholasjacob · 2026-09-03

Thanks @hanyunfan, happy to, and the Power Working Group seems the natural fit for the topic. Since this is personal research I would join as an individual guest. I would cover the validation protocol above, the three failure modes, and the PMIC-referenced dataset, and can go deeper on any of them. What format and timing work for the group?


### hanyunfan · 2026-09-03

I would let the power group chair @araghun to comment, but let me know if you need the invite for the power group meeting. 

### manunicholasjacob · 2026-09-03

Got the invite, thanks. Happy to sync with @araghun on scoping whenever suits.

