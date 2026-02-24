from utils.time_utils import current_timestamp
from incidents.severity_mapper import map_severity
from jira import JIRA
import yaml

def generate_incident(failure_type, root_cause, severity="auto"):
    if severity == "auto":
        severity = map_severity(failure_type)

    incident = {
        "id": f"INCIDENT-{current_timestamp().replace(' ', '-').replace(':','')}",
        "failure_type": failure_type,
        "root_cause": root_cause,
        "severity": severity,
        "timestamp": current_timestamp()
    }

    # Push to Jira
    summary = f"{failure_type} detected"
    description = f"Root cause: {root_cause}\nSeverity: {severity}\nTimestamp: {incident['timestamp']}"
    create_jira_ticket(summary, description)

    return incident

def load_jira_config(config_file="config/jira.yaml"):
    with open(config_file) as f:
        return yaml.safe_load(f)["jira"]

def create_jira_ticket(summary, description, issue_type="Task"):
    config = load_jira_config()
    jira = JIRA(
        server=config["server"],
        basic_auth=(config["email"], config["api_token"])
    )
    issue_dict = {
        "project": {"key": config["project_key"]},
        "summary": summary,
        "description": description,
        "issuetype": {"name": issue_type},
    }
    issue = jira.create_issue(fields=issue_dict)
    print(f"Jira ticket created: {issue.key}")
    return issue.key