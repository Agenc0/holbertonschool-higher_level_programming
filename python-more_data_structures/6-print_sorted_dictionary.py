#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    d_sorted = sorted(a_dictionary.items())
    for key, value in d_sorted:
        print(f"{key}: {value}")
