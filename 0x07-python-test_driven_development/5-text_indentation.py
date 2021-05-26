#!/usr/bin/python3
"""
Function prints the text with two new lines
after each these characters: ., ? and :
"""
def text_indentation(text):
    if type(text) != str:
        raise TypeError("text must be a string")

    cases = [".", ":", "?"]
    lines = "\n\n"

    for i in cases:
        text = str(i + lines).join(a.strip() for a in text.split(i))

    print("{}".format(text))
