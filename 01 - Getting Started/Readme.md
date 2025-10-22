Don't Panic!!

Security does not have to be a difficult or intimidating topic.  

If you are a small to medium sized organization looking to improve your security, start with a few basic things:
 - Make sure you have antivirus setup on all machines / properly enabled. *Why:* Protects against malware and viruses that can steal data or disrupt operations.
 - Use MFA everywhere you can. *Why:* Adds an extra layer of security beyond passwords to prevent unauthorized access.
 - Select strong and unique passwords (sometimes a password manager can help). *Why:* Weak or reused passwords are easily cracked, leading to account compromises.
 - Set all your systems and software to auto-update or implement a process to manage updates and patches. *Why:* Fixes known vulnerabilities that attackers exploit.
 - Talk to your employees about phishing and malware (basic awareness). *Why:* Human error is the leading cause of breaches; education reduces risks.
 - Take a closer look at what is internet facing, and get help if you have things that concern you in this regard. *Why:* Exposed services can be entry points for attackers.
 - If possible, have someone take a look at your cloud email (O365 or gmail) settings and any firewalls or Wi-Fi configurations you may have. *Why:* Misconfigurations in these can lead to data leaks or unauthorized access.
 - Be sure to back up your data and make sure you have back ups in a secure, different location from your business. *Why:* Ensures recovery from ransomware, hardware failure, or other data loss events.

## Next Steps: Assessing Your Current State

Once you've implemented these basics, assess your current security posture:
- Conduct a self-audit: Check off each tip and note any gaps.
- Review recent events: Have there been any suspicious emails, failed logins, or system issues?
- Use free tools: Try online vulnerability scanners or basic network mappers to identify exposed assets.
- Seek professional help: If unsure, consult a cybersecurity expert or use services like those from your cloud provider.

This repository is intended to provide a basic overview of key knowledge area of security, for those ready to move beyond the few bullet points above.

Here are a couple of other resources you can leverage:

 - https://www.accidentalciso.net/
 - https://christiant.io//
 - A basic overview video for SMB: https://www.youtube.com/watch?v=bp-dSKiBLIo

![image](https://github.com/user-attachments/assets/07cf6e82-e84e-4bc7-b29f-d9f88e0ead14)

## Updating the Wiki

This repository includes a script, `update_wiki.sh`, that can be used to automatically populate the project's GitHub Wiki. The script will:

1.  Clone the wiki repository.
2.  Clear any existing content.
3.  Copy the `Readme.md` from each numbered directory into the wiki.
4.  Create a `_Sidebar.md` file for navigation.
5.  Push the changes to the remote wiki.

To use the script, you will need to have SSH authentication configured for your GitHub account. Then, simply run the following command from the root of the repository:

```bash
./update_wiki.sh
```
