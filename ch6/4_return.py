# -*- coding: cp1252 -*-

def main():
    num = int(input("Give a number:"))
    pwrOfTwo(num)

def pwrOfTwo(num):
    pot = pow(2, num)
    print("The result is ", pot)


if __name__ == "__main__":
    main()