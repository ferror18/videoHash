import sqlite3
import os
from modules.readConfig import readConfig
# from readConfig import readConfig
from pprint import pprint
_,_,_,_, database = readConfig()


con = sqlite3.connect(database)
con.row_factory = sqlite3.Row
cur = con.cursor()

def insertOne(workingObj):
    cur.execute(f'''
    INSERT INTO media (id,hash,path,creation_date,year,fileName,ext,finalPath,episode) values(?,?,?,?,?,?,?,?,?);''', (
        workingObj['id'], 
        workingObj['hash'], 
        workingObj['path'],
        workingObj['creation_date'],
        workingObj['year'],
        workingObj['fileName'],
        workingObj['ext'],
        workingObj['finalPath'],
        workingObj['episode']
    ))


def insertMany():
    pass

def getAll():
    cur.execute('select * from media')
    return cur.fetchall()

def closeDB():
    con.commit()
    con.close()


# x = {
#  'id': '17f44a14-3511-49bd-971b-a481e43c6d11',
#  'hash': '0xefefeeeeae800000',
#  'path': 'C:\\Users\\murad\\Desktop\\videoHash\\destination\\2021\\[S2021E1]17f44a14-3511-49bd-971b-a481e43c6d11.mp4',
#  'creation_date': '2021-03-11-14:49:14',
#  'year': '2021',
#  'fileName': '[S2021E1]17f44a14-3511-49bd-971b-a481e43c6d11.mp4',
#  'ext': 'mp4',
#  'episode': 1,
#  'finalPath': 'C:\\Users\\murad\\Desktop\\videoHash\\destination\\2021\\[S2021E1]17f44a14-3511-49bd-971b-a481e43c6d11.mp4',      
#  }

# y = {
#  'id': 'ebfec8c6-930a-4651-8369-bee47277f509',
#  'hash': '0xe1d1d1c3f7e1c580',
#  'path': 'C:\\Users\\murad\\Desktop\\videoHash\\destination\\2021\\[S2021E2]ebfec8c6-930a-4651-8369-bee47277f509.mp4',
#  'creation_date': '2022-03-22-18:24:14',
#  'year': '2022',
#  'fileName': '[S2021E2]ebfec8c6-930a-4651-8369-bee47277f509.mp4',
#  'ext': 'mp4',
#  'episode': 2,
#  'finalPath': 'C:\\Users\\murad\\Desktop\\videoHash\\destination\\2021\\[S2021E2]ebfec8c6-930a-4651-8369-bee47277f509.mp4',      
#  }

# insertOne(x)
# insertOne(y)

# myrows = getAll()
# fileMap = {}
# for row in myrows:
#     fileMap[row['id']] = dict(row)
# pprint(fileMap)
# for key in fileMap:
#     print(key)