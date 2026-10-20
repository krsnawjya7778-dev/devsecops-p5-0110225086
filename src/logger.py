import datetime

def log_event(message: str):
    """
    Mencatat log aktivitas aplikasi dengan timestamp.
    """
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_log = f"[{timestamp}] INFO: {message}"
    print(formatted_log)
    return formatted_log