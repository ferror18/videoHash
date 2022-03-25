#!/usr/bin/python
# The qmark style used with executemany():
# lang_list = [
#     ("Fortran", 1957),
#     ("Python", 1991),
#     ("Go", 2009),
# ]
# cur.executemany("insert into lang values (?, ?)", lang_list)
import os, sys
from pprint import pprint
from this import d
from modules.video_hash import video_hash 
from modules.photo_hash import photo_hash 
from modules.generate_config_file import generate_config_file 
from modules.clear_console import clearConsole
from modules.mapping import generate_map
from modules.creation_time import get_time_in_seconds_from_epoch
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

        if config['mode'] == 'episodes_by_year':
            
            # Map files
            fileMap = generate_map(config['origin_path'])
            pprint('--------------------------------hello world-------------------------------')
            pprint(fileMap)
            pprint('--------------------------------hello world-------------------------------')
            
            # Get hashes
            vidExt = ['mp4', 'mkv', 'mov', 'webm', 'avi']
            photoExt = ['jpg', 'png', 'tiff', 'pdf', 'raw']

            for key in fileMap:
                z = True if fileMap[key]['ext'] in vidExt else False
                hashof = video_hash if z else photo_hash
                hs = hashof(fileMap[key]['path'])
                print( f"Path: {fileMap[key]['path']} Hash: {hs} typed: {'video' if z else 'photo'}" )
                fileMap[key]['hash'] = hs
                fileMap[key]['creation_date'] = get_time_in_seconds_from_epoch(fileMap[key]['path'])
            pprint(fileMap)

        elif config['mode'] == 'photos_oredered_by_month':
            pass
        else:
            print('Unknown mode')
        # Review collisions
        # Move files

    else:
        continue