
#Introduction to the Penetration Tester Path

Pre-Engagement     → understand the scope/contract
Info Gathering     → recon, find targets
Vulnerability Assessment → find weaknesses
Exploitation       → attack the weaknesses
Post-Exploitation  → escalate privileges
Lateral Movement   → move through the network
Proof of Concept   → document and prove the hack
Post-Engagement    → clean up and report

#Exploitation is split into two parts:

Network services running → find misconfigs → exploit them
Web applications running → find vulns → exploit them

Pre-Engagement: Initial documentation and understanding the scope
Info-Gathering: Gathering Information before doing vuln assessment is necessary to understand how to find the vulnerabilities and gaps in the systems
Vulnerability Assessment: Assessing Vulnerabilities and finding in order to perform post-exploitation or exploitation or lateral movement after it
Exploitation: Exploitating the Vulnerabilities is necessary to access the target system
Post-exploitation: It is basically Privilege escalation after exploiting the system
Lateral Movement: Exploiting a dual network and gaining access over it
Proof of Concept: Documenting the Vuln and the process
Post engagement: REporting it to the client

#Risk Management

Find risks → evaluate how bad they are → reduce them as much as possible.

Accept   → live with the risk (low impact, low chance)
Transfer → buy insurance or outsource the risk
Avoid    → stop doing the risky thing entirely
Mitigate → reduce the risk with security controls

#Pentesters job:
✓ Find vulnerabilities
✓ Document them clearly
✓ Show how to reproduce them
✓ Recommend how to fix them

✗ Actually fix the vulnerabilities
✗ Apply patches
✗ Change their code
✗ Monitor their systems ongoing

#Vuln Assessment vs Penetration Tests:

Vuln Assessment  → automated tools only (Nessus, OpenVAS)
                   finds known vulnerabilities
                   quick but misses custom issues
                   
Penetration Test → automated + manual
                   human tester thinks creatively
                   tailored to the specific target
                   finds what automated tools miss\

#External Pentest vs Internal Pentest

External Pentest:

Where you are → outside the company (internet)
What you test → anything publicly accessible
               → website, login portals, VPN endpoints, 
                 email servers, public APIs

Internal Pentest:

Where you are → inside the company network
               (physically on-site or via VPN after breach)
What you test → internal servers, Active Directory,
                databases, internal apps, file shares,
                employee machines

External = you're an outsider trying to get in
Internal = you're already in, seeing how far you can go

1. External pentest → break through the perimeter
2. Get inside the network
3. Internal pentest → see what you can reach from inside

#Types of penetration testing

Blackbox  → you know nothing
            just an IP or domain
            hardest, most realistic
            simulates a real attacker

Greybox   → you know some things
            maybe some URLs, subdomains
            middle ground
            most common in real engagements

Whitebox  → you know everything
            source code, credentials, configs
            fastest, most thorough
            good for finding deep vulnerabilities

Red Team  → full attack simulation
            includes physical break-ins
            social engineering (tricking employees)
            most realistic of all

Purple Team → attackers + defenders work together
              learn from each other
              improve detection and response


#Real-World:

Bug bounty      → Blackbox
Most pentests   → Greybox
Code audit      → Whitebox
Advanced client → Red Team


#Types of testing environments:

Network          → routers, switches, infrastructure
Web App          → websites, web applications
Mobile           → Android/iOS apps
API              → backend endpoints
Thick Clients    → desktop applications
IoT              → smart devices, cameras
Cloud            → AWS, Azure, GCP
Source Code      → review code for vulnerabilities
Physical         → locks, access cards, servers
Employees        → phishing, social engineering
Hosts/Servers    → individual machines
Firewalls/IDS    → security device misconfigs


#Password Spraying

Password spraying is nothing but we use a single password on multiple usernames to get one valid authentication.

User A ──┐
User B ──┼───► Try [ Winter2026! ] ───► Goal: Find 1 valid login without locking accounts
User C ──┘

#The Structure of Information Gathering:

OSINT
↓
Find public info before touching anything
Google, GitHub, LinkedIn, DNS lookups
Goal → leaked creds, subdomains, employee info

Infrastructure Enumeration  
↓
Map the company's entire online presence
DNS servers, mail servers, web servers, cloud
Goal → understand the full attack surface

Service Enumeration
↓
For each server found → what services are running?
FTP, SSH, HTTP, SMB, RDP etc.
What version? Old versions = known vulnerabilities
Goal → find exploitable services

Host Enumeration
↓
For each host → what OS? What ports open?
What does this machine do in the network?
Who does it talk to?
Goal → find misconfigured or vulnerable hosts

Pillaging (after exploitation)
↓
You're already inside a machine
Now steal everything useful
Passwords, config files, SSH keys,
employee data, credentials, scripts
Goal → find data + fuel for next attack


#Vulnerability Assessment

Descriptive  → What do I see?
Diagnostic   → Why does this exist?
Predictive   → What could happen if exploited?
Prescriptive → What should I do about it?


#Exploitation

1. Probability of success  → how likely will it work?
2. Complexity              → how hard is it to execute?
3. Probability of damage   → could it crash the system?

High success + Low complexity + Low damage = Do this first
Low success + High complexity + High damage = Avoid or do last

Can't find working PoC?
→ Set up a VM mirroring the target
→ Same OS, same service versions
→ Test the exploit locally first
→ Make sure it works without breaking things
→ Then run on real target

Not sure if attack will cause damage?
→ Ask the client first
→ Better to ask than crash their production server
→ Always communicate when in doubt

#Post Exploitation 

You're inside now → much easier to get caught
Admin monitoring → one wrong command = alarm

Evasive Testing: 

Three modes:
Evasive        → stay completely hidden
Non-Evasive    → don't care about being caught
Hybrid         → start quiet, get louder gradually


Info Gathering:

Before → you saw the building from outside
Now    → you're inside, see everything differently

Look for:
→ Local network structure
→ Other machines connected
→ Printers, databases, file shares
→ How this machine talks to others

Pillaging:
Steal everything useful from the machine:
→ Passwords in config files
→ SSH keys
→ Scripts with hardcoded credentials
→ Excel/Word files with sensitive data
→ Emails
→ Network interfaces and routing info
→ VPN configs
→ ARP tables (shows other machines)

Persistance:

Problem → if connection drops, you lose access
Solution → install a backdoor before doing anything else

Why first?
→ If your exploit crashes the service
→ You can't get back in same way
→ Persistence = guaranteed re-entry

Privilege Escalation:

You got in as normal user → need admin/root
Why it matters:
→ Normal user = limited access
→ Root/Admin = access to everything

Linux goal  → get root
Windows goal → get SYSTEM or Domain Admin

Two ways:
→ Exploit local vulnerability
→ Find stored credentials of higher privilege user


Data Exfiltration:

Can you actually steal data out of the network?
Companies use DLP and EDR to stop this

Best practice:
→ Don't exfiltrate real sensitive data
→ Create fake data (fake credit cards, fake SSNs)
→ Try to exfiltrate the fake data
→ Tests if security systems catch it
→ You're not liable for real data on your machine

Always ask client before exfiltrating anything
Take screenshots + screen recordings as proof


The full post-exploitation flow:

Get access
→ Establish persistence immediately
→ Gather info from inside
→ Pillage everything useful
→ Assess vulnerabilities from inside
→ Escalate privileges to root/admin
→ Exfiltrate data (fake) as proof
→ Move laterally to other machines


Lateral Movement:

Real attackers don't stop at one machine
They spread through the entire network
Like ransomware → infects one machine
→ spreads to all 5000 machines
→ encrypts everything
→ company pays millions

1. Pivoting        → use hacked machine as bridge
                     to reach other internal machines

2. Evasive Testing → stay hidden from blue team
                     avoid IPS/IDS/EDR alerts

3. Info Gathering  → map the internal network
                     find all reachable hosts

4. Vuln Assessment → internal networks have MORE
                     misconfigs than internet-facing ones

5. Exploitation    → attack internal machines
                     crack passwords, reuse credentials

6. Post-Exploitation → repeat on every new machine


Key-attack techniques:
Pass-the-Hash → steal password hash
               → use hash directly without cracking
               → log in as admin without knowing password

Responder     → tool that intercepts NTLMv2 hashes
               → catch admin hash
               → use it to access other machines


Flow:
Hacked web server
→ pivot to internal network
→ find database server
→ crack or reuse credentials
→ access database
→ find domain admin credentials
→ own entire Active Directory
→ game over for the company

#Proof of Concept(PoC): 

PoC = evidence that the vulnerability actually works

Documentation → written step by step proof
Script/Code   → automated exploit that runs and proves it

Don't just give them a script and call it done

Problem → admins patch ONLY against your script
        → vulnerability still exists
        → different exploit still works

Solution → explain the ROOT CAUSE not just the symptom

Example:
Weak password found → Domain Admin using "Password123"
Wrong fix → change that one password
Right fix → fix the entire PASSWORD POLICY


→ Full attack chain (how you chained multiple flaws)
→ Root cause of each vulnerability
→ Clear remediation advice
→ Fixing one flaw breaks the chain
  but other flaws still exist

#Post-Engagement:

1. Cleanup
   → Delete all tools/scripts from target systems
   → Revert any changes you made
   → Document everything you changed

2. Report (DRAFT first)
   → Attack chain showing full compromise path
   → Executive summary (non-technical language)
   → Each finding with risk rating + how to fix
   → Steps to reproduce every finding
   → Appendices (scope, compromised accounts, 
     files transferred, scan data)

3. Report Review Meeting
   → Walk client through findings
   → Answer questions
   → Clarify anything confusing

4. FINAL Report
   → Client gives feedback on DRAFT
   → You update it
   → Issue FINAL version

5. Post-Remediation Testing
   → Client fixes the vulnerabilities
   → You retest each one
   → Confirm fixed or still vulnerable
   → Issue post-remediation report

6. Data Retention
   → Keep client data encrypted
   → Wipe from your systems after engagement
   → Retain for some time in case questions arise

7. Close Out
   → Wipe all systems
   → Invoice client
   → Send satisfaction survey


Give AI the raw notes for formatting:

Act as an expert technical writer and cybersecurity instructor. 
Clean up, format, and organize my raw HTB study notes into highly scannable Markdown. 
- Use clear visual hierarchies (##, ###).
- Convert comparisons into clean Markdown tables.
- Use ASCII flowcharts for multi-step processes if necessary.
- Highlight critical attack vectors or gotchas using blockquotes.
- Keep the language punchy, direct, and technical.

Here are my raw notes:
[PASTE YOUR MESSY NOTES HERE]


   

