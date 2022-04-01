import os

def organizeCollisions(allHashes, CollP):
    print('\n\n\t++ Please resolve collisions before continuing ++ ')
    for key in allHashes:
        collisionArray = allHashes[key]
        if len(collisionArray) == 1: # Loop trough all hashes but avoid the ones with out collition
            continue

        #Create collision Folder
        unsolved_collision_folder = os.path.join(CollP, key)
        os.mkdir(unsolved_collision_folder)

        #Move collision files into collision folder
        for x in collisionArray:
            x['unsolved_collision_path'] = os.path.join(unsolved_collision_folder, x['fileName'])
            os.rename(x['path'], x['unsolved_collision_path'])