from utils.logger import get_logger

logger = get_logger()

def find_root_cause(health_results, failure_type):
    """
    Determine likely root cause based on failure classification.
    """
    if failure_type == "LAN":
        return "Local gateway unreachable. Possible switch or AP issue."
    elif failure_type == "DNS":
        return "DNS resolution failed. Check DNS server health or misconfiguration."
    elif failure_type == "Routing":
        return "Routing path broken. Possible upstream router or ISP issue."
    elif failure_type == "ISP":
        return "ISP connectivity issue. Escalate to provider."
    elif failure_type == "Healthy":
        return "No issues detected."
    else:
        return "Root cause unknown."