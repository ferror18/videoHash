#!/usr/bin/python
import os
from pprint import pprint
from modules.collisionOrganizer import organizeCollisions
from modules.folderStructure import generateFolderStructure
from modules.nameGenerator import nameGenerator
from modules.video_hash import video_hash 
from modules.photo_hash import photo_hash 
from generate_config_file import generate_config_file 
from modules.clear_console import clearConsole
from modules.mapping import generate_map
from modules.readConfig import readConfig
from modules.databaseDriver import closeDB, deleteAll, getAll, insertOne, openDB

#State
clearConsole()
vidExts = ['mp4', 'mkv', 'mov', 'webm', 'avi']
photoExts = ['jpg', 'png', 'tiff', 'pdf', 'raw', 'webp']
hashTrk = {}
yearTkr = {}
# run tests
origin_path,destination_path,collision_path,database,mode = readConfig()
Unresolved_Collisions = False if len(os.listdir(collision_path)) == 0 else True
# Map files
num = 2
databaseFiles = {}
dropDatabase = False
# print('getall() :')
# for row in getAll():
#     print(f"ID: {row['id']} - config mode: {mode} - file mode: {row['mode']}")
for row in getAll():
    if row['mode'] != mode and row != None:
        print(f"File: {row['fileName']} had mode {row['mode']} current mode is {mode}")
        dropDatabase = True
    databaseFiles[row['id']] = dict(row)
filenames = os.listdir(origin_path)
filenames = list(filter(lambda j: not os.path.isdir(os.path.join(origin_path,j)), filenames)) #Removes all directories

if dropDatabase:
    for key in databaseFiles:
        workingObj = databaseFiles[key]
        curPath = workingObj['path']
        newFileName = workingObj['fileName']
        if newFileName in filenames:
            print('reapeated name')
            curPath = os.path.join(origin_path, newFileName)
            newFileName = workingObj['fileName'].split('.')
            newFileName = newFileName[0] + f' ({num}).' + newFileName[1]
            num+=1
            newPath = os.path.join(origin_path, newFileName)
            os.rename(curPath, newPath)
            curPath = curPath = workingObj['path']
            newFileName = workingObj['fileName']
            newPath = os.path.join(origin_path, newFileName)
            os.rename(curPath, newPath)
        else:
            newPath = os.path.join(origin_path, newFileName)
            os.rename(curPath, newPath)

    deleteAll()
    databaseFiles = {}
    # print('getall() :')
    # for row in getAll():
    #     print(f"ID: {row['id']} - config mode: {mode} - file mode: {row['mode']}")
fileMap = generate_map(origin_path, vidExts, photoExts)
while True:

    print('''
    What would you like to do?

    a) Sort collection
    b) Review collisions
    c) Generate config file
    x) exit
    ''')
    inp = input()
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
        #Populate hashTrk with database
        pprint('-------------------------------- Database ------------------------------')
        for key in databaseFiles:
            workObj=databaseFiles[key]
            hashTrk[workObj['hash']] = [workObj]
            print(f"Database - File: {workObj['fileName']} Hash: {workObj['hash']}")
        pprint('--------------------------------End Database ------------------------------')
        pprint('------------------------------- Start Files -------------------------------')
        #Start cheking new file hashes
        for key in fileMap:
            workObj = fileMap[key]
            workObj['mode'] = mode
            #File Extension
            ext = workObj['ext']
            # if ext not in vidExts or ext not in photoExts:
                
            #     os.rename(workObj['path'], os.path.join(destination_path, 'unknownExtension', workObj['fileName']))
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

        pprint('-------------------------------- End Files -------------------------------')
            
        #Rename and Move Files
        if Unresolved_Collisions:
            organizeCollisions(hashTrk, collision_path)
            continue
        else:
            print('\n\n\t Loading database data')

            nameGenerator(fileMap, databaseFiles, yearTkr, mode)
            
            generateFolderStructure(destination_path,yearTkr,fileMap,insertOne, mode)

            if False:
                for i in getAll():
                    pprint(dict(i))
            
            break 
        
    else:
        continue
    
#This is outside the while loop
closeDB()