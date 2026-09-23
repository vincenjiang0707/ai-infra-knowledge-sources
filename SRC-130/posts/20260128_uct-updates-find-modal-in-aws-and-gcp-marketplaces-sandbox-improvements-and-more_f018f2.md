# Product Updates: Modal in AWS & GCP marketplaces, Sandbox improvements, and more

source: https://modal.com/blog/product-updates-find-modal-in-aws-and-gcp-marketplaces-sandbox-improvements-and-more
published: 2026-01-28T00:00:00.000Z

[Back](https://modal.com/blog)

# Product Updates: Modal in AWS & GCP marketplaces, Sandbox improvements, and more

**Modal is available on AWS and GCP Marketplace**

Enterprise customers can now purchase and manage Modal through AWS or Google Cloud Marketplaces. Existing AWS or GCP spend commitments can be applied to Modal usage.

Chat with us to [learn more](https://modal.fillout.com/contactus).

**Improved Sandbox observability**

We’ve shipped a round of UI updates to make Sandboxes easier to understand at a glance — including clearer resource and region details, and a new execution timeline showing each Sandbox’s full lifecycle from creation to termination

**Client Updates**

Run `uv pip install --upgrade modal`

to get the latest client updates. Here are some highlights from the changelog:

- Added support for Python 3.14, including experimental support for free-threaded Python (3.14t) inside Modal containers (
[1.3.1](https://modal.com/docs/reference/changelog#131-2026-01-22)) - Added
and`modal token info`

flags across key CLI commands to make authentication and logs easier to inspect (`-timestamps`

[1.3.1](https://modal.com/docs/reference/changelog#131-2026-01-22)) - Added experimental async usage warnings to help detect blocking Modal APIs used inside async contexts (
[1.3.0](https://modal.com/docs/reference/changelog#130-2025-12-19))

**How Ramp built Inspect, their internal coding agent, on Modal**

Each Inspect session runs in a sandbox on Modal with a full dev environment, instant startup, filesystem snapshots, and unlimited concurrency. It’s now used to write ~30% of Ramp’s production PRs across frontend and backend, without tying up developer laptops.

Read the[ full breakdown](https://builders.ramp.com/post/why-we-built-our-background-agent) from Ramp.

**Run LLM inference at maximum performance**

In this deep dive, we break down the three major types of inference workloads we see in production today — offline, online, and semi-online — and explain how their performance and cost tradeoffs differ. We share concrete recommendations for engines like vLLM and SGLang, real-world examples from teams running at scale, and how to architect each workload efficiently on Modal.

[Read the full post](https://modal.com/llm-almanac/workloads) or [join our virtual event](https://watch.getcontrast.io/register/high-performance-llm-inference-in-production) to learn more.

**Keeping 20,000+ GPUs healthy at scale**

Modal runs a globally distributed GPU fleet across all major clouds, launching millions of instances and managing over 20,000 concurrent GPUs. In this post, we share how we test instance types, prepare machine images, continuously health-check GPUs, and monitor reliability at scale — plus lessons learned from operating at the edge of GPU failure modes.

Check out the [full post](https://modal.com/blog/gpu-health).

**Modal IRL this February**

We’re hosting a packed month of events across NYC and SF — from reinforcement learning meetups and AI leader breakfasts to startup office hours and biotech mixers. If you’re around, come join us. Here are a few highlights:

[Cafe Compute](https://luma.com/cafecomputenyc26): Feb 12 | New York[FDEs in AI with Modal and Snowflake](https://luma.com/yd4wv75q): Feb 18 | San Francisco[Modal for Startups office hours](https://luma.com/sj8c5lrq): Feb 23 | San Francisco

[See the full list](https://luma.com/modal-labs?k=c) of everything coming up.