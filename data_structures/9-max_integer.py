#!/usr/bin/python3
def max_integer(my_list=[]):
    n = len(my_list)
    if n == 0:
        return None
    max_int = my_list[0]  # Initialize max_int with the first element
    for i in range(1, n):
        if my_list[i] > max_int:
            max_int = my_list[i]  # Update max_int if a larger element is found
    return max_int
