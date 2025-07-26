Business Continuity Planning (BCP)

Definition:
The continuation of business processes in the event of an unplanned outage or unexpected interruption to business processes and operations. Actions result in the movement of services and data to alternate data processing systems for the purpose of enabling a business to continue its operations. 

Summary:
A BCP consists of documentation prioritizing essential business functions gathering feedback from key stakeholders assessing the businesses'  data, personnel, systems, and procedures. 
Prerequisites: Business Impact Analysis (BIA)
Outcome Artifact: Disaster Recover Planning (DRP)

Details:
The purpose of a Business Continuity Plan (BCP) is to ensure that essential business functions are continuously available to business functions. Creating a BIA requires information from stakeholders providing oversight and responsibility for strategic alignment to business objectives as well as assurance of business operations. BIA development benefits from proper data classification, system, and Service Level Agreement (SLA) information. Input into the BIA should identify the business objectives that support the SMB's mission. Failure of a business objective identified in the BIA results in the potential of the BCP being activated to restore business operations to acceptable levels.   

How To
Defining a BCP begins with creating the BIA by gathering personnel with knowledge and understanding of the business objectives. For example, a SMB consisting of an owner, manager, and staff, would identify key individuals from each area within the SMB to represent the SMB's objectives and key roles. It is important to ackowledge that a staff member managing the SMB when the owner is not present, does provide as much value and information into the BIA process as an owner would. A RACI matrix is a valuable visual aide for creating the BIA with its clear roles and responsibilities. 

After the BIA has been completed, the BCP can be assembled and leverage similar data points used for creating the BIA. BCP roles assist the SMB in executing BCP tasks intent on maintaining business objectives, such as continuing to host a website in the event of a power outage at a web hosting company. The overall results of the BCP support business needs up to an agreed upon change in service levels that could transition from a BCP to a DRP. When the SMB identifies business functions are no longer able to be continued and become recoverable, then the SMB will transition from the BCP to the DRP. Normal operations is achieved when the BCP and/or the DRP have been completed. 

I. Creating the BIA
There are a variety of templates available for use to create a BIA. One example is a Microsoft Word document located within NIST SP 800-34, while other forms include spreadsheets and applications available on the web. After selecting a BIA template, the BIA creation begins with a conversation identifying business objectives. Examples of business objectices include: 

          OBJECTIVE
a. Processing payments from customers
b. Hosting a website to receive customer orders

The most important element in the beginning step of creating a BIA is to identify all business objectives, regardless of their priority. Leaving an objective out of the consideration because it may not seem critical could result in a business interruption becoming a business outage. 

Once all the objectives have been identified and documented in the BIA, the conversation shifts to identifying what failures can occur that would prevent the objective from being completed. Looking at the previous two objective examples, some potention failures that could occur for each objective include:
          
          OBJECTIVE                                POTENTIAL FAILURES
a. Processing payments from customers             a1. Temporary Power Loss
                                                  a2. Temporary Internet Outage
                                                  a3. All personnel unavailable

b. Hosting a website to receive customer orders   b1. Website hosting outage
                                                  b2. Expired SSL certificate
                                                  b3. Third-party shopping cart processor outage

After the Potential Failures have been captured, the BIA will move to focusing on the impact the failures could have on the business. Examples include:

          OBJECTIVE                                POTENTIAL FAILURES                                    IMPACT
a. Processing payments from customers             a1. Temporary Power Loss                             a11. Unable to collect payment from customers for services

                                                  a2. Temporary Internet Outage                        a21. Customers make contact for assistance
                                                                                                       a22. Customers purchase from a competitor
                                                  
                                                  a3. All personnel unavailable                        a31. Reputational damage
                                                                                                       a32. Increased business losses
                                                                                                       a33. Low employee morale

b. Hosting a website to receive customer orders   b1. Website hosting outage                           a11. Customers purchase from competitor
                                                                                                       a12. Reputational damage

                                                  b2. Expired SSL certificate                          a21. Unencrypted customer payment information intercepted by adversary
                                                                                        
                                                  b3. Third-party shopping cart processor outage       a31. Customers purchase from competitor

With the Objectives, Potential Failures, and Impact portions complete, your BIA can analyze existing controls or protections that are in place. Using a scoring system of 1, 2, or 3, can provide a simple quantification method. Assign a score to each Potential Failure based on the Impacts listed and measure the Severity, Occurrence, and Detectability. Review the following scoring chart then assign values to each Potential Failure. 

    ** SCORING CHART **
- SEVERITY - (S)
1 - Low (Not severe to the SMB)
2 - Medium (Not detrimental but also not recommended)
3 - High (Would be uncomfortable for the SMB to experience 1 or more times)

- OCCURRENCE - (O)
1 - Low (1 or less times per year)
2 - Medium (2 to 4 times per year)
3 - High (5 or more times per year)

- DETECTABILITY - (D)
1 - Easy (Little to no effort is needed to identify)
2 - Medium (Not easy but also not hard to determine if an issue occurred)
3 - Hard (Usually would require searching and troubleshooting to determine if an issue took place)


With the Scoring Chart, now you can assign metrics to each Potential Failure and calculate the Potential Risk Score (PRS).

          OBJECTIVE                               POTENTIAL FAILURES                 S-O-D = PRS(SxOxD)                   IMPACT                                                          
a. Processing payments from customers             a1. Temporary Power Loss           1-1-1 =  3          a11. Unable to collect payment from customers for services        

                                                  a2. Temporary Internet Outage      2-2-2 =  8          a21. Customers make contact for assistance
                                                                                                         a22. Customers purchase from a competitor
                                                  
                                                  a3. All personnel unavailable      3-2-1 =  6          a31. Reputational damage
                                                                                                         a32. Increased business losses
                                                                                                         a33. Low employee morale

b. Hosting a website to receive customer orders   b1. Website hosting outage         3-3-2 = 12          a11. Customers purchase from competitor
                                                                                                         a12. Reputational damage

                                                  b2. Expired SSL certificate        2-1-3 = 6           a21. Unencrypted customer payment information intercepted by adversary
                                                                                        
                                                  b3. Third-party shopping cart      3-3-3 = 27          a31. Customers purchase from competitor 
                                                      processor outage       

With the PRS calculated, the SMB can prioritize which business objectives are the priority for identifying mitigating controls. In the examples given, the Third-Party shopping cart processor outage has been marked as having the highest Potential Risk Score, indicating that the business 1) values that objective the most and 2) indicates that the focus of the BIA controls begin with that particular objective. 

At this point, the BIA can focus on steps that can be taken to reduce the PRS. Questions for this step center around what can the business better than what it's current practices. The answers should always include the core values of Information Security: confidentiality, integrity, and availability. The third-party shopping cart processor outage does not indicate an issue with confidentiality or integrity but does lead to availability concerns. What would be possible actions to preventing an availability issue with a third-party shopping cart vendor? Perhaps an alternate vendor would be an option, or an alternate website portal may be an alternative. 

Working through each of the Potential Failures from the highest PRS to the lowest, and collecting a list of actions that reduce the PRS for each objective, are the remaining steps when creating a BIA. Implementing the potential actions and rescoring each Potential Failure after the action has been implemented, leads to the BIA cycle being executed. There is no set timeline to complete the BIA as it is a living document that must be reviewed whenever a new Objective is identified, changes in Potential Failures, or changes to any of the PRS factors. Annual BIA reviews are an ideal starting point with BIAs being applicable to entire SMB organizations, departments, groups, or teams. 

II. Completing the BCP
Obtaining a BCP template is the first step to creating the BCP plan. Like BIA, there are multiple templates available for use. NIST SP 800-34 includes a BCP template called the Contingency Planning Guide for creating a BCP. Use the completed BIA to begin transferring over the business objectives from the BIA to the BCP. With the business objectives listed in priority order, identify the systems belonging to each of the business objectives. This exercise places the business systems in order from most critical to least critical. 

Next, determine the Service Level Agreements (SLA) needed to maintain acceptable business operation levels. Service Level Agreements represent the duration for providing a good or service to a consumer. For example, a customer that orders goods with an expected shipment time of 24 hours indicates there is a 24 hour SLA for that business to have the purchased good shipped. 

          OBJECTIVE                                        SYSTEMS                        SLA
a. Processing payments from customers               Website Portal                     1 minute
b. Hosting a website to receive customer orders     Website Portal, Inventory          5 minutes
c. Ship products to customers                       Order System, Customer Database    24 hours

In the example provided, our BCP has identified the systems supporting each of the business objectives, plus the SLA times. The goal for completing the BCP is to identify actions taken to continue providing the SLAs listed. In the example, Processing payments from customers with a 1 minute SLA, the BCP would document actions taken by systems and personnel, along with procedures for keeping the 1 minute SLA. BCP examples may include actions such as routing the customer's transaction to a second SaaS solution hosted with a different cloud service provider. For the example of Ship products to customers within 24 hours, the BCP may include redundant Order Systems and Customer Databases to maintain the 24 hour SLA. Procedures defined within the BCP could also include actions the SMB staff will take to transition from primary to backup systems, escalation procedures, documentation requirements, and customer notification procedures.   

Similar to BIA schedules, BCP reviews along with documentation updates and exercises, are critical to ensuring that business operations remain aligned with business objective requirements. Annual BCP reviews are an ideal starting point along with annual BCP exercises reviewing BCP procedures.  

III. Completing the DRP
One critical output of a BCP is the Disaster Recover Plan (DRP). A DRP is activated when the BCP time has expired and the business has decided to transition from continuity procedures to recovery procedures. This scenario is typically encountered when an emergency or critical event has occurred that has caused significant interruption for the business to achieve its objectives. Within the DRP documentation are two new metrics for guiding DRP activities. Both are applicable to the business objectives, systems, and procedures. Recovery Point Objective (RPO) measures the amount of acceptable data to the business. For example, a business that has its website information backed up every 12 hours indicates that the business has an RPO up to 6 hours. Since the most recent can restore data up to 6 hours ago, there is a potential that any website changes from 1 minute after the backup up to 6 hours ago could be lost. Recovery Time Objectives signify the amount of time it takes to restore systems to their Normal Operations state. One example would be an RPO of 8 hours indicating that it would take up to 8 hours for services to be restored. An update to our BCP could look like the following graph:

          OBJECTIVE                                        SYSTEMS                        SLA          RPO             RTO
a. Processing payments from customers               Website Portal                     1 minute      15 minutes      1 hour
b. Hosting a website to receive customer orders     Website Portal, Inventory          5 minutes     24 hours        2 hours
c. Ship products to customers                       Order System, Customer Database    24 hours      1 hour          1 hour

Just like the BCP, the DRP will include procedures, roles, and systems relevant to the business objectives. Unlike BCP though, a DRP plan can include different environment types such as a cold site, warm site, and a hot-hot site. A cold site represents a location where business processes can be recovered to after updates and setup take place. A cold site requires the most amount of time to prepare for DRP events. A warm site is a site that has infrastructure and software ready for DRP events, but lacks all of the required components for activating DRP procedures. A hot-hot site is a fully active and replicated site where DRP events are transitioned rapidly.  
