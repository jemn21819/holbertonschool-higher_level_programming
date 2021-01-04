#!/usr/bin/python3
from sys import stderr

def safe_function(fct, *args):
    try:
        ptr = fct(*args)
        return (ptr)
    except Exception as msgerr:
        stderr.write("Exception: {}\n".format(msgerr))
        return None
