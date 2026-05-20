"""Unique MLA-C01 practice questions — imported by generate_mla_practice_questions.py."""

from __future__ import annotations

Question = dict


def q(stem: str, options: dict[str, str], answer: str | list[str], why: str) -> Question:
    return {"stem": stem, "options": options, "answer": answer, "why": why.strip()}


def all_questions():
    """Return 220+ unique questions grouped by domain."""
    d1 = _domain1()
    d2 = _domain2()
    d3 = _domain3()
    d4 = _domain4()
    return d1, d2, d3, d4


def _domain1():
    items = []
    scenarios = [
        (
            "A startup loads 500 GB/day of IoT sensor readings into S3. Analysts query last 7 days by device_id. "
            "EMR aggregates hourly. Best format and layout?",
            {"A": "Parquet, partitioned by day and device_id", "B": "Uncompressed CSV single file", "C": "Random JSON blobs without keys", "D": "EFS only"},
            "A",
            "Partition pruning on day/device_id minimizes data scanned. Parquet columnar storage suits aggregation. "
            "Single CSV/JSON at 500 GB/day is inefficient. EFS is not the primary IoT lake store.",
        ),
        (
            "You must validate that the `transaction_amount` column has no nulls and stays between 0 and 100000 before "
            "a weekly training job. Minimal-code governance approach?",
            {"A": "AWS Glue Data Quality rules on the Glue table", "B": "Delete the column", "C": "Train without validation", "D": "Use Amazon Polly"},
            "A",
            "Glue Data Quality integrates with the Data Catalog and can fail jobs when rules break. Deleting features "
            "loses signal. Polly is unrelated.",
        ),
        (
            "Two teams contribute features with the same record ID but different event times. Feature Store should",
            {"A": "use a record identifier and event time for point-in-time correct joins", "B": "overwrite all history silently", "C": "ignore timestamps", "D": "store only in ElastiCache"},
            "A",
            "Feature Store supports event time for point-in-time correctness—critical to avoid label leakage. "
            "Silent overwrite breaks reproducibility. ElastiCache lacks offline store semantics.",
        ),
        (
            "PII must stay in ap-southeast-1; models train in the same region. Which constraint matters most?",
            {"A": "Data residency: S3, KMS keys, and SageMaker resources in ap-southeast-1", "B": "Replicate all data to us-east-1 for convenience", "C": "Disable encryption", "D": "Use public datasets only"},
            "A",
            "Compliance (PII/PHI, residency) requires regional control of storage and keys. Cross-region copies may "
            "violate policy. Encryption is required, not disabled.",
        ),
        (
            "Apache Flink on Managed Service for Apache Flink detects late-arriving events for sessionization. "
            "Output features land in S3 as Parquet. This pattern addresses",
            {"A": "streaming ETL with event-time windows for real-time features", "B": "batch-only reporting with no streams", "C": "DNS routing", "D": "email campaigns"},
            "A",
            "Flink is in-scope for stream processing; event-time windows handle lateness. DNS/email are unrelated.",
        ),
        (
            "Data Wrangler export should feed both SageMaker Processing and scheduled Glue jobs. You should",
            {"A": "export reproducible transformation code/recipe into the pipeline", "B": "keep transformations only in browser memory", "C": "email CSV attachments", "D": "avoid version control"},
            "A",
            "Reproducible exports enable MLOps pipelines (exam skill 1.2). Browser-only flows are not repeatable.",
        ),
        (
            "Selection bias appears because training data only includes users who completed signup. Mitigation includes",
            {"A": "revising sampling to include non-completers and measuring bias with Clarify", "B": "hiding the issue with more epochs", "C": "using larger instance types only", "D": "disabling holdout sets"},
            "A",
            "Selection bias is a pre-training concern; Clarify helps measure; sampling fixes the root cause. "
            "More epochs or bigger instances do not fix biased data collection.",
        ),
        (
            "Athena queries on nested JSON in S3 are slow and expensive. First optimization step?",
            {"A": "Convert to partitioned Parquet via CTAS or Glue ETL", "B": "Increase JSON indentation", "C": "Disable S3 versioning", "D": "Move to Snowmobile"},
            "A",
            "Columnar Parquet plus partitions reduces bytes scanned—Athena best practice. Snowmobile is bulk migration.",
        ),
        (
            "Amazon A2I should be used when",
            {"A": "human review is needed for low-confidence predictions in a loop with SageMaker", "B": "you need only S3 lifecycle rules", "C": "training without labels", "D": "replacing IAM entirely"},
            "A",
            "Augmented AI (A2I) integrates human reviewers for production ML workflows (e.g., moderation). "
            "It does not replace IAM or create labels without a workflow.",
        ),
        (
            "DynamoDB streams feed Lambda to update online features while S3 holds historical exports. This is",
            {"A": "a valid pattern for near-real-time feature updates plus offline history", "B": "invalid because DynamoDB cannot stream", "C": "only for CloudFront", "D": "replaces Feature Store always"},
            "A",
            "Streams + Lambda is a common pattern; Feature Store can still be the canonical store. DynamoDB streams exist. "
            "CloudFront is CDN.",
        ),
        (
            "Tokenization for NLP features in a visual pipeline before BERT fine-tuning can be done in",
            {"A": "SageMaker Data Wrangler or processing scripts with Hugging Face tokenizers", "B": "Route 53", "C": "AWS Budgets", "D": "Amazon SES"},
            "A",
            "Encoding/tokenization is exam knowledge (task 1.2). Route 53/Budgets/SES are unrelated.",
        ),
        (
            "Measurement bias occurs when a sensor miscalibrates for one factory. You should",
            {"A": "detect distribution differences per factory and recalibrate or exclude bad sensors", "B": "merge factories without inspection", "C": "increase learning rate", "D": "use only accuracy on training set"},
            "A",
            "Measurement bias is a data quality issue addressed in preparation, not hyperparameters alone.",
        ),
        (
            "Shuffle and split training/validation/test before upload helps",
            {"A": "reduce leakage and get unbiased performance estimates", "B": "increase S3 API cost only", "C": "eliminate need for monitoring", "D": "avoid encryption"},
            "A",
            "Proper splitting is task 1.3—prevents overly optimistic metrics and leakage.",
        ),
        (
            "Glue DataBrew is BEST for",
            {"A": "visual data preparation without writing Spark code for every transform", "B": "hosting real-time GPU inference", "C": "domain registration", "D": "VPC peering only"},
            "A",
            "DataBrew targets interactive data prep for analytics/ML consumers. It is not an inference or DNS service.",
        ),
        (
            "To accelerate repeated reads of a large S3 dataset on training nodes, you can use",
            {"A": "FSx for Lustre with lazy loading from S3 or SageMaker fast file mode", "B": "Glacier Deep Archive", "C": "Public ACL on artifacts", "D": "Disable caching entirely always"},
            "A",
            "FSx Lustre and SageMaker input modes address I/O bottlenecks (exam storage guidance).",
        ),
    ]
    for s, o, a, w in scenarios:
        items.append(q(s, o, a, w))
    return items


def _domain2():
    items = []
    scenarios = [
        (
            "Image classification with 1M labeled images and need for transfer learning. Fastest path on SageMaker?",
            {"A": "Use a pre-trained model from JumpStart and fine-tune with GPU instances", "B": "Train from random weights on CPU only", "C": "Use Amazon Translate", "D": "Only Batch Transform without training"},
            "A",
            "JumpStart provides pre-trained models; fine-tuning beats training from scratch on large vision data.",
        ),
        (
            "Random search vs Bayesian optimization for HPO with 100 trials budget on SageMaker AMT",
            {"A": "Bayesian explores promising regions faster than naive grid on large spaces", "B": "Grid always cheaper", "C": "HPO impossible on SageMaker", "D": "Only manual tuning allowed"},
            "A",
            "Exam covers Bayesian optimization in AMT for efficient search.",
        ),
        (
            "Dropout in neural networks primarily acts as",
            {"A": "regularization reducing co-adaptation of neurons", "B": "data augmentation for images", "C": "encryption", "D": "S3 replication"},
            "A",
            "Dropout is regularization (task 2.2 knowledge).",
        ),
        (
            "AUC-ROC is preferred when",
            {"A": "you care about ranking quality across thresholds for imbalanced classes", "B": "all classes are perfectly balanced and cost is zero", "C": "regression RMSE is the goal", "D": "monitoring S3 size"},
            "A",
            "ROC/AUC evaluates classifiers across thresholds—exam metric knowledge.",
        ),
        (
            "SageMaker Experiments track",
            {"A": "parameters, artifacts, and lineage across training runs", "B": "only VPC flow logs", "C": "employee badges", "D": "DNS queries"},
            "A",
            "Experiments support reproducibility (task 2.3).",
        ),
        (
            "Combining XGBoost, linear model, and neural net predictions via a meta-learner is",
            {"A": "stacking ensemble", "B": "unsupervised clustering", "C": "data drift", "D": "Glacier restore"},
            "A",
            "Stacking/ensembling is explicit exam knowledge.",
        ),
        (
            "Early stopping during training saves cost by",
            {"A": "halting when validation metric stops improving", "B": "running infinite epochs", "C": "deleting validation data", "D": "disabling checkpoints"},
            "A",
            "Early stopping is a training-time cost/performance method.",
        ),
        (
            "For multilingual sentiment at scale without custom training, consider",
            {"A": "Amazon Comprehend detect_sentiment", "B": "Amazon EBS snapshot", "C": "AWS Snowcone per tweet", "D": "Amazon MQ"},
            "A",
            "Comprehend is in-scope AI service for NLP tasks.",
        ),
        (
            "Weight decay (L2) helps by",
            {"A": "penalizing large weights to reduce overfitting", "B": "increasing model size always", "C": "encrypting gradients", "D": "replacing validation set"},
            "A",
            "L2 regularization is exam knowledge task 2.2.",
        ),
        (
            "Distributed data parallel training on SageMaker is used when",
            {"A": "dataset is large and training time must shrink across many GPUs", "B": "dataset fits in 1 MB", "C": "inference only", "D": "no need for GPUs ever"},
            "A",
            "Distributed training reduces wall-clock time (task 2.2).",
        ),
        (
            "Clarify SHAP explainability after training helps",
            {"A": "interpret feature contributions for stakeholders and debug bias", "B": "compress S3 buckets", "C": "create IAM users", "D": "replace Model Monitor"},
            "A",
            "Clarify explainability is task 2.3; distinct from production monitoring.",
        ),
        (
            "Choosing Linear Learner vs XGBoost on tabular data should consider",
            {"A": "interpretability, non-linearity, training time, and data size", "B": "only logo color", "C": "random choice", "D": "S3 region name only"},
            "A",
            "Algorithm selection weighs business constraints (task 2.1).",
        ),
        (
            "Catastrophic forgetting in continual learning is mitigated by",
            {"A": "rehearsal, regularization, or multi-task training strategies", "B": "deleting old data always without review", "C": "disabling evaluation", "D": "using only Batch Transform"},
            "A",
            "Exam mentions preventing catastrophic forgetting (task 2.2).",
        ),
        (
            "RMSE is the primary metric for",
            {"A": "regression problems", "B": "multi-class image tagging only", "C": "IAM policy size", "D": "S3 object count"},
            "A",
            "RMSE is standard regression metric in guide.",
        ),
        (
            "Personalize is appropriate when",
            {"A": "recommendations for users based on interaction history", "B": "OCR of legal PDFs only", "C": "network firewall rules", "D": "EC2 patching"},
            "A",
            "Amazon Personalize is in-scope ML service for recommendations.",
        ),
    ]
    for s, o, a, w in scenarios:
        items.append(q(s, o, a, w))
    return items


def _domain3():
    items = []
    scenarios = [
        (
            "Traffic is unpredictable with long idle periods; cold starts up to seconds are acceptable. Choose",
            {"A": "SageMaker Serverless Inference", "B": "Always-on ml.g5.12xlarge cluster", "C": "Snowball Edge", "D": "Amazon WorkSpaces"},
            "A",
            "Serverless inference scales to zero and charges per invocation—good for sporadic traffic.",
        ),
        (
            "CodeDeploy-style linear deployment for endpoints means",
            {"A": "gradually increasing traffic to the new variant while monitoring", "B": "instant cutover with zero monitoring", "C": "deleting old model artifacts", "D": "training inside the endpoint"},
            "A",
            "Linear/canary shifts are exam deployment strategies.",
        ),
        (
            "MWAA (Managed Airflow) is chosen when",
            {"A": "existing Airflow DAGs orchestrate ETL and SageMaker jobs", "B": "you need a NoSQL database", "C": "you want to eliminate orchestration", "D": "only for static websites"},
            "A",
            "MWAA is in-scope orchestrator alongside SageMaker Pipelines.",
        ),
        (
            "Step Functions can",
            {"A": "coordinate Lambda, SageMaker jobs, and human approval steps in a state machine", "B": "only send email", "C": "replace S3", "D": "train models without data"},
            "A",
            "Step Functions integrates ML workflows in exam scope.",
        ),
        (
            "ECR image scanning in CI/CD helps",
            {"A": "catch vulnerabilities before deploying inference containers", "B": "tune hyperparameters", "C": "label images", "D": "calculate AUC"},
            "A",
            "Container security is part of deployment best practices.",
        ),
        (
            "Provisioned concurrency on Lambda (when used for ML) reduces",
            {"A": "cold start latency for latency-sensitive sporadic models", "B": "training time on 8 GPUs", "C": "S3 storage cost", "D": "need for any IAM roles"},
            "A",
            "Provisioned concurrency addresses cold starts—task 4.2 capacity knowledge.",
        ),
        (
            "Deploying the same model to EKS instead of SageMaker endpoints is chosen when",
            {"A": "Kubernetes is the standard platform and custom serving stack exists", "B": "you never need containers", "C": "data must not be encrypted", "D": "you want zero orchestration"},
            "A",
            "EKS/ECS are valid deployment targets per task 3.1.",
        ),
        (
            "GitFlow in ML CI/CD typically means",
            {
                "A": "release branches gate production pipeline runs with approvals",
                "B": "no version control",
                "C": "only manual deploys from laptops",
                "D": "shared root credentials in CodeBuild",
            },
            "A",
            "Git branching models integrate with CodePipeline (task 3.3).",
        ),
        (
            "Integration test in ML pipeline should verify",
            {"A": "pipeline stages produce expected artifacts and endpoint health checks pass", "B": "only README spelling", "C": "employee satisfaction", "D": "DNS TTL only"},
            "A",
            "Automated tests include integration/end-to-end per exam.",
        ),
        (
            "Retraining trigger on schema drift should use",
            {"A": "EventBridge + Model Monitor/Data Quality alerts → Pipeline execution", "B": "random cron yearly only", "C": "disabling monitoring", "D": "public webhook without auth"},
            "A",
            "Event-driven retraining is core MLOps orchestration.",
        ),
        (
            "Neo compiles models for",
            {"A": "edge devices with optimized binaries", "B": "S3 Glacier", "C": "IAM policy editor", "D": "Amazon Chime"},
            "A",
            "Neo is edge optimization (task 3.1).",
        ),
        (
            "Multi-container endpoint hosts",
            {"A": "multiple containers in one endpoint (e.g., pre/post processing + model)", "B": "only one algorithm globally", "C": "data without inference", "D": "Route 53 records"},
            "A",
            "Multi-container endpoints are explicit SageMaker capability.",
        ),
        (
            "On-demand vs provisioned SageMaker inference capacity",
            {"A": "on-demand instances scale with traffic; provisioned sets baseline capacity", "B": "they are identical", "C": "only Snowball provisioned", "D": "neither uses EC2"},
            "A",
            "Task 3.2 knowledge: on-demand vs provisioned resources.",
        ),
        (
            "CodeBuild in ML CI/CD runs",
            {"A": "unit tests, docker build, and artifact packaging", "B": "only billing reports", "C": "DNS failover", "D": "ground truth labeling alone"},
            "A",
            "CodeBuild compiles/tests/builds images—task 3.3.",
        ),
        (
            "Hosting on Lambda for inference limits include",
            {"A": "package size, memory, and timeout constraints vs large GPU models", "B": "unlimited 30-minute GPU training", "C": "no need for IAM", "D": "automatic petabyte scaling"},
            "A",
            "Lambda suits small models; large GPU workloads use SageMaker endpoints.",
        ),
    ]
    for s, o, a, w in scenarios:
        items.append(q(s, o, a, w))
    return items


def _domain4():
    items = []
    scenarios = [
        (
            "Model Monitor bias drift schedule compares",
            {"A": "live predictions/features to baseline for fairness metrics over time", "B": "S3 bucket names only", "C": "employee IDs", "D": "CloudFront cache"},
            "A",
            "Bias drift monitoring is SageMaker Clarify/Model Monitor capability.",
        ),
        (
            "CloudWatch alarm on Invocations and ModelLatency for an endpoint helps",
            {
                "A": "detect performance regressions after deploy",
                "B": "train faster",
                "C": "replace KMS",
                "D": "eliminate VPC",
            },
            "A",
            "Infrastructure and model latency monitoring are task 4.1/4.2 skills.",
        ),
        (
            "Trusted Advisor can recommend",
            {"A": "cost optimization and security improvements for ML resources", "B": "hyperparameter values", "C": "labeling bounding boxes", "D": "SQL query plans only"},
            "A",
            "Trusted Advisor is in-scope cost/security tool.",
        ),
        (
            "SageMaker Savings Plans apply to",
            {"A": "committed SageMaker compute usage for cost reduction", "B": "S3 Glacier retrieval only", "C": "IAM MFA", "D": "Route 53 domains"},
            "A",
            "Savings Plans appear in cost optimization task 4.2.",
        ),
        (
            "VPC interface endpoint for SageMaker API allows",
            {"A": "private connectivity without traversing the public internet", "B": "public anonymous access", "C": "disabling security groups", "D": "removing encryption"},
            "A",
            "Private connectivity is network security best practice.",
        ),
        (
            "SageMaker Role Manager helps",
            {"A": "create least-privilege IAM roles tailored to SageMaker personas", "B": "delete all logs", "C": "open security groups to 0.0.0.0/0", "D": "disable MFA"},
            "A",
            "Role Manager is in-scope IAM helper for ML.",
        ),
        (
            "X-Ray tracing on inference microservices helps",
            {"A": "find latency bottlenecks across Lambda/API Gateway/SageMaker", "B": "compute F1 score", "C": "label data", "D": "tune learning rate"},
            "A",
            "X-Ray is observability for distributed inference paths.",
        ),
        (
            "A/B testing on SageMaker endpoint variants routes",
            {"A": "percentage of traffic to each variant to compare metrics", "B": "all traffic blindly to untested model", "C": "only DNS queries", "D": "training data"},
            "A",
            "A/B on variants is production comparison technique (task 4.1).",
        ),
        (
            "QuickSight dashboards for ML ops can visualize",
            {"A": "business KPIs plus CloudWatch-exported operational metrics", "B": "only IAM policies", "C": "raw binary weights", "D": "Git merge conflicts"},
            "A",
            "QuickSight is in-scope for dashboards (task 4.2).",
        ),
        (
            "Secrets in CodePipeline should",
            {"A": "use Secrets Manager or SSM Parameter Store with IAM-scoped access", "B": "be hard-coded in buildspec.yml committed to Git", "C": "posted in Slack", "D": "embedded in public AMIs"},
            "A",
            "CI/CD security best practices forbid hard-coded secrets.",
        ),
        (
            "Service quotas on SageMaker endpoints require",
            {"A": "monitoring utilization and requesting limit increases before launch", "B": "ignoring limits", "C": "using root for all calls", "D": "disabling auto scaling always"},
            "A",
            "Capacity troubleshooting includes quotas (task 4.2).",
        ),
        (
            "Config rules (AWS Config) can",
            {"A": "detect non-compliant SageMaker or S3 settings for governance", "B": "train neural networks", "C": "perform HPO", "D": "replace Model Registry"},
            "A",
            "AWS Config is in-scope governance service.",
        ),
        (
            "DevOps Guru for ML workloads can",
            {"A": "surface operational anomalies using ML on telemetry", "B": "label images", "C": "compile Neo models", "D": "replace CloudTrail"},
            "A",
            "DevOps Guru is in-scope for anomaly detection.",
        ),
        (
            "Encrypting inter-node training traffic in VPC uses",
            {"A": "security groups, NACLs, and optional TLS in distributed frameworks", "B": "public S3 ACLs", "C": "disabling IAM", "D": "sharing access keys in notebook"},
            "A",
            "Network controls and encryption protect training clusters.",
        ),
        (
            "Budgets alerts at 80% forecasted spend help",
            {"A": "proactively control ML experimentation costs", "B": "improve model accuracy directly", "C": "replace tagging", "D": "eliminate CloudWatch"},
            "A",
            "AWS Budgets is explicit cost tool in domain 4.",
        ),
    ]
    for s, o, a, w in scenarios:
        items.append(q(s, o, a, w))
    return items
