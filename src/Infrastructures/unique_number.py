import time

def generate():
    timestamp = int(time.time())  # Get current timestamp
    return f"LN-{timestamp}"
