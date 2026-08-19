BLACKOUT
Offensive Security Assessment & Reconnaissance Analysis

BLACKOUT is a hands-on offensive cybersecurity project built to demonstrate an end-to-end penetration-testing workflow in an isolated VMware laboratory.

The project combines network reconnaissance, vulnerability validation, controlled exploitation, post-exploitation verification, and Python-based analysis of Nmap results.

Lab Environment: All security testing was performed against an intentionally vulnerable Metasploitable 2 virtual machine in an isolated laboratory environment.

🎯 Objectives

BLACKOUT was developed to gain practical experience with:

Network reconnaissance
TCP port and service enumeration
Service and version fingerprinting
Vulnerability research
Vulnerability validation
Controlled exploitation
Post-exploitation verification
Security evidence collection
Python-based security automation
Penetration-testing methodology

🏗️ Lab Architecture

Attacker: Kali Linux — 192.168.254.128

Target: Metasploitable 2 — 192.168.254.130

Network: VMware Host-Only Network

Kali Linux
192.168.254.128
     │
     │ Host-Only Network
     │
     ▼
Metasploitable 2
192.168.254.130


Environment
Component	Role	IP Address
Kali Linux	Attacker / Assessment System	192.168.254.128
Metasploitable 2	Intentionally Vulnerable Target	192.168.254.130
VMware Workstation Pro	Virtualization Platform	—
🛠️ Technologies & Tools
Offensive Security
Kali Linux
Nmap
Metasploit Framework
Meterpreter
Metasploitable 2
Development
Python 3
Regular Expressions
Command-line processing
Nmap output parsing

🔎 Assessment Methodology

BLACKOUT follows a simplified penetration-testing methodology:

Reconnaissance
Service Enumeration
Version Identification
Vulnerability Research
Vulnerability Validation
Controlled Exploitation
Post-Exploitation
Privilege Verification
Evidence Collection
Automated Analysis
1. Reconnaissance

Nmap was used to discover exposed TCP services and identify their versions.

The assessment identified 23 open TCP services, creating a broad attack surface for further investigation.

The original reconnaissance output is preserved in:

recon.txt

Examples of discovered services included:

Port	Service	Version / Information
21/tcp	FTP	vsftpd 2.3.4
22/tcp	SSH	OpenSSH 4.7p1
23/tcp	Telnet	Linux telnetd
80/tcp	HTTP	Apache 2.2.8
139/tcp	NetBIOS	Samba
445/tcp	SMB	Samba
3306/tcp	MySQL	MySQL 5.0.51a
5432/tcp	PostgreSQL	PostgreSQL 8.3.x
5900/tcp	VNC	VNC 3.3
6667/tcp	IRC	UnrealIRCd
8180/tcp	HTTP	Apache Tomcat
2. Vulnerability Identification

During service enumeration, the following service was selected for further investigation:

Field	Finding
Port	21/tcp
Service	FTP
Version	vsftpd 2.3.4
Vulnerability	CVE-2011-2523
Severity	Critical

The identified version is associated with the vsftpd 2.3.4 backdoor vulnerability (CVE-2011-2523).

A version match alone was not treated as proof of successful exploitation. The finding was subsequently validated in the laboratory.

3. Vulnerability Validation

Metasploit was used to validate the identified vulnerability.

The module used was:

exploit/unix/ftp/vsftpd_234_backdoor

The vulnerability check reported:

The target appears to be vulnerable.

This provided a validation step before proceeding with controlled exploitation.

4. Controlled Exploitation

The validated vulnerability was exploited exclusively against the isolated Metasploitable 2 laboratory target.

A Meterpreter session was successfully established.

This demonstrated successful remote compromise of the intentionally vulnerable system.

5. Post-Exploitation Verification

The obtained session was examined to verify the level of access and identify the compromised system.

Identity Verification

Server username: root

Shell Verification

uid=0(root) gid=0(root)

Target Information
Attribute	Result
Hostname	metasploitable.localdomain
Operating System	Ubuntu 8.04
Architecture	i686
Privilege	Root
UID	0

The evidence demonstrates that the controlled exploitation resulted in root-level access to the laboratory target.

🐍 Python Analysis Tool

BLACKOUT includes a Python-based tool for analyzing Nmap reconnaissance data.

The current implementation:

Reads Nmap service/version output.
Extracts discovered services.
Classifies selected findings.
Highlights potentially important services.
Maps known findings to vulnerability information.
Produces a structured security assessment.
Usage

python3 blackout.py recon.txt

Example Output

The tool produces an assessment containing:

Discovered services
Service severity
Key findings
Associated CVEs
Vulnerability reasoning
Attack-chain information

Example finding:

CRITICAL — Port 21/tcp

Service: FTP
Version: vsftpd 2.3.4
CVE: CVE-2011-2523
Reason: Known vsftpd 2.3.4 backdoor vulnerability

📁 Project Structure
blackout/
├── README.md
├── blackout.py
├── recon.txt
└── evidence/
    ├── nmap.txt
    └── vulnerability.txt
blackout.py

Python-based Nmap analysis and security finding classification tool.

recon.txt

Raw Nmap reconnaissance output used as input for the Python analysis tool.

evidence/nmap.txt

Preserved Nmap reconnaissance evidence from the laboratory assessment.

evidence/vulnerability.txt

Documentation of vulnerability identification, validation, exploitation, and privilege verification.

📊 Assessment Results
Category	Result
Target	Metasploitable 2
Open TCP Services	23
Primary Finding	vsftpd 2.3.4
CVE	CVE-2011-2523
Vulnerability Validation	Successful
Exploitation	Successful
Session	Meterpreter
Privilege Level	Root
UID	0
Automation	Python
🧠 Skills Demonstrated
Offensive Security
Reconnaissance
Port scanning
Service enumeration
Version fingerprinting
Vulnerability research
Vulnerability validation
Controlled exploitation
Meterpreter
Post-exploitation
Privilege verification
Network Security
TCP services
Host-only networking
Attack-surface analysis
Service exposure analysis
Security Automation
Python scripting
Regular expressions
Security-tool output parsing
Finding classification
CLI-based security tooling
🚀 Future Development

Planned improvements for future versions:

 CVE database integration
 CVSS-based risk scoring
 Vulnerability confidence scoring
 JSON output
 HTML security reports
 Automated evidence collection
 Attack-chain visualization
 Modular vulnerability detection
 Unit testing
 Additional Nmap output formats

These features are planned for future versions and are not part of the current implementation.

⚠️ Disclaimer

BLACKOUT was developed and tested exclusively in an authorized laboratory environment using an intentionally vulnerable Metasploitable 2 virtual machine.

The techniques demonstrated in this project can compromise real systems.

Do not use these techniques against systems, networks, accounts, or services without explicit authorization.

The author is not responsible for misuse of the information or tools contained in this repository.

👤 Author

Sovon Mitro

Cybersecurity | Penetration Testing | Python | AI/ML
