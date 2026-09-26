# [Issue #5] [Feature]: Stream info service

source: https://github.com/ROCm/rocprofiler-sdk/issues/5
state: closed | updated: 2025-08-01T11:58:28Z
labels: Under Investigation, Feature Request

## 正文

### Suggestion Description

Documenting prior discussion with @jrmadsen :

It would be useful to have a callback service providing tools with information about stream creation/deletion/migration if applicable events. Data that we'd like to record in Score-P:

* Which agent is this stream associated with?
* What are its creation parameters, implicit or explicit? (Priority and synchronous/async are the big two.)
* What HSA queue is this stream associated with?
* (Updates if that queue changes)
* Stream deletion

This then lets us maintain a mapping of streams to agents, rather than streams to devices and devices to agents, and gets rid of a bunch of places where we currently need to query the HIP API from tool code.

### Operating System

_No response_

### GPU

_No response_

### ROCm Component

rocprofiler-sdk

## 评论 (8)

### wrwilliams · 2024-04-30

Additional notes on HIP/SMI calls that we want to be able to avoid in Score-P:

* looking up the device (agent) based on the memory properties of a HIP allocation: can we get malloc/free events with an associated agent?
* looking up the SMI-reported UUID of a device: can this get added to the agent info?
* Agents should have HIP device numbers added; users expect to be able to see `device:stream` style information describing GPU execution and right now trying to map agent IDs to the HIP layer is messy.

So two services and two extra agent fields would solve a bunch of problems for us.

### wrwilliams · 2024-10-10

Update as I've proceeded with implementation:

It is not nice, but probably adequate, for us to assume that any "hipCreateStream*" function will, in fact, create a stream, and that the "stream" parameter will be an outparam containing that stream. We can then take advantage of the nesting of API function callbacks and the events they cause (kernel launch, memcpy, etc) to push the stream as part of an external correlation in the HIP API enter callback and use said stream when handling those kernel/memcpy records that currently only have queues.

Would still be nice to have a `kind=STREAM_MANAGEMENT`, `operation=CREATE,DESTROY` record with details like:
```
typedef struct {
    rocprofiler_hip_stream_t stream;
    rocprofiler_agent_t agent;
    uint64_t flags; // include something here for is_null_stream, as well as the user-provided flags?
    int priority;
} rocprofiler_stream_event_record;
```
and to additionally see a `rocprofiler_hip_stream_t` added for any non-API records that, semantically, are associated with some stream (null if device-synchronous/purely a CPU event). But as noted I can work around that if it's not practical to provide such a field.

### jrmadsen · 2025-05-01

@wrwilliams we have implemented this service, feel free to close this ticket if you are satisfied . 

### wrwilliams · 2025-06-19

Per conversation with @jrmadsen in 18JUN25 telco, updating with a requested tweak:

The first point with the current interface where we can associate a stream with its rocprofiler agent is when we receive a buffer interface event for something that happened on that stream. This gives us a gap where streams have been created but are not fully initialized in Score-P. It would be safer for stream creation events to provide the associated agent, assuming this is possible.

Failing that, we could fall back on intercepting get/set device calls, *if* there were some way to pass a device number to `rocprofiler-sdk` and get an agent struct back...

### wrwilliams · 2025-06-24

A further note: I'm not sure if this is WAI or not, but the SET_STREAM callbacks are delivered with an internal CID of 0, rather than the CID of the stream-based kernel launch/malloc/memcpy that triggered them. I can work around this easily (we already have our own TLS in Score-P), but it does mean I can't directly create and push an external CID during a SET_STREAM, as I need that internal CID in order to find the correct external for retirement.

### wrwilliams · 2025-06-25

Unexpected behavior: `hipStreamSynchronize` does not appear to be delivering STREAM_SET events. Is this intended?

### darren-amd · 2025-07-24

Hi @wrwilliams,

I had a chat with the team and was informed that the issue has been resolved. Can this ticket be closed? 

### wrwilliams · 2025-08-01

> Hi [@wrwilliams](https://github.com/wrwilliams),
> 
> I had a chat with the team and was informed that the issue has been resolved. Can this ticket be closed?

I think so, given that an agent/device service would be separate.
