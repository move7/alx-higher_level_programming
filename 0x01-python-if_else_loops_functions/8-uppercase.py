#!/usr/bin/python3
def uppercase(c):
    for char in c:
        if ord(c) in range(97, 123):
            print("{}".format(chr(ord(char) - 32)), end='')
        else:
            print("{}".format(c), end='')
