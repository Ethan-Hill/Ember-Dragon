import os
import inquirer
from termcolor import colored

hasFire = False



def clear():

    # Clears the terminal at the start

    os.system('clear')


def Start():
dragonDead = False
  # Variable for the NPC name

    NPC = 'Peter The Peasant: '

     # Creating a question for the player choice to help

    peter_questions = [inquirer.List('choice', message=NPC
                       + '*Breathes Fire*',
                       choices=['*Pull out ember fire*',
                       '*Slash with sword*'])]

    # Asking the peter questions

    while dragonDead != True:
        answer = inquirer.prompt(peter_questions)

    # Check what they asked

        if answer['choice'] == '*Pull out ember fire*':
            hasFire = true
            print(colored('You pull out the Ember Fire', 'yellow'))
        if answer['choice'] == '*Slash with sword*':
            if hasfire:
                hasFire = true
                print(colored('You kill the dragon and take the claw',
                              'yellow'))
                dragonDead = true
                print(colored('Collected item: Ember Claw', 'yellow'))
        else:
            print(colored('You have no effect on the dragon', 'yellow'))


if __name__ == '__main__':
    Start()
