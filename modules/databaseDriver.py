import sqlite3
import os
from modules.readConfig import readConfig
from pprint import pprint
_,_,_,_, database = readConfig()


con = sqlite3.connect(database)
con.row_factory = sqlite3.Row
cur = con.cursor()

def insertOne(workingObj):
    cur.execute(f'''
    INSERT INTO media (id,hash,path,creation_date,year,fileName,ext) values(?,?,?,?,?,?,?);''', (
        workingObj['id'], 
        workingObj['hash'], 
        workingObj['path'],
        workingObj['creation_date'],
        workingObj['year'],
        workingObj['fileName'],
        workingObj['ext'])
        )

def insertMany():
    pass

def getAll():
    cur.execute('select * from media')
    return cur.fetchall()


# x = {'creation_date': '2022-03-22-18:24:14',
#  'ext': 'mp4',
#  'fileName': '[S2022E4]527ecb61-3ac8-4835-b2e2-f8d0fd88ae8f.mp4',
#  'hash': '0xffffe000fff80000',
#  'id': '9960fb49-6ead-444a-b146-4a6209a2a308',
#  'new_name': '[S2022E4]9960fb49-6ead-444a-b146-4a6209a2a308.mp4',
#  'new_path': 'C:\\Users\\murad\\Desktop\\videoHash\\destination\\2022\\[S2022E4]9960fb49-6ead-444a-b146-4a6209a2a308.mp4',      
#  'path': 'C:\\Users\\murad\\Desktop\\videoHash\\data\\[S2022E4]527ecb61-3ac8-4835-b2e2-f8d0fd88ae8f.mp4',
#  'year': '2022'}

# insertOne(x)
# myrows = getAll()
# fileMap = {}
# for row in myrows:
#     fileMap[row['id']] = dict(row)
# pprint(fileMap)
# for key in fileMap:
#     print(key)