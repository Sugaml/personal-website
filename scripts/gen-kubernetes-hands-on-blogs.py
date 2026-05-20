#!/usr/bin/env python3
"""Generate Kubernetes hands-on beginner course (5 parts)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from lib.blog_registry import upsert_post  # noqa: E402
from build_site import build_blogs  # noqa: E402

NAV = [
    ("Your local lab (kind, k3s, minikube)", "kubernetes-hands-on-1-local-lab.html"),
    ("Anatomy of a Kubernetes manifest", "kubernetes-hands-on-2-yaml-anatomy.html"),
    ("First workloads: Pod, Deployment, Service", "kubernetes-hands-on-3-first-workloads.html"),
    ("Best practices from day one", "kubernetes-hands-on-4-day-one-practices.html"),
    ("Debug, observe, and what to learn next", "kubernetes-hands-on-5-debug-next-steps.html"),
]


def series_nav(part: int) -> str:
    items = []
    for i, (label, href) in enumerate(NAV, 1):
        if i == part:
            items.append(f"<li><strong>This post:</strong> {label}</li>")
        else:
            items.append(f'<li><a href="{href}">{label}</a></li>')
    return (
        f'<nav class="border rounded p-3 mb-4 bg-light" aria-label="Series navigation">\n'
        f'                <p class="small text-uppercase text-muted mb-2 fw-semibold">'
        f"Kubernetes hands-on · Part {part} of 5</p>\n"
        f'                <ol class="small mb-0 ps-3">\n                  '
        + "\n                  ".join(items)
        + "\n                </ol>\n              </nav>"
    )


def build_article(p: dict) -> str:
    return f"""<article class="inner-page blog-article pb-5">
      <div class="container">
        <div class="row justify-content-center">
          <div class="col-lg-9 col-xl-8">
            <header class="mb-4 pb-3 border-bottom" data-aos="fade-up">
              <p class="text-muted small mb-2">{p['category']} · Part {p['part']} of 5 · <time datetime="2026-05-19">19 May 2026</time></p>
              <h1 class="h2 mb-3">{p['h1']}</h1>
              <p class="lead mb-3">{p['lead']}</p>
              <div class="border-start border-primary border-4 ps-3 py-3 bg-light rounded mb-0" role="note">
                <p class="small text-uppercase text-muted mb-1 fw-semibold">In short</p>
                <p class="mb-0">{p['short']}</p>
              </div>
            </header>
            <div class="blog-prose" data-aos="fade-up" data-aos-delay="50">
              {series_nav(p['part'])}
{p['body']}
            </div>
          </div>
        </div>
      </div>
    </article>"""


def nav_footer(prev_href: str, prev_label: str, next_href: str, next_label: str) -> str:
    return f"""
              <p class="small text-muted mt-4 mb-2"><a href="{prev_href}">← {prev_label}</a> · <a href="../index.html#blog">Blog index</a> · <a href="{next_href}">{next_label} →</a></p>
              <p class="mb-0"><a href="{prev_href}" class="btn btn-outline-primary btn-sm"><i class="bi bi-arrow-left" aria-hidden="true"></i> {prev_label}</a>
              <a href="{next_href}" class="btn btn-primary btn-sm ms-2">{next_label} <i class="bi bi-arrow-right" aria-hidden="true"></i></a></p>"""


POSTS = [
    {
        "file": "kubernetes-hands-on-1-local-lab.html",
        "title_page": "Kubernetes Hands-On Part 1: kind, k3s, or minikube — Babulal Tamang",
        "meta": "Part 1 of a beginner Kubernetes course: pick a local cluster (kind, k3s, minikube), install prerequisites, create a lab, and verify kubectl works—before writing YAML.",
        "crumb": "K8s hands-on (1/5)",
        "part": 1,
        "category": "Kubernetes hands-on",
        "h1": "Start Here: A Local Kubernetes Lab on Your Laptop",
        "lead": "You do not need a cloud account to learn Kubernetes. A <strong>local cluster</strong> on your machine is enough to practice Pods, Deployments, and debugging—safely and for free. This post helps you choose between <strong>kind</strong>, <strong>k3s</strong>, and <strong>minikube</strong>, install the tools, and confirm your lab is ready.",
        "short": "Install kubectl and one local distribution (kind is a strong default for learners). Run a smoke test: nodes Ready, a test Pod runs, you can read logs. Then continue to YAML anatomy in Part 2.",
        "body": """
              <h2 class="h4 mt-4">Who this series is for</h2>
              <p>This five-part course is for developers and operators who want <strong>depth with practice</strong>, not only diagrams. If you want the business case first, read <a href="kubernetes-when-how-why-where.html">Kubernetes for business leaders</a>. If you want architecture in plain language, read <a href="kubernetes-architecture-simple.html">Kubernetes architecture in simple terms</a>. This series assumes you are ready to type commands and apply manifests.</p>

              <h2 class="h4 mt-5">Prerequisites (keep it small)</h2>
              <ul>
                <li><strong>A laptop</strong> with macOS, Linux, or Windows (WSL2 works well on Windows).</li>
                <li><strong>About 4–8 GB free RAM</strong> for a comfortable local cluster (you can run leaner, but debugging gets painful).</li>
                <li><strong>Terminal comfort</strong>—copy/paste commands, read errors, retry once after fixing typos.</li>
                <li><strong>Docker or a compatible container runtime</strong> for kind and minikube (k3s can run without Docker on Linux using its bundled containerd).</li>
              </ul>
              <p>You do <em>not</em> need prior production Kubernetes experience. Basic containers help (“an image is a packaged app; a container is a running instance”), but we explain as we go.</p>

              <h2 class="h4 mt-5">Three local clusters, one idea</h2>
              <p>All three tools below run a <strong>real</strong> Kubernetes API on your machine. Your <code>kubectl</code> commands talk to that API the same way they would in AWS, GCP, or Azure—only the scale is tiny.</p>
              <div class="table-responsive">
                <table class="table table-sm table-bordered align-middle">
                  <thead><tr><th>Tool</th><th>Best for</th><th>Trade-offs</th></tr></thead>
                  <tbody>
                    <tr><td><strong>kind</strong> (Kubernetes in Docker)</td><td>CI-like clusters, multi-node tests, learning controllers</td><td>Runs nodes as Docker containers; needs Docker. Very popular in tutorials and KinD-based test pipelines.</td></tr>
                    <tr><td><strong>k3s</strong></td><td>Lightweight “real” clusters, edge, Raspberry Pi, fast startup</td><td>Smaller binary; some components differ (e.g. SQLite instead of etcd by default in single-node). Great when RAM is tight.</td></tr>
                    <tr><td><strong>minikube</strong></td><td>Beginner-friendly single cluster, many drivers</td><td>One command mental model; can feel heavier than k3s on small machines. Excellent docs and add-ons.</td></tr>
                  </tbody>
                </table>
              </div>
              <p><strong>Pick one and stick with it</strong> for this series. Switching mid-course is fine later, but not necessary on day one. If you have no preference, use <strong>kind</strong>—it matches what many platform teams use in automated tests.</p>

              <h2 class="h4 mt-5">Install kubectl (all paths)</h2>
              <p><code>kubectl</code> is the CLI for the Kubernetes API. Install a version within one minor release of your cluster when possible (e.g. cluster 1.30.x, kubectl 1.30.x).</p>
              <ul>
                <li>macOS (Homebrew): <code>brew install kubectl</code></li>
                <li>Linux: follow the official “Install kubectl” guide for your distro, or <code>curl -LO</code> the stable binary from Kubernetes release artifacts.</li>
                <li>Verify: <code>kubectl version --client</code></li>
              </ul>

              <h2 class="h4 mt-5">Option A — kind (recommended default)</h2>
              <pre class="bg-light p-3 rounded small"><code># Install kind (macOS example)
brew install kind

# Create a cluster named "learn"
kind create cluster --name learn

# Point kubectl at it (kind usually merges kubeconfig for you)
kubectl cluster-info
kubectl get nodes</code></pre>
              <p>Expected: one node (or more if you used a multi-node config) in <code>Ready</code> state.</p>

              <h2 class="h4 mt-5">Option B — k3s</h2>
              <pre class="bg-light p-3 rounded small"><code># Linux one-liner (check k3s.io for your OS)
curl -sfL https://get.k3s.io | sh -

# kubeconfig is often at /etc/rancher/k3s/k3s.yaml — copy or export KUBECONFIG
export KUBECONFIG=/etc/rancher/k3s/k3s.yaml
kubectl get nodes</code></pre>
              <p>On macOS, many learners run k3s inside a VM or use <code>k3d</code> (k3s in Docker)—treat that like kind with a k3s distribution inside.</p>

              <h2 class="h4 mt-5">Option C — minikube</h2>
              <pre class="bg-light p-3 rounded small"><code>brew install minikube   # or use the installer from minikube docs
minikube start
kubectl get nodes</code></pre>
              <p>Minikube can use Docker, Hyperkit, KVM, and other drivers. If <code>minikube start</code> fails, read the suggested driver flag—this is the most common beginner stumbling block.</p>

              <h2 class="h4 mt-5">Smoke test: prove the cluster works</h2>
              <p>Run a disposable Pod and read its logs. If this succeeds, your lab is real enough for the rest of the series.</p>
              <pre class="bg-light p-3 rounded small"><code>kubectl run hello --image=busybox:1.36 --restart=Never -- sleep 3600
kubectl wait --for=condition=Ready pod/hello --timeout=90s
kubectl logs hello
kubectl delete pod hello</code></pre>
              <p>If the Pod stays <code>Pending</code>, run <code>kubectl describe pod hello</code> and read <strong>Events</strong> at the bottom—image pull errors, insufficient CPU, or CNI not ready are the usual suspects on local clusters.</p>

              <h2 class="h4 mt-5">kubectl habits to start now</h2>
              <ul>
                <li><strong>Context and namespace:</strong> <code>kubectl config get-contexts</code> and <code>kubectl get ns</code>. Most tutorials use <code>default</code>; in Part 4 we move workloads into named namespaces.</li>
                <li><strong>Help built in:</strong> <code>kubectl explain pod.spec.containers</code> — your offline documentation (Part 2 goes deeper).</li>
                <li><strong>Do not learn production on <code>kube-system</code>:</strong> avoid deleting platform Pods; practice in <code>default</code> or a dedicated namespace.</li>
              </ul>

              <h2 class="h4 mt-5">Clean up when you are done for the day</h2>
              <ul>
                <li>kind: <code>kind delete cluster --name learn</code></li>
                <li>minikube: <code>minikube delete</code></li>
                <li>k3s: use your install method’s uninstall script</li>
              </ul>
              <p>Stopping the cluster frees RAM. Your manifests (YAML files) should live in Git on your machine—clusters are cattle, files are the memory of what you intended.</p>

              <h2 class="h4 mt-5">What comes next</h2>
              <p>Part 2 dissects a manifest line by line: <code>apiVersion</code>, <code>kind</code>, <code>metadata</code>, <code>spec</code>, labels, and selectors—the vocabulary every other resource reuses.</p>

              <p class="small text-muted mt-4 mb-2"><a href="../index.html#blog">Blog index</a> · <a href="kubernetes-architecture-simple.html">Architecture overview</a> · <a href="kubernetes-hands-on-2-yaml-anatomy.html">Part 2 — YAML anatomy →</a></p>
              <p class="mb-0"><a href="../index.html#blog" class="btn btn-outline-primary btn-sm"><i class="bi bi-arrow-left" aria-hidden="true"></i> Blog index</a>
              <a href="kubernetes-hands-on-2-yaml-anatomy.html" class="btn btn-primary btn-sm ms-2">Continue to Part 2 <i class="bi bi-arrow-right" aria-hidden="true"></i></a></p>""",
    },
    {
        "file": "kubernetes-hands-on-2-yaml-anatomy.html",
        "title_page": "Kubernetes Hands-On Part 2: YAML Manifest Anatomy — Babulal Tamang",
        "meta": "Part 2: anatomy of a Kubernetes YAML manifest—apiVersion, kind, metadata, spec, labels, selectors, multi-document files, and kubectl explain for beginners.",
        "crumb": "K8s hands-on (2/5)",
        "part": 2,
        "category": "Kubernetes hands-on",
        "h1": "Anatomy of a Kubernetes Manifest (YAML, Line by Line)",
        "lead": "Kubernetes is <strong>declarative</strong>: you hand the API a document that says what should exist. That document is usually YAML. Before you memorize twenty resource types, learn the <strong>skeleton</strong> every manifest shares—and how to discover fields you have not memorized yet.",
        "short": "Every object has apiVersion, kind, metadata, and spec. Labels identify things; selectors connect controllers to Pods. Use kubectl explain and dry-run to validate before you apply.",
        "body": """
              <h2 class="h4 mt-4">YAML rules that save beginners hours</h2>
              <ul>
                <li><strong>Indentation matters.</strong> Use spaces, not tabs (two spaces per level is common).</li>
                <li><strong>Maps vs lists:</strong> <code>key: value</code> is a map; <code>- item</code> under a key is a list.</li>
                <li><strong>Strings:</strong> Quote values with special characters. Numbers and booleans are unquoted (<code>replicas: 3</code>, not <code>"3"</code> unless you mean a string).</li>
                <li><strong>One file can hold multiple documents</strong> separated by <code>---</code> on its own line.</li>
              </ul>

              <h2 class="h4 mt-5">The four top-level fields</h2>
              <p>Almost every Kubernetes object you create looks like this shape:</p>
              <pre class="bg-light p-3 rounded small"><code>apiVersion: v1          # which API group and version
kind: Pod               # what type of object
metadata:               # identity and labels
  name: demo
  namespace: default
  labels:
    app.kubernetes.io/name: demo
spec:                   # desired state — shape depends on kind
  containers:
    - name: app
      image: nginx:1.25-alpine
      ports:
        - containerPort: 80</code></pre>

              <h3 class="h5 mt-4">apiVersion</h3>
              <p>Tells the API server which schema to validate against. Examples:</p>
              <ul>
                <li><code>v1</code> — core resources: Pod, Service, ConfigMap, Namespace.</li>
                <li><code>apps/v1</code> — Deployment, ReplicaSet, StatefulSet, DaemonSet.</li>
                <li><code>batch/v1</code> — Job, CronJob.</li>
              </ul>
              <p>Wrong <code>apiVersion</code> usually fails at apply time with a clear error. Use <code>kubectl api-resources</code> to see kinds and versions your cluster supports.</p>

              <h3 class="h5 mt-4">kind</h3>
              <p>The resource type: <code>Pod</code>, <code>Deployment</code>, <code>Service</code>, and so on. It must match <code>apiVersion</code> (you cannot put a Deployment in <code>v1</code>).</p>

              <h3 class="h5 mt-4">metadata</h3>
              <ul>
                <li><strong>name</strong> — unique within the namespace for most types.</li>
                <li><strong>namespace</strong> — scope; omit to use <code>default</code> or set with <code>kubectl apply -n team-a -f file.yaml</code>.</li>
                <li><strong>labels</strong> — key/value tags for selection, governance, and observability (Part 4).</li>
                <li><strong>annotations</strong> — non-identifying metadata (tooling hints, last-applied URLs); not used in label selectors.</li>
              </ul>

              <h3 class="h5 mt-4">spec</h3>
              <p>What you want. The API fills in <strong>status</strong> for you (phase, conditions, Pod IPs). Beginners should read <code>spec</code> in Git and <code>status</code> with <code>kubectl describe</code> when debugging.</p>

              <h2 class="h4 mt-5">Labels and selectors: how objects find each other</h2>
              <p>A <strong>Deployment</strong> does not list Pod names. It says: “keep three Pods that match these labels.” A <strong>Service</strong> routes traffic to Pods with matching labels.</p>
              <pre class="bg-light p-3 rounded small"><code># Fragment — Deployment template labels
spec:
  selector:
    matchLabels:
      app.kubernetes.io/name: demo
  template:
    metadata:
      labels:
        app.kubernetes.io/name: demo</code></pre>
              <p>The Deployment’s <code>spec.selector</code> must match <code>spec.template.metadata.labels</code>. If they diverge, the controller cannot adopt Pods—or worse, adopts the wrong ones. This is one of the most common copy-paste mistakes in workshops.</p>

              <h2 class="h4 mt-5">Read the schema instead of guessing</h2>
              <pre class="bg-light p-3 rounded small"><code>kubectl explain pod
kubectl explain pod.spec.containers
kubectl explain deployment.spec.template</code></pre>
              <p>Think of <code>kubectl explain</code> as structured help for YAML authors. Pair it with the official Kubernetes API reference when you need field-level semantics.</p>

              <h2 class="h4 mt-5">Validate before you mutate the cluster</h2>
              <pre class="bg-light p-3 rounded small"><code># Client-side dry run — catches many typos
kubectl apply -f demo.yaml --dry-run=client

# Server-side dry run (when enabled) — API validates admission
kubectl apply -f demo.yaml --dry-run=server</code></pre>
              <p>Dry-run does not replace review in Git, but it catches “wrong indentation under <code>containers</code>” faster than a crash loop.</p>

              <h2 class="h4 mt-5">Imperative vs declarative (why YAML wins)</h2>
              <p>You <em>can</em> run <code>kubectl run</code> and <code>kubectl expose</code> for quick experiments. For anything you will repeat, prefer <strong>manifests in Git</strong>—the same discipline as <a href="gitops-principles.html">GitOps</a>, even before you install Flux or Argo CD.</p>

              <h2 class="h4 mt-5">Practice exercise</h2>
              <ol>
                <li>Save the Pod example above as <code>demo-pod.yaml</code>.</li>
                <li>Run <code>kubectl apply -f demo-pod.yaml</code> on your lab from <a href="kubernetes-hands-on-1-local-lab.html">Part 1</a>.</li>
                <li>Change the image tag, run <code>kubectl apply</code> again, and observe that Pod spec fields are largely immutable—Kubernetes may recreate the Pod.</li>
                <li>Delete with <code>kubectl delete -f demo-pod.yaml</code>.</li>
              </ol>

              """ + nav_footer(
            "kubernetes-hands-on-1-local-lab.html",
            "Part 1",
            "kubernetes-hands-on-3-first-workloads.html",
            "Part 3",
        ),
    },
    {
        "file": "kubernetes-hands-on-3-first-workloads.html",
        "title_page": "Kubernetes Hands-On Part 3: Pod, Deployment, Service — Babulal Tamang",
        "meta": "Part 3 hands-on: run your first Pod, scale with a Deployment, expose traffic with a Service, and use port-forward on kind, k3s, or minikube.",
        "crumb": "K8s hands-on (3/5)",
        "part": 3,
        "category": "Kubernetes hands-on",
        "h1": "Your First Workloads: Pod, Deployment, and Service",
        "lead": "A lone <strong>Pod</strong> is a teaching tool; a <strong>Deployment</strong> is how you run stateless apps in production; a <strong>Service</strong> gives stable networking to ephemeral Pods. This post walks through all three on your local cluster—with commands you can run in ten minutes.",
        "short": "Create a Deployment with multiple replicas, confirm Pods with labels, expose port 80 with a ClusterIP Service, and reach the app via port-forward. Delete with the same YAML file you applied.",
        "body": """
              <h2 class="h4 mt-4">Mental model</h2>
              <ul>
                <li><strong>Pod</strong> — one or more containers that share network and storage; smallest schedulable unit.</li>
                <li><strong>Deployment</strong> — declares desired replicas and rollout strategy; owns ReplicaSets, which own Pods.</li>
                <li><strong>Service</strong> — stable DNS name and virtual IP targeting Pods by label.</li>
              </ul>
              <p>For architecture context see <a href="kubernetes-architecture-simple.html">Kubernetes architecture in simple terms</a>.</p>

              <h2 class="h4 mt-5">Step 1 — Deployment (three replicas)</h2>
              <p>Save as <code>web.yaml</code>:</p>
              <pre class="bg-light p-3 rounded small"><code>apiVersion: apps/v1
kind: Deployment
metadata:
  name: web
  labels:
    app.kubernetes.io/name: web
spec:
  replicas: 3
  selector:
    matchLabels:
      app.kubernetes.io/name: web
  template:
    metadata:
      labels:
        app.kubernetes.io/name: web
    spec:
      containers:
        - name: nginx
          image: nginx:1.25-alpine
          ports:
            - containerPort: 80</code></pre>
              <pre class="bg-light p-3 rounded small"><code>kubectl apply -f web.yaml
kubectl get deployment web
kubectl get pods -l app.kubernetes.io/name=web</code></pre>
              <p>You should see three Pods, each with a unique name suffix. Kill one Pod with <code>kubectl delete pod &lt;name&gt;</code> and watch the Deployment replace it—<strong>reconciliation</strong> in action.</p>

              <h2 class="h4 mt-5">Step 2 — Service (ClusterIP)</h2>
              <p>Append to the same file after <code>---</code> or save as <code>web-svc.yaml</code>:</p>
              <pre class="bg-light p-3 rounded small"><code>apiVersion: v1
kind: Service
metadata:
  name: web
spec:
  type: ClusterIP
  selector:
    app.kubernetes.io/name: web
  ports:
    - port: 80
      targetPort: 80</code></pre>
              <pre class="bg-light p-3 rounded small"><code>kubectl apply -f web-svc.yaml   # or combined file
kubectl get svc web
kubectl get endpoints web</code></pre>
              <p><code>endpoints</code> should list Pod IPs. If empty, your Service selector does not match Pod labels—return to Part 2’s selector section.</p>

              <h2 class="h4 mt-5">Step 3 — Reach the app locally</h2>
              <p>On a laptop cluster there is usually no cloud load balancer. Use port-forward:</p>
              <pre class="bg-light p-3 rounded small"><code>kubectl port-forward svc/web 8080:80
# In another terminal:
curl -s -o /dev/null -w "%{http_code}\\n" http://127.0.0.1:8080/</code></pre>
              <p>Expect HTTP <code>200</code>. For minikube you can also try <code>minikube service web</code> when using certain addons—port-forward works everywhere.</p>

              <h2 class="h4 mt-5">Optional — one-off Pod (know the difference)</h2>
              <pre class="bg-light p-3 rounded small"><code>apiVersion: v1
kind: Pod
metadata:
  name: debug-once
spec:
  containers:
    - name: shell
      image: busybox:1.36
      command: ["sh", "-c", "echo hello && sleep 30"]</code></pre>
              <p>Pods created alone are not self-healing. Use them for debugging or Jobs—not for serving customer traffic.</p>

              <h2 class="h4 mt-5">Rollout exercise</h2>
              <pre class="bg-light p-3 rounded small"><code>kubectl set image deployment/web nginx=nginx:1.27-alpine
kubectl rollout status deployment/web
kubectl rollout history deployment/web</code></pre>
              <p>Prefer changing image tags in YAML and <code>kubectl apply</code> when practicing GitOps habits. Imperative <code>set image</code> is fine for labs.</p>

              <h2 class="h4 mt-5">Clean up</h2>
              <pre class="bg-light p-3 rounded small"><code>kubectl delete -f web.yaml
# include Service manifest if separate</code></pre>

              """ + nav_footer(
            "kubernetes-hands-on-2-yaml-anatomy.html",
            "Part 2",
            "kubernetes-hands-on-4-day-one-practices.html",
            "Part 4",
        ),
    },
    {
        "file": "kubernetes-hands-on-4-day-one-practices.html",
        "title_page": "Kubernetes Hands-On Part 4: Day-One Best Practices — Babulal Tamang",
        "meta": "Part 4: Kubernetes best practices for beginners—namespaces, recommended labels, resource requests and limits, security contexts, ConfigMaps, and why not to kubectl edit production.",
        "crumb": "K8s hands-on (4/5)",
        "part": 4,
        "category": "Kubernetes hands-on",
        "h1": "Best Practices From Day One (Before Bad Habits Stick)",
        "lead": "Local labs forgive sloppiness; production does not. The good news: a small set of habits—namespaces, labels, resource declarations, sane security defaults, and config in objects instead of images—will make your manifests look like a platform team wrote them from the start.",
        "short": "Isolate by namespace, label with app.kubernetes.io/*, set requests and limits, run non-root where you can, store config in ConfigMaps, keep secrets out of Git, and treat kubectl apply -f as your default workflow.",
        "body": """
              <h2 class="h4 mt-4">Namespaces: soft walls between teams and environments</h2>
              <pre class="bg-light p-3 rounded small"><code>apiVersion: v1
kind: Namespace
metadata:
  name: learn-dev
  labels:
    environment: dev</code></pre>
              <pre class="bg-light p-3 rounded small"><code>kubectl apply -f ns-learn-dev.yaml
kubectl apply -f web.yaml -n learn-dev
kubectl get all -n learn-dev</code></pre>
              <p>Namespaces do not replace security by themselves, but they organize RBAC, quotas, and DNS (<code>service.learn-dev.svc.cluster.local</code>). Avoid dumping everything into <code>default</code> once you share a cluster.</p>

              <h2 class="h4 mt-5">Labels: the address book of the cluster</h2>
              <p>Use the <strong>recommended labels</strong> where they fit:</p>
              <ul>
                <li><code>app.kubernetes.io/name</code> — application name (used in selectors).</li>
                <li><code>app.kubernetes.io/instance</code> — this deployment of the app (e.g. <code>web-prod</code>).</li>
                <li><code>app.kubernetes.io/version</code> — version string or image tag.</li>
                <li><code>app.kubernetes.io/component</code> — <code>api</code>, <code>worker</code>, <code>database</code>.</li>
                <li><code>app.kubernetes.io/part-of</code> — larger system (e.g. <code>billing</code>).</li>
                <li><code>app.kubernetes.io/managed-by</code> — <code>helm</code>, <code>kustomize</code>, or your team name.</li>
              </ul>
              <p>Consistent labels unlock filtering, NetworkPolicies, cost allocation, and GitOps diffs that humans can read.</p>

              <h2 class="h4 mt-5">Resource requests and limits</h2>
              <p>Without requests, the scheduler guesses. Without limits, one noisy neighbor can starve a node.</p>
              <pre class="bg-light p-3 rounded small"><code>resources:
  requests:
    cpu: 100m
    memory: 128Mi
  limits:
    cpu: 250m
    memory: 256Mi</code></pre>
              <p>Start conservative in labs; tune with metrics later. <code>cpu</code> is measured in cores (<code>100m</code> = 0.1 core). <code>memory</code> uses binary suffixes (<code>Mi</code>, <code>Gi</code>).</p>

              <h2 class="h4 mt-5">Security context basics (least privilege)</h2>
              <pre class="bg-light p-3 rounded small"><code>securityContext:
  runAsNonRoot: true
  runAsUser: 101
  allowPrivilegeEscalation: false
  readOnlyRootFilesystem: true
  capabilities:
    drop: ["ALL"]</code></pre>
              <p>Not every image supports non-root or read-only roots on day one—nginx and distroless examples differ. Treat these fields as <strong>goals</strong>: fix the image or mount a writable <code>emptyDir</code> for temp paths instead of disabling security “because local.”</p>

              <h2 class="h4 mt-5">Configuration: ConfigMap, not baked into the image</h2>
              <pre class="bg-light p-3 rounded small"><code>apiVersion: v1
kind: ConfigMap
metadata:
  name: web-config
  namespace: learn-dev
data:
  APP_MODE: "lab"</code></pre>
              <p>Mount as env vars or files in the Pod template. Changing config becomes a reviewed YAML change, not a rebuild of a golden image for every toggle.</p>

              <h2 class="h4 mt-5">Secrets: never commit real ones</h2>
              <ul>
                <li>Local lab: <code>kubectl create secret generic demo --from-literal=token=test</code> is enough to learn wiring.</li>
                <li>Real clusters: use sealed secrets, external secrets operators, or cloud KMS—see <a href="gitops-principles.html">GitOps principles</a>.</li>
                <li>Add <code>*.secret.yaml</code> patterns to <code>.gitignore</code> if you must keep local samples.</li>
              </ul>

              <h2 class="h4 mt-5">Workflow habits that scale</h2>
              <ul>
                <li><strong>Prefer <code>kubectl apply -f</code></strong> over <code>kubectl edit</code> for anything you care about—edit drifts from Git.</li>
                <li><strong>One concern per manifest file</strong> or one kustomization base; avoid thousand-line blobs.</li>
                <li><strong>Pin images</strong> to tags or digests (<code>nginx:1.25-alpine</code>, not <code>latest</code>).</li>
                <li><strong>Probes:</strong> add <code>readinessProbe</code> and <code>livenessProbe</code> before you call a Deployment “production ready” (Part 5 shows debugging when they fail).</li>
                <li><strong>Policy later:</strong> admission controllers (OPA Gatekeeper, Kyverno) encode what you already practice manually.</li>
              </ul>

              <h2 class="h4 mt-5">Lab challenge</h2>
              <p>Refactor your Part 3 <code>web</code> Deployment into namespace <code>learn-dev</code> with recommended labels, resource requests/limits, and a ConfigMap env var. Apply from a folder in Git. Delete the namespace to wipe the experiment: <code>kubectl delete namespace learn-dev</code>.</p>

              """ + nav_footer(
            "kubernetes-hands-on-3-first-workloads.html",
            "Part 3",
            "kubernetes-hands-on-5-debug-next-steps.html",
            "Part 5",
        ),
    },
    {
        "file": "kubernetes-hands-on-5-debug-next-steps.html",
        "title_page": "Kubernetes Hands-On Part 5: Debug and Next Steps — Babulal Tamang",
        "meta": "Part 5: debug Kubernetes on kind, k3s, or minikube—kubectl describe, logs, events, probes, common failures—and a learning path toward GitOps and certification.",
        "crumb": "K8s hands-on (5/5)",
        "part": 5,
        "category": "Kubernetes hands-on",
        "h1": "Debug Like an Operator, Then Choose Your Next Path",
        "lead": "Clusters fail in predictable categories: scheduling, image pull, crash loop, configuration, networking. A short <strong>debugging order</strong> and a handful of commands will carry you through most beginner incidents on kind, k3s, or minikube—and the same order works in production.",
        "short": "Use get → describe → logs → events. Fix ImagePullBackOff, CrashLoopBackOff, and probe failures with intent. Then deepen with GitOps, observability, and structured certification practice.",
        "body": """
              <h2 class="h4 mt-4">The debugging order (memorize this)</h2>
              <ol>
                <li><code>kubectl get pods -n &lt;ns&gt;</code> — phase and restarts at a glance.</li>
                <li><code>kubectl describe pod &lt;name&gt; -n &lt;ns&gt;</code> — events, node, probes, volumes.</li>
                <li><code>kubectl logs &lt;name&gt; -n &lt;ns&gt; [--previous]</code> — stdout/stderr; <code>--previous</code> for crashed containers.</li>
                <li><code>kubectl get events -n &lt;ns&gt; --sort-by='.lastTimestamp'</code> — timeline when describe is noisy.</li>
              </ol>
              <p>For Deployments add <code>kubectl describe deployment</code> and <code>kubectl rollout status</code>. For Services add <code>kubectl get endpoints</code> and verify selectors.</p>

              <h2 class="h4 mt-5">Common Pod states and what they mean</h2>
              <div class="table-responsive">
                <table class="table table-sm table-bordered">
                  <thead><tr><th>Symptom</th><th>Likely cause</th><th>What to do</th></tr></thead>
                  <tbody>
                    <tr><td><code>Pending</code></td><td>No node capacity, taints, PVC not bound</td><td><code>describe pod</code> → Events; <code>get nodes</code></td></tr>
                    <tr><td><code>ImagePullBackOff</code></td><td>Wrong name/tag, private registry auth</td><td>Fix image; <code>create secret docker-registry</code> if private</td></tr>
                    <tr><td><code>CrashLoopBackOff</code></td><td>App exits on start, bad command, missing config</td><td><code>logs --previous</code>; run image locally with same command</td></tr>
                    <tr><td><code>CreateContainerConfigError</code></td><td>Missing Secret/ConfigMap key</td><td><code>describe pod</code>; verify referenced objects exist</td></tr>
                    <tr><td>Running but not Ready</td><td>Readiness probe failing</td><td>Check probe path/port; test inside Pod with <code>kubectl exec</code></td></tr>
                  </tbody>
                </table>
              </div>

              <h2 class="h4 mt-5">Interactive debugging</h2>
              <pre class="bg-light p-3 rounded small"><code>kubectl exec -it deploy/web -n learn-dev -- sh
# inside: wget -qO- http://127.0.0.1/   OR apk/curl depending on image

kubectl run tmp-curl --rm -it --image=curlimages/curl --restart=Never -- \\
  curl -s http://web.learn-dev.svc.cluster.local/</code></pre>
              <p>DNS names follow <code>&lt;service&gt;.&lt;namespace&gt;.svc.cluster.local</code>. If curl from another Pod fails, you have a Service or NetworkPolicy problem—not “the internet is down.”</p>

              <h2 class="h4 mt-5">When port-forward works but Ingress does not</h2>
              <p>Ingress needs an <strong>ingress controller</strong> (nginx, traefik, etc.). Local clusters often do not install one by default. For learning, port-forward and <code>minikube tunnel</code> (when documented for your driver) are enough. Treat Ingress as a follow-on topic after Services make sense.</p>

              <h2 class="h4 mt-5">Observability: the next layer</h2>
              <ul>
                <li><strong>Metrics:</strong> <code>kubectl top pods</code> (requires metrics-server on many clusters).</li>
                <li><strong>Dashboards:</strong> Prometheus/Grafana in a later lab—not required on day one.</li>
                <li><strong>Tracing:</strong> OpenTelemetry when you operate microservices at scale.</li>
              </ul>
              <p>The architecture post’s incident mental model—API → nodes → schedule → container → network—still applies; metrics tell you <em>where</em> in that chain to look.</p>

              <h2 class="h4 mt-5">Where to go after this series</h2>
              <ul>
                <li><strong>GitOps:</strong> <a href="gitops-principles.html">Git as the control plane</a> — store manifests in Git, automate sync.</li>
                <li><strong>Platform context:</strong> <a href="devops-life-business-value.html">DevOps life and business value</a>, <a href="cloud-platform-evolution.html">cloud platform evolution</a>.</li>
                <li><strong>Structured practice:</strong> Kubernetes official tutorials; CKA/CKAD-style tasks (multi-object YAML under time pressure).</li>
                <li><strong>Production topics:</strong> Ingress, PersistentVolumes, StatefulSets, Helm/Kustomize, network policies, pod disruption budgets.</li>
              </ul>

              <h2 class="h4 mt-5">Series recap</h2>
              <ol>
                <li><a href="kubernetes-hands-on-1-local-lab.html">Local lab</a> — kind, k3s, or minikube.</li>
                <li><a href="kubernetes-hands-on-2-yaml-anatomy.html">YAML anatomy</a> — apiVersion, kind, metadata, spec, labels.</li>
                <li><a href="kubernetes-hands-on-3-first-workloads.html">First workloads</a> — Deployment and Service.</li>
                <li><a href="kubernetes-hands-on-4-day-one-practices.html">Day-one practices</a> — namespaces, labels, resources, security.</li>
                <li><strong>This post</strong> — debug and roadmap.</li>
              </ol>
              <p>You now have a loop: declare in YAML → apply → observe → fix → commit. That loop is the job—whether the cluster lives on your laptop or in three regions.</p>

              <p class="small text-muted mt-4 mb-2"><a href="kubernetes-hands-on-4-day-one-practices.html">← Part 4</a> · <a href="../index.html#blog">Blog index</a> · <a href="kubernetes-hands-on-1-local-lab.html">Start over at Part 1</a></p>
              <p class="mb-0"><a href="kubernetes-hands-on-4-day-one-practices.html" class="btn btn-outline-primary btn-sm"><i class="bi bi-arrow-left" aria-hidden="true"></i> Part 4</a>
              <a href="kubernetes-hands-on-1-local-lab.html" class="btn btn-primary btn-sm ms-2">Back to Part 1 <i class="bi bi-arrow-repeat" aria-hidden="true"></i></a></p>""",
    },
]


if __name__ == "__main__":
    for p in POSTS:
        upsert_post(p, build_article(p))
        print("content", p["file"])
    build_blogs()
    print("built", len(POSTS), "posts")
