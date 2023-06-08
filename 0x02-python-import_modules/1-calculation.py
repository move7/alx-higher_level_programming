#!/usr/bin/python3
import calculator_1 as md
if __name__ == "__main__":
    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, md.add(a, b)))
    print("{} - {} = {}".format(a, b, md.sub(a, b)))
    print("{} - {} = {}".format(a, b, md.mul(a, b)))
    print("{} / {} = {}".format(a, b, md.div(a, b)))
