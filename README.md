<p align="center">
  <img src="https://github.com/user-attachments/assets/caf62ecd-f1ef-4aa7-87c1-acb154c577eb" alt="Enterprise Architecture" width="800">
</p>

<h1 align="center">🛠️ Self-Healing Office</h1>

<p align="center">
  <b>Enterprise Network Incident Lifecycle & Automated Triage Engine</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge&logo=python" alt="Python">
  <img src="https://img.shields.io/badge/Reliability-SRE-red?style=for-the-badge" alt="SRE">
  <img src="https://img.shields.io/badge/Automation-DevOps-success?style=for-the-badge" alt="DevOps">
</p>

---

###  Why This Project Matters
Traditional network monitoring tools only alert; they don't analyze. In high-stakes enterprise environments, the gap between **Alerting** and **Resolution** is where money is lost. 

This project simulates a proactive system that **diagnoses, classifies, and documents** incidents in real-time. By automating the triage layer, it demonstrates:
- **SRE Thinking:** Shifting from reactive firefighting to automated reliability.
- **MTTR Reduction:** Eliminating manual steps in the incident documentation phase.
- **Production Observability:** Bridging the gap between raw network signals and actionable Jira-style reports.

---

###  Engineering Highlights
- **Automated Triage Engine:** High-fidelity failure classification (LAN, DNS, Routing, ISP) using multi-stage health signals.
- **Dynamic Severity Mapping:** Real-time P1–P4 escalation logic based on production-grade thresholds.
- **Observability-First Design:** Structured logging paired with automated Markdown-based RCA generation.
- **Modular Architecture:** Clean separation of concerns ensuring the system is scalable and vendor-agnostic.

---

###  Tech Stack

| Category | Technology |
| :--- | :--- |
| **Language** | Python 3.9+ |
| **Configuration** | YAML (Dynamic Thresholds) |
| **Monitoring** | ICMP Ping, DNS Query, Traceroute |
| **Reporting** | Markdown (Jira-Style Templates) |
| **Testing** | Pytest |

---

###  Repository Architecture

```text
self-healing-office/
├── config/          # YAML-based thresholds & monitoring endpoints
├── monitoring/      # Health probes (Network Signal Detection)
├── diagnostics/     # RCA Engine & Failure Classification logic
├── incidents/       # Severity mapping & Ticket generation
├── reports/         # Automated Post-Incident documentation
├── runbooks/        # Markdown-based Standard Operating Procedures (SOPs)
└── main.py          # Core Application Entry Point

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

###  Sample Automated Output (Jira-Style)

> **Incident ID:** `INC-20260225-01`
> **Severity:** `P2 (High)`
> **Issue:** `DNS Resolution Latency`
> **RCA:** `Upstream Provider Timeout (8.8.8.8)`
> **Action:** `Switched to Secondary Resolver; Logged for Audit.`
> **Runbook:** `[view-dns-sop.md](./runbooks/dns.md)`

---

###  Future Roadmap

* [ ] **Jira/ServiceNow API:** Bi-directional sync for automated ticket lifecycle management.
* [ ] **Distributed Probing:** Multi-node monitoring for global infrastructure visibility.
* [ ] **Grafana Integration:** Exporting metrics to Prometheus for real-time visualization.

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
