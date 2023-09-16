# -*- coding: cp1252 -*-

def testme(param):
    hasLetter = False
    hasNum = False

    if len(param) < 6:
        return False
    
    for i in param:
        if i.isalpha():
            hasLetter = True
        if i.isdigit():
            hasNum = True
    
    if hasLetter and hasNum == True:
        return True