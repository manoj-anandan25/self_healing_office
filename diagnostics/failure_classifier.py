from utils.logger import get_logger

logger = get_logger()

def classify_failure(health_results):
    """
    Classify the type of failure based on monitoring results.
    Categories: LAN, DNS, Routing, ISP, Healthy
    """
    if not health_results:
        return "Unknown"

    # Simple heuristics
    if any("Ping request could not find host" in str(v) for v in health_results.values()):
        return "LAN"
    elif any("Non-existent domain" in str(v) for v in health_results.values()):
        return "DNS"
    elif any("Request timed out" in str(v) for v in health_results.values()):
        return "Routing"
    elif any("could not resolve" in str(v).lower() for v in health_results.values()):
        return "ISP"
    else:
        return "Healthy"