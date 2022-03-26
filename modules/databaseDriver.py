import sqlite3
import os

con = sqlite3.connect('vh.db')
cur = con.cursor()
def insertOne(workingObj):
    pass

def insertMany():
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
    cur.execute('''CREATE TABLE media( 
        uuid PRIMARY KEY, 
        hash UNIQUE, 
        path UNIQUE,
        FOREIGN KEY (hash) REFERENCES hashes (hash)
        );''')
    con.commit()
    print('TABLE SCHEMA ==> videos( hash PRIMARY KEY, name UNIQUE, path UNIQUE)')
    con.close()