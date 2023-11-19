from calendar import month
import os

def generateFolderStructure(destination_path,yearTkr,fileMap):
    #Checking existing folders
    print('\n\n\t Creating per year Folder Structure')
    existingDirs = {}
    dirs = os.listdir(destination_path) #List all files in destination path
    dirs = list(filter(lambda j: os.path.isdir(os.path.join(destination_path,j)), dirs)) #Removes all non directories
    #Add existing directories

    for x in dirs:
        existingDirs[x] = 1
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
    print('\n\n\t Collection Sorted Succesfully')