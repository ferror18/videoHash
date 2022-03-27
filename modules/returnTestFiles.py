import os,shutil
from readConfig import readConfig
from clear_console import clearConsole
origin_path,destination_path,collision_path,mode,database = readConfig()

def returnFiles(path):
    original_wd = os.getcwd()
    os.chdir(path)
    files = os.listdir()
    for i in files:
        # print('i: ',i)
        currentPath = os.path.abspath(i)
        if i == 'Thumbs.db':
            os.remove(i)
            continue
        if os.path.isdir(i):
            # print('Folder : ', i)
            # print(currentPath)
            returnFiles(currentPath)
        else:
            newPath = os.path.join(origin_path,i)
            # print(currentPath, '\n',newPath)
            os.rename(currentPath, newPath)
    
    os.chdir(original_wd)



def createCollison(file):
    copyPath = file[:-4] + ' - Copy.mp4'
    shutil.copy2(file, copyPath)


while True:
    print('''
    a) Return files
    b) Create collision file
    c) Exit
    ''')
    inp = input()
    clearConsole()
    if inp == 'a':
        returnFiles(destination_path)
    elif inp == 'b':
        # print(os.listdir('data'))
        collisionFile = os.path.join(os.getcwd(),'data',os.listdir('data')[2])
        createCollison(collisionFile)
    elif inp == 'c':
        break
    else:
        continue
