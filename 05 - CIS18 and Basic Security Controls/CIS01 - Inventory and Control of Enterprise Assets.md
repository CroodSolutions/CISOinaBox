# CIS Control 1: Inventory and Control of Enterprise Assets

## Overview

**What it requires:** Actively manage all enterprise assets connected to the infrastructure — physical, virtual, remote, and cloud — so you know the totality of what needs to be monitored and protected. 

This usually involves identification of unknown, non-compliant, nonstandard, or specialized devices - followed by, taking appropriate action to reduce the risk these devices represent to the organization. 

 - Key points to consider:
   - What type of device is it (IOT, medical, kiosk, BYOD / unauthorized user or host)? 
   - What network segment are they on?
   - Also, what other networks are reachable from the asset (remember to include VPNs, GRE tunnels, ExpressRoute, or similar pathways)?  
   - What Active Directory (AD) domain(s) or directory/identity stores is the device joined to, or connected with?
   - Are any accounts, configuration files, or secrets resident on the asset that could jeopordize systems of a higher trust level or importance?
   - What active sessions exist that could be leveraged by an attacker? 
 - When unauthorized or non-compliant devices are found, a range of options exist including:
   - Installing appropriate agents, patches, or settings to make the device compliant (if possible).
   - Moving devices to the correct network segment (or creating new zones, if adequate segmentation does not exist).
   - Convert unmanaged devices to managed devices.
   - Remove / kick-out unauthorized, compromised, or risky devices. 
 - IOT and Devices Incapable of Compliance:
   - Some devices such as IOT, medical devices, and so on, cannot be made compliant.
   - There are also situations where a device must be available to untrusted user populations (kiosk). 
   - The key to this is proper:
     - Network segmentation / isolation.
     - Monitoring for intrusion or compromise.
     - For Kiosks, make sure they are in a kiosk mode, not joined to an AD domain, and network isolated from important resouces. 

## MITRE ATT&CK Techniques Mitigated 

**ATT&CK Relevance:** Mitigates Reconnaissance (T1595), Initial Access via exposed assets (T1133, T1190), and Discovery techniques (T1082, T1018). You cannot detect an attacker on an asset you do not know exists.

**Implementation Group Progression:**
- **IG1:** Establish and maintain a detailed enterprise asset inventory, updated weekly. Use an active discovery tool to identify assets.
- **IG2:** Use DHCP logging to update the inventory. Ensure accuracy by reconciling with DNS, CMDB, and network scans.
- **IG3:** Use a passive discovery tool to identify assets on the network.

## Solutions and Products 

**Solution Categories and Example Brands:**

| Solution Category | What It Does | Example Brands |
|---|---|---|
| IT Asset Management (ITAM) | Central repository for all hardware and software assets | ServiceNow ITAM, Lansweeper, Armis, Axonius, Flexera |
| Network Discovery & Scanning | Active/passive scanning to find all devices on the network | Nmap, Masscan, Rumble/runZero, Qualys CSAM, Tenable.io |
| Cyber Asset Attack Surface Management (CAASM) | Aggregates data from multiple sources to build a unified asset view | Axonius, Armis, Sevco, JupiterOne, Panaseer |
| Cloud Asset Inventory | Discovers and inventories cloud resources across providers | AWS Config, Azure Resource Graph, Google Cloud Asset Inventory, Wiz |

## Key Points

**Implementation Tip:** Asset inventory is not a one-time project. It must be continuously maintained. Start with network scanning to find everything, then feed that into a CMDB or ITAM platform. Reconcile weekly. Any asset that appears on a scan but not in the inventory is either shadow IT or a compromised device — both demand immediate attention.

---
