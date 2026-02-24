import subprocess
from utils.logger import get_logger

logger = get_logger()

def traceroute_host(host):
    """
    Perform traceroute (Windows uses 'tracert').
    """
    try:
        result = subprocess.run(
            ["tracert", host],
            capture_output=True, text=True
        )
        logger.info(f"Traceroute to {host}: {result.stdout}")
        return result.stdout
    except Exception as e:
        logger.error(f"Traceroute failed: {e}")
        return None