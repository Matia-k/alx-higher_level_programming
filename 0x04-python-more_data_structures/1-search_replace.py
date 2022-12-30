#!/usr/bin/python5
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    for i in range(len(new_list)):
        if new_list[i] == search:
            new_list.remove(search)
            new_list.insert(i, replace)
    return new_list
