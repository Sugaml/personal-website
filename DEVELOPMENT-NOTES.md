# Development notes — personal website

Short log of design decisions and content changes.

## 2026-05-20 — Site structure refactor (templates + build)

- **Goal:** DRY blog chrome (header, nav, footer, assets) while keeping GitHub Pages URLs unchanged (`blogs/*.html`).
- **Layout:** `templates/blog/layout.html`; article bodies in `content/blogs/`; metadata in `data/blog-posts.json`.
- **Build:** `make build` (`scripts/build_site.py`) regenerates `blogs/`. `make extract` re-splits built pages into content + data.
- **Generators / maintenance:** `gen-*.py` and `update-blog-meta.py` target `content/` + registry, then run the build.
- **Docs:** `README.md`. Unused `inner-page.html` → `templates/legacy/`.

## 2026-05-20 — Terraform & IaC for everyone (guide)

- **Title:** “Anyone Can Terraform: Why IaC Exists, How It Works, and the Anatomy of `.tf` and State” (article); index card “Terraform & IaC for everyone”.
- **Intent:** Beginner-friendly IaC guide—why teams adopt it, Terraform init/plan/apply loop, vocabulary, project layout, HCL blocks (terraform, provider, resource, variable, output, data, locals, modules), state file top-level and resource entry anatomy, remote state/locking, plan symbols, ten-minute first apply, pitfalls, learning path. Cross-links to GitOps, network architecture, IAM anatomy, DevOps history.
- **Files:** `blogs/terraform-iac-for-everyone.html`, `index.html` (Platform section before GitOps card), cross-link from `gitops-principles.html`.

## 2026-05-20 — SQL course (relational databases)

- **Title:** “SQL Course Notes: From First SELECT to Production-Ready Queries” (article); index card “SQL course (relational databases)”.
- **Intent:** Detailed course-style guide—relational model, DDL/DML/DCL/TCL, SELECT/joins/aggregations, CTEs and window functions, constraints and normalization, indexes and EXPLAIN, transactions (ACID), dialect comparison (PostgreSQL vs MySQL), SQL in data engineering/ML, lab progression, pitfalls. New **Data & databases** blog subsection on index.
- **Files:** `blogs/sql-course-relational-databases.html`, `index.html`, cross-links from `aws-data-engineering.html` and `how-to-become-ai-developer.html`.

## 2026-05-20 — Redis and redis-cli (guide)

- **Title:** “Redis and redis-cli: The In-Memory Store Behind Fast APIs” (article); index card “Redis and redis-cli”.
- **Intent:** Platform guide on what Redis is, data structures, architecture patterns (cache-aside, sessions, pub/sub, locks, rate limits), single-threaded model, memory/TTL/eviction, RDB/AOF, HA (replicas, Sentinel, Cluster), security, install/connect, and hands-on redis-cli sections (strings, hashes, lists, sets, ZSETs, streams, pub/sub, SCAN/INFO). Cross-links to Docker, Kubernetes architecture, GitOps, FinOps Part 1.
- **Files:** `blogs/redis-and-cli-deep-dive.html`, `index.html` (Platform section after Docker card).

## 2026-05-20 — Incidents & disaster response (guide)

- **Title:** “When Production Breaks: Incidents, Disasters, and How to Respond Calmly” (article); index card “Incidents & disaster response”.
- **Intent:** Deep guide on incident vs disaster, severity model, lifecycle (detect → learn), IC/scribe/comms roles, calm-response habits, DR/BCP (RTO/RPO, failover, security disasters, game days), pre-pager design, ten-minute bridge script, comms templates, pitfalls. Pairs with `devops-psychology-after-hours.html` (mind under pressure) with operational procedure.
- **Files:** `blogs/incident-disaster-response-calm.html`, `index.html` (Platform section after DevOps psychology card), cross-link from psychology post.

## 2026-05-20 — Kubernetes storage PV / PVC / StorageClass (guide)

- **Title:** “Kubernetes Storage: PV, PVC, and StorageClass Explained in Depth” (article); index card “Kubernetes storage (PV, PVC, StorageClass)”.
- **Intent:** Object-model deep-dive—binding lifecycle, static vs dynamic provisioning, PVC/PV/StorageClass YAML, access modes, reclaim policies, volume modes, CSI overview, Pod mounts, StatefulSet `volumeClaimTemplates`, snapshots pointer, troubleshooting table, production practices. Complements `kubernetes-cri-csi-deep-dive.html` (CRI/CSI interfaces) with day-to-day manifest focus.
- **Files:** `blogs/kubernetes-storage-pv-pvc-storageclass.html`, `index.html` (Platform section after CRI/CSI card), cross-link from `kubernetes-architecture-simple.html`.

## 2026-05-20 — Kubernetes CRI and CSI (guide)

- **Title:** “CRI and CSI: How Kubernetes Plugs In Runtimes and Storage” (article); index card “Kubernetes CRI and CSI”.
- **Intent:** Disambiguate CRI vs CSI (and CNI); deep-dive on kubelet↔runtime (sandbox, images, crictl), CSI lifecycle (provisioner, attacher, node plugin, StorageClass), in-tree migration, debugging playbook, production pitfalls. Cross-links to architecture, Docker hidden side, RBAC, hands-on lab.
- **Files:** `blogs/kubernetes-cri-csi-deep-dive.html`, `index.html` (Platform section after architecture), cross-link from `kubernetes-architecture-simple.html` (CRI mention).

## 2026-05-20 — Kubernetes cluster RBAC (guide)

- **Title:** “Kubernetes Cluster RBAC: The Mental Model That Actually Sticks” (article); index card uses shorter “Kubernetes cluster RBAC”.
- **Intent:** Plain-language RBAC guide—authn vs authz, four objects (Role, ClusterRole, RoleBinding, ClusterRoleBinding), rule anatomy, subjects, evaluation, built-in roles, worked patterns, `kubectl auth can-i`, least privilege, RBAC vs NetworkPolicy/Pod Security/cloud IAM, pitfalls, learning path. Cross-links to architecture, hands-on series, GitOps, AWS IAM anatomy.
- **Files:** `blogs/kubernetes-cluster-rbac.html`, `index.html` (Platform section after architecture), cross-link from `kubernetes-architecture-simple.html`.

## 2026-05-20 — IAM policy JSON anatomy (guide)

- **Title:** “IAM Policy JSON Anatomy: Read Every Field Before You Click Allow” (article); index card uses shorter “IAM policy JSON anatomy”.
- **Intent:** Deep-dive companion to Cloud Security Foundations: policy types (identity, resource, boundary, SCP, session), document skeleton (`Version`, `Statement`), every statement field (`Sid`, `Effect`, `Principal`, `Action`/`NotAction`, `Resource`/`NotResource`, `Condition`), evaluation order, trust policies, least-privilege patterns, CI/EKS example, common mistakes, validation tools.
- **Files:** `blogs/aws-iam-policy-json-anatomy.html`, `index.html` (AWS section after network architecture), cross-link from `aws-cloud-security-foundations.html`.

## 2026-05-20 — AWS network architecture design (guide)

- **Title:** “Designing AWS Network Architecture: What a Cloud Architect Actually Decides” (article); index card uses shorter “AWS network architecture”.
- **Intent:** Architect-focused guide on requirements-first VPC design, layered subnets, IPAM/CIDR planning, connectivity patterns (endpoints, NAT, TGW, hybrid), security on the wire, multi-account landing zones, DR, operability, cost levers, pitfalls, and ARB checklist. Cross-links to Cloud Architecting, Cloud Security Foundations, cloud platform evolution, GitOps, and FinOps/GreenOps Part 5.
- **Files:** `blogs/aws-network-architecture-design.html`, `index.html` (AWS section after Cloud Architecting), cross-link from `aws-cloud-architecting.html`.

## 2026-05-19 — Kubernetes hands-on course (5 parts)

- **Series:** Beginner path with practice on local clusters (kind, k3s, minikube): lab setup → YAML anatomy → Pod/Deployment/Service → day-one best practices → debugging and next steps.
- **Intent:** Pair with `kubernetes-architecture-simple.html` and `kubernetes-when-how-why-where.html`; teach manifest structure, selectors, `kubectl explain`, dry-run, namespaces, recommended labels, resource requests/limits, and basic security context before advanced topics.
- **Files:** `blogs/kubernetes-hands-on-{1..5}-*.html`, `scripts/gen-kubernetes-hands-on-blogs.py`, `index.html` (Platform card), cross-link from architecture post.

## 2026-05-19 — FinOps & GreenOps Part 5 (cloud architect rewrite)

- **Change:** Part 5 reframed for solution/cloud architects—Well-Architected cost + sustainability, tagging/landing zones, ARB questions, pattern table, trade-off ADRs, 90-day playbook. Plain-language series parts 1–4 unchanged.
- **Files:** `scripts/gen-finops-greenops-blogs.py`, `blogs/finops-greenops-5-smarter-lighter.html`, `index.html` (card blurb).

## 2026-05-19 — FinOps & GreenOps series (5 posts)

- **Series:** Plain-language sustainability path for a general audience—digital footprint, conservation/sustainability, FinOps, GreenOps, and a closing essay on aligning both disciplines.
- **Titles (articles):**
  1. “The Invisible Bill: How Phones, Apps, and Cloud Touch the Real World”
  2. “Living Within Our Means: Why Conservation and Sustainability Matter to Everyone”
  3. “FinOps in Plain English: Stop Guessing What the Cloud Costs”
  4. “GreenOps in Plain English: Running Technology With a Lighter Footprint”
  5. “Designing for Both Ledgers: When FinOps and GreenOps Belong in Architecture” (cloud architect perspective)
- **Index layout:** Separate blog subsections—**Sustainability & responsible technology** (parts 1, 2, 5), **FinOps** (part 3), **GreenOps** (part 4). Each post includes series navigation.
- **Files:** `blogs/finops-greenops-{1..5}-*.html`, `index.html`, `scripts/gen-finops-greenops-blogs.py` (regenerates posts 3–5 from gitops shell).

## 2026-05-19 — How to become an AI developer (guide)

- **Title:** “How to Become an AI Developer: Terminology, Architecture, Tech Stack, and Why It Matters” (article); index card uses shorter “How to become an AI developer”.
- **Intent:** Hands-on companion to the historical paradigms essay: roles, glossary, layered architecture, foundations order, stack (languages, frameworks, models, cloud/MLOps), phased learning path, pitfalls, and future outlook. Cross-links to AWS ML/Gen AI posts, ISO 42001, cloud platform evolution, and `ai-historical-paradigms.html`.
- **Files:** `blogs/how-to-become-ai-developer.html`, `index.html` (AI/ML section), cross-link from `ai-historical-paradigms.html`.

## 2026-05-19 — AI historical paradigms blog post

- **Title:** “From Symbols to Foundation Models: The Historical Paradigms of Artificial Intelligence” (article); index card uses shorter “Historical paradigms of AI” for scanning.
- **Intent:** Narrative spine for the new **AI/ML** blog section: six paradigms (symbolic, expert systems, connectionism, statistical ML, deep learning, foundation models), AI winters, pioneer table, where the field stands in 2026, and links to AWS ML/GenAI credential posts and ISO 42001.
- **Audience:** Readers who want context before diving into hands-on ML or governance content; pairs with Platform essays in tone (similar to DevOps history post).
- **Files:** `blogs/ai-historical-paradigms.html`, `index.html` (AI/ML section between Platform & culture and ISO & OPSWAT).

## 2026-05-19 — Kubernetes for business (when / how / why / where) blog post

- **Title:** “Kubernetes for Business Leaders: When, How, Why, and Where It Fits” (article); index card uses shorter “Kubernetes for business” for scanning.
- **Intent:** Executive-friendly companion to the architecture essay: plain-language what/why/when/how/where, adoption phases table, industry and environment examples, cost/risk pitfalls, and questions for steering meetings. Cross-links to architecture, GitOps, DevOps business value, and cloud platform posts.
- **Audience:** Product leaders and business stakeholders who need K8s explained without YAML or component deep dives.
- **Files:** `blogs/kubernetes-when-how-why-where.html`, `index.html` (Platform & culture section), cross-link from `kubernetes-architecture-simple.html`.

## 2026-05-19 — Kubernetes architecture (simple) blog post

- **Title:** “Kubernetes Architecture in Simple Terms” (article); index card uses shorter “Kubernetes architecture (simple)” for scanning.
- **Intent:** Plain-language map of K8s for readers who already see orchestration in job descriptions but not in diagrams: cluster vs node, control plane (API server, etcd, scheduler, controllers, cloud controller) vs workers (kubelet, runtime, kube-proxy), plus Pod / Deployment / Service and common add-ons (CNI, DNS, ingress). Includes a short troubleshooting mental model and links to the GitOps essay.
- **Edge case called out:** StatefulSets, volumes, and operators mentioned only as a pointer so the post stays introductory.
- **Files:** `blogs/kubernetes-architecture-simple.html`, `index.html` (Platform & culture section).

## 2026-05-19 — Cloud platform evolution blog post

- **Title:** “The Cloud Platform: Why It Matters, How We Use It, and What Comes After the Shift” (article); index card uses shorter “Cloud platform evolution” for scanning.
- **Intent:** Foundational essay covering cloud platform definition (IaaS/PaaS/SaaS), business importance, usage patterns and history, practical migration guidance (6 Rs, landing zones, FinOps), and forward-looking themes (AI-native, platform engineering, hybrid/edge, sovereignty). Cross-links to AWS Academy posts and Platform & culture siblings.
- **Files:** `blogs/cloud-platform-evolution.html`, `index.html` (Platform & culture section).

## 2026-05-19 — DevOps life & business value blog post

- **Title:** “Shipping Is the Strategy: DevOps Life and the Business Value It Creates” (article); index card uses shorter “DevOps life & business value” for scanning.
- **Intent:** Bridge the DevOps history and GitOps essays with a practitioner-focused piece that ties daily habits (flow, feedback, on-call, platforms) to outcomes leaders fund: speed, reliability, efficiency, and explainable risk. Includes DORA-style mapping table and links to sibling posts.
- **Files:** `blogs/devops-life-business-value.html`, `index.html` (Platform & culture section).

## 2026-05-19 — GitOps blog post

- **Title:** “Git as the Control Plane: GitOps Principles That Survive Production” (article); index card uses shorter “Git as the control plane (GitOps)” for scanning.
- **Intent:** Pair the existing DevOps history essay with a practical GitOps piece: declarative state, Git as system of record, pull-based reconciliation, drift, security, observability, and common pitfalls—aligned with OpenGitOps-style vocabulary without duplicating vendor docs.
- **Files:** `blogs/gitops-principles.html`, `index.html` (Platform & culture section).
