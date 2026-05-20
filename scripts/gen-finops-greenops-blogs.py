#!/usr/bin/env python3
"""Generate FinOps/GreenOps series blog posts 3–5."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from lib.blog_registry import upsert_post  # noqa: E402
from build_site import build_blogs  # noqa: E402

NAV = [
    ("Technology’s real-world footprint", "finops-greenops-1-invisible-bill.html"),
    ("Why conservation and sustainability matter", "finops-greenops-2-conservation-matters.html"),
    ("Stop guessing what the cloud costs", "finops-greenops-3-finops-plain-english.html"),
    ("Running technology with a lighter footprint", "finops-greenops-4-greenops-plain-english.html"),
    ("When FinOps and GreenOps work together", "finops-greenops-5-smarter-lighter.html"),
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
        f"Sustainability &amp; responsible technology · Part {part} of 5</p>\n"
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


POSTS = [
    {
        "file": "finops-greenops-3-finops-plain-english.html",
        "title_page": "FinOps: Making Cloud Spend Visible — Babulal Tamang",
        "meta": "Part 3: FinOps explained for everyone—why cloud bills surprise teams, what FinOps practices do, and how financial accountability helps organizations without blocking innovation.",
        "crumb": "FinOps (3/5)",
        "part": 3,
        "category": "FinOps",
        "h1": "FinOps: Stop Guessing What the Cloud Costs",
        "lead": "Cloud lets you rent computers by the minute—but the bill can feel like a mystery that arrives after the party. FinOps is how mature teams bring cloud spending into daylight: shared visibility, smart trade-offs, and everyone taking a little ownership of the meter.",
        "short": "FinOps is a way of working that helps engineering, finance, and leadership understand and improve cloud costs together. It is not about saying “no”—it is about spending deliberately on what matters.",
        "body": """
              <h2 class="h4 mt-4">What is FinOps?</h2>
              <p><strong>FinOps</strong> (cloud financial operations) is a practice—not a single tool—that helps organizations <strong>get value from cloud spending</strong>. The FinOps Foundation describes it as bringing together engineering, finance, and business so decisions are fast, informed, and accountable.</p>
              <p>If you have ever heard “our AWS bill doubled and nobody knows why,” you have seen the problem FinOps tries to solve.</p>

              <h2 class="h4 mt-5">Why cloud money is confusing</h2>
              <ul>
                <li><strong>Pay-as-you-go:</strong> Costs change daily with traffic, storage, and experiments.</li>
                <li><strong>Many owners:</strong> Dozens of teams can spin up resources with a credit card or account.</li>
                <li><strong>Technical labels:</strong> Bills list services and SKUs, not product features customers use.</li>
                <li><strong>Speed wins:</strong> Teams are rewarded for shipping; cost is noticed later.</li>
              </ul>
              <p>Traditional IT budgeting assumed fixed servers bought once a year. Cloud flipped that model. FinOps is the <strong>new discipline</strong> for a new model.</p>

              <h2 class="h4 mt-5">The three FinOps phases (in human language)</h2>
              <ol>
                <li><strong>Inform:</strong> Make costs visible—who spent what, on which product, this week vs last month.</li>
                <li><strong>Optimize:</strong> Remove waste, right-size systems, use discounts or reserved capacity where it makes sense.</li>
                <li><strong>Operate:</strong> Build habits—budgets, reviews, goals—so cost is part of normal delivery, not a quarterly surprise.</li>
              </ol>
              <p>You do not need to master all three on day one. Start with <strong>visibility</strong>. You cannot fix what you cannot see.</p>

              <h2 class="h4 mt-5">Who is involved?</h2>
              <ul>
                <li><strong>Engineers</strong> choose instance sizes, storage classes, and architectures.</li>
                <li><strong>Product managers</strong> decide which features justify infrastructure.</li>
                <li><strong>Finance</strong> forecasts, allocates, and reports to leadership.</li>
                <li><strong>Leadership</strong> sets priorities: growth vs margin vs reliability.</li>
              </ul>
              <p>FinOps works when cost is a <strong>shared conversation</strong>, not a blame game thrown at one team after the invoice arrives.</p>

              <h2 class="h4 mt-5">Practical habits that help any organization</h2>
              <ul>
                <li>Tag resources by team, environment, and product so bills can be split fairly.</li>
                <li>Shut down or scale down non-production environments nights and weekends.</li>
                <li>Review the top ten cost drivers monthly—not only the total.</li>
                <li>Set targets (“spend per customer,” “cost per transaction”) tied to business metrics.</li>
                <li>Celebrate savings that do not harm reliability—idle clusters removed, oversized databases resized.</li>
              </ul>

              <h2 class="h4 mt-5">FinOps and the environment (bridge to GreenOps)</h2>
              <p>Waste in the cloud is often <strong>waste in the physical world</strong>: servers running with no users, oversized machines, and duplicate data copies all consume electricity. Many FinOps wins—turning off idle resources, right-sizing—also reduce energy use. That is why FinOps pairs naturally with <a href="finops-greenops-4-greenops-plain-english.html">GreenOps</a> in Part 4 and our closing essay in <a href="finops-greenops-5-smarter-lighter.html">Part 5</a>.</p>
              <p>If you have not read the series foundation, start with <a href="finops-greenops-1-invisible-bill.html">Part 1</a> and <a href="finops-greenops-2-conservation-matters.html">Part 2</a>.</p>

              <p class="small text-muted mt-4 mb-2"><a href="finops-greenops-2-conservation-matters.html">← Part 2</a> · <a href="../index.html#blog">Blog index</a> · <a href="finops-greenops-4-greenops-plain-english.html">Part 4 — GreenOps →</a></p>
              <p class="mb-0"><a href="finops-greenops-2-conservation-matters.html" class="btn btn-outline-primary btn-sm"><i class="bi bi-arrow-left" aria-hidden="true"></i> Part 2</a>
              <a href="finops-greenops-4-greenops-plain-english.html" class="btn btn-primary btn-sm ms-2">Continue to Part 4 <i class="bi bi-arrow-right" aria-hidden="true"></i></a></p>""",
    },
    {
        "file": "finops-greenops-4-greenops-plain-english.html",
        "title_page": "GreenOps: Technology That Respects the Planet — Babulal Tamang",
        "meta": "Part 4: GreenOps explained for everyone—how teams reduce the environmental impact of running software, from cleaner energy and efficient code to measuring carbon and avoiding greenwashing.",
        "crumb": "GreenOps (4/5)",
        "part": 4,
        "category": "GreenOps",
        "h1": "GreenOps: Running Technology With a Lighter Footprint",
        "lead": "GreenOps is the operational side of sustainable technology: the everyday choices teams make so software uses less energy, lasts longer, and relies on cleaner power where possible—without pretending one checkbox fixes the climate.",
        "short": "GreenOps brings environmental thinking into how systems are built and run—measurement, efficiency, renewable power, and honest reporting—so digital growth does not ignore physical limits.",
        "body": """
              <h2 class="h4 mt-4">What is GreenOps?</h2>
              <p><strong>GreenOps</strong> (green operations) applies sustainability ideas to <strong>IT operations</strong>: data centers, cloud platforms, networks, and the software that runs on them. It is related to <em>Green IT</em> and <em>sustainable software engineering</em>, but GreenOps stresses <strong>ongoing operations</strong>—what happens after you deploy, every day and every night.</p>
              <p>Where <a href="finops-greenops-3-finops-plain-english.html">FinOps</a> asks “are we spending wisely?”, GreenOps asks “are we using energy and materials responsibly?”</p>

              <h2 class="h4 mt-5">Why GreenOps is needed</h2>
              <p>As <a href="finops-greenops-1-invisible-bill.html">Part 1</a> explained, digital services have a physical cost. Demand for AI, video, and always-on services is growing. Without deliberate design, energy use grows too—even when chips get more efficient (a pattern known as <strong>Jevons paradox</strong>: efficiency can increase total use because services get cheaper to run).</p>
              <p>GreenOps is how teams ensure growth does not automatically mean <strong>maximum waste</strong>.</p>

              <h2 class="h4 mt-5">Pillars anyone can understand</h2>
              <h3 class="h5 mt-4">1. Measure</h3>
              <p>You do not need perfect numbers on day one. Start with proxies: electricity use reported by your cloud provider, estimates of carbon per region, or tools that map services to energy. Transparency beats silence.</p>
              <h3 class="h5 mt-4">2. Reduce waste</h3>
              <ul>
                <li>Turn off idle environments and orphaned resources.</li>
                <li>Right-size compute and storage (often the same fixes as FinOps).</li>
                <li>Schedule heavy batch jobs when grids are cleaner or demand is lower.</li>
                <li>Cache and compress data so fewer bytes travel and fewer disks spin.</li>
              </ul>
              <h3 class="h5 mt-4">3. Choose cleaner energy</h3>
              <p>Major cloud regions differ in how much renewable power feeds the grid. When latency and compliance allow, running workloads in <strong>greener regions</strong> can lower emissions per unit of work.</p>
              <h3 class="h5 mt-4">4. Design efficient software</h3>
              <p>Slower algorithms, chatty APIs, and huge machine-learning models cost more than lean designs. Efficiency is a feature—for users and for the planet.</p>
              <h3 class="h5 mt-4">5. Extend hardware life</h3>
              <p>Refreshing laptops and servers on a sensible cycle, refurbishing, and recycling e-waste responsibly reduces mining and landfill pressure.</p>

              <h2 class="h4 mt-5">GreenOps in daily team life</h2>
              <ul>
                <li>Platform teams publish a simple “sustainability checklist” next to security checklists.</li>
                <li>Product teams ask whether a feature needs real-time global sync or can batch overnight.</li>
                <li>Leadership sets modest public targets—e.g., reduce idle compute by 20%—and reports progress honestly.</li>
              </ul>

              <h2 class="h4 mt-5">Avoiding greenwashing</h2>
              <p>Greenwashing is marketing that sounds eco-friendly without proof. Good GreenOps means:</p>
              <ul>
                <li>Explaining assumptions (“we used provider X’s carbon tool for region Y”).</li>
                <li>Not claiming carbon neutrality from offsets alone while ignoring efficiency.</li>
                <li>Improving the worst hotspots first, not only advertising a solar panel on one office.</li>
              </ul>

              <h2 class="h4 mt-5">Connection to conservation</h2>
              <p><a href="finops-greenops-2-conservation-matters.html">Part 2</a> framed conservation as protecting shared resources. GreenOps is conservation applied to <strong>the digital stack</strong>: less sprawl, cleaner power, longer-lived gear, and software that does the job without excess.</p>

              <p class="small text-muted mt-4 mb-2"><a href="finops-greenops-3-finops-plain-english.html">← Part 3</a> · <a href="../index.html#blog">Blog index</a> · <a href="finops-greenops-5-smarter-lighter.html">Part 5 — Together →</a></p>
              <p class="mb-0"><a href="finops-greenops-3-finops-plain-english.html" class="btn btn-outline-primary btn-sm"><i class="bi bi-arrow-left" aria-hidden="true"></i> Part 3</a>
              <a href="finops-greenops-5-smarter-lighter.html" class="btn btn-primary btn-sm ms-2">Continue to Part 5 <i class="bi bi-arrow-right" aria-hidden="true"></i></a></p>""",
    },
    {
        "file": "finops-greenops-5-smarter-lighter.html",
        "title_page": "FinOps and GreenOps Together — A Cloud Architect's View — Babulal Tamang",
        "meta": "Part 5 (cloud architect): align FinOps and GreenOps in landing zones, architecture reviews, Well-Architected trade-offs, tagging, and platform guardrails—one waste, two ledgers.",
        "crumb": "FinOps + GreenOps (5/5)",
        "part": 5,
        "category": "Sustainability series · Cloud architect",
        "h1": "Designing for Both Ledgers: When FinOps and GreenOps Belong in Architecture",
        "lead": "As a cloud architect, I do not treat FinOps and GreenOps as side projects for finance or sustainability teams. They are design constraints—like security and reliability—that show up in every reference diagram, landing zone policy, and production review. Waste in the cloud always hits two ledgers: the invoice and the planet.",
        "short": "The series closes from an architect's chair: shared visibility, guardrails in the platform, explicit trade-offs in reviews, and patterns that shrink spend and carbon at the same time.",
        "body": """
              <h2 class="h4 mt-4">Where this series lands for architects</h2>
              <p>Parts <a href="finops-greenops-1-invisible-bill.html">1</a> and <a href="finops-greenops-2-conservation-matters.html">2</a> explained why digital systems have a physical cost. <a href="finops-greenops-3-finops-plain-english.html">Part 3</a> made cloud money visible and accountable. <a href="finops-greenops-4-greenops-plain-english.html">Part 4</a> framed GreenOps as ongoing operational care for the environment. This closing post is written for people who <strong>draw the boxes and arrows</strong>: solution and cloud architects, platform engineers, and tech leads who sign off on what gets built.</p>
              <p>If you have read my notes on <a href="aws-cloud-architecting.html">cloud architecting</a> or <a href="cloud-platform-evolution.html">cloud platform evolution</a>, treat FinOps and GreenOps as two more pillars you balance in every design—not slogans on a slide deck.</p>

              <h2 class="h4 mt-5">One waste, two ledgers</h2>
              <p>Architects see waste as a pattern, not a surprise line item. The same anti-patterns show up on FinOps dashboards and carbon estimates:</p>
              <div class="table-responsive">
                <table class="table table-sm table-bordered align-middle">
                  <thead class="table-light">
                    <tr><th scope="col">What you designed (or inherited)</th><th scope="col">FinOps signal</th><th scope="col">GreenOps signal</th></tr>
                  </thead>
                  <tbody>
                    <tr><td>Always-on dev/test clusters</td><td>Flat spend on nights and weekends</td><td>Compute drawing power with no business value</td></tr>
                    <tr><td>Oversized instances “for headroom”</td><td>Low CPU/memory utilization</td><td>Higher embodied energy per useful transaction</td></tr>
                    <tr><td>Unattached or oversized EBS volumes</td><td>Storage cost with no attached workload</td><td>Disk manufacturing and datacenter footprint for nothing</td></tr>
                    <tr><td>Chatty cross-AZ or cross-region traffic</td><td>Data transfer line items</td><td>Extra network gear and energy per request</td></tr>
                    <tr><td>Always-hot GPU pools for occasional training</td><td>Expensive idle accelerators</td><td>High power density sitting unused</td></tr>
                  </tbody>
                </table>
              </div>
              <p>Fixing these once improves both ledgers. That is why mature organizations put cost and sustainability questions in the <strong>same architecture review</strong>, not in separate meetings that never see the diagram.</p>

              <h2 class="h4 mt-5">Well-Architected thinking: cost and sustainability together</h2>
              <p>On AWS, the <strong>Cost Optimization</strong> pillar and the <strong>Sustainability</strong> pillar are explicit companions. Other clouds express similar ideas (cost management, carbon tools, region selection guidance). As an architect, I map decisions to both:</p>
              <ul>
                <li><strong>Right-sizing and autoscaling</strong> — pay for what you use; run fewer watts per user.</li>
                <li><strong>Managed services over self-operated fleets</strong> — shift operational overhead to the provider; often better utilization at hyperscale.</li>
                <li><strong>Region and Availability Zone strategy</strong> — latency, compliance, electricity mix, and data residency in one conversation.</li>
                <li><strong>Storage lifecycle and tiering</strong> — cheaper tiers and less replicated bits when access patterns allow.</li>
                <li><strong>Efficient software</strong> — smaller containers, fewer round trips, batch where real time is not required (GreenOps cares about code; FinOps sees the bill move).</li>
              </ul>
              <p>Sustainability is not “use less cloud.” It is <strong>more outcome per unit of resource</strong>—the same mindset as performance engineering.</p>

              <h2 class="h4 mt-5">Foundation architects must get right first</h2>
              <p>Without visibility, every optimization is guesswork. Before debating instance types, establish:</p>
              <ol>
                <li><strong>Tagging and allocation dimensions</strong> — <code>Environment</code>, <code>Application</code>, <code>Owner</code>, <code>CostCenter</code> (and optional <code>CarbonTier</code> or workload class). Enforce in landing zones; reject untagged creates where policy allows.</li>
                <li><strong>Multi-account structure</strong> — separate prod from sandbox so experiments do not pollute production spend—or production SLOs.</li>
                <li><strong>Curated data</strong> — Cost and Usage Reports (or equivalent), budgets, anomaly detection; pair with provider carbon dashboards or third-party estimates until you have an internal model.</li>
                <li><strong>Golden paths</strong> — platform templates (Terraform modules, <a href="gitops-principles.html">GitOps</a> repos, <a href="kubernetes-hands-on-4-day-one-practices.html">sensible Kubernetes defaults</a>) that already include right-sized SKUs, autoscaling, and shutdown hooks for non-prod.</li>
              </ol>
              <p>Architects who skip this foundation end up arguing about pennies in one service while orphaned resources in another account dominate the bill.</p>

              <h2 class="h4 mt-5">Patterns I put in reference architectures</h2>
              <ul>
                <li><strong>Schedule non-prod</strong> — stop or scale to zero nights and weekends; document exceptions for long-running tests.</li>
                <li><strong>Spot and preemptible for fault-tolerant batch</strong> — cheaper money; better utilization of existing datacenter capacity.</li>
                <li><strong>Horizontal scale over vertical brute force</strong> — smaller nodes often map to finer-grained scaling and less stranded capacity.</li>
                <li><strong>Caching and CDN at the edge</strong> — fewer origin round trips; lower transfer cost and less core compute.</li>
                <li><strong>Async and queue-based peaks</strong> — absorb spikes without permanently provisioning for the worst minute of the year.</li>
                <li><strong>Data proximity</strong> — keep analytics close to storage when regulations allow; avoid shipping terabytes “just because.”</li>
                <li><strong>Carbon-aware batch windows</strong> — where SLAs permit, run heavy jobs when grid carbon intensity is lower (provider tools and open datasets are improving; design hooks now).</li>
              </ul>

              <h2 class="h4 mt-5">When pillars conflict — document the trade-off</h2>
              <p>Good architecture is explicit about what you sacrifice. Examples I raise in reviews:</p>
              <ul>
                <li><strong>Reserved capacity / savings plans</strong> — lower unit cost, risk of stranded commitment if workload shrinks.</li>
                <li><strong>Multi-AZ for availability</strong> — more resources running; justified for prod, often wasteful for disposable sandboxes.</li>
                <li><strong>Cross-region DR</strong> — resilience and compliance vs duplicate spend and replication energy.</li>
                <li><strong>Low-latency global active-active</strong> — user experience vs always-on footprint everywhere.</li>
                <li><strong>Always-on ML inference</strong> — SLO for real-time vs batch or scale-to-zero where latency allows.</li>
              </ul>
              <p>Write one line in the ADR: <em>“We accept higher cost/carbon here because …”</em> Leaders and auditors trust architects who name trade-offs instead of hiding them in footnotes.</p>

              <h2 class="h4 mt-5">Operating model: architecture review board with two extra questions</h2>
              <p>Keep the ritual lightweight. In addition to security, reliability, and operability, every significant design answers:</p>
              <ol>
                <li><strong>Who pays for this at steady state?</strong> (FinOps — owner, budget, forecast)</li>
                <li><strong>What is the main resource this design consumes?</strong> (GreenOps — compute hours, storage TB, egress, GPU)</li>
              </ol>
              <p>Monthly, platform and finance partners review top tag violators, top spenders, and one optimization shipped. Architects bring the next candidate from production metrics—not from a generic checklist.</p>

              <h2 class="h4 mt-5">A 90-day architect playbook</h2>
              <div class="table-responsive">
                <table class="table table-sm table-bordered align-middle">
                  <thead class="table-light">
                    <tr><th scope="col">Phase</th><th scope="col">Focus</th><th scope="col">Outcome</th></tr>
                  </thead>
                  <tbody>
                    <tr><td>Days 1–30</td><td>Tagging enforcement, top-10 idle resources, non-prod schedules</td><td>Shared dashboard; quick wins on invoice</td></tr>
                    <tr><td>Days 31–60</td><td>Golden paths updated; ARB checklist live; rightsizing on top services</td><td>New builds default to efficient patterns</td></tr>
                    <tr><td>Days 61–90</td><td>Carbon view paired with cost; one region or tier optimization pilot</td><td>Joint FinOps/GreenOps story for leadership</td></tr>
                  </tbody>
                </table>
              </div>

              <h2 class="h4 mt-5">For everyone else in the room</h2>
              <p>FinOps and GreenOps still matter outside architecture. Product owners choose features that drive load; finance sets guardrails; sustainability partners keep reporting honest. Architects connect those voices to <strong>concrete diagrams</strong>—what to scale, what to delete, what to defer.</p>
              <p>Share <a href="finops-greenops-1-invisible-bill.html">Part 1</a> with skeptics who think the cloud is weightless. Share <a href="finops-greenops-3-finops-plain-english.html">Part 3</a> with finance and <a href="finops-greenops-4-greenops-plain-english.html">Part 4</a> with ops leads. This part is for the person holding the pen on the next reference architecture.</p>

              <h2 class="h4 mt-5">Closing the series</h2>
              <p>Abundance in the cloud is not infinity. As architects, we shape what gets provisioned before the first deploy button is pressed. Aligning FinOps and GreenOps is not moral decoration—it is <strong>professional craft</strong>: the same discipline that makes systems secure and reliable, applied to money and matter.</p>
              <p>Pick one metric this month—untagged spend, idle non-prod, or estimated kgCO₂e for a top service—and ship one design change that moves it. That is how architecture culture changes.</p>

              <p class="small text-muted mt-4 mb-2"><a href="finops-greenops-4-greenops-plain-english.html">← Part 4</a> · <a href="../index.html#blog">Blog index</a> · <a href="aws-cloud-architecting.html">Cloud architecting</a> · <a href="finops-greenops-1-invisible-bill.html">Start over at Part 1</a></p>
              <p class="mb-0"><a href="finops-greenops-4-greenops-plain-english.html" class="btn btn-outline-primary btn-sm"><i class="bi bi-arrow-left" aria-hidden="true"></i> Part 4</a>
              <a href="finops-greenops-1-invisible-bill.html" class="btn btn-primary btn-sm ms-2">Back to Part 1 <i class="bi bi-arrow-repeat" aria-hidden="true"></i></a></p>""",
    },
]

if __name__ == "__main__":
    for p in POSTS:
        upsert_post(p, build_article(p))
        print("content", p["file"])
    build_blogs()
    print("built", len(POSTS), "posts")
