#!/usr/bin/python3
def element_at(my_list, idx):
    """
    A function that retrieves an element from a list
    """
    n = len(my_list)
    while idx <= n - 1:
        if idx < 0:
            return None
        elif idx >= n:
            return None
        else:
            return my_list[idx]
