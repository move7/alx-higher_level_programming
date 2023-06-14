#!/usr/bin/python3
def common_elements(set_1, set_2):
    if len(set_1) > len(set_2):
        set_1, set_2 = set_2, set_1
    set_common = set()
    for i in set_1:
        if i in set_2 and i not in set_common:
            set_common.add(i)
    return set_common
