source: https://github.com/vllm-project/guidellm/discussions/273

#
`--rate-type=sweep`

does not load vllm with expected count of requests
#273

[Answered](https://github.com#discussioncomment-14076460)by

[sjmonson](https://github.com/sjmonson)

[psydok](https://github.com/psydok)asked this question in

[User Support](https://github.com/vllm-project/guidellm/discussions/categories/user-support)

|
|

[sjmonson](https://github.com/sjmonson)

Aug 11, 2025

## Replies: 1 comment 2 replies

|
For the row you highlighted in the first screenshot, first keep these things in mind:
Start at the beginning of the test, the number of running requests increases by one every two seconds (1). The first request finishes after 25.4 seconds. At this point, new requests are still being added at a rate of 0.5 per second, while finished requests begin to decrease at the same rate (assuming every request takes the same amount of time). In that first 25.4 seconds One of the other things that is confusing is there is input requests per second and output requests per second (responses per second). For GuideLLM the number reported as |

[psydok](https://github.com/psydok)

For the row you highlighted in the first screenshot, first keep these things in mind:

`constant@0.5`

:= Send 0.5 requests every second so every 2 seconds send a new request`25.40 Lat`

:= Each request takes on average 25.4 seconds to completeStart at the beginning of the test, the number of running requests increases by one every two seconds (1). The first request finishes after 25.4 seconds. At this point, new requests are still being added at a rate of 0.5 per second, while finished requests begin to decrease at the same rate (assuming every request takes the same amount of time). In that first 25.4 seconds

`25.4/2 ~= 12`

requests were started. Assuming neither the rate of requests nor the…