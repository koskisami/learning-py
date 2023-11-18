# -*- coding: cp1252 -*-

import time

currentlyopen = "notebook.txt"

try:
    notebook =open(currentlyopen)
except IOError:
	notebook = open(currentlyopen, "w")
	print("No default notebook was found, created one.")

notebook.close()

while True:
    print("Now using file " + currentlyopen)
    # Print out available options
    print("\
    (1) Read the notebook \n\
    (2) Add note \n\
    (3) Empty the notebook \n\
    (4) Change the notebook \n\
    (5) Quit \n")

    # Get input
    sel = int(input("Please select one:"))

    # Read notebook
    if sel == 1:
        notebook = open(currentlyopen, "r")
        line = notebook.readlines()
        for i in line:
            i = i[:-1]
            print(i)
        notebook.close()
    # Write note
    elif sel == 2:
        notetoadd = input("Write a new note:")
        notebook = open(currentlyopen, "a")
        timestamp = time.strftime("%X %x")
        notebook.write(notetoadd + ":::" + timestamp + "\n")
        notebook.close()
    # Clear notebook
    elif sel == 3:
        notebook = open(currentlyopen, "w")
        notebook.close()
        print("Notes deleted.")
    elif sel == 4:
        currentlyopen = input("Give the name of the new file: ")
        try:
            notebook = open(currentlyopen)
            notebook.close()
        except IOError:
            notebook = open(currentlyopen, "w")
            print("No notebook with that name detected, created one.")
            notebook.close()
    # Exit app
    elif sel == 5:
        print("Notebook shutting down, thank you.")
        break
    else:
        print("Incorrect selection.")