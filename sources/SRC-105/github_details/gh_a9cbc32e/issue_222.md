# [Issue #222] Release cadence and MI300 support

source: https://github.com/ROCm/rocprofiler-compute/issues/222
state: closed | updated: 2025-01-16T15:58:22Z
labels: question

## 正文

**Describe your question**
Hi, Thanks for building omniperf. It is very helpful for kernel profiling. I have a few questions.  

1. I'm using omniperf on MI200 on RHEL9 and would like to use the roofline feature. I noticed that support for RHEL9 was added in #188. When would the next release be published so that we can use this feature out of the box? 

1. Would it be possible to share the exact steps to build the tarball? I followed the steps `.github/workflows/tarball.yml` using the 2.x branch but the generated tarball doesn't work.

1. I would like to use omniperf on MI300. By when can we expect support for MI300 and which branch can I use to build a tarball for MI300?

Thanks!

P.S. It would be nice to have instructions on how to build omniperf from source. I hope you will consider adding it to the documentation.

**Additional context**
Add any other context or screenshots about the question here.


## 评论 (3)

### coleramos425 · 2024-01-13

Hi @anupambhatnagar. Glad to hear you've gotten value out of the tool. 

> I'm using omniperf on MI200 on RHEL9 and would like to use the roofline feature. I noticed that support for RHEL9 was added in https://github.com/AMDResearch/omniperf/issues/188. When would the next release be published so that we can use this feature out of the box?

The next release, [v2.0.0](https://github.com/AMDResearch/omniperf/milestone/8), is targeted for Jan. 2024. Until then things are available to preview in the `dev` branch. Expect that release in the next few weeks

> Would it be possible to share the exact steps to build the tarball? I followed the steps .github/workflows/tarball.yml using the 2.x branch but the generated tarball doesn't work.

If you peek at our docs, all [Client-side installation steps](https://amdresearch.github.io/omniperf/installation.html#client-side-installation) are outlined in detail. If you need to install from source, simply follow these instructions from the cloned repo directory
![image](https://github.com/AMDResearch/omniperf/assets/11466906/5e31a69d-065f-4070-953d-2267c71a1565)

> I would like to use omniperf on MI300. By when can we expect support for MI300 and which branch can I use to build a tarball for MI300?

Mi300 support in ROCm software stack is moving rapidly. We're hoping to include support in our [v2.0.0](https://github.com/AMDResearch/omniperf/milestone/8) release. We have a working version available for preview in our `mi300` branch. If you may, reach out to cole.ramos@amd.com and I'll share build instructions for that branch.




### anupambhatnagar · 2024-01-14

Many thanks @coleramos425 for the prompt reply and sharing your email :)  I'll try out the steps you suggested and reach out if needed. Looking forward to the upcoming release!

### jamesxu2 · 2025-01-16

Hi @anupambhatnagar, just an update - MI300 support for omniperf (now called rocprofiler-compute) is nearly complete, but there are a few features that, while functionally enabled for MI300, are still being tested - these include the roofline and memory chart features. 

They will be completed in a future ROCm release. 
