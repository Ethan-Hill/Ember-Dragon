import os
import inquirer
from termcolor import colored

def clear():
    # Clears the terminal at the start
    os.system("clear")

def Start():
  # Variable for the NPC name
    NPC = "Peter The Peasant: "

     # Creating a question for the player choice to help
    peter_questions = [
        inquirer.List('choice',
                      message= NPC + "Hey there traveler, what brings you here?",
                      choices=['What is this curse?', 'Who are you?'],
                      ),
    ]

    # Asking the peter questions
    answer = inquirer.prompt(peter_questions)

    # Check what they asked
    if answer["choice"] == "What is this curse?":
        print(colored(NPC + 'The curse is raverging our village, to know more go see Sam The Smith who lives East of the village', 'green'))
    else:
      print(colored(NPC + 'Im Peter, the village Peasant.', 'green'))

if __name__ == "__main__":
  Start()