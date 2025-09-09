#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
     sorted_dictionary = sorted(a_dictionary)
     for k, v in sorted_dictionary:
          print("{0}: {1}".format(k, v))
