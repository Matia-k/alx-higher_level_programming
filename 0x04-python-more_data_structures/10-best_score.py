#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None

    biggest = 0
    for k, v in a_dictionary.items():
        if v > biggest:
            biggest = v
    for k in a_dictionary:
        if a_dictionary[k] == biggest:
            return k
