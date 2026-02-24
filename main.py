import argparse
import yaml
from utils.logger import get_logger
from monitoring.health_aggregator import run_health_checks
from diagnostics.failure_classifier import classify_failure
from diagnostics.root_cause_engine import find_root_cause
from incidents.incident_generator import generate_incident
from incidents.ticket_writer import write_ticket
from reports.post_incident_report import generate_report

logger = get_logger()

def load_config():
    with open("config/network_endpoints.yaml") as f:
        endpoints = yaml.safe_load(f)
    with open("config/thresholds.yaml") as f:
        thresholds = yaml.safe_load(f)
    return endpoints, thresholds

def main(prod=False):
    logger.info("Starting Self-Healing Office agent...")
    endpoints, thresholds = load_config()

    # Step 1: Monitoring
    health_results = run_health_checks(endpoints, thresholds)
    logger.info(f"Health results collected.")

    # Step 2: Diagnostics
    failure_type = classify_failure(health_results)
    root_cause = find_root_cause(health_results, failure_type)
    logger.info(f"Failure classified as {failure_type}, root cause: {root_cause}")

    # Step 3: Incident
    incident = generate_incident(failure_type, root_cause, severity="auto")
    logger.info(f"Incident generated: {incident['id']}")

    # Step 4: Ticket writing
    if prod:
        ticket_path = write_ticket(incident, "outputs/tickets")
        logger.info(f"Ticket written to {ticket_path}")

    # Step 5: Report generation
    report_path = generate_report(incident, "outputs/reports")
    logger.info(f"Report generated at {report_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--prod", action="store_true", help="Run in production mode (write tickets)")
    args = parser.parse_args()
    main(prod=args.prod)