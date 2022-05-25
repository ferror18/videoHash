import os,shutil
from pprint import pprint
from createDB import createDB
from modules.readConfig import readConfig
from modules.clear_console import clearConsole
origin_path,destination_path,_,database,_,_,_ = readConfig()
ignoreList = ['Thumbs.db']
def returnFiles(path):
    original_wd = os.getcwd()
    os.chdir(path)
    files = os.listdir()
    for i in files:
        currentPath = os.path.abspath(i) #Get the path of the current file
        if i in ignoreList: #Skip it if it is in the ignore list
            continue
        if os.path.isdir(i): #If it is a dir call this func on it
            returnFiles(currentPath)
        else:                                   #If none of the above then move file back to origin_path
            newPath = os.path.join(origin_path,i)
            os.rename(currentPath, newPath)
    os.chdir(original_wd)

def createCollison(file):
    copyPath = file[:-4] + ' - Copy.mp4'
    shutil.copy2(file, copyPath)


while True:
    print('''
    a) Return files
    b) Create collision file
    c) Reset database
    x) Exit
    ''')
    inp = input()
    clearConsole()
    if inp == 'a':
        returnFiles(destination_path)
        print('Test files returned to data folder')
        
    elif inp == 'b':
        # print(os.listdir('data'))
        collisionFile = os.path.join(os.getcwd(),'data',os.listdir('data')[2])
        createCollison(collisionFile)
    elif inp == "c":
        os.remove(database)
        createDB()
    elif inp == 'x':
        break
    else:
        continue
