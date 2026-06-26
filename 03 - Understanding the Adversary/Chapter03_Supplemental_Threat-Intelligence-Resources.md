# Supplemental: Top Resources for Understanding Emerging Threats

*This document is a technical companion to Chapter 03 – Understanding the Adversary. It provides a curated, organized reference of the most useful threat intelligence sources, tools, and communities available to security practitioners — with guidance on what each one is best used for and how to integrate it into your program.*

---

## How to Use This Document

Threat intelligence resources fall into several categories: government and non-profit sources that provide free, high-quality intelligence; commercial platforms with enriched data and analysis; community and peer-sharing networks; technical analysis tools; and ongoing research publications. 

This document is organized by category so you can quickly identify sources that match your team's maturity, budget, and use case. Each entry includes what the resource provides, who it is best suited for, and how to integrate it into your workflow.

A key principle from Chapter 03 applies here: **more sources is not better — actionable sources are better.** Pick two or three sources to start, build a triage process around them, and add more only when you have the capacity to consume them effectively.

---

## Category 1: Government and Non-Profit Sources

These are free, authoritative, and consistently high-quality. Every organization should be consuming at least one or two of these regardless of size or budget.

---

### CISA (Cybersecurity and Infrastructure Security Agency)
**URL:** https://www.cisa.gov/news-events/cybersecurity-advisories

**What it provides:**
- Cybersecurity advisories on actively exploited vulnerabilities, with specific remediation guidance
- Known Exploited Vulnerabilities (KEV) catalog — a prioritized list of vulnerabilities that have confirmed exploitation in the wild
- Alerts on nation-state activity and significant threat campaigns
- Sector-specific guidance for critical infrastructure industries
- Shields Up advisories during periods of elevated threat (geopolitical events, major incidents)

**Best for:** All organizations. CISA advisories are written to be actionable and are specifically prioritized for U.S. organizations. The KEV catalog in particular is the single best source for patch prioritization — if a vulnerability is on the KEV, it is being actively exploited and should be remediated immediately regardless of its CVSS score.

**Integration tip:** Subscribe to CISA email alerts (https://www.cisa.gov/subscribe-updates-cisa) and route them to a designated triage inbox. Review the KEV catalog weekly as part of your vulnerability management process.

---

### MS-ISAC (Multi-State Information Sharing and Analysis Center)
**URL:** https://www.cisecurity.org/ms-isac

**What it provides:**
- Sector-specific threat intelligence for state, local, tribal, and territorial (SLTT) government entities
- Weekly threat briefings and monthly reports
- Malware analysis and IOC feeds
- 24/7 SOC services available to SLTT members
- Incident response assistance for member organizations

**Best for:** State and local government entities, public schools, utilities, and other SLTT organizations. Membership is free for qualifying organizations and provides access to services and intelligence that would otherwise require significant budget.

**Integration tip:** If your organization qualifies, register for membership — it is free and the intelligence is sector-relevant. If you do not qualify, the public reports are still useful reference material.

---

### H-ISAC (Health Information Sharing and Analysis Center)
**URL:** https://h-isac.org/

**What it provides:**
- Healthcare-specific threat intelligence and advisories
- TLP-tagged IOC sharing among member organizations
- Threat briefings on ransomware groups targeting healthcare
- Incident sharing and collaboration among healthcare security teams

**Best for:** Healthcare organizations of all sizes. Healthcare is one of the most heavily targeted sectors for ransomware, and H-ISAC provides sector-relevant intelligence that general sources do not.

**Integration tip:** Membership fees vary by organization size. Evaluate whether the membership cost is justified by the intelligence value for your specific environment.

---

### FS-ISAC (Financial Services ISAC)
**URL:** https://www.fsisac.com/

**What it provides:**
- Financial sector-specific threat intelligence
- Intelligence on fraud, BEC, and account takeover campaigns targeting financial institutions
- Incident sharing among member institutions
- Regulatory liaison and compliance intelligence

**Best for:** Banks, credit unions, payment processors, insurers, and other financial services organizations.

---

### FBI InfraGard
**URL:** https://www.infragard.org/

**What it provides:**
- Partnership between FBI and private sector for threat information sharing
- Industry-specific threat briefings (often classified at TLP:AMBER or TLP:RED)
- Direct access to FBI field office contacts
- Regional chapter events and peer networking

**Best for:** Organizations of all sizes where access to law enforcement intelligence and relationships is valuable. Particularly useful for organizations in critical infrastructure sectors. InfraGard membership is free and available to U.S. citizens who pass a background check.

**Integration tip:** Join the chapter in your region. Attend meetings — the peer networking and law enforcement relationships are as valuable as the formal intelligence products.

---

### FIRST (Forum of Incident Response and Security Teams)
**URL:** https://www.first.org/

**What it provides:**
- Global network of incident response teams that share threat intelligence
- CVSS (Common Vulnerability Scoring System) — the standard scoring system for vulnerability severity
- EPSS (Exploit Prediction Scoring System) — a newer scoring system that predicts the probability a vulnerability will be exploited in the next 30 days
- TLP (Traffic Light Protocol) — the standard framework for classifying intelligence sharing restrictions
- Training and certification resources for IR professionals

**Best for:** Security and incident response teams at organizations with formal IR capability. FIRST membership requires sponsorship from an existing member organization.

---

### ACTRA (Arizona Cyber Threat Response Alliance)
**URL:** https://www.actraaz.org

**What it provides:**
- Arizona-specific threat intelligence sharing among private sector, government, and law enforcement
- Local threat briefings relevant to Arizona organizations
- Peer community for Arizona security professionals

**Best for:** Organizations operating in Arizona. Regional threat intelligence — especially information shared by local law enforcement and peer organizations — often provides faster, more specific intelligence than national sources for locally relevant threats.

---

## Category 2: Free Technical Intelligence Platforms

These platforms provide threat data, IOC lookups, and analysis tools that security teams can use directly in their investigations and detection tuning.

---

### AlienVault OTX (Open Threat Exchange)
**URL:** https://otx.alienvault.com/

**What it provides:**
- Community-driven IOC sharing platform with millions of indicators
- "Pulses" — curated IOC collections organized around specific threat actors, campaigns, or malware families
- Direct integration with many SIEM, EDR, and firewall products via API
- IOC lookups for IPs, domains, file hashes, and URLs
- Free to use; commercial integration options available through AT&T Cybersecurity

**Best for:** Organizations that want a free, high-volume IOC feed with broad community contribution. Good starting point for integrating external threat intelligence into detection tooling.

**Integration tip:** Subscribe to pulses relevant to your threat profile and export IOCs to your SIEM or firewall block lists. Be selective — not all community-contributed pulses are high quality. Filter by contributor reputation and age of indicators (IOCs older than 90 days have sharply reduced value).

---

### VirusTotal
**URL:** https://www.virustotal.com/

**What it provides:**
- File, URL, IP, and domain reputation lookups against 70+ antivirus engines and detection tools
- Behavioral analysis for submitted files (sandboxing)
- Relationship graphs showing connections between files, domains, and IPs
- API access for automated lookups

**Best for:** Rapid triage of suspicious files, URLs, and network indicators during incident investigation. "Is this file malicious?" is almost always answerable via VirusTotal lookup.

**Important caveat:** Files submitted to VirusTotal are shared with antivirus vendors and the security research community. Do not submit files containing sensitive data, proprietary information, or potential evidence from an active investigation. For sensitive analysis, use a private analysis environment or enterprise VirusTotal plan.

**Integration tip:** Use the free web interface for ad hoc lookups. Integrate the API into your SIEM or SOAR for automated indicator enrichment.

---

### Shodan
**URL:** https://www.shodan.io/

**What it provides:**
- Internet-wide scan data showing exposed services, open ports, software versions, and configurations
- Search for specific devices, software, or configurations exposed on the internet
- Organization-level view of your own internet-facing infrastructure as attackers see it
- Vulnerability data for exposed services
- Alerts for new exposures matching your search criteria

**Best for:** External attack surface visibility. Understanding what an attacker sees when they look at your organization from the internet is one of the highest-value security exercises you can perform. Shodan lets you do this systematically.

**Integration tip:** Create a free Shodan account and search for your organization's IP ranges and domain names. What comes back is your external attack surface from an attacker's perspective. Schedule this as a monthly review. Set up alerts for new exposures matching your IP ranges.

---

### Censys
**URL:** https://search.censys.io/

**What it provides:**
- Similar to Shodan — internet-wide scanning data for exposed services and certificates
- Certificate transparency log integration — see all certificates issued for your domains
- Attack Surface Management (ASM) product for ongoing monitoring
- API access for programmatic queries

**Best for:** Attack surface enumeration, especially certificate-based discovery of subdomains and internet-facing assets. Complements Shodan with different scanning methodologies and data.

---

### CISA AIS (Automated Indicator Sharing)
**URL:** https://www.cisa.gov/topics/cyber-threats-and-advisories/information-sharing/automated-indicator-sharing-ais

**What it provides:**
- Machine-readable IOC feeds in STIX/TAXII format
- Near-real-time sharing of malicious indicators between CISA and participating organizations
- Free participation for qualifying U.S. organizations

**Best for:** Organizations with a SIEM or threat intelligence platform (TIP) that can ingest STIX/TAXII feeds. More technical than a digest-based advisory feed — requires tooling to consume effectively.

---

### Have I Been Pwned
**URL:** https://haveibeenpwned.com/

**What it provides:**
- Search for email addresses or domains against known data breach databases
- Notification alerts when your email addresses appear in new breach data
- Domain-level monitoring to see if any email addresses from your organization have been exposed
- Breach data feeds available to organizations monitoring their own domain

**Best for:** Monitoring for compromised credentials from your organization's email domains. Exposed credentials are one of the primary initial access vectors — knowing when your employees' credentials appear in breach data enables proactive password resets before attackers use them.

**Integration tip:** Set up domain monitoring for your organization's primary email domains. This is a free service and one of the highest-value low-cost controls available.

---

## Category 3: Threat Research Publications

These are ongoing research outputs — reports, blogs, and databases — from security vendors and research organizations. They provide deeper analysis than advisory feeds and are the best source for understanding the tactics of specific threat actor groups.

---

### Verizon Data Breach Investigations Report (DBIR)
**URL:** https://www.verizon.com/business/resources/reports/dbir/

**What it provides:**
- Annual analysis of thousands of confirmed data breaches and security incidents
- Statistical breakdown of attack patterns, initial access vectors, threat actor categories, and targeted industries
- Industry-specific findings for healthcare, finance, manufacturing, retail, public sector, and others
- Year-over-year trend data

**Best for:** Understanding the realistic threat landscape based on actual incident data rather than anecdotal reporting. The DBIR is the most data-driven public source for "what attacks actually look like in practice." Use it to validate your threat profile and prioritize controls based on what is causing real breaches in organizations like yours.

**Integration tip:** Read the industry-specific section relevant to your sector. The executive summary provides the top-level findings in accessible language suitable for briefing leadership.

---

### Mandiant M-Trends
**URL:** https://www.mandiant.com/m-trends

**What it provides:**
- Annual report from Mandiant's incident response practice based on hundreds of IR engagements
- Dwell time statistics (how long attackers are in environments before detection)
- Analysis of attacker techniques observed in real investigations
- Industry and regional targeting trends

**Best for:** Understanding attacker behavior from the perspective of an organization that responds to major breaches. M-Trends provides practitioner-level insight into how attacks actually unfold in enterprise environments.

---

### CrowdStrike Global Threat Report
**URL:** https://www.crowdstrike.com/global-threat-report/

**What it provides:**
- Annual report on threat actor activity observed across CrowdStrike's customer base
- Named threat actor profiles and their activities
- eCrime (cybercriminal) and nation-state actor analysis
- Breakout time statistics (how fast attackers move from initial access to lateral movement)

**Best for:** Understanding named threat actor groups and their current targeting priorities. CrowdStrike's threat actor naming convention (bears, pandas, kittens, etc.) is widely referenced in the industry.

---

### Microsoft Security Intelligence Blog
**URL:** https://www.microsoft.com/en-us/security/blog/

**What it provides:**
- Analysis of threats observed across Microsoft's massive telemetry base
- Detailed technical writeups on specific malware families, attack campaigns, and vulnerabilities
- Threat actor profiles from Microsoft's Threat Intelligence Center (MSTIC)
- Security research on emerging attack techniques

**Best for:** Technical depth on specific threats, especially those targeting Microsoft environments (Windows, Azure, M365, Exchange). Given the prevalence of Microsoft infrastructure, this is broadly relevant to most organizations.

---

### Google Project Zero
**URL:** https://googleprojectzero.blogspot.com/

**What it provides:**
- In-depth technical research on zero-day and n-day vulnerabilities
- Analysis of exploitation techniques and attack chains
- Root cause analysis of major vulnerabilities

**Best for:** Security engineers and researchers who want deep technical understanding of vulnerability exploitation. Less relevant for operational security teams at most organizations — the technical depth is significant and the relevance to day-to-day operations is lower unless you are in a product security role.

---

### SANS Internet Storm Center (ISC)
**URL:** https://isc.sans.edu/

**What it provides:**
- Daily threat briefings and handler diaries written by security practitioners
- Real-time tracking of port scanning, malware activity, and emerging threats
- Podcast (StormCast) for daily 5-minute threat updates
- Free educational resources and analysis tools

**Best for:** Daily situational awareness in an accessible format. The ISC handler diaries provide practitioner-level analysis that bridges the gap between raw data and operational insight. StormCast is one of the most time-efficient ways to stay current on emerging threats.

**Integration tip:** Add the StormCast podcast to your daily routine. It is five minutes and covers the most significant daily developments in threat intelligence.

---

### Bleeping Computer
**URL:** https://www.bleepingcomputer.com/

**What it provides:**
- Breaking news on ransomware attacks, data breaches, and vulnerability disclosures
- Technical analysis of malware and attack tools
- Ransomware negotiation and decryption resources (No More Ransom partnership)
- Active forum community for malware analysis

**Best for:** Real-time awareness of active threats and significant security events. Bleeping Computer often breaks news on major ransomware campaigns and data breaches before formal advisory channels publish. Good for staying current on what is actively happening in the threat landscape.

---

### Krebs on Security
**URL:** https://krebsonsecurity.com/

**What it provides:**
- Investigative reporting on cybercrime, data breaches, and threat actors
- Deep-dive reporting on fraud, criminal underground markets, and attacker infrastructure
- Historically significant data breach reporting with victim perspective

**Best for:** Understanding the criminal ecosystem and human elements behind cyber threats. Krebs provides context that technical IOC feeds do not — understanding how criminal organizations operate helps you think like a defender rather than just a technician.

---

## Category 4: Threat Intelligence Platforms and Aggregators

For organizations that have outgrown manual advisory review and need structured intelligence management.

---

### MISP (Malware Information Sharing Platform)
**URL:** https://www.misp-project.org/

**What it provides:**
- Open-source threat intelligence platform for storing, sharing, and correlating IOCs and threat data
- STIX/TAXII support for interoperability with other TIPs
- Integration with analysis tools, SIEMs, and security products
- Community feeds available for organizations that join sharing circles

**Best for:** Organizations that want to build an internal threat intelligence capability with IOC management and sharing. MISP is free and widely deployed by ISACs, government agencies, and enterprise security teams. Requires dedicated setup and maintenance effort.

---

### IBM X-Force Exchange
**URL:** https://exchange.xforce.ibmcloud.com/

**What it provides:**
- Threat intelligence repository with IOCs, vulnerability data, and malware reports
- Collections organized around specific threat campaigns and actors
- Integration with IBM security products
- Free tier with limited API access; commercial plans for full capability

**Best for:** Organizations in the IBM security ecosystem. Also useful for ad hoc threat research and IOC lookups alongside other free platforms.

---

### Recorded Future (Commercial)
**URL:** https://www.recordedfuture.com/

**What it provides:**
- Machine learning-driven threat intelligence aggregation from open, dark web, and technical sources
- Real-time risk scoring for IPs, domains, vulnerabilities, and threat actors
- Automated alert correlation with your environment
- Threat actor profiles and campaign tracking

**Best for:** Large organizations or high-risk environments that require comprehensive, automated intelligence enrichment and have budget for commercial intelligence platforms. Recorded Future is one of the leading commercial TIP vendors but represents a significant investment.

---

## Category 5: Dark Web and Underground Monitoring

For organizations with significant data assets or brand exposure, monitoring criminal marketplaces and forums provides early warning of targeted threats and data exposures.

---

### What Dark Web Monitoring Covers

Criminal underground markets and forums are where:
- Stolen credentials from your organization may be listed for sale
- Threat actors may announce upcoming attacks on your organization or industry
- Ransomware groups publish stolen data from victims who do not pay
- Access brokers sell initial access to compromised organizations
- Threat actors discuss and share tools and techniques

**Practical value for most organizations:** Knowing that your credentials or data are being sold gives you the opportunity to respond before attackers use the access. Early warning of a targeted campaign against your industry allows proactive defensive posture adjustments.

**Implementation options:**
- Commercial dark web monitoring services (many cyber insurance policies include this as a benefit — check your policy)
- Identity theft protection platforms often include dark web credential monitoring
- Specialized vendors: Recorded Future, Intel 471, Flashpoint for enterprise-grade coverage

**Important caveat:** Security teams should not independently access dark web markets or forums. Use properly established commercial monitoring services that provide intelligence without requiring direct access to criminal infrastructure.

---

## Category 6: Vulnerability Intelligence

Knowing about vulnerabilities is only useful if you know which ones attackers are actually using. These sources bridge the gap between the NVD's complete catalog and the smaller subset that matters operationally.

---

### CISA Known Exploited Vulnerabilities (KEV) Catalog
**URL:** https://www.cisa.gov/known-exploited-vulnerabilities-catalog

**What it provides:**
- The definitive list of vulnerabilities that have confirmed exploitation in the wild
- Required patching deadlines for U.S. federal agencies (useful as a prioritization benchmark for all organizations)
- Updated continuously as new exploitation is confirmed

**Integration tip:** Any vulnerability on the KEV catalog should jump to the top of your remediation queue regardless of its CVSS score. If CISA has confirmed active exploitation, attackers are using it now.

---

### EPSS (Exploit Prediction Scoring System)
**URL:** https://www.first.org/epss/

**What it provides:**
- A probability score (0-100%) predicting the likelihood that a given CVE will be exploited in the next 30 days
- Updated daily based on observed exploitation activity
- Complements CVSS by adding temporal likelihood context

**Integration tip:** Use EPSS alongside CVSS and KEV for vulnerability prioritization. A CVE with a moderate CVSS score but high EPSS probability is a higher remediation priority than a critical CVSS score with near-zero EPSS.

---

### NVD (National Vulnerability Database)
**URL:** https://nvd.nist.gov/

**What it provides:**
- The comprehensive catalog of all publicly disclosed CVEs with CVSS scoring
- CPE (Common Platform Enumeration) data linking CVEs to affected products
- The authoritative source for vulnerability data

**Integration tip:** NVD is the foundation — it is where everything starts. Use it as a reference rather than a triage tool; its volume (tens of thousands of CVEs annually) requires filtering by KEV and EPSS before it becomes actionable.

---

## Quick Reference: Source Selection by Organization Size

| Source | IG1 (Small) | IG2 (Medium) | IG3 (Large) |
|--------|-------------|-------------|-------------|
| CISA Advisories + KEV | Required | Required | Required |
| Industry ISAC | Recommended | Required | Required |
| FBI InfraGard | Recommended | Recommended | Recommended |
| Have I Been Pwned (domain) | Recommended | Required | Required |
| SANS ISC / StormCast | Optional | Recommended | Recommended |
| AlienVault OTX | Optional | Recommended | Deployed |
| VirusTotal | On-demand | On-demand | Integrated |
| Shodan (own attack surface) | Annual | Quarterly | Continuous |
| VDBIR (annual read) | Recommended | Required | Required |
| Mandiant M-Trends (annual read) | Optional | Recommended | Required |
| Commercial TIP (Recorded Future, etc.) | Not applicable | Evaluate at IG2+ | Consider |
| MISP (internal TIP) | Not applicable | Evaluate | Deploy |
| Dark web monitoring | Not applicable | Evaluate | Deployed |

---

## Building Your Intelligence Consumption Workflow

Having a list of sources is not the same as having a threat intelligence program. The workflow below turns sources into action.

**Step 1: Select 2-3 primary sources** appropriate for your org size and industry from the categories above. More sources before you have a triage process in place creates noise, not intelligence.

**Step 2: Establish a triage schedule.** Advisory sources (CISA, ISAC) should be reviewed within 24 hours of receipt. Research publications (DBIR, M-Trends) warrant a dedicated reading session when published, with findings integrated into your threat profile. Daily news sources (ISC, Bleeping Computer) can be skimmed for awareness.

**Step 3: Apply the triage filter.** From Chapter 03 — every advisory runs through: Is this technology in our environment? Is it exploitable in our context? Does the attack pattern target organizations like us? What specific action does this enable?

**Step 4: Route actionable intelligence to the right team.** A vulnerability advisory goes to your VM team with a remediation deadline. A behavioral IOC goes to your detection engineer to write or update a rule. A credential exposure from Have I Been Pwned goes to your identity team for a password reset.

**Step 5: Log everything.** What you reviewed, what you determined, and what you acted on. This log is your intelligence program record. It demonstrates program activity to auditors and leadership, and it builds institutional knowledge about your threat landscape over time.

---

## References

- CISA Cybersecurity Advisories: https://www.cisa.gov/news-events/cybersecurity-advisories
- CISA KEV Catalog: https://www.cisa.gov/known-exploited-vulnerabilities-catalog
- CISA AIS: https://www.cisa.gov/topics/cyber-threats-and-advisories/information-sharing/automated-indicator-sharing-ais
- MS-ISAC: https://www.cisecurity.org/ms-isac
- H-ISAC: https://h-isac.org/
- FS-ISAC: https://www.fsisac.com/
- FBI InfraGard: https://www.infragard.org/
- FIRST.org: https://www.first.org/
- EPSS: https://www.first.org/epss/
- ACTRA Arizona: https://www.actraaz.org
- AlienVault OTX: https://otx.alienvault.com/
- VirusTotal: https://www.virustotal.com/
- Shodan: https://www.shodan.io/
- Censys: https://search.censys.io/
- Have I Been Pwned: https://haveibeenpwned.com/
- MISP Project: https://www.misp-project.org/
- IBM X-Force Exchange: https://exchange.xforce.ibmcloud.com/
- Verizon DBIR: https://www.verizon.com/business/resources/reports/dbir/
- Mandiant M-Trends: https://www.mandiant.com/m-trends
- CrowdStrike Global Threat Report: https://www.crowdstrike.com/global-threat-report/
- Microsoft Security Blog: https://www.microsoft.com/en-us/security/blog/
- SANS Internet Storm Center: https://isc.sans.edu/
- Bleeping Computer: https://www.bleepingcomputer.com/
- Krebs on Security: https://krebsonsecurity.com/
- NVD (National Vulnerability Database): https://nvd.nist.gov/
- No More Ransom Project: https://www.nomoreransom.org/
- Awesome Threat Intelligence (curated resource list): https://github.com/hslatman/awesome-threat-intelligence
