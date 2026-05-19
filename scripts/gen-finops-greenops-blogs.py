#!/usr/bin/env python3
"""Generate FinOps/GreenOps series blog posts 3–5 from gitops shell."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BLOGS = ROOT / "blogs"

shell = (BLOGS / "gitops-principles.html").read_text()
head_tpl = re.search(
    r"(<!DOCTYPE.*?<main id=\"main\">\s*<section class=\"breadcrumbs\">.*?</section>)",
    shell,
    re.S,
).group(1)
foot_tpl = re.search(r"(<footer id=\"footer\">.*?</html>)", shell, re.S).group(1)

NAV = [
    ("Technology’s real-world footprint", "finops-greenops-1-invisible-bill.html"),
    ("Why conservation and sustainability matter", "finops-greenops-2-conservation-matters.html"),
    ("FinOps in plain English", "finops-greenops-3-finops-plain-english.html"),
    ("GreenOps in plain English", "finops-greenops-4-greenops-plain-english.html"),
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


def build(p: dict) -> str:
    head = head_tpl.replace(
        "Git as the Control Plane — GitOps Principles — Babulal Tamang", p["title_page"]
    )
    head = re.sub(
        r'<meta content="[^"]*" name="description">',
        f'<meta content="{p["meta"]}" name="description">',
        head,
    )
    head = head.replace("<li>GitOps principles</li>", f"<li>{p['crumb']}</li>")
    article = f"""    <article class="inner-page blog-article pb-5">
      <div class="container">
        <motion.div class="row justify-content-center">
          <div class="col-lg-9 col-xl-8">
            <header class="mb-4 pb-3 border-bottom" data-aos="fade-up">
              <p class="text-muted small mb-2">{p['category']} · Part {p['part']} of 5 · <time datetime="2026-05-19">19 May 2026</time></p>
              <h1 class="h2 mb-3">{p['h1']}</h1>
              <p class="lead mb-3">{p['lead']}</p>
              <div class="border-start border-primary border-4 ps-3 py-3 bg-light rounded mb-0" role="note">
                <p class="small text-uppercase text-muted mb-1 fw-semibold">In short</p>
                <p class="mb-0">{p['short']}</p>
              </motion.div>
            </header>
            <div class="blog-prose" data-aos="fade-up" data-aos-delay="50">
              {series_nav(p['part'])}
{p['body']}
            </motion.div>
          </motion.div>
        </motion.div>
      </motion.div>
    </article>"""
    return (head + "\n" + article + "\n  </main>\n  " + foot_tpl).replace("motion.div", "div")


POSTS = [
    {
        "file": "finops-greenops-3-finops-plain-english.html",
        "title_page": "FinOps in Plain English: Making Cloud Spend Visible — Babulal Tamang",
        "meta": "Part 3: FinOps explained for everyone—why cloud bills surprise teams, what FinOps practices do, and how financial accountability helps organizations without blocking innovation.",
        "crumb": "FinOps (3/5)",
        "part": 3,
        "category": "FinOps",
        "h1": "FinOps in Plain English: Stop Guessing What the Cloud Costs",
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
        "title_page": "GreenOps in Plain English: Technology That Respects the Planet — Babulal Tamang",
        "meta": "Part 4: GreenOps explained for everyone—how teams reduce the environmental impact of running software, from cleaner energy and efficient code to measuring carbon and avoiding greenwashing.",
        "crumb": "GreenOps (4/5)",
        "part": 4,
        "category": "GreenOps",
        "h1": "GreenOps in Plain English: Running Technology With a Lighter Footprint",
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
        "title_page": "Smarter Spending, Lighter Footprint: FinOps and GreenOps Together — Babulal Tamang",
        "meta": "Part 5: how FinOps and GreenOps reinforce each other—save money and energy, build a responsible technology culture, and practical next steps for teams and readers.",
        "crumb": "FinOps + GreenOps (5/5)",
        "part": 5,
        "category": "Sustainability series",
        "h1": "Smarter Spending, Lighter Footprint: When FinOps and GreenOps Work as One",
        "lead": "FinOps and GreenOps are not rival initiatives fighting for budget. They are two lenses on the same truth: waste in the cloud hurts wallets and warms the planet. Organizations that align them move faster with less regret.",
        "short": "The series closes with a simple partnership—financial discipline plus environmental care—so technology serves people today without borrowing from tomorrow.",
        "body": """
              <h2 class="h4 mt-4">Series recap in one paragraph</h2>
              <p>We live in a digital world that still runs on physical resources (<a href="finops-greenops-1-invisible-bill.html">Part 1</a>). Conservation and sustainability explain why careful use matters for everyone (<a href="finops-greenops-2-conservation-matters.html">Part 2</a>). <a href="finops-greenops-3-finops-plain-english.html">FinOps</a> makes cloud money visible and accountable. <a href="finops-greenops-4-greenops-plain-english.html">GreenOps</a> reduces the environmental impact of running systems. This final post shows how they fit together in real organizations—and what you can do next.</p>

              <h2 class="h4 mt-5">The overlap: same waste, two bills</h2>
              <p>An oversized server cluster that nobody uses shows up as:</p>
              <ul>
                <li>A line item on the <strong>cloud invoice</strong> (FinOps pain)</li>
                <li>Unnecessary <strong>electricity and cooling</strong> in a data center (GreenOps pain)</li>
              </ul>
              <p>Fixing it once helps both. That is why the most successful programs do not silo “cost team” vs “sustainability team” on opposite sides of the building. They share dashboards, share wins, and share language leaders understand: <strong>efficiency is strategy</strong>.</p>

              <h2 class="h4 mt-5">When goals seem to conflict</h2>
              <p>Not every decision is win-win. Examples:</p>
              <ul>
                <li><strong>Reserved capacity</strong> can save money but lock you into resources you later do not need—plan carefully.</li>
                <li><strong>Always-on reliability</strong> for life-critical systems may cost more energy—and that trade-off is acceptable if stated clearly.</li>
                <li><strong>Moving data</strong> to a greener region can save carbon but add latency or compliance work.</li>
              </ul>
              <p>Good governance makes trade-offs explicit: “We accept higher cost here for safety” or “We accept slightly slower batch jobs to run on cleaner power overnight.”</p>

              <h2 class="h4 mt-5">A simple operating model for teams</h2>
              <ol>
                <li><strong>See:</strong> Tag cloud resources; track top spenders and estimated emissions.</li>
                <li><strong>Prioritize:</strong> Fix idle waste first—quick money and carbon savings.</li>
                <li><strong>Design:</strong> Bake cost and carbon questions into architecture reviews.</li>
                <li><strong>Learn:</strong> Monthly 30-minute review with engineering, finance, and sustainability champions.</li>
                <li><strong>Tell the truth:</strong> Report progress with numbers, including setbacks.</li>
              </ol>

              <h2 class="h4 mt-5">For readers outside IT</h2>
              <ul>
                <li>Ask employers and vendors what they measure—not only what they promise.</li>
                <li>Prefer services that are fast and purposeful over bloated experiences that drain battery and data.</li>
                <li>Support education and policy that treats digital infrastructure as part of national infrastructure—like roads and power lines.</li>
              </ul>

              <h2 class="h4 mt-5">For engineers and platform teams</h2>
              <ul>
                <li>Pair FinOps dashboards with a simple carbon or energy view—even if approximate at first.</li>
                <li>Document “paved roads” that default to efficient sizes, autoscaling, and shutdown schedules.</li>
                <li>Link to <a href="cloud-platform-evolution.html">cloud platform evolution</a> and <a href="devops-life-business-value.html">DevOps business value</a> essays for cultural context.</li>
              </ul>

              <h2 class="h4 mt-5">Why this series exists</h2>
              <p>Technology will keep advancing. So will climate and resource pressures. We do not need fear; we need <strong>clear habits</strong> at human scale and organizational scale. FinOps and GreenOps are two names for discipline in a world of abundance—reminding us that abundance is not infinity.</p>
              <p>Thank you for reading all five parts. Share Part 1 with someone who thinks the cloud has no footprint. Share Part 3 with a finance partner and Part 4 with an ops lead. Start one visible metric this month—that is how cultures change.</p>

              <p class="small text-muted mt-4 mb-2"><a href="finops-greenops-4-greenops-plain-english.html">← Part 4</a> · <a href="../index.html#blog">Blog index</a> · <a href="finops-greenops-1-invisible-bill.html">Start over at Part 1</a></p>
              <p class="mb-0"><a href="finops-greenops-4-greenops-plain-english.html" class="btn btn-outline-primary btn-sm"><i class="bi bi-arrow-left" aria-hidden="true"></i> Part 4</a>
              <a href="finops-greenops-1-invisible-bill.html" class="btn btn-primary btn-sm ms-2">Back to Part 1 <i class="bi bi-arrow-repeat" aria-hidden="true"></i></a></p>""",
    },
]

for p in POSTS:
    out = BLOGS / p["file"]
    out.write_text(build(p))
    print("wrote", out.name)
