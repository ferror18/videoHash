from cgitb import lookup
import sqlite3
import os

# Open a file
path = "C:/Users/murad/Desktop/videoHash/videos"
dirs = os.listdir( path )
db_exists = False

for file in dirs:
    if file == 'vhdb.db':
        db_exists = True
    else:
        pass

if db_exists:
    print(db_exists)
    open('vhdb.db','x')
        
con = sqlite3.connect('vhdb.db')
cur = con.cursor()