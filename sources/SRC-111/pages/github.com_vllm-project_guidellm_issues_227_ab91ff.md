source: https://github.com/vllm-project/guidellm/issues/227

As it stands, when run with multiple values to the rate parameter, there is nothing written to disk until the end of all the rates. This causes a potential for loss of all results when the higher concurrencies might potentially run into some error. Some checkpointing to the disk would greatly improve the usability of the tool when running into potential errors.

The following is another scenario that we regularly encounter

- We run a list of concurrencies.
- We observe KV Cache depletion on the server side.
- The latter(higher) concurrencies are of no real use. The user cannot choose to end the run. The runs have to complete to get any usable results.

As it stands, when run with multiple values to the rate parameter, there is nothing written to disk until the end of all the rates. This causes a potential for loss of all results when the higher concurrencies might potentially run into some error. Some checkpointing to the disk would greatly improve the usability of the tool when running into potential errors.

The following is another scenario that we regularly encounter