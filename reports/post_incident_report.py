import os

def generate_report(incident, output_dir="outputs/reports"):
    """
    Generate a post-incident RCA report using the template.
    Includes direct link to relevant runbook.
    """
    os.makedirs(output_dir, exist_ok=True)
    filename = f"RCA-{incident['id']}.md"
    filepath = os.path.join(output_dir, filename)

    # Load template
    template_path = "reports/templates/post_incident_template.md"
    with open(template_path, "r") as f:
        template = f.read()

    # Map failure types to runbooks
    runbook_map = {
        "LAN": "runbooks/gateway_down.md",
        "DNS": "runbooks/dns_failure.md",
        "Routing": "runbooks/packet_loss.md",
        "ISP": "runbooks/wifi_outage.md",
        "Healthy": None
    }
    runbook_path = runbook_map.get(incident["failure_type"], None)

    # Replace placeholders
    report_content = template.replace("{{incident_id}}", incident["id"]) \
        .replace("{{timestamp}}", incident["timestamp"]) \
        .replace("{{failure_type}}", incident["failure_type"]) \
        .replace("{{root_cause}}", incident["root_cause"]) \
        .replace("{{severity}}", incident["severity"])

    # Append runbook reference
    report_content += f"""

## Runbook Reference
{runbook_path if runbook_path else "No runbook required"}
"""

    # Write report
    with open(filepath, "w") as f:
        f.write(report_content)

    return filepath