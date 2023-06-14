#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    set_union = set_1.union(set_2)
    set_diff = set()
    for i in set_union:
        if i not in set_1 or i not in set_2:
            set_diff.add(i)
    return set_diff
