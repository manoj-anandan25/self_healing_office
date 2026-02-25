# Self-Healing Office

## Overview
A Python-based agent that monitors network health, classifies failures, generates incidents, and produces post-incident reports. Designed to simulate enterprise triage workflows (LAN/WLAN, DNS, routing, ISP).
![Uploading ChatGPT Image Feb 25, 2026, 02_02_42 PM.png…]()

## Architecture
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

## How to Run
```bash
# Install dependencies
pip install -r requirements.txt

# Run in dry-run mode (no tickets written)
python main.py

# Run in production mode
python main.py --prod
