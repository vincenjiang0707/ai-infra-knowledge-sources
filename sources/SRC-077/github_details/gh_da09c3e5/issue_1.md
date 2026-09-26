# [Issue #1] Status updates

source: https://github.com/gpu-mode/kernelbot/issues/1
state: closed | updated: 2024-12-06T05:10:04Z
labels: 

## 正文

As of d17b626a8cfe7459be8ccb0a9d0c80ea29a3bb5c

Can trigger a github action that runs a script, puts logs in a github artifact and then posts the artifact results to stdout

```
(discord) ➜  discord-cluster-manager git:(main) python bot.py 
GitHub Action triggered successfully! Run ID: 11675205122
Monitoring progress...
Workflow still running... Status: queued
Live view: https://github.com/gpu-mode/discord-cluster-manager/actions/runs/11675205122

Workflow completed with status: success

Training Logs:
[5 7 9]


View the full run at: https://github.com/gpu-mode/discord-cluster-manager/actions/runs/11675205122
```

## 评论 (15)

### msaroufim · 2024-11-05

As of df3d3b308aba3e16256a8e1f738f3340c391ba7a

![image](https://github.com/user-attachments/assets/88ca4285-528d-433e-8ec0-29f7b7e95a6e)

```
(discord) ➜  discord-cluster-manager git:(main) python discord-bot.py
2024-11-04 17:47:37 - INFO - Environment variables loaded
2024-11-04 17:47:37 - INFO - Using GitHub repo: gpu-mode/discord-cluster-manager
2024-11-04 17:47:37 - INFO - Starting bot...
2024-11-04 17:47:37 INFO     discord.client logging in using static token
2024-11-04 17:47:37 - INFO - logging in using static token
2024-11-04 17:47:38 INFO     discord.gateway Shard ID None has connected to Gateway (Session ID: fda5d70f82bed675973eb8e910f2d9d9).
2024-11-04 17:47:38 - INFO - Shard ID None has connected to Gateway (Session ID: fda5d70f82bed675973eb8e910f2d9d9).
2024-11-04 17:47:40 - INFO - Logged in as Cluster-Bot#5007
2024-11-04 17:47:45 - INFO - Bot mentioned in message with 1 attachments
2024-11-04 17:47:45 - INFO - Processing attachment: train.py
2024-11-04 17:47:45 - INFO - Downloading train.py content
2024-11-04 17:47:46 - INFO - Successfully read train.py content
2024-11-04 17:47:46 - INFO - Attempting to trigger GitHub action
2024-11-04 17:47:46 - INFO - Looking for workflow 'train_workflow.yml' in repo gpu-mode/discord-cluster-manager
2024-11-04 17:47:46 - INFO - Found workflow, attempting to dispatch
2024-11-04 17:47:47 - INFO - Workflow dispatch result: True
2024-11-04 17:47:49 - INFO - Found 18 total runs
2024-11-04 17:47:49 - INFO - Checking run 11676018557 created at 2024-11-05 01:47:48+00:00
2024-11-04 17:47:49 - INFO - Found matching run with ID: 11676018557
2024-11-04 17:47:49 - INFO - Successfully triggered workflow with run ID: 11676018557
2024-11-04 17:47:50 - INFO - Starting to monitor workflow status for run 11676018557
2024-11-04 17:47:50 - INFO - Current status: queued
2024-11-04 17:48:21 - INFO - Current status: completed
2024-11-04 17:48:21 - INFO - Workflow completed, downloading artifacts
2024-11-04 17:48:21 - INFO - Attempting to download artifacts for run 11676018557
2024-11-04 17:48:22 - INFO - Found 1 artifacts
2024-11-04 17:48:23 - INFO - Found artifact: training-logs
2024-11-04 17:48:23 - INFO - Successfully downloaded artifact
```


### msaroufim · 2024-11-05

Threaded replies now work as of c1e2b1aaac9ed99b66640c9a57e1b9911e8a7c6d
![Screenshot 2024-11-05 at 10 35 25 AM](https://github.com/user-attachments/assets/b3d9514f-ece8-4a5b-a1d5-c714ab11fce3)


### msaroufim · 2024-11-05

Got caching of torch working

![Screenshot 2024-11-05 at 11 17 10 AM](https://github.com/user-attachments/assets/73a18bb7-d280-4e9e-9db1-f482776baf2a)

EDIT: Actually this didn't work lol, using cache takes as much time as not using the cache


### msaroufim · 2024-11-06

The bot is now always on, basically if you make an update to main then heroku will catch the changes and automatically redeploy 

I get emails if the bot ever crashes and otherwise can check the status here https://dashboard.heroku.com/apps/discord-cluster-manager

To repro

```
 1281  git checkout -b msaroufim/heroku
 1283  brew tap heroku/brew && brew install heroku
 1284  heroku login
 1285  heroku git:remote -a
 1286  heroku git:remote -a discord-cluster-manager
 1287  heroku config:set 
 1310  heroku logs --tail\n\n
 1312  heroku ps:scale worker=1
 1313  heroku ps
```

So testing just got significantly simpler

![Screenshot 2024-11-06 at 12 20 06 PM](https://github.com/user-attachments/assets/a85aa955-db50-4346-b235-54b75ac67863)

![Screenshot 2024-11-06 at 12 21 38 PM](https://github.com/user-attachments/assets/528b3826-e8fe-491a-8926-506dbe7448df)




### msaroufim · 2024-11-06

Server health can now be monitored here
![Screenshot 2024-11-06 at 12 33 27 PM](https://github.com/user-attachments/assets/5e2a8ac4-cfdf-461d-9e1a-8b121eca75e6)


### AndreSlavescu · 2024-11-09

Example leaderboard command usage:

```@Cluster-Bot leaderboard```

<img width="799" alt="image" src="https://github.com/user-attachments/assets/1ad61226-bf46-4cbd-bf41-0e154406a21e">


### msaroufim · 2024-11-11

can now queue gpu jobs to the AMD runner https://github.com/gpu-mode/discord-cluster-manager/pull/16

### msaroufim · 2024-11-12

NVIDIA jobs now working https://github.com/gpu-mode/discord-cluster-manager/pull/17

<img width="768" alt="Screenshot 2024-11-11 at 4 35 11 PM" src="https://github.com/user-attachments/assets/c561c7c1-fcb1-44b3-b544-403cf728ae90">


### msaroufim · 2024-11-12

Bot does not create a new message to then thread

<img width="612" alt="Screenshot 2024-11-11 at 5 31 05 PM" src="https://github.com/user-attachments/assets/9b8ece42-b310-4f2a-85fb-049952a91d68">


### msaroufim · 2024-11-18

Can now support arbitrary filenames and not just train.py
![Screenshot 2024-11-18 at 10 07 35 AM](https://github.com/user-attachments/assets/2cb70833-bf73-4e48-9f77-92baba2112aa)


### msaroufim · 2024-11-18

AMD runners now are connected

![Screenshot 2024-11-18 at 10 41 41 AM](https://github.com/user-attachments/assets/4b56e8aa-e540-43b8-8515-cbf792a22cf1)


### msaroufim · 2024-11-19

Modal scheduler is now merged https://github.com/gpu-mode/discord-cluster-manager/pull/25

Fastest scheduler we have so far for python jobs


![Screenshot 2024-11-18 at 6 40 25 PM](https://github.com/user-attachments/assets/b82ccd6f-3514-4249-9453-68a2171a8f83)


### msaroufim · 2024-11-19

Major update Slash commands now work and make usage instructions super seamless now

https://github.com/gpu-mode/discord-cluster-manager/pull/27

run github/modal/resync/ping

### msaroufim · 2024-11-21

Major refactor landed by @S1ro1 which modularizes our codebase - new commands or functionality can be split into seperate cogs and now accepting new contributions will be easier

### msaroufim · 2024-12-03

Closing this thread in favor of #6 
