import subprocess

def ping(host, count=2, timeout=2):
    try:
        result = subprocess.run(
            ["ping", "-n", str(count), "-w", str(timeout * 1000), host],
            capture_output=True, text=True
        )
        return result.stdout
    except Exception as e:
        return f"Ping failed: {e}"

def nslookup(domain):
    try:
        result = subprocess.run(
            ["nslookup", domain],
            capture_output=True, text=True
        )
        return result.stdout
    except Exception as e:
        return f"DNS lookup failed: {e}"

def traceroute(host):
    try:
        result = subprocess.run(
            ["tracert", host],
            capture_output=True, text=True
        )
        return result.stdout
    except Exception as e:
        return f"Traceroute failed: {e}"