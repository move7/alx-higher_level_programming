#!/usr/bin/python3
def uppercase(c):
    for char in c:
        if ord(char) in range(97, 123):
            char = chr(ord(char) - 32)
        print("{}".format(char), end='')
    print()
