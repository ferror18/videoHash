import os
def readConfig(fileName='config.txt'):
    # Config logic
    path = os.path.join(os.getcwd(),fileName)
    conFile = open(path, "r") #Open config File
    conFile = conFile.readlines() # Split into an array of lines
    conFile = [i for i in conFile if i != '\n' and i[0] != '#' ] # remove new line above and comments
    conFile = [i.replace('\n','') for i in conFile] # remove new lines 
    conFile = [i.split('=') for i in conFile] # Split pair into 
    result = [None] * len(conFile)
    myMap = {
        'origin_path': 0,
        'destination_path':1,
        'collision_path':2,
        'database':3,
        'mode':4
    }
    for i in conFile:
        result[myMap[i[0]]] = i[1]
    return result
    # origin_path,destination_path,collision_path,mode,database = readConfig()
# print(readConfig('C:/Users/murad/Desktop/videoHash/config.txt'))
