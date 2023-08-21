# -*- coding: cp1252 -*-

print("Calculator")

# Ask for 2 numbers to calculate
    
num1 = int(input("Give the first number:"))
num2 = int(input("Give the second number:"))

while True:
    # Print out and ask for a selection for what kind of calculation will be done
    print("\
    (1) + \n\
    (2) - \n\
    (3) * \n\
    (4) / \n\
    (5) Change Numbers \n\
    (6) Quit \n")

    # Print current numbers in menu
    print("Current numbers:", num1, num2)

    sel = int(input("Please select something (1-6):"))

    # Do calculations
    if sel == 1:
        result = num1 + num2
        print("The result is:", result)
    elif sel == 2:
        result = num1 - num2
        print("The result is:", result)
    elif sel == 3:
        result = num1 * num2
        print("The result is:", result)
    elif sel == 4:
        result = num1 / num2
        print("The result is:", result)
    elif sel == 5:
        num1 = int(input("Give the first number:"))
        num2 = int(input("Give the second number:"))
        continue
    elif sel == 6:
        print("Thank you!")
        break
    else:
        print("Selection was not correct.")