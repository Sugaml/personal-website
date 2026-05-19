# Development notes — personal website

Short log of design decisions and content changes.

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
