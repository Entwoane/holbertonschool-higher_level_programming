#!/usr/bin/python3
def remove_char_at(str, n):
    strcp = ""
    for i in range(len(str)):
        if i != n:
            strcp += str[i]
    return strcp
