### **1. Self-Healing Office (The Professional Version)**
<p align="center">
  <img src="https://github.com/user-attachments/assets/caf62ecd-f1ef-4aa7-87c1-acb154c577eb" alt="Architecture" width="800">
</p>

<h1 align="center"> Self-Healing Office</h1>

<p align="center">
  <b>Automated Incident Lifecycle & Network Triage Simulation</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge&logo=python" alt="Python">
  <img src="https://img.shields.io/badge/Net-Automation-orange?style=for-the-badge" alt="Network">
  <img src="https://img.shields.io/badge/Documentation-Jira--Style-success?style=for-the-badge" alt="Docs">
</p>

---

###  Overview
A Python-based agent that monitors network health, classifies failures, and generates enterprise-grade documentation. It simulates a full IT operations workflow, from initial health checks to final RCA (Root Cause Analysis) reports.

###  Enterprise Architecture
```text
self-healing-office/
├── config/          # YAML Endpoints & thresholds
├── monitoring/      # Health checks (Ping, DNS, Traceroute)
├── diagnostics/     # Failure classification & RCA engine
├── incidents/       # Jira-style ticket generation
├── reports/         # Post-incident RCA documentation
├── runbooks/        # Markdown playbooks for standard failures
└── main.py          # Application Entry Point

```

###  How It Works

1. **Monitor:** Active health checks detect latency or outages.
2. **Classify:** Diagnostics engine identifies if the issue is LAN, DNS, Routing, or ISP.
3. **Document:** Automatically generates a Markdown ticket with severity mapping (P1-P4).
4. **Resolve:** Links to specific runbooks and generates a final RCA report.

---

###  Tech Stack

| Category | Technology |
| --- | --- |
| **Language** | Python 3.x |
| **Configuration** | YAML |
| **Reports** | Markdown |
| **Testing** | Pytest |

---

###  Execution Preview

<p align="center">
<img src="https://github.com/user-attachments/assets/bd8bbd52-d3d9-413c-81b5-555a12cc5e36" width="30%" />
<img src="https://github.com/user-attachments/assets/1aac5b8b-929f-4c99-9ce8-85e1b2e67e26" width="30%" />
<img src="https://github.com/user-attachments/assets/03deafb7-e177-4c1e-b658-852e6c06a3ea" width="30%" />
</p>

---

<p align="center"> Developed by <b>Manoj Anandan</b> </p>

### **Why this is better:**

1.  **Fixed Image Gallery:** I used a 3-column layout for your "Execution Output" screenshots so they look like a professional dashboard instead of a long vertical list.
2.  **Cleaned HTML:** Removed the broken `kimg` and replaced it with standard `<p align="center">` and `<img>` tags.
3.  **Visual Hierarchy:** Used emojis and bold headers to make it readable for recruiters.

### **Important Note on the File Structure:**

If you want the "Architecture" section to look "real," you **must** create those folders in your repository.

  * Even if the folders are empty, put a file called `.gitkeep` inside each one.
  * Once you do that, the GitHub sidebar will match your README perfectly.

**Should I help you write the `inventory.yaml` or `requirements.txt` file for the `net-config-bot` next?**

