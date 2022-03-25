#!/usr/bin/python
# The qmark style used with executemany():
# lang_list = [
#     ("Fortran", 1957),
#     ("Python", 1991),
#     ("Go", 2009),
# ]
# cur.executemany("insert into lang values (?, ?)", lang_list)
import os
from pprint import pprint
from modules.video_hash import video_hash 
from modules.photo_hash import photo_hash 
from modules.generate_config_file import generate_config_file 
from modules.clear_console import clearConsole
from modules.mapping import generate_map
from modules.creation_time import get_creation_time
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
            pprint('--------------------------------Start-------------------------------')
            # pprint(fileMap)
            
            # accepted file extensions
            vidExts = ['mp4', 'mkv', 'mov', 'webm', 'avi']
            photoExts = ['jpg', 'png', 'tiff', 'pdf', 'raw']

            # Tracking Dicts
            yearTkr = {}
            hashTkr = {}
            Unresolved_Collisions = False
            collList = []

            for key in fileMap:
                workObj = fileMap[key]
                #File Extension
                ext = workObj['ext']
                z = True if ext in vidExts else False
                hashof = video_hash if z else photo_hash

                #Creation Date and episode number
                workObj['creation_date'] = get_creation_time(workObj['path'])
                year = workObj['creation_date'][:4]
                if year not in yearTkr:
                    episodeNumber = 1
                    yearTkr[year] = 1
                else:
                    yearTkr[year]+=1
                    episodeNumber = yearTkr[year]

                workObj['new_name'] = f"[S{year}E{episodeNumber}]{key}.{ext}"

                #Hash
                hs = hashof(workObj['path'])

                if hs in hashTkr:
                    print('+++++ COLLISION ++++++++')
                    #Add it to collison tracker
                    Unresolved_Collisions = True
                    hashTkr[hs] = [workObj,*hashTkr[hs]]
                    collList.append(hs)
                    pprint(f"Hash: {hs} Number of Files: {len(hashTkr[hs])} Keys: {[i['id'] for i in hashTkr[hs]]}")
                    #Remove both from file map
                else:
                    workObj['hash'] = hs
                    hashTkr[hs] = [fileMap[key]]
                # print( f"Path: {workObj['path'][38::]} Hash: {hs} type: {'video' if z else 'photo'} Creation:{workObj['creation_date']}" )
                print(f"Path: {workObj['path'][38::]} Episode Name: {workObj['new_name']}")
                # pprint(workObj['creation_date'])
                # Review collisions
                # Move files
            # pprint(fileMap)
            pprint('-------------------------------- End -------------------------------')
            #Rename and Move Files
            if Unresolved_Collisions:
                print('\n\n\t++ Please resolve collisions before continuing ++ ')
                pprint(hashTkr)
                for i in collList:
                    print(i)
                continue
            else:
                print('Start Moving and renaming files')







                

        elif config['mode'] == 'photos_oredered_by_month':
            pass
        else:
            print('Unknown mode')
        

    else:
        continue