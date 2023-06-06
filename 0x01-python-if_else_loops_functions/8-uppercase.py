#!/usr/bin/python3
def uppercase(c):
    for char in c:
        if 97 <= ord(c) <= 123:
            print("{}".format(chr(ord(char) - 32)), end='')
        else:
            print("{}".format(c), end='')
