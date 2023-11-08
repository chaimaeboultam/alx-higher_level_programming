#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_integers = set(my_list)  # Convert list to a set to get unique elements
    result = sum(unique_integers)  # Sum all unique elements
    return result
