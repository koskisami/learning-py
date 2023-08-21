# -*- coding: cp1252 -*-

# Print calculator header and ask for 2 numbers to calculate
print("Calculator")
num1 = int(input("Give the first number:"))
num2 = int(input("Give the second number:"))

# Print out and ask for a selection for what kind of calculation will be done
print("(1) + \n\
(2) - \n\
(3) * \n\
(4) / \n")

sel = int(input("Please select something (1-4):"))

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
else:
    print("Selection was not correct.")