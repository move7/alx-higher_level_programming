#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    sum1 = 0
    sum2 = 0
    len_a = len(tuple_a)
    len_b = len(tuple_b)
    if len_a >= 1:
        sum1 += tuple_a[0]
        if len_a >= 2:
            sum2 += tuple_a[1]
    if len_b >= 1:
        sum1 += tuple_b[0]
        if len_b >= 2:
            sum2 += tuple_b[1]
    return ((sum1, sum2))
