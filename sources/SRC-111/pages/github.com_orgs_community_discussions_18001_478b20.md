source: https://github.com/orgs/community/discussions/18001

# Hide Jobs in Actions UI when If is false #18001

[glloydcorecard](https://github.com/glloydcorecard)asked this question in

[Actions](https://github.com/orgs/community/discussions/categories/actions)

## Replies: 82 comments 13 replies

|
This is really desirable!! |

|
The default behavior should be that skipped jobs are hidden. If someone wants to see the skipped jobs, let them optionally enable that. |

|
Whenever this is implemented, Please make it optional. |

|
The default behaviour should be rather that skipped jobs are shown. It would be less of a breaking change to introduce a new job option |

|
Any update on this? I'd still very much like to hide skipped actions on PR's in the UI. |

|
Bump! Also adding a use-case for this feature. I am using "proxy workflows" as a workaround for a lack of dynamic "uses" when triggering reusable workflows (choosing which to execute). I am using a solution similar to The problem is that every use of the "proxy workflow" results in skipped jobs showing up due to the A job-level setting or even a UI setting would be helpful in making this a better experience. Thank you! |

|
Maybe an easier/less invasive option would be to extend the ```
java-build:
name: java-build
needs:
- metaconfig # job
- ${{ jobs.metaconfig.result == 'success' }} # job result
``` This would effectively hide the skipped jobs but would require an evaluation of boolean as well as a job_ids in the |

|
We also make heavy use of shared workflows with switches to turn workflow features on and off. I'd love to see this feature added. As a workaround, we use the following pattern which allows some ability to distinguish between a step not being enabled, and it being skipped for other reasons.
One note is that if you use a step outcome/output in place of the enable input here, it will still work. But the formatted string will not be evaluated until the job completes. While the job is running, the code that generates the name will be displayed. |

|
I would like to +1. In my case I have a reusable workflow inside a matrix, and one of the job of the reusable workflow should run only in some cases, after other jobs in the reusable workflow. A job-level setting would be great to hide those that don't run. |

|
+1. Definitely a needed enhancement to GitHub Actions UI. At least have a UI option to hide skipped jobs. |

|
+1 it would be great the have the option! |

|
+1 Bumping up, would love to see this feature! |

|
+1 |

|
+1 |

|
+1, would be very cool if we could hide skipped jobs! |

|
+1 |

|
+1 |

|
+1 |

|
+1 |

|
+1 |

|
👋 Hey folks! I created a userscript that hides skipped jobs in the actions UI. I've been using it for well over a year (don't let the commit date fool you, I just cleaned up my local code and made the repo public) to my enjoyment. ⚙️ Give it a try, and feel free to suggest any improvements (PRs or otherwise) in the repo itself! Best, |

|
+1 |

|
+1 !! |

|
The more I use GitHub Actions the more basic features I find are missing. Showing jobs that are conditionally skipped is such a bad design decision. It makes designing reusable workflows a mess. I should not have to maintain separate workflows with different jobs just cause I want to hide something from the UI. I have hundreds of repos I need to do CICD from and l want to use 1 centralized reusable workflow that everything is nested under. This way I can decouple jobs into independent reusable workflows nested in a root workflow. So all my repos just have to reference 1 main reusable workflow that conditionally runs jobs depending on that projects needs. |

|
It's almost like Microsoft bought Github so they can reduce the support to nothing so that people switch to something else. |

|
+1 |

|
Bump, I mean seriously, it's just a hide skip flows, why not just implement it and closed this topic :( |

## Uh oh!

There was an error while loading. Please reload this page.

At time of writing this when you have a multi-stage workflow defined it will show every single job and set of steps defined in all associated workflows and composite actions. Having the ability to hide a job in the UI if it will not be ran would be a great feature.

Examples of this are build testing, integration testing, code scanning, and security scanning. There are times when they will not be ran and having them show up in the UI really clutters it up.

Current Workflow Example Below in the UI

Current Workflow Example Below in the UI

## All reactions