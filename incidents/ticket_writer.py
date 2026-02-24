import os

def write_ticket(incident, output_dir="outputs/tickets"):
    """
    Write incident summary to a Markdown file (Jira-style).
    Includes direct link to relevant runbook.
    """
    os.makedirs(output_dir, exist_ok=True)
    filename = f"{incident['id']}.md"
    filepath = os.path.join(output_dir, filename)

    # Map failure types to runbooks
    runbook_map = {
        "LAN": "runbooks/gateway_down.md",
        "DNS": "runbooks/dns_failure.md",
        "Routing": "runbooks/packet_loss.md",
        "ISP": "runbooks/wifi_outage.md",
        "Healthy": None
    }
    runbook_path = runbook_map.get(incident["failure_type"], None)

    content = f"""# Incident Ticket

**ID:** {incident['id']}
**Timestamp:** {incident['timestamp']}
**Failure Type:** {incident['failure_type']}
**Root Cause:** {incident['root_cause']}
**Severity:** {incident['severity']}

---

### Next Steps
- Review runbook: {runbook_path if runbook_path else "No runbook required"}
- Assign to appropriate team
- Monitor for recurrence
"""

    with open(filepath, "w") as f:
        f.write(content)

    return filepath