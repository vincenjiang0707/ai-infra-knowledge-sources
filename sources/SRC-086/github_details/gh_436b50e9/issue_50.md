# [Issue #50] Install the package with the console script ?

source: https://github.com/FasterDecoding/Medusa/issues/50
state: closed | updated: 2024-01-24T14:06:13Z
labels: 

## 正文

Setuptools can inherently create a console script from the `pyproject.toml`, and users can use

```shell
medusa --model path/to/model
```
`medusa` as the CLI name may clash with other eariler CLIs for any other tools though, so I'd suggest to make the name of the CLI sth like `medusa-llm`.

## 评论 (1)

### ctlllll · 2024-01-24

Thanks for the suggestion! We currently don't have a plan to enable the CLI name as this is a more research-oriented project rather than a battle-test product :)
