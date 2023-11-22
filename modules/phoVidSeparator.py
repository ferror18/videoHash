import pprint

def phoVidSeparator(Map):
    listofVidKey, listofVidPath, listofPhoKey, listofPhoPath = [],[],[],[]

    fileList = [ _[1] for _ in Map.items()] # make a list of file objects
    fileListVid = list(filter(lambda obj: obj['isVid'], fileList))
    fileListPho = list(filter(lambda obj: obj['isPho'], fileList))
    listofVidKey = [ _['id'] for _ in fileListVid] # get a list of IDs 
    listofVidPath = [ _['path'] for _ in fileListVid] # get a list of paths
    listofPhoKey = [ _['id'] for _ in fileListPho] # get a list of IDs 
    listofPhoPath = [ _['path'] for _ in fileListPho] # get a list of paths
    return listofVidKey, listofVidPath, listofPhoKey, listofPhoPath