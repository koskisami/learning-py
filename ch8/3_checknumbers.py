# -*- coding: cp1252 -*-

import math

def getnumber(usernum):
    while True:
        try:
            number = float(input(usernum))
            return number
        except ValueError:
            print("This input is invalid.")

def calculator():
    
    print("Calculator")
    
    num1 = getnumber("Give a number: ")
    num2 = getnumber("Give a number: ")
    # Ask for 2 numbers to calculate
    while True:    
        # Print out and ask for a selection for what kind of calculation will be done
        print("\
        (1) + \n\
        (2) - \n\
        (3) * \n\
        (4) / \n\
        (5)sin(number1/number2) \n\
        (6)cos(number1/number2) \n\
        (7) Change Numbers \n\
        (8) Quit")

        # Print current numbers in menu
        print("Current numbers:", int(num1), int(num2))

        sel = int(input("Please select something (1-6):"))

        # Do calculations
        if sel == 1:
            result = num1 + num2
            print("The result is:", int(result))
        elif sel == 2:
            result = num1 - num2
            print("The result is:", int(result))
        elif sel == 3:
            result = num1 * num2
            print("The result is:", int(result))
        elif sel == 4:
            result = num1 / num2
            print("The result is:", int(result))
        elif sel == 5:
            result = math.sin(num1/num2)
            print("The result is:", result)
        elif sel == 6:
            result = math.cos(num1/num2)
            print("The result is:", result)
        elif sel == 7:
            num1 = int(input("Give the first number:"))
            num2 = int(input("Give the second number:"))
        elif sel == 8:
            print("Thank you!")
            break
        else:
            print("Selection was not correct.")

if __name__ == "__main__":
    calculator()