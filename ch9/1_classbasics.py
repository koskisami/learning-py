# -*- coding: cp1252 -*-

class player:
    """Class defines a player"""
    teamcolor = "Default"
    points = 0

 
def main():
    blueguy = player()
    blueguy.teamcolor = "Blue"
    blueguy.points = 300

    print("The " + blueguy.teamcolor + " contender has " + str(blueguy.points) + " points!")

if __name__ == "__main__":
    main()