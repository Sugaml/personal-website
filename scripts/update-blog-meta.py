#!/usr/bin/env python3
"""Add author, keywords meta, and visible tags/labels to blog articles."""

import re
from pathlib import Path

BLOGS_DIR = Path(__file__).resolve().parent.parent / "blogs"
AUTHOR = "Babulal Tamang"

# label: index-style type badge; tags: visible topic tags; keywords: meta keywords
POSTS = {
    "aws-cloud-practitioner.html": {
        "label": "Exam",
        "tags": ["AWS", "Cloud Practitioner", "Certification", "Credly"],
        "keywords": "AWS, Cloud Practitioner, certification, Credly, cloud basics, Babulal Tamang",
    },
    "aws-cloud-architecting.html": {
        "label": "Academy",
        "tags": ["AWS", "Cloud Architecting", "Well-Architected", "Credly"],
        "keywords": "AWS Academy, cloud architecting, availability, security, Credly, Babulal Tamang",
    },
    "aws-cloud-security-foundations.html": {
        "label": "Academy",
        "tags": ["AWS", "Cloud Security", "IAM", "Credly"],
        "keywords": "AWS Academy, cloud security, IAM, shared responsibility, Credly, Babulal Tamang",
    },
    "aws-data-engineering.html": {
        "label": "Academy",
        "tags": ["AWS", "Data Engineering", "Pipelines", "Credly"],
        "keywords": "AWS Academy, data engineering, ETL, data quality, Credly, Babulal Tamang",
    },
    "aws-machine-learning-foundations.html": {
        "label": "Academy",
        "tags": ["AWS", "Machine Learning", "ML", "Credly"],
        "keywords": "AWS Academy, machine learning, SageMaker, ML foundations, Credly, Babulal Tamang",
    },
    "aws-generative-ai-foundations.html": {
        "label": "Academy",
        "tags": ["AWS", "Generative AI", "Gen AI", "Credly"],
        "keywords": "AWS Academy, generative AI, foundation models, responsible AI, Credly, Babulal Tamang",
    },
    "aws-partner-enablement.html": {
        "label": "Partner",
        "tags": ["AWS", "Partner", "Sales", "Credly"],
        "keywords": "AWS Partner, sales accreditation, technical accredited, Credly, Babulal Tamang",
    },
    "aws-network-architecture-design.html": {
        "label": "Guide",
        "tags": ["AWS", "VPC", "Networking", "Architecture"],
        "keywords": "AWS, VPC, network architecture, hub-spoke, cloud architect, Babulal Tamang",
    },
    "aws-iam-policy-json-anatomy.html": {
        "label": "Guide",
        "tags": ["AWS", "IAM", "Security", "JSON"],
        "keywords": "AWS IAM, policy JSON, least privilege, ABAC, security, Babulal Tamang",
    },
    "how-to-become-ai-developer.html": {
        "label": "Guide",
        "tags": ["AI", "ML", "Career", "Software"],
        "keywords": "AI developer, machine learning, tech stack, learning path, Babulal Tamang",
    },
    "ai-historical-paradigms.html": {
        "label": "Essay",
        "tags": ["AI", "History", "Deep Learning", "Transformers"],
        "keywords": "AI history, symbolic AI, neural networks, transformers, Babulal Tamang",
    },
    "docker-containerization-hidden-side.html": {
        "label": "Essay",
        "tags": ["Docker", "Containers", "DevOps", "Linux"],
        "keywords": "Docker, containers, cgroups, namespaces, container security, Babulal Tamang",
    },
    "kubernetes-when-how-why-where.html": {
        "label": "Essay",
        "tags": ["Kubernetes", "Business", "Platform"],
        "keywords": "Kubernetes, business value, when to use K8s, platform, Babulal Tamang",
    },
    "kubernetes-architecture-simple.html": {
        "label": "Essay",
        "tags": ["Kubernetes", "Architecture", "Control Plane"],
        "keywords": "Kubernetes architecture, control plane, pods, deployments, Babulal Tamang",
    },
    "kubernetes-cluster-rbac.html": {
        "label": "Guide",
        "tags": ["Kubernetes", "RBAC", "Security", "IAM"],
        "keywords": "Kubernetes RBAC, Role, ClusterRole, least privilege, authorization, Babulal Tamang",
    },
    "kubernetes-hands-on-1-local-lab.html": {
        "label": "Course",
        "tags": ["Kubernetes", "kind", "minikube", "Hands-on"],
        "keywords": "Kubernetes hands-on, kind, k3s, minikube, local lab, Babulal Tamang",
    },
    "kubernetes-hands-on-2-yaml-anatomy.html": {
        "label": "Course",
        "tags": ["Kubernetes", "YAML", "Manifests", "Hands-on"],
        "keywords": "Kubernetes YAML, manifests, apiVersion, kubectl explain, Babulal Tamang",
    },
    "kubernetes-hands-on-3-first-workloads.html": {
        "label": "Course",
        "tags": ["Kubernetes", "Deployments", "Services", "Hands-on"],
        "keywords": "Kubernetes workloads, Pod, Deployment, Service, hands-on, Babulal Tamang",
    },
    "kubernetes-hands-on-4-day-one-practices.html": {
        "label": "Course",
        "tags": ["Kubernetes", "Best Practices", "Production", "Hands-on"],
        "keywords": "Kubernetes best practices, probes, resources, day-one, Babulal Tamang",
    },
    "kubernetes-hands-on-5-debug-next-steps.html": {
        "label": "Course",
        "tags": ["Kubernetes", "Debugging", "kubectl", "Hands-on"],
        "keywords": "Kubernetes debugging, kubectl, troubleshooting, hands-on, Babulal Tamang",
    },
    "devops-historical-foundations.html": {
        "label": "Essay",
        "tags": ["DevOps", "History", "CI/CD", "Platform Engineering"],
        "keywords": "DevOps history, CI/CD, SRE, platform engineering, Babulal Tamang",
    },
    "gitops-principles.html": {
        "label": "Essay",
        "tags": ["GitOps", "Kubernetes", "Flux", "Argo CD"],
        "keywords": "GitOps, declarative, reconciliation, Argo CD, Flux, Babulal Tamang",
    },
    "devops-life-business-value.html": {
        "label": "Essay",
        "tags": ["DevOps", "Business Value", "Platform", "Reliability"],
        "keywords": "DevOps business value, DORA, platform engineering, Babulal Tamang",
    },
    "devops-professional-nature.html": {
        "label": "Essay",
        "tags": ["DevOps", "Professionalism", "Culture", "Platform"],
        "keywords": "DevOps professional, mindset, ownership, blameless, Babulal Tamang",
    },
    "devops-psychology-after-hours.html": {
        "label": "Essay",
        "tags": ["DevOps", "Psychology", "On-call", "Wellbeing"],
        "keywords": "DevOps psychology, on-call stress, burnout, operations, Babulal Tamang",
    },
    "cloud-platform-evolution.html": {
        "label": "Essay",
        "tags": ["Cloud", "Platform Engineering", "Migration", "FinOps"],
        "keywords": "cloud platform, landing zone, migration, platform engineering, Babulal Tamang",
    },
    "finops-greenops-1-invisible-bill.html": {
        "label": "Series",
        "tags": ["Sustainability", "FinOps", "GreenOps", "Series 1/5"],
        "keywords": "sustainability, digital footprint, FinOps, GreenOps, series, Babulal Tamang",
    },
    "finops-greenops-2-conservation-matters.html": {
        "label": "Series",
        "tags": ["Sustainability", "Conservation", "GreenOps", "Series 2/5"],
        "keywords": "conservation, sustainability, responsible technology, series, Babulal Tamang",
    },
    "finops-greenops-3-finops-plain-english.html": {
        "label": "FinOps",
        "tags": ["FinOps", "Cloud Cost", "Optimization", "Series 3/5"],
        "keywords": "FinOps, cloud cost, Inform Optimize Operate, series, Babulal Tamang",
    },
    "finops-greenops-4-greenops-plain-english.html": {
        "label": "GreenOps",
        "tags": ["GreenOps", "Sustainability", "Carbon", "Series 4/5"],
        "keywords": "GreenOps, sustainable IT, carbon, efficiency, series, Babulal Tamang",
    },
    "finops-greenops-5-smarter-lighter.html": {
        "label": "Series",
        "tags": ["FinOps", "GreenOps", "Cloud Architect", "Series 5/5"],
        "keywords": "FinOps, GreenOps, landing zone, Well-Architected, cloud architect, Babulal Tamang",
    },
    "iso-27001-lead-auditor-information-security.html": {
        "label": "Lead Auditor",
        "tags": ["ISO 27001", "ISMS", "Security", "Credly"],
        "keywords": "ISO 27001, lead auditor, ISMS, information security, Credly, Babulal Tamang",
    },
    "iso-42001-lead-auditor-ai-management.html": {
        "label": "Lead Auditor",
        "tags": ["ISO 42001", "AIMS", "AI Governance", "Credly"],
        "keywords": "ISO 42001, AI management, lead auditor, AIMS, Credly, Babulal Tamang",
    },
    "opswat-icip-critical-infrastructure.html": {
        "label": "OPSWAT",
        "tags": ["Critical Infrastructure", "CIP", "OPSWAT", "Credly"],
        "keywords": "OPSWAT, ICIP, critical infrastructure, CIP, Credly, Babulal Tamang",
    },
    "credly-digital-badges.html": {
        "label": "Hub",
        "tags": ["Credly", "Certifications", "AWS", "ISO"],
        "keywords": "Credly, digital badges, AWS, ISO, certifications, Babulal Tamang",
    },
}


def tags_html(tags):
    items = "\n".join(
        f'                <li><span class="badge rounded-pill text-bg-light border text-muted">{t}</span></li>'
        for t in tags
    )
    return f"""              <ul class="blog-tags list-unstyled d-flex flex-wrap gap-1 mb-0" aria-label="Tags">
{items}
              </ul>"""


def build_meta_block(inner: str, label: str, tags: list[str]) -> str:
    label_bit = f' · <span class="blog-meta-label">{label}</span>'
    if label.lower() in inner.lower() or f"· {label}" in inner:
        label_bit = ""
    return f"""              <motion class="blog-article-meta mb-3">
                <p class="text-muted small mb-2">{inner}{label_bit} · By <a href="../index.html#about" class="blog-author text-reset fw-semibold" rel="author">{AUTHOR}</a></p>
{tags_html(tags)}
              </div>""".replace("<motion", "<motion").replace(
        "<motion class", "<div class"
    ).replace("</motion>", "</motion>").replace(
        'class="blog-article-meta', 'class="blog-article-meta'
    )


def fix_meta_block(s: str) -> str:
    return s.replace("<motion class", "<motion class").replace(
        "<motion class=\"blog-article-meta", '<motion class="blog-article-meta'
    )


def build_meta_block_clean(inner: str, label: str, tags: list[str]) -> str:
    label_bit = ""
    if label and label.lower() not in inner.lower():
        label_bit = f' · <span class="blog-meta-label">{label}</span>'
    return (
        '              <div class="blog-article-meta mb-3">\n'
        f'                <p class="text-muted small mb-2">{inner}{label_bit} · By <a href="../index.html#about" class="blog-author text-reset fw-semibold" rel="author">{AUTHOR}</a></p>\n'
        f"{tags_html(tags)}\n"
        "              </div>"
    )


def add_head_metas(content: str, keywords: str) -> str:
    if 'name="author"' not in content:
        content = re.sub(
            r'(<meta content="[^"]*" name="description">)\s*\n',
            rf'\1\n  <meta name="author" content="{AUTHOR}">\n',
            content,
            count=1,
        )
    if 'name="keywords"' not in content:
        content = re.sub(
            r'(<meta name="author" content="[^"]*">)\s*\n',
            rf'\1\n  <meta name="keywords" content="{keywords}">\n',
            content,
            count=1,
        )
    else:
        content = re.sub(
            r'<meta name="keywords" content="[^"]*">',
            f'<meta name="keywords" content="{keywords}">',
            content,
            count=1,
        )
    return content


def update_article_header(content: str, label: str, tags: list[str]) -> str:
    if "blog-article-meta" in content:
        return content
    pattern = re.compile(
        r'(<header class="mb-4 pb-3 border-bottom"[^>]*>\s*)'
        r'<p class="text-muted small mb-2">(.*?)</p>',
        re.DOTALL,
    )
    m = pattern.search(content)
    if not m:
        print("  WARN: no article header meta line found")
        return content
    inner = m.group(2).strip()
    replacement = m.group(1) + build_meta_block_clean(inner, label, tags)
    return content[: m.start()] + replacement + content[m.end() :]


def main():
    updated = 0
    for name, meta in POSTS.items():
        path = BLOGS_DIR / name
        if not path.exists():
            print(f"SKIP missing: {name}")
            continue
        text = path.read_text(encoding="utf-8")
        orig = text
        text = add_head_metas(text, meta["keywords"])
        text = update_article_header(text, meta["label"], meta["tags"])
        if text != orig:
            path.write_text(text, encoding="utf-8")
            updated += 1
            print(f"OK {name}")
        else:
            print(f"UNCHANGED {name}")
    print(f"\nUpdated {updated} files.")


if __name__ == "__main__":
    main()
