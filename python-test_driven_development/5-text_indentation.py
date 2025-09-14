#!/usr/bin/python3
"""

This module prints a text with a 2 new lines after each of
these characters: `.`, `?`, `:`

Example:

    Lorem ipsum dolor sit amet, consectetur adipiscing elit.$
    $
    Quonam modo?$
    $
    Utrum igitur tibi litteram videor an totas paginas commovere?$
    $
    Non autem hoc:$
    $

    * text must be a string

    * There should be no space at the beginning or
    at the end of each printed line

"""
def text_indentation(text):
    if type(text) is not str:
        raise TypeError('text must be a string')
    text_length = len(text)
    i = 0
    new_string = ''
    starting = True
    while i < text_length:
        if text[i] == ' ' and starting is True:
            i += 1
            continue
        starting = False
        if text[i] in '.?:':
            new_string += text[i]
            new_string += '\n'
            new_string += '\n'
            i += 1
            while i < text_length and text[i] == ' ':
                i += 1
            continue
        if i < text_length:
            new_string += text[i]
            i += 1
    print(new_string, end='')
