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
from signal import raise_signal
from modules.video_hash import video_hash 
from modules.photo_hash import photo_hash 
from modules.generate_config_file import generate_config_file 
from modules.clear_console import clearConsole
from modules.mapping import generate_map
from modules.creation_time import get_creation_time
clearConsole()
config = {}
collList = []
hashTkr = {}
yearTkr = {}
Unresolved_Collisions = False
# run tests
# Config logic
conFile = open("config.txt", "r") #Open config File
conFile = conFile.readlines() # Split into an array of lines
conFile = [i for i in conFile if i != '\n' and i[0] != '#' ] # remove new line above and comments
conFile = [i.replace('\n','') for i in conFile] # remove new lines 
conFile = [i.split('=') for i in conFile] # Split pair into 
for i in conFile:
    # print(i)
    globals()[i[0]] = i[1]
# print(f'''
# collison_path: {collision_path}
# destination_path : {destination_path}
# origin_path: {origin_path}
# mode: {mode}
# ''')
# Map files
fileMap = generate_map(origin_path)
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
        original_wd = os.getcwd()
        os.chdir(collision_path)
        directorie = os.listdir()
        unresolved = len(directorie)
        solved = 0
        for  i in directorie:
            items = os.listdir(i)
            if len(items) == 1:
                for x in hashTkr[i]:
                    print(x['fileName'], items[0])
                    if x['fileName'] == items[0]:
                        os.rename(x['new_path'], x['path'])
                        #Update State
                        hashTkr[i] = [x]
                        collList = list(filter(lambda j: j != i, collList))
                        print(collList)
                        os.rmdir(i)
                    else:
                        del fileMap[x['id']]
                solved += 1
                hashTkr = {}
                os.chdir(original_wd)

                
        if unresolved == solved:
            print('All collisions resolved')
            Unresolved_Collisions = False
        else:
            print(f"Solved {solved} collisions, there are {unresolved} collisions unresolved left.")
            



    elif inp == "a":
        

        if mode == 'episodes_by_year':
            pprint('--------------------------------Start-------------------------------')
            # pprint(fileMap)
            
            # accepted file extensions
            vidExts = ['mp4', 'mkv', 'mov', 'webm', 'avi']
            photoExts = ['jpg', 'png', 'tiff', 'pdf', 'raw']

            # Tracking Dicts

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
                workObj['year'] = year
                #Hash
                hs = hashof(workObj['path'])

                if hs in hashTkr:
                    print('+++++ COLLISION ++++++++')
                    #Add it to collison tracker
                    Unresolved_Collisions = True
                    hashTkr[hs] = [workObj,*hashTkr[hs]]
                    collList.append(hs) if hs not in collList else None
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
                for i in collList:
                    new_path = os.path.join(collision_path, i)
                    os.mkdir(new_path)
                    for x in hashTkr[i]:
                        x['new_path'] = os.path.join(new_path, x['fileName'])
                        os.rename(x['path'], x['new_path'])
                continue
            else:
                print('\n\n\t Creating Folder Structure')
                #Creating File Structure
                print(yearTkr)
                existingDirs = {}
                dirs = os.listdir(destination_path) #List all files in destination path
                dirs = list(filter(lambda j: os.path.isdir(os.path.join(destination_path,j)), dirs)) #Removes all non directories
                #Add existing directories
                # print(f'dirs: {dirs}')
                for x in dirs:
                    existingDirs[x] = 1
                # Create remaining directories
                for i in yearTkr:
                    if i not in existingDirs:
                        os.mkdir(os.path.join(destination_path,i))
                #Moving files around
                for key in fileMap:
                    workObj = fileMap[key]
                    workObj['new_path'] = os.path.join(destination_path, workObj['year'], workObj['new_name'])
                    # print(workObj['path'], workObj['new_path'])
                    os.rename(workObj['path'], workObj['new_path'])
                #Updating database







                

        elif mode == 'photos_oredered_by_month':
            pass
        else:
            print('Unknown mode')
        

    else:
        continue