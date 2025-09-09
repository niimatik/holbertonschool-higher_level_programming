#!/usr/bin/python3
def best_score(a_dictionary):
    if None in a_dictionary:
        return (None)
    b_value = max(a_dictionary.values(), default=None)
    for k, v in a_dictionary.items():
        if v == b_value:
            return (k)
