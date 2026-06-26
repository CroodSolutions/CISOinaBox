# Chapter 03 – Understanding the Adversary

---

## Introduction

One of the first things new CISOs discover is that the word "adversary" gets used as if it always means some sophisticated hacker sitting in a basement halfway around the world, patiently plotting a targeted attack against your organization. The reality is significantly messier — and in some ways, more manageable — than that.

The adversary landscape has two very different problems bundled into one word, and most organizations underweight one of them dramatically. External threats are real. Probes against your environment happen constantly — automated scanners, credential stuffing campaigns, phishing runs that go out to tens of thousands of organizations simultaneously without anyone specifically choosing *you*. But the breach that actually takes your organization down? Statistically, there is a very high probability it either started from the inside or was significantly enabled by someone on the inside — not because your people are bad actors, but because humans make mistakes, and attackers know how to exploit that.

This chapter is not about building a paranoid security culture. It is about building an informed one. The goal is to give you a practical, grounded way to think about who and what is actually coming at your organization, so you can make better decisions about where to invest your controls, how to consume the flood of threat intelligence coming at you every day, and how to protect your organization without treating every employee like a suspect.

Here is the core thesis of this chapter: **proactive control validation beats reactive threat chasing.** If your foundational controls are solid and your environment is well understood, a large percentage of threats become irrelevant before you ever hear about them. That is the posture this chapter is designed to help you build.

---

## What This Looks Like in Practice

Imagine you get an alert from your ISAC on a Monday morning. There is a new ransomware campaign actively targeting manufacturing companies using a specific vulnerability in a legacy SCADA system. Your inbox also has a vendor threat report about a nation-state group running a spear-phishing campaign. Your SOC analyst sends you a Slack message with a link to a Twitter thread from a well-known threat researcher about a new C2 framework being used in the wild.

That is three separate threat advisories before 9 AM. None of them come with a clear label that says "this one matters to you."

Here is how most organizations handle this situation: they try to investigate all three, burn significant analyst time, find nothing, and then do it again next week. Eventually, teams get exhausted and start ignoring the alerts entirely — which is the other failure mode.

Here is how a mature organization handles it: they run each advisory through a simple triage filter. Does the vulnerability exist in systems we actually run? Do we use the technology being targeted? Does our network architecture even allow the C2 communication pattern described? In many cases, the answer is no, and the advisory gets logged and closed in under 15 minutes. When the answer is yes, that advisory becomes a priority action item with an owner and a deadline.

The difference between those two organizations is not more analysts. It is a clear, repeatable process for determining what is in scope and what is not — built on a solid understanding of their own environment and the realistic threats facing organizations like theirs.

That is what this chapter helps you build.

---

## Section 1: The Threat Actor Taxonomy

Before you can assess threats intelligently, you need a clear picture of who is actually out there and what they want. This is not an academic exercise — it directly shapes which controls matter most, how you configure your monitoring, and where insider risk fits into your overall program.

### External Threat Actors

**Nation-State / Advanced Persistent Threat (APT) Groups**

These are well-resourced, patient, and skilled. They are typically sponsored or tolerated by a government and operate with specific strategic objectives: espionage, intellectual property theft, disruption of critical infrastructure, or long-term access for future use. The defining characteristic is persistence — they are willing to spend months establishing a foothold before taking any action that might be detected.

The important calibration here is scope. There are a finite number of true APT groups, and the vast majority of organizations are not their primary targets. If you are in defense contracting, critical infrastructure, financial services at scale, or developing technology with national security implications, APT risk is real and should shape your program meaningfully. For most other organizations, understanding APT tactics is useful for building detection capability, but worrying about being specifically targeted by a nation-state is probably not the highest and best use of your time.

Where APT knowledge does pay off is when you have confirmed indicators of a sophisticated actor in your environment. At that point, understanding their historical behavior patterns — what techniques they prefer, how they establish persistence, how they move laterally — helps you predict their next move and get ahead of them. MITRE ATT&CK is invaluable for this specific use case.

**Cybercriminal Organizations**

This is the category responsible for the majority of breaches that make the news. These groups operate like businesses: they have specializations, they use affiliate models, they buy and sell access, and they are primarily motivated by financial return. Ransomware groups are the most visible example, but this category also includes credential theft operations, business email compromise (BEC) groups, and fraud rings.

The key operational insight about cybercriminal organizations is that they are broadly opportunistic. They are not usually picking you specifically. They are running campaigns at scale, looking for organizations that have exposed vulnerabilities, weak authentication, or employees who can be socially engineered. This means your best defense is removing the opportunities they depend on — and we will cover exactly how to do that in Section 5.

**Hacktivists**

Hacktivist groups are ideologically motivated — they attack organizations to make a statement, cause disruption, or draw attention to a cause. Their capabilities vary enormously, from basic DDoS attacks and website defacement to more sophisticated intrusions. Most organizations will rarely encounter this category directly unless they are publicly associated with a politically contentious issue, have taken a public position on a social or environmental topic, or are in an industry that attracts activist attention (energy, government, financial services).

If hacktivist risk is relevant to your organization, the primary controls are DDoS mitigation, strong web application security, and a communications plan for your PR and legal teams — not necessarily a sophisticated detection engineering program.

**Opportunists and Script Kiddies**

This is the largest category by volume and the one most organizations will encounter most often. These actors are not sophisticated. They are using tools pulled from GitHub, running automated scanners, and trying techniques they found in tutorials. They are not designing novel attack architectures. They are looking for low-hanging fruit: default credentials, unpatched systems with known exploits, open ports that should have been closed.

The good news is that this category is almost entirely defeated by good basic hygiene. Patch management, MFA, eliminating unnecessary exposed services, and removing default credentials make your organization largely invisible to this group. They will move on to a softer target.

Do not underestimate the volume, though. Even if each individual attempt is unsophisticated, the sheer number of automated probes hitting your environment daily is significant. This is where detection and logging matter — not to catch a sophisticated actor, but to maintain situational awareness of what is coming at you.

### Insider Threats

This is the category that most organizations dramatically underweight, and it is the one most likely to be a contributing factor in a significant breach. There are two very distinct types, and they require different responses.

**Malicious Insiders**

A malicious insider is someone who intentionally uses their authorized access to harm the organization. The motivations vary: financial gain (selling data, committing fraud), retaliation (a disgruntled employee who feels wronged), or external coercion (an employee who has been compromised or pressured by an outside party).

The signals for this type of insider threat are behavioral — and this is where User and Entity Behavior Analytics (UEBA) tools provide real value. Patterns like accessing large volumes of data outside normal work hours, downloading data to external storage, accessing systems outside their normal scope, or unusual communication patterns with external parties are all indicators worth flagging. The key is establishing what "normal" looks like first, so anomalies are meaningful rather than just noise.

**Non-Malicious Insiders (Accidental)**

This is the much larger and often more impactful category. These are good people who made a mistake: they clicked a phishing link, misconfigured a cloud storage bucket, emailed the wrong attachment, or left a system in an insecure state. There is no malicious intent — but the outcome can be just as damaging as an intentional act.

The controls here are different. You are not looking for behavioral anomalies from a bad actor; you are looking for technical safeguards that reduce the blast radius of human error. Email security controls that catch phishing before it reaches the inbox. DLP tools that flag unusual data movement before it leaves. Configuration management that enforces secure defaults so one engineer's mistake does not expose a database. Security awareness training that turns employees into an active defense layer rather than a passive risk factor.

Most organizations struggle here because they treat insider threat as a single problem requiring a single solution. It is not. Malicious insiders and accidental insiders require fundamentally different approaches, and your program needs to address both.

---

## Section 2: Motivation and Attribution — How Much Does It Actually Matter?

This is one of the most common areas where organizations — especially those new to building a threat intelligence program — invest in the wrong thing.

Attribution is the process of determining *who* is behind an attack. And it feels important. If you can identify that a specific nation-state group is targeting your sector, surely that helps you defend better, right?

Sometimes. But less often than you might think.

Here is the honest reality: knowing the geographic origin of an attack or the name of the threat group responsible almost never changes your defensive actions on Monday morning. If you have just discovered that a phishing email was sent to your organization from an infrastructure associated with a known APT group, the immediate response is identical to what you would do for a less sophisticated attack: contain the affected systems, reset credentials, investigate the scope of access, and harden the entry point that was used. The attribution does not change the playbook.

**The narrow case where attribution matters**

There is one specific scenario where attribution becomes operationally valuable: when you have confirmed that a sophisticated, known actor is *already in your environment* and you need to predict their next move. In that case, understanding their historical behavior — the techniques they have used in past campaigns, how they establish persistence, where they tend to go after initial access — gives you an intelligence advantage. You can look for the techniques they are known to use before they use them in your environment. MITRE ATT&CK's group profiles are the right resource for this.

Outside of that scenario, attribution is largely a post-incident exercise useful for regulatory reporting and insurance purposes — not a real-time defensive tool.

**Behavior over identity**

What actually changes your defenses is understanding *behaviors*, not *identities*. Tactics, Techniques, and Procedures (TTPs) are the patterns of how attacks work — and they are far more stable and actionable than knowing who is behind an attack. A ransomware group's C2 communication pattern, their preferred initial access vector, or their known lateral movement techniques are all things you can build detection for — and those detections work regardless of which specific group is running the campaign.

This is the practical value of MITRE ATT&CK: it is a catalog of behaviors, not a list of actors. When you map your controls and detections to ATT&CK techniques, you are building defenses that work against the *class* of attack, not just one group.

**The sophistication reality**

One more calibration worth making: the vast majority of attack groups operating today are not elite. They are assembling tools from public repositories, running off-the-shelf exploit frameworks, and relying heavily on automation to cast a wide net. They are not building novel attack platforms. They are not designing custom malware from scratch.

This matters because it means your basic controls — if properly implemented — defeat the majority of what is coming at you. The percentage of threat actors who could bypass a well-configured MFA implementation, a properly segmented network, and a patched environment is small. This is not an argument for complacency; it is an argument for getting the fundamentals right before investing in sophisticated threat intelligence programs.

---

## Section 3: Consuming Threat Intelligence Without Drowning in It

If you have been in security for more than a few months, you already know the problem: there is *so much* threat intelligence coming at you. Your ISAC sends weekly digests. Your security vendors publish monthly threat reports. Researchers post findings on social media daily. Government agencies issue advisories. Your peers share what they are seeing in industry forums.

All of it feels important. None of it comes pre-filtered for your specific environment. And your team has a finite number of hours in the day.

Most organizations struggle here because they either try to consume everything (and burn out their team) or they give up and consume nothing (and miss something that matters). Neither extreme works.

### The CTI Triage Framework

The recommended approach is a simple, repeatable triage process that every advisory or threat report runs through before anyone spends meaningful time on it. This is not a complicated framework — it is a series of fast questions that quickly separate "relevant and actionable" from "interesting but not applicable."

**Step 1: Is the affected technology in our environment?**
This is the fastest filter. If the advisory is about a vulnerability in a product you do not use, a platform you do not run, or a protocol you have disabled, it is not relevant. Close it, log it, move on. This single filter will eliminate a significant percentage of advisories for most organizations.

**Step 2: If the technology is present, is it in a context that is exploitable?**
Just because you run a piece of software does not automatically mean you are vulnerable. Is the vulnerable version deployed? Is the attack vector accessible from your network architecture? Are there compensating controls already in place? Sometimes the answer is yes, you are exposed. Sometimes you are running a version that is not affected, or the attack requires network access you have already restricted.

**Step 3: What is the realistic likelihood that this technique targets organizations like ours?**
This requires knowing your threat profile (more on that in Section 4). A sophisticated spear-phishing campaign targeting defense contractors is worth noting but probably not worth deep investigation if you are a regional healthcare provider. The techniques matter; the specific actor targeting may not.

**Step 4: What specific action does this intelligence enable?**
This is the question that separates actionable intelligence from interesting information. If you cannot identify a concrete defensive action — a detection rule to write, a configuration to change, an IOC to block, a patch to prioritize — the intelligence does not warrant significant analyst time right now. It can be logged and referenced if related activity appears later.

### When to Act vs. When to Monitor vs. When to File

Not every piece of intelligence requires immediate action, and forcing everything into an action queue will overwhelm your team. A tiered response model works well:

**Act now:** The threat is relevant to technology you run, the attack vector is currently accessible in your environment, and there is a clear defensive action available. This goes on the immediate work queue with an owner and a deadline.

**Monitor:** The threat is relevant but your current controls may already address it, or the likelihood of targeting is low. Add relevant IOCs to your detection tools, set a flag to revisit if related activity appears, and move on.

**File and reference:** The threat is not applicable to your current environment, but the techniques described are worth understanding. Log it in your threat intelligence repository for reference and move on.

### When a Dedicated Threat Research Team Makes Sense

Here is an important organizational calibration: most organizations do not need a dedicated threat research team, and building one before you have the fundamentals covered is a misallocation of resources.

A dedicated threat research function makes sense when one of the following is true:

Your organization has extremely high risk exposure — you hold data or operate infrastructure where a breach would be catastrophic, and the intelligence advantage justifies the investment.

Your organization develops technology that is itself a potential attack vector. If you build security products, network equipment, or platforms that others depend on, threat research becomes part of your product quality assurance. If you are building firewalls, you need people actively researching how those firewalls might be defeated — not because you are being targeted, but because that research is how you build a better product and serve your customers responsibly.

For everyone else, the right model is a defined process that routes the right threat intelligence to the right people on your existing team — not a dedicated function. Start there, and build toward more dedicated capability as your program matures and the need becomes clear.

---

## Section 4: Building Your Threat Profile

Before you can make good decisions about which threats warrant attention, you need to understand the realistic threat landscape for an organization like yours. This is your threat profile, and it answers a fundamental question: who is actually likely to come after us, and why?

### Step 1: Define Your Attractive Attributes

Attackers choose targets for reasons. Understanding what makes your organization potentially attractive helps you understand who might target you and why. Ask these questions:

- What data do we hold that has value? (customer PII, payment card data, health records, intellectual property, financial data)
- What do we operate that could be disrupted for financial extortion? (production systems, patient care systems, revenue-generating platforms)
- What industry are we in, and is it currently being actively targeted? (healthcare, manufacturing, and financial services have historically been high-value ransomware targets)
- Do we have geopolitical exposure? (are we in a sector or geography that draws nation-state interest)
- How large are we? (enterprise organizations attract more targeted attention; SMBs attract more opportunistic automation)

### Step 2: Identify the Most Realistic Threat Categories

Based on your attractive attributes, you can now prioritize which threat actor categories are most realistic. For most mid-market organizations, the priority order looks something like this:

1. Opportunistic cybercriminals running automated campaigns (everyone)
2. Ransomware groups targeting your industry vertical (very common in healthcare, manufacturing, education)
3. Non-malicious insider threats / accidental actions (universal)
4. Malicious insiders (varies by data sensitivity and access controls)
5. Targeted cybercriminal groups (if you have high-value data worth specific effort)
6. Nation-state APTs (specific industries and geographies)

### Step 3: Map Threats to Your Environment

For each realistic threat category, ask: what would they need to succeed in our environment? A ransomware group needs initial access (typically phishing or an exposed vulnerability), the ability to move laterally, and the ability to deploy and execute their payload. If you have email security controls catching phishing, patch management eliminating known exploited vulnerabilities, network segmentation limiting lateral movement, and endpoint protection blocking payload execution — you have significantly disrupted their entire attack chain, regardless of which specific group is running the campaign.

This is the power of threat-informed defense: you are not reacting to specific actors, you are eliminating the conditions those actors depend on.

### Step 4: Validate Your Controls Against Realistic Attack Paths

This is where threat profiling connects to your security program. Take the top two or three threat scenarios for your organization and walk through how each attack would need to progress. At each stage, identify: what control would stop this, and do we have confidence that control is actually working?

This is a proactive exercise, not a reactive one — and it is far more valuable than chasing down every threat advisory that hits your inbox.

---

## Section 5: Using MITRE ATT&CK Practically

MITRE ATT&CK is one of the most valuable resources available to defenders, and one of the most commonly misused. The mistake most organizations make is treating it like a reference document — something to look at when they want to understand a specific technique. The real value is in using it as a structured framework for mapping your defensive coverage.

### What ATT&CK Actually Is

ATT&CK is a catalog of adversary behaviors organized by tactic (the goal of a specific phase of an attack) and technique (the method used to achieve that goal). It is built from real-world observations of how actual attacks have worked, which means every technique in the matrix represents something attackers have actually done in real environments.

The tactics follow a logical attack progression: initial access → execution → persistence → privilege escalation → defense evasion → credential access → discovery → lateral movement → collection → exfiltration → impact. Understanding this sequence is useful because it shows you that attacks have multiple stages — and you have multiple opportunities to detect or disrupt them.

### How to Use ATT&CK in Your Program

**Start with your threat profile.** Based on the threat profiling work in Section 4, identify the two or three threat scenarios most relevant to your organization. For each one, look up the techniques associated with that type of attack. If ransomware is your top threat, ATT&CK has specific technique mappings for how ransomware campaigns typically operate.

**Map your existing controls.** For each technique in your priority scenarios, ask: do we have a control that would detect or prevent this? This does not need to be exhaustive on day one. Start with the techniques most relevant to your top threats and build from there.

**Identify coverage gaps.** The techniques where you have no detection and no prevention are your prioritized investment list. Address the gaps that correspond to your most realistic threat scenarios first.

**Use ATT&CK for detection engineering.** When your SOC is building detection rules, ATT&CK technique IDs (like T1566 for phishing or T1078 for valid accounts) provide a common language for describing what the rule is designed to catch. This makes your detection library far more maintainable and organized.

**Reference group profiles when relevant.** If you have confirmed indicators of a specific threat actor in your environment, ATT&CK's group pages list the techniques that group is known to use. This gives you a prioritized list of what to look for next.

### What ATT&CK Is Not

ATT&CK is not a compliance checklist, and trying to achieve full coverage across the entire matrix is neither realistic nor necessary for most organizations. It is a prioritization tool — use it that way.

---

## Section 6: Insider Threat — Without Creating a Boogeyman Culture

Let us address the tension directly: insider threat is real, insider threat causes significant breaches, and you absolutely need controls to address it. And also: treating every employee like a potential threat is corrosive to your organization's culture, damages the trust relationship that makes people effective, and ultimately makes your security program harder to operate — not easier.

These things are not in conflict if you approach insider threat the right way.

### The Trust Baseline

When an organization hires someone, they extend a meaningful level of trust. They give that person access to systems, data, and resources because that access is necessary for them to do their job. Security should operate within that trust relationship, not against it. The goal is not to prevent every conceivable insider action — it is to detect meaningful anomalies and reduce the blast radius of mistakes.

### The Organizational Duty

Here is something that rarely gets stated clearly: the organization has a reciprocal obligation in the insider threat equation. If you are going to hold employees accountable for security outcomes, you also have a duty to give them tools that are safe to use, configured to protect them from mistakes, and environments where they can report errors without fear of disproportionate consequences.

An employee who clicks a phishing link because your email security controls failed to filter it is not the primary control failure. The email control is. An employee who accidentally shares a file publicly because your cloud storage defaulted to public access is not the primary failure. The misconfigured default is.

Build the controls first. Train the people second. Monitor for anomalies third. That sequence matters.

### What Monitoring Is Appropriate

The right insider threat monitoring program focuses on behavioral anomalies — patterns that deviate meaningfully from established baselines — rather than blanket surveillance of everything everyone does. The right capabilities, scaled by org size:

**Email and web monitoring:** Appropriate at all sizes. You should know if large volumes of data are being sent externally, if employees are visiting known malicious sites, or if unusual attachment patterns are appearing. This is standard practice and generally expected by employees in professional environments.

**User and Entity Behavior Analytics (UEBA):** These tools establish baseline behavior for individual users and flag meaningful deviations — accessing systems outside normal working hours, pulling unusually large data sets, logging in from anomalous locations. This is the right tool for detecting the early stages of malicious insider activity. Typically an IG2/IG3 investment.

**Privileged access monitoring:** Users with elevated privileges — administrators, engineers with production access, finance users with payment system access — warrant closer monitoring than standard users. This is not about distrust; it is proportional to the impact their access could have if misused or compromised.

**DLP (Data Loss Prevention):** Controls that catch data leaving the organization through unauthorized channels — personal email, cloud storage, USB drives. Useful for both malicious and accidental data loss scenarios.

### Behavioral Indicators to Watch For

These are patterns worth investigating, not automatic conclusions of malicious intent. Context always matters.

- Significant increases in data access volume, especially before offboarding or resignation
- Accessing systems or data outside normal role scope
- Repeated failed access attempts to restricted systems
- External data transfers to personal accounts or services
- Printing or downloading large volumes of sensitive data
- Accessing systems during unusual hours without a clear business reason
- Disabling or attempting to disable security tools

### How to Investigate Without Damaging Trust

When a behavioral alert fires, the right first step is not an accusation — it is a quiet investigation to understand context. Most anomalies have benign explanations: a project deadline that required after-hours work, a legitimate data pull for a business need, a manager who asked them to access something outside their normal scope. Investigate first. Escalate to HR and Legal when the investigation warrants it, not before.

---

## Section 7: Translating Adversary Knowledge Into Program Decisions

All of the adversary understanding in the world is only valuable if it shapes actual security program decisions. This section connects the threat landscape to your defensive priorities.

### The Control Priority Framework

For each of your top threat scenarios, the recommended approach is to work backward from the attack chain and ask: where can we interrupt this, and what does that require?

**If ransomware is your top threat (common for healthcare, manufacturing, education, mid-market generally):**
Your priority controls are email security (primary initial access vector), endpoint detection and response (catching payload execution and lateral movement), privileged access management (limiting the blast radius of compromised credentials), and backup integrity (your recovery capability if prevention fails). Patch management matters significantly because many ransomware campaigns use known, exploited vulnerabilities for initial access.

**If credential theft and fraud is your top threat (common for financial services, retail, high-value data holders):**
Your priority controls are MFA everywhere (especially on externally facing systems), privileged access management, anomaly detection on authentication patterns, and strong email security against phishing. Business Email Compromise (BEC) specifically requires email authentication controls (DMARC, DKIM, SPF) and user training on financial authorization processes.

**If insider threat is your top risk (common for organizations with highly sensitive IP, regulated data, or significant access by employees):**
Your priority controls are least-privilege access management (limiting who has access to what), UEBA or behavioral monitoring, DLP, and strong offboarding processes. Just as important is building a culture where people can report mistakes without fear — early disclosure of accidental incidents dramatically reduces the damage.

### The Opportunity Disruption Mindset

One of the most effective defensive postures you can adopt is systematically eliminating attack opportunities rather than trying to detect and respond to every attack. This means regularly asking: what services, protocols, or configurations in our environment are not strictly necessary for business operations but could be exploited by an attacker?

Exposed RDP access that is not needed? Disable it. Legacy authentication protocols that support downgrade attacks? Block them. Admin interfaces accessible from the public internet? Restrict them to internal networks or VPN. Default credentials on any system? Eliminate them. Unnecessary ports and services? Close them.

This approach works because it reduces the surface area that every threat actor — sophisticated or not — has to work with. Every unnecessary service you eliminate disrupts the potential attacks that depended on it, across all threat categories simultaneously.

---

## Common Pitfalls

**Over-investing in attribution at the expense of fundamentals.** It is more interesting to read about APT groups than to make sure your patch management is running on schedule. Do not let that bias drive your program priorities. Attribution is a tool for specific situations, not a foundation for a security program.

**CTI paralysis — too much intelligence, no action.** If your team is spending more time reading threat reports than building and validating controls, your intelligence consumption has become a liability. Intelligence that does not enable a specific action is not worth significant analyst time. Build the triage process and enforce it.

**Treating insider threat as a single problem.** The controls for malicious insiders and accidental insiders are fundamentally different. If your insider threat program consists entirely of a DLP tool and behavioral monitoring, you are missing the technical safeguards, secure-by-default tooling, and cultural components that address the larger accidental category.

**Building a boogeyman culture.** If employees feel like they are constantly surveilled and that any mistake will result in punishment, they will stop reporting incidents, hide problems, and disengage from security culture. This directly undermines your ability to detect and respond to incidents early. Investigate anomalies quietly. Assume benign explanations until you have evidence otherwise. Create an environment where early disclosure is rewarded, not punished.

**Chasing threats that do not apply to your environment.** Not every advisory requires investigation. Without a triage process, your team will waste enormous amounts of time on threats that were never applicable. Build the filter.

**Assuming sophistication where there is none — and vice versa.** Most attacks are opportunistic and unsophisticated. But assuming every attack is low-sophistication is how you miss the early indicators of something more serious. Treat anomalies seriously. Investigate them methodically. Let the evidence tell you what you are dealing with.

**Ignoring the non-malicious insider.** The accidental insider causes a significant percentage of breaches. A program focused entirely on malicious behavior will miss this entirely. Address human error through technical controls and a no-blame reporting culture, not just behavioral monitoring.

---

## What Good Looks Like

### IG1 — Small Organizations (Basic)

At the foundational level, a small organization should be able to demonstrate:

- A documented, high-level understanding of the two or three most realistic threat categories facing the organization (typically: opportunistic cybercriminals, phishing/social engineering, and accidental insider actions)
- Basic security controls that address the most common attack vectors: email filtering, MFA on externally facing systems, patching, endpoint protection
- A simple process for receiving and triaging external threat advisories — even if that process is just "CISO reviews ISAC digest weekly and flags anything relevant"
- A security awareness program that educates employees about phishing and social engineering — addressing the non-malicious insider risk
- A clear offboarding process that terminates access promptly when employees leave

### IG2 — Medium Organizations (Foundational)

At the operational level, a medium organization should be able to demonstrate:

- A documented threat profile that identifies realistic threat actors, their likely techniques, and the controls mapped against those techniques
- A formal CTI triage process with defined criteria for escalation vs. monitoring vs. filing
- UEBA or behavioral monitoring capability for detecting insider threat indicators
- MITRE ATT&CK coverage mapping — even a basic one — identifying which techniques your top threat scenarios use and where your detection coverage exists
- Regular threat-informed reviews of control effectiveness: do our controls actually stop what we think they stop?
- A DLP implementation addressing the most critical data types
- A defined process for handling insider threat investigations that includes HR and Legal

### IG3 — Large Organizations (Advanced)

At the advanced level, a large organization should be able to demonstrate:

- A mature threat intelligence program with defined consumption, triage, and actioning workflows
- Full ATT&CK coverage mapping across all priority threat scenarios, with active detection engineering tied to technique coverage
- Threat hunting capability — proactive searches for attacker behavior in the environment, not just reactive alerting
- A formal insider threat program with dedicated process, cross-functional ownership (Security, HR, Legal), and regular case reviews
- Continuous control validation through purple team exercises or automated breach and attack simulation (BAS) tools
- Intelligence sharing participation — contributing back to ISACs and peer communities, not just consuming
- Regular threat modeling exercises that revisit the threat profile as the business changes

---

## Templates and Checklists

---

### Template 1: Organizational Threat Profile

*Use this to document the realistic threat landscape for your organization. Review and update annually or when significant business changes occur.*

---

**Organization:** Acme Manufacturing Co.
**Industry:** Manufacturing
**Size:** ~1,200 employees
**Key Data Assets:** Customer contracts, proprietary product designs, ERP/financial data, employee PII
**Critical Systems:** ERP (SAP), production control systems, email (M365), customer portal

---

**Attractive Attributes Assessment**

| Attribute | Present? | Notes |
|-----------|----------|-------|
| Customer PII | Yes | ~50,000 customer records in CRM |
| Payment Card Data | No | Payments handled by third-party processor |
| Health Records | No | Not applicable |
| Intellectual Property | Yes | Product designs, manufacturing processes |
| Critical Infrastructure Dependencies | Partial | Production systems — disruption has financial impact |
| High-Value Financial Data | Yes | Revenue ~$180M; ERP holds pricing and contract data |
| Regulated Data (HIPAA/GDPR) | Partial | EU employee and customer data in scope for GDPR |

---

**Threat Actor Priority Assessment**

| Threat Category | Likelihood | Potential Impact | Priority |
|-----------------|------------|-----------------|----------|
| Opportunistic cybercriminals (automated) | High | Medium | High |
| Ransomware groups targeting manufacturing | High | High | Critical |
| Non-malicious insider (accidental) | High | Medium–High | High |
| Business Email Compromise | Medium | High | High |
| Malicious insider | Low–Medium | High | Medium |
| Hacktivist groups | Low | Medium | Low |
| Nation-state APT | Low | Very High | Monitor |

---

**Top 3 Threat Scenarios and Control Mapping**

**Scenario 1: Ransomware via phishing initial access**

Attack path: Phishing email → credential theft or malware execution → lateral movement → ransomware deployment

| Stage | Required Control | Status | Gap? |
|-------|-----------------|--------|------|
| Phishing delivery | Email filtering + anti-spoofing (DMARC) | Deployed | DMARC not enforced — remediation in Q3 |
| Execution | Endpoint protection (EDR) | Deployed | Coverage at 94% of endpoints — gap list exists |
| Lateral movement | Network segmentation + privileged access controls | Partial | Production network not fully segmented — roadmap item |
| Deployment | Application whitelisting / behavioral blocking | Partial | EDR behavioral blocking enabled; whitelisting not implemented |
| Recovery | Immutable backups | Deployed | Backup integrity last tested Q1 — schedule quarterly |

**Scenario 2: Business Email Compromise targeting finance**

Attack path: Spoofed or compromised email → fraudulent wire transfer or vendor payment request

| Stage | Required Control | Status | Gap? |
|-------|-----------------|--------|------|
| Spoofed email | DMARC, DKIM, SPF enforcement | Partial | SPF/DKIM deployed; DMARC not enforced |
| Compromised account | MFA on M365 | Deployed | MFA at 98% — 3 finance accounts exempted; remediation scheduled |
| Authorization | Dual approval for wire transfers >$10K | Deployed | Process confirmed with Finance |
| Detection | Anomaly alerting on wire transfer requests | Not deployed | Add to Q4 roadmap |

**Scenario 3: Non-malicious insider data loss**

Attack path: Employee error → data sent to wrong recipient, uploaded to personal storage, or exposed via misconfiguration

| Stage | Required Control | Status | Gap? |
|-------|-----------------|--------|------|
| Email DLP | Email DLP for sensitive data patterns | Partial | Rules exist but not tuned — high false positive rate |
| Cloud storage | DLP for cloud uploads | Not deployed | Roadmap: Q4 |
| Misconfiguration | Cloud posture management (CSPM) | Deployed | M365 Secure Score at 68% — target 80% by Q3 |
| Reporting culture | No-blame incident reporting process | Partial | Process exists; not well communicated — add to awareness training |

---

### Template 2: Threat Intelligence Triage Checklist

*Run every significant threat advisory through this checklist before assigning analyst time.*

---

**Advisory:** ISAC Advisory — Active exploitation of CVE-2024-XXXX in Ivanti Connect Secure VPN
**Source:** MS-ISAC
**Date Received:** [Date]
**Triaged By:** [Name]

---

**Step 1 — Technology Relevance**

- [ ] Does the affected technology exist in our environment?
  - Technology named in advisory: **Ivanti Connect Secure VPN**
  - Do we use this? **Yes — deployed for remote access**
  - If No → Close advisory. Log date and reason. No further action.

**Step 2 — Exploitability Assessment**

- [ ] Are we running the affected version?
  - Current version deployed: **22.5R1.1**
  - Affected versions per advisory: **22.4R2 and earlier**
  - Result: **Not affected — current version not listed as vulnerable**
  - If not affected → Downgrade to Monitor. Log and close.

- [ ] Is the attack vector accessible from our architecture?
  - Required access for exploitation: **Unauthenticated network access to management interface**
  - Is management interface internet-facing? **No — restricted to internal network**
  - Result: **Additional compensating control confirmed**

**Step 3 — Likelihood Assessment**

- [ ] Is this technique being used against organizations in our industry/size?
  - Advisory notes targeting: **Government and critical infrastructure primarily**
  - Does this match our profile? **Partial — manufacturing not specifically called out**

**Step 4 — Action Determination**

- [ ] What specific action does this intelligence enable?

  - [ ] **Act Now** — Relevant, exploitable, clear action available → Assign owner, set deadline
  - [x] **Monitor** — Relevant but mitigated or low likelihood → Add IOCs to detection tools, flag for follow-up
  - [ ] **File** — Not applicable to our environment → Log and close

**Assigned Action:** Add advisory IOCs to SIEM watchlist. Confirm patch notification process for Ivanti is active for future versions. Revisit if management interface exposure status changes.

**Owner:** [SOC Lead]
**Follow-up Date:** [30 days]

---

### Template 3: Insider Threat Indicator Reference Card

*Use this as a reference for behavioral patterns worth investigating. These are indicators, not conclusions — context always determines appropriate response.*

---

**Data Access Anomalies**

| Indicator | Potential Explanation | Investigation Priority |
|-----------|----------------------|----------------------|
| Accessing 5x or more normal data volume in a single session | Project deadline, legitimate data pull, role change | Medium — verify business context |
| Accessing data outside normal role scope | Cross-team project, manager request, system error | Medium — verify with manager |
| Bulk downloads to local storage or external drive | Legitimate work need, offboarding data pull, data theft | High — especially if near resignation/offboarding |
| Accessing sensitive systems outside business hours | Timezone difference, on-call work, unauthorized access | Medium — review access logs for context |

**Communication and Transfer Anomalies**

| Indicator | Potential Explanation | Investigation Priority |
|-----------|----------------------|----------------------|
| Email with large attachments to personal addresses | Legitimate convenience, policy violation, data theft | High — especially for sensitive data types |
| Upload to unauthorized cloud storage (personal Dropbox, Google Drive) | Convenience, awareness gap, intentional exfiltration | High — implement DLP blocking |
| Forwarding of email threads to external parties | Legitimate collaboration, unauthorized sharing | Medium — review recipients and content |
| Unusual volume of printing sensitive documents | Presentation prep, legitimate need, data staging | Medium — especially if near departure |

**Access and Authentication Anomalies**

| Indicator | Potential Explanation | Investigation Priority |
|-----------|----------------------|----------------------|
| Repeated failed access to restricted systems | Legitimate need without proper access, probing | Medium — review with access management |
| Login from anomalous geographic location | Travel, VPN usage, account compromise | High — verify with employee directly |
| Account sharing or credential delegation | Convenience (policy violation), cover for unauthorized action | High — always a policy violation regardless of intent |
| Attempting to disable security tools | Technical troubleshooting, malicious action | Critical — immediate investigation |

**Behavioral and Contextual Indicators**

| Indicator | Potential Explanation | Investigation Priority |
|-----------|----------------------|----------------------|
| Accessing systems after resignation notice | Offboarding activity, data preservation, unauthorized copying | High — access should be reviewed immediately upon notice |
| Expressed significant dissatisfaction or grievance | Normal frustration, potential escalation risk | Low — monitor for additional indicators; do not assume threat |
| Sudden changes in work patterns | Personal circumstances, role dissatisfaction, prelude to action | Low — context dependent |

**Investigation Protocol**

When an indicator fires, follow this sequence:

1. **Gather context first.** Pull the access logs, understand the full picture of what happened, and determine what data or systems were involved.
2. **Check for business context.** Is there a project, deadline, or legitimate business need that explains the anomaly? Check with the employee's manager before contacting the employee directly.
3. **Assess severity.** Is sensitive data actually involved? Is this a pattern or an isolated event?
4. **Escalate appropriately.** If the investigation confirms a potential policy violation or incident, loop in HR and Legal before taking action against the employee. Security should not conduct terminations or formal investigations alone.
5. **Document everything.** If this becomes a formal investigation, your documentation is the evidence chain.

---

### Checklist: CTI Program Starter (IG1/IG2 Organizations)

Use this checklist to establish a baseline threat intelligence consumption capability without overcommitting resources.

**Intelligence Sources — Select 2-3 to Start**
- [ ] ISAC relevant to your industry (MS-ISAC for state/local government; H-ISAC for healthcare; FS-ISAC for financial services)
- [ ] CISA advisories and alerts (free, well-curated, actionable)
- [ ] Your primary security vendors' threat reports (EDR, email security, SIEM vendors all publish regularly)
- [ ] FBI InfraGard (industry-specific briefings, recommended for most organizations)

**Triage Process — Establish Before You Start Consuming**
- [ ] Document who receives and triages advisories (typically CISO or security lead)
- [ ] Define triage criteria (use the Threat Intelligence Triage Checklist above)
- [ ] Set a weekly time box for advisory review — do not let it expand without intentional justification
- [ ] Create a simple log for advisories reviewed (date, source, determination, action taken)

**IOC Integration — Connect Intelligence to Detection**
- [ ] Confirm your SIEM or EDR can ingest IOC feeds
- [ ] Identify 1-2 free IOC feeds to start (CISA AIS, AlienVault OTX are both reliable)
- [ ] Establish a process for adding high-confidence IOCs to your detection tools
- [ ] Set a review cadence for aging out stale IOCs (IOCs older than 90 days have sharply reduced value)

**Threat Profile — Document Your Baseline**
- [ ] Complete the Organizational Threat Profile template (Template 1 above)
- [ ] Review and update annually, or when significant business or technology changes occur
- [ ] Share the threat profile with senior leadership — this is a business risk document, not just a security document

**Insider Threat — Baseline Controls**
- [ ] Confirm offboarding process terminates access within 24 hours (same day for involuntary departures)
- [ ] Implement email DLP for sensitive data patterns (even basic rules are better than none)
- [ ] Confirm monitoring is in place for privileged accounts
- [ ] Include insider threat scenarios in security awareness training
- [ ] Communicate a clear, no-blame process for employees to self-report mistakes

---

## References

- MITRE ATT&CK Framework: https://attack.mitre.org/
- MITRE ATT&CK Groups (for attribution research): https://attack.mitre.org/groups/
- CISA Cybersecurity Advisories: https://www.cisa.gov/news-events/cybersecurity-advisories
- MS-ISAC (Multi-State ISAC): https://www.cisecurity.org/ms-isac
- FBI InfraGard: https://www.infragard.org/
- FIRST.org (Incident Response Coordination): https://www.first.org/
- AlienVault OTX (Free IOC Platform): https://otx.alienvault.com/
- Lockheed Martin Cyber Kill Chain: https://www.lockheedmartin.com/en-us/capabilities/cyber/cyber-kill-chain.html
- CISA Automated Indicator Sharing (AIS): https://www.cisa.gov/topics/cyber-threats-and-advisories/information-sharing/automated-indicator-sharing-ais
- ACTRA Arizona Threat Sharing: https://www.actraaz.org
- NIST SP 800-150 – Guide to Cyber Threat Information Sharing: https://csrc.nist.gov/publications/detail/sp/800-150/final
- Awesome Threat Intelligence (curated CTI resources): https://github.com/hslatman/awesome-threat-intelligence
