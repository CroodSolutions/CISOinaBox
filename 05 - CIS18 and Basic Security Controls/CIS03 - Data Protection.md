# CIS Control 3: Data Protection

## Overview

**What it requires:** Develop processes and technical controls to identify, classify, securely handle, retain, and dispose of data.

And, that is obviously, a lot. So, how do we approach this topic in the real world?

 - Here are some tips as a general flow for getting started with data protection:
  - Start by brainstorming with people who know the environment and map out as much as you can (you will still need to validate later).
  - Examine what platform solutions that are already in place, have data discovery or DLP solutions (e.g., O365, Google, etc.).
  - Determine gaps in visibility and enforcement, and prioritize these accordance to probability (of serious issue) and impact (if issue).
 - Examine solutions to bridge these gaps, considering:
   - Unstructured data (file shares, SharePoint, Google Drive, Box, etc.)
   - Structured data (databases and Enterprise Software / SaaS applications)
   - User accounts, access, and permissions mapping (including nested groups and non-human accounts).
   - Data flows / handling of sensitive data or secrets in code.
 - Common solution types to consider, from the perspective of the jobs they do:
   - Data discovery / scanning DLP (unstructured)
   - Data discovery (structured)
   - Inline DLP (Network DLP, CASB, etc.)
   - User Entity Behavior Analytics (CASB)
   - Dark web / adversary data monitoring tools (e.g., Flare, Dehashed, HaveIbeenPwnd, etc.) 

A few super important things to remember with inline DLP and such technologies:
 - DLP is good at fixing stupid (some joker sends out a spreadsheet full of PII via email).
 - DLP almost never stops a committed threat actor who has made it to the last phases of a/the killchain.
 - Once the primary domain is compromised (e.g., attacker is Domain Admin), no level of permissions management will matter (they have it all).
 - Data Protection is super important, but we all need to understand the boundaries of where it helps, and where it does not.  

## MITRE ATT&CK Techniques Mitigated 

**ATT&CK Relevance:** Mitigates Collection (T1005, T1039, T1114), Exfiltration (T1041, T1048, T1567), and Impact (T1486 — ransomware encryption of sensitive data). Data protection is both a preventive and detective control.

## Solutions and Products 

**Solution Categories and Example Brands:**

| Solution Category | What It Does | Example Brands |
|---|---|---|
| Data Loss Prevention (DLP) | Monitors and blocks sensitive data from leaving the organization | Microsoft Purview DLP, Symantec DLP (Broadcom), Digital Guardian (Fortra), Netskope |
| Data Classification | Automatically identifies and labels sensitive data | Microsoft Purview Information Protection, SailPoint, HelpSystems, Varonis, BigID |
| Encryption (At Rest & In Transit) | Protects data through encryption | BitLocker, FileVault, VeraCrypt, Vormetric (Thales), AWS KMS, Azure Key Vault |
| Cloud Access Security Broker (CASB) | Controls data flow to and from cloud applications | Netskope, Microsoft Defender for Cloud Apps, Palo Alto Prisma Access, Zscaler |
| Data Discovery & Governance | Finds sensitive data across structured and unstructured repositories | Varonis, SailPoint, BigID, Spirion, Securiti |

---
