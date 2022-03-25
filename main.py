#!/usr/bin/python
import os, sys
from pprint import pprint
from modules.video_hash import video_hash 
from modules.photo_hash import photo_hash 
from modules.generate_config_file import generate_config_file 
from modules.clear_console import clearConsole
clearConsole()
while True:
    print('''
    What would you like to do?

    a) Sort collection
    b) Generate config file
    c) exit
    ''')
    inp = input("")
    clearConsole()
    if inp == "c":
        break
    elif inp == "b":
        generate_config_file()
    elif inp == "a":
        # runTests()
        pass

    else:
        continue