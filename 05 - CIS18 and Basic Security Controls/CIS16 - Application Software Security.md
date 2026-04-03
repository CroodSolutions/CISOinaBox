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
