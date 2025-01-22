#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_d = a_dictionary.keys()
    sorted_d = sorted(sorted_d)
    for key in sorted_d:
        print(key, ':', a_dictionary[key])
