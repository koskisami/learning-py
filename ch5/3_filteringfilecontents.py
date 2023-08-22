# -*- coding: cp1252 -*-

thefile = open("strings.txt","r")
content = thefile.readlines()

for i in content:
    i = i[:-1]
    if i.isalnum() == True:
        print(i, "was ok.")
    else:
        print(i, "was invalid.")

thefile.close()