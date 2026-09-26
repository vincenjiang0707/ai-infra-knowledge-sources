# [Issue #2481] [Bug :bug:]: lint-dockerfile-envvars.py never checks scripts invoked on RUN continuation lines

source: https://github.com/llm-d/llm-d/issues/2481
state: open | updated: 2026-09-12T11:31:26Z
labels: 

## 正文

### What happened?

`scripts/lint-dockerfile-envvars.py` (pre-commit hook `lint-dockerfile-envvars`, run in the CI `pre-commit` job) is supposed to verify that every var in a script's `# Required environment variables:` header is declared as `ARG`/`ENV` in the Dockerfile stage that runs it.

`find_script_runs` only regex-scans the line that literally starts with `RUN`. `DockerfileParser.parse` in the same file joins `\` continuations; `find_script_runs` does not. Almost every script in `docker/Dockerfile.cuda` is invoked as

    RUN --mount=type=cache,target=/var/cache/dnf \
        /tmp/install-base-packages.sh && \
        rm -f /tmp/install-base-packages.sh

so the script path is on the second line and is never seen.

On `main` (f97c2c5b) the linter sees 2 of the 12 script invocations in `Dockerfile.cuda` (`install-runtime-packages.sh`, `package-utils.sh`). The other 10 are unchecked.

Expected: every script invoked by a `RUN`, including on continuation lines, is checked.

Once continuations are joined, the linter reports one real finding: `build-gdrcopy.sh` lists `GDRCOPY_PREFIX` as required, but the script has hardcoded `PREFIX=/usr/local` since #391 and no Dockerfile declares it. It also reports `UCCL_DEVICE` from `build-uccl.sh`, which is the Optional-block false positive already fixed in #2416.

This is the `find_script_runs` follow-up discussed in #2416.

Related: #2445 also edits `find_script_runs` (inline `VAR=x /script.sh` assignments) but still scans line by line, so it does not cover this. The two changes are independent; whichever lands second needs a trivial rebase.

### Version

main (f97c2c5b)

### Area

CI/CD

### Relevant log output

    $ python3 - <<'EOF'
    import importlib.util, pathlib
    spec = importlib.util.spec_from_file_location("l", "scripts/lint-dockerfile-envvars.py")
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    print(sorted({r[1] for r in m.find_script_runs(pathlib.Path("docker/Dockerfile.cuda").read_text())}))
    EOF
    ['install-runtime-packages.sh', 'package-utils.sh']


## 评论 (1)

### malamsyah · 2026-09-12

/assign
