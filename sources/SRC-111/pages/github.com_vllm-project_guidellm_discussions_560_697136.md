source: https://github.com/vllm-project/guidellm/discussions/560

## Replies: 1 comment

|
If you want something nearly identical to the previous synthetic dataset behavior, I suggest taking a look at |

0 replies

|
If you want something nearly identical to the previous synthetic dataset behavior, I suggest taking a look at |

## Uh oh!

There was an error while loading. Please reload this page.

I'd like to ask the current and intended behavior regarding the

`source`

parameter for synthetic datasets:QuestionThe documentation accepts a

`source`

parameter, meaning that synthetic prompts can be generated based on custom source text (file or URL). However, in guidellm 0.5.x, the prompt generation for synthetic datasets only uses the Faker library, and the`source`

parameter appears to be ignored.`source`

?Additional context`_create_prompt`

method (`src/guidellm/data/deserializers/synthetic.py`

) does not use`config.source`

at all.`src/guidellm/utils/text.py`

contains an`EndlessTextCreator`

class that appears designed for this purpose.`TestSyntheticDatasetConfig`

(`tests/unit/data/deserializers/test_synthetic.py`

), the source param is present.Would appreciate clarification on:`source`

parameter as a text source for synthetic prompts intended? If not a feature anymore, would a PR to restore/implement this be welcome?Thanks for your input 😊

## All reactions