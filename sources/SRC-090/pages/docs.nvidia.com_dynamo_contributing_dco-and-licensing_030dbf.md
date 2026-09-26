source: https://docs.nvidia.com/dynamo/contributing/dco-and-licensing
lastmod: 2026-09-24T19:58:16.636Z

# DCO and Licensing

Dynamo requires every commit to include a Developer Certificate of Origin (DCO) sign-off. The
sign-off certifies that you have the right to submit the contribution under the project’s
[Apache 2.0 License](https://github.com/ai-dynamo/dynamo/blob/v1.4.2/LICENSE).

## Create a Signed-off Commit

Configure your Git identity with the name and email you intend to use:

Add the sign-off trailer with `git commit -s`

:

The resulting commit message ends with:

Use your real name. The trailer’s name and email must match the commit author identity.

## Verify the Latest Commit

Display the complete commit message:

Confirm that it contains the expected `Signed-off-by`

line.

## Verify Every Commit

Check all commits on your branch relative to upstream `main`

:

Each listed commit must have a sign-off trailer.

## Repair the Latest Commit

If only the latest commit is missing its sign-off, amend it:

Amending changes the commit SHA. Use `--force-with-lease`

, not `--force`

, when updating a published
branch.

## Repair Multiple Commits

Start an interactive rebase that includes the unsigned commits:

Mark each unsigned commit as `edit`

. For each stop, run:

After the rebase, verify every commit again, then update the remote branch:

For additional recovery options, see the repository’s
[DCO troubleshooting guide](https://github.com/ai-dynamo/dynamo/blob/v1.4.2/DCO.md).

## Licensing

By contributing, you agree that your contribution is licensed under the
[Apache 2.0 License](https://github.com/ai-dynamo/dynamo/blob/v1.4.2/LICENSE). All participation is
also governed by the
[Code of Conduct](https://github.com/ai-dynamo/dynamo/blob/v1.4.2/CODE_OF_CONDUCT.md).