def checkIfEpisode(name):
    if len(name) < 9:
        return False
    a = name[0] == '['
    b = name[1] == 'S'
    c = name[6] == 'E'
    d = name[8] == ']'

    return a and b and c and d


def nameGenerator(fileMap, databaseFiles, yearTkr, mode):

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
        if checkIfEpisode(workObj['fileName']):
            workObj['fileName'] = workObj['fileName'][9:]
            # print(workObj['fileName'])
        if mode[1] == 'r':
            workObj['new_name'] = f"[S{year}E{episode}]{key}.{ext}" if mode[0] == 'e' else f"{key}.{ext}"
        else:
            workObj['new_name'] = f"[S{year}E{episode}]{workObj['fileName']}" if mode[0] == 'e' else workObj['fileName']