# Supplemental: Frameworks for Defending Against Attacks — PICERL, MITRE, and Beyond

*This document is a technical companion to Chapter 03 – Understanding the Adversary. It covers the primary frameworks security teams use to organize their defensive operations — from incident response to threat intelligence to security program structure.*

---

## Why Frameworks Matter (And Why They Are Not the Goal)

Frameworks are organizing tools, not destinations. The goal is a security program that detects threats, responds effectively, and reduces risk to the organization. Frameworks give you a common language, a structured way to assess gaps, and a reference point for communicating program maturity to leadership.

The mistake most organizations make is treating a framework as a compliance checkbox rather than a practical guide. This document covers the most useful frameworks for a working security team — with emphasis on how to actually apply them, not just what they are.

---

## PICERL — The Incident Response Lifecycle

PICERL is the most widely used framework for structuring how security teams respond to incidents. The acronym stands for: **Preparation, Identification, Containment, Eradication, Recovery, and Lessons Learned.**

It was formalized in NIST SP 800-61 (Computer Security Incident Handling Guide) and is the foundation of virtually every incident response program. If you have a SOC or an incident response capability, your processes map to this framework whether you have formalized it that way or not.

### Phase 1: Preparation

Preparation is everything you do before an incident happens to ensure you can respond effectively when one does. This is the phase most organizations underinvest in — until they have a bad incident.

**What preparation actually means in practice:**

- **Incident Response Plan (IRP):** A documented plan that defines what constitutes an incident, who is responsible for what, how decisions get made, and how communication flows internally and externally. The plan should be tested — a plan that has never been exercised is a document, not a capability.
- **Contact lists and escalation paths:** Who gets called at 2 AM when ransomware is deploying? Do you have current mobile numbers for IT leadership, legal counsel, your cyber insurance carrier, and external IR retainer contacts? This sounds basic. Most organizations cannot answer all of these questions during an actual incident.
- **Tooling:** EDR deployed across endpoints, SIEM ingesting logs from critical systems, network detection and response (NDR) or at minimum firewall/DNS logs. You cannot respond to what you cannot see.
- **Playbooks:** Scenario-specific response guides for your most likely incident types — ransomware, BEC/wire fraud, data exfiltration, insider threat. Each playbook should define the specific steps, owners, and decision points for that scenario.
- **Tabletop exercises:** Walk your team and relevant stakeholders (Legal, Finance, Communications, executive leadership) through realistic scenarios at least annually. Tabletops surface gaps in your plan before a real incident does.
- **External retainer:** If your organization does not have internal IR capability, having a retainer with an external IR firm means they already have your environment documentation and can mobilize faster when you need them.

**What good looks like:** Your team can answer "what would we do in the first hour of a ransomware incident?" with a specific, step-by-step answer — not a general concept.

---

### Phase 2: Identification

Identification is the process of detecting that an incident has occurred and confirming that it is real. This includes the initial triage to determine the scope, nature, and severity of the incident.

**What identification actually means in practice:**

- **Alert triage:** Your SIEM, EDR, or other detection tool fires an alert. The first question is: is this a true positive or a false positive? Effective triage requires documented criteria for escalation and a team that has seen enough alerts to make that judgment quickly.
- **Scope assessment:** Once an alert is confirmed as a true positive, the next question is: how far has this gone? Is this a single compromised endpoint, or are there indicators of lateral movement? Is data potentially involved? The answers drive containment urgency.
- **Severity classification:** Not all incidents are equal. A formal severity classification scheme (P1 through P4, or Critical/High/Medium/Low) ensures the right level of response is mobilized. A single malware infection on an isolated endpoint is not the same incident as active ransomware deployment on your production environment.
- **Documentation from the start:** Every action taken, every artifact observed, and every decision made should be logged in real time. This becomes your incident timeline, your evidence chain, and the foundation of your lessons learned.

**Common failure point:** Organizations often struggle here because they have too many alerts and too little context. High-volume, low-fidelity alerts lead to alert fatigue, which leads to real incidents being missed. Reducing alert noise and improving alert quality is an ongoing operational priority.

**Key questions to answer during identification:**
- What systems are affected?
- What data may be involved?
- Is the attacker still active in the environment?
- What is the likely initial access vector?
- Is this contained to one system or has lateral movement occurred?

---

### Phase 3: Containment

Containment stops the spread of the incident without necessarily removing the threat entirely. There are two types: short-term containment (stopping the bleeding immediately) and long-term containment (stabilizing the environment while full eradication is prepared).

**Short-term containment actions:**
- Isolate affected systems from the network (while maintaining forensic access — do not power systems off without guidance from your IR team)
- Block identified malicious IP addresses, domains, and file hashes at the perimeter and endpoint
- Disable compromised user accounts (do not delete them — they are evidence)
- Revoke or rotate credentials for accounts that may have been exposed
- Notify your cyber insurance carrier and legal counsel if the incident crosses defined thresholds — timing of notification matters for coverage

**Long-term containment actions:**
- Deploy additional monitoring on systems adjacent to confirmed compromised hosts
- Implement enhanced logging on privileged accounts and critical systems
- Restrict access to sensitive systems to a minimum set of users while the investigation continues
- Preserve forensic evidence: memory captures, disk images, log exports before they roll over

**Critical considerations:**
- Do not tip off the attacker that they have been detected before you are ready to contain. In some cases, maintaining the attacker's access temporarily while you complete forensics and prepare a coordinated containment action is better than premature partial containment that causes them to accelerate.
- Legal and regulatory notification obligations may be triggered during containment. Involve Legal early.
- Communication discipline: limit knowledge of the incident to those who need to know during containment. Premature broad communication creates confusion, leaks to media, and can alert the attacker.

---

### Phase 4: Eradication

Eradication removes the threat from the environment entirely. This means removing all malware, backdoors, persistence mechanisms, and attacker-controlled accounts — not just the obvious ones.

**What eradication actually means in practice:**

- **Complete forensic investigation before eradication.** You need to understand the full scope of what the attacker did and what they left behind before you start cleaning. Premature eradication destroys evidence and risks missing persistence mechanisms that will cause re-compromise.
- **Rebuild compromised systems.** For systems where you have confirmed compromise, rebuilding from known-good images is almost always preferable to attempting to clean the existing system. You cannot be certain you have found everything.
- **Patch the vulnerability that was exploited.** Eradicating the attacker while leaving the entry point open invites immediate re-compromise.
- **Credential rotation.** Any credentials that were or may have been exposed must be rotated. In a domain-wide compromise, this may mean rotating all privileged credentials, including service accounts and the krbtgt account.
- **Review for additional persistence.** Check scheduled tasks, registry run keys, startup scripts, new user accounts, modified group policies, and web shells. Sophisticated attackers plant multiple persistence mechanisms — finding and removing one does not mean you have found them all.

**Common failure point:** Organizations rush eradication because of pressure to restore operations. Incomplete eradication leads to re-compromise — often within days. Resist the pressure. A slightly longer eradication that is complete is far better than a fast one that is not.

---

### Phase 5: Recovery

Recovery restores affected systems and services to normal operations while maintaining heightened monitoring to confirm that eradication was complete and re-compromise has not occurred.

**What recovery actually means in practice:**

- **Phased restoration:** Do not restore everything at once. Bring systems back in a controlled sequence, starting with the least sensitive, and verify clean operation before proceeding.
- **Monitoring during recovery:** Maintain elevated logging and alerting during the recovery period. If the attacker has any remaining access, they may attempt to re-establish persistence once they see systems coming back online.
- **Stakeholder communication:** Business leadership, customer-facing teams, and (where required) regulatory bodies and customers need to be informed of the recovery timeline and status. Communication during recovery should be accurate, measured, and coordinated with Legal and Communications.
- **Define return-to-normal criteria:** What does "recovered" actually mean? Define it explicitly: all affected systems rebuilt and restored from clean backups, no malicious indicators detected for 72 hours, all credentials rotated, vulnerability patched, monitoring baseline re-established.

---

### Phase 6: Lessons Learned

Lessons learned is the phase most organizations skip entirely — and the one that determines whether the same incident happens again.

**What lessons learned actually means in practice:**

- **Conduct a formal post-incident review within two weeks** while the incident is still fresh. Include IR team members, IT operations, relevant business stakeholders, and leadership.
- **Answer these questions without blame assignment:**
  - What happened, and how did the attacker get in?
  - How long were they in before detection?
  - What detection controls worked? What failed?
  - What in our response went well? What slowed us down?
  - What would have prevented this incident?
  - What would have allowed us to detect it sooner?
- **Convert findings into action items** with owners and deadlines. A lessons learned session that produces a report no one acts on is theater.
- **Update your IR plan and playbooks** based on what you learned. Your plan should be a living document that improves after every incident.
- **Brief leadership.** A clear, business-focused summary of what happened, what it cost, and what changes are being made is both appropriate governance and an opportunity to build the case for security investments.

---

## MITRE ATT&CK in Depth

MITRE ATT&CK was introduced in Chapter 03 as a practical tool for defenders. This section goes deeper on how to operationalize it within a working security program.

### The Three ATT&CK Matrices

ATT&CK maintains separate matrices for different environments:

**Enterprise:** The most comprehensive matrix, covering Windows, macOS, Linux, cloud (AWS, Azure, GCP, Office 365, Google Workspace), containers, and network infrastructure. This is the primary reference for most organizations.

**Mobile:** Covers Android and iOS attack techniques. Relevant for organizations with significant mobile device management requirements or mobile application security concerns.

**ICS (Industrial Control Systems):** Covers attack techniques specific to operational technology (OT) and industrial environments. Relevant for manufacturing, utilities, energy, and critical infrastructure operators.

For most organizations, Enterprise is the starting point. ICS becomes relevant if you operate production control systems, SCADA, or other OT infrastructure.

### Understanding the ATT&CK Data Model

Each entry in ATT&CK follows a consistent structure that makes it actionable:

**Tactic:** The adversary's tactical goal — the "why" of a specific action. Tactics are the columns in the ATT&CK matrix. Example: Persistence.

**Technique:** The general method used to achieve the tactic. Example: T1053 – Scheduled Task/Job.

**Sub-technique:** A more specific implementation of a technique. Example: T1053.005 – Scheduled Task (Windows Task Scheduler specifically). Sub-techniques allow for more precise detection rule writing and more granular coverage assessment.

**Procedure:** A specific, real-world observed instance of a technique being used by a particular threat actor. Procedures are documented in the group and software pages.

**Mitigations:** ATT&CK documents recommended mitigations for each technique. These map to security controls and configurations that reduce technique effectiveness.

**Detection:** Guidance on what data sources and detection logic can identify the technique in use. This is the section your detection engineers live in.

### Building an ATT&CK Coverage Map

The ATT&CK Navigator (https://mitre-attack.github.io/attack-navigator/) is a free, browser-based tool for visualizing coverage. Here is a practical workflow:

**Step 1: Start with your top threat scenarios.** Based on your threat profile (Chapter 03, Template 1), identify the two or three most realistic attack scenarios for your organization. Look up the techniques associated with those scenarios.

**Step 2: Color-code by coverage type.** In the Navigator, create a layer and color techniques by their current status:
- Green: We have active detection for this technique and have validated it works
- Yellow: We have partial coverage or untested detection
- Red: No coverage — no prevention and no detection
- Blue: Prevention control in place but limited detection capability

**Step 3: Identify and prioritize gaps.** Focus on red techniques that fall within your priority threat scenarios. Those are your highest-priority detection engineering investments.

**Step 4: Build detection incrementally.** You will never cover the entire matrix, and trying to is a trap. Focus on the techniques your most likely adversaries use most often. The Pareto principle applies: covering the 20% of techniques responsible for 80% of real-world incidents is achievable and impactful.

**Step 5: Validate and update.** Coverage maps go stale. Revisit your ATT&CK coverage quarterly and after major environment changes. Run tabletop exercises or purple team engagements to validate that your detections actually fire against real technique execution — not just in theory.

### ATT&CK Groups and Software

The Groups section of ATT&CK (https://attack.mitre.org/groups/) catalogs known threat actor groups with:
- Known techniques they have used
- Software and tooling they commonly deploy
- Industries and regions they target
- Associated reporting and references

The Software section catalogs malware, tools, and exploit frameworks with their associated techniques.

**Practical use:** If your threat profile identifies ransomware as your primary threat, you can look up ransomware groups that target your industry and see exactly which ATT&CK techniques they use most. This directly informs your detection priority list.

---

## NIST Cybersecurity Framework (CSF)

The NIST CSF is the most widely adopted security program framework in the United States. It provides a structured approach for organizing a security program across five core functions.

### The Five Functions

```
Identify → Protect → Detect → Respond → Recover
```

**Identify:** Develop an understanding of your organization's cybersecurity risk to systems, assets, data, and capabilities. This is the foundation — you cannot protect what you do not know you have. Covers asset management, business environment context, governance, risk assessment, and supply chain risk management.

**Protect:** Implement safeguards to ensure delivery of critical services. Covers access control, awareness and training, data security, information protection processes, maintenance, and protective technology.

**Detect:** Develop and implement activities to identify the occurrence of a security event. Covers anomalies and events, security continuous monitoring, and detection processes.

**Respond:** Develop and implement activities to take action regarding a detected security event. Covers response planning, communications, analysis, mitigation, and improvements.

**Recover:** Develop and implement activities to maintain plans for resilience and to restore capabilities impaired by a security event. Covers recovery planning, improvements, and communications.

### CSF Implementation Tiers

The CSF also defines four implementation tiers that describe the rigor and sophistication of an organization's cybersecurity risk management practices:

| Tier | Description | Typical Profile |
|------|-------------|----------------|
| Tier 1: Partial | Risk management is ad hoc and reactive. Limited awareness of risk. | Organizations with no formal security program |
| Tier 2: Risk Informed | Risk management practices are approved by management but not organization-wide policy. | Organizations with some security practices but limited consistency |
| Tier 3: Repeatable | Risk management is formally approved, expressed as policy, and consistently implemented. | Organizations with mature, documented security programs |
| Tier 4: Adaptive | Organization adapts practices in real time based on lessons learned and continuous improvement. | Advanced organizations with active threat intelligence integration |

**Practical use:** The CSF is most useful as a program assessment and communication tool. Map your current security activities to the five functions to identify gaps. Use the tier definitions to establish a target maturity state and communicate program progress to leadership in business-accessible language.

### CSF 2.0

NIST released CSF 2.0 in 2024, adding a sixth function: **Govern.** Govern covers the policies, processes, and procedures used to manage and monitor the organization's cybersecurity risk management strategy. It reflects the growing recognition that security governance — not just technical controls — is a core program component.

---

## CIS Controls v8

The CIS Controls (formerly known as the SANS Top 20) are a prioritized set of 18 control groups that provide a prescriptive, action-oriented baseline for security programs. Where the NIST CSF is a flexible framework, the CIS Controls are a more specific list of what to implement.

### The 18 Control Groups

| # | Control | Focus Area |
|---|---------|-----------|
| 1 | Inventory and Control of Enterprise Assets | Know what you have |
| 2 | Inventory and Control of Software Assets | Know what is running |
| 3 | Data Protection | Protect sensitive data |
| 4 | Secure Configuration of Enterprise Assets and Software | Eliminate default weaknesses |
| 5 | Account Management | Control who has access |
| 6 | Access Control Management | Enforce least privilege |
| 7 | Continuous Vulnerability Management | Find and fix weaknesses |
| 8 | Audit Log Management | Maintain visibility |
| 9 | Email and Web Browser Protections | Defend the most common attack vectors |
| 10 | Malware Defenses | Detect and block malicious code |
| 11 | Data Recovery | Ensure you can restore |
| 12 | Network Infrastructure Management | Secure the network layer |
| 13 | Network Monitoring and Defense | Detect network-layer threats |
| 14 | Security Awareness and Skills Training | Reduce human error |
| 15 | Service Provider Management | Manage third-party risk |
| 16 | Application Software Security | Secure what you build |
| 17 | Incident Response Management | Know how to respond |
| 18 | Penetration Testing | Validate your defenses |

### Implementation Groups (IG1 / IG2 / IG3)

The CIS Controls use Implementation Groups to provide a maturity-tiered approach:

**IG1 (Basic Cyber Hygiene):** The minimum standard of security for all organizations. These are the controls that, if implemented, protect against the most common attacks. Designed for small organizations with limited IT/security resources. Covers roughly 56 safeguards across the 18 controls.

**IG2 (Foundational):** Builds on IG1. Designed for organizations with dedicated IT staff managing more complex environments with sensitive data. Introduces more formal processes, additional monitoring, and expanded tooling.

**IG3 (Organizational):** The full control set. Designed for organizations with security experts on staff managing large enterprises or environments with regulatory requirements for security. Includes advanced capabilities like security operations, threat hunting, and penetration testing programs.

**Practical use:** Start with IG1 — all of it. If you are a small or medium organization that has fully implemented IG1, you have meaningfully better security than the majority of organizations your size. Use the IG2 and IG3 controls as a roadmap for maturity progression.

---

## ISO 27001 / ISO 27002

ISO 27001 is an international standard for Information Security Management Systems (ISMS). It defines the requirements for establishing, implementing, maintaining, and continually improving an information security management system within an organization.

ISO 27002 is the companion guidance document — where 27001 defines what you must do to be certified, 27002 provides detailed implementation guidance for the controls.

### When ISO 27001 Matters

ISO 27001 is most relevant when:
- Your organization operates internationally or has customers in regions where ISO 27001 is expected
- You are pursuing enterprise sales where customers demand formal security certification
- You operate in regulated industries where recognized security standards are part of compliance requirements
- You want a globally recognized framework for structuring your program

ISO 27001 certification requires an independent audit by an accredited certification body. The certification process is rigorous and resource-intensive, but it produces a formally recognized attestation of your security program's maturity.

For most small and medium organizations, the CIS Controls or NIST CSF provide more practical value without the overhead of formal certification. ISO 27001 becomes more important as you grow and as your customer base demands it.

---

## NIST SP 800-53

NIST SP 800-53 (Security and Privacy Controls for Information Systems and Organizations) is the most comprehensive security control catalog available. Rev 5 includes over 1,000 controls and control enhancements organized into 20 control families.

It is the mandatory standard for U.S. federal systems and is widely adopted in defense contracting (via NIST 800-171 and CMMC), healthcare (via HIPAA alignment), and financial services.

**Practical use for non-federal organizations:** Most organizations do not implement 800-53 directly. Instead, they use it as a reference when a specific control area requires more depth than the CIS Controls provide, or when they need to demonstrate alignment with federal security requirements (e.g., for government contracts or FedRAMP compliance).

If you are in a regulated industry or pursuing government contracts, understanding which 800-53 control families apply to your compliance requirements is important. Your security team does not need to memorize the catalog — they need to know how to use it as a reference.

---

## Diamond Model of Intrusion Analysis

The Diamond Model is a framework for analyzing intrusion events that complements both the Kill Chain and ATT&CK. It provides a structured way to understand the relationship between the four core elements of any intrusion.

### The Four Elements

```
        Adversary
           |
  Infrastructure ←→ Capability
           |
         Victim
```

**Adversary:** The threat actor responsible for the intrusion — their identity, motivation, and intent.

**Infrastructure:** The technical infrastructure used by the adversary — servers, domains, IP addresses, and other resources used to stage and execute the attack.

**Capability:** The tools, techniques, and malware used to execute the attack.

**Victim:** The target of the attack — their identity, industry, and the specific assets or data being targeted.

### How to Use the Diamond Model

The Diamond Model is most useful as an analytical tool for threat intelligence and incident investigation. When you are analyzing an intrusion, populating the Diamond gives you a structured way to document what you know and identify what you still need to determine.

**For threat intelligence:** Shared intelligence about an adversary group (their infrastructure, capabilities, and typical victims) can be mapped to the Diamond. When you see similar infrastructure or capabilities in your environment, you can quickly assess whether the adversary and victim profile match your organization.

**For incident response:** During an active investigation, the Diamond helps you think through attribution questions systematically. What capability (malware, technique) was used? What infrastructure (C2 server, dropper domain) was involved? Does the victim profile (your organization's industry, size, data assets) match known targeting patterns for any identified adversary?

**For connecting incidents:** The Diamond is particularly useful for determining whether two separate incidents are related. Shared infrastructure or shared capabilities between incidents suggest a common adversary, even if the specific techniques differ.

---

## Framework Interoperability

These frameworks are not mutually exclusive. They address different aspects of security program management and work best when used together.

| Framework | Primary Use | Best For |
|-----------|-------------|---------|
| PICERL / NIST 800-61 | Incident response process | Structuring how you respond to incidents |
| MITRE ATT&CK | Threat behavior catalog | Detection engineering, threat hunting, control coverage mapping |
| Cyber Kill Chain | Attack progression model | Understanding attack stages, defensive planning |
| Diamond Model | Intrusion analysis | Threat intelligence analysis, incident investigation |
| NIST CSF | Security program structure | Program assessment, executive communication, gap analysis |
| CIS Controls v8 | Prescriptive control set | Implementation roadmap, baseline security requirements |
| ISO 27001 | Formal certification | Enterprise sales requirements, international compliance |
| NIST 800-53 | Comprehensive control catalog | Regulated industries, federal alignment, deep control reference |

A practical way to use these together:
- Use **NIST CSF** to structure and communicate your overall program
- Use **CIS Controls** as your implementation roadmap for what to build
- Use **MITRE ATT&CK** to map your detection coverage and prioritize detection engineering
- Use **PICERL** to structure your incident response capability
- Use the **Kill Chain** and **Diamond Model** when analyzing specific incidents or threat intelligence

---

## References

- NIST SP 800-61 Rev.2 – Computer Security Incident Handling Guide: https://csrc.nist.gov/publications/detail/sp/800-61/rev-2/final
- MITRE ATT&CK Enterprise: https://attack.mitre.org/matrices/enterprise/
- MITRE ATT&CK Navigator: https://mitre-attack.github.io/attack-navigator/
- NIST Cybersecurity Framework 2.0: https://www.nist.gov/cyberframework
- CIS Controls v8: https://www.cisecurity.org/controls/v8
- CIS Controls Implementation Groups: https://www.cisecurity.org/controls/implementation-groups
- ISO 27001 Overview: https://www.iso.org/isoiec-27001-information-security.html
- NIST SP 800-53 Rev.5: https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final
- Diamond Model of Intrusion Analysis (original paper): https://www.activeresponse.org/wp-content/uploads/2013/07/diamond.pdf
- MITRE D3FEND (defensive countermeasures): https://d3fend.mitre.org/
