# [Issue #1370] Clarification on unverified MLPerf Inference Power results

source: https://github.com/mlcommons/inference/issues/1370
state: closed | updated: 2026-05-14T00:45:44Z
labels: Stale

## 正文

Intel plans to measure MLPerf Inference Power benchmark results on Xeon and use the information in a whitepaper or collaterals as unverified results. The results will be mentioned as per rules [https://github.com/mlcommons/policies/blob/master/MLPerf_Results_Messaging_Guidelines.adoc#5-when-comparing-mlperf-results-you-must-identify-any-submission-differences](https://github.com/mlcommons/policies/blob/master/MLPerf_Results_Messaging_Guidelines.adoc#5-when-comparing-mlperf-results-you-must-identify-any-submission-differences) and [https://github.com/mlcommons/policies/blob/master/MLPerf_Results_Messaging_Guidelines.adoc#6-when-comparing-mlperf-results-use-official-mlperf-power-metrics](https://github.com/mlcommons/policies/blob/master/MLPerf_Results_Messaging_Guidelines.adoc#6-when-comparing-mlperf-results-use-official-mlperf-power-metrics )

## 评论 (6)

### rnaidu02 · 2023-05-08

@s-idgunji @tejus@mlcommons.org Based on the offline email communication, Power WG chairs wanted this to be discussed in Inference WG. Can you please confirm this so that Inference WG can make a recommendation.

### mrasquinha-g · 2023-05-09

Discussion was held on 5/9 and there are no objections from the inference WG.

### arjunsuresh · 2023-06-01

The timing of [result disclosures](https://github.com/mlcommons/policies/blob/master/MLPerf_Results_Messaging_Guidelines.adoc#7-timing-for-results-disclosures) mentions the following:

"Submitters (i.e., those who have submitted results for review and verification by MLCommons) are not allowed to publish any results for a given benchmark version before its official publication date."

Is this embargo applicable only from the date of submission? I mean currently can we publish unverified MLPerf power results until the submission date for 3.1? For most of our power results we are going to follow [manual range setting](https://github.com/mlcommons/power-dev/issues/296) which is not approved by the power WG chairs and so we have to publish them as unverified results. 

### DilipSequeira · 2023-06-02

The original intent of this rule was that results for a particular round cannot be made public prior to the official publication date.

(However, my understanding of the rules is that you can publish unverified versions of benchmarks from previous rounds – so if the benchmark is the same in 3.0 and 3.1, and you want to publish your results as “unverified 3.0” results, that’s OK.)

From: Arjun Suresh ***@***.***>
Sent: Thursday, June 1, 2023 4:02 PM
To: mlcommons/inference ***@***.***>
Cc: Subscribed ***@***.***>
Subject: Re: [mlcommons/inference] Clarification on unverified MLPerf Inference Power results (Issue #1370)


The timing of result disclosures<https://github.com/mlcommons/policies/blob/master/MLPerf_Results_Messaging_Guidelines.adoc#7-timing-for-results-disclosures> mentions the following:

"Submitters (i.e., those who have submitted results for review and verification by MLCommons) are not allowed to publish any results for a given benchmark version before its official publication date."

Is this embargo applicable only from the date of submission? I mean currently can we publish unverified MLPerf power results until the submission date for 3.1? For most of our power results we are going to follow manual range setting<https://github.com/mlcommons/power-dev/issues/296> which are not approved by the power WG and so we have to publish them as unverified results.

—
Reply to this email directly, view it on GitHub<https://github.com/mlcommons/inference/issues/1370#issuecomment-1572898257>, or unsubscribe<https://github.com/notifications/unsubscribe-auth/AB7AINAQ5O2WITNFSCNH2O3XJENOLANCNFSM6AAAAAAX2KOM2Y>.
You are receiving this because you are subscribed to this thread.Message ID: ***@***.******@***.***>>


### arjunsuresh · 2023-06-02

Thank you @DilipSequeira for confirming. Our intend is not to waste resources to do an unnecessary ranging mode run just to make the power results verified. Once more submitters try the large language models with power I expect some support for my proposal 🙂

### github-actions[bot] · 2026-05-14

🔒 This issue has been **automatically closed** because it has been open for more than 2 years with no activity.
If this is still relevant, you may **reopen it or create a new one**.
