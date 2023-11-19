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
from generate_config_file import generate_config_file 
from modules.clear_console import clearConsole
from modules.mapping import generate_map
from modules.readConfig import readConfig
from modules.databaseDriver import closeDB, deleteAll, getAll, insertOne
from modules.mapHasher import mapHasher
#State
clearConsole()
origin_path,destination_path,collision_path,database,mode,extraVidExt, extraPhotoExt = readConfig()
vidExts = ['mp4', 'mkv', 'mov', 'webm', 'avi'] 
vidExts = vidExts+extraVidExt.split(',') if extraVidExt != '0' else vidExts
photoExts = ['jpg', 'png', 'tiff', 'pdf', 'raw', 'webp']
photoExts = photoExts+extraPhotoExt.split(',') if extraPhotoExt != '0' else photoExts
hashTrk = {}
yearTkr = {}
Unresolved_Collisions = False


# Traverse the dir and create a map

filenames = os.listdir(origin_path)
filenames = list(filter(lambda j: not os.path.isdir(os.path.join(origin_path,j)), filenames)) #Removes all directories
fileMap = generate_map(origin_path, vidExts, photoExts)



Unresolved_Collisions = mapHasher(fileMap, vidExts, video_hash, photo_hash,hashTrk)
print(Unresolved_Collisions)


print(f"Total files counted {len(fileMap)} \n")
for i in hashTrk:
    repeated = len(hashTrk[i])
    if repeated > 1:
        pprint(f"{i} = {repeated}")
if Unresolved_Collisions:
    forDeleteion = organizeCollisions(hashTrk, collision_path)
    for i in forDeleteion:
        fileMap.pop(i)
print(f'Unique files {len(fileMap)}')

nameGenerator(fileMap, yearTkr)
pprint(yearTkr)
generateFolderStructure(destination_path,yearTkr,fileMap)

end = time()
print(f"{end-start} seconds")