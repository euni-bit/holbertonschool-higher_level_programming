#!/usr/bin/python3
def uppercase(input_str):
    result_str = ""
    for char in input_str:
        if 97 <= ord(char) <= 122:
            char = chr(ord(char) - 32)
        result_str += char
    print("{}".format(result_str))
