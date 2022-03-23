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
    open('vh.db','x')        
    con = sqlite3.connect('vh.db')
    cur = con.cursor()
    cur.execute('''CREATE TABLE Videos( hash PRIMARY KEY, name UNIQUE, path UNIQUE)''')
    con.commit()
    print('TABLE SCHEMA ==> Videos( hash PRIMARY KEY, name UNIQUE, path UNIQUE)')
    con.close()





else:
    print('Db already exists')
