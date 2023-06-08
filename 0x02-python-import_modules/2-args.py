#!/usr/bin/python3
import sys
length = len(argv)
if length > 1:
    print("{} arguments:".format(length))
else:
    print("{} argument:".format(length))
for(i=1, i < length, i++):
    print("{}: {}".format(i, argv[i]))
