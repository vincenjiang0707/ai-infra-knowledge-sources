source: https://github.com/orgs/community/discussions/163932

# Improved pull request "Files Changed" experience feedback #163932

## Replies: 3246 comments 1357 replies

|
I would like to be able to scroll through the Pull Request while the comment modal is open. Reason: When a comment is outdated, we need to look at the current version to check if it actually addresses the comment. I really love this feature! THANK YOU!!! |

|
Update: I just found out that it appears when there's enough space (1280px width). Here's the updated feedback. I'd like to see the branch name in the sticky header at all times so that I can easily copy it when I'm reviewing a PR. I wrote the following before thoroughly experimenting. I'd like to see the branch name when the sticky header is shown (i.e., when you've scrolled to the bottom). The reason is that when I'm reviewing a long PR and want to checkout the branch to continue reviewing it locally, I have to go back all the way up to see or copy the branch name and then go back to where I left off. |

|
I find the comment indicators in the sidebar really useful. It might also be useful to have them in the "diff file header." It's very useful when you've marked a file as "viewed" because you can see how many comments it has as you're scrolling without having to expand it. |

This is really cool. Is it also possible to seamlessly toggle hiding white spaces? If that's achievable without doing a refresh would be amazing. |

|
This is so much better, I might go back from reviewing with the VSCode extension now 🚀 I love the new alerts panel, unfortunately it looks like pressing Maybe we could have some grouping or clustering in the alerts panel in the future. |

|
I would love to see the file tree sorted alphabetically with folders on top, then files. It is quite jarring to have changed files in the middle of folders when viewing the file tree currently. Example of current state
Example of desired state
This would mirror how the majority of developers view the code in their IDE |

|
Hi, I would like to play around with this, but I'm not seeing the opt-in mentioned in
Am I missing something? |

|
Why is it not word wrapping based on screen dimensions on diff? I have to scroll horizontally. |

|
When reviewing a PR I want to look only at source files, that aren't tests.
|

|
Why are we unable to add a PR comment to an |

|
Could there be a setting to let users always use single-file view, even for small PRs please? It's excellent for ticking off viewed files. The scroll has always been frustratingly buggy/jumpy in multi-file view for anything beyond a few small files. |

|
Image diffs are not loading reliably, I have to jump back to the classic experience any time I need to do image diffing (which is often) |

|
This is my first ever comment on a community discussion, and i am still a beginner to github and the tech community surround me.I like the new design. It feels easier to review changes, especially with the comments being saved and the improved file navigation. It would be nice to have an even easier way to move between files in bigger pull requests.i would love to collaborate with open source contributors . Thanks |

|
This has been removed? |

|
I have to scroll all the way to the top to go back to the PR description. |

|
When reviewing and clicking on the checkbox to be seen/reviewed, I like the tree structure to show the files in bold font or normal font based on whether it's been reviewed or not. Otherwise, it's a lot of scrolling for me. |

|
Diffs hijack the |

|
Can you stop hijacking all the scripts I've been doing to remove the clutter? |

|
When viewing a single patch, I would like a single button to click to go to the next patch in the PR. Then I can review commit-by-commit, exactly the way the author intends. The current UI requires 4-5 clicks to try to just navigate to the next patch in the series. For larger patch series in a PR, this makes it tedious to navigate through the changes one by one. |

## Uh oh!

There was an error while loading. Please reload this page.

## Uh oh!

There was an error while loading. Please reload this page.

## About the new experience

This updated experience focuses on performance, accessibility, and user productivity. Read more in the changelog.

Tip

If you are not already using the new experience, click the

✨Try the new experiencein the upper-right corner of the classic "Files changed" page. You can easily switch back from thePreviewmenu.## ✨ What's new

If you are coming from the classic experience, the new experience should feel familiar but adds some significant improvements:

Comment on any line:You can now comment on any line of a changed file, not just the lines surrounding a change.View the description without switching pages:You can now view the pull request description from the new Overview panel on the "Files changed" page.Reviewing made easierEnhanced file tree:The file tree is now resizable with indicators showing the files with comments, errors, and warnings.Review your pending comments:Pending comments are now shown in the review submission panel, so you can double-check your feedback before submitting.Draft comments:New comments and replies are saved locally so you won't lose them if you accidentally close your browser or refresh the page.Fewer page reloads:ClickingRefreshto pull in new changes, switching between split and unified modes, and other tasks will no longer force a full page refresh.Accessibility & readability:Keyboard navigation, screen reader landmarks, and increased line spacing options are now available to make the experience available to everyone.## ✨ Updates

See what's been fixed and improved since the launch of the public preview:

## 🟡 Limitations

As of the initial public preview release, there are some

temporary limitationsthat will be addressed over time:While our previous experience had hard limits on large PRs, this new experience is being built to scale. That said, we’re increasing our limits incrementally. To start with, our additional current limitations are:

## How you can help

Thanks for helping us build a better review experience—we read every comment!

## All reactions