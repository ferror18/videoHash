#!/usr/bin/python
import os, sys
from pprint import pprint
from modules.video_hash import video_hash 
from modules.photo_hash import photo_hash 
from modules.generate_config_file import generate_config_file 
from modules.clear_console import clearConsole
clearConsole()
config = {}
while True:
    print('''
    What would you like to do?

    a) Sort collection
    b) Review collisions
    c) Generate config file
    d) exit
    ''')
    inp = input("")
    clearConsole()
    if inp == "d":
        break
    elif inp == "c":
        generate_config_file()
    elif inp == "b":
        #Review collisions
        pass
    elif inp == "a":
        # run tests
        # Config logic
        conFile = open("config.txt", "r")
        conFile = conFile.readlines()
        conFile = [i for i in conFile if i != '\n' and i[0] != '#' ]
        conFile = [i.replace('\n','') for i in conFile]
        conFile = [i.split('=') for i in conFile]
        for i in conFile:
            config[i[0]]=i[1]
        # pprint(config)

        if config['mode'] == 'episodes_same_folder':
            pass
        elif config['mode'] == 'photos_oredered_by_month':
            pass
        else:
            print('Unknown mode')
        # Map files
        # Get hashes
        # Review collisions
        # Move files

    else:
        continue