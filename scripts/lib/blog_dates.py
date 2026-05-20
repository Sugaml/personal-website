"""Publication date helpers for blog posts."""

from __future__ import annotations

from datetime import date, datetime, timedelta

# Credential and hub posts keep real-world dates; guides get sequential days.
KNOWN_PUBLISHED: dict[str, str] = {
    "aws-data-engineering": "2025-03-05",
    "aws-partner-enablement": "2025-12-03",
    "aws-cloud-practitioner": "2025-12-16",
    "aws-cloud-security-foundations": "2025-12-20",
    "opswat-icip-critical-infrastructure": "2026-01-10",
    "iso-27001-lead-auditor-information-security": "2026-01-13",
    "aws-cloud-architecting": "2026-02-21",
    "aws-machine-learning-foundations": "2026-04-25",
    "aws-generative-ai-foundations": "2026-04-25",
    "iso-42001-lead-auditor-ai-management": "2026-04-26",
    "credly-digital-badges": "2026-05-12",
}

# Narrative publish order (oldest → newest) for posts without fixed dates.
SEQUENTIAL_ORDER: list[str] = [
    "devops-historical-foundations",
    "gitops-principles",
    "devops-life-business-value",
    "cloud-platform-evolution",
    "docker-containerization-hidden-side",
    "kubernetes-architecture-simple",
    "kubernetes-when-how-why-where",
    "finops-greenops-1-invisible-bill",
    "finops-greenops-2-conservation-matters",
    "finops-greenops-3-finops-plain-english",
    "finops-greenops-4-greenops-plain-english",
    "finops-greenops-5-smarter-lighter",
    "kubernetes-hands-on-1-local-lab",
    "kubernetes-hands-on-2-yaml-anatomy",
    "kubernetes-hands-on-3-first-workloads",
    "kubernetes-hands-on-4-day-one-practices",
    "kubernetes-hands-on-5-debug-next-steps",
    "ai-historical-paradigms",
    "how-to-become-ai-developer",
    "aws-network-architecture-design",
    "aws-iam-policy-json-anatomy",
    "kubernetes-cluster-rbac",
    "kubernetes-cri-csi-deep-dive",
    "kubernetes-storage-pv-pvc-storageclass",
    "incident-disaster-response-calm",
    "devops-psychology-after-hours",
    "devops-professional-nature",
    "redis-and-cli-deep-dive",
    "terraform-iac-for-everyone",
    "git-github-course-in-depth",
    "sql-course-relational-databases",
    "computing-in-depth",
    "linux-in-depth",
    "what-happens-when-you-run-ls",
    "kubernetes-troubleshooting-playbook",
    "aws-ebs-s3-efs-storage-deep-dive",
    "aws-s3-in-depth",
    "aws-emr-hadoop-components-deep-dive",
    "aws-gcp-azure-hyperscaler-comparison",
    "aws-gcp-azure-services-mapping",
    "supervised-unsupervised-reinforcement-learning",
    "neural-networks-in-depth",
    "generative-ai-in-depth",
    "llm-in-depth",
    "rag-retrieval-augmented-generation-deep-dive",
    "ai-foundation-models-deep-dive",
    "ai-ml-terminology-glossary",
    "aws-mla-c01-practice-questions",
]

SEQUENTIAL_START = date(2026, 5, 1)


def format_display(iso: str) -> str:
    """e.g. 2026-05-20 → 20 May 2026"""
    d = date.fromisoformat(iso)
    return f"{d.day} {d.strftime('%b %Y')}"


def time_element(iso: str) -> str:
    return f'<time datetime="{iso}">{format_display(iso)}</time>'


def build_published_map(slugs: list[str]) -> dict[str, str]:
    """Assign one ISO date per slug; known dates win, then sequential fill."""
    published = dict(KNOWN_PUBLISHED)
    used = set(published.values())
    current = SEQUENTIAL_START

    for slug in SEQUENTIAL_ORDER:
        if slug in published:
            continue
        if slug not in slugs:
            continue
        while current.isoformat() in used:
            current += timedelta(days=1)
        published[slug] = current.isoformat()
        used.add(current.isoformat())
        current += timedelta(days=1)

    for slug in slugs:
        if slug not in published:
            while current.isoformat() in used:
                current += timedelta(days=1)
            published[slug] = current.isoformat()
            used.add(current.isoformat())
            current += timedelta(days=1)

    return published


def parse_git_date(iso_datetime: str) -> str:
    return iso_datetime.split(" ", 1)[0]


def max_iso(a: str, b: str) -> str:
    return a if a >= b else b
