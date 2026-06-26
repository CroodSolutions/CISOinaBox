# Supplemental: How Cyber Attacks Work — The Attack Kill Chain

*This document is a technical companion to Chapter 03 – Understanding the Adversary. It is intended for security practitioners who want a deeper understanding of attack progression models and how to apply them defensively.*

---

## Why Attack Models Matter

Understanding how attacks work is not an academic exercise. It is the foundation of effective defense. When you know the stages an attacker must move through to achieve their objective, you gain something valuable: multiple opportunities to detect or disrupt them before they get there.

No attack — regardless of how sophisticated the actor — skips steps entirely. They may compress them, automate them, or execute them faster than expected. But the progression is consistent. An attacker must get in before they can move. They must move before they can steal. They must establish persistence before they can wait. Each of those stages is a detection opportunity and a potential chokepoint.

The models covered in this document give you a structured way to think about that progression and map your defenses against it.

---

## The Cyber Kill Chain

The Cyber Kill Chain was developed by Lockheed Martin's intelligence-driven defense team and published in 2011. It remains one of the most widely used mental models for understanding how targeted attacks progress from reconnaissance through impact. The model has seven stages.

```
Reconnaissance → Weaponization → Delivery → Exploitation → Installation → Command & Control → Actions on Objectives
```

### Stage 1: Reconnaissance

The attacker gathers information about the target before launching any active attack. This phase is largely passive from the defender's perspective — much of it happens outside your environment entirely.

**What attackers are doing:**
- Scanning public-facing infrastructure with tools like Shodan, Censys, or nmap to identify exposed services, open ports, and software versions
- Harvesting employee email addresses, organizational structure, and technology stack from LinkedIn, company websites, job postings, and public documents
- Reviewing code repositories (GitHub, GitLab) for accidentally committed credentials, API keys, or internal documentation
- Reviewing DNS records, WHOIS data, and SSL certificate transparency logs to map infrastructure

**What you can do:**
- Conduct your own external attack surface review regularly — see what an attacker sees before they do (Chapter 04 covers this in depth)
- Monitor for your domains and IPs in certificate transparency logs and passive DNS
- Enforce clean commit practices and secrets scanning in your development pipelines
- Limit what job postings and public documentation reveal about your specific technology stack
- Enable web application firewall (WAF) logging to detect reconnaissance scanning patterns

**Defender advantage:** Disrupting reconnaissance does not stop a determined attacker from eventually finding an entry point, but it raises the cost of targeting you specifically. Many opportunistic attackers will move on to an easier target if your external surface is well-managed.

---

### Stage 2: Weaponization

The attacker creates or acquires the tool or payload they will use to exploit the target. This stage happens entirely off your network — you will not see it in your logs. But understanding it helps you anticipate what is coming.

**What attackers are doing:**
- Selecting or modifying exploit code for a known vulnerability in software you run
- Building a malicious document (weaponized PDF, Office macro, HTML smuggling payload) designed to execute when opened
- Purchasing access to exploit kits or pre-built malware from criminal markets
- Registering lookalike domains or setting up attacker-controlled infrastructure for command and control
- Crafting phishing lures using the information gathered in reconnaissance

**What you can do:**
- Patch aggressively — if the vulnerability does not exist in your environment, the weapon does not work
- Disable or restrict features that are commonly weaponized: Office macros, PowerShell execution policy, legacy script interpreters
- Subscribe to vulnerability intelligence feeds (CISA KEV, vendor advisories) to identify vulnerabilities being actively weaponized in the wild
- Monitor for lookalike domain registrations against your primary domains

**Key insight:** The weaponization stage is where patch management has its biggest impact. A large percentage of successful attacks use vulnerabilities that have had patches available for months or years. Keeping systems current eliminates an enormous percentage of available weapons before the attack even begins.

---

### Stage 3: Delivery

The attacker delivers the weapon to the target environment. This is the first stage that crosses into your environment and the first stage where your controls have a direct opportunity to intercept.

**What attackers are doing:**
- Sending phishing emails with malicious attachments or links (most common delivery vector)
- Exploiting publicly exposed services directly (internet-facing RDP, unpatched web applications, exposed admin interfaces)
- Using watering hole attacks — compromising websites the target's employees are known to visit
- Delivering via removable media in physical access scenarios
- Using supply chain compromise — embedding malicious code in a software update or dependency

**What you can do:**
- Email security controls: anti-phishing, attachment sandboxing, URL rewriting and scanning, DMARC/DKIM/SPF enforcement
- Web proxy filtering: block known malicious domains and categories, inspect SSL/TLS traffic
- Reduce the external attack surface: close unnecessary ports, disable internet-facing admin interfaces, require VPN for remote access to internal systems
- Endpoint controls: application control policies that prevent execution of files from user writeable directories, script execution restrictions

**Defender advantage:** Delivery is one of the highest-leverage stages for defenders. Email filtering and web proxies operating at scale can block the vast majority of commodity delivery attempts before they reach the end user. Investing here has outsized returns.

---

### Stage 4: Exploitation

The weapon executes and exploits a vulnerability or behavior to gain an initial foothold. The attacker is now active in the environment.

**What attackers are doing:**
- Triggering a software vulnerability (memory corruption, privilege escalation, remote code execution)
- Exploiting a configuration weakness (default credentials, misconfigured permissions)
- Leveraging human behavior (user clicks a link, opens a file, enters credentials into a fake login page)
- Chaining multiple low-severity issues to achieve higher-impact access

**What you can do:**
- Endpoint Detection and Response (EDR): behavioral detection engines that identify exploit patterns (shellcode execution, process injection, suspicious child processes) in real time
- Application hardening: ASLR, DEP/NX, sandboxing for vulnerable application categories (browsers, document readers, email clients)
- Privileged access controls: ensure exploitation of a standard user account does not immediately yield administrative access
- User training: reducing the success rate of social engineering exploitation — trained users are a detection layer, not just a risk factor
- Multi-factor authentication: even if credentials are harvested via exploitation, MFA blocks their immediate use

**Key insight:** This is the stage where endpoint controls earn their place in the stack. Prevention at delivery is ideal, but when something gets through, EDR behavioral detection is your next line of defense. The goal is to catch exploitation before the attacker has time to complete the next stage.

---

### Stage 5: Installation

The attacker establishes persistence — a mechanism that ensures continued access even if the initial exploit vector is closed or the system is rebooted.

**What attackers are doing:**
- Installing a remote access tool (RAT) or backdoor
- Creating new user accounts or modifying existing accounts with elevated privileges
- Adding scheduled tasks, registry run keys, or service installations that survive reboot
- Modifying startup scripts or boot processes
- Planting web shells on compromised web servers

**What you can do:**
- EDR behavioral detection for common persistence mechanisms (scheduled task creation, registry modifications, service installs by unexpected processes)
- File integrity monitoring (FIM) on critical system paths and web directories
- Privileged access monitoring: alerting on new local admin account creation, changes to privileged groups
- Immutable infrastructure patterns: if systems are rebuilt regularly from known-good images, persistence is harder to maintain
- Logging: Windows Event IDs 4698 (scheduled task created), 4720 (user account created), 7045 (new service installed) are high-value signals

**Defender advantage:** Detection at the installation stage — before the attacker begins moving laterally or exfiltrating data — significantly limits the blast radius of an incident. Many IR engagements reveal that attackers had persistent access for weeks or months before taking any action that triggered detection. The earlier you catch installation, the smaller your problem.

---

### Stage 6: Command and Control (C2)

The installed malware or backdoor establishes an outbound communication channel to attacker-controlled infrastructure. This is how the attacker issues commands, receives data, and maintains interactive control of the compromised system.

**What attackers are doing:**
- Establishing encrypted HTTPS beaconing to attacker-controlled servers (mimics normal web traffic)
- Using legitimate platforms as C2 channels: GitHub, Pastebin, Discord, Slack, Telegram — services that are difficult to block and generate traffic that blends in
- Implementing low-and-slow beaconing patterns with jitter to evade detection based on timing regularity
- Using DNS-based C2 (DNS tunneling) to exfiltrate data and receive commands through DNS queries
- Leveraging compromised legitimate infrastructure to make C2 traffic appear to come from trusted sources

**What you can do:**
- DNS filtering and monitoring: block known malicious domains, alert on unusual DNS query patterns, flag DGA (domain generation algorithm) traffic
- Network traffic analysis: identify beaconing patterns, unusual outbound connection timing, unexpected protocols or destinations
- TLS inspection: decrypt and inspect HTTPS traffic (where legally and technically feasible) to identify malicious content in encrypted channels
- Egress filtering: restrict outbound connections to only necessary destinations and ports — unknown destinations generate alerts
- Threat intelligence integration: feed known C2 infrastructure IOCs into your SIEM and network controls

**Key insight:** C2 detection is where network-layer monitoring earns its keep. Many organizations have good endpoint and email controls but limited visibility into outbound network behavior. DNS filtering in particular is a high-value, low-cost control that catches a significant percentage of C2 activity.

---

### Stage 7: Actions on Objectives

The attacker achieves their ultimate goal. Depending on their motivation, this could be data exfiltration, ransomware deployment, destructive action, or sustained access for future operations.

**What attackers are doing:**
- Lateral movement to reach high-value systems (domain controllers, file servers, databases, backup systems)
- Credential harvesting (Mimikatz, LSASS dumping, Kerberoasting) to obtain privileged account credentials
- Data staging and exfiltration to external infrastructure
- Ransomware deployment: encrypting files across network shares and endpoints, deleting backup copies
- Establishing additional persistent access points (in case the primary backdoor is discovered)

**What you can do:**
- Network segmentation: limit the systems a compromised endpoint can reach — lateral movement should require crossing a network boundary that generates alerts
- Privileged access management: limit the blast radius of any single compromised account
- Backup integrity: maintain immutable, offline, or air-gapped backup copies that cannot be reached by ransomware
- Honeypots and canary tokens: place deceptive artifacts in high-value locations — any access generates a high-confidence alert
- Data Loss Prevention (DLP): monitor and alert on large-volume data transfers, especially to external destinations
- User and Entity Behavior Analytics (UEBA): detect anomalous access patterns — a compromised account suddenly accessing hundreds of systems it has never touched is a clear signal

---

## The Kill Chain as a Defensive Planning Tool

The Kill Chain is most useful not as a checklist but as a planning framework. The exercise looks like this:

For each stage of the Kill Chain, ask three questions:

**1. What controls do we have that address attacker activity at this stage?**
Map your existing tools and processes to each stage. This gives you a visibility map of where you are covered and where you have gaps.

**2. If an attacker gets through this stage undetected, what is the next opportunity to catch them?**
Defense in depth means every stage is another chance. If your email controls miss a phishing payload, your endpoint detection should catch exploitation. If that misses, your network monitoring should catch C2 beaconing. Understanding your layered coverage helps you assess realistic detection scenarios.

**3. What would it take to disrupt this stage entirely for the most likely attacks against our organization?**
Some stages can be made very difficult for specific attack types. If your top threat is ransomware via phishing, investing heavily in email controls, endpoint behavioral detection, and privileged access management can disrupt the kill chain at stages 3, 4, and 7 simultaneously.

---

## Beyond the Kill Chain: The MITRE ATT&CK Framework

The Kill Chain is excellent for understanding attack progression at a high level, but it lacks the granularity needed for practical detection engineering and control mapping. MITRE ATT&CK was developed to fill that gap.

Where the Kill Chain gives you seven broad stages, ATT&CK gives you fourteen tactics and hundreds of specific techniques — each documented with real-world examples, detection guidance, and mitigation recommendations.

### The ATT&CK Tactics (Enterprise Matrix)

| Tactic | What It Represents |
|--------|-------------------|
| Reconnaissance | Information gathering before active attack |
| Resource Development | Acquiring infrastructure, capabilities, accounts for use in attacks |
| Initial Access | Gaining an initial foothold in the environment |
| Execution | Running attacker-controlled code on target systems |
| Persistence | Maintaining access across restarts, credential changes, and interruptions |
| Privilege Escalation | Gaining higher-level permissions |
| Defense Evasion | Avoiding detection by security tools and analysts |
| Credential Access | Stealing account credentials |
| Discovery | Learning about the environment (systems, users, network topology) |
| Lateral Movement | Moving through the environment to reach target systems |
| Collection | Gathering data of interest |
| Command and Control | Communicating with compromised systems |
| Exfiltration | Stealing data out of the environment |
| Impact | Manipulating, interrupting, or destroying systems or data |

### How ATT&CK Differs from the Kill Chain

The Kill Chain is a linear model — it assumes attacks move through stages sequentially. ATT&CK is a matrix model that reflects how attacks actually work in practice: tactics can be revisited, techniques can be combined, and sophisticated actors operate across multiple tactics simultaneously.

For example, an attacker who has established initial access may cycle through Defense Evasion, Discovery, and Privilege Escalation repeatedly before moving to Lateral Movement. ATT&CK captures that non-linear reality.

### Practical ATT&CK Usage

**Detection engineering:** Each ATT&CK technique includes detection guidance. When your SOC writes a detection rule, tag it with the relevant ATT&CK technique ID (e.g., T1059.001 for PowerShell execution). Over time, this creates a coverage map that shows which techniques you can detect and which have no current coverage.

**Threat hunting:** Use ATT&CK technique descriptions to inform hunting hypotheses. "Are there any scheduled tasks created by non-standard processes in the last 30 days?" is a hunt for T1053.005. ATT&CK gives you a structured library of what to look for.

**Purple team exercises:** When red and blue teams work together, ATT&CK provides a shared language for describing what techniques were used and whether detection and response worked as expected.

**Vendor evaluation:** When evaluating security tools, ask vendors which ATT&CK techniques their product detects. This gives you an objective framework for comparing coverage rather than relying on marketing claims.

**Starting point for small teams:** The ATT&CK Navigator (https://mitre-attack.github.io/attack-navigator/) is a free web tool that lets you visualize your coverage across the matrix. Color-code techniques by whether you have prevention, detection, or no coverage. Even a rough assessment is illuminating.

---

## The P > D + R Formula

One of the most useful conceptual frameworks for understanding security posture comes from incident response practitioners:

```
P > D + R
```

**Prevention Time > Detection Time + Response Time**

This formula states that for a security control to be effective, the time it takes an attacker to get through your prevention controls must be greater than the time it takes you to detect an intrusion and respond to it.

If an attacker can compromise a system in two hours, but your average detection time is 72 hours and your response time is another 24 hours — your controls have failed regardless of how good your prevention is on paper.

This framework has practical implications:

**Invest in detection, not just prevention.** No prevention is perfect. If your entire posture is prevention-focused and you have no meaningful detection capability, a single prevention failure becomes a catastrophic incident. Detection is what turns a major breach into a contained incident.

**Measure your actual detection and response times.** Most organizations do not know how long it would take them to detect a real intrusion. Tabletop exercises and red team engagements answer this question. The answer is almost always longer than expected.

**Reduce dwell time.** The time between initial compromise and detection is called dwell time. Industry data consistently shows that dwell time is measured in weeks to months for undetected intrusions. Every day of dwell time means more lateral movement, more persistence mechanisms, and a more complex remediation. Reducing dwell time is one of the highest-impact investments a security program can make.

---

## Common Attack Vectors Reference

Understanding the most common initial access vectors helps you prioritize where to focus preventive controls. The following table summarizes the most frequently observed initial access methods in real-world incident data.

| Attack Vector | Description | Primary Controls |
|---------------|-------------|-----------------|
| Phishing (email) | Malicious links or attachments delivered via email | Email filtering, attachment sandboxing, user training, DMARC/DKIM/SPF |
| Spear phishing | Targeted phishing using personalized lures | Same as phishing, plus executive awareness training |
| Credential stuffing | Using leaked credential pairs against login portals | MFA everywhere, rate limiting, breach credential monitoring |
| Exposed remote services | RDP, SSH, VPNs exposed to the internet | Eliminate unnecessary exposure, MFA, network access controls |
| Unpatched vulnerabilities | Known CVEs with available exploits | Patch management program, CISA KEV prioritization |
| Watering hole attacks | Compromising websites the target visits | Web proxy filtering, browser isolation, endpoint behavioral detection |
| Removable media | Malicious USBs or physical devices | USB port control policies, endpoint protection |
| Valid accounts | Using legitimate credentials obtained via phishing or purchase | MFA, privileged access management, credential monitoring |
| Supply chain compromise | Malicious code in software updates or dependencies | Software composition analysis, vendor security assessments |
| Insider action | Legitimate user deliberately or accidentally causing harm | Access controls, DLP, UEBA, security awareness |

---

## References

- Lockheed Martin Cyber Kill Chain: https://www.lockheedmartin.com/en-us/capabilities/cyber/cyber-kill-chain.html
- MITRE ATT&CK Enterprise Matrix: https://attack.mitre.org/matrices/enterprise/
- MITRE ATT&CK Navigator: https://mitre-attack.github.io/attack-navigator/
- MITRE ATT&CK Groups: https://attack.mitre.org/groups/
- CISA Known Exploited Vulnerabilities (KEV) Catalog: https://www.cisa.gov/known-exploited-vulnerabilities-catalog
- NIST SP 800-61 Rev.2 – Computer Security Incident Handling Guide: https://csrc.nist.gov/publications/detail/sp/800-61/rev-2/final
- Verizon Data Breach Investigations Report (DBIR) – Annual: https://www.verizon.com/business/resources/reports/dbir/
- Mandiant M-Trends Report – Annual: https://www.mandiant.com/m-trends
