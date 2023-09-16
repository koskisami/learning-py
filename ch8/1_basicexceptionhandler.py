# -*- coding: cp1252 -*-

try:
    num = input("Give a number: ")
    converted = int(num)
except Exception:
    print("The input was malformed.")
else:
    print("The input was suitable!")