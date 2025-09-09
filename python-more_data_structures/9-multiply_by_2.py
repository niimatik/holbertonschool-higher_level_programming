#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dictionary = a_dictionary
    for values in new_dictionary.value():
        value = values * 2
    return (new_dictionary)
