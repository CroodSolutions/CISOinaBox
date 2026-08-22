# Attack Surface Management

## Introduction: Seeing Your Organization the Way an Attacker Does

Effective cybersecurity starts with a shift in perspective: before you can defend your organization, you have to see it the way an attacker sees it from the outside in: no credentials, no internal access, no map. Your **attack surface** is the sum of everything about your organization that is discoverable, reachable, or exploitable from the open internet. It includes your internet-facing servers and applications, your domains and certificates, your cloud storage, your employees' exposed credentials, the lookalike domains someone else registered to impersonate you, and the forgotten test server a developer stood up last quarter and never tore down.

**Attack Surface Management (ASM) is the ongoing practice of discovering, cataloging, prioritizing, and reducing that exposure, continuously, before an attacker finds it first.** Note the word *ongoing*. A lot of teams treat this as a one-time mapping exercise: run a scan, get a report, file it. That is where most programs fail. Your attack surface changes every single day. Every new cloud instance, every marketing microsite, every acquired subsidiary, every credential dumped in a breach adds to it. A snapshot from last quarter is already wrong. This is a program, not a project.

Here is the uncomfortable part. Most security programs are built inside-out. You start with endpoint protection, internal vulnerability scanning, identity and access management, patch management. All of it necessary, all of it valuable. But none of it tells you what an attacker sees *before they even knock on the door*. The exposures ASM catches (leaked credentials, an exposed dev server, a lookalike domain, an expiring certificate on a forgotten subdomain) happen entirely outside your network. None of them require a compromise. None of them trip your SIEM. None of them show up on a quarterly pen test. You cannot firewall your way out of these risks, because they exist on infrastructure and in databases you do not control. You have to *see* them first.

For a new CISO, this is also increasingly not just a technical problem. It is a board-level, insurance, and regulatory conversation. Cyber insurance carriers now run their own external scans and price your premium on what they find. Breach notification laws and regulators care about exposed customer data regardless of where it sat. M&A due diligence routinely includes an external exposure assessment. When your CEO or your board asks "how exposed are we, really?", ASM is the discipline that lets you answer with something better than a shrug.

**One clarification before we go further, because these three things get conflated constantly:**

- **Vulnerability Management** (covered in its own chapter) is about the known weaknesses *inside* your environment, the CVEs on systems you already know you own. It answers "what's broken on my assets?"
- **Attack Surface Management** is about discovering what's exposed to the internet in the first place, *including assets you didn't know you had*. It answers "what can an attacker even see and reach?"
- **Security Ratings services** (SecurityScorecard, BitSight, and similar) grade organizations from the outside using a limited set of observable signals. They are built primarily so *other people* can assess *your* risk, specifically vendor and third-party risk management. They are not comprehensive discovery-and-remediation tools for your own exposure, and treating a good rating as "we've done ASM" is a common and costly mistake.

The goal of this chapter is simple: by the end, you should understand what ASM is, be able to scope a program appropriate to your organization's size and risk, know how to cut through the noise that sinks most programs, and be able to start building (or buying) the capability the next day.

---

## What This Looks Like in Practice

Concepts are easy to nod along to. What makes ASM real is seeing how these exposures actually happen, to competent teams, with good intentions, following (or almost following) reasonable processes. The following are composite, anonymized scenarios drawn from real situations. Each one is the kind of thing continuous external monitoring catches before it becomes a headline. As you read them, notice how often the failure is not incompetence but simply a lack of *visibility* into something outside the normal field of view.

### The Migration Window

An organization was migrating its email system from on-premises to the cloud. During the cutover (a routine, well-planned migration), a misconfiguration briefly exposed the email server directly to the internet. Not for long. But within five minutes, automated internet-wide scanners had already found it and started probing. The team caught it and had enough data to pull it back offline within ten minutes.

**Why it matters:** The window between "something got exposed" and "someone is probing it" is measured in minutes, not days. Services like Shodan, Censys, and BinaryEdge continuously re-scan the entire internet address space. "We're careful during cutovers, and we have a firewall" is not a defense against a five-minute exposure that a bot finds in three. You need something watching the same things the attackers are watching, at the same speed.

### The Server Nobody Meant to Stand Up

A development team had a documented, safe playbook for standing up new test infrastructure. One developer, under deadline pressure, skipped it. The server they created was publicly internet-facing, ran insecure default configurations, , and worst of all, was connected back to internal directory services. It exposed directory information, internal email structure, and organizational data to anyone who found it. It was discovered by accident, during an unrelated security engagement. It could have sat there exposed for months.

**Why it matters:** Shadow IT and unauthorized infrastructure are created constantly, by well-meaning people in every department, in the gap between "we have a process" and "everyone follows it every time." A program that only scans assets you already know about misses the entire point. The whole value of ASM is discovering what you *don't* know you have.

### The Deadline No One Knew About

An organization had outsourced its main marketing website to a third-party agency, a completely normal arrangement. During an unrelated security engagement, the team discovered that a vulnerability researcher had already reported a serious flaw in that site directly to the agency, and had attached a 90-day public-disclosure deadline. Only 10 days were left on that clock. IT didn't know. Marketing didn't know. Security didn't know. The countdown was running and nobody inside the organization was aware it existed.

**Why it matters:** Your brand appears on infrastructure you don't control: vendor-hosted sites, portals, integrations. In the eyes of a customer, a regulator, or an attacker, all of it is still *you*. "That site is managed externally, so it's not our risk" is exactly the assumption that leaves you 10 days from a public disclosure you didn't know about. (This is also a strong argument for a formal Vulnerability Disclosure Program, more on that later.)

### The Portal That Wasn't Theirs

A healthcare organization discovered, well after the fact, that a third party had stood up a lookalike website offering "appointment scheduling" for their providers. It looked legitimate. It collected patient information. It was actively trying to push that data into the real organization's intake API. And because it lacked proper privacy notices, it exposed the *real* organization to legal threats over a site they had never built and did not control. They didn't create it. They still had to deal with the lawyers, the regulators, and the confused, angry patients.

**Why it matters:** "Who would bother impersonating us?" is one of the most expensive assumptions in security. Lookalike domains and brand impersonation are not just reputational nuisances. They create real legal, regulatory, and operational damage, and in regulated industries the liability can land on you even when the fraud isn't yours. Detecting them early is the only real defense.

### The Password That Never Left

Websites get crawled and archived constantly by the Internet Archive's Wayback Machine, by search engine caches, by dozens of other indexers. Developers occasionally commit code or content that includes credentials, API keys, or internal URLs. Even after that content is removed from the live site, the *archived* copy stays public, often for years, unless someone finds it and formally requests removal. A scan that only looks at "what is on your site right now" misses this entirely.

**Why it matters:** The internet has a long memory. Removing something from your live site does not remove it from the archives. "We take sensitive content down quickly when we find it" is necessary but not sufficient. You also have to check what's already been captured and preserved, and coordinate its removal.

### The Exposure You Hear About From Underwriting

Cyber insurance carriers are increasingly running their own external scans (or hiring pen testers) and using the results to set premiums, deny claims, or decline coverage entirely. More than a few organizations first learn about a critical external exposure from their *insurance renewal questionnaire*, not from their own security team.

**Why it matters:** If an insurance underwriter can find it, an attacker can find it, and so can you. "Our premium is already high, so we must be in decent shape" gets the logic backwards. Better to find and fix your exposure before the carrier does, so you can walk into the renewal with a clean profile and negotiate from strength, instead of explaining a finding you didn't know about.

### The Certificate Nobody Owns

Most organizations believe they have one clean, managed process for TLS/SSL certificates on their primary domain. In practice, certificates accumulate everywhere else: legacy applications with self-signed certs, subdomains a vendor registered for an integration, a microsite marketing launched and forgot, an internal tool that was briefly made external for a project and never torn back down. Certificate management is already hard. Certificate management across infrastructure nobody remembers exists is impossible without external discovery.

**Why it matters:** An expired certificate on a forgotten subdomain erodes customer trust the instant someone lands on it, breaks integrations silently, and signals a deeper asset-inventory problem to any auditor who goes looking. You cannot manage what is not in your inventory, and ASM is how that inventory gets built and maintained, continuously, from the outside in.

### Attack Paths: From Foothold to Crown Jewels

There is one more idea that ties all of these together, and it is the one most new programs overlook. Finding individual exposures is necessary but not sufficient. Modern attackers rarely rely on a single exploit. They **chain** weaknesses together into an *attack path* that leads from an initial foothold toward your most sensitive systems, the "crown jewels."

Think about "The Server Nobody Meant to Stand Up" from earlier. On its own, an exposed dev server sounds like a medium-severity finding. But trace the path: the server is internet-facing (foothold), it runs default credentials (access), and it is connected back to internal directory services (pivot). Now that "medium" finding is a direct route from the public internet to your identity infrastructure. The individual weaknesses were unremarkable. The *path* they formed was critical.

This is why prioritization has to think in paths, not just points. When you evaluate a finding, ask the attacker's question: "If I get in here, where can I go next?" A minor exposure that opens onto a route toward customer data or admin credentials outranks a scary-sounding vulnerability that dead-ends into nothing. Mapping these paths in advance lets you break the chain at its weakest link, and often lets you neutralize a high-value path by fixing one cheap, unglamorous thing in the middle of it.

---

## What You're Actually Monitoring

ASM covers a lot of ground, because attackers don't respect categorical boundaries. A leaked credential on a code repository can lead to a cloud account takeover; a lookalike domain can seed a phishing campaign against your customers. Here is the full landscape of what a mature external attack surface program watches. **Do not read this as a day-one to-do list.** No small or mid-size team should try to cover all of it at once. The next section gives you a concrete way to decide what's in scope for *your* organization. For now, understand the terrain:

- **External infrastructure & DNS:** your domains, subdomains, IP ranges and ASNs, cloud services, and forgotten or legacy assets. This is the foundation; almost everything else hangs off knowing what's actually yours.
- **Exposed services & misconfigurations:** open ports and protocols (SSH, RDP, FTP, SMTP, exposed databases), missing security headers, weak or expired TLS, and DNS hygiene issues.
- **Cloud storage exposure:** publicly readable S3 buckets, Azure Blob containers, Google Cloud Storage, and similar. A single misconfigured bucket is one of the most common causes of large data exposure.
- **Leaked credentials & secrets:** employee credentials in breach databases, infostealer logs, and paste sites; API keys and secrets committed to public code repositories.
- **Shadow IT & shadow AI:** unsanctioned SaaS integrations, unregistered subdomains, forgotten dev environments, and increasingly, unmanaged AI/ML endpoints and integrations that expose data or model access.
- **Brand & impersonation exposure:** lookalike and typosquatted domains, phishing infrastructure prepared against you, and social media impersonation.
- **Human & social attack surface:** the OSINT footprint of your employees (names, titles, emails harvestable from LinkedIn and corporate sites) that fuels targeted phishing and social engineering.
- **Dark web & underground exposure:** mentions of your brand on ransomware leak sites, underground forums, and Tor-based marketplaces.
- **Historical & archived exposure:** sensitive content preserved in the Wayback Machine and search caches long after it left your live site.
- **Third-party, subsidiary & supply-chain footprint:** the external exposure of acquired entities, vendor-hosted properties, and the broader corporate structure attached to your name.
- **Attack paths:** the analysis layer that ties the above together, mapping how individual findings chain toward high-value assets.

A first full scan across even a subset of these categories routinely produces *tens of thousands* of data points. That volume is exactly why scoping and triage (covered in the next two sections) are the difference between a program people trust and a report people ignore.

---

## Scoping: Where to Actually Start

The eleven categories above are the whole map. Trying to cover the whole map on day one is the single most common way a new ASM program stalls before it delivers anything. **Most organizations struggle here because they conflate "comprehensive" with "mature."** A shallow program that reliably covers the handful of things that matter most beats an ambitious program that covers three categories deeply and quietly ignores the rest.

Start by deciding what is genuinely in scope for your organization's size and risk profile. The matrix below is your starting point. Read the tiers as: **Must-have** (start here, get it running before anything else), **Should-have** (add once must-haves are on a real cadence), **Nice-to-have** (valuable, not urgent), and **Skip for now** (real capability, but wait until you've matured the basics).

| Attack Surface Category | Small (<500) | Medium (500–5,000) | Large (>5,000) |
|---|---|---|---|
| External infrastructure & DNS | Must-have | Must-have | Must-have |
| Exposed services & misconfigurations | Must-have | Must-have | Must-have |
| Leaked credentials & secrets | Must-have | Must-have | Must-have |
| Cloud storage exposure | Should-have | Must-have | Must-have |
| Shadow IT & shadow AI | Should-have | Must-have | Must-have |
| Brand & impersonation exposure | Nice-to-have\* | Should-have\* | Must-have |
| Human & social attack surface | Nice-to-have | Should-have | Must-have |
| Third-party, subsidiary & supply-chain | Skip for now\*\* | Should-have\*\* | Must-have |
| Dark web & underground exposure | Skip for now | Nice-to-have | Should-have |
| Historical & archived exposure | Skip for now | Nice-to-have | Should-have |
| Attack path / chaining analysis | Skip for now | Nice-to-have | Should-have |

**\* Regulatory override:** If you're in healthcare, financial services, or critical infrastructure, bump **Brand & Impersonation** up one full tier regardless of size. HIPAA, GLBA, and similar regimes raise the legal and regulatory stakes on impersonation specifically. The "Portal That Wasn't Theirs" scenario earlier is a direct example of an org facing legal exposure over a site it didn't even build.

**\*\* M&A override:** If your organization is actively acquiring or divesting, treat **Third-Party & Subsidiary footprint** as Must-have regardless of size. When you acquire a company, you instantly inherit its entire external attack surface, often before it's integrated into anything you monitor. When you divest, orphaned assets need to be decommissioned, not forgotten. Inherited and orphaned exposure does not wait for next year's budget cycle.

**How to use this table, prescriptively:**

1. **Get everything marked Must-have running on a real, repeating cadence before you touch a single Should-have item.** Breadth matters up to the Must-have line; past it, depth beats breadth every time.
2. **Re-run this scoping exercise at least annually**, and immediately after any material change: an acquisition or divestiture, a new regulatory obligation, crossing a headcount threshold, or a board or insurance conversation that surfaced a gap you weren't tracking.
3. **Write your scope down.** The scoping worksheet in the Templates section turns the tier you land on into a concrete list of domains, IP ranges, subsidiaries, cloud accounts, and brand terms. That written scope is the input to everything that follows.

---

## How to Implement: Step by Step

With scope decided, this is the operating loop. This is model-agnostic; it works whether you build the capability in-house with open-source tools, buy a commercial platform, or engage a managed service. The steps don't change; only who executes them does.

**Step 1: Scope it.** Use the matrix above to decide which categories are in play, then translate that into a concrete inventory of what you're monitoring: primary domains, known subdomains, IP ranges, cloud accounts, subsidiaries, and brand/keyword terms. Fill out the Attack Surface Scoping Worksheet (Templates). This is the ground truth everything else is measured against.

**Step 2: Choose your model.** Decide how you'll actually run this: build in-house, buy a platform, or engage a managed service. The decision hinges on three things: team size, in-house OSINT/recon skill, and how many FTE-hours per week you can realistically dedicate to *triaging noise* (not just running scans). The Build vs. Buy vs. Managed-Service Decision Matrix (Templates) walks through this honestly. If you're going the in-house route, the "Where to Get Help" section points you at free and low-cost ways to build the skill.

**Step 3: Run the baseline discovery scan.** Your first scan is always noisy, and that's normal. Do not treat the raw output as a finding list. Instead, budget real time to *validate the asset list*: for each discovered asset, decide whether it's yours, vendor-managed on your behalf, or unrelated (a false attribution). This validated inventory becomes your baseline. Rushing this step poisons every cycle that follows.

**Step 4: Build a triage and prioritization process.** Raw scan output is not a report; it's raw material. This is where most programs live or die, so it gets its own full section next. Structurally, map your process to the industry-standard **CTEM** model (Continuous Threat Exposure Management): *Scoping → Discovery → Prioritization → Validation → Mobilization*. You've already done Scoping (Step 1) and Discovery (Step 3); Prioritization and Validation are the triage work; Mobilization is remediation.

**Step 5: Set your cadence.** How often you scan depends on maturity and scope. Small programs might run quarterly; mature large programs run continuously. Match the cadence to how fast your attack surface actually changes and how quickly you can act on findings. Scanning weekly while only reviewing quarterly just builds a backlog. The Maturity Model section gives concrete starting points.

**Step 6: Build the executive communication loop.** Findings that never reach a decision-maker don't reduce risk. Following the handbook's **Crayons Framework** (if it can't be understood in under 30 seconds, simplify it), build a standing executive artifact: a letter grade or simple risk score, a trend line (are we improving, holding, or slipping?), the top handful of findings, and, critically, the *decision needed*. A board slide that says "six months ago we were a D, we're now a B, here's how" is worth more than a 40-page scan export. The Executive Readout One-Pager (Templates) is built for exactly this.

**Step 7: Integrate with remediation tracking.** Every finding that survives triage needs three things: an *owner*, a *ticket* in your system of record, and a *closed-loop status* (open → ticketed → closed). Push findings into your existing ITSM or GRC platform rather than tracking them in a side spreadsheet nobody looks at. If findings can't be tracked to closure, you don't have a program; you have a recurring report.

**Step 8: Re-baseline every cycle.** Your attack surface changed while you were remediating the last batch. Each cycle, re-run discovery, fold new assets into the inventory, confirm whether prior findings actually got fixed, and update the trend line. ASM is a loop, not a line.

---

## Cutting the Noise: The Triage Process That Makes or Breaks the Program

This is what vendor demos gloss over: **the hard part of ASM is not finding things. It's figuring out which of the tens of thousands of things you found actually matter.** A single full scan can surface tens of thousands of raw data points. If your team treats each one at face value, they will burn out, and, far worse, they will start ignoring entire categories of findings. The day your team learns to reflexively dismiss "credential exposure" alerts because the last fifty were junk is the day your program dies, quietly, right before the one alert that mattered.

Two noise sources deserve special attention because they are the ones that erode trust fastest, and both were surfaced by practitioners running real programs: **domain/brand-similarity false positives** and **stale breach-credential matches**. We'll build a general triage principle first, then a specific process for each.

### The Core Principle: Confidence Tiering, Not Binary Alerting

Stop treating findings as "alert" or "no alert." Every finding gets sorted into one of four dispositions *before* it consumes a human decision-maker's attention:

1. **Confirmed:** verified real and actionable. Escalate now.
2. **Likely:** strong signal, needs an owner's review, but it's not a fire drill.
3. **Possible / Low-Confidence:** weak signal. Batch these for periodic review; don't chase them individually.
4. **Dismissed – Documented:** investigated once, determined benign, and *logged with the reasoning and a revalidation date* so nobody re-investigates it from scratch next cycle.

That fourth disposition is the one teams skip, and skipping it is why they redo the same work every quarter. Which brings us to the single most important artifact in the whole process, but first, the two specific sub-processes.

### Sub-Process A: Domain & Brand-Similarity Validation

The problem: a discovery tool flags every domain that *looks* like yours as a potential impersonation threat. Most of them aren't. Some are coincidental (a legitimate business with a similar name), some are shared infrastructure artifacts, and some are *your own* defensive registrations. Before any "lookalike domain" gets treated as a real threat, run it through this checklist:

- **Registration check:** Who registered it, when, through which registrar, and is WHOIS privacy in use? A domain registered nine days ago behind privacy protection is a very different signal than one registered eight years ago.
- **Content check:** Does the site actually mimic your brand and collect data? Or is it parked, for sale, or hosting entirely unrelated content? A parked domain is not an active threat.
- **Infrastructure check:** Is it on shared hosting or a CDN that could cause a false "it's near your IPs" attribution? Confirm it's not just IP-neighbor noise.
- **Ownership correlation:** Could this be a coincidentally similar but legitimate business, a reseller or affiliate, or a *defensive registration your own marketing or legal team already owns*? Check internally before you escalate externally. This one check alone eliminates a large share of lookalike noise.
- **Age & behavior signal:** Recently registered + close to your brand name + WHOIS-private + content that mimics your site = high signal. Years old + no complaint history + unrelated content = low priority.
- **DNS & redirect check:** Look at MX records (is it set up to send mail?), the TLS cert issuer, and whether it redirects toward your real domain (a strong red flag for a phishing setup) or has no relationship to you at all.

**Disposition:** A confirmed impersonation escalates immediately into your takedown/legal workflow. Anything coincidental or legitimate gets logged *once* in the suppression list with the reasoning, and does not get re-flagged every cycle unless its behavior changes (new content appears, it starts redirecting to you, a takeover is attempted).

### Sub-Process B: Breach & Credential Exposure Aging

This is the one practitioners flag most often: a breach-database match from *ten years ago* gets reported with the same visual weight as one from last week. Chase enough decade-old hits that turn out to be irrelevant and your team learns to ignore the entire "leaked credentials" category. That is the worst possible outcome, because a genuinely fresh credential leak is one of the highest-value findings ASM produces.

The trap to avoid: age alone is *not* a sufficient filter. A reused password on a still-active account with no MFA is a real risk no matter how old the breach is. So the process checks age **and** current relevance together:

1. **Pull the breach date** for every credential match. This is your starting filter, not your final answer.
2. **Apply tiered urgency by age:**
   - **Under 12 months:** High priority. Verify the account and force a reset if there's any doubt.
   - **1–3 years:** Medium priority. Confirm the account is still active, and check whether your password-rotation policy would already have cycled it. (If you enforce 90-day rotation, a two-year-old password is almost certainly no longer valid. Verify, don't chase.)
   - **3+ years:** Low priority. Focus on verifying account status and MFA enforcement rather than chasing the specific old password.
3. **Cross-reference identity/HR records first.** A huge share of wasted investigation time goes into breach hits for people who *left the organization years ago*. Check employment status before you do anything else. A terminated account is often a two-minute close.
4. **Check MFA enforcement on the account.** If MFA is enforced org-wide, an old leaked password's individual risk drops sharply regardless of breach age. Document MFA as the compensating control and deprioritize accordingly.
5. **Log confirmed-stale hits once**, with the specific reasoning (departed employee / MFA enforced / rotation policy confirms staleness / low-fidelity breach source), and add them to the suppression list so the same decade-old breach doesn't generate fresh work every quarter.

### The Artifact That Actually Saves the Time: A Living Suppression List

Confidence tiering and checklists only pay off if the *decision persists between cycles*. The mechanism that makes that happen is a single running table, the Suppression / Exception List. This is the artifact that prevents your team from re-investigating the same false positive four times a year:

| Finding | Type | First Seen | Disposition | Reasoning | Reviewed By | Next Revalidation |
|---|---|---|---|---|---|---|
| `secure-portal-yourbrand.com` | Lookalike domain | 2024-03 | Dismissed – Documented | Registered 2019, parked page, no brand content, no complaint history | J. Ramirez | 2026-09 (annual) |
| `yourbrand-billing.net` | Lookalike domain | 2026-02 | Confirmed | Registered 9 days prior, WHOIS-private, mirrors login page, active MX records | J. Ramirez | Closed – takedown filed |
| `j.smith@company.com` (2016 breach) | Breach credential | 2026-01 | Dismissed – Documented | Employee departed 2021; account deprovisioned | M. Chen | N/A – account terminated |
| `a.patel@company.com` (2019 combo list) | Breach credential | 2026-01 | Dismissed – Documented | Active employee; MFA enforced org-wide since 2023; rotation policy cycles password every 90 days | M. Chen | 2027-01 (annual, or sooner if MFA policy changes) |

Revisit the *suppression list itself* on a fixed cadence (quarterly is reasonable) but not to re-investigate each line. You're only confirming the exception still holds. A departed-employee suppression stays valid indefinitely. An MFA-based suppression must be reopened immediately if org-wide MFA enforcement ever lapses. That conditional revalidation is the whole point: you're not ignoring findings, you're *time-boxing* how often you look at settled ones.

### Close the Loop: Let False Positives Tune the Program

Finally, treat your dismissed findings as data. Track your **false-positive rate** as a standing metric each cycle: the percentage of raw findings your team dismisses as noise. A *declining* false-positive rate over successive cycles is one of the truest signs your program is maturing, and it's a great thing to show leadership. Feed the patterns back into your scan configuration: permanently exclude a known internal dev domain, suppress a breach source that's proven consistently low-fidelity for your environment, and tune the correlation rules that keep generating the same category of junk. In CTEM terms, this is the **Validation** stage doing its full job. Validation isn't only "is this exploitable," it's also "is this still relevant right now."

---

## Maturity Model by Organization Size

ASM is not one-size-fits-all, and you should not attempt a large-enterprise program on a small-business budget. Here's what "appropriate" looks like at each stage. These map to the CIS Controls Implementation Groups (IG1/IG2/IG3) used throughout this handbook.

**Small organization (under 500 employees), IG1 baseline.**
Start free. Enroll in **CISA's Cyber Hygiene Services** (no-cost continuous vulnerability and web-application scanning for eligible U.S. organizations; details in the next section). Layer on a manual quarterly self-review: enumerate your domains and subdomains, check your certificates and their expiry, review your social media presence for impersonation, and do some basic open-source recon on your own footprint. If budget allows, add a low-cost, SMB-tier commercial tool. Focus entirely on the Must-have categories from the scope matrix. Don't chase dark web monitoring or attack-path analysis yet. Nail the fundamentals first.

**Medium organization (500–5,000 employees), IG2 operational maturity.**
Move to a dedicated commercial EASM tool or a managed service, running on a monthly or quarterly cadence. Assign a *named owner*. Often this is a responsibility layered onto a security manager rather than a dedicated full-time hire at this stage. Build the triage process and suppression list as real, maintained artifacts, not ad-hoc effort. Start folding in Should-have categories (cloud storage, shadow IT, human/social surface) and stand up the executive reporting loop so leadership sees a trend line.

**Large organization (over 5,000 employees), IG3 advanced.**
Run an enterprise EASM platform integrated into your SOC/XDR stack, scanning continuously. Staff a dedicated function or analyst team that owns triage and remediation coordination. Actively track M&A and subsidiary attack surface as a standing concern. Do full attack-path analysis. Report trend lines to the board. At this scale, ASM is a continuous, instrumented capability feeding your broader threat-exposure program, not a periodic scan.

Wherever you're starting, **start.** A small organization running CISA's free scans and a disciplined quarterly self-review is in dramatically better shape than a large one with an expensive platform nobody triages.

---

## The Tooling Landscape

A quick, intentionally vendor-neutral tour. Specific products and pricing shift constantly, so the goal here is to understand the *categories* and how to evaluate within them, not to hand you a leaderboard that's stale in twelve months. Evaluate any option against the Tool/Vendor Evaluation Matrix in the Templates section rather than against marketing claims.

**Open-source and free tools.** You can build a genuinely capable in-house discovery pipeline from open-source components, and doing so is also the best way to *understand the mechanics* before you buy anything:

- **Amass** (an OWASP project): subdomain and asset discovery; about as close to a community standard as external recon has.
- **theHarvester:** gathers emails, names, subdomains, and hosts from public OSINT sources.
- **SpiderFoot** (open-source edition): modular OSINT automation across a wide range of data sources; several commercial platforms are built on top of engines like this.
- **The ProjectDiscovery toolkit** (subfinder, httpx, nuclei, dnsx): modern, actively maintained CLI tools for teams comfortable assembling their own pipeline.
- **Shodan and Censys:** free tiers let you run manual internet-wide search queries against your own footprint; paid tiers add API access and scale.

The trade-off with open-source is real and worth stating plainly: someone has to own the configuration, the upkeep, and, most importantly, the triage. The raw output is noisy (that's what the entire previous section was about). These tools give you capability, not a finished program. Best fit: small organizations, hands-on security teams building skill, and anyone who wants to know what a platform is doing before paying for one.

**Self-service commercial tools (SMB-friendly).** A middle tier of platforms, often with published pricing, that automate discovery and provide a workflow UI with less hand-holding than a full managed service. Good fit for teams with *some* but not full-time capacity to run their own triage.

**Enterprise commercial platforms.** The heavyweight EASM platforms differ mainly on their *discovery method*: seed-based (you give it domains, it expands outward), entity-mapping (it models your corporate structure first), or internet-wide scanning (it indexes the whole internet and attributes assets back to you). They also differ on how well they integrate with your existing security stack. These are powerful and correspondingly priced. Evaluate them on discovery method, integration fit, triage workflow, and total cost including the internal hours to operate them, not on module counts.

**Managed / white-glove services.** Here a provider runs the scanning platform, does the triage, delivers prioritized findings and an executive readout, and helps coordinate remediation. The trade-off is simple: you pay more in dollars but far less in your team's time. For an organization without spare FTE-hours to own triage, this is often the most *effective* option, but it is not automatically "better" than a well-run in-house program, and you should evaluate it on the same neutral footing as every other option in the Build vs. Buy vs. Managed-Service matrix.

**A distinction worth calling out explicitly: security ratings are not ASM.** Services like SecurityScorecard and BitSight produce an outside-in letter grade of an organization's security posture. They are useful, but their primary design purpose is *third-party and vendor risk*, letting you assess your suppliers, and letting your customers and insurers assess you. They rely on a limited set of externally observable signals; they are not built to comprehensively discover your unknown assets, dedupe and triage findings against your specific environment, or coordinate remediation. Do not mistake a good security rating for "we've done ASM." They answer different questions.

**A free starting point worth naming again.** For eligible U.S. organizations, **CISA's Cyber Hygiene Services** is a legitimate no-cost way to get continuous external vulnerability and web-application scanning. For a small organization or nonprofit, it is often the single best first move. More on how to access it next.

---

## Where to Get Help Building the Capability

One of the most common questions a new CISO has isn't "what is good" but "how do I *get* to good, and who can help me?" Unlike the commercial tooling landscape, most of what follows is free or low-cost and carries no vendor conflict, so this section names specific, practical resources.

**Government and no-cost programs.** Start with **CISA's Cyber Hygiene Services**, free continuous scanning for eligible U.S. organizations; you enroll by emailing CISA directly, and scanning typically begins within a few business days. Pair it with CISA's **Cross-Sector Cybersecurity Performance Goals (CPGs)** as a free baseline maturity checklist to measure your program against. If you're a state, local, tribal, or territorial government or a public education institution, join the **MS-ISAC** (Multi-State Information Sharing and Analysis Center), where membership is free for eligible organizations and includes its own scanning and threat-intelligence services.

**Industry-specific threat sharing (ISACs).** If your sector has an Information Sharing and Analysis Center (Health-ISAC for healthcare, FS-ISAC for financial services, REN-ISAC for higher education, and many others), joining gives you peer intelligence, benchmarking against organizations facing the same threats, and often member-only tooling or guidance. This is signal you are almost certainly not getting today, frequently at little or no cost.

**Open-source communities.** OWASP runs global and local chapters that do real project work and produce guidance far beyond the famous Top 10. The **OSINT Framework** is a maintained directory of free discovery tools organized by category and a great map when you're building an in-house pipeline. The ProjectDiscovery community is a strong place for teams that want hands-on recon skill before evaluating a commercial platform.

**Stand up a Vulnerability Disclosure Program (VDP).** This one deserves its own line, because it directly addresses "The Deadline No One Knew About" scenario from earlier. A VDP is a formal, published channel (a security.txt file and a clear policy) that tells outside researchers how to report what they find, and commits you to handling it. It effectively crowdsources external-exposure discovery for free. NIST guidance (SP 800-216) and CISA's published VDP guidance are the reference points. An organization *without* a VDP is relying on luck for exactly the kind of finding a researcher will otherwise sit on for a 90-day disclosure window and then publish.

**Peer networks and professional associations.** ISACA, ISSA, and (ISC)² local chapters, plus informal CISO roundtables, are useful for the question a vendor will never answer honestly: "how are other organizations my size actually scoping and staffing this?"

**Vendor-neutral buyer research.** When you do evaluate commercial tools, lean on reviewer-driven sources like **Gartner Peer Insights**, **G2**, and **PeerSpot** rather than vendor marketing pages. They're free, they reflect real deployments, and they age better than any fixed "top 10" list.

**Training to build in-house skill.** For teams that want to run more of this internally, SANS courses with an OSINT/reconnaissance focus and GIAC certifications generally are the well-regarded path.

**When in-house genuinely isn't realistic.** Fractional or virtual CISO services, independent consultants, and managed service providers are a legitimate path for organizations without the bandwidth to build this internally. That's a category recommendation, not a specific endorsement. Evaluate any provider the same way you'd evaluate any other option in the decision matrix.

---

## Common Pitfalls

Where ASM programs break down in practice. If you recognize your own program in several of these, that's normal, and fixable.

- **Treating ASM as a one-time scan instead of a continuous program.** The most fundamental error. Your attack surface changes daily; a project has an end date, and this doesn't.
- **No named owner for findings.** Reports pile up, nothing closes, and the program becomes theater. Every finding needs an owner and a ticket.
- **Drowning in raw output with no triage capacity.** Tens of thousands of results on a first scan is normal. Without a triage process, the team either burns out or tunes out. (See the whole triage section.)
- **Treating every finding as equally urgent regardless of confidence or age.** This is what trains teams to eventually ignore entire finding categories, including the credential leaks and impersonation domains that actually matter.
- **Re-investigating the same false positive every cycle** because there's no suppression list carrying dispositions forward. Pure wasted effort, cycle after cycle.
- **Trying to cover all eleven categories on day one** instead of using the scope matrix to prioritize. The fastest way to stall a program before it delivers anything.
- **Only tracking IT-registered assets.** The whole point is discovering what you *don't* know about: the marketing microsite, the vendor-hosted portal, the rogue dev server.
- **Confusing security ratings with ASM.** A good third-party-risk score is not a discovery-and-remediation program for your own exposure.
- **No executive communication loop.** Findings that never reach a decision-maker never reduce risk. Build the Crayons-style readout.
- **Ignoring the human and brand surface** in favor of purely technical findings. Lookalike domains and employee OSINT are attack surface too, often the most damaging kind.

---

## What Good Looks Like

You'll know your ASM program is working, and can show leadership it's working, when:

- You maintain a **continuously updated asset inventory that is actually ground truth**, not a spreadsheet from last year with unknown accuracy.
- You can show a **visible trend line** (improving, holding, or slipping) on a single board-ready slide, and back it with the story of how you got there.
- **Every surviving finding has an owner, a status, and an SLA**, tracked to closure in your system of record rather than a side spreadsheet.
- Your **false-positive rate is declining cycle over cycle**, hard evidence the triage process is working and your team's attention is going to real risk, not noise.
- **Remediation coordination happens between cycles, not just at report time.** Findings don't wait for the next scan to get attention.
- You've **moved past the Must-have tier** on the scope matrix and are actively expanding into Should-have territory, a program that's building outward, not perpetually reacting to the same baseline gaps.

The through-line: a mature program isn't the one that finds the most things. It's the one where the *right* things reliably get found, prioritized, owned, and fixed, and where leadership can see that happening at a glance.

---

## Templates & Checklists

Everything below is populated with realistic examples so you can adapt rather than start from a blank page. Replace the sample values with your own; don't ship them empty.

### Template 1: Attack Surface Scoping Worksheet

The foundational inventory. Fill this out in Step 1 and revisit it every cycle.

| Field | Example Entry | Notes |
|---|---|---|
| Primary domains | `company.com`, `company.org` | Your main brand domains |
| Known subdomains | `mail.`, `vpn.`, `portal.`, `dev.` | Seed list; discovery will find more |
| External IP ranges / ASNs | `203.0.113.0/24`, ASN 64512 | Used to distinguish your infra from lookalikes |
| Cloud accounts / tenants | AWS acct 1234-5678, Azure tenant `company.onmicrosoft.com` | So cloud storage/exposure ties back to you |
| Subsidiaries / DBAs | Acme Regional LLC, "CompanyHealth" | Inherited attack surface; expand for M&A |
| Known third-party-hosted properties | Marketing site (Agency X), careers portal (SaaS Y) | Vendor-managed but still "you" to the world |
| Brand / keyword terms | "Company", "CompanyPay", product names | Feeds impersonation & dark-web monitoring |
| Employee email pattern(s) | `first.last@company.com` | Feeds breach-credential correlation |
| In-scope categories (from matrix) | Infra/DNS, Exposed services, Credentials, Cloud storage | Your Must-haves for this cycle |
| Scan cadence | Quarterly (moving to monthly Q3) | Match to maturity |

### Template 2: Scope Decision Matrix

The prioritization table from the Scoping section, ready to use as-is. Mark your organization's column, apply the regulatory and M&A overrides, and everything marked Must-have becomes this cycle's scope. (Reproduced here so it lives with your other working artifacts; see the Scoping section for the full override notes.)

### Template 3: First-Scan Asset Validation Checklist

Run this against every asset the baseline scan discovers, before treating anything as a finding.

- [ ] Is this asset **ours** (we own/operate it)? → Add to confirmed inventory.
- [ ] Is it **vendor-managed on our behalf** (marketing site, SaaS portal)? → Tag with the responsible vendor and internal owner.
- [ ] Is it **unrelated** (false attribution, shared IP, coincidental name)? → Log in suppression list with reasoning.
- [ ] Is it **unknown / needs investigation**? → Assign to an analyst; do not leave undecided across cycles.
- [ ] For confirmed assets: is there a **named internal owner**? → If not, assign one now.
- [ ] Is the asset **supposed to be internet-facing**? → If not, that's your first finding.

### Template 4: Finding Triage & Prioritization Rubric

Score each finding on three axes; the combination sets the disposition and priority.

| Axis | Low (1) | Medium (2) | High (3) |
|---|---|---|---|
| **Severity** (technical) | Informational / hygiene | Exploitable but limited impact | Critical: direct compromise vector |
| **Exploitability** (attacker effort) | Theoretical / hard | Known technique, some effort | Trivial / actively exploited in the wild |
| **Business impact** (what it touches) | Non-sensitive, isolated | Internal data / moderate systems | Crown jewels, customer/regulated data, or an attack-path pivot |

**Priority = Severity × Exploitability × Business impact.** Example: an exposed dev server with default credentials that connects to internal directory services scores High × High × High → top priority, even if in isolation it looked like a medium. Always ask the attack-path question: does this finding open a route toward something worse?

### Template 5: False-Positive Triage Checklist

**Domain / brand-similarity findings: validate before escalating:**
- [ ] Registration date, registrar, and WHOIS privacy checked
- [ ] Site content reviewed (mimics brand & collects data? vs. parked/for-sale/unrelated)
- [ ] Confirmed not shared-hosting/CDN false attribution
- [ ] Checked internally: not our own defensive registration, reseller, or affiliate
- [ ] Age + behavior assessed (recent + brand-close + mimicking = high signal)
- [ ] DNS/redirect checked (MX active? redirects to us? cert issuer?)
- [ ] Disposition assigned; if dismissed, logged in suppression list

**Breach / credential findings: age *and* relevance:**
- [ ] Breach date pulled and urgency tier assigned (<12mo / 1–3yr / 3yr+)
- [ ] Employment status checked against HR/identity (departed = often a fast close)
- [ ] Account still active? Password-rotation policy would have cycled it?
- [ ] MFA enforced on the account? (compensating control; document it)
- [ ] Disposition assigned; if dismissed, logged with specific reasoning

### Template 6: Suppression / Exception List

The living table that stops your team from re-investigating settled findings. Populated example (adapt the columns to your tooling):

| Finding | Type | First Seen | Disposition | Reasoning | Reviewed By | Next Revalidation |
|---|---|---|---|---|---|---|
| `secure-portal-yourbrand.com` | Lookalike domain | 2024-03 | Dismissed – Documented | Registered 2019, parked, no brand content, no complaints | J. Ramirez | 2026-09 (annual) |
| `yourbrand-billing.net` | Lookalike domain | 2026-02 | Confirmed | Registered 9 days prior, WHOIS-private, mirrors login, active MX | J. Ramirez | Closed – takedown filed |
| `j.smith@company.com` (2016) | Breach credential | 2026-01 | Dismissed – Documented | Departed 2021; account deprovisioned | M. Chen | N/A – terminated |
| `a.patel@company.com` (2019) | Breach credential | 2026-01 | Dismissed – Documented | Active; org-wide MFA since 2023; 90-day rotation | M. Chen | 2027-01 or on MFA policy change |
| `198.51.100.20:3389` | Exposed RDP | 2026-02 | Confirmed | Jump host, no business need for public RDP | S. Okoro | Closed – port restricted |

### Template 7: Executive Readout One-Pager (Crayons Framework)

Structure for the standing leadership artifact. Fits on one page; understandable in under 30 seconds.

```
EXTERNAL ATTACK SURFACE: EXECUTIVE READOUT           Q2 2026

OVERALL GRADE:  B-      (last cycle: C)   ▲ improving

┌─ WHERE WE STAND ─────────────────────────────────────────┐
│  Trend: 6 months ago D → now B-. Closed 14 of 19          │
│  criticals. 3 open, 2 pending vendor.                     │
└──────────────────────────────────────────────────────────┘

TOP FINDINGS THIS CYCLE
 1. Exposed RDP on jump host        → CLOSED (port restricted)
 2. Lookalike phishing domain       → takedown filed, in progress
 3. Leaked creds, 2 active accounts → reset + MFA enforced

DECISION NEEDED
 → Budget approval for continuous (vs. quarterly) scanning
   to close the 3-month visibility gap. Est. $X/yr.

WHAT'S IMPROVING: false-positive rate down 22% cycle-over-cycle.
```

### Template 8: Build vs. Buy vs. Managed-Service Decision Matrix

Answer honestly. The right answer depends on your reality, not on what's most sophisticated.

| Question | Lean Build (open-source, in-house) | Lean Buy (commercial platform) | Lean Managed Service |
|---|---|---|---|
| Team size / spare capacity? | Have skilled staff + weekly hours to triage | Have staff, limited time to *operate* tooling | Little to no spare FTE capacity |
| In-house OSINT/recon skill? | Strong | Moderate | Minimal; need expertise on tap |
| Org size (scope matrix) | Small, learning-focused | Medium–Large | Any size lacking bandwidth |
| Who owns triage every cycle? | Named internal analyst | Named internal analyst | Provider does first-pass triage |
| Budget shape | Low $, high time | Moderate–high $, moderate time | Higher $, low time |
| Biggest risk | Nobody maintains it; skill leaves with the person | Buying a platform nobody operates | Weaker internal knowledge; vendor dependency |

Note: "Small org → open-source + CISA free scanning" is a completely legitimate destination in this matrix, not a consolation prize.

### Template 9: Remediation RACI

Because ASM findings routinely cross team boundaries, ambiguity here is where remediation dies. Populate for your org; example:

| Finding type | Responsible | Accountable | Consulted | Informed |
|---|---|---|---|---|
| Exposed service / misconfig | IT / Infra | CISO | SecOps | Asset owner |
| Web app vulnerability | Dev / App team | CISO | AppSec | Product owner |
| Leaked credentials | IAM / IT | CISO | HR (if personnel) | Affected user |
| Lookalike domain / impersonation | Security | CISO | **Legal, Marketing/PR** | Comms |
| Vendor-hosted site finding | Vendor + IT liaison | CISO | Procurement, Legal | Business owner |
| Certificate expiry / sprawl | IT / PKI owner | CISO | Affected app teams | Service owner |

Note the impersonation and vendor rows: **Legal and Marketing/PR are not optional consults** for brand findings. A takedown or a cease-and-desist runs through them, not through the security team alone.

### Template 10: Tool / Vendor Evaluation Matrix

Score candidates on what actually matters, not module counts. Weight the rows for your priorities.

| Criterion | What to look for | Weight |
|---|---|---|
| Discovery method | Seed-based vs. entity-mapping vs. internet-wide; does it find *unknown* assets? | High |
| False-positive handling | Built-in triage workflow, suppression/exception tracking, confidence scoring | High |
| Coverage vs. your scope | Matches your Must-have categories from the matrix | High |
| Cadence | Supports the scan frequency your maturity needs | Medium |
| Integration | Feeds your ITSM/GRC/SIEM; bi-directional ticket sync | Medium |
| Remediation support | Ownership tracking, closure workflow, or managed coordination | Medium |
| Total cost of ownership | License **plus** the internal hours to operate it | High |
| Data handling / AI transparency | How your data is processed, retained, and (if AI-assisted triage) protected | Medium |

### Template 11: Program-Building Resource Quick Reference

Standalone list of where to get help (from the "Where to Get Help" section), for handoff to whoever owns the program:

- **Free scanning:** CISA Cyber Hygiene Services (email CISA to enroll); MS-ISAC (SLTT & public education)
- **Baseline checklist:** CISA Cross-Sector Cybersecurity Performance Goals (CPGs)
- **Sector intelligence:** Your industry ISAC (Health-ISAC, FS-ISAC, REN-ISAC, etc.)
- **Open-source tooling & community:** OWASP (Amass), OSINT Framework directory, ProjectDiscovery
- **Crowdsource discovery:** Stand up a Vulnerability Disclosure Program (NIST SP 800-216, CISA VDP guidance)
- **Peer benchmarking:** ISACA, ISSA, (ISC)² local chapters; CISO roundtables
- **Vendor-neutral reviews:** Gartner Peer Insights, G2, PeerSpot
- **Skill building:** SANS OSINT/recon courses, GIAC certifications
- **Outsourced option:** Fractional/virtual CISO, consultants, MSSPs (evaluate like any other option)

---

## Key Takeaways

- Your attack surface is everything about you discoverable from the open internet, and it changes every day. **ASM is a continuous program, not a one-time scan.**
- The exposures ASM catches happen *outside* your network. You can't firewall your way out of them; you have to see them first, ideally before an attacker or your insurance carrier does.
- **Scope deliberately.** Don't attempt all eleven categories on day one. Use the scope matrix, respect the regulatory and M&A overrides, and get your Must-haves running before anything else.
- **The hard part is triage, not discovery.** A living suppression list, confidence tiering, and age-plus-relevance checks on credentials are what keep your team from tuning out the findings that matter.
- **Match the program to your size.** A small org on CISA's free scanning with disciplined quarterly reviews beats a large org with an unused platform.
- **Stay vendor-neutral in your own decision.** Build, buy, and managed service are all legitimate. The right answer depends on your team's capacity and skill, not on what's most sophisticated.
- **Findings that don't reach a decision-maker don't reduce risk.** Build the executive loop, track every finding to closure, and show the trend line.

If you walk away able to scope a program, cut the noise, and route findings to closure, you can start building the next day. That's the goal.
