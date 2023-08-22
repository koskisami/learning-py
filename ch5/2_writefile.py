# -*- coding: cp1252 -*-

filename = input("Give a file name:")
content =  input("Write something:")

myfile = open(filename, "w")
myfile.write(content)
myfile.close()

print("Wrote", content, "to the file", filename)