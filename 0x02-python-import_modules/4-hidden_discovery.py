#!/usr/bin/python3
import sys
import hidden_4
if __name__ == "__main__":
    list_names = dir(hidden_4)
    for name in list_names:
        if name[:2] != "__":
            print("{}".format(name))
