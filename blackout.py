#!/usr/bin/env python3

import re
import sys


def parse_nmap(filename):
    findings = []

    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            match = re.match(
                r"^(\d+)/tcp\s+open\s+(\S+)(?:\s+(.+))?$",
                line.strip()
            )

            if match:
                port = int(match.group(1))
                service = match.group(2)
                version = (match.group(3) or "Unknown").strip()

                findings.append({
                    "port": port,
                    "service": service,
                    "version": version
                })

    return findings


def analyze_finding(finding):
    port = finding["port"]
    service = finding["service"]
    version = finding["version"]

    if service == "ftp" and "vsftpd 2.3.4" in version:
        return {
            "severity": "CRITICAL",
            "cve": "CVE-2011-2523",
            "reason": "Known vsftpd 2.3.4 backdoor vulnerability"
        }

    if port == 1524:
        return {
            "severity": "CRITICAL",
            "cve": "N/A",
            "reason": "Metasploitable root shell service detected"
        }

    if service in ["telnet", "rsh", "login"]:
        return {
            "severity": "HIGH",
            "cve": "N/A",
            "reason": "Legacy remote-access service detected"
        }

    return {
        "severity": "INFO",
        "cve": "N/A",
        "reason": "Service requires further enumeration"
    }


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 blackout.py <nmap_output>")
        sys.exit(1)

    filename = sys.argv[1]
    findings = parse_nmap(filename)

    print("\n" + "=" * 65)
    print("                 BLACKOUT SECURITY ASSESSMENT")
    print("=" * 65)

    print(f"\nTarget services discovered: {len(findings)}")

    print("\nATTACK SURFACE")
    print("-" * 65)

    for finding in findings:
        analysis = analyze_finding(finding)

        print(
            f"{finding['port']:5}/tcp  "
            f"{finding['service']:12} "
            f"{analysis['severity']:8} "
            f"{finding['version']}"
        )

    print("\nKEY FINDINGS")
    print("-" * 65)

    for finding in findings:
        analysis = analyze_finding(finding)

        if analysis["severity"] != "INFO":
            print(f"\n[{analysis['severity']}] Port {finding['port']}/tcp")
            print(f"Service : {finding['service']}")
            print(f"Version : {finding['version']}")
            print(f"CVE     : {analysis['cve']}")
            print(f"Reason  : {analysis['reason']}")

    print("\nATTACK CHAIN")
    print("-" * 65)
    print("Reconnaissance")
    print("      ↓")
    print("Service Enumeration")
    print("      ↓")
    print("Vulnerability Identification")
    print("      ↓")
    print("Controlled Exploitation")
    print("      ↓")
    print("Root Access Verification")

    print("\n" + "=" * 65)


if __name__ == "__main__":
    main()
