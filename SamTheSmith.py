import os
import inquirer
from termcolor import colored

def clear():
    # Clears the terminal at the start
    os.system("c")

def Start():
  # Variable for the NPC name
    NPC = "Sam The Smith: "

     # Creating a question for the player choice to help
    sam_questions = [
        inquirer.List('choice',
                      message= NPC + "Who are you?",
                      choices=['Im a travler looking for information on this curse.'],
                      ),
    ]

    # Asking the peter questions
    answer = inquirer.prompt(sam_questions)

    # Check what they asked
    if answer["choice"] == "Im a travler looking for information on this curse.":
        print(colored(NPC + 'There is a dragon which is only weak to the ember fire which i hold in my hand, use this against it and you will defeat it. Cut the claw off and return it too the village and you will save us. The cave it sleeps in is south east', 'cyan'))
        print(colored('Collected item: Ember Fire', 'yellow'))

if __name__ == "__main__":
  Start()