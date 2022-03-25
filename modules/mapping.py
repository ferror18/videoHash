import os
from pickletools import read_uint1
from pprint import pprint
from uuid import uuid4

def generate_map(path):
    original_wd = os.getcwd()
    os.chdir(path)
    fileMap = {}
    fileExts = {}
    dir = os.listdir(path)
    ignore = {
        'Thumbs.db':1
    }

    for item in dir:
        if item in ignore:
            print(f'item ignored: {item}')
            continue

        item = os.path.abspath(item)
        # print(item, os.path.isdir(item)) debug print
        if os.path.isdir(item):
            fileMap = fileMap | generate_map(item)
        else:
            # Track extension names
            extension = item.split('.')[-1]
            if extension not in fileExts:
                fileExts[extension] = 1
            else:
                fileExts[extension]+=1

            #Generate map
            id = str(uuid4())
            if id not in fileMap:
                fileMap[id] = {'id':id,'path':item, 'ext':extension}
    os.chdir(original_wd)
    return fileMap




