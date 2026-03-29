# CIS Control 5: Account Management

## Overview

**What it requires:** Use processes and tools to assign and manage authorization to credentials for user accounts, including administrator accounts and service accounts.

What does this really mean in the real world?  

There are a few critical scenarios that need to be figured out for account management:
 - How do new users get added, across the different types of users and input flows, which could come into play?
 - What roles, rights, or access levels should be inherited?
 - In what ways is contractor access managed, reviewed, validated, and audited.  
 - How are rights or roles removed, if there is a change in employment or customer status:
   - What if an employee is fired?
   - What if they are transferred to a different job (more, less, or different access)?
   - Is there a probitionary status if a powerful user is under review for misconduct or leaving the organization?
   - How quickly are powerful permissions removed, if a poweruser/admin becomes a hostile termination?
   - What does the logging/audit capability look like?
   - Are accounts forever, or checked out / leased for short term use?
 - Access Removal
   - Has access removal been validated, across all of the relevant scenarios?
   - Is there a clear / well-defined process for returning contractors or employees?
 - Access Logging
   - Are authentiction events logged?
   - Are access logs available?


## MITRE ATT&CK Techniques Mitigated 

**ATT&CK Relevance:** Mitigates Credential Access (T1078 — Valid Accounts, T1098 — Account Manipulation), Persistence (T1136 — Create Account), and Privilege Escalation via account abuse. Orphaned and over-privileged accounts are among the most exploited attack surfaces.

## Solutions and Products

**Solution Categories and Leading Brands:**

| Solution Category | What It Does | Leading Brands |
|---|---|---|
| Identity Governance & Administration (IGA) | Manages account lifecycle: provisioning, review, deprovisioning | SailPoint, Saviynt, Microsoft Entra ID Governance, One Identity |
| Privileged Access Management (PAM) | Secures, rotates, and audits privileged account usage | CyberArk, BeyondTrust, Delinea (Thycotic/Centrify), HashiCorp Vault |
| Directory Services | Central identity store and authentication | Microsoft Entra ID (Azure AD), Okta, Ping Identity |

---
