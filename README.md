# Self-Healing Office

## Overview
A Python-based agent that monitors network health, classifies failures, generates incidents, and produces post-incident reports. Designed to simulate enterprise triage workflows (LAN/WLAN, DNS, routing, ISP).

## Architecture
```
self-healing-office/
├── config/              # Endpoints & thresholds
├── monitoring/          # Health checks (ping, DNS, traceroute)
├── diagnostics/         # Failure classification & RCA
├── incidents/           # Incident generation & ticket writing
├── reports/             # Post-incident RCA reports
├── runbooks/            # Markdown playbooks for common failures
├── outputs/             # Generated tickets & reports
├── utils/               # Logging & helper functions
├── tests/               # Unit tests
└── main.py              # Entry point
```

<img width="1536" height="1024" alt="architecture jpg" src="https://github.com/user-attachments/assets/caf62ecd-f1ef-4aa7-87c1-acb154c577eb" />

##### System Architecture Overview

1. Monitoring Layer
- Ping checks
- DNS resolution
- Traceroute
2. Diagnostics Layer
- Failure classification (LAN / DNS / Routing / ISP)
- Root Cause Analysis engine
3. Incident Layer
- Severity mapping (P1–P4)
- Jira-style Markdown ticket generation
4. Reports Layer
- Post-incident RCA reports
- Direct runbook references
5. Runbooks
- Gateway down
- DNS failure
- Packet loss
- Wi-Fi outage

##### How It Works
1. Health checks run
3. Failure classified
3. Root cause suggested
4. Incident generated
5. Ticket saved
6. RCA report generated
7. Runbook linked

### Execution Output

<img width="1377" height="832" alt="output1" src="https://github.com/user-attachments/assets/bd8bbd52-d3d9-413c-81b5-555a12cc5e36" />
<img width="1313" height="822" alt="output2" src="https://github.com/user-attachments/assets/1aac5b8b-929f-4c99-9ce8-85e1b2e67e26" />
<img width="1147" height="811" alt="output3" src="https://github.com/user-attachments/assets/03deafb7-e177-4c1e-b658-852e6c06a3ea" />

### Feature Highlights
- Dry-run safe mode
- Config-driven thresholds (YAML)
- Modular enterprise architecture
- Automated severity mapping
- Markdown-based Jira-style tickets
- Auto-generated RCA reports
- Direct runbook linking
- Reviewer-friendly outputs
- Unit testing included
- Clean separation of concerns

### Tech Stack
| Category      | Technology                 |
|--------------|----------------------------|
| Language     | Python 3                   |
| Config       | YAML                       |
| Monitoring   | Ping, DNS, Traceroute      |
| Reports      | Markdown                   |
| Logging      | Python Logging             |
| Testing      | Pytest                     |
| Architecture | Modular Design             |

### Enterprise Value
This project simulates a real IT operations workflow:
- Incident lifecycle automation
- Failure classification
- Root cause reporting
- Documentation-first design
- Next step: Jira API integration + multi-host scaling.
