# -*- coding: cp1252 -*-
import random

# Score
won = 0
ties = 0
rounds = 0

# Foot = 1
# Nuke = 2
# Cockroach = 3

while True:
    playerSel = input("Foot, Nuke or Cockroach? (Quit ends):")

    # Player selection translator text to number
    if playerSel == "Foot":
        playerSelNum = 1
    elif playerSel == "Nuke":
        playerSelNum = 2
    elif playerSel == "Cockroach":
        playerSelNum = 3
    elif playerSel == "Quit":
        print("You played ", rounds, " rounds, and won ", won," rounds, playing tie in ", ties, " rounds.")
        break
    else:
        print("Incorrect Selection.")
        continue
    
    # Computer selection and round increment
    computerSel = random.randint(1,3)
    rounds += 1
    
    # Computer selection translator number to text
    if computerSel == 1:
        computerSelStr = "Foot"
    elif computerSel == 2:
        computerSelStr = "Nuke"
    else:
        computerSelStr = "Cockroach"

    # Print choices
    print("You chose: " + playerSel)
    print("Computer chose: " + computerSelStr)

    # Ties and Nuke VS Nuke
    if playerSelNum == computerSel:
        if playerSelNum == 2:
            print("Both LOSE!")
        else:
            print("It is a tie!")
            ties += 1
    # Foot VS Cockroach
    elif playerSelNum == 1 and computerSel == 3:
        print("You WIN!")
        won += 1
    # Cockroach VS Nuke
    elif playerSelNum == 3 and computerSel == 2:
        print("You WIN!")
        won += 1
    # Nuke VS Foot
    elif playerSelNum == 2 and computerSel == 1:
        print("You WIN!")
        won += 1
    # Player Loses.
    else:
        print("You LOSE!")