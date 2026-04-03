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
