
def mapHasher(fileMap ,vidExts, video_hash, photo_hash, hashTrk):
    totalFiles = 0
    Unresolved_Collisions = False
    for key in fileMap:
        workObj = fileMap[key]
        ext = workObj['ext']
        isVid = True if ext in vidExts else False
        hashof = video_hash if isVid else photo_hash
        hs = hashof(workObj['path'])
        workObj['hash'] = hs
        totalFiles+=1
        progress = round(totalFiles/(len(fileMap))*100)
        print(f"Progress:{progress}%\t {len(fileMap)-totalFiles} remaining\t{workObj['fileName']}")
        #Check hash traker for collision
        if hs in hashTrk:
            print('+++++ COLLISION ++++++++', hs)
            #Add it to collison tracker
            Unresolved_Collisions = True
            hashTrk[hs] = [workObj,*hashTrk[hs]]
            #Remove both from file map
        else:
            hashTrk[hs] = [fileMap[key]]
    return Unresolved_Collisions