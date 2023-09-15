# -*- coding: cp1252 -*-

def main():
    while True:
        inputText = input("Write something (quit ends): ")
        if inputText == "quit":
            break
        elif len(inputText) < 10:
            tester()
        else:
            tester(inputText)

def tester(givenstring = "Too short"):
    print(givenstring)
    
    
if __name__ == "__main__":
    main()