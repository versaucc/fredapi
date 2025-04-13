import re, json
from datetime import datetime

def print_params(params):
    # Convert dict to list, print out elements neat.
    key = list(params.keys())
    for key in params: 
        value = params[key]
        print(f"{key}: {params[key]}")

def clean_string(s, replacement="_"):
    # Replace anything that is not a letter, number, or underscore with the replacement
    return re.sub(r"[^\w]", replacement, s)

def remove_time(dt):
    """
    Removes the time component from a datetime object.
    """
    return dt.date()

def clean_datetime_values(d):
    """
    Loop through dictionary and remove time from all datetime objects.
    """
    for k, v in d.items():
        if isinstance(v, datetime):
            d[k] = remove_time(v)
    return d