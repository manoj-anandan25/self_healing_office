<p align="center">
  <img src="https://github.com/user-attachments/assets/caf62ecd-f1ef-4aa7-87c1-acb154c577eb" alt="Enterprise Architecture" width="800">
</p>

<h1 align="center"> Self-Healing Office</h1>

<p align="center">
  <b>Enterprise Network Incident Lifecycle & Automated Triage Engine</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge&logo=python" alt="Python">
  <img src="https://img.shields.io/badge/Reliability-SRE-red?style=for-the-badge" alt="SRE">
  <img src="https://img.shields.io/badge/Automation-DevOps-success?style=for-the-badge" alt="DevOps">
</p>

---

###  Problem Statement
In large-scale enterprise environments, manual network triage is the primary driver of high **MTTR (Mean Time To Resolution)**. Reactive documentation leads to inconsistent RCA (Root Cause Analysis) and delayed incident response. 

**The Solution:** This project simulates a proactive "Self-Healing" agent that automates the transition from **Detection** to **Documentation**, ensuring every network failure is classified, logged, and mapped to a resolution runbook in seconds—not hours.

###  Engineering Highlights
- **Automated Triage Engine:** Classifies failures into LAN, DNS, Routing, or ISP tiers using multi-stage health signals.
- **Dynamic Severity Mapping:** Real-time P1–P4 escalation logic based on pre-defined enterprise thresholds.
- **Observability-First Design:** Implements structured logging and automated Jira-style Markdown ticket generation.
- **Modular Architecture:** Clean separation of concerns between monitoring, diagnostics, and reporting layers.

---

###  Repository Architecture
```text
self-healing-office/
├── config/          # YAML-based thresholds & monitoring endpoints
├── monitoring/      # Health probes (ICMP Ping, DNS Query, Traceroute)
├── diagnostics/     # RCA Engine & Failure Classification logic
├── incidents/       # Incident lifecycle & P1-P4 mapping
├── reports/         # Automated Post-Incident RCA generation
├── runbooks/        # Markdown-based standard operating procedures (SOPs)
└── main.py          # Application Entry Point

```

---

###  Setup & Execution

1. **Environment Setup**
```bash
git clone [https://github.com/manoj-anandan25/self_healing_office.git](https://github.com/manoj-anandan25/self_healing_office.git)
cd self_healing_office
pip install -r requirements.txt

```


2. **Run the Simulation**
```bash
python main.py

```



---

###  Sample Automated Output (Jira-Style)

> **Incident ID:** `INC-20260225-01`
> **Severity:** `P2 (High)`
> **Issue:** `DNS Resolution Latency`
> **RCA:** `Upstream Provider Timeout (8.8.8.8)`
> **Action:** `Switched to Secondary Resolver; Logged for Audit.`
> **Runbook:** `[view-dns-sop.md](./runbooks/dns.md)`

---

###  Execution Dashboards

<p align="center">
<img src="https://github.com/user-attachments/assets/bd8bbd52-d3d9-413c-81b5-555a12cc5e36" width="32%" />
<img src="https://github.com/user-attachments/assets/1aac5b8b-929f-4c99-9ce8-85e1b2e67e26" width="32%" />
<img src="https://github.com/user-attachments/assets/03deafb7-e177-4c1e-b658-852e6c06a3ea" width="32%" />
</p>

---

<p align="center"> Developed by <b>Manoj Anandan</b> </p>

```

-----


**Ready to move to the `net-config-bot`?** I can give it the same "Enterprise Treatment" to make it look like a professional DevOps tool.

```
