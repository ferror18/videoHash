import sqlite3
import os
from modules.readConfig import readConfig
# from readConfig import readConfig
from pprint import pprint
_,_,_,database,_ = readConfig()

con = sqlite3.connect(database)
con.row_factory = sqlite3.Row
cur = con.cursor()
def openDB():
    con = sqlite3.connect(database)
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    return con, cur
def insertOne(workingObj):
    return cur.execute(f'''
    INSERT INTO media (id,hash,path,creation_date,year, month, fileName,ext,finalPath,episode,mode) values(?,?,?,?,?,?,?,?,?,?,?);''', (
        workingObj['id'], 
        workingObj['hash'], 
        workingObj['path'],
        workingObj['creation_date'],
        workingObj['year'],
        workingObj['month'],
        workingObj['fileName'],
        workingObj['ext'],
        workingObj['finalPath'],
        workingObj['episode'],
        workingObj['mode']
    ))

def getAll():
    cur.execute('select * from media')
    return cur.fetchall()

def deleteAll():
    cur.execute('DELETE FROM media')

def closeDB():
    con.commit()
    con.close()

def update(workingObj):
    cur.execute(f'''
    UPDATE media 
    SET hash = ?,
        path = ?,
        creation_date = ?,
        year = ?,
        month = ?,
        fileName = ?,
        ext = ?,
        finalPath = ?,
        episode = ?,
        mode = ? 
    WHERE id = ?''', (
        workingObj['hash'], 
        workingObj['path'],
        workingObj['creation_date'],
        workingObj['year'],
        workingObj['month'],
        workingObj['fileName'],
        workingObj['ext'],
        workingObj['finalPath'],
        workingObj['episode'],
        workingObj['mode'],
        workingObj['id'] 
    ))

# x = {
#  'id': '17f44a14-3511-49bd-971b-a481e43c6d11',
#  'hash': '0xefefeeeea234234e800000',
#  'path': 'C:\\Users\\murad\\Desktop\\videoHash\\destination\\2021\\[S2021E1]17f44a14-3511-49bd-971b-a481e43c6d11.mp4',
#  'creation_date': '2021-03-11-14:49:14',
#  'year': '2021',
#  'month': '01',
#  'fileName': '[S2021E1]17f44a14-3511-49bd-971b-a481e43c6d11.mp4',
#  'ext': 'mp4',
#  'episode': 1,
#  'mode': 'ery',
#  'finalPath': 'C:\\Users\\murad\\Desktop\\videoHash\\destination\\2021\\[S2021E1]17f44a14-3511-49bd-971b-a481e43c6d11.mp4',      
#  }


# x = {
#  'id': '17f44a14-3511-49bd-971b-a481e43c6d11',
#  'hash': '0xasdfasdf800000',
#  'path': 'asdfasdfasdfasdf',
#  'creation_date': 'asdfasdfsdf',
#  'year': 'asdf',
#  'month': 'asdf',
#  'fileName': 'asdfasdfasdf',
#  'ext': 'asdfasdf',
#  'episode': 2,
#  'mode': 'asdfasdf',
#  'finalPath': 'asdfasdfasdf'
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

# print(insertOne(x))
# insertOne(y)

# update(x)

# myrows = getAll()
# closeDB()
# fileMap = {}
# for row in myrows:
#     fileMap[row['id']] = dict(row)
# pprint(fileMap)
# for key in fileMap:
#     print(key)