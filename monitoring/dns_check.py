import subprocess
from utils.logger import get_logger

logger = get_logger()

def dns_lookup(domain="google.com"):
    """
    Perform DNS resolution using nslookup.
    """
    try:
        result = subprocess.run(
            ["nslookup", domain],
            capture_output=True, text=True
        )
        logger.info(f"DNS lookup for {domain}: {result.stdout}")
        return result.stdout
    except Exception as e:
        logger.error(f"DNS lookup failed: {e}")
        return None