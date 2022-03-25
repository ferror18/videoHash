from cgitb import lookup
import sqlite3
import os

# Open a file
path = "C:/Users/murad/Desktop/videoHash"
dirs = os.listdir( path )
db_exists = False

for file in dirs:
    # print(file)
    if file == 'vh.db':
        db_exists = True
    else:
        pass

if not db_exists:
    print('New database was created with the name vh.db')
    x = open('vh.db','x')
    x.close()

    con = sqlite3.connect('vh.db')
    cur = con.cursor()
    cur.execute('PRAGMA foreign_keys = ON;')
    cur.execute('''CREATE TABLE hashes(
        hash PRIMARY KEY
    );''')
    cur.execute('''CREATE TABLE videos( 
        uuid PRIMARY KEY, 
        hash UNIQUE, 
        path UNIQUE,
        FOREIGN KEY (hash) REFERENCES hashes (hash)
        );''')
    con.commit()
    print('TABLE SCHEMA ==> videos( hash PRIMARY KEY, name UNIQUE, path UNIQUE)')
    con.close()





else:
    print('Db already exists')
