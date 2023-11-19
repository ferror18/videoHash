from pprint import pprint

def nameGenerator(fileMap, yearTkr):

    for key in fileMap:
        year = fileMap[key]['year']
        if year not in yearTkr:
            yearTkr[year] = 1
        else:
            yearTkr[year]+=1
    for key in fileMap:
        workObj = fileMap[key]
        unique = key.replace('-','')
        creationDate = workObj['creation_date'][0:10]
        extension = workObj['ext']
        newName = f"{creationDate}-{unique}.{extension}"
        workObj['new_name'] = newName