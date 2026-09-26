# [Issue #309] Bake HTML dependencies into report

source: https://github.com/vllm-project/guidellm/issues/309
state: closed | updated: 2026-06-10T14:56:28Z
labels: priority-medium, internal

## 正文

**Is your feature request related to a problem? Please describe.**
The HTML report relies on hosted code to render. This can cause older reports to break when changes are made to the template. See also #303.

**Describe the solution you'd like**
Bake all external dependencies into the HTML file or export them as an archive.

**Additional context**

Broken report due to missing js and manifest:

<img width="1906" height="709" alt="Image" src="https://github.com/user-attachments/assets/81d7aacc-a9da-4023-bba8-b57b92a02311" />

## 评论 (6)

### DaltheCow · 2025-09-09

@sjmonson Just posted a reply here with my thoughts on a simple solution: https://github.com/vllm-project/guidellm/issues/303#issuecomment-3271457680

If we don't go with my proposed solution and leave the default build as ui/latest then I do think it would be necessary to find some way to export and manage the html as an archive. I don't think jamming all of the dependencies into the html would be a viable solution although it is probably possible. The archive route seems tricky but more doable. If we save the whole hosted build as an archive, I guess I would need some script to write over the old hosted asset paths wherever they're used in all of the files and swap them with a localhost asset path. But I think that would require extra steps since the html would no longer function unless the user opted to host the archived build locally.

I guess we could opt for both solutions, maybe there is some benefit to having an archive, definitely would take more time to set up though.

Another issue I've been dealing with that is sort of related, is that whenever I push fixes, anyone using the default pathway won't get the benefit of those fixes until a new version is released, which should be the expected behavior for anyone using the last build image I suppose (I've been bypassing this by pushing up builds with the fixes as ui/latest, but that would likely have been breaking old html reports, so I won't be doing that anymore). But for anyone running guidellm locally, they probably want it reference main, but unless you manually update the guidellm env var to be dev, then you wouldn't get the latest since it defaults to using prod which is the release build. I don't have versioned dev builds, but if the user did updated the guidellm env variable to dev then whenever the dev build was updated via a push to main, their html report would break.

I guess I could have versioned builds be the default for prod staging and dev, and then recommend anyone trying to run the latest to run `export GUIDELLM__ENV=dev` before.

Does that seem like a good solution? Whenever a new build is created, always update the reference in config.py to use a versioned build for prod/staging/dev, probably not directly, but through an env file or some other means.

### markurtz · 2025-09-18

Adding in here that the desired pathway here was release management for the UI flows. The UI dependencies should be referencing versioned URLs and that should be incrementing semantically so we avoid old reports breaking 

### jaredoconnell · 2025-09-18

Embedding all HTML dependencies will also have the advantage of allowing older HTML reports to work, whereas there is a risk of the schemas changing and breaking older reports.

I have found the dependency on the hosted HTML mildly bothersome.

### hassanai71 · 2026-05-11

How can I resolve the CORB error I'm encountering in my browser? Is there any workaround?

### jaredoconnell · 2026-05-27

> How can I resolve the CORB error I'm encountering in my browser? Is there any workaround?

That problem is now fixed in main thanks to #744 
But that is a separate problem from this issue. But once this issue is implemented, the HTML report will be less fragile.

### dbutenhof · 2026-06-08

Not planned
