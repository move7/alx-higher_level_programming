#!/usr/bini/python3
def uniq_add(my_list=[]):
    sum_uniq = 0
    for i in range(len(my_list)):
        if i == my_list.index(my_list[i]):
            sum_uniq += my_list[i]
    return sum_uniq
