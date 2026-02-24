def map_severity(failure_type):
    """
    Map failure type to severity level (P1–P4).
    """
    if failure_type == "LAN":
        return "P1"  # Critical, office-wide outage
    elif failure_type == "DNS":
        return "P2"  # Major, users cannot resolve domains
    elif failure_type == "Routing":
        return "P2"  # Major, upstream path broken
    elif failure_type == "ISP":
        return "P3"  # External provider issue
    elif failure_type == "Healthy":
        return "P4"  # Informational
    else:
        return "P4"