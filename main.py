import os
os.system("pip install termcolor")
os.system("pip install inquirer")
os.system("clear")

import Intro
import Map

# Start the intro
Intro.start()

# Start the navigation
Map.userInput()