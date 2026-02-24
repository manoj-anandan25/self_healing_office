from datetime import datetime

def current_timestamp():
    return datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")