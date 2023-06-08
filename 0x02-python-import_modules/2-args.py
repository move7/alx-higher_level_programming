#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    length = len(argv) - 1
    if length > 1:
        print("{} arguments:".format(length))
    else:
        print("{} argument:".format(length))
    for(i=1, i <= length, i++):
        print("{}: {}".format(i, argv[i]))
