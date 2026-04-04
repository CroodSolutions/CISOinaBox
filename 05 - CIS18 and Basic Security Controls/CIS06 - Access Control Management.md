# CIS Control 6: Access Control Management

## Overview

**What it requires:** This control is about the processes and tools to create, assign, manage, and revoke accounts and access. 

This involves making sure people who are onboarded (**join**) receive the appropriate accounts and access levels, those who **leave** have all access removed, and those who **move** have access adjusted to line up with their new role. 

Lifecycle Management considers:
 - **Joiner** receives the appropriate account, and a grant of the required baseline access.
 - **Mover** receives new levels of access when their role within the organization changes.
 - **Leaver** has access immediately revoked, including any active sessions via OAUTH / tokens.

Account types / access levels may include:
 - **Customer** with only the access and permissions required to conduct business with you, in their low-trust role
 - **Employee** with a standard user account, as required for every day work tasks.
 - **Elevated** (normal) users:
   - Management roles allowing approvers in workflows (but not admin)
   - Administrators or builders on specific SaaS applications, where business (non-IT) stakeholders maintain or evolve a product or platform. 
 - **Privileged/Admin** users:
   - Admin accounts (see AD group membership)
   - Domain Admin accounts
   - Global Administrator (M365)
 - **Service Accounts** 

It is important to identify different roles and group memberships (including Active Directory/Entra) and scope out the minimum required permissions for a role to be effective.  

## MITRE ATT&CK Techniques Mitigated 

**ATT&CK Relevance:** Mitigates Lateral Movement (T1021 — Remote Services), Privilege Escalation (T1078), and Initial Access (T1078 — Valid Accounts with stolen credentials). MFA alone blocks the vast majority of credential-stuffing and password-spray attacks.

**Solution Categories and Example Brands:**

## Solutions and Products

| Solution Category | What It Does | Example Brands |
|---|---|---|
| Multi-Factor Authentication (MFA) | Requires second factor for authentication | Microsoft Entra MFA, Duo (Cisco), Okta Verify, YubiKey (Yubico), PingID |
| Single Sign-On (SSO) | Centralizes authentication to reduce credential sprawl | Okta, Microsoft Entra ID, Ping Identity, OneLogin |
| Zero Trust Network Access (ZTNA) | Replaces VPN with identity-aware, least-privilege access | Zscaler Private Access, Palo Alto Prisma Access, Cloudflare Access, Netskope |
| Privileged Access Management (PAM) | Controls and audits privileged sessions | CyberArk, BeyondTrust, Delinea |

---

## See Also

Also, be sure to visit the CIS18 section on [Account Management](https://github.com/CroodSolutions/CISOinaBox/edit/main/05%20-%20CIS18%20and%20Basic%20Security%20Controls/CIS05%20-%20Account%20Management.md) and the CISO-in-a-Box section on [Identity and Access Management](https://github.com/CroodSolutions/CISOinaBox/tree/main/09%20-%20Identity%20and%20Access%20Management).
