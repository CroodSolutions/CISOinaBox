# CIS Control 2: Inventory and Control of Software Assets

## Overview

**What it requires:** Actively manage all software across the environment, including programs running on/in:
 - User Workstations
 - Servers and Containers
 - Kiosks
 - Cloud Workloads
   - Software as a Service (SaaS)
   - Infrastructure as a Service (IaaS)
   - Platform as a Service (PaaS)
 - Extension Ecosystems (Browsers, IDEs, and other applications with extensions)
 - AI Skills

The goal is to understand, track, and manage the different kinds of software deployed across the environment.

In most modern enterprise environments, this also includes managing cloud software such as Software-as-a-Service (SaaS) applications, as well as software running in cloud platforms such as Amazon (AWS), Google (GCP), or Microsoft (Azure). 

A huge portion of this also has cross-over into [Data Protection](https://github.com/CroodSolutions/CISOinaBox/blob/main/05%20-%20CIS18%20and%20Basic%20Security%20Controls/CIS03%20-%20Data%20Protection.md), as Enterprise Software solutions and projects require integrations between software systems; as well as [Account](https://github.com/CroodSolutions/CISOinaBox/blob/main/05%20-%20CIS18%20and%20Basic%20Security%20Controls/CIS05%20-%20Account%20Management.md) and [Access Control](https://github.com/CroodSolutions/CISOinaBox/blob/main/05%20-%20CIS18%20and%20Basic%20Security%20Controls/CIS06%20-%20Access%20Control%20Management.md) since non-human identities, proper scoping of access levels and permissions, and BYOID/SSO are often important elements of such projects. 

## MITRE ATT&CK Techniques Mitigated 

**ATT&CK Relevance:** Directly counters Execution tactics (T1204, T1059) and Persistence via trojaned software (T1554). Application allowlisting is one of the single most effective controls against malware execution, although in large and complex environments and ecosystems it can prove elusive at times. This is where control of software assets will often lead into the [Malware Defence](https://github.com/CroodSolutions/CISOinaBox/blob/main/05%20-%20CIS18%20and%20Basic%20Security%20Controls/CIS10%20-%20Malware%20Defenses.md) and [Incident Response](https://github.com/CroodSolutions/CISOinaBox/blob/main/05%20-%20CIS18%20and%20Basic%20Security%20Controls/CIS17%20-%20Incident%20Response%20Management.md) topics.  

## Solutions and Products 

**Solution Categories and Example Brands:**

| Solution Category | What It Does | Example Brands |
|---|---|---|
| Software Asset Management (SAM) | Tracks installed software, versions, and license compliance | Flexera, Snow Software, ServiceNow SAM |
| Application Control / Allowlisting | Prevents unauthorized executables from running | Microsoft AppLocker / WDAC, Carbon Black App Control, Airlock Digital, ThreatLocker |
| Endpoint Management / UEM | Deploys, patches, and manages software across endpoints | Microsoft Intune, Jamf, SCCM, NinjaOne |

## Key Points

**Implementation Tip:** As pointed out above, application allowlisting is often viewed as too difficult to implement broadly, at least in the beginning. Start in audit mode — log what would be blocked without actually blocking it. This builds your baseline. Then roll out enforcement to high-value targets (servers, privileged workstations) first, using that baseline, and expand from there.

---
