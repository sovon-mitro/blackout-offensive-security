🕶️ BLACKOUT
Offensive Security Assessment & Automated Reconnaissance Analysis

A hands-on penetration-testing project combining network reconnaissance, vulnerability assessment, controlled exploitation, post-exploitation verification, and Python-based security analysis.

📌 Overview

BLACKOUT is an offensive cybersecurity laboratory project designed to simulate a real-world penetration-testing workflow against an intentionally vulnerable system.

The project begins with network reconnaissance and service enumeration, progresses through vulnerability identification and validation, and concludes with controlled exploitation and privilege verification.

A custom Python tool was also developed to analyze Nmap reconnaissance results and produce a structured security assessment.

Core Workflow
Reconnaissance
      ↓
Service Enumeration
      ↓
Version Detection
      ↓
Vulnerability Research
      ↓
Vulnerability Validation
      ↓
Controlled Exploitation
      ↓
Post-Exploitation
      ↓
Privilege Verification
      ↓
Evidence Collection
      ↓
Automated Analysis

🎯 Objectives

The main goal of BLACKOUT was not simply to exploit a vulnerable machine, but to understand the complete offensive-security process.

Security Objectives
Perform network reconnaissance
Identify exposed services
Fingerprint service versions
Research potential vulnerabilities
Validate vulnerabilities before exploitation
Perform controlled exploitation
Verify obtained privileges
Collect technical evidence
Document the attack chain
Development Objectives
Parse Nmap output using Python
Extract service information
Classify security findings
Identify high-risk services
Build a reusable CLI security-analysis tool

🧪 Laboratory Environment

BLACKOUT was developed inside an isolated VMware laboratory.

System	Role	IP Address
Kali Linux	Attacker / Security Assessment	192.168.254.128
Metasploitable 2	Intentionally Vulnerable Target	192.168.254.130
VMware Workstation Pro	Virtualization	—

Network Architecture
                    VMware Host-Only Network
                              │
                              │
                 ┌────────────┴────────────┐
                 │                         │
                 ▼                         ▼
        ┌─────────────────┐      ┌──────────────────┐
        │   Kali Linux    │      │  Metasploitable 2│
        │                 │      │                  │
        │     ATTACKER    │─────▶│      TARGET      │
        │                 │      │                  │
        │ 192.168.254.128 │      │ 192.168.254.130  │
        └─────────────────┘      └──────────────────┘

Safety: The target is an intentionally vulnerable Metasploitable 2 VM running inside an isolated lab network.

🛠️ Tools & Technologies
Category	Technologies
Operating System	Kali Linux
Target	Metasploitable 2
Virtualization	VMware Workstation Pro
Reconnaissance	Nmap
Exploitation	Metasploit Framework
Post-Exploitation	Meterpreter
Development	Python 3
Parsing	Regular Expressions
Evidence	Nmap / Metasploit output

🔍 Phase 1 — Reconnaissance

Nmap was used to identify exposed TCP services and fingerprint their versions.

The scan discovered:

23 open TCP services

Some of the most relevant findings were:

Port	Service	Version
21	FTP	vsftpd 2.3.4
22	SSH	OpenSSH 4.7p1
23	Telnet	Linux telnetd
80	HTTP	Apache 2.2.8
139	NetBIOS	Samba
445	SMB	Samba
3306	MySQL	5.0.51a
5432	PostgreSQL	8.3.x
5900	VNC	Protocol 3.3
6667	IRC	UnrealIRCd
8180	HTTP	Apache Tomcat

The complete reconnaissance output is preserved in:

recon.txt

🚨 Phase 2 — Vulnerability Identification

The FTP service on port 21 was selected for deeper investigation.

Finding
Attribute	Value
Port	21/tcp
Service	FTP
Version	vsftpd 2.3.4
Vulnerability	CVE-2011-2523
Severity	🔴 Critical

The vsftpd 2.3.4 version is associated with a known backdoor vulnerability.

A version match alone was not considered sufficient evidence. The vulnerability was subsequently validated using Metasploit.

✅ Phase 3 — Vulnerability Validation

The Metasploit module used for validation was:

exploit/unix/ftp/vsftpd_234_backdoor

Metasploit reported:

The target appears to be vulnerable.

This provided an additional validation step before exploitation.

💥 Phase 4 — Controlled Exploitation

The validated vulnerability was exploited against the isolated Metasploitable 2 target.

The exploitation successfully established a:

Meterpreter session

This demonstrated successful remote compromise of the intentionally vulnerable system.

👑 Phase 5 — Privilege Verification

The obtained session was analyzed to determine the level of access.

Identity

Server username: root

Shell Verification

uid=0(root) gid=0(root)

Target
Attribute	Result
Hostname	metasploitable.localdomain
OS	Ubuntu 8.04
Architecture	i686
Account	root
UID	0
Privilege	🔴 Root

Attack Chain
FTP Service
     │
     ▼
vsftpd 2.3.4
     │
     ▼
CVE-2011-2523
     │
     ▼
Vulnerability Validation
     │
     ▼
Controlled Exploitation
     │
     ▼
Meterpreter Session
     │
     ▼
Root Access

🐍 BLACKOUT Python Analyzer

The project includes a custom Python tool that analyzes Nmap reconnaissance output.

Input

recon.txt

Processing
Nmap Output
     │
     ▼
Service Parser
     │
     ▼
Version Extraction
     │
     ▼
Finding Classification
     │
     ▼
Risk Identification
     │
     ▼
Security Assessment
Example
=============================================================
              BLACKOUT SECURITY ASSESSMENT
=============================================================


Target services discovered: 23


ATTACK SURFACE
-------------------------------------------------------------
21/tcp  ftp       CRITICAL  vsftpd 2.3.4
22/tcp  ssh       INFO      OpenSSH 4.7p1
23/tcp  telnet    HIGH      Linux telnetd
...


KEY FINDINGS
-------------------------------------------------------------


[CRITICAL] Port 21/tcp
Service : ftp
Version : vsftpd 2.3.4
CVE     : CVE-2011-2523
Reason  : Known vsftpd 2.3.4 backdoor vulnerability
Run

python3 blackout.py recon.txt

📂 Project Structure
blackout/
│
├── README.md
├── blackout.py
├── recon.txt
│
└── evidence/
    ├── nmap.txt
    └── vulnerability.txt
Components

blackout.py
Custom Python reconnaissance analysis and finding-classification tool.

recon.txt
Raw Nmap service enumeration output.

evidence/nmap.txt
Preserved Nmap reconnaissance evidence.

evidence/vulnerability.txt
Vulnerability validation, exploitation, and privilege-verification evidence.

📊 Results
Metric	Result
Target	Metasploitable 2
Open TCP Services	23
Primary Vulnerability	CVE-2011-2523
Vulnerable Service	vsftpd 2.3.4
Vulnerability Validation	✅ Successful
Exploitation	✅ Successful
Meterpreter Session	✅ Obtained
Root Access	✅ Verified
Python Automation	✅ Implemented
🧠 Skills Demonstrated
Offensive Security
Network reconnaissance
Port scanning
Service enumeration
Version fingerprinting
Vulnerability research
Vulnerability validation
Controlled exploitation
Meterpreter
Post-exploitation
Privilege verification
Security Engineering
Python scripting
Nmap output parsing
Regular expressions
Finding classification
Security automation
Evidence collection
Technical documentation
Infrastructure
VMware networking
Host-only network configuration
Linux environments
Attacker/target lab architecture
🚀 Roadmap
v1.1
 Improve service parsing
 Expand vulnerability detection
 Add confidence scoring
 Add CVE mapping
v1.2
 CVSS risk scoring
 JSON output
 Better CLI interface
 Automated evidence collection
v2.0
 HTML penetration-testing reports
 Attack-chain visualization
 Modular vulnerability engine
 Automated assessment workflow
 Unit testing
⚠️ Disclaimer

BLACKOUT was developed and tested exclusively within an authorized laboratory environment using an intentionally vulnerable Metasploitable 2 virtual machine.

The techniques demonstrated by this project can compromise real systems.

Do not use these techniques against systems, networks, accounts, or services without explicit authorization.

The author is not responsible for misuse of the information or tools contained in this repository.

👤 Author
Sovon Mitro

Cybersecurity | Penetration Testing | Python | AI/ML
