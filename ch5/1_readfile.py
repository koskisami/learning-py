# -*- coding: cp1252 -*-

thefile = open("facts.txt","r")
filetext = thefile.read()
print("Following was read from the file:", filetext)
thefile.close()