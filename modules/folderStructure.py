from calendar import month
import os

def generateFolderStructure(destination_path,yearTkr,fileMap,insertOne, mode):
    #Checking existing folders
    print('\n\n\t Creating per year Folder Structure')
    existingDirs = {}
    dirs = os.listdir(destination_path) #List all files in destination path
    dirs = list(filter(lambda j: os.path.isdir(os.path.join(destination_path,j)), dirs)) #Removes all non directories
    #Add existing directories

    for x in dirs:
        existingDirs[x] = 1
    if mode[2] == 'y':
        # Create remaining directories
        for i in yearTkr:
            if i not in existingDirs:
                os.mkdir(os.path.join(destination_path,i))
        #Moving files around
        print('\n\n\t Moving files to respective folders')
        for key in fileMap:
            workObj = fileMap[key]
            workObj['finalPath'] = os.path.join(destination_path, workObj['year'], workObj['new_name'])
            os.rename(workObj['path'], workObj['finalPath'])
    elif mode[2] == 'm':
        # Create remaining directories
        months = ['01','02','03','04','05','06','07','08','09','10','11','12']
        for i in yearTkr:
            for j in months:
                j  = f"{i} {j}"
                if j not in existingDirs:
                   os.mkdir(os.path.join(destination_path,j))
        #Moving files around
        print('\n\n\t Moving files to respective folders')
        for key in fileMap:
            workObj = fileMap[key]
            workObj['finalPath'] = os.path.join(destination_path, f"{workObj['year']} {workObj['month']}", workObj['new_name'])
            os.rename(workObj['path'], workObj['finalPath'])
    else:
        #Moving files around
        print('\n\n\t Moving files to respective folders')
        for key in fileMap:
            workObj = fileMap[key]
            workObj['finalPath'] = os.path.join(destination_path, workObj['new_name'])
            os.rename(workObj['path'], workObj['finalPath'])




    for key in fileMap:
        workObj = fileMap[key]
        #Update State
        workObj['path'] = workObj['finalPath']
        workObj['fileName'] = workObj['new_name']
        del workObj['new_name']
        # print(workObj)
    #Updating database
        insertOne(workObj)
    print('\n\n\t Updating database')
    print('\n\n\t Collection Sorted Succesfully')