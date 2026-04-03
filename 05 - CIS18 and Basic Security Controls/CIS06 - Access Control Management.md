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
