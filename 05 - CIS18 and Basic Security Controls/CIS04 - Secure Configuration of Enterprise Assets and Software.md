# CIS Control 4: Secure Configuration of Enterprise Assets and Software

## Overview

**What it requires:** Establish and maintain secure configurations for all enterprise assets and software, including hardened images, configuration baselines, and change management.

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

**Implementation Tip:** Use CIS Benchmarks as your configuration baseline — they are consensus-developed, freely available, and map directly to ATT&CK. Automate compliance checking with tools like CIS-CAT, then enforce drift detection through your configuration management platform.

---
