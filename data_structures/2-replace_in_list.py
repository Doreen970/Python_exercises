#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """
    a function that replaces an element of a list at a specific position
    """
    n = len(my_list)
    while idx < n:
        if idx < 0:
            return my_list
        elif idx == n:
            return my_list
        else:
            my_list[idx] = element
            return my_list
