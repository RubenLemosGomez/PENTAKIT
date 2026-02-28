<div align="center">
  <img src="./assets/banner.gif" width="800" alt="PentaKit"/>
</div>

<div align="center">

```
╔══════════════════════════════════════════════════════════════════════════╗
║                                                                          ║
║    root@pentakit:~$ pentakit auto --company "Target Corp"                ║
║                                                                          ║
║    [■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■] 100%                      ║
║                                                                          ║
║    🔴 4 critical  🟠 9 high  🟡 6 medium  🟢 2 low                       ║
║    📄 report saved → reports/targetcorp_20250115.pdf                     ║
║                                                                          ║
╚══════════════════════════════════════════════════════════════════════════╝
```

# 🔐 PentaKit

### *The Business Penetration Testing Toolkit*

**"The first open-source toolkit that goes from company name to full professional pentest report in a single command."**

---

[![Python](https://img.shields.io/badge/Python-3.12-00ff41?style=for-the-badge&logo=python&logoColor=white&labelColor=0d0d0d)](https://python.org)
[![MongoDB](https://img.shields.io/badge/MongoDB-Integrated-00ff41?style=for-the-badge&logo=mongodb&logoColor=white&labelColor=0d0d0d)](https://mongodb.com)
[![Docker](https://img.shields.io/badge/Docker-Ready-00ff41?style=for-the-badge&logo=docker&logoColor=white&labelColor=0d0d0d)](https://docker.com)
[![License](https://img.shields.io/badge/License-MIT-00ff41?style=for-the-badge&labelColor=0d0d0d)](./LICENSE)
[![Status](https://img.shields.io/badge/Status-Active_Development-ff6600?style=for-the-badge&labelColor=0d0d0d)]()
[![Author](https://img.shields.io/badge/By-Manteigha-00ff41?style=for-the-badge&labelColor=0d0d0d)](https://github.com/RubenLemosGomez)

---

> ⚠️ **DISCLAIMER:** PentaKit is designed exclusively for authorized security testing, bug bounty programs, CTF competitions, and educational purposes. The author is not responsible for any misuse. Always obtain explicit written authorization before testing any system you do not own.

</div>

---

## 📖 Table of Contents

- [What is PentaKit?](#-what-is-pentakit)
- [Why PentaKit vs the competition?](#-why-pentakit-vs-the-competition)
- [Features](#-features)
- [Architecture](#-architecture)
- [Quick Start](#-quick-start)
- [Modules](#-modules)
- [API Integrations](#-api-integrations)
- [Auto Mode](#-auto-mode---the-crown-jewel)
- [Reports](#-reports)
- [MongoDB Persistence](#-mongodb-persistence)
- [Docker Lab](#-docker-lab)
- [Roadmap](#-roadmap)
- [Contributing](#-contributing)

---

## 🎯 What is PentaKit?

PentaKit is a **professional business pentesting toolkit** built in Python 3 from scratch. Unlike other frameworks that just wrap existing tools, PentaKit features its own modules, integrates over **10 external intelligence APIs**, and connects every phase of a pentest — from OSINT to exploitation to report generation — into a single unified pipeline.

You type one command. PentaKit does the rest.

```bash
pentakit auto --company "Empresa SA"
```

```
[OSINT]    Querying 10+ intelligence sources...
           → Domain:     empresa.com
           → Emails:     admin@empresa.com, dev@empresa.com (+14 more)
           → Employees:  23 found via LinkedIn
           → Breaches:   "LinkedIn 2021", "Adobe 2013" — 847 credentials
           → GitHub:     API key leaked in public repo (3 days ago)
           → Shodan:     Apache 2.4.49 exposed on port 8080

[RECON]    Mapping attack surface...
           → Subdomains: 31 found (admin.empresa.com, api.empresa.com...)
           → Live hosts:  18 responding
           → Open ports:  80, 443, 22, 8080, 3306
           → Tech stack:  Apache 2.4.49 · WordPress 5.8 · PHP 7.4.12

[CVE]      Matching versions against vulnerability databases...
           → CVE-2021-41773  CVSS 9.8  🔴 CRITICAL  PoC available
           → CVE-2021-42013  CVSS 9.8  🔴 CRITICAL  RCE confirmed
           → CVE-2021-26084  CVSS 9.8  🔴 CRITICAL  Confluence RCE
           → EPSS Score: 0.97 — actively exploited in the wild
           → KEV Catalog: CISA confirmed active exploitation

[WEB]      Scanning web attack surface...
           → XSS:          /search?q= parameter vulnerable
           → SQLi:         /product?id= time-based injection confirmed
           → CSRF:         /transfer form missing token
           → Secrets:      AWS_KEY found in /static/app.js

[PASSWORDS] Testing leaked credentials against live services...
           → admin@empresa.com:password123  ✅ VALID on /wp-admin

[NETWORK]  Analyzing network security...
           → TLS 1.0 enabled — weak cipher suites
           → SSH port 22 open — default banner exposed

[MONGODB]  Persisting results...
           → scan_id: 507f1f77bcf86cd799439011

[REPORT]   Generating professional report...
           → reports/empresa_sa_20250115.html  ✅
           → reports/empresa_sa_20250115.pdf   ✅
           → reports/empresa_sa_20250115.json  ✅

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅  Audit completed in 6m 42s
🔴  4 critical   🟠  9 high   🟡  6 medium   🟢  2 low
📄  Report ready to submit to HackerOne / Bugcrowd
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## 🆚 Why PentaKit vs the competition?

| Feature | fsociety | Burp Suite Pro | Nessus | ProjectDiscovery | **PentaKit** |
|---|:---:|:---:|:---:|:---:|:---:|
| Company → Report (1 command) | ❌ | ❌ | ❌ | ❌ | ✅ **UNIQUE** |
| Native OSINT (10+ APIs) | ❌ | ❌ | ❌ | ❌ | ✅ **UNIQUE** |
| EPSS + KEV priority scoring | ❌ | ❌ | ❌ | ❌ | ✅ **UNIQUE** |
| Credential stuffing from breaches | ❌ | ❌ | ❌ | ❌ | ✅ **UNIQUE** |
| HackerOne/Bugcrowd ready reports | ❌ | ❌ | ❌ | ❌ | ✅ **UNIQUE** |
| MongoDB scan history | ❌ | ❌ | ❌ | ❌ | ✅ |
| Nuclei 9000+ templates | ❌ | ❌ | ❌ | ✅ | ✅ |
| Real-time alerts (Telegram/Slack) | ❌ | ❌ | ❌ | ✅ | ✅ |
| Web hacking | ⚠️ wrappers | ✅ | ❌ | ⚠️ | ✅ |
| CVE detection | ❌ | ❌ | ✅ | ⚠️ | ✅ |
| Network / MITM | ⚠️ wrappers | ❌ | ✅ | ❌ | ✅ |
| Wireless testing | ⚠️ wrappers | ❌ | ❌ | ❌ | ✅ |
| Post exploitation | ⚠️ wrappers | ❌ | ❌ | ❌ | ✅ |
| Python 3 native | ❌ (py2) | — | — | ✅ | ✅ |
| Open source | ✅ | ❌ | ❌ | ✅ | ✅ |
| **Price** | Free | **$449/yr** | **$3,990/yr** | Free | **🆓 Free** |

---

## ✨ Features

### 🚀 Auto Mode
Full automated audit from a single company name. OSINT → Recon → CVE → Web → Network → Report. No human intervention required.

### 👤 OSINT Engine
Query 10+ intelligence APIs simultaneously: Shodan, Censys, FOFA, ZoomEye, Criminal IP, Hunter.io, HaveIBeenPwned, VirusTotal, SecurityTrails, GitHub, URLScan. All results cross-referenced and deduplicated.

### 🎯 Bug Bounty Core
The heart of PentaKit. Nuclei with 9000+ templates, CVE detection with **EPSS scoring** (exploit probability) and **KEV catalog** (actively exploited), plus 15 vulnerability classes: XSS, SQLi, CSRF, SSRF, XXE, CORS, CRLF, LFI, Open Redirect, Secrets, Subdomain Takeover, 403 Bypass, HTTP Smuggling, API fuzzing, SSL/TLS analysis.

### 🧠 Intelligent CVE Prioritization
Not all CVEs are equal. PentaKit crosses NVD data with:
- **CVSS Score** — severity rating
- **EPSS Score** — probability of exploitation in next 30 days
- **KEV Catalog** — CISA confirmed active exploitation in the wild

This means PentaKit tells you not just *what* is vulnerable, but *what to fix first*.

### 🍃 MongoDB Persistence
Every scan, every finding, every CVE — persisted and queryable. Compare scans over time, track remediation, search across all your targets. The memory that no other free tool has.

### 📄 Professional Reports
HTML, PDF, and JSON reports designed to be submitted directly to bug bounty platforms. Includes CVSS scores, reproduction steps, evidence, CVE references, and a professional executive summary.

### 🔔 Real-time Alerts
Critical finding? PentaKit notifies you instantly via Telegram, Slack, or Discord webhook. Never miss a 9.8 CVSS again.

---

## 🏗️ Architecture

```
pentakit/
├── core/
│   ├── cli.py                    # Rich TUI — unified entry point
│   ├── db.py                     # MongoDB — persistent memory
│   ├── reporter.py               # HTML / PDF / JSON reports
│   ├── scope.py                  # Ethical guardian — validates targets
│   ├── orchestrator.py           # Auto Mode pipeline
│   ├── api_manager.py            # Centralized API key management
│   └── notifier.py               # Telegram / Slack / Discord alerts
│
├── modules/
│   ├── 00_auto/                  # 🚀 Full audit orchestration
│   ├── 01_recon/                 # 🔍 Subfinder · Amass · httpx · Nmap
│   ├── 02_osint/                 # 👤 Shodan · Censys · FOFA · HIBP · GitHub
│   ├── 03_bugbounty/             # 🎯 Nuclei · CVE · EPSS · KEV · 15 vuln types
│   ├── 04_password_attacks/      # 🔑 CeWL · Hashcat · Hydra · Credential stuffing
│   ├── 05_wireless/              # 📡 WiFi · WPA2 · Evil Twin · Bluetooth
│   ├── 06_exploitation/          # 💥 CVE PoCs · CMS · RCE · File upload
│   ├── 07_sniffing_spoofing/     # 🕵️  ARP · SSL Strip · DNS spoof · Bettercap
│   ├── 08_web_hacking/           # 🌐 CMS · FFuf · Nikto · GraphQL · CF bypass
│   ├── 09_post_exploitation/     # 💀 Shell mgmt · LinPEAS · Impacket · Cleanup
│   └── 10_reporting/             # 📄 HTML · PDF · JSON · HackerOne format
│
├── wordlists/                    # SecLists + custom payloads
├── nuclei-templates/             # 9000+ templates (community + custom)
├── reports/                      # Generated audit reports
├── scope.yaml                    # Authorized targets
├── api_keys.yaml                 # API key configuration
├── docker-compose.yml            # Full environment in one command
└── main.py                       # Entry point
```

---

## ⚡ Quick Start

### Prerequisites
- Python 3.12+
- Docker & Docker Compose
- Mac M2 / Linux / WSL2

### Installation

```bash
# Clone the repository
git clone https://github.com/RubenLemosGomez/pentakit.git
cd pentakit

# Install dependencies
pip install -r requirements.txt

# Configure API keys (optional — works without, more power with)
cp api_keys.example.yaml api_keys.yaml
# Edit api_keys.yaml with your keys

# Launch full environment (MongoDB + lab targets)
docker-compose up -d

# Run PentaKit
python main.py
```

### First scan

```bash
# Interactive menu
python main.py

# Direct command — Bug Bounty scan
python main.py bugbounty --url https://example.com

# Full automated audit
python main.py auto --company "Example Corp"

# OSINT only
python main.py osint --target example.com

# Network analysis
python main.py network --interface en0 --mode passive
```

---

## 📦 Modules

### 🔍 01 — Information Gathering
```bash
python main.py recon --target example.com
```
Subdomain enumeration (Subfinder + Amass + crt.sh), port scanning (Nmap + Masscan), technology fingerprinting, WAF/CDN detection, cloud asset enumeration (AWS, GCP, Azure), historical URLs (Wayback Machine + GAU), parameter discovery (ParamSpider).

---

### 👤 02 — OSINT
```bash
python main.py osint --target example.com
python main.py osint --company "Example Corp"
```
Company intelligence from 10+ sources: exposed emails, employee enumeration, breach data, GitHub leaks, metadata extraction from public documents, IP history, subdomain history, VirusTotal reputation, URLScan history.

---

### 🎯 03 — Bug Bounty ⭐
```bash
python main.py bugbounty --url https://example.com
```
The flagship module. Nuclei with 9000+ templates, CVE detection with EPSS + KEV prioritization, and 15 vulnerability scanners: XSS (reflected + stored), SQLi (error + time-based), CSRF, SSRF (AWS metadata + localhost), XXE, CORS misconfiguration, CRLF injection, LFI, Open Redirect, Secret leaks (API keys, tokens, passwords in JS/HTML), Subdomain Takeover (50+ service fingerprints), 403 bypass techniques, HTTP Request Smuggling, API endpoint fuzzing (FFuf), SSL/TLS analysis.

---

### 🔑 04 — Password Attacks
```bash
python main.py passwords --target example.com
```
CeWL-based custom wordlist generation from the target website, wordlists enriched with OSINT data (employee names, company terms, breach patterns), offline hash cracking (Hashcat), online brute force (Hydra — SSH, FTP, HTTP, RDP, SMTP), automated credential stuffing using credentials found in breach data.

---

### 📡 05 — Wireless Testing
```bash
python main.py wireless --interface en0
```
WiFi network scanner (encryption type, signal strength), WPA2 handshake analysis, Evil Twin AP for authorized audits, Bluetooth device discovery. **Requires explicit authorization.**

---

### 💥 06 — Exploitation Tools
```bash
python main.py exploit --target example.com
```
CVE exploitation with public PoC validation, CMS-specific exploits (WordPress, Joomla, Drupal), automated SQLi exploitation, Remote Code Execution testing, FTP misconfiguration bypass, file upload restriction bypass.

---

### 🕵️ 07 — Sniffing & Spoofing
```bash
python main.py sniff --interface en0 --mode passive
```
ARP spoofing (Scapy), SSL Strip (HTTPS downgrade), full packet capture and analysis, DNS spoofing, SMTP open relay testing, Bettercap integration for advanced MITM. **Requires authorization on the network being tested.**

---

### 🌐 08 — Web Hacking
```bash
python main.py web --url https://example.com
```
CMS vulnerability scanner (WP plugins, Joomla, Drupal), directory/file fuzzing (FFuf + Nikto), admin panel finder, exposed backup file finder (ZIP, SQL, tar.gz), Cloudflare real-IP bypass, GraphQL introspection and attack surface mapping.

---

### 💀 09 — Post Exploitation
```bash
python main.py postexploit --session <id>
```
Shell session management, privilege escalation detection (LinPEAS/WinPEAS), lateral movement (Impacket), persistence technique analysis, evidence cleanup. **Authorized engagements only.**

---

## 🌐 API Integrations

PentaKit integrates 13 external APIs for maximum intelligence coverage. All are optional — PentaKit works without API keys but is significantly more powerful with them.

| API | Purpose | Free Tier |
|---|---|---|
| [Shodan](https://shodan.io) | Internet-exposed devices | ✅ Limited |
| [Censys](https://censys.io) | Certificates + open ports | ✅ Limited |
| [FOFA](https://fofa.info) | Global asset discovery | ✅ Limited |
| [ZoomEye](https://zoomeye.org) | Cyberspace search engine | ✅ Limited |
| [Criminal IP](https://criminalip.io) | Threat intelligence | ✅ Limited |
| [Hunter.io](https://hunter.io) | Corporate email discovery | ✅ 25/mo |
| [HaveIBeenPwned](https://haveibeenpwned.com) | Breach detection | ✅ Free |
| [VirusTotal](https://virustotal.com) | Domain reputation | ✅ Limited |
| [SecurityTrails](https://securitytrails.com) | DNS + subdomain history | ✅ Limited |
| [URLScan.io](https://urlscan.io) | Web scan history | ✅ Free |
| [GitHub](https://github.com) | Code leak detection | ✅ Free |
| [NVD NIST](https://nvd.nist.gov) | CVE database | ✅ Free |
| [OSV](https://osv.dev) | Open source vulnerabilities | ✅ Free |

---

## 🚀 Auto Mode — The Crown Jewel

```bash
pentakit auto --company "Target Corp"
```

Auto Mode orchestrates all modules in the optimal sequence, passing data between them intelligently:

```
Phase 1 — PASSIVE INTELLIGENCE (zero noise, target unaware)
  ┌─────────────────────────────────────────────────────────┐
  │  Shodan + Censys + FOFA + ZoomEye ──→ exposed assets   │
  │  Hunter.io + LinkedIn ────────────→ emails + employees  │
  │  HaveIBeenPwned + GitHub ─────────→ breaches + leaks   │
  │  SecurityTrails + crt.sh ─────────→ subdomain history  │
  │  VirusTotal + URLScan ────────────→ reputation history  │
  └─────────────────────────────────────────────────────────┘
                          │
                          ▼
Phase 2 — ACTIVE RECONNAISSANCE
  ┌─────────────────────────────────────────────────────────┐
  │  Subfinder + Amass ──────→ enumerate all subdomains     │
  │  httpx ──────────────────→ identify live hosts          │
  │  Naabu + Nmap ───────────→ port + service detection     │
  │  Katana + Wayback ───────→ crawl all URLs               │
  │  ParamSpider ────────────→ discover all parameters      │
  └─────────────────────────────────────────────────────────┘
                          │
                          ▼
Phase 3 — VULNERABILITY DETECTION
  ┌─────────────────────────────────────────────────────────┐
  │  Nuclei (9000+ templates) ────→ CVEs + misconfigs       │
  │  NVD + OSV + KEV + EPSS ──────→ known vulns + priority  │
  │  15 custom scanners ──────────→ web vulnerabilities     │
  │  Credential stuffing ─────────→ from breach data        │
  └─────────────────────────────────────────────────────────┘
                          │
                          ▼
Phase 4 — PERSIST + ALERT
  ┌─────────────────────────────────────────────────────────┐
  │  MongoDB ────────────────→ all findings persisted        │
  │  Telegram/Slack ─────────→ instant critical alerts      │
  └─────────────────────────────────────────────────────────┘
                          │
                          ▼
Phase 5 — PROFESSIONAL REPORT
  ┌─────────────────────────────────────────────────────────┐
  │  HTML ────────→ visual report with evidence             │
  │  PDF ─────────→ professional deliverable                │
  │  JSON ────────→ machine-readable for integrations       │
  │  HackerOne ───→ ready to paste on bug bounty platform   │
  └─────────────────────────────────────────────────────────┘
```

---

## 📄 Reports

PentaKit generates professional reports designed to be submitted directly to clients or bug bounty platforms.

**HTML Report** — Visual report with color-coded severity, payloads, CVE references, and reproduction steps.

**PDF Report** — Professional deliverable generated from HTML via WeasyPrint.

**JSON Report** — Machine-readable structured data for tool integrations and custom processing.

**HackerOne / Bugcrowd Format** — Pre-formatted vulnerability report with title, description, impact statement, reproduction steps, evidence, and CVSS score. Copy, paste, submit.

---

## 🍃 MongoDB Persistence

PentaKit remembers everything across sessions. Every scan builds on previous knowledge.

```
Collections:
  companies       → Target company profile and metadata
  targets         → Full history of scanned hosts
  osint_results   → Emails, employees, breaches, leaks
  scans           → Each complete scan execution
  vulnerabilities → Every finding with status tracking
  cve_cache       → Cached CVE data (7-day TTL auto-refresh)
  credentials     → Found/tested credentials
  reports         → Generated report metadata
```

**Vulnerability Status Tracking:**
```bash
# Mark a vuln as reported to HackerOne
python main.py history --vuln-id abc123 --status reported

# Compare two scans — what changed?
python main.py history --compare scan_id_1 scan_id_2

# Search all findings across all targets
python main.py history --search "SQLi" --severity high
```

---

## 🐳 Docker Lab

Full isolated test environment with one command:

```bash
docker-compose up -d
```

| Container | Purpose | Port |
|---|---|---|
| `pentakit` | Main toolkit | — |
| `mongodb` | Persistent storage | 27017 |
| `dvwa` | Web vulns (XSS, SQLi, CSRF) | 8080 |
| `juiceshop` | API + auth vulnerabilities | 3000 |
| `vulnapi` | REST API vulnerabilities | 8081 |
| `metasploitable` | Network + CVE testing | — |

Test everything locally before any real engagement.

---

## 🗺️ Roadmap

```
v1.0  ✅ Core + Recon + OSINT + Bug Bounty + Web Hacking + Reports
v1.1  🔄 Password Attacks + Credential Stuffing + Sniffing
v1.2  📅 Wireless Testing + Exploitation Tools  
v1.3  📅 Post Exploitation + Advanced Auto Mode
v2.0  📅 Web Dashboard (FastAPI + Chart.js)
v2.1  📅 ML-based Risk Scoring
v2.2  📅 Continuous monitoring mode (24/7 background)
```

---

## 🤝 Contributing

PentaKit is built to grow. Contributions welcome:

1. Fork the repo
2. Create a feature branch: `git checkout -b feat/new-module`
3. Add your module under `modules/` following the existing structure
4. Open a pull request

Please read [CONTRIBUTING.md](./CONTRIBUTING.md) first.

---

## ⚖️ Legal & Ethics

PentaKit is a professional security tool. With great power comes great responsibility.

- ✅ **Authorized** bug bounty programs with active scope
- ✅ **Your own** infrastructure and systems
- ✅ **CTF** competitions and lab environments
- ✅ **Client engagements** with signed authorization
- ❌ **Never** scan systems without explicit written permission
- ❌ Unauthorized scanning is illegal in most jurisdictions

The `scope.yaml` file acts as the ethical guardian — PentaKit will refuse to operate against any target not declared in scope.

---

## 📜 License

MIT License — free to use, modify, and distribute.

---

<div align="center">

```
root@pentakit:~$ echo "Built with ♥ from Vigo, Galicia"
> Built with ♥ from Vigo, Galicia

root@pentakit:~$ echo "If you can't hack it, you don't understand it"
> If you can't hack it, you don't understand it
```

**[⭐ Star this repo](https://github.com/RubenLemosGomez/pentakit)** if PentaKit helps you in your security research.

Made by **[Manteigha](https://github.com/RubenLemosGomez)** — Rubén Lemos Gómez

</div>
