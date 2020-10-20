import inquirer
import os
from termcolor import colored


def clear():
    # Clears the terminal at the start
    os.system("clear")


def start():

    # Variable for the NPC name
    NPC = "Garry The Goblin: "

    # Printing the opening line
    print(colored(NPC + 'WAKE UP! Finally you have arrived traveller to save our village, what is your name traveller?', 'green'))

    # Creating a question for the player name
    playerName = inquirer.Text('name', message="What's your name"),
    
    player = inquirer.prompt(playerName)

    player = player["name"]

    # Thanking the player with their name
    print(colored(NPC + 'Thank god you came ' + player +
                  ', we need your help with saving our village from this horrible curse. Will you do it?', 'green'))

    # Creating a question for the player choice to help
    will_you_help_us_question = [
        inquirer.List('choice',
                      message="Will you help us?",
                      choices=['Of course!', 'Nah, dont feel like it'],
                      ),
    ]

    # Asking the player if they will help
    answer = inquirer.prompt(will_you_help_us_question)

    clear()

    # Check to see if they agreed
    if answer["choice"] == "Of course!":
        print(colored(NPC + 'Thank you so much!', 'green'))

    # Check if they disagreed
    else:
        print(colored(NPC + 'But ' +
                      player["name"] + ' you must help us.', 'green'))

    clear()

    # Print their difficulty
    print(colored(NPC + 
                  'Thank you, go NORTH too the village to start. Good luck!', 'green'))
    return player

if __name__ == "__main__":
  start()
