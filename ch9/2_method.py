# -*- coding: cp1252 -*-

class player:
    """Class defines a player"""
    teamcolor = "Default"
    __points = 0

    def tellscore(self):
        print("I am " + self.teamcolor + ", we have " + str(self.__points) + " points!")

    def goal(self):
        self.__points += 1
 
def main():
    blueguy = player()
    blueguy.teamcolor = "Blue"

    blueguy.goal()
    blueguy.tellscore()

if __name__ == "__main__":
    main()