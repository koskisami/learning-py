# -*- coding: cp1252 -*-

while True:
    try:
        thefile = input("Give the file name: ")
        thisfile = open(thefile,"r")
        filecontent = thisfile.read()

        fileinteger = float(filecontent)
        divided = 1000 / fileinteger

    except IOError:
        print("There seems to be no file with that name.")
        exit()
    except ValueError:
        print("The file contents were unsuitable.")
        exit()
    except Exception:
        print("There was a problem with the program")
        exit()
    else:
        print("The result was " + str(divided))
        exit()