
def nameGenerator(fileMap, databaseFiles, yearTkr):

    #Year and episode number
    for key in databaseFiles:
        workObj = databaseFiles[key]
        #Episode number
        year = workObj['year']
        if year not in yearTkr:
            episode = 1
            yearTkr[year] = 1
        else:
            yearTkr[year]+=1

    print('\n\n\t Orgainizing by year')
    for key in fileMap:
        workObj = fileMap[key]
        #Episode number
        year = workObj['year']
        if year not in yearTkr:
            episode = 1
            yearTkr[year] = 1
        else:
            yearTkr[year]+=1
        episode = yearTkr[year]
        ext = workObj['ext']
        workObj['episode'] = episode
        workObj['new_name'] = f"[S{year}E{episode}]{key}.{ext}"