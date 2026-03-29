# CIS Control 4: Secure Configuration of Enterprise Assets and Software

## Overview

**What it requires:** Establish and maintain secure configurations for all enterprise assets and software, including hardened images, configuration baselines, and change management.

Of course, strong words like "all" we know will not happen in any modern enterprise environment, in the real world. 

So what is actually possible / what should organizations strive for?

Here are a few good first steps for those starting the journey:
 - Understand what you have (covered in previous control), but also how it is used (business/data mapping aspect).
 - Come up with secure baselines for images and containers that include necessary agents, remove unneeded programs and services, and apply secure polices.
 - Assure agent compliance, logging, and mapping of high risk scenarios to detection and response flows.  


## MITRE ATT&CK Techniques Mitigated 

**ATT&CK Relevance:** Broadly mitigates Privilege Escalation (T1068, T1548), Persistence (T1053, T1547), and Defense Evasion (T1562). Misconfigurations are involved in the majority of breaches. Hardened configurations eliminate entire categories of attack techniques.

## Solutions and Products 

**Solution Categories and Example Brands:**

| Solution Category | What It Does | Example Brands |
|---|---|---|
| Configuration Management / Hardening | Automates baseline configuration and compliance checks | Terraform, CIS-CAT Pro (CIS Benchmarks), Microsoft GPO / Intune, Chef, Puppet, Ansible |
| Cloud Security Posture Management (CSPM) | Detects misconfigurations in cloud infrastructure | Wiz, Prisma Cloud (Palo Alto), Microsoft Defender for Cloud, Orca Security |
| Vulnerability / Configuration Scanning | Identifies deviations from secure baselines | Tenable Nessus, Qualys VMDR, Rapid7 InsightVM |
| Image / Container Hardening | Ensures golden images and containers start from a secure baseline | CIS Hardened Images (marketplace images), Docker Bench, Aqua Security, Sysdig |

## Key Points

**Implementation Tip:** One option is to use CIS Benchmarks as a configuration baseline — they are consensus-developed, freely available, and map directly to ATT&CK. Note that infrastrucure as code, is a growing trend that may be impossible to ignore, when approaching the topic of configuration management. 

---
