import os
import inquirer
from termcolor import colored

def clear():
    # Clears the terminal at the start
    os.system("clear")

def Start():
  # Variable for the NPC name
    NPC = "Vilage People: "

    print(colored(NPC + 'The curse is gone, our village is free! Thank you so much traveler!', 'green'))

    print(colored('Well done, you have finished the game!', 'red'))
    exit()

if __name__ == "__main__":
  Start()