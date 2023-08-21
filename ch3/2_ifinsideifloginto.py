# -*- coding: cp1252 -*-

user = "John"
passwd = "ABC123"

tryuser = input("Give name:")

if tryuser == user:
    trypass = input("Give Password:")
    if trypass == passwd:
        print("Both inputs are correct!")
    else:
        print("The password is incorrect.")
else:
    print("The given name is wrong.")