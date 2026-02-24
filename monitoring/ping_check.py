import subprocess
from utils.logger import get_logger

logger = get_logger()

def ping_host(host, count=2, timeout=2):
    """
    Perform ICMP ping to check reachability and latency.
    Works on Windows using 'ping -n'.
    """
    try:
        result = subprocess.run(
            ["ping", "-n", str(count), "-w", str(timeout * 1000), host],
            capture_output=True, text=True
        )
        logger.info(f"Ping result for {host}: {result.stdout}")
        return result.stdout
    except Exception as e:
        logger.error(f"Ping failed for {host}: {e}")
        return None