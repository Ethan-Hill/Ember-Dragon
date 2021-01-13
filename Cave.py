import os
import inquirer
from termcolor import colored


def clear():

    # Clears the terminal at the start

    os.system('c')


def Start():

    hasFire = False
    dragonDead = False

    # Variable for the NPC name

    NPC = 'Ember dragon: '

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
            hasFire = True
            print(colored('You pull out the Ember Fire', 'yellow'))
        if answer['choice'] == '*Slash with sword*':
            if hasFire:
                hasFire = True
                print(colored('You kill the dragon and take the claw',
                              'yellow'))
                dragonDead = True
                print(colored('Collected item: Ember Claw', 'yellow'))
            else:
                print(colored('You have no effect on the dragon', 'yellow'))


if __name__ == '__main__':
    Start()
