import sqlite3
import os
from modules.readConfig import readConfig

def createDB():

    dirs = os.listdir()
    _,_,_,database,_,_,_ = readConfig()
    db_exists = False
    for file in dirs:
        if file == database:
            db_exists = True
        else:
            pass

    if not db_exists:
        print(f'New database was created with the name {database}')
        x = open(database,'x')
        x.close()

        con = sqlite3.connect(database)
        cur = con.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS media (
            id text PRIMARY KEY, 
            hash text UNIQUE, 
            path text UNIQUE,
            creation_date text,
            year text,
            month text,
            fileName text,
            ext text,
            finalPath text,
            episode integer,
            mode text
            ) WITHOUT ROWID;''')
        con.commit()
        # print('TABLE SCHEMA ==> videos( hash PRIMARY KEY, name UNIQUE, path UNIQUE)')
        con.close()
    else:
        print('Database detected')
        pass