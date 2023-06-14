#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return None
    best_value = float('-inf')
    best_key = 'None'
    for key in a_dictionary:
        if a_dictionary[key] > best_value:
            best_value = a_dictionary[key]
            best_key = key
    return best_key
