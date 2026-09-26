source: https://github.com/vllm-project/guidellm/issues/97

The INFO log level is way to verbose about the inner config of objects. We should push many of the messages to higher log levels and/or rewrite some messages to be less verbose.

Here is a proposal for what we could focus on in each log level:

`ERROR`

: Anything that leads to complete failure of the test
`WARNING`

: Things might be going wrong, or not happening in the expected way
- Requests erroring
- Concurrency saturated

`INFO`

: Things that should be happening that help explain the state
- Info about run configuration, dataset...
- What RPS settings are calculated in the sweep
- Infrequent status updates
- Info about output calculations / files that its dumped to

`DEBUG`

: Stuff like prompts and results
`TRACE`

: token-level events from the requests

The INFO log level is way to verbose about the inner config of objects. We should push many of the messages to higher log levels and/or rewrite some messages to be less verbose.

Here is a proposal for what we could focus on in each log level:

`ERROR`

: Anything that leads to complete failure of the test`WARNING`

: Things might be going wrong, or not happening in the expected way`INFO`

: Things that should be happening that help explain the state`DEBUG`

: Stuff like prompts and results`TRACE`

: token-level events from the requests