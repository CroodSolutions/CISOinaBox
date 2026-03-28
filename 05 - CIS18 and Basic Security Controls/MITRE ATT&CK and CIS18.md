# CIS 18 Security Controls: A Strategic Planning Guide for the Modern Enterprise

Note that this guide was made with the help of Anthropic Opus 4.6, pointed to community resources as well as videos and presentations by the authors of the **CISOinaBox** project.  

**Important Note:** We thought it was important to include a few examples of vendors that are popular for each product category, as a place to start - in particular, for people who are new to any of these topics. That said, this is **NOT an Endoresement** of any particular compay or product. In fact, there are some companies here that I am not very fond of personally. 

## Anchored in MITRE ATT&CK Attack Flow Mapping

> *"The CIS Controls mitigate approximately 83% of all attack techniques found in the MITRE ATT&CK Framework, and 90% of ransomware techniques can be defended against by organizations that implement Implementation Group 1 alone."*
> — CIS Community Defense Model v2.0

---

## How to Use This Guide

This guide is designed for CISOs, security architects, and IT leaders who need to plan, prioritize, and execute a security controls strategy from the ground up. It walks through all 18 CIS Critical Security Controls (v8.1), maps them to MITRE ATT&CK tactics and techniques, identifies the specific solution categories you need to implement each control, and names the leading commercial and open-source brands in each category.

The structure follows a deliberate progression: you start with knowing what you have (Controls 1–2), move through protecting it (Controls 3–7), then into actively defending it (Controls 8–13), and finally into organizational maturity (Controls 14–18). This mirrors how real attacks unfold and how layered defenses must be constructed.

---

## Understanding the Two Frameworks

### CIS Controls v8.1

The CIS Critical Security Controls are a prioritized, prescriptive set of 18 controls organized into 153 individual Safeguards. They are structured into three Implementation Groups (IGs) based on organizational maturity:

- **IG1 — Essential Cyber Hygiene (56 Safeguards):** The minimum standard every organization should implement. Defends against the most common, non-targeted attacks. If you do nothing else, do IG1.
- **IG2 — Expanded Maturity (74 additional Safeguards):** For organizations with moderate IT complexity and dedicated security staff. Adds deeper configuration management, logging, and access controls.
- **IG3 — Advanced / Comprehensive (23 additional Safeguards):** For organizations facing sophisticated, targeted threats. Includes penetration testing, red teaming, and advanced data protection.

### MITRE ATT&CK

MITRE ATT&CK is a globally accessible knowledge base that catalogs adversary behavior across 14 Enterprise Tactics and hundreds of Techniques and Sub-Techniques. It is not a checklist — it is a model of how attackers actually operate. The tactics represent the "why" of an attack (the adversary's goal at each phase), while techniques represent the "how."

The 14 ATT&CK Enterprise Tactics, in rough kill-chain order:

1. **Reconnaissance** — Gathering information about the target
2. **Resource Development** — Building infrastructure and tooling
3. **Initial Access** — Getting a foothold in the network
4. **Execution** — Running malicious code
5. **Persistence** — Maintaining access across reboots and credential changes
6. **Privilege Escalation** — Gaining higher-level permissions
7. **Defense Evasion** — Avoiding detection
8. **Credential Access** — Stealing credentials
9. **Discovery** — Learning about the environment
10. **Lateral Movement** — Moving through the network
11. **Collection** — Gathering data of interest
12. **Command and Control (C2)** — Communicating with compromised systems
13. **Exfiltration** — Stealing data out of the environment
14. **Impact** — Disrupting, destroying, or manipulating systems and data

### The Strategic Connection

CIS Controls tell you *what to implement*. MITRE ATT&CK tells you *what you're defending against*. The CIS Community Defense Model formally maps every CIS Safeguard to the ATT&CK techniques it mitigates. This guide leverages that mapping to show you, for every control, exactly which phases of an attack you are disrupting.

---

## Attack Flow Mapping: How CIS Controls Disrupt the Kill Chain

A typical enterprise breach follows a predictable pattern. Here is how the CIS 18 controls layer together to break the attack at every stage:

### Phase 1: Reconnaissance & Initial Access
**ATT&CK Tactics:** Reconnaissance (TA0043), Resource Development (TA0042), Initial Access (TA0001)

The attacker scans for exposed assets, identifies unpatched vulnerabilities, crafts phishing emails, or purchases stolen credentials.

**Controls that disrupt this phase:**
- **CIS 1 (Asset Inventory)** — You cannot protect what you cannot see. Unknown, unmanaged assets are the #1 entry point.
- **CIS 2 (Software Inventory)** — Unauthorized software (shadow IT) creates unmonitored attack surface.
- **CIS 4 (Secure Configuration)** — Hardened configurations reduce the number of exploitable services.
- **CIS 7 (Continuous Vulnerability Management)** — Patched systems eliminate the vulnerabilities attackers scan for.
- **CIS 9 (Email and Web Browser Protections)** — Email is the most common initial access vector. Filtering, sandboxing, and browser isolation block phishing and drive-by downloads.
- **CIS 14 (Security Awareness Training)** — Trained users are the last line of defense against social engineering.

### Phase 2: Execution & Persistence
**ATT&CK Tactics:** Execution (TA0002), Persistence (TA0003)

The attacker runs malicious code — a macro, a PowerShell script, a trojan — and establishes mechanisms to survive reboots.

**Controls that disrupt this phase:**
- **CIS 2 (Software Inventory)** — Application allowlisting prevents unauthorized executables from running.
- **CIS 4 (Secure Configuration)** — Disabling macros, scripting engines, and unnecessary services removes execution vectors.
- **CIS 10 (Malware Defenses)** — Endpoint protection platforms (EPP) and endpoint detection and response (EDR) detect and block malicious execution.
- **CIS 8 (Audit Log Management)** — Process execution logging creates the trail needed to detect persistence mechanisms.

### Phase 3: Privilege Escalation & Credential Access
**ATT&CK Tactics:** Privilege Escalation (TA0004), Credential Access (TA0006)

The attacker escalates from a standard user to admin, dumps password hashes, steals tokens, or forges tickets.

**Controls that disrupt this phase:**
- **CIS 4 (Secure Configuration)** — Least-privilege configurations, removal of local admin rights, and disabling legacy authentication protocols.
- **CIS 5 (Account Management)** — Proper lifecycle management of accounts eliminates orphaned and over-privileged accounts.
- **CIS 6 (Access Control Management)** — Role-based access control, MFA enforcement, and privileged access management restrict what stolen credentials can do.

### Phase 4: Defense Evasion, Discovery & Lateral Movement
**ATT&CK Tactics:** Defense Evasion (TA0005), Discovery (TA0007), Lateral Movement (TA0008)

The attacker disables security tools, enumerates the network, and moves laterally to high-value targets — domain controllers, file servers, databases.

**Controls that disrupt this phase:**
- **CIS 12 (Network Infrastructure Management)** — Proper segmentation limits blast radius.
- **CIS 13 (Network Monitoring and Defense)** — NDR, IDS/IPS, and flow analysis detect lateral movement and C2 traffic.
- **CIS 8 (Audit Log Management)** — Centralized logging with tamper-proof storage detects tool disablement and anomalous discovery commands.
- **CIS 3 (Data Protection)** — Data classification and segmentation ensure that even after lateral movement, the crown jewels are isolated and encrypted.

### Phase 5: Collection, Exfiltration & Impact
**ATT&CK Tactics:** Collection (TA0009), Command and Control (TA0011), Exfiltration (TA0010), Impact (TA0040)

The attacker stages data, exfiltrates it over encrypted channels, deploys ransomware, or destroys systems.

**Controls that disrupt this phase:**
- **CIS 3 (Data Protection)** — DLP solutions detect and block large-scale data movement.
- **CIS 11 (Data Recovery)** — Immutable, tested backups are the ultimate defense against ransomware.
- **CIS 13 (Network Monitoring and Defense)** — DNS monitoring, SSL inspection, and egress filtering detect C2 and exfiltration.
- **CIS 17 (Incident Response Management)** — A tested IR plan ensures the organization can contain, eradicate, and recover quickly.
- **CIS 18 (Penetration Testing)** — Regular testing validates that all of the above actually works before an attacker tests it for you.

---

## The 18 Controls: Deep Dive with Solutions and Brands

Each section below follows a consistent structure: what the control requires, which ATT&CK techniques it primarily mitigates, the solution categories needed for implementation, and the leading brands in each category.

---

### CIS Control 1: Inventory and Control of Enterprise Assets

**What it requires:** Actively manage all enterprise assets connected to the infrastructure — physical, virtual, remote, and cloud — so you know the totality of what needs to be monitored and protected. Identify and remove unauthorized and unmanaged assets.

**ATT&CK Relevance:** Mitigates Reconnaissance (T1595), Initial Access via exposed assets (T1133, T1190), and Discovery techniques (T1082, T1018). You cannot detect an attacker on an asset you do not know exists.

**Implementation Group Progression:**
- **IG1:** Establish and maintain a detailed enterprise asset inventory, updated weekly. Use an active discovery tool to identify assets.
- **IG2:** Use DHCP logging to update the inventory. Ensure accuracy by reconciling with DNS, CMDB, and network scans.
- **IG3:** Use a passive discovery tool to identify assets on the network.

**Solution Categories and Leading Brands:**

| Solution Category | What It Does | Leading Brands |
|---|---|---|
| IT Asset Management (ITAM) | Central repository for all hardware and software assets | ServiceNow ITAM, Lansweeper, Armis, Axonius, Flexera |
| Network Discovery & Scanning | Active/passive scanning to find all devices on the network | Nmap, Masscan, Rumble/runZero, Qualys CSAM, Tenable.io |
| Cyber Asset Attack Surface Management (CAASM) | Aggregates data from multiple sources to build a unified asset view | Axonius, Armis, Sevco, JupiterOne, Panaseer |
| Cloud Asset Inventory | Discovers and inventories cloud resources across providers | AWS Config, Azure Resource Graph, Google Cloud Asset Inventory, Wiz |

**Implementation Tip:** Asset inventory is not a one-time project. It must be continuously maintained. Start with network scanning to find everything, then feed that into a CMDB or ITAM platform. Reconcile weekly. Any asset that appears on a scan but not in the inventory is either shadow IT or a compromised device — both demand immediate attention.

---

### CIS Control 2: Inventory and Control of Software Assets

**What it requires:** Actively manage all software on the network so that only authorized software is installed and can execute, and unauthorized software is found and prevented from installation or execution.

**ATT&CK Relevance:** Directly counters Execution tactics (T1204, T1059) and Persistence via trojaned software (T1554). Application allowlisting is one of the single most effective controls against malware execution.

**Solution Categories and Leading Brands:**

| Solution Category | What It Does | Leading Brands |
|---|---|---|
| Software Asset Management (SAM) | Tracks installed software, versions, and license compliance | Flexera, Snow Software, ServiceNow SAM |
| Application Control / Allowlisting | Prevents unauthorized executables from running | Microsoft AppLocker / WDAC, Carbon Black App Control, Airlock Digital, ThreatLocker |
| Endpoint Management / UEM | Deploys, patches, and manages software across endpoints | Microsoft Intune, Jamf, SCCM, NinjaOne |

**Implementation Tip:** Application allowlisting is often viewed as too difficult to implement broadly. Start in audit mode — log what would be blocked without actually blocking it. This builds your baseline. Then roll out enforcement to high-value targets (servers, privileged workstations) first, expanding from there.

---

### CIS Control 3: Data Protection

**What it requires:** Develop processes and technical controls to identify, classify, securely handle, retain, and dispose of data.

**ATT&CK Relevance:** Mitigates Collection (T1005, T1039, T1114), Exfiltration (T1041, T1048, T1567), and Impact (T1486 — ransomware encryption of sensitive data). Data protection is both a preventive and detective control.

**Solution Categories and Leading Brands:**

| Solution Category | What It Does | Leading Brands |
|---|---|---|
| Data Loss Prevention (DLP) | Monitors and blocks sensitive data from leaving the organization | Microsoft Purview DLP, Symantec DLP (Broadcom), Digital Guardian (Fortra), Netskope |
| Data Classification | Automatically identifies and labels sensitive data | Microsoft Purview Information Protection, SailPoint, HelpSystems, Varonis, BigID |
| Encryption (At Rest & In Transit) | Protects data through encryption | BitLocker, FileVault, VeraCrypt, Vormetric (Thales), AWS KMS, Azure Key Vault |
| Cloud Access Security Broker (CASB) | Controls data flow to and from cloud applications | Netskope, Microsoft Defender for Cloud Apps, Palo Alto Prisma Access, Zscaler |
| Data Discovery & Governance | Finds sensitive data across structured and unstructured repositories | Varonis, SailPoint, BigID, Spirion, Securiti |

---

### CIS Control 4: Secure Configuration of Enterprise Assets and Software

**What it requires:** Establish and maintain secure configurations for all enterprise assets and software, including hardened images, configuration baselines, and change management.

**ATT&CK Relevance:** Broadly mitigates Privilege Escalation (T1068, T1548), Persistence (T1053, T1547), and Defense Evasion (T1562). Misconfigurations are involved in the majority of breaches. Hardened configurations eliminate entire categories of attack techniques.

**Solution Categories and Leading Brands:**

| Solution Category | What It Does | Leading Brands |
|---|---|---|
| Configuration Management / Hardening | Automates baseline configuration and compliance checks | CIS-CAT Pro (CIS Benchmarks), Microsoft GPO / Intune, Chef, Puppet, Ansible |
| Cloud Security Posture Management (CSPM) | Detects misconfigurations in cloud infrastructure | Wiz, Prisma Cloud (Palo Alto), Microsoft Defender for Cloud, Orca Security |
| Vulnerability / Configuration Scanning | Identifies deviations from secure baselines | Tenable Nessus, Qualys VMDR, Rapid7 InsightVM |
| Image / Container Hardening | Ensures golden images and containers start from a secure baseline | CIS Hardened Images (marketplace images), Docker Bench, Aqua Security, Sysdig |

**Implementation Tip:** Use CIS Benchmarks as your configuration baseline — they are consensus-developed, freely available, and map directly to ATT&CK. Automate compliance checking with tools like CIS-CAT, then enforce drift detection through your configuration management platform.

---

### CIS Control 5: Account Management

**What it requires:** Use processes and tools to assign and manage authorization to credentials for user accounts, including administrator accounts and service accounts.

**ATT&CK Relevance:** Mitigates Credential Access (T1078 — Valid Accounts, T1098 — Account Manipulation), Persistence (T1136 — Create Account), and Privilege Escalation via account abuse. Orphaned and over-privileged accounts are among the most exploited attack surfaces.

**Solution Categories and Leading Brands:**

| Solution Category | What It Does | Leading Brands |
|---|---|---|
| Identity Governance & Administration (IGA) | Manages account lifecycle: provisioning, review, deprovisioning | SailPoint, Saviynt, Microsoft Entra ID Governance, One Identity |
| Privileged Access Management (PAM) | Secures, rotates, and audits privileged account usage | CyberArk, BeyondTrust, Delinea (Thycotic/Centrify), HashiCorp Vault |
| Directory Services | Central identity store and authentication | Microsoft Entra ID (Azure AD), Okta, Ping Identity |

---

### CIS Control 6: Access Control Management

**What it requires:** Use processes and tools to create, assign, manage, and revoke access credentials and privileges for user, administrator, and service accounts.

**ATT&CK Relevance:** Mitigates Lateral Movement (T1021 — Remote Services), Privilege Escalation (T1078), and Initial Access (T1078 — Valid Accounts with stolen credentials). MFA alone blocks the vast majority of credential-stuffing and password-spray attacks.

**Solution Categories and Leading Brands:**

| Solution Category | What It Does | Leading Brands |
|---|---|---|
| Multi-Factor Authentication (MFA) | Requires second factor for authentication | Microsoft Entra MFA, Duo (Cisco), Okta Verify, YubiKey (Yubico), PingID |
| Single Sign-On (SSO) | Centralizes authentication to reduce credential sprawl | Okta, Microsoft Entra ID, Ping Identity, OneLogin |
| Zero Trust Network Access (ZTNA) | Replaces VPN with identity-aware, least-privilege access | Zscaler Private Access, Palo Alto Prisma Access, Cloudflare Access, Netskope |
| Privileged Access Management (PAM) | Controls and audits privileged sessions | CyberArk, BeyondTrust, Delinea |

---

### CIS Control 7: Continuous Vulnerability Management

**What it requires:** Develop a plan to continuously assess and track vulnerabilities on all enterprise assets to remediate and minimize the window of opportunity for attackers.

**ATT&CK Relevance:** Directly counters Initial Access (T1190 — Exploit Public-Facing Application), Privilege Escalation (T1068 — Exploitation for Privilege Escalation), and Execution (T1203 — Exploitation for Client Execution). Unpatched vulnerabilities remain the most common technical root cause of breaches.

**Solution Categories and Leading Brands:**

| Solution Category | What It Does | Leading Brands |
|---|---|---|
| Vulnerability Scanning | Discovers and prioritizes vulnerabilities across assets | Tenable Nessus / Tenable One, Qualys VMDR, Rapid7 InsightVM, Microsoft Defender Vulnerability Management |
| Patch Management | Automates deployment of patches to endpoints and servers | Microsoft SCCM/Intune/WSUS, Ansible, ManageEngine Patch Manager Plus, Automox |
| Risk-Based Vulnerability Prioritization | Correlates vulnerability data with threat intelligence and asset context | Tenable Vulnerability Priority Rating (VPR), Qualys TruRisk, Kenna.vm (Cisco) |

**Implementation Tip:** Vulnerability management is not the same as vulnerability scanning. Scanning finds problems; management fixes them. The critical success factor is operationalizing remediation — assigning owners, setting SLAs tied to severity, and measuring mean time to remediate (MTTR). Aim for critical vulnerabilities patched within 48 hours, high within 7 days, and medium within 30 days.

---

### CIS Control 8: Audit Log Management

**What it requires:** Collect, alert, review, and retain audit logs of events that could help detect, understand, or recover from an attack.

**ATT&CK Relevance:** This is the foundational detection control. It enables visibility into nearly every ATT&CK tactic from Execution through Impact. Specifically critical for detecting Defense Evasion (T1562 — Impair Defenses / Disable Logging), Discovery (T1087, T1069), and Credential Access (T1003 — OS Credential Dumping). Without logs, attackers operate invisibly.

**Solution Categories and Leading Brands:**

| Solution Category | What It Does | Leading Brands |
|---|---|---|
| Security Information and Event Management (SIEM) | Aggregates, correlates, and alerts on security events | Splunk, Microsoft Sentinel,  Elastic Security, Google Chronicle, LogRhythm, IBM QRadar |
| Log Management / Data Lake | Scalable storage and search for high-volume log data | Cribl (log routing), Elastic, Splunk, Datadog, Sumo Logic |
| SOAR (Security Orchestration, Automation and Response) | Automates triage, enrichment, and response workflows | Palo Alto XSOAR, Splunk SOAR, Swimlane, Tines |

**Implementation Tip:** The most common SIEM failure is collecting too much data without knowing what you are looking for. Start with use cases mapped to ATT&CK techniques: failed authentication attempts (T1110), process creation events (T1059), suspicious PowerShell (T1059.001), new service installations (T1543), and log clearing events (T1070). Build detection rules for these first, then expand.

---

### CIS Control 9: Email and Web Browser Protections

**What it requires:** Improve protections and detections of threats from email and web vectors, as these are the most common entry points for attacks.

**ATT&CK Relevance:** Directly mitigates Initial Access (T1566 — Phishing, T1189 — Drive-By Compromise), Execution (T1204 — User Execution), and Command and Control (T1071 — Web Protocols). Phishing is the #1 initial access vector across virtually all threat reports.

**Solution Categories and Leading Brands:**

| Solution Category | What It Does | Leading Brands |
|---|---|---|
| Secure Email Gateway (SEG) | Filters phishing, malware, and spam before delivery | Microsoft Defender for Office 365, Proofpoint, Mimecast, Abnormal Security |
| Browser Isolation | Executes web content in a sandboxed environment | Menlo Security, Zscaler Browser Isolation, Island Enterprise Browser |
| DNS Filtering | Blocks connections to known malicious domains | Cisco Umbrella, Cloudflare Gateway, Infoblox BloxOne, DNSFilter |
| URL Filtering / Secure Web Gateway (SWG) | Inspects and controls web traffic | Zscaler Internet Access, Palo Alto Prisma Access, Netskope, Cisco Secure Web Appliance |

---

### CIS Control 10: Malware Defenses

**What it requires:** Prevent or control the installation, spread, and execution of malicious applications, code, or scripts on enterprise assets.

**ATT&CK Relevance:** Core defense against Execution (T1059, T1204), Persistence (T1547 — Boot or Logon Autostart Execution), Defense Evasion (T1027 — Obfuscated Files), and Impact (T1486 — Data Encrypted for Impact / Ransomware).

**Solution Categories and Leading Brands:**

| Solution Category | What It Does | Leading Brands |
|---|---|---|
| Endpoint Detection and Response (EDR) | Real-time monitoring, detection, and response on endpoints | CrowdStrike Falcon, Elastic Agent EDR, Huntress, Microsoft Defender for Endpoint, SentinelOne, Palo Alto Cortex XDR |
| Extended Detection and Response (XDR) | Correlates telemetry across endpoint, network, cloud, and email | CrowdStrike Falcon, Microsoft Defender XDR, Palo Alto Cortex XDR, Trend Micro Vision One |
| Next-Gen Antivirus (NGAV) | Behavioral and ML-based malware prevention | CrowdStrike, SentinelOne, Carbon Black (VMware/Broadcom), Microsoft Defender |
| Sandboxing / Detonation | Executes suspicious files in isolated environments for analysis | Palo Alto WildFire, CrowdStrike Falcon Sandbox, Joe Sandbox, ANY.RUN |

**Implementation Tip:** Traditional antivirus is dead. Modern malware defenses require EDR at minimum, which provides behavioral detection, memory analysis, and response capabilities. The strategic evolution is toward XDR, which unifies detection across endpoints, network, cloud, and identity into a single correlated view. If you are evaluating a new platform, buy XDR — you will get EDR capabilities as part of it.

---

### CIS Control 11: Data Recovery

**What it requires:** Establish and maintain data recovery practices sufficient to restore enterprise assets to a pre-incident and trusted state.

**ATT&CK Relevance:** The primary defense against Impact (T1486 — Data Encrypted for Impact, T1485 — Data Destruction, T1490 — Inhibit System Recovery). Ransomware is an existential business risk; immutable backups are the insurance policy.

**Solution Categories and Leading Brands:**

| Solution Category | What It Does | Leading Brands |
|---|---|---|
| Enterprise Backup & Recovery | Automated backup with rapid recovery capabilities | Veeam, Commvault, Cohesity, Rubrik, Veritas |
| Immutable / Air-Gapped Backup | Prevents ransomware from encrypting or deleting backup data | Rubrik, Cohesity, AWS S3 Object Lock, Azure Immutable Blob Storage |
| Disaster Recovery as a Service (DRaaS) | Cloud-based failover for business continuity | Zerto, Veeam, Azure Site Recovery, AWS Elastic Disaster Recovery |

**Implementation Tip:** The 3-2-1-1-0 rule: maintain 3 copies of data, on 2 different media types, with 1 offsite, 1 immutable/air-gapped, and 0 errors in recovery testing. Test restores quarterly at minimum. A backup you have never tested is not a backup — it is a hope.

---

### CIS Control 12: Network Infrastructure Management

**What it requires:** Establish, implement, and actively manage network devices to prevent attackers from exploiting vulnerable network services and access points.

**ATT&CK Relevance:** Mitigates Lateral Movement (T1021, T1210 — Exploitation of Remote Services), Initial Access via exposed network services (T1133 — External Remote Services), and Defense Evasion through network-level manipulation.

**Solution Categories and Leading Brands:**

| Solution Category | What It Does | Leading Brands |
|---|---|---|
| Next-Generation Firewall (NGFW) | Application-aware, identity-aware perimeter and internal filtering | Palo Alto Networks, Fortinet FortiGate, Cisco Secure Firewall, Check Point |
| Network Access Control (NAC) | Enforces device health and identity before granting network access | Cisco ISE, Aruba ClearPass, Forescout, Portnox |
| Microsegmentation | Enforces granular, workload-level network policies | Illumio, Guardicore (Akamai), VMware NSX, Zscaler Workload Communications |
| SD-WAN / SASE | Secure, optimized WAN connectivity with integrated security | Zscaler, Palo Alto Prisma SASE, Fortinet Secure SD-WAN, Cato Networks |
| Network Configuration Management | Automates and audits network device configurations | Cisco DNA Center, Arista CloudVision, BackBox, SolarWinds NCM |

**Implementation Tip:** Network segmentation is the single most impactful control for limiting lateral movement. At minimum, segment the network into trust zones: user endpoints, servers, production databases, management networks, IoT/OT, and DMZ. The evolution beyond VLANs is microsegmentation, which enforces identity-based policies at the workload level regardless of network topology.

---

### CIS Control 13: Network Monitoring and Defense

**What it requires:** Operate processes and tooling to establish and maintain comprehensive network monitoring and defense against security threats.

**ATT&CK Relevance:** The primary detective control for Command and Control (T1071, T1095, T1573), Lateral Movement (T1021, T1210), Exfiltration (T1041, T1048), and Defense Evasion (T1090 — Proxy). This is where you catch attackers who have evaded endpoint controls.

**Solution Categories and Leading Brands:**

| Solution Category | What It Does | Leading Brands |
|---|---|---|
| Network Detection and Response (NDR) | Analyzes network traffic for threats using AI/ML and behavioral analysis | Darktrace, ExtraHop Reveal(x), Vectra AI, Cisco Secure Network Analytics (Stealthwatch) |
| Intrusion Detection / Prevention (IDS/IPS) | Signature and anomaly-based detection of malicious traffic | Snort (open source), Suricata (open source), Palo Alto (integrated in NGFW), Cisco Secure IPS |
| Network Traffic Analysis (NTA) / Flow Analysis | Deep visibility into traffic patterns and anomalies | Kentik, NetFlow (Cisco), ExtraHop, Elastic |
| SSL/TLS Inspection | Decrypts and inspects encrypted traffic for threats | Palo Alto NGFW, Zscaler, F5, Gigamon |
| DNS Security | Monitors and blocks malicious DNS activity | Cisco Umbrella, Infoblox BloxOne Threat Defense, Cloudflare Gateway |

---

### CIS Control 14: Security Awareness and Skills Training

**What it requires:** Establish and maintain a security awareness program to influence behavior among the workforce to be security conscious and properly skilled to reduce cybersecurity risks.

**ATT&CK Relevance:** Mitigates Initial Access (T1566 — Phishing, T1598 — Phishing for Information), Execution (T1204 — User Execution), and the entire social engineering dimension of ATT&CK. Humans remain the most targeted and most exploitable vector.

**Solution Categories and Leading Brands:**

| Solution Category | What It Does | Leading Brands |
|---|---|---|
| Security Awareness Training Platforms | Delivers training content, phishing simulations, and compliance tracking | KnowBe4, Proofpoint Security Awareness, SANS Security Awareness, Cofense |
| Phishing Simulation | Tests employees with realistic phishing campaigns | KnowBe4, Cofense PhishMe, Proofpoint, Hoxhunt |

---

### CIS Control 15: Service Provider Management

**What it requires:** Develop a process to evaluate service providers who hold sensitive data or are responsible for critical IT platforms, ensuring they are protecting those platforms and data appropriately.

**ATT&CK Relevance:** Mitigates Initial Access (T1199 — Trusted Relationship) and the entire supply chain attack surface (T1195 — Supply Chain Compromise). The SolarWinds, Kaseya, and MOVEit attacks demonstrated that third-party compromise is a primary intrusion vector for sophisticated adversaries.

**Solution Categories and Leading Brands:**

| Solution Category | What It Does | Leading Brands |
|---|---|---|
| Third-Party Risk Management (TPRM) | Assesses and monitors vendor security posture | BitSight, SecurityScorecard, Prevalent, OneTrust |
| Vendor Risk Assessment Platforms | Manages questionnaires, audits, and compliance documentation | OneTrust, Archer (RSA), ServiceNow VRM, Vanta |
| Supply Chain Security | Monitors for compromises in the software supply chain | Sonatype Nexus, Snyk, Socket, Chainguard |

---

### CIS Control 16: Application Software Security

**What it requires:** Manage the security lifecycle of in-house developed, hosted, or acquired software to prevent, detect, and remediate security weaknesses.

**ATT&CK Relevance:** Mitigates Initial Access (T1190 — Exploit Public-Facing Application), Execution (T1203), and the broader class of application-layer attacks. Web applications are the most common target for external attackers after email.

**Solution Categories and Leading Brands:**

| Solution Category | What It Does | Leading Brands |
|---|---|---|
| Static Application Security Testing (SAST) | Analyzes source code for vulnerabilities | SonarQube, Checkmarx, Veracode, Semgrep |
| Dynamic Application Security Testing (DAST) | Tests running applications for vulnerabilities | Burp Suite (PortSwigger), OWASP ZAP (open source), Invicti, HCL AppScan |
| Software Composition Analysis (SCA) | Identifies vulnerabilities in open-source dependencies | Snyk, Sonatype, Black Duck (Synopsys), Mend.io |
| Web Application Firewall (WAF) | Filters and blocks malicious HTTP traffic | Cloudflare WAF, AWS WAF, Akamai, Imperva |
| Runtime Application Self-Protection (RASP) | Detects and blocks attacks from within the application | Contrast Security, Imperva, Signal Sciences (Fastly) |

---

### CIS Control 17: Incident Response Management

**What it requires:** Establish a program to develop and maintain an incident response capability — policies, plans, procedures, defined roles, training, and communications — to prepare, detect, and quickly respond to an attack.

**ATT&CK Relevance:** This control spans the entire ATT&CK matrix. Incident response is the organizational capability that ties together every detective and responsive control. Without it, detection is meaningless — you see the alert but cannot act on it.

**Solution Categories and Leading Brands:**

| Solution Category | What It Does | Leading Brands |
|---|---|---|
| SIEM (see Control 8) | Detection and investigation platform | Splunk, Microsoft Sentinel, Elastic Security, Google Chronicle |
| SOAR (see Control 8) | Automates playbook execution and response orchestration | Palo Alto XSOAR, Splunk SOAR, Swimlane, Tines |
| Incident Response Retainers | On-call expert responders for major incidents | CrowdStrike Services, Mandiant (Google), Secureworks, Unit 42 (Palo Alto) |
| Forensics & Investigation Tools | Deep analysis of compromised systems | Magnet AXIOM, Velociraptor (open source), X-Ways, EnCase (OpenText) |
| Threat Intelligence Platforms (TIP) | Enriches alerts with context on threat actors and IOCs | Recorded Future, Mandiant Threat Intelligence, ThreatConnect, MISP (open source) |
| Case Management | Tracks incidents from detection through resolution | TheHive (open source), ServiceNow SecOps, PagerDuty |

**Implementation Tip:** Your IR plan must be tested before you need it. Run tabletop exercises quarterly and full technical simulations annually. The exercise should involve not just the security team but also legal, communications, executive leadership, and IT operations. The worst time to discover that your plan has gaps is during a real incident.

---

### CIS Control 18: Penetration Testing

**What it requires:** Test the effectiveness and resiliency of enterprise assets through identifying and exploiting weaknesses in controls (people, processes, and technology), and simulating the objectives and actions of an attacker.

**ATT&CK Relevance:** Penetration testing validates the effectiveness of every other control by simulating real adversary behavior across the full ATT&CK matrix. Red teams specifically map their operations to ATT&CK techniques to measure defensive coverage.

**Solution Categories and Leading Brands:**

| Solution Category | What It Does | Leading Brands |
|---|---|---|
| Penetration Testing Services | Expert-led testing of networks, applications, and people | Bishop Fox, SecurIT360, Rapid7, NetSPI, Coalfire, Cobalt |
| Breach and Attack Simulation (BAS) | Continuous, automated testing of security controls | AttackIQ, SafeBreach, Cymulate, Picus Security |
| Red Team / Adversary Emulation | Simulates real threat actor TTPs against the environment | MITRE Caldera (open source), Atomic Red Team (open source), Cobalt Strike (Fortra), Brute Ratel, BeaconatorC2 |
| Attack Surface Management (ASM) | Discovers and tests the external attack surface continuously | Censys, Ionix, Shodan, Mandiant ASM, CrowdStrike Falcon Surface |

**Implementation Tip:** Breach and Attack Simulation (BAS) platforms are the force multiplier that connects CIS 18 to MITRE ATT&CK operationally. These tools continuously simulate specific ATT&CK techniques against your production environment and tell you, per technique, whether your SIEM detected it, whether your EDR blocked it, and whether your firewall filtered it. This gives you a quantifiable coverage map: "We detect 78% of ATT&CK techniques. Here are the 22% where we have gaps." That drives your investment roadmap.

---

## Building Your Strategy: A Phased Implementation Roadmap

### Phase 1: Foundation (Months 1–3) — IG1 Essentials
Focus on the controls that provide the most risk reduction with the least complexity:

1. **Asset & Software Inventory (CIS 1, 2):** Deploy a scanning tool (runZero, Nmap) and establish a living inventory.
2. **Secure Configuration (CIS 4):** Apply CIS Benchmarks to all systems. Automate with GPO, Intune, or Ansible.
3. **Account Management & MFA (CIS 5, 6):** Enforce MFA everywhere, especially on admin accounts and remote access. Deploy a PAM solution for privileged accounts.
4. **Malware Defenses (CIS 10):** Deploy EDR to all endpoints. CrowdStrike, SentinelOne, or Microsoft Defender for Endpoint.
5. **Data Recovery (CIS 11):** Implement immutable backups. Test restores.
6. **Security Awareness (CIS 14):** Launch phishing simulations and basic training.

### Phase 2: Visibility & Detection (Months 4–8) — IG2
Build the detection and monitoring layer:

7. **Audit Log Management (CIS 8):** Deploy or tune SIEM. Start with ATT&CK-mapped detection rules for the top 20 techniques.
8. **Vulnerability Management (CIS 7):** Deploy continuous scanning. Establish SLA-based remediation workflows.
9. **Email & Web Protections (CIS 9):** Harden email with SPF/DKIM/DMARC, deploy SEG and DNS filtering.
10. **Network Monitoring (CIS 13):** Deploy NDR or IDS on critical network segments. Implement DNS monitoring.
11. **Network Infrastructure (CIS 12):** Segment the network. Deploy or harden NGFW rules. Implement NAC.

### Phase 3: Maturity & Resilience (Months 9–12) — IG3
Advance into proactive and organizational controls:

12. **Data Protection (CIS 3):** Deploy DLP and data classification. Implement encryption at rest for sensitive data stores.
13. **Application Security (CIS 16):** Integrate SAST/DAST into CI/CD pipelines. Deploy WAF for public-facing apps.
14. **Service Provider Management (CIS 15):** Assess critical vendors. Establish continuous monitoring with a TPRM platform.
15. **Incident Response (CIS 17):** Formalize IR plan. Deploy SOAR. Run tabletop exercises.
16. **Penetration Testing (CIS 18):** Conduct initial pen test. Deploy BAS for continuous validation.

### Phase 4: Continuous Optimization (Ongoing)
- Map BAS results to ATT&CK coverage gaps. Invest in controls that close the biggest gaps.
- Revisit and harden configurations as new CIS Benchmarks are released.
- Conduct annual red team exercises with ATT&CK-mapped objectives.
- Maintain and update the asset inventory weekly. Drift detection is a continuous process.
- Review and update the IR plan after every exercise and real incident.

---

## Putting It All Together: The Integrated Defense Architecture

The strategic insight is that no single control stands alone. They form an integrated system where each layer compensates for the gaps in the others:

- **Prevent:** Controls 1, 2, 4, 5, 6, 7, 9, 10, 12, 14, 16 reduce the attack surface and block initial exploitation.
- **Detect:** Controls 8, 10, 13 provide real-time visibility into attacker activity that evades preventive controls.
- **Respond:** Controls 11, 17 ensure the organization can contain the damage and recover.
- **Validate:** Controls 18 continuously test whether the Prevent-Detect-Respond chain actually works.

When mapped to a real attack flow — say, a phishing email leading to credential theft, lateral movement, and ransomware deployment — every stage of the kill chain encounters resistance from multiple, overlapping controls. The attacker has to defeat all of them. The defender only has to win at one.

---

## Key Resources

- **CIS Controls v8.1 Download:** [cisecurity.org/controls](https://www.cisecurity.org/controls)
- **CIS Controls Navigator (mappings to NIST, ISO, HIPAA, etc.):** [cisecurity.org/controls/cis-controls-navigator](https://www.cisecurity.org/controls/cis-controls-navigator)
- **CIS Community Defense Model v2.0:** [cisecurity.org/insights/white-papers](https://www.cisecurity.org/insights/white-papers)
- **MITRE ATT&CK Enterprise Matrix:** [attack.mitre.org](https://attack.mitre.org)
- **CISA Best Practices for MITRE ATT&CK Mapping:** [cisa.gov](https://www.cisa.gov/sites/default/files/2023-01/Best%20Practices%20for%20MITRE%20ATTCK%20Mapping.pdf)
- **CISO in a Box — CIS18 Module:** [github.com/CroodSolutions/CISOinaBox](https://github.com/CroodSolutions/CISOinaBox/tree/main/05%20-%20CIS18%20and%20Basic%20Security%20Controls)
- **CIS18 Video Walkthrough (Crood Solutions):** [youtu.be/3HQPMbO3Mgw](https://youtu.be/3HQPMbO3Mgw)

---

*This guide is designed to be a living document. As your organization matures, revisit each control, upgrade your implementation group, and continuously validate effectiveness through ATT&CK-mapped testing. The threat landscape evolves; your defenses must evolve with it.*

