# -*- coding: cp1252 -*-

num = int(input("Give a number:"))
newnum = 0

for i in range(num):
    newnum = i + newnum
print("The sum was:", newnum)