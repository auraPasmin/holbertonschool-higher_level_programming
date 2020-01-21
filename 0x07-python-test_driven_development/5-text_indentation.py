#!/usr/bin/python3
"""Write a function that prints a text with 2 new lines
after each of these characters: ., ? and:"""


def text_indentation(text):
    """new lines after each of these characters: ., ? and :
    Args:
        text (str):
    Raises:
        TypeError: text must be a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    lenght = 0
    while lenght < len(text) and text[lenght] == ' ':
        lenght += 1

    while lenght < len(text):
        print(text[lenght], end="")
        if text[lenght] == "\n" or text[lenght] in ".?:":
            if text[lenght] in ".?:":
                print('\n')
            lenght += 1
            while lenght < len(text) and text[lenght] == ' ':
                lenght += 1
            continue
        lenght += 1
