#!/usr/bin/python3
def max_integer(my_list=[]):
    length = len(my_list)
    if length == 0:
        return 0
    else:
        return(sorted(my_list)[length - 1])