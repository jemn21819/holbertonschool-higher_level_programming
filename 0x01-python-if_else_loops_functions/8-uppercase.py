#!/usr/bin/python3
def uppercase(str):
    for i in str:
        word = ord(i)
        if i.islower():
            word -= 32
        print("{:c}".format(word), end="")
    print()
