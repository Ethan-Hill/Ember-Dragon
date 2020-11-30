import inquirer
import os
import SamTheSmith
import Village
import Cave
import End
from termcolor import colored

xLimit = 10
yLimit = 10
xPos = 1
yPos = 1

SamVisited = False
PeterVisited = False
CaveVisited = False
EndVisited = False

VillagePeopleX = 1
VillagePeopleY = 3

SamTheSmithX = 1
SamTheSmithY = 6

CaveX = 7
CaveY = 3

EndX = 1
EndY = 3

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
    elif "help" in command:
        help() 
    elif "hint" in command:
        hint() 
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

def help():
  print(colored('HELP', 'yellow'))
  print(colored('CONTROLS', 'green'))
  print(colored('Movement -', 'yellow'))
  print(colored('Walk north: "walk north"', 'yellow'))
  print(colored('Walk east: "walk east"', 'yellow'))
  print(colored('Walk south: "walk south"', 'yellow'))
  print(colored('Walk west: "walk west"', 'yellow'))
  print(colored('HINTS', 'green'))
  print(colored('Hint: "hint"', 'yellow'))
  userInput()

def hint():
  print(colored('HINT', 'yellow'))
  if PeterVisited == False:
    print(colored('Find Peter at 1, 3', 'yellow'))
  elif PeterVisited == True and SamTheSmith == False:
    print(colored('Find Sam at 1, 6', 'yellow'))
  elif PeterVisited == True and SamTheSmith == True and CaveVisited == False:
    print(colored('Find the cave at 7, 3', 'yellow'))
  elif PeterVisited == True and SamTheSmith == True and CaveVisited == True and EndVisited == False:
    print(colored('Find the end at 1, 3', 'yellow'))
  userInput()
# Walks in a direction


def walkNorth():
    global yPos
    global xPos
    global PeterVisited
    global SamVisited
    global CaveVisited
    global EndVisited

    if yPos < 10:
        print("You Walk North...")
        yPos += 1
        if xPos == VillagePeopleX and yPos == VillagePeopleY and SamVisited == False and CaveVisited == False and EndVisited == False:
          Village.Start()
          PeterVisited = True
        if xPos == SamTheSmithX and yPos == SamTheSmithY and PeterVisited == True and CaveVisited == False and SamVisited == False and EndVisited == False:
          SamTheSmith.Start()
          SamVisited = True
        if xPos == CaveX and yPos == CaveY and PeterVisited == True and CaveVisited == False and SamVisited == True and EndVisited == False:
          Cave.Start()
          CaveVisited = True
        if xPos == EndX and yPos == EndY and PeterVisited == True and CaveVisited == True and SamVisited == True and EndVisited == False:
          End.Start()
          EndVisited = True
        printCoords()
        userInput()
    else:
        print("You Feel You Have Strayed Too Far, And Turn Back.")
        userInput()


def walkEast():
    global xPos
    global xPos
    global PeterVisited
    global SamVisited
    global CaveVisited
    global EndVisited

    if xPos < 10:
        print("You Walk East...")
        xPos += 1
        if xPos == VillagePeopleX and yPos == VillagePeopleY and SamVisited == False and CaveVisited == False and EndVisited == False:
          Village.Start()
          PeterVisited = True
        if xPos == SamTheSmithX and yPos == SamTheSmithY and PeterVisited == True and CaveVisited == False and SamVisited == False and EndVisited == False:
          SamTheSmith.Start()
          SamVisited = True
        if xPos == CaveX and yPos == CaveY and PeterVisited == True and CaveVisited == False and SamVisited == True and EndVisited == False:
          Cave.Start()
          CaveVisited = True
        if xPos == EndX and yPos == EndY and PeterVisited == True and CaveVisited == True and SamVisited == True and EndVisited == False:
          End.Start()
          EndVisited = True
        printCoords()
        userInput()
    else:
        print("You Feel You Have Strayed Too Far, And Turn Back.")
        userInput()


def walkSouth():
    global yPos
    global xPos
    global PeterVisited
    global SamVisited
    global CaveVisited
    global EndVisited

    if yPos > 1:
        print("You Walk South...")
        yPos -= 1
        if xPos == VillagePeopleX and yPos == VillagePeopleY and SamVisited == False and CaveVisited == False and EndVisited == False:
          Village.Start()
          PeterVisited = True
        if xPos == SamTheSmithX and yPos == SamTheSmithY and PeterVisited == True and CaveVisited == False and SamVisited == False and EndVisited == False:
          SamTheSmith.Start()
          SamVisited = True
        if xPos == CaveX and yPos == CaveY and PeterVisited == True and CaveVisited == False and SamVisited == True and EndVisited == False:
          Cave.Start()
          CaveVisited = True
        if xPos == EndX and yPos == EndY and PeterVisited == True and CaveVisited == True and SamVisited == True and EndVisited == False:
          End.Start()
          EndVisited = True
        printCoords()
        userInput()
    else:
        print("You Feel You Have Strayed Too Far, And Turn Back.")
        userInput()


def walkWest():
    global xPos
    global xPos
    global PeterVisited
    global SamVisited
    global CaveVisited
    global EndVisited

    if xPos > 1:
        print("You Walk West...")
        xPos -= 1
        if xPos == VillagePeopleX and yPos == VillagePeopleY and SamVisited == False and CaveVisited == False and EndVisited == False:
          Village.Start()
          PeterVisited = True
        if xPos == SamTheSmithX and yPos == SamTheSmithY and PeterVisited == True and CaveVisited == False and SamVisited == False and EndVisited == False:
          SamTheSmith.Start()
          SamVisited = True
        if xPos == CaveX and yPos == CaveY and PeterVisited == True and CaveVisited == False and SamVisited == True and EndVisited == False:
          Cave.Start()
          CaveVisited = True
        if xPos == EndX and yPos == EndY and PeterVisited == True and CaveVisited == True and SamVisited == True and EndVisited == False:
          End.Start()
          EndVisited = True
        printCoords()
        userInput()
    else:
        print("You Feel You Have Strayed Too Far, And Turn Back.")
        userInput()


def printCoords():
    print("Current Position: X=" + str(xPos) + ", Y=" + str(yPos))

if __name__ == "__main__":
  userInput()
