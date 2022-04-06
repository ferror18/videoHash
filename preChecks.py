import os
from createDB import createDB
from generate_config_file import generate_config_file
from modules.clear_console import clearConsole

def preCheckPassed():
    clearConsole()
    while True:
        configExists = False
        modeisValid = True
        pathsExist = True
        databaseExist = False
        databaseSchemaCorrect = True

        #Check config file is in CWD
        dirs = os.listdir()
        if 'config.txt' in dirs:
            configExists = True
        else:
            clearConsole()
            print("""

                    You are missing 'config.txt', would you like to generate one?:

                    a) Yes
                    x) exit
            
            """)
            inp = input()
            if inp == 'a':
                generate_config_file()
                continue
            elif inp == 'x':
                exit()
            else:
                continue
        #Import config
        from modules.readConfig import readConfig
        origin_path,destination_path,collision_path,database,mode,_,_ = readConfig()
        #Check that mode is valid
        modeisValid = modeisValid and True if mode[0] in ['e','n'] else False
        modeisValid = modeisValid and True if mode[1] in ['k','r'] else False
        modeisValid = modeisValid and True if mode[2] in ['s','y','m'] else False
        if modeisValid == False:
            clearConsole()
            print(f'''
            
                    Your mode '{mode}' is invalid please remake config or manually change it to a valid mode ('config.txt'):

                    a) Remake config.txt
                    x) Exit
            ''')
            inp = input()
            if inp == 'a':
                generate_config_file()
                continue
            elif inp == 'x':
                exit()
            else:
                continue
        #Check that paths exist
        paths = [origin_path,destination_path,collision_path]
        paths = [os.path.abspath(i) for i in paths]
        for i in paths:
            j = os.path.exists(i)
            pathsExist = pathsExist and j
            if j == False:
                break
        if pathsExist == False:
            clearConsole()
            print(f'''
            
            
                    Seems like your destination folder does not exist would you like to create it?
                    {i}


                    a) Yes create the folder for me
                    b) No please remake my 'config.txt' file
                    x) exit
            ''')
            inp = input()
            if inp == 'a':
                os.mkdir(i)
                continue
            elif inp == 'b':
                generate_config_file()
                continue
            elif inp == 'x':
                exit()
            else:
                continue
            

        #Check database exists
        if database in dirs:
            databaseExist = True
        else:
            clearConsole()
            print(f"""


                    No database found with name '{database}' what would you like to do?:

                    a) Create a new one
                    b) Look again (If you dragged and droped it just now)
                    x) Exit
            """)
            inp = input()
            if inp == 'a':
                createDB()
            elif inp == 'x':
                exit()
            else:
                continue
        # Check database schema
        if databaseExist:
            dbSchema = [(0, 'id', 'TEXT', 1, None, 1),
                (1, 'hash', 'TEXT', 0, None, 0),
                (2, 'path', 'TEXT', 0, None, 0),
                (3, 'creation_date', 'TEXT', 0, None, 0),
                (4, 'year', 'TEXT', 0, None, 0),
                (5, 'month', 'TEXT', 0, None, 0),
                (6, 'fileName', 'TEXT', 0, None, 0),
                (7, 'ext', 'TEXT', 0, None, 0),
                (8, 'finalPath', 'TEXT', 0, None, 0),
                (9, 'episode', 'INTEGER', 0, None, 0),
                (10, 'mode', 'TEXT', 0, None, 0)]
            import sqlite3
            conn = sqlite3.connect(database)
            cur = conn.cursor()
            dbdata = list(cur.execute("PRAGMA table_info('media')").fetchall())
            if len(dbdata) != len(dbSchema):
                databaseSchemaCorrect = False
            for row in dbdata:
                databaseSchemaCorrect = databaseSchemaCorrect and dbSchema[row[0]] == row
            conn.close()
            if databaseSchemaCorrect == False:
                clearConsole()
                print(f"""


                        Database  '{database}' is not the db needed in this program what would you like to do?:

                        a) Reset database '{database}'
                        b) Remake my config.txt (Switch to a difrent database)
                        x) Exit
                """)
                inp = input()
                if inp == 'a':
                    os.remove(database)
                    createDB()
                    continue
                elif inp == 'b':
                    generate_config_file()
                    continue
                elif inp == 'x':
                    exit()
                else:
                    continue
        if configExists and modeisValid and pathsExist and databaseExist and databaseSchemaCorrect:
            return 'Pre-Checks succesfull'
