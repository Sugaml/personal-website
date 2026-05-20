# AWS Certified Machine Learning Engineer – Associate (MLA-C01)
## Practice Question Bank (334 unique questions)

> **Exam name clarification:** AWS markets this as **Machine Learning Engineer – Associate (MLA-C01)**, not a separate “MLOps Associate” badge. It is the associate-level cert for **building, deploying, orchestrating, monitoring, and securing** ML workloads—the practical MLOps role on SageMaker and related services.

| Attribute | Value |
|-----------|-------|
| Scored questions on exam | 50 |
| Total questions (incl. unscored) | 65 |
| Time | 130 minutes |
| Passing score | 720 / 1000 (scaled) |

| Domain | Weight |
|--------|--------|
| 1 — Data Preparation | 28% |
| 2 — ML Model Development | 26% |
| 3 — Deployment & Orchestration | 22% |
| 4 — Monitoring, Maintenance & Security | 24% |

[Official exam guide (PDF)](https://d1.awsstatic.com/training-and-certification/docs-machine-learning-engineer-associate/AWS-Certified-Machine-Learning-Engineer-Associate_Exam-Guide.pdf)

---


## Domain 1: Data Preparation for ML

### Question 1

A data team stores 2 TB of clickstream logs accessed mostly by column (user_id, event_type, timestamp). They run nightly Spark jobs on EMR and occasional ad-hoc Athena queries. Which storage format best balances cost and query performance?

- **A)** JSON files in Amazon S3 with gzip compression
- **B)** Apache Parquet with Snappy compression partitioned by date
- **C)** CSV without compression for human readability
- **D)** Amazon EBS gp3 volumes attached to a single EC2 instance

**Correct answer:** B

**Why this is correct (detailed):**

Parquet is columnar: Spark and Athena read only needed columns, reducing I/O versus row formats like JSON/CSV. Snappy gives fast compression/decompression suitable for big data. Partitioning by date limits scan scope. EBS on one instance does not scale for shared analytics lakes.

**Why the distractors are incorrect:**
- **A)** JSON files in Amazon S3 with gzip compression — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **C)** CSV without compression for human readability — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **D)** Amazon EBS gp3 volumes attached to a single EC2 instance — Does not best satisfy the scenario's primary requirement compared to the correct option.

---
### Question 2

An ML engineer must land real-time fraud features into a feature store while also archiving raw events for compliance. Which architecture satisfies both paths?

- **A)** Kinesis Data Streams → Lambda → SageMaker Feature Store; parallel Firehose delivery to S3
- **B)** S3 PUT events only, with no streaming layer
- **C)** Amazon RDS Multi-AZ as the sole ingestion point
- **D)** AWS Snowball Edge for every transaction

**Correct answer:** A

**Why this is correct (detailed):**

Kinesis ingests streams; Lambda writes online features; Firehose archives to S3 for audit/replay.

**Why the distractors are incorrect:**
- **B)** S3 PUT events only, with no streaming layer — Too narrow or contradicts the scenario's scale, latency, or compliance needs.
- **C)** Amazon RDS Multi-AZ as the sole ingestion point — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **D)** AWS Snowball Edge for every transaction — Does not best satisfy the scenario's primary requirement compared to the correct option.

---
### Question 3

Before training a credit model, you must detect label imbalance across protected groups. Which AWS tool is purpose-built for pre-training bias metrics (e.g., CI, DPL)?

- **A)** Amazon Macie
- **B)** SageMaker Clarify pre-training bias analysis
- **C)** AWS WAF
- **D)** Amazon CloudFront

**Correct answer:** B

**Why this is correct (detailed):**

Clarify computes CI, DPL, and related pre-training metrics. Macie finds sensitive data; WAF/CloudFront are edge security/CDN.

**Why the distractors are incorrect:**
- **A)** Amazon Macie — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **C)** AWS WAF — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **D)** Amazon CloudFront — Does not best satisfy the scenario's primary requirement compared to the correct option.

---
### Question 4

A tabular regression problem has 50k rows and strong linear relationships. Fast baseline on SageMaker?

- **A)** Linear Learner
- **B)** Object Detection
- **C)** BlazingText Word2Vec only
- **D)** Seq2Seq

**Correct answer:** A

**Why this is correct (detailed):**

Linear Learner fits tabular regression/classification. Others target vision, embeddings, or sequences.

**Why the distractors are incorrect:**
- **B)** Object Detection — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **C)** BlazingText Word2Vec only — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **D)** Seq2Seq — Does not best satisfy the scenario's primary requirement compared to the correct option.

---
### Question 5

Hyperparameter search across 20 continuous parameters with limited budget—smarter than naive grid?

- **A)** SageMaker Automatic Model Tuning (Bayesian optimization)
- **B)** S3 Intelligent-Tiering only
- **C)** Manual prod endpoint tweak
- **D)** Amazon Connect flows

**Correct answer:** A

**Why this is correct (detailed):**

AMT supports Bayesian optimization for efficient search in large spaces.

**Why the distractors are incorrect:**
- **B)** S3 Intelligent-Tiering only — Too narrow or contradicts the scenario's scale, latency, or compliance needs.
- **C)** Manual prod endpoint tweak — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **D)** Amazon Connect flows — Does not best satisfy the scenario's primary requirement compared to the correct option.

---
### Question 6

Model versions must be approved before production with audit trail.

- **A)** SageMaker Model Registry
- **B)** Public S3 ACL
- **C)** Disable CloudTrail
- **D)** Amazon Polly lexicons

**Correct answer:** A

**Why this is correct (detailed):**

Model Registry tracks packages and approval status for governed promotion.

**Why the distractors are incorrect:**
- **B)** Public S3 ACL — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **C)** Disable CloudTrail — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **D)** Amazon Polly lexicons — Does not best satisfy the scenario's primary requirement compared to the correct option.

---
### Question 7

Sub-second synchronous predictions 24/7 with autoscaling.

- **A)** Real-time inference endpoint
- **B)** Batch Transform only
- **C)** Glacier retrieval per request
- **D)** WorkDocs

**Correct answer:** A

**Why this is correct (detailed):**

Real-time endpoints serve low-latency InvokeEndpoint traffic with auto scaling.

**Why the distractors are incorrect:**
- **B)** Batch Transform only — Too narrow or contradicts the scenario's scale, latency, or compliance needs.
- **C)** Glacier retrieval per request — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **D)** WorkDocs — Does not best satisfy the scenario's primary requirement compared to the correct option.

---
### Question 8

Monthly scoring of 10M records, no low-latency requirement.

- **A)** SageMaker Batch Transform
- **B)** Always-on multi-GPU endpoint
- **C)** Lambda@Edge per row sync
- **D)** SES

**Correct answer:** A

**Why this is correct (detailed):**

Batch Transform is cost-effective bulk offline inference from/to S3.

**Why the distractors are incorrect:**
- **B)** Always-on multi-GPU endpoint — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **C)** Lambda@Edge per row sync — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **D)** SES — Does not best satisfy the scenario's primary requirement compared to the correct option.

---
### Question 9

Payloads up to 1 GB; client polls for results within minutes.

- **A)** Asynchronous inference endpoint
- **B)** Serverless endpoint for 1 GB sync
- **C)** Batch with 1s row SLA
- **D)** Translate API

**Correct answer:** A

**Why this is correct (detailed):**

Async inference queues large requests and writes output to S3 when complete.

**Why the distractors are incorrect:**
- **B)** Serverless endpoint for 1 GB sync — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **C)** Batch with 1s row SLA — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **D)** Translate API — Does not best satisfy the scenario's primary requirement compared to the correct option.

---
### Question 10

Five small sklearn models on one GPU to save cost.

- **A)** Multi-Model Endpoint
- **B)** Five AWS accounts only
- **C)** Lightsail DB
- **D)** DeepRacer

**Correct answer:** A

**Why this is correct (detailed):**

MME hosts multiple models from S3 behind one endpoint.

**Why the distractors are incorrect:**
- **B)** Five AWS accounts only — Too narrow or contradicts the scenario's scale, latency, or compliance needs.
- **C)** Lightsail DB — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **D)** DeepRacer — Out of exam scope or violates security and governance requirements.

---
### Question 11

CI/CD on main: build image, test, train, register model.

- **A)** CodePipeline + CodeBuild + SageMaker Pipelines
- **B)** Manual SSH
- **C)** Pinpoint only
- **D)** No Git

**Correct answer:** A

**Why this is correct (detailed):**

Exam expects CodePipeline/CodeBuild integrated with SageMaker Pipelines.

**Why the distractors are incorrect:**
- **B)** Manual SSH — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **C)** Pinpoint only — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **D)** No Git — Does not best satisfy the scenario's primary requirement compared to the correct option.

---
### Question 12

Production accuracy drops; input feature distributions shifted.

- **A)** Data drift — Model Monitor data quality baseline
- **B)** IAM drift only
- **C)** Intelligent-Tiering
- **D)** RI expiration

**Correct answer:** A

**Why this is correct (detailed):**

Data drift is input distribution change detected vs training baseline.

**Why the distractors are incorrect:**
- **B)** IAM drift only — Too narrow or contradicts the scenario's scale, latency, or compliance needs.
- **C)** Intelligent-Tiering — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **D)** RI expiration — Does not best satisfy the scenario's primary requirement compared to the correct option.

---
### Question 13

Least-privilege notebook access to one S3 prefix and KMS-encrypted artifacts.

- **A)** Scoped IAM execution role with kms:Decrypt on the CMK
- **B)** Root access keys in notebook
- **C)** s3:* on *
- **D)** Public bucket ACL

**Correct answer:** A

**Why this is correct (detailed):**

SageMaker assumes IAM roles; scope resources and KMS grants.

**Why the distractors are incorrect:**
- **B)** Root access keys in notebook — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **C)** s3:* on * — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **D)** Public bucket ACL — Does not best satisfy the scenario's primary requirement compared to the correct option.

---
### Question 14

Endpoint only reachable from corporate VPC applications.

- **A)** VPC config with private subnets and restrictive security groups
- **B)** Public InvokeEndpoint for all
- **C)** Remove security groups
- **D)** Public GitHub model repo

**Correct answer:** A

**Why this is correct (detailed):**

VPC-hosted endpoints keep inference off the public internet.

**Why the distractors are incorrect:**
- **B)** Public InvokeEndpoint for all — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **C)** Remove security groups — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **D)** Public GitHub model repo — Does not best satisfy the scenario's primary requirement compared to the correct option.

---
### Question 15

Right-size inference instance before launch.

- **A)** SageMaker Inference Recommender
- **B)** Amazon Translate
- **C)** DeepRacer
- **D)** SES bounces

**Correct answer:** A

**Why this is correct (detailed):**

Inference Recommender load-tests candidate instance types.

**Why the distractors are incorrect:**
- **B)** Amazon Translate — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **C)** DeepRacer — Out of exam scope or violates security and governance requirements.
- **D)** SES bounces — Does not best satisfy the scenario's primary requirement compared to the correct option.

---
### Question 16

A startup loads 500 GB/day of IoT sensor readings into S3. Analysts query last 7 days by device_id. EMR aggregates hourly. Best format and layout?

- **A)** Parquet, partitioned by day and device_id
- **B)** Uncompressed CSV single file
- **C)** Random JSON blobs without keys
- **D)** EFS only

**Correct answer:** A

**Why this is correct (detailed):**

Partition pruning on day/device_id minimizes data scanned. Parquet columnar storage suits aggregation. Single CSV/JSON at 500 GB/day is inefficient. EFS is not the primary IoT lake store.

**Why the distractors are incorrect:**
- **B)** Uncompressed CSV single file — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **C)** Random JSON blobs without keys — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **D)** EFS only — Does not best satisfy the scenario's primary requirement compared to the correct option.

---
### Question 17

You must validate that the `transaction_amount` column has no nulls and stays between 0 and 100000 before a weekly training job. Minimal-code governance approach?

- **A)** AWS Glue Data Quality rules on the Glue table
- **B)** Delete the column
- **C)** Train without validation
- **D)** Use Amazon Polly

**Correct answer:** A

**Why this is correct (detailed):**

Glue Data Quality integrates with the Data Catalog and can fail jobs when rules break. Deleting features loses signal. Polly is unrelated.

**Why the distractors are incorrect:**
- **B)** Delete the column — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **C)** Train without validation — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **D)** Use Amazon Polly — Does not best satisfy the scenario's primary requirement compared to the correct option.

---
### Question 18

Two teams contribute features with the same record ID but different event times. Feature Store should

- **A)** use a record identifier and event time for point-in-time correct joins
- **B)** overwrite all history silently
- **C)** ignore timestamps
- **D)** store only in ElastiCache

**Correct answer:** A

**Why this is correct (detailed):**

Feature Store supports event time for point-in-time correctness—critical to avoid label leakage. Silent overwrite breaks reproducibility. ElastiCache lacks offline store semantics.

**Why the distractors are incorrect:**
- **B)** overwrite all history silently — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **C)** ignore timestamps — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **D)** store only in ElastiCache — Does not best satisfy the scenario's primary requirement compared to the correct option.

---
### Question 19

PII must stay in ap-southeast-1; models train in the same region. Which constraint matters most?

- **A)** Data residency: S3, KMS keys, and SageMaker resources in ap-southeast-1
- **B)** Replicate all data to us-east-1 for convenience
- **C)** Disable encryption
- **D)** Use public datasets only

**Correct answer:** A

**Why this is correct (detailed):**

Compliance (PII/PHI, residency) requires regional control of storage and keys. Cross-region copies may violate policy. Encryption is required, not disabled.

**Why the distractors are incorrect:**
- **B)** Replicate all data to us-east-1 for convenience — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **C)** Disable encryption — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **D)** Use public datasets only — Does not best satisfy the scenario's primary requirement compared to the correct option.

---
### Question 20

Apache Flink on Managed Service for Apache Flink detects late-arriving events for sessionization. Output features land in S3 as Parquet. This pattern addresses

- **A)** streaming ETL with event-time windows for real-time features
- **B)** batch-only reporting with no streams
- **C)** DNS routing
- **D)** email campaigns

**Correct answer:** A

**Why this is correct (detailed):**

Flink is in-scope for stream processing; event-time windows handle lateness. DNS/email are unrelated.

**Why the distractors are incorrect:**
- **B)** batch-only reporting with no streams — Too narrow or contradicts the scenario's scale, latency, or compliance needs.
- **C)** DNS routing — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **D)** email campaigns — Does not best satisfy the scenario's primary requirement compared to the correct option.

---
### Question 21

Data Wrangler export should feed both SageMaker Processing and scheduled Glue jobs. You should

- **A)** export reproducible transformation code/recipe into the pipeline
- **B)** keep transformations only in browser memory
- **C)** email CSV attachments
- **D)** avoid version control

**Correct answer:** A

**Why this is correct (detailed):**

Reproducible exports enable MLOps pipelines (exam skill 1.2). Browser-only flows are not repeatable.

**Why the distractors are incorrect:**
- **B)** keep transformations only in browser memory — Too narrow or contradicts the scenario's scale, latency, or compliance needs.
- **C)** email CSV attachments — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **D)** avoid version control — Does not best satisfy the scenario's primary requirement compared to the correct option.

---
### Question 22

Selection bias appears because training data only includes users who completed signup. Mitigation includes

- **A)** revising sampling to include non-completers and measuring bias with Clarify
- **B)** hiding the issue with more epochs
- **C)** using larger instance types only
- **D)** disabling holdout sets

**Correct answer:** A

**Why this is correct (detailed):**

Selection bias is a pre-training concern; Clarify helps measure; sampling fixes the root cause. More epochs or bigger instances do not fix biased data collection.

**Why the distractors are incorrect:**
- **B)** hiding the issue with more epochs — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **C)** using larger instance types only — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **D)** disabling holdout sets — Does not best satisfy the scenario's primary requirement compared to the correct option.

---
### Question 23

Athena queries on nested JSON in S3 are slow and expensive. First optimization step?

- **A)** Convert to partitioned Parquet via CTAS or Glue ETL
- **B)** Increase JSON indentation
- **C)** Disable S3 versioning
- **D)** Move to Snowmobile

**Correct answer:** A

**Why this is correct (detailed):**

Columnar Parquet plus partitions reduces bytes scanned—Athena best practice. Snowmobile is bulk migration.

**Why the distractors are incorrect:**
- **B)** Increase JSON indentation — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **C)** Disable S3 versioning — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **D)** Move to Snowmobile — Does not best satisfy the scenario's primary requirement compared to the correct option.

---
### Question 24

Amazon A2I should be used when

- **A)** human review is needed for low-confidence predictions in a loop with SageMaker
- **B)** you need only S3 lifecycle rules
- **C)** training without labels
- **D)** replacing IAM entirely

**Correct answer:** A

**Why this is correct (detailed):**

Augmented AI (A2I) integrates human reviewers for production ML workflows (e.g., moderation). It does not replace IAM or create labels without a workflow.

**Why the distractors are incorrect:**
- **B)** you need only S3 lifecycle rules — Too narrow or contradicts the scenario's scale, latency, or compliance needs.
- **C)** training without labels — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **D)** replacing IAM entirely — Does not best satisfy the scenario's primary requirement compared to the correct option.

---
### Question 25

DynamoDB streams feed Lambda to update online features while S3 holds historical exports. This is

- **A)** a valid pattern for near-real-time feature updates plus offline history
- **B)** invalid because DynamoDB cannot stream
- **C)** only for CloudFront
- **D)** replaces Feature Store always

**Correct answer:** A

**Why this is correct (detailed):**

Streams + Lambda is a common pattern; Feature Store can still be the canonical store. DynamoDB streams exist. CloudFront is CDN.

**Why the distractors are incorrect:**
- **B)** invalid because DynamoDB cannot stream — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **C)** only for CloudFront — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **D)** replaces Feature Store always — Does not best satisfy the scenario's primary requirement compared to the correct option.

---
### Question 26

Tokenization for NLP features in a visual pipeline before BERT fine-tuning can be done in

- **A)** SageMaker Data Wrangler or processing scripts with Hugging Face tokenizers
- **B)** Route 53
- **C)** AWS Budgets
- **D)** Amazon SES

**Correct answer:** A

**Why this is correct (detailed):**

Encoding/tokenization is exam knowledge (task 1.2). Route 53/Budgets/SES are unrelated.

**Why the distractors are incorrect:**
- **B)** Route 53 — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **C)** AWS Budgets — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **D)** Amazon SES — Does not best satisfy the scenario's primary requirement compared to the correct option.

---
### Question 27

Measurement bias occurs when a sensor miscalibrates for one factory. You should

- **A)** detect distribution differences per factory and recalibrate or exclude bad sensors
- **B)** merge factories without inspection
- **C)** increase learning rate
- **D)** use only accuracy on training set

**Correct answer:** A

**Why this is correct (detailed):**

Measurement bias is a data quality issue addressed in preparation, not hyperparameters alone.

**Why the distractors are incorrect:**
- **B)** merge factories without inspection — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **C)** increase learning rate — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **D)** use only accuracy on training set — Does not best satisfy the scenario's primary requirement compared to the correct option.

---
### Question 28

Shuffle and split training/validation/test before upload helps

- **A)** reduce leakage and get unbiased performance estimates
- **B)** increase S3 API cost only
- **C)** eliminate need for monitoring
- **D)** avoid encryption

**Correct answer:** A

**Why this is correct (detailed):**

Proper splitting is task 1.3—prevents overly optimistic metrics and leakage.

**Why the distractors are incorrect:**
- **B)** increase S3 API cost only — Too narrow or contradicts the scenario's scale, latency, or compliance needs.
- **C)** eliminate need for monitoring — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **D)** avoid encryption — Does not best satisfy the scenario's primary requirement compared to the correct option.

---
### Question 29

Glue DataBrew is BEST for

- **A)** visual data preparation without writing Spark code for every transform
- **B)** hosting real-time GPU inference
- **C)** domain registration
- **D)** VPC peering only

**Correct answer:** A

**Why this is correct (detailed):**

DataBrew targets interactive data prep for analytics/ML consumers. It is not an inference or DNS service.

**Why the distractors are incorrect:**
- **B)** hosting real-time GPU inference — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **C)** domain registration — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **D)** VPC peering only — Does not best satisfy the scenario's primary requirement compared to the correct option.

---
### Question 30

To accelerate repeated reads of a large S3 dataset on training nodes, you can use

- **A)** FSx for Lustre with lazy loading from S3 or SageMaker fast file mode
- **B)** Glacier Deep Archive
- **C)** Public ACL on artifacts
- **D)** Disable caching entirely always

**Correct answer:** A

**Why this is correct (detailed):**

FSx Lustre and SageMaker input modes address I/O bottlenecks (exam storage guidance).

**Why the distractors are incorrect:**
- **B)** Glacier Deep Archive — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **C)** Public ACL on artifacts — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **D)** Disable caching entirely always — Does not best satisfy the scenario's primary requirement compared to the correct option.

---
### Question 31

Image classification with 1M labeled images and need for transfer learning. Fastest path on SageMaker?

- **A)** Use a pre-trained model from JumpStart and fine-tune with GPU instances
- **B)** Train from random weights on CPU only
- **C)** Use Amazon Translate
- **D)** Only Batch Transform without training

**Correct answer:** A

**Why this is correct (detailed):**

JumpStart provides pre-trained models; fine-tuning beats training from scratch on large vision data.

**Why the distractors are incorrect:**
- **B)** Train from random weights on CPU only — Too narrow or contradicts the scenario's scale, latency, or compliance needs.
- **C)** Use Amazon Translate — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **D)** Only Batch Transform without training — Does not best satisfy the scenario's primary requirement compared to the correct option.

---
### Question 32

Random search vs Bayesian optimization for HPO with 100 trials budget on SageMaker AMT

- **A)** Bayesian explores promising regions faster than naive grid on large spaces
- **B)** Grid always cheaper
- **C)** HPO impossible on SageMaker
- **D)** Only manual tuning allowed

**Correct answer:** A

**Why this is correct (detailed):**

Exam covers Bayesian optimization in AMT for efficient search.

**Why the distractors are incorrect:**
- **B)** Grid always cheaper — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **C)** HPO impossible on SageMaker — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **D)** Only manual tuning allowed — Does not best satisfy the scenario's primary requirement compared to the correct option.

---
### Question 33

Dropout in neural networks primarily acts as

- **A)** regularization reducing co-adaptation of neurons
- **B)** data augmentation for images
- **C)** encryption
- **D)** S3 replication

**Correct answer:** A

**Why this is correct (detailed):**

Dropout is regularization (task 2.2 knowledge).

**Why the distractors are incorrect:**
- **B)** data augmentation for images — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **C)** encryption — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **D)** S3 replication — Does not best satisfy the scenario's primary requirement compared to the correct option.

---
### Question 34

AUC-ROC is preferred when

- **A)** you care about ranking quality across thresholds for imbalanced classes
- **B)** all classes are perfectly balanced and cost is zero
- **C)** regression RMSE is the goal
- **D)** monitoring S3 size

**Correct answer:** A

**Why this is correct (detailed):**

ROC/AUC evaluates classifiers across thresholds—exam metric knowledge.

**Why the distractors are incorrect:**
- **B)** all classes are perfectly balanced and cost is zero — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **C)** regression RMSE is the goal — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **D)** monitoring S3 size — Does not best satisfy the scenario's primary requirement compared to the correct option.

---
### Question 35

SageMaker Experiments track

- **A)** parameters, artifacts, and lineage across training runs
- **B)** only VPC flow logs
- **C)** employee badges
- **D)** DNS queries

**Correct answer:** A

**Why this is correct (detailed):**

Experiments support reproducibility (task 2.3).

**Why the distractors are incorrect:**
- **B)** only VPC flow logs — Too narrow or contradicts the scenario's scale, latency, or compliance needs.
- **C)** employee badges — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **D)** DNS queries — Does not best satisfy the scenario's primary requirement compared to the correct option.

---
### Question 36

Combining XGBoost, linear model, and neural net predictions via a meta-learner is

- **A)** stacking ensemble
- **B)** unsupervised clustering
- **C)** data drift
- **D)** Glacier restore

**Correct answer:** A

**Why this is correct (detailed):**

Stacking/ensembling is explicit exam knowledge.

**Why the distractors are incorrect:**
- **B)** unsupervised clustering — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **C)** data drift — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **D)** Glacier restore — Does not best satisfy the scenario's primary requirement compared to the correct option.

---
### Question 37

Early stopping during training saves cost by

- **A)** halting when validation metric stops improving
- **B)** running infinite epochs
- **C)** deleting validation data
- **D)** disabling checkpoints

**Correct answer:** A

**Why this is correct (detailed):**

Early stopping is a training-time cost/performance method.

**Why the distractors are incorrect:**
- **B)** running infinite epochs — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **C)** deleting validation data — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **D)** disabling checkpoints — Does not best satisfy the scenario's primary requirement compared to the correct option.

---
### Question 38

For multilingual sentiment at scale without custom training, consider

- **A)** Amazon Comprehend detect_sentiment
- **B)** Amazon EBS snapshot
- **C)** AWS Snowcone per tweet
- **D)** Amazon MQ

**Correct answer:** A

**Why this is correct (detailed):**

Comprehend is in-scope AI service for NLP tasks.

**Why the distractors are incorrect:**
- **B)** Amazon EBS snapshot — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **C)** AWS Snowcone per tweet — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **D)** Amazon MQ — Does not best satisfy the scenario's primary requirement compared to the correct option.

---
### Question 39

Weight decay (L2) helps by

- **A)** penalizing large weights to reduce overfitting
- **B)** increasing model size always
- **C)** encrypting gradients
- **D)** replacing validation set

**Correct answer:** A

**Why this is correct (detailed):**

L2 regularization is exam knowledge task 2.2.

**Why the distractors are incorrect:**
- **B)** increasing model size always — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **C)** encrypting gradients — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **D)** replacing validation set — Does not best satisfy the scenario's primary requirement compared to the correct option.

---
### Question 40

Distributed data parallel training on SageMaker is used when

- **A)** dataset is large and training time must shrink across many GPUs
- **B)** dataset fits in 1 MB
- **C)** inference only
- **D)** no need for GPUs ever

**Correct answer:** A

**Why this is correct (detailed):**

Distributed training reduces wall-clock time (task 2.2).

**Why the distractors are incorrect:**
- **B)** dataset fits in 1 MB — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **C)** inference only — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **D)** no need for GPUs ever — Does not best satisfy the scenario's primary requirement compared to the correct option.

---
### Question 41

Clarify SHAP explainability after training helps

- **A)** interpret feature contributions for stakeholders and debug bias
- **B)** compress S3 buckets
- **C)** create IAM users
- **D)** replace Model Monitor

**Correct answer:** A

**Why this is correct (detailed):**

Clarify explainability is task 2.3; distinct from production monitoring.

**Why the distractors are incorrect:**
- **B)** compress S3 buckets — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **C)** create IAM users — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **D)** replace Model Monitor — Does not best satisfy the scenario's primary requirement compared to the correct option.

---
### Question 42

Choosing Linear Learner vs XGBoost on tabular data should consider

- **A)** interpretability, non-linearity, training time, and data size
- **B)** only logo color
- **C)** random choice
- **D)** S3 region name only

**Correct answer:** A

**Why this is correct (detailed):**

Algorithm selection weighs business constraints (task 2.1).

**Why the distractors are incorrect:**
- **B)** only logo color — Too narrow or contradicts the scenario's scale, latency, or compliance needs.
- **C)** random choice — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **D)** S3 region name only — Does not best satisfy the scenario's primary requirement compared to the correct option.

---
### Question 43

Catastrophic forgetting in continual learning is mitigated by

- **A)** rehearsal, regularization, or multi-task training strategies
- **B)** deleting old data always without review
- **C)** disabling evaluation
- **D)** using only Batch Transform

**Correct answer:** A

**Why this is correct (detailed):**

Exam mentions preventing catastrophic forgetting (task 2.2).

**Why the distractors are incorrect:**
- **B)** deleting old data always without review — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **C)** disabling evaluation — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **D)** using only Batch Transform — Does not best satisfy the scenario's primary requirement compared to the correct option.

---
### Question 44

RMSE is the primary metric for

- **A)** regression problems
- **B)** multi-class image tagging only
- **C)** IAM policy size
- **D)** S3 object count

**Correct answer:** A

**Why this is correct (detailed):**

RMSE is standard regression metric in guide.

**Why the distractors are incorrect:**
- **B)** multi-class image tagging only — Too narrow or contradicts the scenario's scale, latency, or compliance needs.
- **C)** IAM policy size — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **D)** S3 object count — Does not best satisfy the scenario's primary requirement compared to the correct option.

---
### Question 45

Personalize is appropriate when

- **A)** recommendations for users based on interaction history
- **B)** OCR of legal PDFs only
- **C)** network firewall rules
- **D)** EC2 patching

**Correct answer:** A

**Why this is correct (detailed):**

Amazon Personalize is in-scope ML service for recommendations.

**Why the distractors are incorrect:**
- **B)** OCR of legal PDFs only — Too narrow or contradicts the scenario's scale, latency, or compliance needs.
- **C)** network firewall rules — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **D)** EC2 patching — Does not best satisfy the scenario's primary requirement compared to the correct option.

---
### Question 46

Traffic is unpredictable with long idle periods; cold starts up to seconds are acceptable. Choose

- **A)** SageMaker Serverless Inference
- **B)** Always-on ml.g5.12xlarge cluster
- **C)** Snowball Edge
- **D)** Amazon WorkSpaces

**Correct answer:** A

**Why this is correct (detailed):**

Serverless inference scales to zero and charges per invocation—good for sporadic traffic.

**Why the distractors are incorrect:**
- **B)** Always-on ml.g5.12xlarge cluster — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **C)** Snowball Edge — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **D)** Amazon WorkSpaces — Does not best satisfy the scenario's primary requirement compared to the correct option.

---
### Question 47

CodeDeploy-style linear deployment for endpoints means

- **A)** gradually increasing traffic to the new variant while monitoring
- **B)** instant cutover with zero monitoring
- **C)** deleting old model artifacts
- **D)** training inside the endpoint

**Correct answer:** A

**Why this is correct (detailed):**

Linear/canary shifts are exam deployment strategies.

**Why the distractors are incorrect:**
- **B)** instant cutover with zero monitoring — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **C)** deleting old model artifacts — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **D)** training inside the endpoint — Does not best satisfy the scenario's primary requirement compared to the correct option.

---
### Question 48

MWAA (Managed Airflow) is chosen when

- **A)** existing Airflow DAGs orchestrate ETL and SageMaker jobs
- **B)** you need a NoSQL database
- **C)** you want to eliminate orchestration
- **D)** only for static websites

**Correct answer:** A

**Why this is correct (detailed):**

MWAA is in-scope orchestrator alongside SageMaker Pipelines.

**Why the distractors are incorrect:**
- **B)** you need a NoSQL database — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **C)** you want to eliminate orchestration — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **D)** only for static websites — Does not best satisfy the scenario's primary requirement compared to the correct option.

---
### Question 49

Step Functions can

- **A)** coordinate Lambda, SageMaker jobs, and human approval steps in a state machine
- **B)** only send email
- **C)** replace S3
- **D)** train models without data

**Correct answer:** A

**Why this is correct (detailed):**

Step Functions integrates ML workflows in exam scope.

**Why the distractors are incorrect:**
- **B)** only send email — Too narrow or contradicts the scenario's scale, latency, or compliance needs.
- **C)** replace S3 — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **D)** train models without data — Does not best satisfy the scenario's primary requirement compared to the correct option.

---
### Question 50

ECR image scanning in CI/CD helps

- **A)** catch vulnerabilities before deploying inference containers
- **B)** tune hyperparameters
- **C)** label images
- **D)** calculate AUC

**Correct answer:** A

**Why this is correct (detailed):**

Container security is part of deployment best practices.

**Why the distractors are incorrect:**
- **B)** tune hyperparameters — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **C)** label images — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **D)** calculate AUC — Does not best satisfy the scenario's primary requirement compared to the correct option.

---
### Question 51

Provisioned concurrency on Lambda (when used for ML) reduces

- **A)** cold start latency for latency-sensitive sporadic models
- **B)** training time on 8 GPUs
- **C)** S3 storage cost
- **D)** need for any IAM roles

**Correct answer:** A

**Why this is correct (detailed):**

Provisioned concurrency addresses cold starts—task 4.2 capacity knowledge.

**Why the distractors are incorrect:**
- **B)** training time on 8 GPUs — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **C)** S3 storage cost — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **D)** need for any IAM roles — Does not best satisfy the scenario's primary requirement compared to the correct option.

---
### Question 52

Deploying the same model to EKS instead of SageMaker endpoints is chosen when

- **A)** Kubernetes is the standard platform and custom serving stack exists
- **B)** you never need containers
- **C)** data must not be encrypted
- **D)** you want zero orchestration

**Correct answer:** A

**Why this is correct (detailed):**

EKS/ECS are valid deployment targets per task 3.1.

**Why the distractors are incorrect:**
- **B)** you never need containers — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **C)** data must not be encrypted — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **D)** you want zero orchestration — Does not best satisfy the scenario's primary requirement compared to the correct option.

---
### Question 53

GitFlow in ML CI/CD typically means

- **A)** release branches gate production pipeline runs with approvals
- **B)** no version control
- **C)** only manual deploys from laptops
- **D)** shared root credentials in CodeBuild

**Correct answer:** A

**Why this is correct (detailed):**

Git branching models integrate with CodePipeline (task 3.3).

**Why the distractors are incorrect:**
- **B)** no version control — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **C)** only manual deploys from laptops — Out of exam scope or violates security and governance requirements.
- **D)** shared root credentials in CodeBuild — Does not best satisfy the scenario's primary requirement compared to the correct option.

---
### Question 54

Integration test in ML pipeline should verify

- **A)** pipeline stages produce expected artifacts and endpoint health checks pass
- **B)** only README spelling
- **C)** employee satisfaction
- **D)** DNS TTL only

**Correct answer:** A

**Why this is correct (detailed):**

Automated tests include integration/end-to-end per exam.

**Why the distractors are incorrect:**
- **B)** only README spelling — Too narrow or contradicts the scenario's scale, latency, or compliance needs.
- **C)** employee satisfaction — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **D)** DNS TTL only — Does not best satisfy the scenario's primary requirement compared to the correct option.

---
### Question 55

Retraining trigger on schema drift should use

- **A)** EventBridge + Model Monitor/Data Quality alerts → Pipeline execution
- **B)** random cron yearly only
- **C)** disabling monitoring
- **D)** public webhook without auth

**Correct answer:** A

**Why this is correct (detailed):**

Event-driven retraining is core MLOps orchestration.

**Why the distractors are incorrect:**
- **B)** random cron yearly only — Too narrow or contradicts the scenario's scale, latency, or compliance needs.
- **C)** disabling monitoring — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **D)** public webhook without auth — Does not best satisfy the scenario's primary requirement compared to the correct option.

---
### Question 56

Neo compiles models for

- **A)** edge devices with optimized binaries
- **B)** S3 Glacier
- **C)** IAM policy editor
- **D)** Amazon Chime

**Correct answer:** A

**Why this is correct (detailed):**

Neo is edge optimization (task 3.1).

**Why the distractors are incorrect:**
- **B)** S3 Glacier — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **C)** IAM policy editor — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **D)** Amazon Chime — Does not best satisfy the scenario's primary requirement compared to the correct option.

---
### Question 57

Multi-container endpoint hosts

- **A)** multiple containers in one endpoint (e.g., pre/post processing + model)
- **B)** only one algorithm globally
- **C)** data without inference
- **D)** Route 53 records

**Correct answer:** A

**Why this is correct (detailed):**

Multi-container endpoints are explicit SageMaker capability.

**Why the distractors are incorrect:**
- **B)** only one algorithm globally — Too narrow or contradicts the scenario's scale, latency, or compliance needs.
- **C)** data without inference — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **D)** Route 53 records — Does not best satisfy the scenario's primary requirement compared to the correct option.

---
### Question 58

On-demand vs provisioned SageMaker inference capacity

- **A)** on-demand instances scale with traffic; provisioned sets baseline capacity
- **B)** they are identical
- **C)** only Snowball provisioned
- **D)** neither uses EC2

**Correct answer:** A

**Why this is correct (detailed):**

Task 3.2 knowledge: on-demand vs provisioned resources.

**Why the distractors are incorrect:**
- **B)** they are identical — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **C)** only Snowball provisioned — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **D)** neither uses EC2 — Does not best satisfy the scenario's primary requirement compared to the correct option.

---
### Question 59

CodeBuild in ML CI/CD runs

- **A)** unit tests, docker build, and artifact packaging
- **B)** only billing reports
- **C)** DNS failover
- **D)** ground truth labeling alone

**Correct answer:** A

**Why this is correct (detailed):**

CodeBuild compiles/tests/builds images—task 3.3.

**Why the distractors are incorrect:**
- **B)** only billing reports — Too narrow or contradicts the scenario's scale, latency, or compliance needs.
- **C)** DNS failover — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **D)** ground truth labeling alone — Does not best satisfy the scenario's primary requirement compared to the correct option.

---
### Question 60

Hosting on Lambda for inference limits include

- **A)** package size, memory, and timeout constraints vs large GPU models
- **B)** unlimited 30-minute GPU training
- **C)** no need for IAM
- **D)** automatic petabyte scaling

**Correct answer:** A

**Why this is correct (detailed):**

Lambda suits small models; large GPU workloads use SageMaker endpoints.

**Why the distractors are incorrect:**
- **B)** unlimited 30-minute GPU training — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **C)** no need for IAM — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **D)** automatic petabyte scaling — Does not best satisfy the scenario's primary requirement compared to the correct option.

---
### Question 61

Model Monitor bias drift schedule compares

- **A)** live predictions/features to baseline for fairness metrics over time
- **B)** S3 bucket names only
- **C)** employee IDs
- **D)** CloudFront cache

**Correct answer:** A

**Why this is correct (detailed):**

Bias drift monitoring is SageMaker Clarify/Model Monitor capability.

**Why the distractors are incorrect:**
- **B)** S3 bucket names only — Too narrow or contradicts the scenario's scale, latency, or compliance needs.
- **C)** employee IDs — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **D)** CloudFront cache — Does not best satisfy the scenario's primary requirement compared to the correct option.

---
### Question 62

CloudWatch alarm on Invocations and ModelLatency for an endpoint helps

- **A)** detect performance regressions after deploy
- **B)** train faster
- **C)** replace KMS
- **D)** eliminate VPC

**Correct answer:** A

**Why this is correct (detailed):**

Infrastructure and model latency monitoring are task 4.1/4.2 skills.

**Why the distractors are incorrect:**
- **B)** train faster — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **C)** replace KMS — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **D)** eliminate VPC — Does not best satisfy the scenario's primary requirement compared to the correct option.

---
### Question 63

Trusted Advisor can recommend

- **A)** cost optimization and security improvements for ML resources
- **B)** hyperparameter values
- **C)** labeling bounding boxes
- **D)** SQL query plans only

**Correct answer:** A

**Why this is correct (detailed):**

Trusted Advisor is in-scope cost/security tool.

**Why the distractors are incorrect:**
- **B)** hyperparameter values — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **C)** labeling bounding boxes — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **D)** SQL query plans only — Does not best satisfy the scenario's primary requirement compared to the correct option.

---
### Question 64

SageMaker Savings Plans apply to

- **A)** committed SageMaker compute usage for cost reduction
- **B)** S3 Glacier retrieval only
- **C)** IAM MFA
- **D)** Route 53 domains

**Correct answer:** A

**Why this is correct (detailed):**

Savings Plans appear in cost optimization task 4.2.

**Why the distractors are incorrect:**
- **B)** S3 Glacier retrieval only — Too narrow or contradicts the scenario's scale, latency, or compliance needs.
- **C)** IAM MFA — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **D)** Route 53 domains — Does not best satisfy the scenario's primary requirement compared to the correct option.

---
### Question 65

VPC interface endpoint for SageMaker API allows

- **A)** private connectivity without traversing the public internet
- **B)** public anonymous access
- **C)** disabling security groups
- **D)** removing encryption

**Correct answer:** A

**Why this is correct (detailed):**

Private connectivity is network security best practice.

**Why the distractors are incorrect:**
- **B)** public anonymous access — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **C)** disabling security groups — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **D)** removing encryption — Does not best satisfy the scenario's primary requirement compared to the correct option.

---
### Question 66

SageMaker Role Manager helps

- **A)** create least-privilege IAM roles tailored to SageMaker personas
- **B)** delete all logs
- **C)** open security groups to 0.0.0.0/0
- **D)** disable MFA

**Correct answer:** A

**Why this is correct (detailed):**

Role Manager is in-scope IAM helper for ML.

**Why the distractors are incorrect:**
- **B)** delete all logs — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **C)** open security groups to 0.0.0.0/0 — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **D)** disable MFA — Does not best satisfy the scenario's primary requirement compared to the correct option.

---
### Question 67

X-Ray tracing on inference microservices helps

- **A)** find latency bottlenecks across Lambda/API Gateway/SageMaker
- **B)** compute F1 score
- **C)** label data
- **D)** tune learning rate

**Correct answer:** A

**Why this is correct (detailed):**

X-Ray is observability for distributed inference paths.

**Why the distractors are incorrect:**
- **B)** compute F1 score — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **C)** label data — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **D)** tune learning rate — Does not best satisfy the scenario's primary requirement compared to the correct option.

---
### Question 68

A/B testing on SageMaker endpoint variants routes

- **A)** percentage of traffic to each variant to compare metrics
- **B)** all traffic blindly to untested model
- **C)** only DNS queries
- **D)** training data

**Correct answer:** A

**Why this is correct (detailed):**

A/B on variants is production comparison technique (task 4.1).

**Why the distractors are incorrect:**
- **B)** all traffic blindly to untested model — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **C)** only DNS queries — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **D)** training data — Does not best satisfy the scenario's primary requirement compared to the correct option.

---
### Question 69

QuickSight dashboards for ML ops can visualize

- **A)** business KPIs plus CloudWatch-exported operational metrics
- **B)** only IAM policies
- **C)** raw binary weights
- **D)** Git merge conflicts

**Correct answer:** A

**Why this is correct (detailed):**

QuickSight is in-scope for dashboards (task 4.2).

**Why the distractors are incorrect:**
- **B)** only IAM policies — Too narrow or contradicts the scenario's scale, latency, or compliance needs.
- **C)** raw binary weights — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **D)** Git merge conflicts — Does not best satisfy the scenario's primary requirement compared to the correct option.

---
### Question 70

Secrets in CodePipeline should

- **A)** use Secrets Manager or SSM Parameter Store with IAM-scoped access
- **B)** be hard-coded in buildspec.yml committed to Git
- **C)** posted in Slack
- **D)** embedded in public AMIs

**Correct answer:** A

**Why this is correct (detailed):**

CI/CD security best practices forbid hard-coded secrets.

**Why the distractors are incorrect:**
- **B)** be hard-coded in buildspec.yml committed to Git — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **C)** posted in Slack — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **D)** embedded in public AMIs — Does not best satisfy the scenario's primary requirement compared to the correct option.

---
### Question 71

Service quotas on SageMaker endpoints require

- **A)** monitoring utilization and requesting limit increases before launch
- **B)** ignoring limits
- **C)** using root for all calls
- **D)** disabling auto scaling always

**Correct answer:** A

**Why this is correct (detailed):**

Capacity troubleshooting includes quotas (task 4.2).

**Why the distractors are incorrect:**
- **B)** ignoring limits — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **C)** using root for all calls — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **D)** disabling auto scaling always — Does not best satisfy the scenario's primary requirement compared to the correct option.

---
### Question 72

Config rules (AWS Config) can

- **A)** detect non-compliant SageMaker or S3 settings for governance
- **B)** train neural networks
- **C)** perform HPO
- **D)** replace Model Registry

**Correct answer:** A

**Why this is correct (detailed):**

AWS Config is in-scope governance service.

**Why the distractors are incorrect:**
- **B)** train neural networks — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **C)** perform HPO — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **D)** replace Model Registry — Does not best satisfy the scenario's primary requirement compared to the correct option.

---
### Question 73

DevOps Guru for ML workloads can

- **A)** surface operational anomalies using ML on telemetry
- **B)** label images
- **C)** compile Neo models
- **D)** replace CloudTrail

**Correct answer:** A

**Why this is correct (detailed):**

DevOps Guru is in-scope for anomaly detection.

**Why the distractors are incorrect:**
- **B)** label images — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **C)** compile Neo models — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **D)** replace CloudTrail — Does not best satisfy the scenario's primary requirement compared to the correct option.

---
### Question 74

Encrypting inter-node training traffic in VPC uses

- **A)** security groups, NACLs, and optional TLS in distributed frameworks
- **B)** public S3 ACLs
- **C)** disabling IAM
- **D)** sharing access keys in notebook

**Correct answer:** A

**Why this is correct (detailed):**

Network controls and encryption protect training clusters.

**Why the distractors are incorrect:**
- **B)** public S3 ACLs — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **C)** disabling IAM — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **D)** sharing access keys in notebook — Does not best satisfy the scenario's primary requirement compared to the correct option.

---
### Question 75

Budgets alerts at 80% forecasted spend help

- **A)** proactively control ML experimentation costs
- **B)** improve model accuracy directly
- **C)** replace tagging
- **D)** eliminate CloudWatch

**Correct answer:** A

**Why this is correct (detailed):**

AWS Budgets is explicit cost tool in domain 4.

**Why the distractors are incorrect:**
- **B)** improve model accuracy directly — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **C)** replace tagging — Does not best satisfy the scenario's primary requirement compared to the correct option.
- **D)** eliminate CloudWatch — Does not best satisfy the scenario's primary requirement compared to the correct option.

---
### Question 76

An ML platform team needs to populate the Glue Data Catalog from S3. Which AWS capability is MOST appropriate?

- **A)** Use Glue Crawler
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Glue Crawler: enables discoverable schema for ETL and Athena.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 77

An ML platform team needs to migrate on-premises NFS datasets to S3 for training. Which AWS capability is MOST appropriate?

- **A)** Use Data Sync
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Data Sync: hybrid ingest for large legacy stores.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 78

An ML platform team needs to apply tag-based access control on the data lake. Which AWS capability is MOST appropriate?

- **A)** Use Lake Formation
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Lake Formation: governed sharing for feature teams.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 79

An ML platform team needs to power vector/text hybrid search features for RAG sidecars. Which AWS capability is MOST appropriate?

- **A)** Use OpenSearch
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

OpenSearch: in-scope analytics search service.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 80

An ML platform team needs to warehouse joins for feature engineering at scale. Which AWS capability is MOST appropriate?

- **A)** Use Redshift
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Redshift: structured analytics before SageMaker.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 81

An ML platform team needs to run Spark without managing long-lived clusters. Which AWS capability is MOST appropriate?

- **A)** Use EMR Serverless
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

EMR Serverless: cost-aware batch feature generation.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 82

An ML platform team needs to notify on-call when Model Monitor violation fires. Which AWS capability is MOST appropriate?

- **A)** Use SNS
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

SNS: integration for operational alerts.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 83

An ML platform team needs to buffer retraining requests from many producers. Which AWS capability is MOST appropriate?

- **A)** Use SQS
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

SQS: decouple pipeline triggers.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 84

An ML platform team needs to detect anomalies in operational KPI time series. Which AWS capability is MOST appropriate?

- **A)** Use Lookout for Metrics
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Lookout for Metrics: managed anomaly detection.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 85

An ML platform team needs to defect detection with custom vision models. Which AWS capability is MOST appropriate?

- **A)** Use Lookout for Vision
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Lookout for Vision: specialized CV service when not using custom SageMaker.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 86

An ML platform team needs to online fraud scoring with AWS-managed models. Which AWS capability is MOST appropriate?

- **A)** Use Fraud Detector
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Fraud Detector: pre-built fraud ML service.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 87

An ML platform team needs to extract text from scanned forms for NLP features. Which AWS capability is MOST appropriate?

- **A)** Use Textract
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Textract: document ML ingest.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 88

An ML platform team needs to speech-to-text for audio feature pipelines. Which AWS capability is MOST appropriate?

- **A)** Use Transcribe
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Transcribe: audio AI service in scope.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 89

An ML platform team needs to build conversational bots—not primary batch training. Which AWS capability is MOST appropriate?

- **A)** Use Lex
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Lex: NLP conversational service.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 90

An ML platform team needs to enterprise search over documents. Which AWS capability is MOST appropriate?

- **A)** Use Kendra
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Kendra: RAG/search complement.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 91

An ML platform team needs to store Python dependencies for reproducible training images. Which AWS capability is MOST appropriate?

- **A)** Use CodeArtifact
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

CodeArtifact: artifact repo for builds.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 92

An ML platform team needs to declare SageMaker Domain and execution roles as code. Which AWS capability is MOST appropriate?

- **A)** Use CloudFormation
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

CloudFormation: IaC reproducibility.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 93

An ML platform team needs to define pipeline stacks in TypeScript/Python. Which AWS capability is MOST appropriate?

- **A)** Use CDK
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

CDK: IaC alternative in scope.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---

## Domain 2: ML Model Development

### Question 94

An ML platform team needs to scale endpoint instances on InvocationsPerInstance. Which AWS capability is MOST appropriate?

- **A)** Use Auto Scaling
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Auto Scaling: elastic inference capacity.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 95

An ML platform team needs to patch and manage notebook instances/hosts. Which AWS capability is MOST appropriate?

- **A)** Use Systems Manager
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Systems Manager: ops management in scope.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 96

An ML platform team needs to discover PII in S3 before labeling. Which AWS capability is MOST appropriate?

- **A)** Use Macie
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Macie: sensitive data discovery.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 97

An ML platform team needs to encrypt model artifacts at rest with CMK policies. Which AWS capability is MOST appropriate?

- **A)** Use KMS
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

KMS: encryption control plane.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 98

An ML platform team needs to audit CreateEndpoint and UpdateEndpoint API calls. Which AWS capability is MOST appropriate?

- **A)** Use CloudTrail
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

CloudTrail: API audit trail.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 99

An ML platform team needs to analyze SageMaker spend by tag. Which AWS capability is MOST appropriate?

- **A)** Use Cost Explorer
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Cost Explorer: cost visibility.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 100

An ML platform team needs to recommend smaller inference instances. Which AWS capability is MOST appropriate?

- **A)** Use Compute Optimizer
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Compute Optimizer: rightsizing recommendations.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 101

An ML platform team needs to schedule data quality against training baseline. Which AWS capability is MOST appropriate?

- **A)** Use Model Monitor
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Model Monitor: production data drift detection.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 102

An ML platform team needs to capture tensors to detect vanishing gradients. Which AWS capability is MOST appropriate?

- **A)** Use Debugger
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Debugger: training convergence debug.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 103

An ML platform team needs to run Spark/scikit preprocessing at scale. Which AWS capability is MOST appropriate?

- **A)** Use Processing Job
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Processing Job: managed feature engineering jobs.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 104

An ML platform team needs to run distributed GPU script mode. Which AWS capability is MOST appropriate?

- **A)** Use Training Job
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Training Job: core training primitive.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 105

An ML platform team needs to DAG of Processing/Training/Register steps. Which AWS capability is MOST appropriate?

- **A)** Use Pipeline
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Pipeline: native ML workflow orchestration.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 106

An ML platform team needs to deploy pre-trained models quickly. Which AWS capability is MOST appropriate?

- **A)** Use JumpStart
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

JumpStart: accelerator for common architectures.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 107

An ML platform team needs to invoke foundation models without self-hosting weights. Which AWS capability is MOST appropriate?

- **A)** Use Bedrock
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Bedrock: managed FM inference.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 108

An ML platform team needs to face/object APIs without custom training. Which AWS capability is MOST appropriate?

- **A)** Use Rekognition
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Rekognition: vision AI service.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 109

An ML platform team needs to PHI-aware NLP on clinical text. Which AWS capability is MOST appropriate?

- **A)** Use Comprehend Medical
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Comprehend Medical: healthcare NLP service.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 110

An ML platform team needs to attach accelerator to CPU instances (legacy pattern). Which AWS capability is MOST appropriate?

- **A)** Use Elastic Inference
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Elastic Inference: cost inference acceleration where applicable.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 111

An ML platform team needs to run containerized batch scoring jobs at scale. Which AWS capability is MOST appropriate?

- **A)** Use Batch
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Batch: non-SageMaker batch compute option.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 112

An ML platform team needs to run custom inference containers orchestrated by ECS. Which AWS capability is MOST appropriate?

- **A)** Use ECS
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

ECS: container deployment target.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 113

An ML platform team needs to expose Lambda/SageMaker behind REST API. Which AWS capability is MOST appropriate?

- **A)** Use API Gateway
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

API Gateway: edge API for ML microservices.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 114

An ML platform team needs to lightweight inference for sporadic low-volume models. Which AWS capability is MOST appropriate?

- **A)** Use Lambda
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Lambda: serverless inference pattern.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 115

An ML platform team needs to react to S3 Object Created for pipelines. Which AWS capability is MOST appropriate?

- **A)** Use EventBridge
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

EventBridge: event-driven MLOps.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 116

An ML platform team needs to visual profiling and recipes without Spark code. Which AWS capability is MOST appropriate?

- **A)** Use DataBrew
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

DataBrew: interactive data prep.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 117

An ML platform team needs to managed labeling with quality controls. Which AWS capability is MOST appropriate?

- **A)** Use Ground Truth
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Ground Truth: dataset labeling at scale.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 118

An ML platform team needs to online/offline feature consistency. Which AWS capability is MOST appropriate?

- **A)** Use Feature Store
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Feature Store: feature management service.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 119

An ML platform team needs to SHAP and bias reports. Which AWS capability is MOST appropriate?

- **A)** Use Clarify
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Clarify: explainability and fairness insights.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 120

An ML platform team needs to governed model promotion. Which AWS capability is MOST appropriate?

- **A)** Use Model Registry
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Model Registry: versioning and approvals.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 121

An ML platform team needs to compile models for edge hardware. Which AWS capability is MOST appropriate?

- **A)** Use Neo
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Neo: edge optimization.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 122

An ML platform team needs to benchmark latency/throughput across instances. Which AWS capability is MOST appropriate?

- **A)** Use Inference Recommender
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Inference Recommender: sizing guidance.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 123

An ML platform team needs to discount training with checkpoint resume. Which AWS capability is MOST appropriate?

- **A)** Use Spot Training
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Spot Training: cost-optimized training.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 124

An ML platform team needs to compare new model on copied traffic. Which AWS capability is MOST appropriate?

- **A)** Use Shadow variant
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Shadow variant: safe production evaluation.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 125

An ML platform team needs to shift small traffic % then increase. Which AWS capability is MOST appropriate?

- **A)** Use Canary deployment
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Canary deployment: risk-managed rollout.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 126

An ML platform team needs to parallel stacks then switch traffic. Which AWS capability is MOST appropriate?

- **A)** Use Blue/green deployment
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Blue/green deployment: rollback-friendly release.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 127

An ML platform team needs to trigger CodePipeline from repo webhook. Which AWS capability is MOST appropriate?

- **A)** Use GitHub Actions (via CodeSuite)
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

GitHub Actions (via CodeSuite): CI integration pattern.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 128

An ML platform team needs to define CodeBuild phases for test and docker build. Which AWS capability is MOST appropriate?

- **A)** Use Buildspec
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Buildspec: CI build definition.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 129

An ML platform team needs to manual gate in CodePipeline before prod deploy. Which AWS capability is MOST appropriate?

- **A)** Use Approval stage
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Approval stage: human-in-the-loop governance.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 130

An ML platform team needs to allocate ML costs to cost centers. Which AWS capability is MOST appropriate?

- **A)** Use Tagging strategy
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Tagging strategy: financial governance.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 131

An ML platform team needs to alert when forecast exceeds monthly ML cap. Which AWS capability is MOST appropriate?

- **A)** Use Budgets
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Budgets: proactive spend control.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 132

An ML platform team needs to dashboard model KPIs for business users. Which AWS capability is MOST appropriate?

- **A)** Use QuickSight
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

QuickSight: BI visualization.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 133

An ML platform team needs to query inference logs for errors. Which AWS capability is MOST appropriate?

- **A)** Use CloudWatch Logs Insights
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

CloudWatch Logs Insights: log analytics.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 134

An ML platform team needs to trace latency across microservices. Which AWS capability is MOST appropriate?

- **A)** Use X-Ray
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

X-Ray: distributed tracing.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 135

An ML platform team needs to private S3/SageMaker access without NAT. Which AWS capability is MOST appropriate?

- **A)** Use VPC endpoints
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

VPC endpoints: network isolation.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 136

An ML platform team needs to restrict endpoint ENI to app subnet CIDR. Which AWS capability is MOST appropriate?

- **A)** Use Security group
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Security group: network ACL at instance level.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 137

An ML platform team needs to restrict SageMaker actions by vpc/tag. Which AWS capability is MOST appropriate?

- **A)** Use IAM condition keys
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

IAM condition keys: fine-grained authorization.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 138

An ML platform team needs to deny non-TLS S3 access for artifacts. Which AWS capability is MOST appropriate?

- **A)** Use Bucket policy
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Bucket policy: data perimeter control.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 139

An ML platform team needs to customer-managed keys for compliance. Which AWS capability is MOST appropriate?

- **A)** Use SSE-S3 vs SSE-KMS
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

SSE-S3 vs SSE-KMS: KMS for key policy control.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 140

An ML platform team needs to allow central tooling account to deploy models. Which AWS capability is MOST appropriate?

- **A)** Use Cross-account role
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Cross-account role: enterprise access pattern.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 141

An ML platform team needs to collaborative IDE for experiments. Which AWS capability is MOST appropriate?

- **A)** Use SageMaker Studio
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

SageMaker Studio: unified ML IDE.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 142

An ML platform team needs to automate notebook setup scripts. Which AWS capability is MOST appropriate?

- **A)** Use Lifecycle config
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Lifecycle config: repeatable dev environments.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 143

An ML platform team needs to stream S3 data without full download. Which AWS capability is MOST appropriate?

- **A)** Use Pipe input mode
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Pipe input mode: training I/O optimization.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 144

An ML platform team needs to copy dataset to training volume. Which AWS capability is MOST appropriate?

- **A)** Use File input mode
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

File input mode: when repeated local reads help.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 145

An ML platform team needs to optimized mount for large datasets. Which AWS capability is MOST appropriate?

- **A)** Use FastFile mode
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

FastFile mode: reduced startup for big data.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 146

An ML platform team needs to batch size affects memory and convergence. Which AWS capability is MOST appropriate?

- **A)** Use Hyperparameter
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Hyperparameter: tuning impacts training stability.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 147

An ML platform team needs to epoch is full pass; step is one batch update. Which AWS capability is MOST appropriate?

- **A)** Use Epoch vs step
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Epoch vs step: training vocabulary.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 148

An ML platform team needs to combine models to reduce variance. Which AWS capability is MOST appropriate?

- **A)** Use Ensembling
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Ensembling: performance technique.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 149

An ML platform team needs to remove weights to shrink model size. Which AWS capability is MOST appropriate?

- **A)** Use Pruning
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Pruning: compression technique in scope.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 150

An ML platform team needs to visualize CNN focus for debugging. Which AWS capability is MOST appropriate?

- **A)** Use Heat map
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Heat map: evaluation visualization.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 151

An ML platform team needs to see per-class errors. Which AWS capability is MOST appropriate?

- **A)** Use Confusion matrix
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Confusion matrix: classification evaluation.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 152

An ML platform team needs to tune threshold for fraud use cases. Which AWS capability is MOST appropriate?

- **A)** Use Precision/recall tradeoff
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Precision/recall tradeoff: metric interpretation.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 153

An ML platform team needs to high error on train and validation. Which AWS capability is MOST appropriate?

- **A)** Use Underfitting
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Underfitting: needs more capacity or features.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 154

An ML platform team needs to low train error, high validation error. Which AWS capability is MOST appropriate?

- **A)** Use Overfitting
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Overfitting: needs regularization or more data.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 155

An ML platform team needs to P(Y|X) changes over time. Which AWS capability is MOST appropriate?

- **A)** Use Concept drift
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Concept drift: monitor model quality metrics.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 156

An ML platform team needs to features contain future information. Which AWS capability is MOST appropriate?

- **A)** Use Label leakage
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Label leakage: prevent with point-in-time joins.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 157

An ML platform team needs to categorical to binary columns. Which AWS capability is MOST appropriate?

- **A)** Use One-hot encoding
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

One-hot encoding: encoding technique task 1.2.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 158

An ML platform team needs to discretize continuous variables. Which AWS capability is MOST appropriate?

- **A)** Use Binning
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Binning: feature engineering technique.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 159

An ML platform team needs to stabilize skewed numeric features. Which AWS capability is MOST appropriate?

- **A)** Use Log transform
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Log transform: feature engineering technique.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 160

An ML platform team needs to efficient SageMaker built-in ingest. Which AWS capability is MOST appropriate?

- **A)** Use RecordIO protobuf
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

RecordIO protobuf: format for algorithms.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 161

An ML platform team needs to columnar alternative to Parquet. Which AWS capability is MOST appropriate?

- **A)** Use ORC
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

ORC: valid lake format.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 162

An ML platform team needs to schema evolution friendly row format. Which AWS capability is MOST appropriate?

- **A)** Use Avro
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Avro: common in Kafka sinks.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 163

An ML platform team needs to parallelism unit for streams. Which AWS capability is MOST appropriate?

- **A)** Use Kinesis shard
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Kinesis shard: streaming scalability concept.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 164

An ML platform team needs to batch small records to S3 objects. Which AWS capability is MOST appropriate?

- **A)** Use Firehose buffering
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Firehose buffering: efficient land in lake.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 165

An ML platform team needs to crowd labeling integrated via Ground Truth. Which AWS capability is MOST appropriate?

- **A)** Use Mechanical Turk
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Mechanical Turk: labeling workforce option.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 166

An ML platform team needs to human review loop for low-confidence predictions. Which AWS capability is MOST appropriate?

- **A)** Use A2I
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

A2I: human-in-the-loop production.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 167

An ML platform team needs to real-time recommendations API. Which AWS capability is MOST appropriate?

- **A)** Use Personalize
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Personalize: recommendation service.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 168

An ML platform team needs to text-to-speech—not training labels. Which AWS capability is MOST appropriate?

- **A)** Use Polly
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Polly: speech synthesis service.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 169

An ML platform team needs to language translation API. Which AWS capability is MOST appropriate?

- **A)** Use Translate
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Translate: NLP service selection.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 170

An ML platform team needs to FHIR data store for healthcare analytics. Which AWS capability is MOST appropriate?

- **A)** Use HealthLake
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

HealthLake: health data service.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 171

An ML platform team needs to ML-powered code review for quality. Which AWS capability is MOST appropriate?

- **A)** Use CodeGuru
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

CodeGuru: dev quality tool in ML category.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 172

An ML platform team needs to manage edge deployments (where used). Which AWS capability is MOST appropriate?

- **A)** Use SageMaker Edge Manager
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

SageMaker Edge Manager: edge lifecycle complement to Neo.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 173

An ML platform team needs to sidecar preprocessing container. Which AWS capability is MOST appropriate?

- **A)** Use Multi-container endpoint
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Multi-container endpoint: deploy pre/post with model.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 174

An ML platform team needs to SNS when inference output ready. Which AWS capability is MOST appropriate?

- **A)** Use Async inference notification
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Async inference notification: client notification pattern.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 175

An ML platform team needs to scale to zero with cold starts. Which AWS capability is MOST appropriate?

- **A)** Use Serverless inference
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Serverless inference: intermittent traffic pattern.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 176

An ML platform team needs to A/B traffic split on endpoint. Which AWS capability is MOST appropriate?

- **A)** Use Real-time multi-variant
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Real-time multi-variant: production experimentation.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 177

An ML platform team needs to list S3 objects to score. Which AWS capability is MOST appropriate?

- **A)** Use Batch Transform manifest
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Batch Transform manifest: batch input format.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 178

An ML platform team needs to organize versions in registry. Which AWS capability is MOST appropriate?

- **A)** Use Model package group
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Model package group: registry structure.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 179

An ML platform team needs to pass dynamic config between steps. Which AWS capability is MOST appropriate?

- **A)** Use Pipeline parameter
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Pipeline parameter: parameterized workflows.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 180

An ML platform team needs to reuse outputs when inputs unchanged. Which AWS capability is MOST appropriate?

- **A)** Use CacheConfig on pipeline step
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

CacheConfig on pipeline step: pipeline cost optimization.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---

## Domain 3: Deployment and Orchestration

### Question 181

An ML platform team needs to handle transient training failures. Which AWS capability is MOST appropriate?

- **A)** Use Retry policy
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Retry policy: resilient orchestration.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 182

An ML platform team needs to checkpoint resume from S3. Which AWS capability is MOST appropriate?

- **A)** Use Spot failure
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Spot failure: fault-tolerant spot training.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 183

An ML platform team needs to keep data plane private. Which AWS capability is MOST appropriate?

- **A)** Use VPC-only S3 gateway endpoint
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

VPC-only S3 gateway endpoint: network cost/privacy.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 184

An ML platform team needs to allow private subnet outbound for pip install. Which AWS capability is MOST appropriate?

- **A)** Use NAT gateway
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

NAT gateway: egress for package installs.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 185

An ML platform team needs to private connectivity to SageMaker API. Which AWS capability is MOST appropriate?

- **A)** Use Interface endpoint
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Interface endpoint: privateLink pattern.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 186

An ML platform team needs to faster cross-region uploads. Which AWS capability is MOST appropriate?

- **A)** Use S3 Transfer Acceleration
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

S3 Transfer Acceleration: distant client ingest.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 187

An ML platform team needs to transition old artifacts to IA/Glacier. Which AWS capability is MOST appropriate?

- **A)** Use S3 lifecycle
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

S3 lifecycle: artifact cost control.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 188

An ML platform team needs to low-latency key-value online features. Which AWS capability is MOST appropriate?

- **A)** Use DynamoDB feature
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

DynamoDB feature: alternative online store pattern.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 189

An ML platform team needs to caching layer—not full feature store. Which AWS capability is MOST appropriate?

- **A)** Use ElastiCache
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

ElastiCache: cache vs feature store distinction.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 190

An ML platform team needs to transactional source—not primary lake. Which AWS capability is MOST appropriate?

- **A)** Use RDS
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

RDS: OLTP vs analytics separation.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 191

An ML platform team needs to document source for features. Which AWS capability is MOST appropriate?

- **A)** Use DocumentDB
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

DocumentDB: NoSQL ingest option.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 192

An ML platform team needs to graph relationships as features. Which AWS capability is MOST appropriate?

- **A)** Use Neptune
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Neptune: graph ML ingest.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 193

An ML platform team needs to create Parquet tables from queries. Which AWS capability is MOST appropriate?

- **A)** Use Athena CTAS
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Athena CTAS: lake transformation pattern.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 194

An ML platform team needs to incremental ETL processing. Which AWS capability is MOST appropriate?

- **A)** Use Glue bookmark
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Glue bookmark: incremental pipeline state.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 195

An ML platform team needs to distributed transform for features. Which AWS capability is MOST appropriate?

- **A)** Use Spark on Glue
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Spark on Glue: serverless Spark option.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 196

An ML platform team needs to long-running Spark when always-on needed. Which AWS capability is MOST appropriate?

- **A)** Use EMR cluster
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

EMR cluster: cluster tradeoff vs Serverless.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 197

An ML platform team needs to fail job on null rate threshold. Which AWS capability is MOST appropriate?

- **A)** Use Data Quality ruleset
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Data Quality ruleset: quality gate before training.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 198

An ML platform team needs to difference in proportions of labels across groups. Which AWS capability is MOST appropriate?

- **A)** Use Clarify DPL
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Clarify DPL: bias metric name.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 199

An ML platform team needs to class imbalance measure. Which AWS capability is MOST appropriate?

- **A)** Use Clarify CI
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Clarify CI: bias metric name.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 200

An ML platform team needs to balance rare classes. Which AWS capability is MOST appropriate?

- **A)** Use Synthetic data
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Synthetic data: mitigate imbalance.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 201

An ML platform team needs to expand training images via transforms. Which AWS capability is MOST appropriate?

- **A)** Use Augmentation
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Augmentation: vision regularization/data volume.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 202

An ML platform team needs to unbiased estimate of generalization. Which AWS capability is MOST appropriate?

- **A)** Use Train/val/test split
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Train/val/test split: fundamental modeling practice.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 203

An ML platform team needs to reproducible experiments. Which AWS capability is MOST appropriate?

- **A)** Use Random seed
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Random seed: experiment tracking practice.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 204

An ML platform team needs to bring custom training script. Which AWS capability is MOST appropriate?

- **A)** Use Script mode
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Script mode: custom framework training.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 205

An ML platform team needs to custom inference container from ECR. Which AWS capability is MOST appropriate?

- **A)** Use BYOC inference
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

BYOC inference: custom serving stack.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 206

An ML platform team needs to start SageMaker training job via SDK. Which AWS capability is MOST appropriate?

- **A)** Use Estimator.fit
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Estimator.fit: SDK training invocation.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 207

An ML platform team needs to high-level deploy from trained estimator. Which AWS capability is MOST appropriate?

- **A)** Use Predictor
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Predictor: SDK deployment helper.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 208

An ML platform team needs to objective metric for AMT jobs. Which AWS capability is MOST appropriate?

- **A)** Use HPO metric
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

HPO metric: tuning optimization target.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 209

An ML platform team needs to stop unpromising training jobs in HPO. Which AWS capability is MOST appropriate?

- **A)** Use Early stopping rule
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Early stopping rule: save tuning budget.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 210

An ML platform team needs to use prior tuning job results. Which AWS capability is MOST appropriate?

- **A)** Use Warm start tuning
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Warm start tuning: accelerate HPO.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 211

An ML platform team needs to use Spot instances for Training jobs. Which AWS capability is MOST appropriate?

- **A)** Use Managed Spot Training
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Managed Spot Training: training cost optimization.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 212

An ML platform team needs to optimize models for faster training/inference. Which AWS capability is MOST appropriate?

- **A)** Use Training Compiler
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Training Compiler: compilation optimization.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 213

An ML platform team needs to split large models across GPUs. Which AWS capability is MOST appropriate?

- **A)** Use Model parallelism
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Model parallelism: large model training.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 214

An ML platform team needs to split batches across replicas. Which AWS capability is MOST appropriate?

- **A)** Use Data parallelism
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Data parallelism: scale training throughput.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 215

An ML platform team needs to stream data from S3 during training. Which AWS capability is MOST appropriate?

- **A)** Use Pipe mode
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Pipe mode: I/O optimization.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 216

An ML platform team needs to list of training samples in S3. Which AWS capability is MOST appropriate?

- **A)** Use Manifest file
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Manifest file: input definition pattern.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 217

An ML platform team needs to bounding boxes for object detection. Which AWS capability is MOST appropriate?

- **A)** Use Augmented manifest
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Augmented manifest: structured label format.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 218

An ML platform team needs to custom Docker training image. Which AWS capability is MOST appropriate?

- **A)** Use Bring your own algorithm
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Bring your own algorithm: maximum training flexibility.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 219

An ML platform team needs to batch multiple rows per request on endpoint. Which AWS capability is MOST appropriate?

- **A)** Use Multi-record batch inference
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Multi-record batch inference: throughput optimization.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 220

An ML platform team needs to TargetTrackingScaling on CPU or custom metric. Which AWS capability is MOST appropriate?

- **A)** Use Auto scaling target
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Auto scaling target: scaling policy type.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 221

An ML platform team needs to prevent flapping when traffic drops. Which AWS capability is MOST appropriate?

- **A)** Use Scale-in cooldown
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Scale-in cooldown: stability of autoscaling.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 222

An ML platform team needs to reserved capacity pattern (where applicable). Which AWS capability is MOST appropriate?

- **A)** Use Provisioned throughput mode
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Provisioned throughput mode: capacity planning concept.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 223

An ML platform team needs to no user impact from shadow responses. Which AWS capability is MOST appropriate?

- **A)** Use Shadow production variant
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Shadow production variant: safe comparison.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 224

An ML platform team needs to traffic split percentage. Which AWS capability is MOST appropriate?

- **A)** Use Production variant weight
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Production variant weight: A/B configuration.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 225

An ML platform team needs to immutable definition of variants and instances. Which AWS capability is MOST appropriate?

- **A)** Use Endpoint config
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Endpoint config: deployment artifact.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 226

An ML platform team needs to move endpoint to new config with rollout. Which AWS capability is MOST appropriate?

- **A)** Use UpdateEndpoint
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

UpdateEndpoint: deployment API.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 227

An ML platform team needs to revert to previous endpoint config on alarms. Which AWS capability is MOST appropriate?

- **A)** Use Rollback
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Rollback: operational safety.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 228

An ML platform team needs to invoke endpoint with sample payload. Which AWS capability is MOST appropriate?

- **A)** Use Integration test in pipeline
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Integration test in pipeline: automated quality gate.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 229

An ML platform team needs to validate data transform functions. Which AWS capability is MOST appropriate?

- **A)** Use Unit test in CodeBuild
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Unit test in CodeBuild: shift-left quality.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 230

An ML platform team needs to production pipeline triggered from release/*. Which AWS capability is MOST appropriate?

- **A)** Use Gitflow release branch
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Gitflow release branch: branching strategy.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 231

An ML platform team needs to encrypt CodePipeline artifacts with KMS. Which AWS capability is MOST appropriate?

- **A)** Use Artifact encryption
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Artifact encryption: CI/CD security.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 232

An ML platform team needs to CodeBuild role scoped to ECR and S3 prefixes. Which AWS capability is MOST appropriate?

- **A)** Use Least privilege build role
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Least privilege build role: pipeline IAM best practice.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 233

An ML platform team needs to page ops when inference errors spike. Which AWS capability is MOST appropriate?

- **A)** Use CloudWatch alarm on 5xx
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

CloudWatch alarm on 5xx: operational monitoring.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 234

An ML platform team needs to publish business KPI from inference container. Which AWS capability is MOST appropriate?

- **A)** Use Custom metric
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Custom metric: application-level monitoring.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 235

An ML platform team needs to control storage cost of verbose inference logs. Which AWS capability is MOST appropriate?

- **A)** Use Log group retention
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Log group retention: log cost management.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 236

An ML platform team needs to mask or exclude from CloudWatch. Which AWS capability is MOST appropriate?

- **A)** Use PII in logs
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

PII in logs: compliance in observability.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 237

An ML platform team needs to prevent use of unapproved regions for ML. Which AWS capability is MOST appropriate?

- **A)** Use Organizations SCP
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Organizations SCP: guardrail at org level.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 238

An ML platform team needs to approved SageMaker products for teams. Which AWS capability is MOST appropriate?

- **A)** Use Service Catalog
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Service Catalog: governed self-service.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 239

An ML platform team needs to Slack notifications from CloudWatch alarms. Which AWS capability is MOST appropriate?

- **A)** Use Chatbot
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Chatbot: ops integration.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 240

An ML platform team needs to underutilized SageMaker endpoints. Which AWS capability is MOST appropriate?

- **A)** Use Trusted Advisor check
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Trusted Advisor check: waste identification.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 241

An ML platform team needs to commit to consistent SageMaker compute. Which AWS capability is MOST appropriate?

- **A)** Use Savings Plans
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Savings Plans: discount for steady workloads.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 242

An ML platform team needs to reserve instances for always-on endpoints. Which AWS capability is MOST appropriate?

- **A)** Use RI
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

RI: predictable baseline cost.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 243

An ML platform team needs to generally avoided for steady SLA real-time. Which AWS capability is MOST appropriate?

- **A)** Use Spot for inference
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Spot for inference: Spot better for fault-tolerant batch/train.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 244

An ML platform team needs to stop idle Studio apps to save cost. Which AWS capability is MOST appropriate?

- **A)** Use Rightsizing notebook
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Rightsizing notebook: dev environment cost control.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 245

An ML platform team needs to dev/stage/prod isolation for ML. Which AWS capability is MOST appropriate?

- **A)** Use Separate accounts
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Separate accounts: blast radius reduction.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 246

An ML platform team needs to DR for model artifacts—watch residency. Which AWS capability is MOST appropriate?

- **A)** Use Cross-region replication
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Cross-region replication: BC/DR vs compliance tradeoff.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 247

An ML platform team needs to document intended use and limitations. Which AWS capability is MOST appropriate?

- **A)** Use Model card
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Model card: governance documentation practice.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 248

An ML platform team needs to diverse labelers in Ground Truth. Which AWS capability is MOST appropriate?

- **A)** Use Human review bias
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Human review bias: labeling quality practice.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 249

An ML platform team needs to measure labeling quality. Which AWS capability is MOST appropriate?

- **A)** Use Inter-annotator agreement
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Inter-annotator agreement: Ground Truth quality mechanism.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 250

An ML platform team needs to label uncertain samples first. Which AWS capability is MOST appropriate?

- **A)** Use Active learning
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Active learning: efficient labeling strategy.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 251

An ML platform team needs to fine-tune vs train from scratch. Which AWS capability is MOST appropriate?

- **A)** Use Transfer learning
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Transfer learning: faster convergence with less data.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 252

An ML platform team needs to large pre-trained model adapted downstream. Which AWS capability is MOST appropriate?

- **A)** Use Foundation model
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Foundation model: modern NLP/CV approach.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 253

An ML platform team needs to optimize inputs to FM APIs. Which AWS capability is MOST appropriate?

- **A)** Use Prompt engineering
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Prompt engineering: Bedrock usage pattern.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---

## Domain 4: Monitoring, Maintenance, and Security

### Question 254

An ML platform team needs to retrieve context then generate answer. Which AWS capability is MOST appropriate?

- **A)** Use RAG
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

RAG: reduce hallucination pattern.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 255

An ML platform team needs to scheduled Batch Transform after ETL. Which AWS capability is MOST appropriate?

- **A)** Use Batch inference pipeline
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Batch inference pipeline: scheduled scoring pattern.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 256

An ML platform team needs to Kinesis + SageMaker Processing/Endpoints. Which AWS capability is MOST appropriate?

- **A)** Use Streaming inference
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Streaming inference: near-real-time pattern.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 257

An ML platform team needs to test feature code on PR in CodeBuild. Which AWS capability is MOST appropriate?

- **A)** Use Feature pipeline CI
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Feature pipeline CI: feature store governance.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 258

An ML platform team needs to schema expectations between teams. Which AWS capability is MOST appropriate?

- **A)** Use Data contract
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Data contract: prevent breaking changes.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 259

An ML platform team needs to Glue schema version for Avro/JSON. Which AWS capability is MOST appropriate?

- **A)** Use Schema registry
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Schema registry: evolution control.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 260

An ML platform team needs to tokenize before labeling. Which AWS capability is MOST appropriate?

- **A)** Use PII masking
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

PII masking: privacy technique.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 261

An ML platform team needs to add noise for privacy (awareness). Which AWS capability is MOST appropriate?

- **A)** Use Differential privacy
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Differential privacy: advanced privacy concept.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 262

An ML platform team needs to Clarify post-training bias metrics. Which AWS capability is MOST appropriate?

- **A)** Use Model bias post-training
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Model bias post-training: fairness after training.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 263

An ML platform team needs to SHAP for regulated decisions. Which AWS capability is MOST appropriate?

- **A)** Use Explainability threshold
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Explainability threshold: interpretability requirement.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 264

An ML platform team needs to awareness for security testing models. Which AWS capability is MOST appropriate?

- **A)** Use Adversarial robustness
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Adversarial robustness: ML security awareness.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 265

An ML platform team needs to encrypt data in transit to InvokeEndpoint. Which AWS capability is MOST appropriate?

- **A)** Use Endpoint TLS
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Endpoint TLS: encryption in transit.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 266

An ML platform team needs to mutual TLS for service-to-service. Which AWS capability is MOST appropriate?

- **A)** Use mTLS
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

mTLS: advanced auth pattern.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 267

An ML platform team needs to consumer VPC accesses SageMaker privately. Which AWS capability is MOST appropriate?

- **A)** Use PrivateLink
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

PrivateLink: private connectivity.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 268

An ML platform team needs to pipeline must pass SageMaker execution role. Which AWS capability is MOST appropriate?

- **A)** Use IAM PassRole
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

IAM PassRole: common permission error.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 269

An ML platform team needs to S3 bucket policy allowing SageMaker role. Which AWS capability is MOST appropriate?

- **A)** Use Resource-based policy
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Resource-based policy: cross-service access.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 270

An ML platform team needs to restrict S3 access to VPC endpoint. Which AWS capability is MOST appropriate?

- **A)** Use Condition aws:SourceVpc
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Condition aws:SourceVpc: data exfiltration prevention.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 271

An ML platform team needs to Registry + Pipeline execution ARN. Which AWS capability is MOST appropriate?

- **A)** Use Audit model lineage
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Audit model lineage: traceability for compliance.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 272

An ML platform team needs to EventBridge cron starts Pipeline. Which AWS capability is MOST appropriate?

- **A)** Use Retrain on schedule
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Retrain on schedule: scheduled refresh.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 273

An ML platform team needs to CloudWatch alarm → Lambda → Pipeline. Which AWS capability is MOST appropriate?

- **A)** Use Retrain on drift
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Retrain on drift: conditional refresh.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 274

An ML platform team needs to challenger variant gets minority traffic. Which AWS capability is MOST appropriate?

- **A)** Use Champion/challenger
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Champion/challenger: continuous evaluation pattern.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 275

An ML platform team needs to never used during HPO to avoid leakage. Which AWS capability is MOST appropriate?

- **A)** Use Holdout set
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Holdout set: honest final evaluation.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 276

An ML platform team needs to k-fold on training for robust metrics. Which AWS capability is MOST appropriate?

- **A)** Use Cross-validation
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Cross-validation: evaluation technique.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 277

An ML platform team needs to preserve class ratios in splits. Which AWS capability is MOST appropriate?

- **A)** Use Stratified split
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Stratified split: imbalanced data practice.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 278

An ML platform team needs to synthetic minority oversampling technique. Which AWS capability is MOST appropriate?

- **A)** Use SMOTE
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

SMOTE: imbalance handling option.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 279

An ML platform team needs to penalize misclassification of rare class. Which AWS capability is MOST appropriate?

- **A)** Use Class weights
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Class weights: algorithm-level imbalance handling.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 280

An ML platform team needs to adjust decision threshold on validation. Which AWS capability is MOST appropriate?

- **A)** Use Threshold tuning
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Threshold tuning: optimize precision/recall.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 281

An ML platform team needs to align predicted probabilities with outcomes. Which AWS capability is MOST appropriate?

- **A)** Use Calibration
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Calibration: probability quality.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 282

An ML platform team needs to choose appropriate loss and metrics. Which AWS capability is MOST appropriate?

- **A)** Use Multiclass vs multilabel
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Multiclass vs multilabel: problem framing.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 283

An ML platform team needs to mAP vs simple accuracy. Which AWS capability is MOST appropriate?

- **A)** Use Object detection metric
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Object detection metric: CV evaluation awareness.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 284

An ML platform team needs to pixel-level masks—specialized algorithms. Which AWS capability is MOST appropriate?

- **A)** Use Segmentation
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Segmentation: CV task type.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 285

An ML platform team needs to forecasting algorithms (DeepAR etc.). Which AWS capability is MOST appropriate?

- **A)** Use Time series
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Time series: SageMaker forecasting domain.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 286

An ML platform team needs to Personalize campaign for new users. Which AWS capability is MOST appropriate?

- **A)** Use Cold start recommendation
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Cold start recommendation: recommendation feature.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 287

An ML platform team needs to online store vs offline store latency. Which AWS capability is MOST appropriate?

- **A)** Use Real-time vs batch features
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Real-time vs batch features: Feature Store architecture.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 288

An ML platform team needs to join features as of event timestamp. Which AWS capability is MOST appropriate?

- **A)** Use Point-in-time query
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Point-in-time query: prevent leakage.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 289

An ML platform team needs to logical collection in Feature Store. Which AWS capability is MOST appropriate?

- **A)** Use Feature group
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Feature group: Feature Store primitive.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 290

An ML platform team needs to historical features for training. Which AWS capability is MOST appropriate?

- **A)** Use Offline store S3
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Offline store S3: batch training data source.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 291

An ML platform team needs to low-latency serving layer. Which AWS capability is MOST appropriate?

- **A)** Use Online store DynamoDB
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Online store DynamoDB: inference feature retrieval.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 292

An ML platform team needs to expire stale online features. Which AWS capability is MOST appropriate?

- **A)** Use TTL on features
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

TTL on features: freshness control.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 293

An ML platform team needs to populate historical features. Which AWS capability is MOST appropriate?

- **A)** Use Backfill pipeline
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Backfill pipeline: Feature Store operations.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 294

An ML platform team needs to explore before production pipeline. Which AWS capability is MOST appropriate?

- **A)** Use Ingestion notebook
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Ingestion notebook: iterative then operationalize.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 295

An ML platform team needs to non-secret config for pipelines. Which AWS capability is MOST appropriate?

- **A)** Use Parameter Store
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Parameter Store: configuration management.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 296

An ML platform team needs to rotate DB creds without downtime. Which AWS capability is MOST appropriate?

- **A)** Use Secrets rotation
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Secrets rotation: Secrets Manager capability.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 297

An ML platform team needs to speed docker layer rebuilds. Which AWS capability is MOST appropriate?

- **A)** Use Build cache in CodeBuild
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Build cache in CodeBuild: CI performance.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 298

An ML platform team needs to prevent image overwrite. Which AWS capability is MOST appropriate?

- **A)** Use Immutable tags in ECR
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Immutable tags in ECR: supply chain integrity.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 299

An ML platform team needs to verify trusted inference images. Which AWS capability is MOST appropriate?

- **A)** Use Image signing
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Image signing: supply chain security awareness.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 300

An ML platform team needs to wait for S3 prefix in MWAA DAG. Which AWS capability is MOST appropriate?

- **A)** Use Airflow sensor
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Airflow sensor: orchestration dependency.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 301

An ML platform team needs to integrate external approval systems. Which AWS capability is MOST appropriate?

- **A)** Use SageMaker pipeline callback
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

SageMaker pipeline callback: enterprise integration.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 302

An ML platform team needs to lightweight custom logic between steps. Which AWS capability is MOST appropriate?

- **A)** Use Lambda step in pipeline
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Lambda step in pipeline: pipeline extensibility.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 303

An ML platform team needs to branch on metric threshold in pipeline. Which AWS capability is MOST appropriate?

- **A)** Use Conditional step
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Conditional step: gated promotion.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 304

An ML platform team needs to register model package after training. Which AWS capability is MOST appropriate?

- **A)** Use Register step
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Register step: registry integration.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 305

An ML platform team needs to create deployable model entity. Which AWS capability is MOST appropriate?

- **A)** Use CreateModel step
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

CreateModel step: deployment prep step.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 306

An ML platform team needs to batch score in pipeline. Which AWS capability is MOST appropriate?

- **A)** Use Transform step
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Transform step: validation scoring in CI.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 307

An ML platform team needs to pass evaluation report to approval step. Which AWS capability is MOST appropriate?

- **A)** Use PropertyFile
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

PropertyFile: metric-based gates.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 308

An ML platform team needs to Approved vs Rejected in registry. Which AWS capability is MOST appropriate?

- **A)** Use Model approval status
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Model approval status: governance gate.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 309

An ML platform team needs to CloudWatch alarm triggers config revert. Which AWS capability is MOST appropriate?

- **A)** Use Endpoint auto rollback
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Endpoint auto rollback: automated safety.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 310

An ML platform team needs to CSV, JSON, or NPY for InvokeEndpoint. Which AWS capability is MOST appropriate?

- **A)** Use Inference payload format
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Inference payload format: client integration detail.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 311

An ML platform team needs to required for correct deserialization. Which AWS capability is MOST appropriate?

- **A)** Use Content-Type header
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Content-Type header: inference API detail.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 312

An ML platform team needs to route to specific production variant. Which AWS capability is MOST appropriate?

- **A)** Use Target variant header
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Target variant header: testing specific variant.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 313

An ML platform team needs to enable data capture for Model Monitor. Which AWS capability is MOST appropriate?

- **A)** Use Capture data
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Capture data: production baseline updates.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 314

An ML platform team needs to upload labels to compare model quality. Which AWS capability is MOST appropriate?

- **A)** Use Ground truth labels for monitor
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Ground truth labels for monitor: supervised monitor setup.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 315

An ML platform team needs to cron on Model Monitor schedule. Which AWS capability is MOST appropriate?

- **A)** Use Schedule hourly monitor
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Schedule hourly monitor: continuous validation.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 316

An ML platform team needs to alert when constraints breached. Which AWS capability is MOST appropriate?

- **A)** Use Violations SNS
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Violations SNS: operational response.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 317

An ML platform team needs to update monitor baseline after approved drift. Which AWS capability is MOST appropriate?

- **A)** Use Rebaselining
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Rebaselining: lifecycle management.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 318

An ML platform team needs to cost allocation on training spend. Which AWS capability is MOST appropriate?

- **A)** Use Training job tags
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Training job tags: financial governance.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 319

An ML platform team needs to allocate endpoint costs. Which AWS capability is MOST appropriate?

- **A)** Use Inference tags
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Inference tags: financial governance.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 320

An ML platform team needs to zero invocations but running instances. Which AWS capability is MOST appropriate?

- **A)** Use Idle endpoint detection
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Idle endpoint detection: waste to eliminate.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 321

An ML platform team needs to RDS for feature source HA—not endpoint HA alone. Which AWS capability is MOST appropriate?

- **A)** Use Multi-AZ
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Multi-AZ: data source availability.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 322

An ML platform team needs to deploy across AZ with multiple instances. Which AWS capability is MOST appropriate?

- **A)** Use Endpoint HA
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Endpoint HA: inference availability.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 323

An ML platform team needs to InvokeEndpoint or container /ping. Which AWS capability is MOST appropriate?

- **A)** Use Health check
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Health check: load balancer / SageMaker health.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 324

An ML platform team needs to optimize for Inf1/GPU edge. Which AWS capability is MOST appropriate?

- **A)** Use Model compilation Neo
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Model compilation Neo: hardware-specific optimization.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 325

An ML platform team needs to cost-efficient inference chips. Which AWS capability is MOST appropriate?

- **A)** Use Inf2 instances
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Inf2 instances: instance family awareness.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 326

An ML platform team needs to GPU inference for deep learning. Which AWS capability is MOST appropriate?

- **A)** Use G5 instances
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

G5 instances: instance family selection.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 327

An ML platform team needs to CPU inference for classical ML. Which AWS capability is MOST appropriate?

- **A)** Use C6i
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

C6i: right-size compute family.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 328

An ML platform team needs to large embedding models. Which AWS capability is MOST appropriate?

- **A)** Use Memory-optimized
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Memory-optimized: instance family for memory-bound.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 329

An ML platform team needs to large payload async/batch needs. Which AWS capability is MOST appropriate?

- **A)** Use Network bandwidth
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Network bandwidth: infrastructure sizing factor.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 330

An ML platform team needs to VPC endpoint scaling constraint. Which AWS capability is MOST appropriate?

- **A)** Use ENI limits
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

ENI limits: VPC planning awareness.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 331

An ML platform team needs to plan CIDR for scaled endpoints. Which AWS capability is MOST appropriate?

- **A)** Use Subnet IP exhaustion
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Subnet IP exhaustion: VPC capacity planning.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 332

An ML platform team needs to minimize via VPC endpoints. Which AWS capability is MOST appropriate?

- **A)** Use NAT cost
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

NAT cost: cost-aware networking.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 333

An ML platform team needs to centralized networking for SageMaker. Which AWS capability is MOST appropriate?

- **A)** Use Shared VPC
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Shared VPC: enterprise network pattern.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---
### Question 334

An ML platform team needs to central ML platform account. Which AWS capability is MOST appropriate?

- **A)** Use Hub account deployment
- **B)** Use AWS DeepRacer exclusively
- **C)** Disable IAM and encryption
- **D)** Store artifacts only on local laptops

**Correct answer:** A

**Why this is correct (detailed):**

Hub account deployment: multi-account ML pattern.

**Why the distractors are incorrect:**
- **B)** Use AWS DeepRacer exclusively — Out of exam scope or violates security and governance requirements.
- **C)** Disable IAM and encryption — Out of exam scope or violates security and governance requirements.
- **D)** Store artifacts only on local laptops — Out of exam scope or violates security and governance requirements.

---

## How to use this bank

1. Study by domain weights (28 / 26 / 22 / 24).
2. For each wrong answer, write *why* the scenario rejects it—exam distractors are plausible.
3. Lab: SageMaker Pipelines, Model Registry, three endpoint types, Model Monitor, CodePipeline integration.
4. Cross-read: [ML Foundations blog](../blogs/aws-machine-learning-foundations.html), [Generative AI Foundations](../blogs/aws-generative-ai-foundations.html), [Data Engineering](../blogs/aws-data-engineering.html).

*Unofficial practice material. Verify against the latest MLA-C01 exam guide.*