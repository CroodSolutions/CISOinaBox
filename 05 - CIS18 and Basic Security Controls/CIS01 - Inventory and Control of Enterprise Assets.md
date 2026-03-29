# CIS Control 1: Inventory and Control of Enterprise Assets

## Overview

**What it requires:** Actively manage all enterprise assets connected to the infrastructure — physical, virtual, remote, and cloud — so you know the totality of what needs to be monitored and protected. Identify and remove unauthorized and unmanaged assets.

## MITRE ATT&CK Techniques Mitigated 

**ATT&CK Relevance:** Mitigates Reconnaissance (T1595), Initial Access via exposed assets (T1133, T1190), and Discovery techniques (T1082, T1018). You cannot detect an attacker on an asset you do not know exists.

**Implementation Group Progression:**
- **IG1:** Establish and maintain a detailed enterprise asset inventory, updated weekly. Use an active discovery tool to identify assets.
- **IG2:** Use DHCP logging to update the inventory. Ensure accuracy by reconciling with DNS, CMDB, and network scans.
- **IG3:** Use a passive discovery tool to identify assets on the network.

## Solutions and Products 

**Solution Categories and Leading Brands:**

| Solution Category | What It Does | Leading Brands |
|---|---|---|
| IT Asset Management (ITAM) | Central repository for all hardware and software assets | ServiceNow ITAM, Lansweeper, Armis, Axonius, Flexera |
| Network Discovery & Scanning | Active/passive scanning to find all devices on the network | Nmap, Masscan, Rumble/runZero, Qualys CSAM, Tenable.io |
| Cyber Asset Attack Surface Management (CAASM) | Aggregates data from multiple sources to build a unified asset view | Axonius, Armis, Sevco, JupiterOne, Panaseer |
| Cloud Asset Inventory | Discovers and inventories cloud resources across providers | AWS Config, Azure Resource Graph, Google Cloud Asset Inventory, Wiz |

## Key Points

**Implementation Tip:** Asset inventory is not a one-time project. It must be continuously maintained. Start with network scanning to find everything, then feed that into a CMDB or ITAM platform. Reconcile weekly. Any asset that appears on a scan but not in the inventory is either shadow IT or a compromised device — both demand immediate attention.

---
