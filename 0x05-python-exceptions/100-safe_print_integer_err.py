#!/usr/bin/python3
from sys import stderr

def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError) as msgerr:
        stderr.write("Exception: {}\n".format(msgerr))
        return False
    return True
