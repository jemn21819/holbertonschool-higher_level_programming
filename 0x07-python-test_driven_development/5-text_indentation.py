#!/usr/bin/python3
"""
Module text_indentation
prints a text with 2 new lines after each
of these characters . ? :
"""


def text_indentation(text):
    """text_indentation
    Arguments:
        text {[type]} -- [description]
    Raises:
        TypeError: [description]
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    text = text.rstrip(' ')
    for i in range(len(text)):
        if text[i] == ' ' and text[i + 1] == ' ':
            continue
        if text[i] is ' ' and text[i - 1] is '.':
            continue
        if text[i] is ' ' and text[i - 1] is '?':
            continue
        if text[i] is ' ' and text[i - 1] is ':':
            continue
        if text[i] is ' ' and text[i - 1] is ' ':
            continue
        print(text[i], end='')
        if text[i] == '.' or text[i] == '?' or text[i] == ':':
            print()
            print()
