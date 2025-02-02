import os
import inquirer
from termcolor import colored

def clear():
    # Clears the terminal at the start
    os.system("c")

def Start():
  # Variable for the NPC name
    NPC = "Peter The Peasant: "

     # Creating a question for the player choice to help
    peter_questions = [
        inquirer.List('choice',
                      message= NPC + "Hey there traveler, what brings you here?",
                      choices=['What is this curse?'],
                      ),
    ]

    # Asking the peter questions
    answer = inquirer.prompt(peter_questions)

    # Check what they asked
    if answer["choice"] == "What is this curse?":
        print(colored(NPC + 'The curse is raverging our village, to know more go see Sam The Smith who lives North of the village', 'green'))

if __name__ == "__main__":
  Start()