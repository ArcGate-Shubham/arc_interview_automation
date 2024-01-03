import time
import string
import random


def generate_email_time_stamp():
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    timestamp = timestamp.replace('-', '_').replace(' ', '_').replace(':', '_')
    return "arun"+timestamp+"@arcgate.com"

def generate_username_time_stamp():
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    timestamp = timestamp.replace('-', '_').replace(' ', '_').replace(':', '_')
    return "arun"+timestamp

def generate_random_string_subject():
    number = 7
    result = ''.join(random.choices(string.ascii_lowercase, k=number))
    return result

def generate_random_dynamic_string(number):
    result = ''.join(random.choices(string.ascii_lowercase, k=number))
    return result
