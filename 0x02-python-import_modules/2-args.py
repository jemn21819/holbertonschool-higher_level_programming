#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    if len(argv) == 2:
        dscrp = "argument:"
    elif len(argv) < 2:
        dscrp = "arguments."
    else:
        dscrp = "arguments:"
    print("{} {}".format(len(argv) - 1, dscrp))
    for i in range(1, len(argv)):
        print("{}: {}".format(i, argv[i]))
