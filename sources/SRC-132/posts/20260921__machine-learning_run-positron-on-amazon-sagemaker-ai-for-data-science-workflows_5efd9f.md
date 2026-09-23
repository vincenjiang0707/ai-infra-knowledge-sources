# Run Positron on Amazon SageMaker AI for data science workflows

source: https://aws.amazon.com/blogs/machine-learning/run-positron-on-amazon-sagemaker-ai-for-data-science-workflows/
published: Mon, 21 Sep 2026 16:34:21 +0000

[Artificial Intelligence](https://aws.amazon.com/blogs/machine-learning/)

# Run Positron on Amazon SageMaker AI for data science workflows

Data science teams often move among separate tools for governed data access, R analysis, Python model development, deployment, application development, and reporting. Positron, Posit’s integrated development environment (IDE) for data science, now runs on Amazon SageMaker AI.

For a data scientist, running Positron on SageMaker AI means:

**Data access without managing credentials.**Positron runs under the Space execution role, so you query Amazon Athena, the AWS Glue Data Catalog, and Amazon Simple Storage Service (Amazon S3) directly from the IDE. Access follows the role’s permissions, with no keys to store or rotate.**Compute that is ready when you are.**You launch a Space on the instance size you need, and teams can reserve capacity with SageMaker AI training plans so compute is available for scheduled training.**AI assistance that stays in your account.**Posit Assistant, Posit’s AI coding assistant, can use Amazon Bedrock as its model provider, so AI help runs on models in your own AWS account and AWS Region.**Room to work in parallel and together.**You can run multiple Spaces at once for independent projects, and use a shared Space so several people collaborate in the same Positron application.

Posit publishes a container image definition for Positron, built on the Amazon SageMaker Distribution image. Platform administrators build that image, push it to their own Amazon Elastic Container Registry (Amazon ECR) repository, register it with SageMaker AI, and attach it to a Studio domain. Data scientists then choose Positron when they create a Space and open the IDE directly in Studio.

This post shows how a data scientist experiences Positron in SageMaker AI, from exploring an Amazon Athena table to deploying a real-time endpoint.

# Solution overview

This walkthrough uses a synthetic 50,000-loan portfolio. Amazon S3 stores the source data, and the AWS Glue Data Catalog registers it. Amazon Athena queries the data, R validates features, and Python trains an XGBoost classifier. Shiny for Python invokes the endpoint, and Quarto records the workflow. The screenshots and metrics come from the captured run. The data does not represent a production lending system.

## Prerequisites

To follow this walkthrough, an organization needs:

- A Posit license grant and access to the Posit-published Positron image definition.
- Administrator permissions to manage Amazon ECR and configure custom images for the Amazon SageMaker Studio domain.
- A Space execution role with access to Amazon Athena and the AWS Glue Data Catalog.
- An Amazon S3 source location and a configured Athena query-results location.
- Amazon Bedrock model access in the same AWS Region as the Studio domain when using Posit Assistant, Posit’s AI coding assistant.
- An
`ml.t3.xlarge`

instance or larger for the demonstrated environment.

## Step 1: Positron in a SageMaker Studio Space

The run began with Positron in a SageMaker Studio Space. The project explorer, editor, R and Python sessions, Variables pane, plots, terminal, and application preview were available in one browser-based environment on SageMaker compute under the Space execution role.

## Step 2: Governed data discovery with Posit Assistant

From the same Space, Posit Assistant identified `credit_risk_blog.loan_tape_source`

in the AWS Glue Data Catalog and prepared a read-only Amazon Athena query. The query returned five sample rows across six fields, scanned 2.18 MiB, and completed in under one second.

## 2.1: Amazon Bedrock token and cache usage

Posit Assistant can use Amazon Bedrock as a model provider with AWS credentials and a configured AWS Region. No separate model-provider API key is required when Amazon Bedrock authentication resolves through the environment’s AWS credentials. Customer content is encrypted, isn’t used to improve base models, and isn’t shared with model providers ([see Amazon Bedrock data protection](https://docs.aws.amazon.com/bedrock/latest/userguide/data-protection.html)). Private connectivity can be configured with AWS PrivateLink.

The captured Session information view recorded 6,657,942 tokens, including 6,118,411 cache-read and 462,905 cache-write tokens, with an estimated cost of $6.319 and 92.5 percent cache efficiency, as shown in the following figure. Those values describe this session and the Assistant’s estimate. They aren’t an AWS invoice or a general cost benchmark. Cache behavior and pricing depend on the selected model and provider.

## Step 3: Data profiling in Amazon Athena

The workflow used an aggregate Athena query to examine row counts, identifier uniqueness, missing values, numeric ranges, and target validity. The results identified 50,000 loans, including 1,500 records with missing income and 1,015 defaults, for an overall default rate of 2.03 percent.

## Step 4: Interactive data exploration in R

The workflow loaded the 50,000-row table into the active R session and opened it in Data Explorer. R created debt-to-income and log-income features and displayed the debt-to-income distribution in the Plots pane. Excluding the 1,500 incomplete records left 48,500 loans for modeling and scoring.

## Step 5: Feature validation and Python model training

The validated feature definitions then moved into Python. An XGBoost classifier trained on a matrix containing 40,000 rows and three model features. The held-out evaluation produced an AUC of 0.834 and showed a 12.3 percent observed default rate in the highest-risk decile.

## Step 6: Managed deployment with SageMaker AI

The workflow wrote predicted probabilities and risk deciles for 48,500 loans to Parquet and registered the results as `credit_risk_blog.scored_loans`

in Athena. It then created a SageMaker AI model, endpoint configuration, and real-time endpoint. The endpoint reached `InService`

, and an invocation using a synthetic applicant payload succeeded.

## Step 7: Live inference with a Shiny for Python application

The project used a Shiny for Python application to invoke the deployed endpoint. The application accepted synthetic applicant information, applied the feature definitions used during training, and displayed the returned probability of default. The source code and running application remained in the same Positron project which runs behind the Amazon SageMaker Studio application proxy and is reachable only by users authenticated to the Space. It invokes the endpoint under the Space execution role rather than any stored key, and the role is limited to `sagemaker:InvokeEndpoint`

on the endpoint ARN.

## Step 8: Reproducible reporting with Quarto

The run concluded with a Quarto report that connected the Athena source, data-quality findings, R validation, Python model, scored output, SageMaker AI endpoint, and Shiny application. The report was generated directly from the project, preserving the workflow’s evidence and results in one reproducible document.

# Deployment architecture

The deployment involves two paths: an administrator path that builds and registers the custom Positron image, and a data science path that uses it to analyze data and deploy models.

### Administrative path

Positron runs as a custom image built on the Amazon SageMaker Distribution image in SageMaker AI. An administrator builds the Posit-published image definition, pushes it to a private Amazon Elastic Container Registry (Amazon ECR) repository in the Studio domain’s AWS Region, registers a SageMaker AI image and version, creates a JupyterLab app image configuration, verifies licensing, grants the execution role the required permissions, and attaches the image to the domain. Posit publishes the image definition, for example the [Positron SageMaker Containerfile](https://github.com/posit-dev/images-specialized/blob/main/positron-sagemaker/2026.09/Containerfile.ubuntu2404), which builds on the SageMaker Distribution base image. Amazon Bedrock is optional and is involved only when it’s selected as the Posit Assistant provider.

Responsibilities remain separate. Posit provides the software image and product support. The customer manages identity, permissions, licensing, networking, logging, image updates, and approved AWS services. AWS operates the managed cloud services.

### Data science path

The data scientist launches JupyterLab in a SageMaker Studio Space, opens Positron, and uses R, Python, Quarto, Posit Database Drivers, and optionally Posit Assistant to query and analyze data and deploy models.

# What the recorded run established

The recorded workflow demonstrated the following capabilities within a single Positron Space:

**Governed data access.**Athena discovery, sampling, and profiling ran from the configured Space.**Cross-language analysis.**R validated the data and features before Python trained the model.**Measured model behavior.**The held-out AUC was 0.834 and the top risk decile had a 12.3 percent observed default rate.**Managed deployment.**The workflow registered 48,500 scored rows in Athena and brought a real-time endpoint to InService.**Connected outputs.**The live Shiny application and Quarto report were produced from the same project.

# Scope and limitations

The dataset and applicant payloads were synthetic. The workflow didn’t establish model fairness, calibration, lending suitability, production latency, load behavior, monitoring, or regulatory compliance. The AUC and decile results came from one held-out split, and the lower deciles weren’t strictly monotonic. The screenshots document one recorded run and shouldn’t be presented as a general performance or cost benchmark.

Production adoption also requires validating the Posit preview terms, license grant, and image version alongside supported AWS Regions and model availability. Teams must also confirm network design, least-privilege permissions, secrets handling, logging, image patching, and operational ownership.

# Clean up

To avoid ongoing charges, delete the resources this walkthrough created. Delete them in the following order, because the real-time endpoint depends on both its endpoint configuration and its model: delete the endpoint first, then the endpoint configuration, then the model.

**Delete the real-time inference endpoint.**In the SageMaker AI console, go to**Inference**>**Endpoints**, select your endpoint, and choose**Delete**.

**Delete the endpoint configuration.**Go to**Inference**>**Endpoint configurations**, select your configuration, and choose**Delete**.

**Delete the model.**Go to**Inference**>**Models**, select your model, and choose**Delete**.

**Delete the query-output objects and drop the Athena table.**In the Amazon S3 console, open your bucket, go to the output prefix, select the objects, and choose**Delete**.

Then, in the Amazon Athena console query editor, run:

**Delete the Amazon ECR image version.**In the Amazon ECR console, go to**Repositories**, select your repository, select the image tag, and choose**Delete**.

**Delete the SageMaker AI image registration.**In the SageMaker AI console, go to**Admin configurations**>**Images**, select your image, and choose**Delete**.

**Stop and delete Test Spaces you are not using.**Back up any project files you need and confirm the Space’s storage-retention behavior first. In SageMaker Studio, go to**Spaces**, select the Space, and choose**Stop**. Delete the Space only after you have backed up its files.

# Conclusion

The recorded workflow shows how a custom Positron image can keep governed AWS data access, R and Python analysis, model deployment, application development, and reproducible reporting in one SageMaker Studio Space. The continuity is useful because the evidence, code, deployment result, and communication artifact remain connected. Production use still depends on the customer’s security, governance, validation, and operating controls.

# Related resources

For related background, see:

[Positron Set up Guide on SageMaker](https://docs.posit.co/partnerships/aws-sagemaker/positron/admin.html)[Posit Assistant](https://assistant.posit.co/)[Run interactive IDEs on Amazon EKS with SageMaker AI to power up your AI workflows](https://aws.amazon.com/blogs/machine-learning/run-interactive-ides-on-amazon-eks-with-sagemaker-ai-to-power-up-your-ai-workflows/)[Amazon SageMaker Studio documentation](https://docs.aws.amazon.com/sagemaker/latest/dg/studio.html)[Amazon ECR User Guide](https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html)[Positron Docker Image](https://github.com/posit-dev/images-specialized/blob/main/positron-sagemaker/2026.09/Containerfile.ubuntu2404)[AWS License Manager User Guide](https://docs.aws.amazon.com/license-manager/latest/userguide/license-manager.html)