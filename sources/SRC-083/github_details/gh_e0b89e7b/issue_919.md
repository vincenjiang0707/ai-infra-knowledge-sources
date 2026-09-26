# [Issue #919] Noisy logs

source: https://github.com/bitsandbytes-foundation/bitsandbytes/issues/919
state: closed | updated: 2026-03-02T15:22:45Z
labels: Enhancement, Medium Priority, Contributions Welcome, Low Risk

## 正文

This library is quite noisy in the logs that it outputs simply from importing `bitsandbytes` somewhere. it would be great if all the print statements could be switched to proper logs so that downstream users can decided how to handle those logs, and filter them out if they so choose. Thanks!

## 评论 (2)

### younesbelkada · 2023-12-18

Thanks for the suggestion ! Do you have any pointers / suggestions on how we could proceed for this? 

### dakinggg · 2023-12-18

The general idea is that python libraries should never really use `print`, but rather `log = logging.getLogger(__name__)` and then `log.info` or `log.debug`, etc. That allows downstream users to control how those logs are handled.

See e.g. https://stackoverflow.com/questions/27016870/how-should-logging-be-used-in-a-python-package
