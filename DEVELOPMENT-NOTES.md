# Development notes — personal website

Short log of design decisions and content changes.

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
