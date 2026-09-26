# [Issue #2576] Power measurement proposal #1 - Nameplate Power

source: https://github.com/mlcommons/inference/issues/2576
state: open | updated: 2026-07-30T13:21:57Z
labels: 

## 正文

This topic has been discussed by the working group for several weeks, but there does not appear to be sufficient momentum to proceed at this time. As a result, we will move the discussion offline for now.

The detailed proposal can be found here (members only):
https://docs.google.com/document/d/1Pr4N3dR5BdX_LsqVj5pji6YLbCXvPGz6p-zYFp8ruoE/edit?tab=t.0#heading=h.ia2wutct1aw0

The corresponding PR is available here:
https://github.com/mlcommons/inference_policies/pull/324

Please leave a comment if you are interested, and we can continue the discussion offline. If we are unable to gather sufficient interest, this PR will be closed automatically.

## 评论 (14)

### araghun · 2026-05-12

@hanyunfan we bought this topic up in the PowerWG a few times I am hoping to start seeing engagement on this issue.

### guthrieg · 2026-05-12

Adding comment from 324: This PR will make it incredibly easy for organizations to include power measurements in their inference submissions to align with regulations of the upper bound power measurements of their equipment. I am in support of this.

### ShaohuiLiu · 2026-05-12

This will be a very useful feature and provide solid references if nameplate values are provided. Two potential minor clarification items:

1. For submitters who are not 'system owners', it is not easy to access nameplate values.
2. For same type of servers (e.g. same CPU,GPU,RAM,Disk etc.), different vendors/customers may have/request different configurations, e.g. N+1, N+2, ... , 2N for PSUs. But different N+x's do not necessarily imply server nameplate powers are different. Similarly, same hardware (CPU,GPU) might also be set at different power level.

### Sreebhargavibalijaa · 2026-05-12

@hanyunfan @araghun 
The proposal does not specify which components are mandatory in the YAML hierarchy, nor does it define any automated validation to enforce completeness at submission time. 
What prevents a submitter from reporting only accelerator PSU capacity while omitting CPUs, networking, or storage, and will the MLPerf submission checker be updated with normative validation rules to flag incomplete component hierarchies before a submission is accepted?

### zhangbinbj2048-design · 2026-05-12

For customers, there are two references:
1.It enables customers to fully understand the performance and power consumption performance of their server.
2.It helps summarize the direction for power consumption optimization.

### fujitsu-notsu · 2026-05-19

It would be beneficial to have a field for the number of devices or servers.

Recent submissions have systems with over a dozen nodes, and inputting the same information for each node is cumbersome.
Therefore, it would be better to provide a field, such as "counts," where the number of units is specified.
If this field is not entered, the number of units should be interpreted as one.

### hanyunfan · 2026-06-02

Current Concerns from My Side:


1. The Inference WG does not appear to show strong interest in this proposal, as it introduces additional strict requirements that could potentially block submissions due to non-coding-related issues.


2. The use of nameplate power can be misleading. For example, if Server A has a higher nameplate power, it does not necessarily indicate poorer power efficiency. This distinction may also be difficult to clearly communicate to readers.


3. Nameplate power is not commonly used for datacenter design in practice. Designing datacenter capacity based on nameplate power could lead to significant over-provisioning and inefficient resource utilization. But this is just my understanding, we need more feedbacks.


4. Has the Power WG received feedback from other working groups? Specifically, are the Training and Storage WGs planning to adopt nameplate power as well?



### hanyunfan · 2026-06-03

Alternatively, another approach could be to capture the power supply nameplate information instead of the overall system nameplate power. This would simplify the process, and much of this information may be directly retrievable from the system.

We could define a set of required and optional fields, such as:

Input voltage range
Input current
Frequency
Output voltage
Output current
Maximum output power
Power supply model
Redundancy configuration (e.g., 1+1, 2+1)
Number of PSUs
Certification details (e.g., 80 PLUS rating)

One example: 
https://supportkb.dell.com/img/ka0Do0000002giBIAQ/ka0Do0000002giBIAQ_en_US_1.jpeg

If this can be integrated into the automated system.json generation script, it would allow us to include power-related information for Inference while adding minimal overhead for submitters.

### guthrieg · 2026-06-08

@araghun could the nameplate power be collected automatically in the harness leveraging the Redfish topology API?

### dslik · 2026-06-08

> 3\. Nameplate power is not commonly used for datacenter design in practice. Designing datacenter capacity based on nameplate power could lead to significant over-provisioning and inefficient resource utilization. But this is just my understanding, we need more feedbacks.

The nameplate power (regulatory rating of max input power draw of each power supply) is required to be factored into power distribution design by national electrical codes (wire sizing, connector types, protective breakers, etc). When there is redundancy (e.g. an A-bus and B-bus), everything must be sized assuming that either of the two busses may take up the entire load at any time. Depending on the reliability design approach for the data center, upstream PDUs and UPSes may also need to take into account the total nameplate power vs. the lower design power. This is why it is also important to collect both nameplate power and design power (sum of the nameplate power for all active PSUs).

> 4\. Has the Power WG received feedback from other working groups? Specifically, are the Training and Storage WGs planning to adopt nameplate power as well?

Storage WG is planning to collect nameplate power for each power supply, and design power for each system component in the 3.0 submission round. From their YAML schemas:

```
---
#
# This represents the power configuration for a node or switch.  We need to know the number of
# power supplies that are present in the chassis, plus the minimum number that are required to
# keep the node or switch running.  There are many possible configurations:
#   active/passive 1+1 -- one active and one standby
#   active/active N+1  -- N in total but only 1 is needed to keep the gear running
#   active/active N+M  -- N in total but only M are needed to keep the gear running
#
power_device:
    min_psus_active:            int( min=1 )
    psus_configured:            list( include( 'power_supply' ), min=1 )

---
#
# Each individual power supply needs to be described
#
power_supply:
    unit_count:                 int( min=1 )        # Number of power supplies that look like this
    power_capacity_watts:       int( min=1 )        # The total nameplate capacity of the power supply
    efficiency:                 enum( 'Gold', 'Platinum', 'Titanium', 'Ruby' )
```

Some refinements are still being made to this schema.

> [@araghun](https://github.com/araghun) could the nameplate power be collected automatically in the harness leveraging the Redfish topology API?

Yes. Most of the information in the list @hanyunfan provided can be obtained programmatically using RedFish.

### dslik · 2026-06-16

Here is a link to the full system description shema from the ML Perf Storage WG: https://github.com/mlcommons/storage/blob/0d75e204c4e7de7e8099856084945caa9805dce8/mlpstorage_py/system_description/schema.yaml#L131

### arav-agarwal2 · 2026-07-01

I've seen a PR tackling this issue by @dslik - https://github.com/mlcommons/inference_policies/pull/324/changes. 

Is this supposed to be merged for the July inference submission? If so can I get clarification on my comments on the PR - copying it over here for visibility:

```
For validation purposes, is the intent to validate what's expected in the RedFish PowerSupply schema for each item, or does "based on the PowerSupply schema" here mean that there's some list of required subfields?

I'm asking this as the PowerSupply schema only requires the following fields, according to my understanding of their JSON schema:

@odata.id
@odata.type
Id
Name
The https://github.com/OData fields are used to identify the schema and the version of the schema used, so while I can omit them we'd need to pick a version of the PowerSupply schema for our purposes, or decide to have a YAML-wide @odata.type field to record the PowerSupply schema version.

I'm more worried about the fields, like PowerCapacityWatts, that aren't required by the resource schema but are probably required to make the data useful for everyone. If we want validation on this YAML, can we include which fields are required for submission?
```

### nvashutoshd · 2026-07-29

I think its important to require that any listing/claim of power be backed by publicly available data.

For example - if you claim your PSU consumes X watts, and you have Y PSUs - that needs to be documented publicly. 
Similarly - claims about TDP need to have public documentation.

This is important for accountability and audit. Else, submitters could claim anything in a submission, and theres no way to verify or validate. 

### hanyunfan · 2026-07-30

I like this idea. I’ll add it to the WG meeting agenda so we can spend a few minutes discussing it, and I’d also recommend covering it in more detail during the review meeting.
