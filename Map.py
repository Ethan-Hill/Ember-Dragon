import inquirer
import os
import Village
from termcolor import colored

xLimit = 10
yLimit = 10
xPos = 1
yPos = 1

VillagePeople = 3

def clear():
    # Clears the terminal at the start
    os.system("clear")

# user input function for taking commands from the user


def userInput():
    global yPos
    global xPos
    global yLimit
    global xLimit
    # takes input from the user and forwards it on through a parameter
    command = input("What would you like to do? ")
    if "walk" in command:
        getDirection(command)
    else:
        print("Unknown command, Please Try Again.")
        userInput()

# finds out which direction the user wants to travel


def getDirection(command):
    if "north" in command:
        walkNorth()
    elif "east" in command:
        walkEast()
    elif "south" in command:
        walkSouth()
    elif "west" in command:
        walkWest()
    else:
        print("Unknown Direction, Please Try Again. ")
        userInput()

# Walks in a direction


def walkNorth():
    global yPos

    if yPos < 10:
        print("You Walk North...")
        yPos += 1
        if yPos == VillagePeople:
          Village.Start()
        printCoords()
        userInput()
    else:
        print("You Feel You Have Strayed Too Far, And Turn Back.")
        userInput()


def walkEast():
    global xPos

    if xPos < 10:
        print("You Walk East...")
        xPos += 1
        printCoords()
        userInput()
    else:
        print("You Feel You Have Strayed Too Far, And Turn Back.")
        userInput()


def walkSouth():
    global yPos

    if yPos > 1:
        print("You Walk South...")
        yPos -= 1
        printCoords()
        userInput()
    else:
        print("You Feel You Have Strayed Too Far, And Turn Back.")
        userInput()


def walkWest():
    global xPos

    if xPos > 1:
        print("You Walk West...")
        xPos -= 1
        printCoords()
        userInput()
    else:
        print("You Feel You Have Strayed Too Far, And Turn Back.")
        userInput()


def printCoords():
    print("Current Position: X=" + str(xPos) + ", Y=" + str(yPos))

if __name__ == "__main__":
  userInput()
