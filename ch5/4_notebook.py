# -*- coding: cp1252 -*-

while True:
    # Print out available options
    print("\
    (1) Read the notebook \n\
    (2) Add note \n\
    (3) Empty the notebook \n\
    (4) Quit \n")

    # Get input
    sel = int(input("Please select one:"))

    # Read notebook
    if sel == 1:
        notebook = open("notebook.txt", "r")
        line = notebook.readlines()
        for i in line:
            i = i[:-1]
            print(i)
        notebook.close()
    # Write note
    elif sel == 2:
        notetoadd = input("Write a new note:")
        notebook = open("notebook.txt", "a")
        notebook.write(notetoadd + "\n")
        notebook.close()
    # Clear notebook
    elif sel == 3:
        notebook = open("notebook.txt", "w")
        notebook.close()
        print("Notes deleted.")
    # Exit app
    elif sel == 4:
        print("Notebook shutting down, thank you.")
        break
    else:
        print("Incorrect selection.")