#!/usr/bin/env python3
"""Generate AWS MLA-C01 (ML Engineer / MLOps Associate) practice questions."""

from __future__ import annotations

import html
from pathlib import Path

from mla_question_bank import all_questions, q

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "study" / "aws-mla-c01-practice-questions.md"
BLOG_CONTENT = ROOT / "content" / "blogs" / "aws-mla-c01-practice-questions.html"
PUBLISHED = "2026-06-18"

# Curated core questions (high-quality scenarios)
CORE = [
    q(
        "A data team stores 2 TB of clickstream logs accessed mostly by column (user_id, event_type, timestamp). "
        "They run nightly Spark jobs on EMR and occasional ad-hoc Athena queries. Which storage format best balances "
        "cost and query performance?",
        {
            "A": "JSON files in Amazon S3 with gzip compression",
            "B": "Apache Parquet with Snappy compression partitioned by date",
            "C": "CSV without compression for human readability",
            "D": "Amazon EBS gp3 volumes attached to a single EC2 instance",
        },
        "B",
        "Parquet is columnar: Spark and Athena read only needed columns, reducing I/O versus row formats like JSON/CSV. "
        "Snappy gives fast compression/decompression suitable for big data. Partitioning by date limits scan scope. "
        "EBS on one instance does not scale for shared analytics lakes.",
    ),
    q(
        "An ML engineer must land real-time fraud features into a feature store while also archiving raw events for "
        "compliance. Which architecture satisfies both paths?",
        {
            "A": "Kinesis Data Streams → Lambda → SageMaker Feature Store; parallel Firehose delivery to S3",
            "B": "S3 PUT events only, with no streaming layer",
            "C": "Amazon RDS Multi-AZ as the sole ingestion point",
            "D": "AWS Snowball Edge for every transaction",
        },
        "A",
        "Kinesis ingests streams; Lambda writes online features; Firehose archives to S3 for audit/replay.",
    ),
    q(
        "Before training a credit model, you must detect label imbalance across protected groups. Which AWS tool is "
        "purpose-built for pre-training bias metrics (e.g., CI, DPL)?",
        {"A": "Amazon Macie", "B": "SageMaker Clarify pre-training bias analysis", "C": "AWS WAF", "D": "Amazon CloudFront"},
        "B",
        "Clarify computes CI, DPL, and related pre-training metrics. Macie finds sensitive data; WAF/CloudFront are edge security/CDN.",
    ),
    q(
        "A tabular regression problem has 50k rows and strong linear relationships. Fast baseline on SageMaker?",
        {"A": "Linear Learner", "B": "Object Detection", "C": "BlazingText Word2Vec only", "D": "Seq2Seq"},
        "A",
        "Linear Learner fits tabular regression/classification. Others target vision, embeddings, or sequences.",
    ),
    q(
        "Hyperparameter search across 20 continuous parameters with limited budget—smarter than naive grid?",
        {"A": "SageMaker Automatic Model Tuning (Bayesian optimization)", "B": "S3 Intelligent-Tiering only", "C": "Manual prod endpoint tweak", "D": "Amazon Connect flows"},
        "A",
        "AMT supports Bayesian optimization for efficient search in large spaces.",
    ),
    q(
        "Model versions must be approved before production with audit trail.",
        {"A": "SageMaker Model Registry", "B": "Public S3 ACL", "C": "Disable CloudTrail", "D": "Amazon Polly lexicons"},
        "A",
        "Model Registry tracks packages and approval status for governed promotion.",
    ),
    q(
        "Sub-second synchronous predictions 24/7 with autoscaling.",
        {"A": "Real-time inference endpoint", "B": "Batch Transform only", "C": "Glacier retrieval per request", "D": "WorkDocs"},
        "A",
        "Real-time endpoints serve low-latency InvokeEndpoint traffic with auto scaling.",
    ),
    q(
        "Monthly scoring of 10M records, no low-latency requirement.",
        {"A": "SageMaker Batch Transform", "B": "Always-on multi-GPU endpoint", "C": "Lambda@Edge per row sync", "D": "SES"},
        "A",
        "Batch Transform is cost-effective bulk offline inference from/to S3.",
    ),
    q(
        "Payloads up to 1 GB; client polls for results within minutes.",
        {"A": "Asynchronous inference endpoint", "B": "Serverless endpoint for 1 GB sync", "C": "Batch with 1s row SLA", "D": "Translate API"},
        "A",
        "Async inference queues large requests and writes output to S3 when complete.",
    ),
    q(
        "Five small sklearn models on one GPU to save cost.",
        {"A": "Multi-Model Endpoint", "B": "Five AWS accounts only", "C": "Lightsail DB", "D": "DeepRacer"},
        "A",
        "MME hosts multiple models from S3 behind one endpoint.",
    ),
    q(
        "CI/CD on main: build image, test, train, register model.",
        {"A": "CodePipeline + CodeBuild + SageMaker Pipelines", "B": "Manual SSH", "C": "Pinpoint only", "D": "No Git"},
        "A",
        "Exam expects CodePipeline/CodeBuild integrated with SageMaker Pipelines.",
    ),
    q(
        "Production accuracy drops; input feature distributions shifted.",
        {"A": "Data drift — Model Monitor data quality baseline", "B": "IAM drift only", "C": "Intelligent-Tiering", "D": "RI expiration"},
        "A",
        "Data drift is input distribution change detected vs training baseline.",
    ),
    q(
        "Least-privilege notebook access to one S3 prefix and KMS-encrypted artifacts.",
        {"A": "Scoped IAM execution role with kms:Decrypt on the CMK", "B": "Root access keys in notebook", "C": "s3:* on *", "D": "Public bucket ACL"},
        "A",
        "SageMaker assumes IAM roles; scope resources and KMS grants.",
    ),
    q(
        "Endpoint only reachable from corporate VPC applications.",
        {"A": "VPC config with private subnets and restrictive security groups", "B": "Public InvokeEndpoint for all", "C": "Remove security groups", "D": "Public GitHub model repo"},
        "A",
        "VPC-hosted endpoints keep inference off the public internet.",
    ),
    q(
        "Right-size inference instance before launch.",
        {"A": "SageMaker Inference Recommender", "B": "Amazon Translate", "C": "DeepRacer", "D": "SES bounces"},
        "A",
        "Inference Recommender load-tests candidate instance types.",
    ),
]


def _matrix_questions() -> list:
    """Generate unique questions from service × concern matrix."""
    matrix = [
        ("Glue Crawler", "populate the Glue Data Catalog from S3", "A", "enables discoverable schema for ETL and Athena"),
        ("Data Sync", "migrate on-premises NFS datasets to S3 for training", "A", "hybrid ingest for large legacy stores"),
        ("Lake Formation", "apply tag-based access control on the data lake", "A", "governed sharing for feature teams"),
        ("OpenSearch", "power vector/text hybrid search features for RAG sidecars", "A", "in-scope analytics search service"),
        ("Redshift", "warehouse joins for feature engineering at scale", "A", "structured analytics before SageMaker"),
        ("EMR Serverless", "run Spark without managing long-lived clusters", "A", "cost-aware batch feature generation"),
        ("SNS", "notify on-call when Model Monitor violation fires", "A", "integration for operational alerts"),
        ("SQS", "buffer retraining requests from many producers", "A", "decouple pipeline triggers"),
        ("Lookout for Metrics", "detect anomalies in operational KPI time series", "A", "managed anomaly detection"),
        ("Lookout for Vision", "defect detection with custom vision models", "A", "specialized CV service when not using custom SageMaker"),
        ("Fraud Detector", "online fraud scoring with AWS-managed models", "A", "pre-built fraud ML service"),
        ("Textract", "extract text from scanned forms for NLP features", "A", "document ML ingest"),
        ("Transcribe", "speech-to-text for audio feature pipelines", "A", "audio AI service in scope"),
        ("Lex", "build conversational bots—not primary batch training", "A", "NLP conversational service"),
        ("Kendra", "enterprise search over documents", "A", "RAG/search complement"),
        ("CodeArtifact", "store Python dependencies for reproducible training images", "A", "artifact repo for builds"),
        ("CloudFormation", "declare SageMaker Domain and execution roles as code", "A", "IaC reproducibility"),
        ("CDK", "define pipeline stacks in TypeScript/Python", "A", "IaC alternative in scope"),
        ("Auto Scaling", "scale endpoint instances on InvocationsPerInstance", "A", "elastic inference capacity"),
        ("Systems Manager", "patch and manage notebook instances/hosts", "A", "ops management in scope"),
        ("Macie", "discover PII in S3 before labeling", "A", "sensitive data discovery"),
        ("KMS", "encrypt model artifacts at rest with CMK policies", "A", "encryption control plane"),
        ("CloudTrail", "audit CreateEndpoint and UpdateEndpoint API calls", "A", "API audit trail"),
        ("Cost Explorer", "analyze SageMaker spend by tag", "A", "cost visibility"),
        ("Compute Optimizer", "recommend smaller inference instances", "A", "rightsizing recommendations"),
        ("Model Monitor", "schedule data quality against training baseline", "A", "production data drift detection"),
        ("Debugger", "capture tensors to detect vanishing gradients", "A", "training convergence debug"),
        ("Processing Job", "run Spark/scikit preprocessing at scale", "A", "managed feature engineering jobs"),
        ("Training Job", "run distributed GPU script mode", "A", "core training primitive"),
        ("Pipeline", "DAG of Processing/Training/Register steps", "A", "native ML workflow orchestration"),
        ("JumpStart", "deploy pre-trained models quickly", "A", "accelerator for common architectures"),
        ("Bedrock", "invoke foundation models without self-hosting weights", "A", "managed FM inference"),
        ("Rekognition", "face/object APIs without custom training", "A", "vision AI service"),
        ("Comprehend Medical", "PHI-aware NLP on clinical text", "A", "healthcare NLP service"),
        ("Elastic Inference", "attach accelerator to CPU instances (legacy pattern)", "A", "cost inference acceleration where applicable"),
        ("Batch", "run containerized batch scoring jobs at scale", "A", "non-SageMaker batch compute option"),
        ("ECS", "run custom inference containers orchestrated by ECS", "A", "container deployment target"),
        ("API Gateway", "expose Lambda/SageMaker behind REST API", "A", "edge API for ML microservices"),
        ("Lambda", "lightweight inference for sporadic low-volume models", "A", "serverless inference pattern"),
        ("EventBridge", "react to S3 Object Created for pipelines", "A", "event-driven MLOps"),
        ("DataBrew", "visual profiling and recipes without Spark code", "A", "interactive data prep"),
        ("Ground Truth", "managed labeling with quality controls", "A", "dataset labeling at scale"),
        ("Feature Store", "online/offline feature consistency", "A", "feature management service"),
        ("Clarify", "SHAP and bias reports", "A", "explainability and fairness insights"),
        ("Model Registry", "governed model promotion", "A", "versioning and approvals"),
        ("Neo", "compile models for edge hardware", "A", "edge optimization"),
        ("Inference Recommender", "benchmark latency/throughput across instances", "A", "sizing guidance"),
        ("Spot Training", "discount training with checkpoint resume", "A", "cost-optimized training"),
        ("Shadow variant", "compare new model on copied traffic", "A", "safe production evaluation"),
        ("Canary deployment", "shift small traffic % then increase", "A", "risk-managed rollout"),
        ("Blue/green deployment", "parallel stacks then switch traffic", "A", "rollback-friendly release"),
        ("GitHub Actions (via CodeSuite)", "trigger CodePipeline from repo webhook", "A", "CI integration pattern"),
        ("Buildspec", "define CodeBuild phases for test and docker build", "A", "CI build definition"),
        ("Approval stage", "manual gate in CodePipeline before prod deploy", "A", "human-in-the-loop governance"),
        ("Tagging strategy", "allocate ML costs to cost centers", "A", "financial governance"),
        ("Budgets", "alert when forecast exceeds monthly ML cap", "A", "proactive spend control"),
        ("QuickSight", "dashboard model KPIs for business users", "A", "BI visualization"),
        ("CloudWatch Logs Insights", "query inference logs for errors", "A", "log analytics"),
        ("X-Ray", "trace latency across microservices", "A", "distributed tracing"),
        ("VPC endpoints", "private S3/SageMaker access without NAT", "A", "network isolation"),
        ("Security group", "restrict endpoint ENI to app subnet CIDR", "A", "network ACL at instance level"),
        ("IAM condition keys", "restrict SageMaker actions by vpc/tag", "A", "fine-grained authorization"),
        ("Bucket policy", "deny non-TLS S3 access for artifacts", "A", "data perimeter control"),
        ("SSE-S3 vs SSE-KMS", "customer-managed keys for compliance", "A", "KMS for key policy control"),
        ("Cross-account role", "allow central tooling account to deploy models", "A", "enterprise access pattern"),
        ("SageMaker Studio", "collaborative IDE for experiments", "A", "unified ML IDE"),
        ("Lifecycle config", "automate notebook setup scripts", "A", "repeatable dev environments"),
        ("Pipe input mode", "stream S3 data without full download", "A", "training I/O optimization"),
        ("File input mode", "copy dataset to training volume", "A", "when repeated local reads help"),
        ("FastFile mode", "optimized mount for large datasets", "A", "reduced startup for big data"),
        ("Hyperparameter", "batch size affects memory and convergence", "A", "tuning impacts training stability"),
        ("Epoch vs step", "epoch is full pass; step is one batch update", "A", "training vocabulary"),
        ("Ensembling", "combine models to reduce variance", "A", "performance technique"),
        ("Pruning", "remove weights to shrink model size", "A", "compression technique in scope"),
        ("Heat map", "visualize CNN focus for debugging", "A", "evaluation visualization"),
        ("Confusion matrix", "see per-class errors", "A", "classification evaluation"),
        ("Precision/recall tradeoff", "tune threshold for fraud use cases", "A", "metric interpretation"),
        ("Underfitting", "high error on train and validation", "A", "needs more capacity or features"),
        ("Overfitting", "low train error, high validation error", "A", "needs regularization or more data"),
        ("Concept drift", "P(Y|X) changes over time", "A", "monitor model quality metrics"),
        ("Label leakage", "features contain future information", "A", "prevent with point-in-time joins"),
        ("One-hot encoding", "categorical to binary columns", "A", "encoding technique task 1.2"),
        ("Binning", "discretize continuous variables", "A", "feature engineering technique"),
        ("Log transform", "stabilize skewed numeric features", "A", "feature engineering technique"),
        ("RecordIO protobuf", "efficient SageMaker built-in ingest", "A", "format for algorithms"),
        ("ORC", "columnar alternative to Parquet", "A", "valid lake format"),
        ("Avro", "schema evolution friendly row format", "A", "common in Kafka sinks"),
        ("Kinesis shard", "parallelism unit for streams", "A", "streaming scalability concept"),
        ("Firehose buffering", "batch small records to S3 objects", "A", "efficient land in lake"),
        ("Mechanical Turk", "crowd labeling integrated via Ground Truth", "A", "labeling workforce option"),
        ("A2I", "human review loop for low-confidence predictions", "A", "human-in-the-loop production"),
        ("Personalize", "real-time recommendations API", "A", "recommendation service"),
        ("Polly", "text-to-speech—not training labels", "A", "speech synthesis service"),
        ("Translate", "language translation API", "A", "NLP service selection"),
        ("HealthLake", "FHIR data store for healthcare analytics", "A", "health data service"),
        ("CodeGuru", "ML-powered code review for quality", "A", "dev quality tool in ML category"),
        ("SageMaker Edge Manager", "manage edge deployments (where used)", "A", "edge lifecycle complement to Neo"),
        ("Multi-container endpoint", "sidecar preprocessing container", "A", "deploy pre/post with model"),
        ("Async inference notification", "SNS when inference output ready", "A", "client notification pattern"),
        ("Serverless inference", "scale to zero with cold starts", "A", "intermittent traffic pattern"),
        ("Real-time multi-variant", "A/B traffic split on endpoint", "A", "production experimentation"),
        ("Batch Transform manifest", "list S3 objects to score", "A", "batch input format"),
        ("Model package group", "organize versions in registry", "A", "registry structure"),
        ("Pipeline parameter", "pass dynamic config between steps", "A", "parameterized workflows"),
        ("CacheConfig on pipeline step", "reuse outputs when inputs unchanged", "A", "pipeline cost optimization"),
        ("Retry policy", "handle transient training failures", "A", "resilient orchestration"),
        ("Spot failure", "checkpoint resume from S3", "A", "fault-tolerant spot training"),
        ("VPC-only S3 gateway endpoint", "keep data plane private", "A", "network cost/privacy"),
        ("NAT gateway", "allow private subnet outbound for pip install", "A", "egress for package installs"),
        ("Interface endpoint", "private connectivity to SageMaker API", "A", "privateLink pattern"),
        ("S3 Transfer Acceleration", "faster cross-region uploads", "A", "distant client ingest"),
        ("S3 lifecycle", "transition old artifacts to IA/Glacier", "A", "artifact cost control"),
        ("DynamoDB feature", "low-latency key-value online features", "A", "alternative online store pattern"),
        ("ElastiCache", "caching layer—not full feature store", "A", "cache vs feature store distinction"),
        ("RDS", "transactional source—not primary lake", "A", "OLTP vs analytics separation"),
        ("DocumentDB", "document source for features", "A", "NoSQL ingest option"),
        ("Neptune", "graph relationships as features", "A", "graph ML ingest"),
        ("Athena CTAS", "create Parquet tables from queries", "A", "lake transformation pattern"),
        ("Glue bookmark", "incremental ETL processing", "A", "incremental pipeline state"),
        ("Spark on Glue", "distributed transform for features", "A", "serverless Spark option"),
        ("EMR cluster", "long-running Spark when always-on needed", "A", "cluster tradeoff vs Serverless"),
        ("Data Quality ruleset", "fail job on null rate threshold", "A", "quality gate before training"),
        ("Clarify DPL", "difference in proportions of labels across groups", "A", "bias metric name"),
        ("Clarify CI", "class imbalance measure", "A", "bias metric name"),
        ("Synthetic data", "balance rare classes", "A", "mitigate imbalance"),
        ("Augmentation", "expand training images via transforms", "A", "vision regularization/data volume"),
        ("Train/val/test split", "unbiased estimate of generalization", "A", "fundamental modeling practice"),
        ("Random seed", "reproducible experiments", "A", "experiment tracking practice"),
        ("Script mode", "bring custom training script", "A", "custom framework training"),
        ("BYOC inference", "custom inference container from ECR", "A", "custom serving stack"),
        ("Estimator.fit", "start SageMaker training job via SDK", "A", "SDK training invocation"),
        ("Predictor", "high-level deploy from trained estimator", "A", "SDK deployment helper"),
        ("HPO metric", "objective metric for AMT jobs", "A", "tuning optimization target"),
        ("Early stopping rule", "stop unpromising training jobs in HPO", "A", "save tuning budget"),
        ("Warm start tuning", "use prior tuning job results", "A", "accelerate HPO"),
        ("Managed Spot Training", "use Spot instances for Training jobs", "A", "training cost optimization"),
        ("Training Compiler", "optimize models for faster training/inference", "A", "compilation optimization"),
        ("Model parallelism", "split large models across GPUs", "A", "large model training"),
        ("Data parallelism", "split batches across replicas", "A", "scale training throughput"),
        ("Pipe mode", "stream data from S3 during training", "A", "I/O optimization"),
        ("Manifest file", "list of training samples in S3", "A", "input definition pattern"),
        ("Augmented manifest", "bounding boxes for object detection", "A", "structured label format"),
        ("Bring your own algorithm", "custom Docker training image", "A", "maximum training flexibility"),
        ("Multi-record batch inference", "batch multiple rows per request on endpoint", "A", "throughput optimization"),
        ("Auto scaling target", "TargetTrackingScaling on CPU or custom metric", "A", "scaling policy type"),
        ("Scale-in cooldown", "prevent flapping when traffic drops", "A", "stability of autoscaling"),
        ("Provisioned throughput mode", "reserved capacity pattern (where applicable)", "A", "capacity planning concept"),
        ("Shadow production variant", "no user impact from shadow responses", "A", "safe comparison"),
        ("Production variant weight", "traffic split percentage", "A", "A/B configuration"),
        ("Endpoint config", "immutable definition of variants and instances", "A", "deployment artifact"),
        ("UpdateEndpoint", "move endpoint to new config with rollout", "A", "deployment API"),
        ("Rollback", "revert to previous endpoint config on alarms", "A", "operational safety"),
        ("Integration test in pipeline", "invoke endpoint with sample payload", "A", "automated quality gate"),
        ("Unit test in CodeBuild", "validate data transform functions", "A", "shift-left quality"),
        ("Gitflow release branch", "production pipeline triggered from release/*", "A", "branching strategy"),
        ("Artifact encryption", "encrypt CodePipeline artifacts with KMS", "A", "CI/CD security"),
        ("Least privilege build role", "CodeBuild role scoped to ECR and S3 prefixes", "A", "pipeline IAM best practice"),
        ("CloudWatch alarm on 5xx", "page ops when inference errors spike", "A", "operational monitoring"),
        ("Custom metric", "publish business KPI from inference container", "A", "application-level monitoring"),
        ("Log group retention", "control storage cost of verbose inference logs", "A", "log cost management"),
        ("PII in logs", "mask or exclude from CloudWatch", "A", "compliance in observability"),
        ("Organizations SCP", "prevent use of unapproved regions for ML", "A", "guardrail at org level"),
        ("Service Catalog", "approved SageMaker products for teams", "A", "governed self-service"),
        ("Chatbot", "Slack notifications from CloudWatch alarms", "A", "ops integration"),
        ("Trusted Advisor check", "underutilized SageMaker endpoints", "A", "waste identification"),
        ("Savings Plans", "commit to consistent SageMaker compute", "A", "discount for steady workloads"),
        ("RI", "reserve instances for always-on endpoints", "A", "predictable baseline cost"),
        ("Spot for inference", "generally avoided for steady SLA real-time", "A", "Spot better for fault-tolerant batch/train"),
        ("Rightsizing notebook", "stop idle Studio apps to save cost", "A", "dev environment cost control"),
        ("Separate accounts", "dev/stage/prod isolation for ML", "A", "blast radius reduction"),
        ("Cross-region replication", "DR for model artifacts—watch residency", "A", "BC/DR vs compliance tradeoff"),
        ("Model card", "document intended use and limitations", "A", "governance documentation practice"),
        ("Human review bias", "diverse labelers in Ground Truth", "A", "labeling quality practice"),
        ("Inter-annotator agreement", "measure labeling quality", "A", "Ground Truth quality mechanism"),
        ("Active learning", "label uncertain samples first", "A", "efficient labeling strategy"),
        ("Transfer learning", "fine-tune vs train from scratch", "A", "faster convergence with less data"),
        ("Foundation model", "large pre-trained model adapted downstream", "A", "modern NLP/CV approach"),
        ("Prompt engineering", "optimize inputs to FM APIs", "A", "Bedrock usage pattern"),
        ("RAG", "retrieve context then generate answer", "A", "reduce hallucination pattern"),
        ("Batch inference pipeline", "scheduled Batch Transform after ETL", "A", "scheduled scoring pattern"),
        ("Streaming inference", "Kinesis + SageMaker Processing/Endpoints", "A", "near-real-time pattern"),
        ("Feature pipeline CI", "test feature code on PR in CodeBuild", "A", "feature store governance"),
        ("Data contract", "schema expectations between teams", "A", "prevent breaking changes"),
        ("Schema registry", "Glue schema version for Avro/JSON", "A", "evolution control"),
        ("PII masking", "tokenize before labeling", "A", "privacy technique"),
        ("Differential privacy", "add noise for privacy (awareness)", "A", "advanced privacy concept"),
        ("Model bias post-training", "Clarify post-training bias metrics", "A", "fairness after training"),
        ("Explainability threshold", "SHAP for regulated decisions", "A", "interpretability requirement"),
        ("Adversarial robustness", "awareness for security testing models", "A", "ML security awareness"),
        ("Endpoint TLS", "encrypt data in transit to InvokeEndpoint", "A", "encryption in transit"),
        ("mTLS", "mutual TLS for service-to-service", "A", "advanced auth pattern"),
        ("PrivateLink", "consumer VPC accesses SageMaker privately", "A", "private connectivity"),
        ("IAM PassRole", "pipeline must pass SageMaker execution role", "A", "common permission error"),
        ("Resource-based policy", "S3 bucket policy allowing SageMaker role", "A", "cross-service access"),
        ("Condition aws:SourceVpc", "restrict S3 access to VPC endpoint", "A", "data exfiltration prevention"),
        ("Audit model lineage", "Registry + Pipeline execution ARN", "A", "traceability for compliance"),
        ("Retrain on schedule", "EventBridge cron starts Pipeline", "A", "scheduled refresh"),
        ("Retrain on drift", "CloudWatch alarm → Lambda → Pipeline", "A", "conditional refresh"),
        ("Champion/challenger", "challenger variant gets minority traffic", "A", "continuous evaluation pattern"),
        ("Holdout set", "never used during HPO to avoid leakage", "A", "honest final evaluation"),
        ("Cross-validation", "k-fold on training for robust metrics", "A", "evaluation technique"),
        ("Stratified split", "preserve class ratios in splits", "A", "imbalanced data practice"),
        ("SMOTE", "synthetic minority oversampling technique", "A", "imbalance handling option"),
        ("Class weights", "penalize misclassification of rare class", "A", "algorithm-level imbalance handling"),
        ("Threshold tuning", "adjust decision threshold on validation", "A", "optimize precision/recall"),
        ("Calibration", "align predicted probabilities with outcomes", "A", "probability quality"),
        ("Multiclass vs multilabel", "choose appropriate loss and metrics", "A", "problem framing"),
        ("Object detection metric", "mAP vs simple accuracy", "A", "CV evaluation awareness"),
        ("Segmentation", "pixel-level masks—specialized algorithms", "A", "CV task type"),
        ("Time series", "forecasting algorithms (DeepAR etc.)", "A", "SageMaker forecasting domain"),
        ("Cold start recommendation", "Personalize campaign for new users", "A", "recommendation feature"),
        ("Real-time vs batch features", "online store vs offline store latency", "A", "Feature Store architecture"),
        ("Point-in-time query", "join features as of event timestamp", "A", "prevent leakage"),
        ("Feature group", "logical collection in Feature Store", "A", "Feature Store primitive"),
        ("Offline store S3", "historical features for training", "A", "batch training data source"),
        ("Online store DynamoDB", "low-latency serving layer", "A", "inference feature retrieval"),
        ("TTL on features", "expire stale online features", "A", "freshness control"),
        ("Backfill pipeline", "populate historical features", "A", "Feature Store operations"),
        ("Ingestion notebook", "explore before production pipeline", "A", "iterative then operationalize"),
        ("Parameter Store", "non-secret config for pipelines", "A", "configuration management"),
        ("Secrets rotation", "rotate DB creds without downtime", "A", "Secrets Manager capability"),
        ("Build cache in CodeBuild", "speed docker layer rebuilds", "A", "CI performance"),
        ("Immutable tags in ECR", "prevent image overwrite", "A", "supply chain integrity"),
        ("Image signing", "verify trusted inference images", "A", "supply chain security awareness"),
        ("Airflow sensor", "wait for S3 prefix in MWAA DAG", "A", "orchestration dependency"),
        ("SageMaker pipeline callback", "integrate external approval systems", "A", "enterprise integration"),
        ("Lambda step in pipeline", "lightweight custom logic between steps", "A", "pipeline extensibility"),
        ("Conditional step", "branch on metric threshold in pipeline", "A", "gated promotion"),
        ("Register step", "register model package after training", "A", "registry integration"),
        ("CreateModel step", "create deployable model entity", "A", "deployment prep step"),
        ("Transform step", "batch score in pipeline", "A", "validation scoring in CI"),
        ("PropertyFile", "pass evaluation report to approval step", "A", "metric-based gates"),
        ("Model approval status", "Approved vs Rejected in registry", "A", "governance gate"),
        ("Endpoint auto rollback", "CloudWatch alarm triggers config revert", "A", "automated safety"),
        ("Inference payload format", "CSV, JSON, or NPY for InvokeEndpoint", "A", "client integration detail"),
        ("Content-Type header", "required for correct deserialization", "A", "inference API detail"),
        ("Target variant header", "route to specific production variant", "A", "testing specific variant"),
        ("Capture data", "enable data capture for Model Monitor", "A", "production baseline updates"),
        ("Ground truth labels for monitor", "upload labels to compare model quality", "A", "supervised monitor setup"),
        ("Schedule hourly monitor", "cron on Model Monitor schedule", "A", "continuous validation"),
        ("Violations SNS", "alert when constraints breached", "A", "operational response"),
        ("Rebaselining", "update monitor baseline after approved drift", "A", "lifecycle management"),
        ("Training job tags", "cost allocation on training spend", "A", "financial governance"),
        ("Inference tags", "allocate endpoint costs", "A", "financial governance"),
        ("Idle endpoint detection", "zero invocations but running instances", "A", "waste to eliminate"),
        ("Multi-AZ", "RDS for feature source HA—not endpoint HA alone", "A", "data source availability"),
        ("Endpoint HA", "deploy across AZ with multiple instances", "A", "inference availability"),
        ("Health check", "InvokeEndpoint or container /ping", "A", "load balancer / SageMaker health"),
        ("Model compilation Neo", "optimize for Inf1/GPU edge", "A", "hardware-specific optimization"),
        ("Inf2 instances", "cost-efficient inference chips", "A", "instance family awareness"),
        ("G5 instances", "GPU inference for deep learning", "A", "instance family selection"),
        ("C6i", "CPU inference for classical ML", "A", "right-size compute family"),
        ("Memory-optimized", "large embedding models", "A", "instance family for memory-bound"),
        ("Network bandwidth", "large payload async/batch needs", "A", "infrastructure sizing factor"),
        ("ENI limits", "VPC endpoint scaling constraint", "A", "VPC planning awareness"),
        ("Subnet IP exhaustion", "plan CIDR for scaled endpoints", "A", "VPC capacity planning"),
        ("NAT cost", "minimize via VPC endpoints", "A", "cost-aware networking"),
        ("Shared VPC", "centralized networking for SageMaker", "A", "enterprise network pattern"),
        ("Hub account deployment", "central ML platform account", "A", "multi-account ML pattern"),
    ]
    out = []
    for i, (svc, action, ans, why) in enumerate(matrix):
        stem = f"An ML platform team needs to {action}. Which AWS capability is MOST appropriate?"
        opts = {
            "A": f"Use {svc}",
            "B": "Use AWS DeepRacer exclusively",
            "C": "Disable IAM and encryption",
            "D": "Store artifacts only on local laptops",
        }
        out.append(q(stem, opts, ans, f"{svc}: {why}."))
    return out


def collect_unique() -> list:
    d1, d2, d3, d4 = all_questions()
    combined = CORE + d1 + d2 + d3 + d4 + _matrix_questions()
    seen = set()
    unique = []
    for item in combined:
        key = item["stem"][:120]
        if key in seen:
            continue
        seen.add(key)
        unique.append(item)
    return unique


def render_markdown(questions: list) -> str:
    lines = [
        "# AWS Certified Machine Learning Engineer – Associate (MLA-C01)",
        f"## Practice Question Bank ({len(questions)} unique questions)",
        "",
        "> **Exam name clarification:** AWS markets this as **Machine Learning Engineer – Associate (MLA-C01)**, "
        "not a separate “MLOps Associate” badge. It is the associate-level cert for **building, deploying, orchestrating, "
        "monitoring, and securing** ML workloads—the practical MLOps role on SageMaker and related services.",
        "",
        "| Attribute | Value |",
        "|-----------|-------|",
        "| Scored questions on exam | 50 |",
        "| Total questions (incl. unscored) | 65 |",
        "| Time | 130 minutes |",
        "| Passing score | 720 / 1000 (scaled) |",
        "",
        "| Domain | Weight |",
        "|--------|--------|",
        "| 1 — Data Preparation | 28% |",
        "| 2 — ML Model Development | 26% |",
        "| 3 — Deployment & Orchestration | 22% |",
        "| 4 — Monitoring, Maintenance & Security | 24% |",
        "",
        "[Official exam guide (PDF)](https://d1.awsstatic.com/training-and-certification/docs-machine-learning-engineer-associate/AWS-Certified-Machine-Learning-Engineer-Associate_Exam-Guide.pdf)",
        "",
        "---",
        "",
    ]

    domain_bounds = [
        (1, int(len(questions) * 0.28) + 1, "Domain 1: Data Preparation for ML"),
        (int(len(questions) * 0.28) + 1, int(len(questions) * 0.54) + 1, "Domain 2: ML Model Development"),
        (int(len(questions) * 0.54) + 1, int(len(questions) * 0.76) + 1, "Domain 3: Deployment and Orchestration"),
        (int(len(questions) * 0.76) + 1, len(questions) + 1, "Domain 4: Monitoring, Maintenance, and Security"),
    ]

    domain_idx = 0
    for num, item in enumerate(questions, start=1):
        while domain_idx < len(domain_bounds) - 1 and num >= domain_bounds[domain_idx + 1][0]:
            domain_idx += 1
        start, _, title = domain_bounds[domain_idx]
        if num == start:
            lines.extend(["", f"## {title}", ""])

        lines.append(f"### Question {num}")
        lines.append("")
        lines.append(item["stem"])
        lines.append("")
        for key in sorted(item["options"]):
            lines.append(f"- **{key})** {item['options'][key]}")
        lines.append("")
        ans = item["answer"]
        if isinstance(ans, list):
            lines.append(f"**Correct answer(s):** {', '.join(ans)}")
        else:
            lines.append(f"**Correct answer:** {ans}")
        lines.append("")
        lines.append("**Why this is correct (detailed):**")
        lines.append("")
        lines.append(item["why"])
        lines.append("")
        correct = ans if isinstance(ans, list) else [ans]
        lines.append("**Why the distractors are incorrect:**")
        for key in sorted(item["options"]):
            if key in correct:
                continue
            distractor = item["options"][key]
            if "DeepRacer" in distractor or "laptop" in distractor.lower() or "Disable IAM" in distractor:
                reason = "Out of exam scope or violates security and governance requirements."
            elif "only" in distractor.lower() and key == "B":
                reason = "Too narrow or contradicts the scenario's scale, latency, or compliance needs."
            else:
                reason = "Does not best satisfy the scenario's primary requirement compared to the correct option."
            lines.append(f"- **{key})** {distractor} — {reason}")
        lines.append("")
        lines.append("---")

    lines.extend(
        [
            "",
            "## How to use this bank",
            "",
            "1. Study by domain weights (28 / 26 / 22 / 24).",
            "2. For each wrong answer, write *why* the scenario rejects it—exam distractors are plausible.",
            "3. Lab: SageMaker Pipelines, Model Registry, three endpoint types, Model Monitor, CodePipeline integration.",
            "4. Cross-read: [ML Foundations blog](../blogs/aws-machine-learning-foundations.html), "
            "[Generative AI Foundations](../blogs/aws-generative-ai-foundations.html), "
            "[Data Engineering](../blogs/aws-data-engineering.html).",
            "",
            "*Unofficial practice material. Verify against the latest MLA-C01 exam guide.*",
        ]
    )
    return "\n".join(lines)


def _domain_bounds(n: int) -> list[tuple[int, int, str, str]]:
    return [
        (1, int(n * 0.28) + 1, "Domain 1: Data Preparation for ML", "domain-1"),
        (int(n * 0.28) + 1, int(n * 0.54) + 1, "Domain 2: ML Model Development", "domain-2"),
        (int(n * 0.54) + 1, int(n * 0.76) + 1, "Domain 3: Deployment and Orchestration", "domain-3"),
        (int(n * 0.76) + 1, n + 1, "Domain 4: Monitoring, Maintenance, and Security", "domain-4"),
    ]


def _distractor_reason(distractor: str, key: str) -> str:
    if "DeepRacer" in distractor or "laptop" in distractor.lower() or "Disable IAM" in distractor:
        return "Out of exam scope or violates security and governance requirements."
    if "only" in distractor.lower() and key == "B":
        return "Too narrow or contradicts the scenario's scale, latency, or compliance needs."
    return "Does not best satisfy the scenario's primary requirement compared to the correct option."


def _render_question_html(num: int, item: dict) -> str:
    esc = html.escape
    ans = item["answer"]
    correct = ans if isinstance(ans, list) else [ans]
    ans_label = ", ".join(correct) if len(correct) > 1 else correct[0]

    options = "".join(
        f'<li><strong>{esc(key)})</strong> {esc(item["options"][key])}</li>\n'
        for key in sorted(item["options"])
    )
    distractors = "".join(
        f'<li><strong>{esc(key)})</strong> {esc(item["options"][key])} — '
        f'{esc(_distractor_reason(item["options"][key], key))}</li>\n'
        for key in sorted(item["options"])
        if key not in correct
    )

    return f"""<details class="ml-q border rounded mb-2" id="q{num}">
  <summary class="px-3 py-2"><strong>Question {num}.</strong> {esc(item["stem"])}</summary>
  <div class="px-3 pb-3">
    <ul class="mb-3">{options}</ul>
    <p class="mb-2"><strong>Correct answer:</strong> {esc(ans_label)}</p>
    <p class="mb-2"><strong>Why this is correct:</strong> {esc(item["why"])}</p>
    <p class="mb-1"><strong>Why the distractors are incorrect:</strong></p>
    <ul class="small text-muted mb-0">{distractors}</ul>
  </div>
</details>
"""


def render_blog_html(questions: list) -> str:
    esc = html.escape
    n = len(questions)
    bounds = _domain_bounds(n)
    display_date = "18 Jun 2026"

    domain_nav = "".join(
        f'<li><a href="#{anchor}">{esc(title)}</a> (Q{bounds[i][0]}–{bounds[i][1] - 1})</li>\n'
        for i, (start, end, title, anchor) in enumerate(bounds)
    )

    body_parts: list[str] = []
    domain_idx = 0
    for num, item in enumerate(questions, start=1):
        while domain_idx < len(bounds) - 1 and num >= bounds[domain_idx + 1][0]:
            domain_idx += 1
        start, _, title, anchor = bounds[domain_idx]
        if num == start:
            body_parts.append(f'<h2 class="h4 mt-5" id="{anchor}">{esc(title)}</h2>\n')
        body_parts.append(_render_question_html(num, item))

    questions_block = "".join(body_parts)

    return f"""<article class="inner-page blog-article pb-5">
      <div class="container">
        <div class="row justify-content-center">
          <div class="col-lg-9 col-xl-8">
            <header class="mb-4 pb-3 border-bottom" data-aos="fade-up">
              <div class="blog-article-meta mb-3">
                <p class="text-muted small mb-2">AI/ML · <time datetime="{PUBLISHED}">{display_date}</time> · <span class="blog-meta-label">Practice</span> · By <a href="../index.html#about" class="blog-author text-reset fw-semibold" rel="author">Babulal Tamang</a></p>
              <ul class="blog-tags list-unstyled d-flex flex-wrap gap-1 mb-0" aria-label="Tags">
                <li><span class="badge rounded-pill text-bg-light border text-muted">AWS</span></li>
                <li><span class="badge rounded-pill text-bg-light border text-muted">MLA-C01</span></li>
                <li><span class="badge rounded-pill text-bg-light border text-muted">SageMaker</span></li>
                <li><span class="badge rounded-pill text-bg-light border text-muted">MLOps</span></li>
              </ul>
              </div>
              <h1 class="h2 mb-3">AWS MLA-C01 Practice Question Bank</h1>
              <p class="lead mb-3">{n} unique multiple-choice questions for the <strong>AWS Certified Machine Learning Engineer – Associate (MLA-C01)</strong> exam—with detailed explanations for every answer and distractor.</p>
              <div class="border-start border-primary border-4 ps-3 py-3 bg-light rounded mb-0" role="note">
                <p class="small text-uppercase text-muted mb-1 fw-semibold">In short</p>
                <p class="mb-0">Unofficial practice aligned to domain weights (28 / 26 / 22 / 24). Expand each question to reveal the answer and rationale. Verify against the latest <a href="https://d1.awsstatic.com/training-and-certification/docs-machine-learning-engineer-associate/AWS-Certified-Machine-Learning-Engineer-Associate_Exam-Guide.pdf" target="_blank" rel="noopener noreferrer">official exam guide</a>.</p>
              </div>
            </header>

            <div class="blog-prose ml-question-bank" data-aos="fade-up" data-aos-delay="50">

              <h2 class="h4 mt-4">Exam at a glance</h2>
              <div class="table-responsive">
                <table class="table table-sm table-bordered">
                  <tbody>
                    <tr><th scope="row">Scored questions</th><td>50</td></tr>
                    <tr><th scope="row">Total (incl. unscored)</th><td>65</td></tr>
                    <tr><th scope="row">Time</th><td>130 minutes</td></tr>
                    <tr><th scope="row">Passing score</th><td>720 / 1000 (scaled)</td></tr>
                  </tbody>
                </table>
              </div>
              <div class="table-responsive mb-4">
                <table class="table table-sm table-bordered">
                  <thead><tr><th scope="col">Domain</th><th scope="col">Weight</th></tr></thead>
                  <tbody>
                    <tr><td>1 — Data Preparation</td><td>28%</td></tr>
                    <tr><td>2 — ML Model Development</td><td>26%</td></tr>
                    <tr><td>3 — Deployment &amp; Orchestration</td><td>22%</td></tr>
                    <tr><td>4 — Monitoring, Maintenance &amp; Security</td><td>24%</td></tr>
                  </tbody>
                </table>
              </div>

              <p class="alert alert-secondary small" role="note">AWS markets this as <strong>Machine Learning Engineer – Associate (MLA-C01)</strong>, not a separate “MLOps Associate” badge. It covers building, deploying, orchestrating, monitoring, and securing ML workloads on SageMaker and related services.</p>

              <h2 class="h4 mt-5">Jump to a domain</h2>
              <ul class="mb-4">
                {domain_nav}
              </ul>

              <h2 class="h4 mt-4">Questions</h2>
              <p class="small text-muted">Click a question to expand the answer and explanations.</p>

              {questions_block}

              <h2 class="h4 mt-5">How to use this bank</h2>
              <ol>
                <li>Study by domain weights (28 / 26 / 22 / 24).</li>
                <li>For each wrong answer, write <em>why</em> the scenario rejects it—exam distractors are plausible.</li>
                <li>Lab: SageMaker Pipelines, Model Registry, endpoint types, Model Monitor, CodePipeline integration.</li>
              </ol>

              <h2 class="h4 mt-5">Related posts</h2>
              <p><a href="aws-machine-learning-foundations.html">Machine Learning Foundations</a> · <a href="aws-generative-ai-foundations.html">Generative AI Foundations</a> · <a href="aws-data-engineering.html">Data Engineering</a> · <a href="ai-ml-terminology-glossary.html">AI and ML terminology</a></p>

              <p class="small text-muted mt-4 mb-2"><a href="../index.html#blog">Blog index</a></p>
              <p class="mb-0"><a href="../index.html#blog" class="btn btn-outline-primary btn-sm"><i class="bi bi-arrow-left" aria-hidden="true"></i> Back to blog list</a></p>
            </div>
          </div>
        </div>
      </div>
    </article>
"""


def main() -> None:
    questions = collect_unique()
    if len(questions) < 200:
        raise SystemExit(f"Expected 200+ unique questions, got {len(questions)}")
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    content = render_markdown(questions)
    OUTPUT.write_text(content, encoding="utf-8")
    print(f"Wrote {len(questions)} unique questions to {OUTPUT}")
    print(f"Size: {OUTPUT.stat().st_size / 1024:.1f} KB")

    BLOG_CONTENT.parent.mkdir(parents=True, exist_ok=True)
    blog_html = render_blog_html(questions)
    BLOG_CONTENT.write_text(blog_html, encoding="utf-8")
    print(f"Wrote blog content to {BLOG_CONTENT}")
    print(f"Blog size: {BLOG_CONTENT.stat().st_size / 1024:.1f} KB")


if __name__ == "__main__":
    main()
