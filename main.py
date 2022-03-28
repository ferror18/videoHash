#!/usr/bin/python
import os
from pprint import pprint
from modules.createDB import createDB
from modules.video_hash import video_hash 
from modules.photo_hash import photo_hash 
from modules.generate_config_file import generate_config_file 
from modules.clear_console import clearConsole
from modules.mapping import generate_map
from modules.readConfig import readConfig
from modules.databaseDriver import closeDB, getAll, insertOne

#State
clearConsole()
vidExts = ['mp4', 'mkv', 'mov', 'webm', 'avi']
photoExts = ['jpg', 'png', 'tiff', 'pdf', 'raw']
# config = {}
hashTrk = {}
yearTkr = {}
# run tests
origin_path,destination_path,collision_path,mode,database = readConfig()
Unresolved_Collisions = False if len(os.listdir(collision_path)) == 0 else True
# Map files
fileMap = generate_map(origin_path)
databaseFiles = {}
for row in getAll():
    databaseFiles[row['id']] = dict(row)


while True:

    print('''
    What would you like to do?

    a) Sort collection
    b) Review collisions
    c) Generate config file
    x) exit
    ''')
    inp = input("")
    clearConsole()
    
    if inp == "x":
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
        for  i in directorie: # Loop throug folders named by hash
            items = os.listdir(i) # List what is inside one hash folder
            if len(items) == 1: # Check wether there is only one file in hash folder
                for x in hashTrk[i]: # loop trough collision array in hashTrk
                    if x['fileName'] == items[0]: 
                        os.rename(x['unsolved_collision_path'], x['path'])
                        os.rmdir(i)
                    else:
                        del fileMap[x['id']]
                        
                #Update State
                hashTrk = {}
                solved += 1
                os.chdir(original_wd)

                
        if unresolved == solved:
            print('\n\n\t+++ All collisions resolved +++')
            Unresolved_Collisions = False
        else:
            print(f"Solved {solved} collisions, there are {unresolved} collisions unresolved left.")
            
    elif inp == "a":
        if Unresolved_Collisions:
            print('\n\n\t++ Please resolve collisions before continuing ++ ')
            print(f"\n\n\t++ There are {len(os.listdir(collision_path))} collisions unresolved ++ ")
            continue

        if mode == 'episodes_by_year':
            #Populate hashTrk with database
            
            for key in databaseFiles:
                workObj=databaseFiles[key]
                hashTrk[workObj['hash']] = [workObj]
                print(f"Database - File: {workObj['fileName']} Hash: {workObj['hash']}")

            # pprint(f"Data Base Files: {databaseFiles}")
            pprint('--------------------------------Start-------------------------------')
            #Start cheking new file hashes
            for key in fileMap:
                workObj = fileMap[key]
                #File Extension
                ext = workObj['ext']
                isVid = True if ext in vidExts else False

                #Hash
                hashof = video_hash if isVid else photo_hash
                hs = hashof(workObj['path'])
                workObj['hash'] = hs
                print(f"Origin - File: {workObj['fileName']} Hash: {workObj['hash']}")
                #Check hash traker for collision
                if hs in hashTrk:
                    print('+++++ COLLISION ++++++++')
                    #Add it to collison tracker
                    Unresolved_Collisions = True
                    hashTrk[hs] = [workObj,*hashTrk[hs]]
                    # pprint(f"Hash: {hs} Number of Files: {len(hashTrk[hs])} Keys: {[i['fileName'] for i in hashTrk[hs]]}")
                    #Remove both from file map
                else:
                    hashTrk[hs] = [fileMap[key]]
                    
                # print(f"File: {workObj['fileName']} Hash: {workObj['hash']}")
            pprint('-------------------------------- End -------------------------------')
            #Rename and Move Files
            if Unresolved_Collisions:
                print('\n\n\t++ Please resolve collisions before continuing ++ ')
                for key in hashTrk:
                    collisionArray = hashTrk[key]
                    if len(collisionArray) == 1: # Loop trough all hashes but avoid the ones with out collition
                        continue


                    #Create collision Folder
                    unsolved_collision_folder = os.path.join(collision_path, key)
                    os.mkdir(unsolved_collision_folder)

                    #Move collision files into collision folder
                    for x in collisionArray:
                        x['unsolved_collision_path'] = os.path.join(unsolved_collision_folder, x['fileName'])
                        os.rename(x['path'], x['unsolved_collision_path'])

                continue
            else:
                print('\n\n\t Creating Folder Structure')

                #Year and episode number
                for key in databaseFiles:
                    workObj = databaseFiles[key]
                    #Episode number
                    year = workObj['year']
                    if year not in yearTkr:
                        episode = 1
                        yearTkr[year] = 1
                    else:
                        yearTkr[year]+=1

                for key in fileMap:
                    workObj = fileMap[key]
                    #Episode number
                    year = workObj['year']
                    if year not in yearTkr:
                        episode = 1
                        yearTkr[year] = 1
                    else:
                        yearTkr[year]+=1
                    episode = yearTkr[year]
                    workObj['episode'] = episode
                    workObj['new_name'] = f"[S{year}E{episode}]{key}.{ext}"
                

                #Creating File Structure
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
                    workObj['finalPath'] = os.path.join(destination_path, workObj['year'], workObj['new_name'])
                    os.rename(workObj['path'], workObj['finalPath'])
                    #Update State
                    workObj['path'] = workObj['finalPath']
                    workObj['fileName'] = workObj['new_name']
                    del workObj['new_name']
                    # print(workObj)
                #Updating database
                    insertOne(workObj)

                
                # for row in getAll():
                #     pprint(dict(row))
                # print('\n\n\t Succes collection sorted ')
                break 

        elif mode == 'photos_oredered_by_month':
            pass
        else:
            print('Unknown mode')
        

    else:
        continue
#This is outside the while loop
closeDB()