import os
from uuid import uuid4
from modules.creation_time import get_creation_time

def generate_map(path, vidExts, photoExts):
    original_wd = os.getcwd()
    os.chdir(path)
    fileMap = {}
    fileExtensions = vidExts + photoExts
    dir = os.listdir(path)

    for item in dir:


        item = os.path.abspath(item)
        # print(item, os.path.isdir(item)) debug print
        if os.path.isdir(item):
            fileMap = fileMap | generate_map(item, vidExts, photoExts)
        # elif 
        else:
            # Track extension names
            extension = os.path.splitext(item)[1][1:]
            if extension not in fileExtensions:
                continue

            #Generate map
            id = str(uuid4())
            creation_string = get_creation_time(item)
            if id not in fileMap:
                fileMap[id] = {
                    'id':id,
                    'path':item, 
                    'ext':extension, 
                    'fileName':os.path.basename(item),
                    'creation_date' : creation_string,
                    'year': creation_string[0:4],
                    'month': creation_string[5:7]
                    }
    os.chdir(original_wd)
    return fileMap




