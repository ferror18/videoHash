#!/usr/bin/python
import os
from pprint import pprint
from modules import createDB
from modules.video_hash import video_hash 
from modules.photo_hash import photo_hash 
from modules.generate_config_file import generate_config_file 
from modules.clear_console import clearConsole
from modules.mapping import generate_map
from modules.creation_time import get_creation_time
from modules.readConfig import readConfig
from modules.databaseDriver import getAll
clearConsole()
config = {}
collList = []
hashTkr = {}
yearTkr = {}
# run tests
origin_path,destination_path,collision_path,mode,database = readConfig()
Unresolved_Collisions = False if len(os.listdir(collision_path)) == 0 else True
# Map files
fileMap = generate_map(origin_path)
databaseFiles = {}




# {'0x7bf801fffff000': [{'creation_date': '2022-03-22-18:24:14',
#                        'ext': 'mp4',
#                        'fileName': '[S2022E10]38fa0ae5-ccf1-41a0-8130-60a5edbcbce6.mp4',
#                        'hash': '0x7bf801fffff000',
#                        'id': '163245f2-841d-40e0-952b-7e2ab4a19974',
#                        'new_name': '[S2022E8]163245f2-841d-40e0-952b-7e2ab4a19974.mp4',
#                        'new_path': 'C:\\Users\\murad\\Desktop\\videoHash\\destination\\2022\\[S2022E8]163245f2-841d-40e0-952b-7e2ab4a19974.mp4',
#                        'path': 'C:\\Users\\murad\\Desktop\\videoHash\\data\\[S2022E10]38fa0ae5-ccf1-41a0-8130-60a5edbcbce6.mp4',                       'year': '2022'}],
#  '0x94b4616f7b1e4e18': [{'creation_date': '2022-03-24-19:33:15',
#                          'ext': 'jpg',
#                          'fileName': '[S2022E8]a1d4c338-65f5-4331-a565-4ea9240e6365.jpg',
#                          'hash': '0x94b4616f7b1e4e18',
#                          'id': '4f06804f-66bb-42ae-ae08-c6ce8b017169',
#                          'new_name': '[S2022E12]4f06804f-66bb-42ae-ae08-c6ce8b017169.jpg',
#                          'new_path': 'C:\\Users\\murad\\Desktop\\videoHash\\destination\\2022\\[S2022E12]4f06804f-66bb-42ae-ae08-c6ce8b017169.jpg',
#                          'path': 'C:\\Users\\murad\\Desktop\\videoHash\\data\\[S2022E8]a1d4c338-65f5-4331-a565-4ea9240e6365.jpg',
#                          'year': '2022'}],
#  '0xbfbfff9999808000': [{'creation_date': '2022-03-22-18:24:14',
#                          'ext': 'mp4',
#                          'fileName': '[S2022E13]6193f228-cc9b-46da-b668-b96da795bafc.mp4',
#                          'hash': '0xbfbfff9999808000',
#                          'id': '2ac73084-2f05-4999-8089-27f7b52de9a4',
#                          'new_name': '[S2022E11]2ac73084-2f05-4999-8089-27f7b52de9a4.mp4',
#                          'new_path': 'C:\\Users\\murad\\Desktop\\videoHash\\destination\\2022\\[S2022E11]2ac73084-2f05-4999-8089-27f7b52de9a4.mp4',
#                          'path': 'C:\\Users\\murad\\Desktop\\videoHash\\data\\[S2022E13]6193f228-cc9b-46da-b668-b96da795bafc.mp4',
#                          'year': '2022'}],
#  '0xff9b9db9ff800000': [{'creation_date': '2021-11-03-14:50:08',
#                          'ext': 'mp4',
#                          'fileName': '[S2021E2]2fcc1ac3-44c3-4b1b-9705-ffa8f806db4e.mp4',
#                          'hash': '0xff9b9db9ff800000',
#                          'id': '5bd968eb-ecd0-40d1-8c81-543e8ffec1ed',
#                          'new_name': '[S2021E2]5bd968eb-ecd0-40d1-8c81-543e8ffec1ed.mp4',
#                          'new_path': 'C:\\Users\\murad\\Desktop\\videoHash\\destination\\2021\\[S2021E2]5bd968eb-ecd0-40d1-8c81-543e8ffec1ed.mp4',
#                          'path': 'C:\\Users\\murad\\Desktop\\videoHash\\data\\[S2021E2]2fcc1ac3-44c3-4b1b-9705-ffa8f806db4e.mp4',
#                          'year': '2021'}],
#  '0xffbf99bfb9800000': [{'creation_date': '2022-03-22-18:24:14',
#                          'ext': 'mp4',
#                          'fileName': '[S2022E11]7ac3fe9f-fdef-493d-b792-ebbb700a1317.mp4',
#                          'hash': '0xffbf99bfb9800000',
#                          'id': '90d4ecec-184d-4ea0-85ed-cc7932faf707',
#                          'new_name': '[S2022E9]90d4ecec-184d-4ea0-85ed-cc7932faf707.mp4',
#                          'new_path': 'C:\\Users\\murad\\Desktop\\videoHash\\destination\\2022\\[S2022E9]90d4ecec-184d-4ea0-85ed-cc7932faf707.mp4',
#                          'path': 'C:\\Users\\murad\\Desktop\\videoHash\\data\\[S2022E11]7ac3fe9f-fdef-493d-b792-ebbb700a1317.mp4',
#                          'year': '2022'}],
#  '0xffffcceef8800000': [{'creation_date': '2022-03-22-18:24:14',
#                          'ext': 'mp4',
#                          'fileName': '[S2022E9]29127627-4de2-4be7-9451-8e7abfa22546.mp4',
#                          'hash': '0xffffcceef8800000',
#                          'id': 'b761709e-9b04-42b8-aad8-5f197e647c10',
#                          'new_name': '[S2022E13]b761709e-9b04-42b8-aad8-5f197e647c10.mp4',
#                          'new_path': 'C:\\Users\\murad\\Desktop\\videoHash\\destination\\2022\\[S2022E13]b761709e-9b04-42b8-aad8-5f197e647c10.mp4',
#                          'path': 'C:\\Users\\murad\\Desktop\\videoHash\\data\\[S2022E9]29127627-4de2-4be7-9451-8e7abfa22546.mp4',
#                          'year': '2022'}],
#  '0xffffe000fff80000': [{'creation_date': '2022-03-22-18:24:14',
#                          'ext': 'mp4',
#                          'fileName': '[S2022E12]9df7acb5-9394-420b-b452-4c2387cd39d1.mp4',
#ADD EXISTING FILES
for row in getAll():
    databaseFiles[row['id']] = dict(row)

# for key in databaseFiles:
#     workObj=databaseFiles[key]
#     hashTkr[workObj['hash']] = [workObj]
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
                    # print(x['fileName'], items[0])
                    if x['fileName'] == items[0]: # This check is likely unecesary unless you want save same hash items
                        os.rename(x['new_path'], x['path'])
                        #Update State
                        hashTkr[i] = [x]
                        collList = list(filter(lambda j: j != i, collList))
                        # print(collList)
                        os.rmdir(i)
                    else:
                        del fileMap[x['id']]
                solved += 1
                # pprint(hashTkr)
                hashTkr = {}
                os.chdir(original_wd)

                
        if unresolved == solved:
            print('\n\n\t+++ All collisions resolved +++')
            Unresolved_Collisions = False
            print(f"Coll list : {collList}")
        else:
            print(f"Solved {solved} collisions, there are {unresolved} collisions unresolved left.")
            
    elif inp == "a":
        if Unresolved_Collisions:
            print('\n\n\t++ Please resolve collisions before continuing ++ ')
            print(f"\n\n\t++ There are {len(os.listdir(collision_path))} collisions unresolved ++ ")
            continue

        if mode == 'episodes_by_year':
            pprint('--------------------------------Start-------------------------------')
            # pprint(fileMap)
            
            # accepted file extensions
            vidExts = ['mp4', 'mkv', 'mov', 'webm', 'avi']
            photoExts = ['jpg', 'png', 'tiff', 'pdf', 'raw']

            # Tracking Dicts
            for key in databaseFiles:
                workObj = database[key]
                hashTkr[workObj['hash']] = [workObj]
            pprint(hashTkr)
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
                    # pprint(workObj)
                    workObj = fileMap[key]
                    workObj['new_path'] = os.path.join(destination_path, workObj['year'], workObj['new_name'])
                    # print(workObj['path'], workObj['new_path'])
                    os.rename(workObj['path'], workObj['new_path'])
                #Updating database
                # for key in hashTkr:
                #     print(len(hashTkr[key]))
                pprint(hashTkr)






                

        elif mode == 'photos_oredered_by_month':
            pass
        else:
            print('Unknown mode')
        

    else:
        continue