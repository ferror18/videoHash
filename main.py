#!/usr/bin/python
from time import time
start = time()
import os
import multiprocessing as mp
from pprint import pprint
from modules.collisionOrganizer import organizeCollisions
from modules.folderStructure import generateFolderStructure
from modules.nameGenerator import nameGenerator
from modules.video_hash import video_hash 
from modules.photo_hash import photo_hash 
from modules.clear_console import clearConsole
from modules.mapping import generate_map
from modules.readConfig import readConfig
from modules.mapHasher import mapHasher
import concurrent.futures
#State
clearConsole()
origin_path,destination_path,collision_path,database,mode,extraVidExt, extraPhotoExt = readConfig()
vidExts = ['mp4', 'mkv', 'mov', 'webm', 'avi'] 
vidExts = vidExts+extraVidExt.split(',') if extraVidExt != '0' else vidExts
photoExts = ['jpg', 'png', 'tiff', 'pdf', 'raw', 'webp']
photoExts = photoExts+extraPhotoExt.split(',') if extraPhotoExt != '0' else photoExts
yearTkr = {}
hashTrk = {}
Unresolved_Collisions = False

if __name__ == '__main__':
# Traverse the dir and create a map
    filenames = os.listdir(origin_path)
    filenames = list(filter(lambda j: not os.path.isdir(os.path.join(origin_path,j)), filenames)) #Removes all directories
    fileMap = generate_map(origin_path, vidExts, photoExts)
    totalFiles = 0
    # d1 = dict(list(fileMap.items())[len(fileMap)//2:])
    # d2 = dict(list(fileMap.items())[:len(fileMap)//2])
    fileList = [ _[1] for _ in fileMap.items()]
    videoList = [ (_['id'],_['path']) for _ in fileList]
    with concurrent.futures.ProcessPoolExecutor as executor:
        results = executor.map(video_hash, videoList)
        for _ in results: 
            print(_)
    #     hs = hashof(workObj['path'])

    #     # workObj['hash'] = hs
    #     # totalFiles+=1
    #     # progress = round(totalFiles/(len(fileMap))*100)
    #     # print(f"Progress:{progress}%\t{len(fileMap)-totalFiles} remaining\t{workObj['fileName']}")
        
        
        
        
        
        
    #     #Check hash traker for collision
    #     if hs in hashTrk:
    #         print('+++++ COLLISION ++++++++', hs)
    #         #Add it to collison tracker
    #         Unresolved_Collisions = True
    #         hashTrk[hs] = [workObj,*hashTrk[hs]]
    #         #Remove both from file map
    #     else:
    #         hashTrk[hs] = [fileMap[key]]


    print(f"Total files counted {len(hashTrk)} \n")
    for i in hashTrk:
        print(i)
        repeated = len(hashTrk[i])
        if repeated > 1:
            pprint(f"{i} = {repeated}")
    if Unresolved_Collisions:
        forDeleteion = organizeCollisions(hashTrk, collision_path)
        for i in forDeleteion:
            fileMap.pop(i)
    print(f'Non Collisions {len(fileMap)}')

    nameGenerator(fileMap, yearTkr)
    pprint(yearTkr)
    generateFolderStructure(destination_path,yearTkr,fileMap)

    end = time()
    print(f"{end-start} seconds")