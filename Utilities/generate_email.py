import time


def generate_email_time_stamp():
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    timestamp = timestamp.replace('-', '_').replace(' ', '_').replace(':', '_')
    return "arun"+timestamp+"@arcgate.com"

def generate_username_time_stamp():
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    timestamp = timestamp.replace('-', '_').replace(' ', '_').replace(':', '_')
    return "arun"+timestamp
