from monitoring.ping_check import ping_host
from monitoring.dns_check import dns_lookup
from monitoring.traceroute_check import traceroute_host
from utils.logger import get_logger

logger = get_logger()

def run_health_checks(endpoints, thresholds):
    """
    Run ping, DNS, and traceroute checks.
    Aggregate results into a health dictionary.
    """
    health = {}

    # Ping gateways
    for gw in endpoints.get("gateways", []):
        health[f"ping_{gw}"] = ping_host(gw)

    # DNS servers
    for dns in endpoints.get("dns_servers", []):
        health[f"dns_{dns}"] = dns_lookup(dns)

    # Traceroute to first gateway
    if endpoints.get("gateways"):
        health["traceroute"] = traceroute_host(endpoints["gateways"][0])

    logger.info("Health checks completed.")
    return health