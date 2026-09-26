source: https://github.com/vllm-project/guidellm/actions/runs/35942843175/workflow

# fix: load SQLite dataset files through a database connection #2390

#### Workflow file for this run

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)| name: PR Styling | ||
|
Check warning on line 1 in .github/workflows/pr-styling.yml ## GitHub Actions / PR StylingWorkflow execution policy warning (evaluate mode)
|
||
| on: | ||
| # This has to be pull_request_target since its editing but | ||
| # that means the the version from main runs not the PR's | ||
| pull_request_target: | ||
| types: [opened, synchronize, reopened, edited] | ||
| permissions: | ||
| contents: read | ||
| pull-requests: write | ||
| concurrency: | ||
| group: pr-description-${{ github.event.pull_request.number }} | ||
| cancel-in-progress: true | ||
| jobs: | ||
| update-description: | ||
| runs-on: ubuntu-slim | ||
| steps: | ||
| - name: Checkout code | ||
| uses: actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1 # v7.0.1 | ||
| with: | ||
| fetch-depth: 0 | ||
| - name: Skip dependabot PRs | ||
| if: github.actor == 'dependabot[bot]' | ||
| run: echo "Skipping PR styling for dependabot PRs" | ||
| - name: Update PR description | ||
| if: github.actor != 'dependabot[bot]' | ||
| env: | ||
| GH_TOKEN: ${{ github.token }} | ||
| PR_NUMBER: ${{ github.event.pull_request.number }} | ||
| PR_BASE_REF: ${{ github.event.pull_request.base.ref }} | ||
| PR_HEAD_SHA: ${{ github.event.pull_request.head.sha }} | ||
| run: | | ||
| # Fetch the PR branch since we are on base repo | ||
| # NOTE: DO NOT checkout the branch | ||
| git fetch origin "refs/pull/${PR_NUMBER}/head" | ||
| CURRENT_BODY="$(gh pr view "$PR_NUMBER" --json body -q .body)" | ||
| NEW_BODY_FILE="$(mktemp)" | ||
| printf '%s' "$CURRENT_BODY" \ | ||
| | ./scripts/format_pr.sh "origin/$PR_BASE_REF" "$PR_HEAD_SHA" \ | ||
| > "$NEW_BODY_FILE" | ||
| NEW_BODY="$(cat "$NEW_BODY_FILE")" | ||
| if [ "$CURRENT_BODY" = "$NEW_BODY" ]; then | ||
| echo "PR body is already up to date, skipping update." | ||
| rm -f "$NEW_BODY_FILE" | ||
| exit 0 | ||
| fi | ||
| gh pr edit "$PR_NUMBER" --body-file "$NEW_BODY_FILE" | ||
| rm -f "$NEW_BODY_FILE" |