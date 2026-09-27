# [Issue #191] AWQ and VILA dependency compatible issue

source: https://github.com/mit-han-lab/llm-awq/issues/191
state: open | updated: 2024-12-18T01:36:10Z
labels: 

## 正文

Hi Team,
I encountered some issues while trying to run AWQ and VILA. It appears that the dependencies for these two projects, based on the latest commits, have conflicts and compatibility issues. Specifically, AWQ seems to use older dependencies compared to VILA.
I would suggest moving to a Docker container and building these projects via Docker images. This approach is likely to help us avoid such dependency conflicts in the future.

Please advise on the best way to proceed.

Thank you for your consideration.

## 评论 (4)

### mfriedman-pr · 2024-06-11

Seconding this. Running the instructions as posted leads to installation problems.

### HariSeldon11988 · 2024-06-26

Can confirm this. VILA and AWQ have some dependencies issues if following installation instructions. Has someone found a solution yet?

### mattam301 · 2024-08-21

I encountered the same problem, the installation of VILA now need updating

### mit10000 · 2024-12-18

docker is 1 million time better than conda. Just provide a docker image, everything is done.
