### CIS Control 11: Data Recovery

**What it requires:** Establish and maintain data recovery practices sufficient to restore enterprise assets to a pre-incident and trusted state.

**ATT&CK Relevance:** The primary defense against Impact (T1486 — Data Encrypted for Impact, T1485 — Data Destruction, T1490 — Inhibit System Recovery). Ransomware is an existential business risk; immutable backups are the insurance policy.

**Solution Categories and Leading Brands:**

| Solution Category | What It Does | Leading Brands |
|---|---|---|
| Enterprise Backup & Recovery | Automated backup with rapid recovery capabilities | Veeam, Commvault, Cohesity, Rubrik, Veritas |
| Immutable / Air-Gapped Backup | Prevents ransomware from encrypting or deleting backup data | Rubrik, Cohesity, AWS S3 Object Lock, Azure Immutable Blob Storage |
| Disaster Recovery as a Service (DRaaS) | Cloud-based failover for business continuity | Zerto, Veeam, Azure Site Recovery, AWS Elastic Disaster Recovery |

**Implementation Tip:** The 3-2-1-1-0 rule: maintain 3 copies of data, on 2 different media types, with 1 offsite, 1 immutable/air-gapped, and 0 errors in recovery testing. Test restores quarterly at minimum. A backup you have never tested is not a backup — it is a hope.

---
