#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    bigest_v = 0
    for key in a_dictionary:
        if a_dictionary[key] > bigest_v:
            bigest_v = a_dictionary[key]
    for key in a_dictionary:
        if a_dictionary[key] == bigest_v:
            return key
