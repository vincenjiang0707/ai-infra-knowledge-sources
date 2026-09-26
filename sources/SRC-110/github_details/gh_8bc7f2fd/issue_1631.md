# [Issue #1631] Followup to #1629: CICD Improvements

source: https://github.com/modelscope/evalscope/issues/1631
state: open | updated: 2026-09-01T15:00:56Z
labels: 

## 正文

## Summary

#1629 proposes the migration to `ruff`. This issue document possible improvements that enhances the CICD workflow (mostly `pre-commit`).

Since CICD causes a lot of file updates, I will leave all changes to maintainers and only propose ways to improve. (I found issue > PR, due to a lot of conflicts and merges.)

## Linting

- [x] I ([isort](https://docs.astral.sh/ruff/rules/#isort-i))
- [x] E ([pydocstyle error](https://docs.astral.sh/ruff/rules/#pycodestyle-e-w))
- [x] W ([pydocstyle warning](https://docs.astral.sh/ruff/rules/#pycodestyle-e-w))
- [x] ~~B ([flake8-bugbear](https://docs.astral.sh/ruff/rules/#flake8-bugbear-b))~~
- [x] ~~Q ([flake8-quotes](https://docs.astral.sh/ruff/rules/#flake8-quotes-q))~~
- [ ] UP ([pyupgrade](https://docs.astral.sh/ruff/rules/#pyupgrade-up))
- [ ] SIM ([flake8-simplify](https://docs.astral.sh/ruff/rules/#flake8-simplify-sim))
- [x] remove flake8 from pre-commit hook
- [ ] F401 in `evalscope`
- [ ] E/F/W rules in `tests`

## Formatting

- [x] add ruff-format and remove yapf in pre-commit hook (example: https://github.com/vllm-project/vllm/pull/26247)

## Why do we need migration?

In addition to discussion #1629, ruff brings a faster, unified lint+format experience, as flake8 and yapf may conflict, an example:

```py
match var:
    # some comments here
    case 1:
        pass
```

flake8 will always format as above, while yapf will always format as below. This makes `make lint` never pass.

```py
match var:
# some comments here
    case 1:
        pass
```

## 评论 (1)

### Moenupa · 2026-08-31

@Yunnglin please consider reopening this issue.

I believe some of the rules in `ignore = ["E501", "E741", "F401", "F403", "F405", "F541"]` are useful and reduce runtime. I noticed a lot of unused imports and other issues picked up by these rules.

Also, we can gradually enforce lint/format in tests to standardize code style.
