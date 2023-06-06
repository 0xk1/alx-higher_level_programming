#!/usr/bin/python3
def uppercase(str):
    for char in str:
        print(chr(ord(char) - 32) if char >= 'a' and char <= 'z' else char,
              end="")
    print("")
