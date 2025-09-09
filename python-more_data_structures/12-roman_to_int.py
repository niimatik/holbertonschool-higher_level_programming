#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return (0)
    roman_letter = [
        ['I', 1], ['V', 5], ['X', 10], ['L', 50],
        ['C', 100], ['D', 500], ['M', 1000]
    ]
    last = 0
    num = 0
    for letter in reversed(roman_string):
        value = roman_letter.get(letter, 0)
        if value < last:
            num -= value
        else:
            num += value
        last = value
    return (num)
