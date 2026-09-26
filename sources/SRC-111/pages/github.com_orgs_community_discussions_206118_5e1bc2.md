source: https://github.com/orgs/community/discussions/206118

# Codespace stuck - 500 then 400 error on start, export also failing, contains uncommitted work #206118

[vivekludhani-web](https://github.com/vivekludhani-web)asked this question in

[Codespaces](https://github.com/orgs/community/discussions/categories/codespaces)

## Replies: 4 comments

|
Thank you for taking the time to share your insights with us! Your feedback is invaluable as we build a better GitHub experience for all our users.
As a member of the GitHub community, your participation is essential. While we can't promise that every suggestion will be implemented, we want to emphasize that your feedback is instrumental in guiding our decisions and priorities. Thank you once again for your contribution to making GitHub even better! We're grateful for your ongoing support and collaboration in shaping the future of our platform. ⭐ |

|
Update: I also tried using GitHub CLI (gh codespace ssh) directly from a terminal, bypassing the browser entirely. Got the exact same error: error starting codespace: HTTP 400: 39. I then tried "gh codespace cp" to copy files without starting the full session - same error again. This confirms the issue is server-side (the container itself cannot start), not a browser/client problem. |

|
I wouldn’t delete the codespace yet, since the uncommitted work may only exist there. Check GitHub Status for any ongoing Codespaces issue and keep trying the start/export options. If possible, contact GitHub Support again with the error code 39 and export failure details before recreating it. |

|
I’m seeing a very similar Codespaces recovery failure, with an additional API inconsistency that may help diagnose the backend issue. Codespace: curly-memory-jr4gr9pj5wp7c5w69 The Codespace still exists and reports Available, but the VS Code workbench fails with: The workbench failed to connect to the server (Error: exception was thrown by handler. exception: failed to start vs code remote server.) I have already tried browser access, gh codespace ssh, normal rebuild, full rebuild, and Export changes to a branch. None restored access. The export API is now in an inconsistent state: GET /user/codespaces/curly-memory-jr4gr9pj5wp7c5w69/exports/latest returns: state: failed But a new: POST /user/codespaces/curly-memory-jr4gr9pj5wp7c5w69/exports returns: 422 An export of that codespace is already in progress. GitHub Support also closed my recovery ticket because my account currently only has self-service support resources. The Codespace contains important unpublished files under /workspaces/acoes-codex, so I am not deleting it. This looks like a stuck export job or inconsistent Codespaces backend state. If anyone from GitHub can identify a workaround that preserves the existing /workspaces persistent storage, that would be very helpful. |

## Uh oh!

There was an error while loading. Please reload this page.

## 🏷️ Discussion Type

Bug

## Body

My codespace has been unable to start for over 24 hours, and I'm at risk of losing uncommitted work.

Codespace name: urban-fiesta-qv9rrjw46x6ph96r9 Repository: vivekludhani-web/trading-terminal (private)

Timeline of what happened:

Codespace stopped normally after inactivity, as usual.

On restart, it got stuck indefinitely at "Setting up remote connection: Starting codespace..."

After several hours, it started returning: 500 Unexpected token '<', "<!DOCTYPE "... is not valid JSON on https://api.github.com/user/codespaces/urban-fiesta-qv9rrjw46x6ph96r9/start

Later it changed to a 400 error (error code 39) on the same start endpoint.

I tried "Export changes to a branch" from the Codespaces dashboard as a way to at least recover the uncommitted files - this also failed with "Your codespace export did not complete. Please try again."

What I've already tried:

Restarting from github.com/codespaces (multiple times, different browsers, different networks)

Restart and reconnect button from the error page

Incognito/clearing cache

Different device

Waiting several hours between attempts

Contacting GitHub Support (ticket was closed - told only self-service resources are available for my account tier)

What I need: The codespace container has important uncommitted work that was never pushed to the repo. I'd really appreciate any guidance on:

Whether this is a known/ongoing issue

Any other way to recover the uncommitted files from a codespace that won't start or export

Whether deleting and recreating tends to resolve this, or if that's a bad idea while data is still uncommitted

Thanks in advance for any help.

Content

## All reactions