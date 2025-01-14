#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if 'a' <= char <= 'z':
            print(f"{chr(ord(char) - 32)}", end='')
        else:
            print(f"{char}", end='')
    print()
    