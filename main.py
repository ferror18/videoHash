#!/usr/bin/python
from time import time
start = time()
import os
from pprint import pprint
from modules.collisionOrganizer import organizeCollisions
from modules.folderStructure import generateFolderStructure
from modules.nameGenerator import nameGenerator
from modules.video_hash import video_hash 
from modules.photo_hash import photo_hash 
from modules.clear_console import clearConsole
from modules.mapping import generate_map
from modules.readConfig import readConfig
from modules.phoVidSeparator import phoVidSeparator
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
    originalLen = len(fileMap)
    totalFiles = 0

    videoListKey,videoListPath,photoListKey,photoListPath = phoVidSeparator(fileMap)

    
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = executor.map(video_hash, videoListKey, videoListPath, chunksize=len(fileMap)//40 if len(fileMap)//40>1 else 1 )
        for _ in results:
            workObj = fileMap[_[0]]
            hs = _[1]
            
            #Check hash traker for collision
            if hs in hashTrk:
                print('+++++ COLLISION ++++++++', hs)
                #Add it to collison tracker
                Unresolved_Collisions = True
                hashTrk[hs] = [workObj,*hashTrk[hs]]
                #Remove both from file map
            else:
                hashTrk[hs] = [fileMap[_[0]]]
        results2 = executor.map(photo_hash, photoListKey, photoListPath, chunksize=len(fileMap)//40 if len(fileMap)//40>1 else 1 )
        for _ in results2:
            workObj = fileMap[_[0]]
            hs = _[1]
            #Check hash traker for collision
            if hs in hashTrk:
                print('+++++ COLLISION ++++++++', hs)
                #Add it to collison tracker
                Unresolved_Collisions = True
                hashTrk[hs] = [workObj,*hashTrk[hs]]
                #Remove both from file map
            else:
                hashTrk[hs] = [fileMap[_[0]]]


    print(f"Total files counted {originalLen} \n")
    #Move collisions to collions folder and delete collisions from fileMap
    if Unresolved_Collisions:
        forDeleteion = organizeCollisions(hashTrk, collision_path)
        for i in forDeleteion:
            fileMap.pop(i)
    print(f'Non Collisions {len(fileMap)}')
    print(f"Collisions: {originalLen-len(fileMap)}")
    nameGenerator(fileMap, yearTkr) # Create the new fileNames
    pprint(yearTkr)
    generateFolderStructure(destination_path,yearTkr,fileMap) #Create organizing folders and move items

    end = time()
    print(f"{end-start} seconds")