# -*- coding: cp1252 -*-

def main():
    while True:
        inputText = input("Write something (quit ends): ")
        if inputText == "quit":
            break
        if tester(inputText):
            print("X spotted!")

def tester(givenstring = "Too short"):
    if len(givenstring) < 10:
        print("Too short")
        return False
    elif 'X' in givenstring:
        print(givenstring)
        return True
    else:
        print(givenstring)
        return False
    
if __name__ == "__main__":
    main()